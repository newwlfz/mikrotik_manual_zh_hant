---
sidebar_key: "cli-reference/interface/ovpn-server/server/index"
sidebar_position: 2
title: "server"
sidebar_label: "server"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/ovpn-server/server
captured_at: '2026-11-01T21:27:32+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ovpn-server/server {#interfaceovpn-serverserver}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="I" typ="inactive">未啟用</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="mode" typ="enum (ip | ethernet) { ip:0, ethernet:1 }"></ArgTableRow>
<ArgTableRow arg="protocol" typ="enum (tcp | udp)"></ArgTableRow>
<ArgTableRow arg="netmask" typ="num"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="max-mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="keepalive-timeout" typ="enum (disabled) { disabled:0 }"></ArgTableRow>
<ArgTableRow arg="default-profile" typ="enum"></ArgTableRow>
<ArgTableRow arg="certificate" typ="enum"></ArgTableRow>
<ArgTableRow arg="require-client-certificate" typ="bool"></ArgTableRow>
<ArgTableRow arg="tls-version" typ="enum (any | only-1.2) { any:0, only-1.2:2 }"></ArgTableRow>
<ArgTableRow arg="auth" typ="ubit (sha1, md5, sha256, sha384, sha512, null)"></ArgTableRow>
<ArgTableRow arg="cipher" typ="ubit (blowfish128, aes128-cbc, aes192-cbc, aes256-cbc, aes128-gcm, aes192-gcm, aes256-gcm, null)"></ArgTableRow>
<ArgTableRow arg="reneg-sec" typ="num">加密金鑰重新協商間隔（0 - disabled）</ArgTableRow>
<ArgTableRow arg="redirect-gateway" typ="ubit (disabled, def1, ipv6)">向 VPN 用戶端推送 'redirect-gateway def1 ipv6' 選項</ArgTableRow>
<ArgTableRow arg="push-routes" typ="string"></ArgTableRow>
<ArgTableRow arg="push-routes-ipv6" typ="string"></ArgTableRow>
<ArgTableRow arg="enable-tun-ipv6" typ="bool">在 ovpn 隧道內啟用 ipv6</ArgTableRow>
<ArgTableRow arg="tun-server-ipv6" typ="ip6Addr">伺服器 ipv6 地址</ArgTableRow>
<ArgTableRow arg="ipv6-prefix-len" typ="num">用於隧道化 ipv6 的字首長度</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum"></ArgTableRow>
<ArgTableRow arg="user-auth-method" typ="enum (pap | mschap2) { pap:16, mschap2:2 }"></ArgTableRow>
</ArgTable>
