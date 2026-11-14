---
sidebar_key: "cli-reference/tool/traffic-generator/port"
sidebar_position: 4
title: "port"
sidebar_label: 'port'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/tool/traffic-generator/port
captured_at: '2026-11-01T21:26:05+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/traffic-generator/port {#tooltraffic-generatorport}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">無效</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="first-header" typ="enum (mac | vlan | ip | udp | raw | ipv6 | tcp) { mac:1, vlan:2, ip:3, udp:4, raw:5, ipv6:6, tcp:7 }"></ArgTableRow>
</ArgTable>
