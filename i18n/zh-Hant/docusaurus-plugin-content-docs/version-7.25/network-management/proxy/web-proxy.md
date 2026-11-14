---
sidebar_key: "network-management/proxy/web-proxy"
sidebar_position: 1
title: "Web 代理"
sidebar_label: "Web 代理"
description: "RouterOS Web 代理為網路中的用戶端獲取 Web 內容。它按主機名、路徑和方法過濾請求，快取純 HTTP 內容，透過父代理傳送請求，並可作為常規代理或透明代理工作。"
tags:
  - 'proxy'
  - 'firewall'
  - 'caching'
source: https://manual.mikrotik.com/docs/7.25/network-management/proxy/web-proxy
captured_at: '2026-11-04T11:21:20+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

**子選單：** `/ip/proxy`

Web 代理接受來自你網路中用戶端的 Web 請求，併為其從伺服器獲取內容。可用於：

- 按用戶端、主機名、路徑或 HTTP 方法允許、拒絕或重定向請求。
- 在路由器上快取純 HTTP 內容，可快取在 RAM 或磁碟中。
- 透過另一個代理（父代理）傳送請求。

用戶端透過以下兩種方式之一使用代理。常規代理用戶端（例如配置了代理設定的瀏覽器）會將其所有 Web 請求（HTTP 和 HTTPS）傳送給代理。在透明模式下，防火牆規則會把用戶端的純 HTTP 連線重定向到代理，用戶端無需任何設定。

HTTPS 內容在用戶端和伺服器之間加密，因此代理僅對其進行中繼。路由器可以按主機名、地址和埠允許或拒絕 HTTPS 連線，但無法看到請求路徑或快取內容，並且無法在透明模式下接受 HTTPS 連線。按路徑過濾和快取僅適用於純 HTTP。

Web 代理預設處於停用狀態。它在 `home` 和 `basic` [裝置模式](../../system-information-and-utilities/device-mode.md) 中不可用。

## 設定常規代理 {#set-up-a-regular-proxy}

啟用代理：

```ros
/ip/proxy/set enabled=yes
```

代理會監聽路由器所有 IPv4 和 IPv6 地址上的 TCP 埠 8080。要使用其他埠，請設定 `port`，例如 `port=8080,3128`。

在瀏覽器或作業系統的代理設定中，輸入路由器的地址（例如 `192.168.88.1`）和埠 8080，分別用於 HTTP 和 HTTPS。要從安裝了 curl 的計算機測試代理：

```bash
curl -x http://192.168.88.1:8080 -I http://example.com/
```

### 僅允許你的用戶端 {#allow-only-your-clients}

任何人都能訪問的代理是開放代理：其他人可以透過它傳送流量並隱藏其來源。預設防火牆配置會丟棄不是來自 LAN 的到路由器的連線，這也會保護代理。如果你的防火牆接受來自其他網路的連線，請丟棄不是來自 LAN 的代理連線（適用於 IPv4 和 IPv6）：

```ros
/ip/firewall/filter/add chain=input protocol=tcp dst-port=8080 in-interface-list=!LAN action=drop comment="web proxy: LAN only"
/ipv6/firewall/filter/add chain=input protocol=tcp dst-port=8080 in-interface-list=!LAN action=drop comment="web proxy: LAN only"
```

將這些規則移到任何接受這些連線的規則之前。

代理會向任意埠開啟 HTTPS 隧道（`CONNECT` 方法）。要僅允許到 HTTPS 埠 443 的隧道：

```ros
/ip/proxy/access/add method=CONNECT dst-port=!443 action=deny
```

## 設定透明代理 {#set-up-a-transparent-proxy}

在透明模式下，目標 NAT 規則會把用戶端的 HTTP 連線重定向到代理埠，用戶端無需代理設定：

```ros
/ip/proxy/set enabled=yes
/ip/firewall/nat/add chain=dstnat protocol=tcp dst-port=80 in-interface-list=LAN action=redirect to-ports=8080 comment="transparent web proxy"
```

代理連線的是請求中指定的主機（`Host` 標頭），而不是用戶端所連線的地址。

