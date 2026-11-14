---
sidebar_key: "cli-reference/system/telnet"
sidebar_position: 35
title: "telnet"
sidebar_label: 'telnet'
source: https://manual.mikrotik.com/docs/cli-reference/system/telnet
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/telnet {#systemtelnet}
**型別：** 命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="address" typ="alt { ip-address: ipAddr
, ipv6-address: composite { addr: ip6Addr
, interface: [ iface_enum]
 }
 }"></ArgTableRow>
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="vrf" typ="enum"></ArgTableRow>
</ArgTable>
