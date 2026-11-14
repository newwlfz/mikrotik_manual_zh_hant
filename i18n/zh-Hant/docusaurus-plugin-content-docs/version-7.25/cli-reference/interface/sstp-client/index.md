---
sidebar_key: "cli-reference/interface/sstp-client/index"
sidebar_position: 1
title: "sstp-client"
sidebar_label: 'sstp-client'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/sstp-client
captured_at: '2026-11-01T21:23:01+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/sstp-client {#interfacesstp-client}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">該項是否被停用。</ArgTableRow>
<ArgTableRow arg="R" typ="running">介面是否正在執行。</ArgTableRow>
<ArgTableRow arg="H" typ="hw-crypto">硬體加密是否處於活動狀態。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">介面的描述性名稱。</ArgTableRow>
<ArgTableRow arg="max-mtu" typ="num">最大傳輸單元。</ArgTableRow>
<ArgTableRow arg="max-mru" typ="num">最大接收單元。</ArgTableRow>
<ArgTableRow arg="mrru" typ="num">鏈路上可接收的最大封包大小。如果封包大於隧道 MTU，則會拆分為多個數據包，從而允許透過隧道傳送全尺寸 IP 或 Ethernet 封包。</ArgTableRow>
<ArgTableRow arg="connect-to" typ="address (flags=D46v)" mandatory="1">SSTP 伺服器的遠端地址。</ArgTableRow>
<ArgTableRow arg="port" typ="num">要連線的埠。</ArgTableRow>
<ArgTableRow arg="http-proxy" typ="alt { address: ipAddr
, ipv6-address: ip6Addr
, name: string
 }">代理地址。</ArgTableRow>
<ArgTableRow arg="proxy-port" typ="num">代理埠。</ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none) { none:0 }">證書儲存中的用戶端證書。</ArgTableRow>
<ArgTableRow arg="verify-server-certificate" typ="bool">根據路由器的證書儲存驗證伺服器證書。</ArgTableRow>
<ArgTableRow arg="verify-server-address-from-certificate" typ="bool">根據證書驗證伺服器地址。</ArgTableRow>
<ArgTableRow arg="user" typ="string" mandatory="1">用於身份驗證的使用者名稱。</ArgTableRow>
<ArgTableRow arg="password" typ="string">用於身份驗證的密碼。</ArgTableRow>
<ArgTableRow arg="profile" typ="enum">指定建立隧道時使用哪個 PPP 配置檔案。</ArgTableRow>
<ArgTableRow arg="keepalive-timeout" typ="enum (disabled) { disabled:0 }">Keepalive 超時時間，單位為秒。</ArgTableRow>
<ArgTableRow arg="add-default-route" typ="bool">是否將 SSTP 遠端地址新增為預設路由。</ArgTableRow>
<ArgTableRow arg="default-route-distance" typ="num">啟用 add-default-route 時，應用於自動建立的預設路由的距離值。</ArgTableRow>
<ArgTableRow arg="dial-on-demand" typ="bool">僅在生成出站流量時才連線。如果啟用，則在連線尚未建立時，會新增一條閘道器地址來自 10.112.112.0/24 網路的路由。</ArgTableRow>
<ArgTableRow arg="authentication" typ="ubit (pap, chap, mschap1, mschap2)">允許的身份驗證方法。預設允許所有方法。</ArgTableRow>
<ArgTableRow arg="pfs" typ="enum (no | yes | required) { no:0, yes:1, required:2 }">指定要使用哪種 TLS 身份驗證。`yes` - TLS 使用 ECDHE-RSA 和 DHE-RSA。`required` - 僅使用 ECDHE。</ArgTableRow>
<ArgTableRow arg="tls-version" typ="enum (any | only-1.2) { any:0, only-1.2:2 }">指定允許使用哪個 TLS 版本。</ArgTableRow>
<ArgTableRow arg="ciphers" typ="ubit (aes256-sha, aes256-gcm-sha384)">允許的加密套件。</ArgTableRow>
<ArgTableRow arg="add-sni" typ="bool">將 TLS SNI 擴充套件新增到 Client Hello 封包中。從 RouterOS 7.15 版本開始可用。</ArgTableRow>
</ArgTable>