透明模式僅適用於純 HTTP。不要將 HTTPS（埠 443）重定向到代理：代理不接受 TLS 連線，重定向後的 HTTPS 連線會失敗。

同一個代理可同時為常規用戶端和透明用戶端提供服務。

## 檢查與故障排除 {#check-and-troubleshoot}

`/ip/proxy/monitor` 顯示代理是否執行、其開啟的連線，以及它從快取中回答了多少請求（`hits`）：

```ros
[admin@MikroTik] > /ip/proxy/monitor once
                 status: running
                 uptime: 35s
     client-connections: 0
     server-connections: 5
               requests: 313
                   hits: 69
             cache-used: 0KiB
         total-ram-used: 0KiB
  received-from-servers: 10090KiB
        sent-to-clients: 12126KiB
   hits-sent-to-clients: 1920KiB
```

`/ip/proxy/connections/print` 列出開啟的連線：`C` 表示來自用戶端的連線，`S` 表示到伺服器的連線。

要記錄每個請求，請為 `web-proxy` 主題新增日誌規則：

```ros
/system/logging/add topics=web-proxy,!debug
```

每個請求都會記錄用戶端地址、方法、URL、訪問列表的動作，以及代理是否從快取中回答：

```text
web-proxy,account 192.168.88.10 GET http://example.com/  action=allow cache=MISS
web-proxy,account 192.168.88.10 CONNECT example.com:443  action=allow cache=MISS
```

如果不使用 `!debug`，日誌還會顯示每個請求和響應的標頭。

常見問題：

- 瀏覽器顯示 `ERROR: Forbidden` 和 `Access Denied`：匹配到了 `action=deny` 的訪問規則。`/ip/proxy/access/print` 的 `hits` 列顯示是哪條規則。
- HTTPS 站點在透明模式下無法開啟：透明模式僅適用於 HTTP。只重定向埠 80。
- `ERROR: Gateway Timeout`：代理無法連線到伺服器或父代理。頁面會顯示原因，例如 `Operation timed out`。
- 快取沒有回答任何內容：大多數站點使用 HTTPS，代理無法快取這些內容，而且許多 HTTP 響應不可快取。相關條件在快取部分列出。

## 過濾請求 {#filter-requests}

訪問列表 `/ip/proxy/access` 決定代理服務哪些請求。路由器從上到下檢查規則，第一條匹配的規則起決定作用。不匹配任何規則的請求會被允許。規則在其所有匹配條件都匹配時匹配，而沒有匹配條件的規則會匹配每個請求。

主機名和路徑的匹配方式如下：

- 值必須匹配整個主機名或路徑。`dst-host=example.com` 不匹配 `www.example.com`。
- `*` 匹配任意數量的字元，`?` 匹配一個字元。`dst-host=*.example.com` 匹配 `example.com` 中的所有主機，但不匹配 `example.com` 本身。
- 主機名匹配不區分大小寫。
- `path` 以 `/` 開頭幷包含查詢字串。`path=*.mp3` 匹配 `/music/song.mp3`，但不匹配 `/music/song.mp3?id=1`。
- 以 `:` 開頭的值是正則表示式，它會匹配值的任意部分：`dst-host=:ads` 匹配包含 `ads` 的每個主機名。使用 `^` 和 `$` 匹配開頭和結尾。
- HTTPS 請求有主機名和埠，但沒有路徑，因此 `path` 規則永遠不會匹配它們。

拒絕某個站點及其所有子域：

```ros
/ip/proxy/access
add dst-host=example.com action=deny
add dst-host=*.example.com action=deny
```

拒絕下載某些檔案型別：

```ros
/ip/proxy/access
add path=*.exe action=deny
add path=*.zip action=deny
```

僅針對一個網路拒絕某個站點：

```ros
/ip/proxy/access/add src-address=192.168.88.0/24 dst-host=*.example.net action=deny
```

僅允許某些站點，並拒絕所有其他站點：

```ros
/ip/proxy/access
add dst-host=*.example.com action=allow
add action=deny
```

代理可以重定向瀏覽器到另一個頁面，而不是拒絕請求。用戶端會收到指向 `action-data` 中 URL 的 HTTP 307 重定向：

