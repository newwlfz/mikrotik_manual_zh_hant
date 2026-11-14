---
sidebar_key: "cli-reference/radius"
title: "radius"
sidebar_label: 'radius'
source: https://manual.mikrotik.com/docs/cli-reference/radius
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## radius {#radius}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="service" typ="ubit (ppp, login, hotspot, wireless, dhcp, ipsec, dot1x)"></ArgTableRow>
<ArgTableRow arg="called-id" typ="string"></ArgTableRow>
<ArgTableRow arg="domain" typ="string"></ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46v)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="secret" typ="string"></ArgTableRow>
<ArgTableRow arg="authentication-port" typ="num"></ArgTableRow>
<ArgTableRow arg="accounting-port" typ="num"></ArgTableRow>
<ArgTableRow arg="timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="radsec-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="accounting-backup" typ="bool"></ArgTableRow>
<ArgTableRow arg="realm" typ="string"></ArgTableRow>
<ArgTableRow arg="src-address" typ="alt { ip-address: ipAddr
, ipv6-address: ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="protocol" typ="enum (udp | radsec)"></ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none) { none:0 }"></ArgTableRow>
<ArgTableRow arg="require-message-auth" typ="enum (no | yes-for-request-resp)"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
</ArgTable>
