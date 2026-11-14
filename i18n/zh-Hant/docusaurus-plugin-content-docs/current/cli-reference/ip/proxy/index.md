---
sidebar_key: "cli-reference/ip/proxy"
title: "proxy"
sidebar_label: 'proxy'
source: https://manual.mikrotik.com/docs/cli-reference/ip/proxy
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/proxy {#ipproxy}
**型別：** 設定目錄

Web 代理的設定。該代理轉發其用戶端的請求（HTTP、HTTPS（`CONNECT`）和 FTP），以及透過目標 NAT 重定向到它的連線的請求，並快取 HTTP 響應。更改此選單中的任何設定都會清除快取。有關概覽和示例，請參見 [Web 代理](../../../network-management/proxy/web-proxy.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="enabled" typ="bool">Web 代理是否執行。預設：no。</ArgTableRow>
<ArgTableRow arg="src-address" typ="object { address: alt { address: ipAddr
, address6: ip6Addr
 }
 }">代理向伺服器開啟的連線的源地址。它必須是路由器的地址；否則，以及當未設定時，路由器使用由路由選擇的源地址。預設：`::`（未設定）。</ArgTableRow>
<ArgTableRow arg="port" typ="multi { port: num [1 .. 65535]
 }">代理監聽的 TCP 埠，或以逗號分隔列表形式給出的多個埠，例如 `8080,3128`。代理監聽路由器的所有 IPv4 和 IPv6 地址，因此請用防火牆規則保護該埠。要在規則中區分這些埠，請在訪問列表、快取列表和直接列表中使用 `local-port`。預設：8080。</ArgTableRow>
<ArgTableRow arg="anonymous" typ="bool">
代理是否向伺服器告知用戶端資訊。
- `no`（預設）- 將 `Via: 1.1 <router address> (Mikrotik HttpProxy)`、`X-Forwarded-For: <client address>` 和 `X-Proxy-ID` 新增到發往伺服器的請求中。當請求到達時已設定 `Via` 和 `X-Forwarded-For`，例如來自另一個代理，代理會將自己的條目新增到其中。
- `yes` - 不傳送這些標頭。
</ArgTableRow>
<ArgTableRow arg="parent-proxy" typ="alt { host: ipAddr
, host6: ip6Addr
 }">另一個代理的 IPv4 或 IPv6 地址，該代理接收請求，包括 HTTPS（`CONNECT`）請求，但 [`/ip/proxy/direct`](./direct/index.md) 直接傳送到伺服器的請求除外。僅當 `parent-proxy-port` 不為 0 時才使用父代理。當無法訪問父代理時，用戶端會收到錯誤頁面；路由器不會回退到直接連線。預設：`::`（無）。</ArgTableRow>
<ArgTableRow arg="parent-proxy-port" typ="num">父代理的 TCP 埠。為 0 時不使用父代理，即使已設定 `parent-proxy`。預設：0。</ArgTableRow>
<ArgTableRow arg="cache-administrator" typ="string">在代理的錯誤頁面上作為 `mailto:` 連結顯示的名稱或電子郵件地址，即錯誤頁面模板的 `$(admin)` 變數（參見 [`reset-html`](./reset-html.md)）。預設：webmaster。</ArgTableRow>
<ArgTableRow arg="max-cache-size" typ="alt { special: enum (none | unlimited) { none:0, unlimited:0xffffffff }
, value: num
 }">
快取的總大小上限，單位為 KiB。
- `unlimited`（預設）- 無限制。此時 RAM 快取可能會使用路由器的大部分可用記憶體，因此請在執行其他服務的路由器上設定限制。
- `none` - 不快取。
- 數字 - 以 KiB 為單位的限制。
</ArgTableRow>
<ArgTableRow arg="max-cache-object-size" typ="num">代理儲存在快取中的最大響應大小，單位為 KiB。更大的響應會直接到達用戶端而不被儲存。預設：2048KiB。</ArgTableRow>
<ArgTableRow arg="cache-on-disk" typ="bool">
代理將快取儲存在何處。
- `no`（預設）- 在 RAM 中。
- `yes` - 在路由器的儲存上，位於由 `cache-path` 命名的儲存中，`/file` 會以 `web-proxy store` 型別顯示該儲存。
</ArgTableRow>
<ArgTableRow arg="max-client-connections" typ="num">代理同時服務的用戶端連線數上限。更多請求會等待直到有連線空閒。預設：600。</ArgTableRow>
<ArgTableRow arg="max-server-connections" typ="num">預設：600。</ArgTableRow>
<ArgTableRow arg="max-fresh-time" typ="time">預設：3d。</ArgTableRow>
<ArgTableRow arg="serialize-connections" typ="bool">預設：no。</ArgTableRow>
<ArgTableRow arg="always-from-cache" typ="bool">預設：no。</ArgTableRow>
<ArgTableRow arg="cache-hit-dscp" typ="num">路由器對從快取提供的響應封包設定的 DSCP 值，範圍為 0 到 63。可在佇列和防火牆規則中用其識別快取命中。預設：4。</ArgTableRow>
<ArgTableRow arg="cache-path" typ="string">快取目錄的名稱。當 `cache-on-disk=yes` 時，路由器會在其儲存上將其建立為 `web-proxy store`。路徑（例如磁碟上的 `usb1/web-proxy`）需要對應一個已存在的目錄；否則路由器會以 `bad cache path` 拒絕它。它不能為空。預設：web-proxy。</ArgTableRow>
</ArgTable>