```ros
/ip/proxy/access/add dst-host=*.example.net action=redirect action-data=http://intranet.example.com/blocked.html
```

### 錯誤頁面 {#error-page}

代理會用錯誤頁面（HTTP 403）響應被拒絕的請求，該頁面將 `cache-administrator` 列為聯絡人，並且對其他錯誤也使用同一頁面。要更改頁面，請將預設模板寫入路由器的檔案：

```ros
/ip/proxy/reset-html
```

這會建立 `webproxy/error.html`。編輯該檔案或用你自己的 HTML 替換它，代理會立即使用新頁面。模板可以使用以下變數：

- `$(status)` - HTTP 狀態，例如 `Forbidden`。
- `$(url)` - 請求的 URL。
- `$(error)` - 原因，例如 `Access Denied`。
- `$(admin)` - `cache-administrator` 的值。
- `$(signature)` - 包含時間和代理地址的一行。

`/ip/proxy/reset-html` 恢復預設頁面。

## 快取 {#cache}

代理會儲存其獲取的純 HTTP 內容，並將其傳送給下一個請求相同 URL 的用戶端，而無需再次從伺服器獲取。代理執行時快取預設開啟，且位於 RAM 中。

![Without a cached copy, the proxy fetches the file from the web server and sends it to the user; with a cached copy, it answers the user from the cache](/img/0a86ba2a141c09fa.webp)

當以下所有條件都成立時，代理會儲存響應：

- 請求使用 `GET` 方法，並且響應狀態為 200 (OK) 或 301 (Moved Permanently)。其他響應（例如 302 重定向和 404 錯誤）不會被儲存。
- 響應具有 `Last-Modified` 或 `ETag` 標頭，並且沒有 `Expires` 標頭。
- 響應未標記為 `Cache-Control: no-store` 或 `Cache-Control: private`。
- 響應不大於 `max-cache-object-size`（預設 2048 KiB）。
- `/ip/proxy/cache` 中沒有 `deny` 規則匹配該請求。

當儲存的物件具有 `Last-Modified` 標頭且其 URL 沒有查詢字串（`?`）時，代理會直接從快取回答，而不詢問伺服器。對於其他儲存的物件，它會在每次請求時詢問伺服器物件是否已更改。

大多數 Web 內容透過 HTTPS 傳送，其餘內容中也有許多是為每個請求動態生成的，因此快取能夠回答的流量佔比通常很小。

來自快取的響應具有 `X-Cache: HIT` 標頭。路由器還會用 DSCP 4（`cache-hit-dscp`）標記其封包，因此你可以在防火牆和佇列規則中匹配它們。代理不儲存 `Set-Cookie` 標頭，因此用戶端永遠不會獲得另一個用戶端的 Cookie。

### 快取大小與儲存 {#cache-size-and-storage}

使用預設值 `max-cache-size=unlimited` 時，RAM 快取可以使用路由器的大部分空閒記憶體。在執行其他服務的路由器上，請以 KiB 為單位設定限制，例如 64 MiB：

```ros
/ip/proxy/set max-cache-size=65536
```

要將快取儲存在磁碟上，請設定 `cache-on-disk=yes` 以及磁碟上的路徑，例如 USB 磁碟 `usb1` 上：

```ros
/ip/proxy/set cache-on-disk=yes cache-path=usb1/web-proxy
```

快取會作為 `web-proxy store` 儲存在 `/file` 中。設定快取路徑時，不存在的路徑中的目錄會自動建立，包括任何中間目錄：

```ros
[admin@MikroTik] >  /ip/proxy/set cache-path=usb1/cache-n-db/proxy/
```

```ros
[admin@MikroTik] >  /file/print
 # NAME                                              TYPE                             SIZE CREATION-TIME
 0 skins                                             directory                             2015-03-02 18:56:23
 1 sys-note.txt                                      .txt file                        23   2015-07-03 11:40:48
 2 usb1                                             disk                                  2015-07-03 11:35:05
 3 usb1/lost+found                                  directory                             2015-07-03 11:34:56
 4 usb1/cache-n-db                                  directory                             2015-07-03 11:41:54
 5 usb1/cache-n-db/proxy                            web-proxy store                       2015-07-03 11:42:09
```

