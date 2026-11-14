---
sidebar_key: "cli-reference/ip/socks/connections"
sidebar_position: 2
title: "connections"
sidebar_label: "connections"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/socks/connections
captured_at: '2026-11-01T21:28:57+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/socks/connections {#ipsocksconnections}
**型別：** 目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="src-address" typ="composite { address: alt { addr-ipv4: ipAddr
, addr-ipv6: ip6Addr
 }
, port: num
 }"></ArgTableRow>
<ArgTableRow arg="dst-address" typ="composite { address: alt { addr-ipv4: ipAddr
, addr-ipv6: ip6Addr
, addr-domain: string
 }
, port: num
 }"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (unknown | out | in) { unknown:0, out:1, in:2 }"></ArgTableRow>
<ArgTableRow arg="tx" typ="num"></ArgTableRow>
<ArgTableRow arg="rx" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="user" typ="enum"></ArgTableRow>
</ArgTable>
