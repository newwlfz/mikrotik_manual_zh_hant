---
sidebar_key: "system-information-and-utilities/fetch"
sidebar_position: 4
title: "獲取"
sidebar_label: "獲取"
description: "Fetch 是 RouterOS 中用於透過 HTTP、HTTPS、FTP、TFTP 和 SFTP 傳輸檔案的實用工具，支援可配置的身份驗證、壓縮、重定向和變數儲存選項。它同時支援下載/上傳模式以及 VRF 整合，以便進行定向傳輸。"
tags:
  - 'fetch'
source: https://manual.mikrotik.com/docs/7.24/system-information-and-utilities/fetch
captured_at: '2026-11-04T11:33:26+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Fetch 是 RouterOS 控制檯實用程式，用於複製檔案並執行基於 HTTP 的請求。它支援 HTTP、HTTPS、FTP、TFTP 和 SFTP，允許上傳、下載，以及對遠端伺服器執行任意 GET 或 POST 操作。

## 屬性 {#properties}

| 屬性 | 描述 |
| :-- | :-- |
| **address** (*string*; 預設： ) | 目標裝置的 IP 地址。在特定 VRF 中執行 fetch 操作時，追加 `@vrf_name`；或者在使用 <code>url</code> 引數時省略 address，僅提供 VRF |
| **as-value** (*set \| not-set*; 預設：**not-set**) | 設定後，將 fetch 結果儲存到變數中（需要 `output` 引數） |
| **ascii** (*yes \| no*; 預設：**no**) | 為 FTP/TFTP 傳輸啟用 ASCII 模式 |
| **certificate**(*string*; 預設： ) | [證書儲存中的證書](../authentication-authorization-accounting/certificates.md)，在 HTTPS 模式下用於伺服器驗證，僅在啟用 <code>check-certificate</code> 時適用 |
| **check-certificate** (*yes \| yes-without-crl \| no*; 預設：**no**) | 啟用針對路由器本地證書儲存的信任鏈驗證。`yes-without-crl` 會驗證證書但跳過 CRL 檢查。僅限 HTTPS |
| **dst-path** (*string*; 預設： ) | 獲取的檔案將儲存到的目標路徑 |
| **duration** (*time;* 預設： ) | fetch 操作的最大執行時間 |
| **host** (*string*; 預設： ) | 遠端 Web 伺服器的主機名或虛擬主機名。當同一 IP 為多個虛擬主機提供服務時很有用。例如，`address=manual.mikrotik.com host=forum.mikrotik.com` |
| **http-auth-scheme** (*basic\|digest*; 預設：**basic**) | HTTP 認證方案 |
| **http-method** (*delete\|get\|head\|post\|put\|patch*; 預設：**get**) | HTTP 方法 |
| **http-data** (*string*; 預設： ) | 要傳輸的資料。最大資料限制為 64 Kb |
| **http-header-field** (*string*; 預設：**\*empty\***) | 所有標頭欄位和值的列表，形式為 `http-header-field="h1:fff,h2:yyy"` 或 `http-header-field="h:fff\\,yyy"`（在單個標頭內，多個值需要使用兩個反斜槓進行“轉義”）。 |
| **http-content-encoding** (*deflate\|gzip*; 預設：\***empty\***) | 使用 **gzip** 或 **deflate** 壓縮對有效載荷進行編碼，並新增相應的 `Content-Encoding` 標頭。僅適用於 POST 和 PUT 方法 |
| **http-max-redirect-count** (*integer*; 預設：2) | fetch 將自動跟隨的 HTTP 重定向最大數量 |
| **http-percent-encoding**(*yes \| no*; 預設：**no**) | 啟用請求路徑的 URL 百分號編碼 |
| **http-version** (*http1\_1* \| *http2*; 預設：**http1\_1**) | 選擇 HTTP 協定版本。HTTP2 僅在 ARM64 和 x86/CHR 裝置上受支援 |
| **idle-timeout** (*time;* 預設：10s) | 自上次讀/寫操作以來的空閒超時 |
| **ip-type** (*any \| ipv4 \| ipv6;* 預設：**any**) | 指定在處理域名時優先使用哪個 IP 地址族 |
| **keep-result** (*yes \| no*; 預設：**yes**) | 啟用後，獲取的資料會寫入檔案 |
| **mode** (*ftp\|http\|https\|sftp\|tftp*; 預設：**http**) | 用於連線的協定。優先透過 `url` 引數指定協定（例如，`url=sftp://ip_address/path` |
| **output** (*none\|file\|user\|user-with-headers*; 預設：**file**) | 確定獲取的資料儲存在哪裡：`none` - 不儲存下載的資料<code>file</code> - 將下載的資料儲存到檔案中`user` - 將下載的資料儲存到 data 變數中（變數限制為 64Kb）`user-with-headers` - 將下載的資料和標頭儲存到 data 變數中（變數限制為 64Kb - 下載資料 20Kb，標頭 44Kb） |
| **password** (*string*; 預設：**anonymous**) | 用於在遠端裝置上進行認證的密碼 |
| **port** (*integer*; 預設： ) | 用於連線的埠 |
| **src-address** (ip address; 預設： ) | 用於建立連線的源 IP 地址，僅適用於 HTTP/S 和 SFTP 模式 |
| **src-path** (*string*; 預設： ) | 遠端檔案的路徑 |
| **upload** (*yes \| no*; 預設：**no**) | 為 FTP/SFTP 傳輸啟用上傳模式，需要 `src-path` 和 `dst-path` |
| **url** (*string*; 預設： ) | 資源的完整 URL；可以替代單獨的 `address` 和 `src-path` 引數 |
| **user** (*string*; 預設：**anonymous**) | 用於在遠端裝置上進行認證的使用者名稱 |