要僅將代理用於過濾，請使用 `max-cache-size=none` 關閉快取。

更改任何代理設定都會清空快取。要自行清空快取，請執行 `/ip/proxy/clear-cache`。

### 從快取中排除站點 {#exclude-sites-from-the-cache}

快取列表 `/ip/proxy/cache` 的工作方式與訪問列表類似：第一條匹配的規則起決定作用，`action=deny` 會阻止代理儲存響應。不匹配任何規則的請求會被快取。例如，要永不快取某個站點的頁面：

```ros
/ip/proxy/cache/add dst-host=*.example.com action=deny
```

### 檢視快取內容 {#see-what-is-in-the-cache}

`/ip/proxy/cache-contents/print` 列出儲存的物件及其 URL 和大小。刪除某個條目以使代理重新獲取它。`/ip/proxy/lookups` 和 `/ip/proxy/inserts` 中的計數器顯示快取回答了多少請求以及儲存了多少物件。

## 父代理 {#parent-proxy}

要透過另一個代理傳送請求，請設定其地址和埠：

```ros
/ip/proxy/set parent-proxy=192.0.2.10 parent-proxy-port=3128
```

隨後所有請求（HTTP 和 HTTPS）都會經過父代理。當無法連線到父代理時，用戶端會收到錯誤頁面：代理不會自行連線到伺服器。

直接列表 `/ip/proxy/direct` 指定不經過父代理而直接發往伺服器的請求。第一條匹配的規則起決定作用：`action=allow` 將請求直接傳送到伺服器，`action=deny` 則透過父代理傳送。不匹配任何規則的請求會經過父代理。例如，要直接訪問某個域的伺服器：

```ros
/ip/proxy/direct/add dst-host=*.example.com action=allow
```

## 技術細節 {#technical-details}

### 標頭 {#headers}

代理會向其發往伺服器的請求新增以下標頭：

- `Via` - 代理，例如 `1.1 ::ffff:192.168.88.1 (Mikrotik HttpProxy)`。
- `X-Forwarded-For` - 用戶端地址。路徑上的每個代理都會將其用戶端新增到列表中。
- `X-Proxy-ID` - 代理的識別符號。

使用 `anonymous=yes` 時，代理不會新增其中任何一個，因此伺服器無法獲知用戶端地址。

來自快取的響應會獲得 `X-Cache: HIT` 標頭。代理已向伺服器檢查過的儲存物件會獲得 `X-Cache-Lookup: HIT`。

### HTTP 方法 {#http-methods}

訪問、快取和直接列表的 `method` 匹配條件採用 [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110#name-methods) 中的 HTTP 方法：

| 方法 | 用途 | 在代理中 |
| :-- | :-- | :-- |
| `GET` | 獲取頁面或檔案。 | 代理唯一會快取其響應的方法。 |
| `HEAD` | 僅獲取頁面或檔案的標頭。 | 始終傳送到伺服器。 |
| `POST` | 將資料（例如表單）傳送到伺服器。 | 始終傳送到伺服器。 |
| `PUT`、`DELETE` | 在伺服器上儲存或刪除檔案。 | 傳送到伺服器。 |
| `OPTIONS`、`TRACE` | 詢問伺服器支援哪些方法，或回顯請求。 | 傳送到伺服器。 |
| `CONNECT` | 透過代理開啟隧道，用於 HTTPS。 | 代理會中繼該隧道。規則可以匹配其主機名、地址和埠，但不能匹配路徑。 |

### FTP {#ftp}

常規代理用戶端還可以請求 `ftp://` URL。代理會從 FTP 伺服器獲取它們，並以 HTML 頁面形式返回目錄列表。

### 連線限制 {#connection-limits}

`max-client-connections` 限制用戶端連線數，預設 600。達到限制時，新請求會等待，直到有連線空閒。

所有屬性都在 [`/ip/proxy`](../../cli-reference/ip/proxy/index.md) CLI 參考中描述。
