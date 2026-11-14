---
sidebar_key: "cli-reference/ip/service/index"
sidebar_position: 1
title: "service"
sidebar_label: 'service'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/service
captured_at: '2026-11-01T21:24:26+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/service {#ipservice}
**型別：** 目錄

路由器的管理和服務監聽器：WinBox、SSH、Telnet、FTP、Web 伺服器（HTTP 使用 `www`，HTTPS 使用 `www-ssl`）、API（`api`、`api-ssl`）以及反向代理。每個條目設定服務接受用戶端連線的埠、地址和 VRF，以及 TLS 服務的證書。不能新增服務，只能更改和停用現有服務。列表還會顯示動態條目：其他功能和容器監聽的埠，以及到服務的已建立連線。關於 Web 伺服器部分（WebFig、REST API、圖表），請參閱 [`/ip/service/webserver`](./webserver.md)。有關概述和 RouterOS 使用的埠列表，請參閱 [服務](../../../system-information-and-utilities/services.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="D" typ="dynamic">由 RouterOS 建立的動態條目：其他功能或容器監聽的埠（例如 `btest`、`discover`、`resolver`、`dhcp`、`upnp`），或者與 `c` 標誌一起，表示到服務的已建立連線。</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">服務已停用，不在其埠上監聽。</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">服務無法使用其設定執行，例如因為另一個服務已使用該埠。原因以註釋形式顯示，例如 `cannot bind to port 80: Address in use (12)`。</ArgTableRow>
<ArgTableRow arg="c" typ="connection">該條目是到服務的已建立連線。`local` 和 `remote` 顯示連線的地址。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="port" typ="num">服務監聽的 TCP 埠，`1..65535`。當另一個服務已在該埠上監聽時，該條目會變為無效（`I`）。預設值取決於服務：`ftp` 21、`ssh` 22、`telnet` 23、`www` 80、`www-ssl` 443、`winbox` 8291、`api` 8728、`api-ssl` 8729、`reverse-proxy` 443。</ArgTableRow>
<ArgTableRow arg="address" typ="object { address: alt { address: ipPrefix
, address: ip6Prefix
 }
 }" deprecated="1">`available-from` 的已棄用名稱。使用 `address` 設定的值會寫入 `available-from`。</ArgTableRow>
<ArgTableRow arg="available-from" typ="object { address: alt { address: ipPrefix
, address: ip6Prefix
 }
 }">允許使用該服務的用戶端的 IPv4 和 IPv6 字首。來自其他地址的用戶端仍可開啟 TCP 連線，隨後路由器會在不服務該用戶端的情況下關閉連線，因此埠仍然可見。要從未信任網路隱藏服務，還應在防火牆 input 鏈中丟棄流量。空表示任意地址。預設值：空。</ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none) { none:0 }">服務向 TLS 用戶端出示的證書。適用於 `www-ssl`、`api-ssl` 和 `reverse-proxy`。使用 `none` 時，`www-ssl` 和 `api-ssl` 僅接受匿名 Diffie-Hellman 密碼套件：連線會加密，但路由器不證明其身份，並且瀏覽器和 cURL 等工具無法連線。為 HTTPS 設定證書。對於 `reverse-proxy`，該證書由自身沒有證書的規則使用（參見 [`/ip/reverse-proxy`](../reverse-proxy.md)）。預設值：none。</ArgTableRow>
<ArgTableRow arg="tls-version" typ="enum (any | only-1.2) { any:0, only-1.2:2 }">
服務接受的 TLS 版本。適用於 TLS 服務。
- `any`（預設）- TLS 1.0、1.1 和 1.2。
- `only-1.2` - 僅 TLS 1.2。
</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">服務監聽的 VRF。預設值：main。</ArgTableRow>
<ArgTableRow arg="max-sessions" typ="num">服務的最大同時會話數，`1..1000`。預設值：20。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="container" typ="enum () { :0 }">監聽該埠的容器名稱，適用於由容器建立的動態條目。</ArgTableRow>
<ArgTableRow arg="netns" typ="num">監聽該埠的容器的網路名稱空間編號，適用於由容器建立的動態條目。</ArgTableRow>
<ArgTableRow arg="name" typ="string">服務名稱。對於動態條目，為監聽該埠或持有連線的功能或程式。</ArgTableRow>
<ArgTableRow arg="proto" typ="enum ()">埠的傳輸協定：`tcp` 或 `udp`。</ArgTableRow>
<ArgTableRow arg="local" typ="ip6Addr">已建立連線的路由器地址（帶有 `c` 標誌的條目）。</ArgTableRow>
<ArgTableRow arg="remote" typ="composite { ip: ip6Addr
, port: num
 }">已建立連線的用戶端地址和埠（帶有 `c` 標誌的條目）。</ArgTableRow>
</ArgTable>