## 配置示例 {#configuration-examples}

以下示例展示如何透過 FTP 協定從 IP 地址為 192.168.88.2 的裝置複製檔名為 "conf.rsc" 的檔案，並將其儲存為檔名為 "123.rsc" 的檔案。登入該裝置需要使用者名稱和密碼。

```ros
[admin@MikroTik] /tool> fetch address=192.168.88.2 src-path=conf.rsc user=admin mode=ftp password=123 dst-path=123.rsc port=21 host="" keep-result=yes
```

將檔案上傳到另一臺路由器的示例：

```ros
[admin@MikroTik] /tool> fetch address=192.168.88.2 src-path=conf.rsc user=admin mode=ftp password=123 dst-path=123.rsc upload=yes
```

另一個檔案下載示例，演示 url 屬性的用法。

```ros
[admin@MikroTik] /> /tool/fetch url="https://www.mikrotik.com/img/netaddresses2.pdf" mode=http
  status: finished

[admin@test_host] /> /file/print
 # NAME                     TYPE                  SIZE                 CREATION-TIME
 ...
 5 netaddresses2.pdf        .pdf file             11547                2010-06-01 11:59:51
```

可以透過在 “@” 符號後附加 VRF 名稱，讓 /tool fetch 透過特定 VRF 執行：

* 在 URL 中 – ```url="http://192.168.88.2@vrf1/…"```（適用於 HTTP/HTTPS，不適用於 SFTP）。
* 在 address 屬性中 – ```address=192.168.88.2@vrf1```
* 作為單獨的 address 引數 –  ```address=@vrf1```，與提供 IP 的 URL 結合使用。

address 屬性可以與 VRF 組合並用 "@" 分隔（`address=192.168.88.2@vrf1`），或者僅作為 address 引數，在 VRF 名稱前帶有 “@” 符號，如示例所示（使用 URL 中的地址，並將其與 address 引數中的 VRF 名稱組合）：

```ros
[admin@MikroTik] /> /tool/fetch url="sftp://192.168.88.2" address=@test src-path=test.txt user=admin password="" upload=yes

  status: finished
```

### 向遠端主機發送資訊 {#sending-information-to-a-remote-host}

可以使用 HTTP POST 請求向已準備好接收資訊的遠端伺服器傳送資訊。在以下示例中，我們將地理座標傳送到 PHP 頁面：

```ros
/tool/fetch http-method=post http-header-field="Content-Type:application/json" http-data="{\"lat\":\"56.12\",\"lon\":\"25.12\"}" url="https://testserver.lv/index.php"    
```

在此示例中，資料以檔案形式上傳。重要說明：由於變數資料來自檔案，檔案大小最多隻能為 4KB。這是 RouterOS 變數的限制。

```ros
/export file=export.rsc

:global data [/file/get [/file/find name=export.rsc] contents];
:global url "https://prod-51.westeurope.logic.azure.com:443/workflows/blabla/triggers/manual/paths/invoke....";

/tool/fetch mode=https http-method=put http-data=$data url=$url
```

### 將返回值儲存到變數 {#return-value-to-a-variable}

可以將 fetch 命令的結果儲存到變數中。

#### 示例 1 {#example-1}

可以根據 HTTP 頁面返回的結果觸發特定操作。下面是一個非常簡單的示例，每當 PHP 頁面返回 "0" 時，就會停用 **ether2**：

```ros
{
    :local result [/tool/fetch url=https://10.0.0.1/disable_ether2.php as-value output=user];
    :if ($result->"status" = "finished") do={
        :if ($result->"data" = "0") do={
            /interface/ethernet/set ether2 disabled=yes;
        } else={
            /interface/ethernet/set ether2 disabled=no;
        }
    }
}
```

#### 示例 2 {#example-2}

如果 fetch 失敗，可以訪問錯誤程式碼（"code"）和返回的 HTTP 標頭（"http-headers"）。

```ros
:onerror err,attr in={ /tool/fetch http://127.0.0.1/error as-value} do={:put $err;:put ($attr->"code");:put ($attr->"http-headers")}
failure: Status 404, Not Found
404
Cache-Control: no-store;Connection: Keep-Alive;Content-Length: 99;Content-Type: text/html;Date: Tue, 09 Dec 2025 13:27:44 GMT;Expires: 0;Pragma: no-cache;X-Frame-Options: sameorigin 
```
