---
sidebar_key: "cli-reference/interface/ovpn-client/index"
sidebar_position: 2
title: "ovpn-client"
sidebar_label: "ovpn-client"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/ovpn-client
captured_at: '2026-11-01T21:27:30+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ovpn-client {#interfaceovpn-client}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
<ArgTableRow arg="H" typ="hw-crypto">hw-crypto</ArgTableRow>
<ArgTableRow arg="Ta" typ="tls-auth">tls-auth</ArgTableRow>
<ArgTableRow arg="Tc" typ="tls-crypt">tls-crypt</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="max-mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="connect-to" typ="address (flags=D46v)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="mode" typ="enum (ip | ethernet) { ip:0, ethernet:1 }"></ArgTableRow>
<ArgTableRow arg="protocol" typ="enum (tcp | udp)"></ArgTableRow>
<ArgTableRow arg="user" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="profile" typ="enum"></ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none) { none:0 }"></ArgTableRow>
<ArgTableRow arg="verify-server-certificate" typ="bool"></ArgTableRow>
<ArgTableRow arg="tls-version" typ="enum (any | only-1.2) { any:0, only-1.2:2 }"></ArgTableRow>
<ArgTableRow arg="auth" typ="enum (sha1 | md5 | sha256 | sha384 | sha512 | null) { sha1:1, md5:2, sha256:8, sha384:32, sha512:16, null:4 }"></ArgTableRow>
<ArgTableRow arg="cipher" typ="enum (blowfish128 | aes128-cbc | aes192-cbc | aes256-cbc | aes128-gcm | aes192-gcm | aes256-gcm | null) { blowfish128:1, aes128-cbc:2, aes192-cbc:4, aes256-cbc:8, aes128-gcm:16, aes192-gcm:32, aes256-gcm:64, null:128 }"></ArgTableRow>
<ArgTableRow arg="use-peer-dns" typ="enum (no | yes | exclusively) { no:0, yes:1, exclusively:2 }"></ArgTableRow>
<ArgTableRow arg="add-default-route" typ="bool"></ArgTableRow>
<ArgTableRow arg="route-nopull" typ="bool">如果啟用，用戶端將不會使用伺服器推送的任何路由（包括 def1）</ArgTableRow>
<ArgTableRow arg="disconnect-notify" typ="bool">使用 UDP 模式時傳送顯式中斷通知</ArgTableRow>
</ArgTable>
