---
sidebar_key: "cli-reference/interface/ovpn-server/server"
title: "server"
sidebar_label: 'server'
source: https://manual.mikrotik.com/docs/cli-reference/interface/ovpn-server/server
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ovpn-server/server {#interfaceovpn-serverserver}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="I" typ="inactive">伺服器是否處於非活動狀態。</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">專案是否已停用。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">伺服器的名稱。</ArgTableRow>
<ArgTableRow arg="port" typ="num">執行伺服器的埠。</ArgTableRow>
<ArgTableRow arg="mode" typ="enum (ip | ethernet) { ip:0, ethernet:1 }">三層或二層隧道模式（也可稱為 tun、tap）。</ArgTableRow>
<ArgTableRow arg="protocol" typ="enum (tcp | udp)">與遠端端點連線時使用的傳輸協定。</ArgTableRow>
<ArgTableRow arg="netmask" typ="num">應用於用戶端的子網掩碼。</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">伺服器自動生成的 MAC 地址。</ArgTableRow>
<ArgTableRow arg="max-mtu" typ="num">最大傳輸單元。OVPN 介面在不進行封包分片的情況下可以傳送的最大封包大小。</ArgTableRow>
<ArgTableRow arg="keepalive-timeout" typ="enum (disabled) { disabled:0 }">定義時間段（以秒為單位），在該時間之後，路由器開始每秒傳送 keepalive 封包。如果在 keepalive-timeout 的兩倍時間內未收到任何流量和 keepalive 響應，則無響應的用戶端將被斷開連線。</ArgTableRow>
<ArgTableRow arg="default-profile" typ="enum">指定建立隧道時使用的 PPP 配置檔案。</ArgTableRow>
<ArgTableRow arg="certificate" typ="enum">OVPN 伺服器使用的、來自證書儲存的證書。</ArgTableRow>
<ArgTableRow arg="require-client-certificate" typ="bool">如果設定為 yes，伺服器會檢查用戶端證書是否屬於同一證書鏈。</ArgTableRow>
<ArgTableRow arg="tls-version" typ="enum (any | only-1.2) { any:0, only-1.2:2 }">指定允許哪些 TLS 版本。</ArgTableRow>
<ArgTableRow arg="auth" typ="ubit (sha1, md5, sha256, sha384, sha512, null)">伺服器接受的認證方法。</ArgTableRow>
<ArgTableRow arg="cipher" typ="ubit (blowfish128, aes128-cbc, aes192-cbc, aes256-cbc, aes128-gcm, aes192-gcm, aes256-gcm, null)">允許的加密演算法。</ArgTableRow>
<ArgTableRow arg="reneg-sec" typ="num">加密金鑰重新協商間隔（秒）。0 表示停用重新協商。</ArgTableRow>
<ArgTableRow arg="redirect-gateway" typ="ubit (disabled, def1, ipv6)">指定 OVPN 用戶端必須向路由表新增哪些路由。`def1` - 使用 0.0.0.0/1 和 128.0.0.0/1 覆蓋預設閘道器，而不是 0.0.0.0/0。`disabled` - 不推送 redirect-gateway 標誌。`ipv6` - 透過新增 2000::/4 和 3000::/4 路由，將 IPv6 路由重定向到隧道中。</ArgTableRow>
<ArgTableRow arg="push-routes" typ="string">要推送到用戶端的路由。最大輸入限制為 1400 個字元或 37 條路由。7.21 版本新增了 IPv6 支援。</ArgTableRow>
<ArgTableRow arg="push-routes-ipv6" typ="string">要推送到用戶端的 IPv6 路由。</ArgTableRow>
<ArgTableRow arg="enable-tun-ipv6" typ="bool">是否為該 OVPN 伺服器啟用 IPv6 隧道。</ArgTableRow>
<ArgTableRow arg="tun-server-ipv6" typ="ip6Addr">伺服器端生成 OVPN 介面時使用的 IPv6 字首地址。</ArgTableRow>
<ArgTableRow arg="ipv6-prefix-len" typ="num">用於隧道 IPv6 地址的字首長度。</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">用於監聽連線嘗試的 VRF。</ArgTableRow>
<ArgTableRow arg="user-auth-method" typ="enum (pap | mschap2) { pap:16, mschap2:2 }">預設使用 PAP 認證。設定為 mschap2 以使用 CHAP 質詢認證。</ArgTableRow>
</ArgTable>
