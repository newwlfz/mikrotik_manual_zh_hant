---
sidebar_key: "cli-reference/port/remote-access"
sidebar_position: 1
title: "remote-access"
sidebar_label: 'remote-access'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/port/remote-access
captured_at: '2026-11-01T21:24:56+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## port/remote-access {#portremote-access}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未啟用</ArgTableRow>
<ArgTableRow arg="A" typ="active">已啟用</ArgTableRow>
<ArgTableRow arg="B" typ="busy">busy</ArgTableRow>
<ArgTableRow arg="L" typ="logging-active">logging-active</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="port" typ="enum"></ArgTableRow>
<ArgTableRow arg="channel" typ="num"></ArgTableRow>
<ArgTableRow arg="remote-addresses" typ="object { peer-spec: super { addr0: address (flags=46/)
, [addr1] [ -address (flags=46)]
, [port] [ @num]
 }
 }"></ArgTableRow>
<ArgTableRow arg="local-address" typ="alt { ipv4: ipAddr
, ipv6: ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="ip-port" typ="num"></ArgTableRow>
<ArgTableRow arg="protocol" typ="enum (tcp-server | rfc2217 | tcp-client | udp) { tcp-server:0, rfc2217:1, tcp-client:2, udp:3 }"></ArgTableRow>
<ArgTableRow arg="log-file" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="active-peer" typ="ip6Addr"></ArgTableRow>
<ArgTableRow arg="active-peer-port" typ="num"></ArgTableRow>
</ArgTable>
