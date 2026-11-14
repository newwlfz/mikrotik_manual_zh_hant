---
sidebar_key: "cli-reference/tool/traffic-generator/port"
sidebar_position: 4
title: "port"
sidebar_label: 'port'
source: https://manual.mikrotik.com/docs/cli-reference/tool/traffic-generator/port
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/traffic-generator/port {#tooltraffic-generatorport}
**型別：** Directory
埠將介面繫結到流量生成器，用於傳送和接收生成的封包。參見 [流量生成器](../../../diagnostics-monitoring-and-troubleshooting/traffic-generator.md) 指南。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">無效</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">埠的描述性名稱。</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">與該埠關聯的介面名稱。必填。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="first-header" typ="enum (mac | vlan | ip | udp | raw | ipv6 | tcp) { mac:1, vlan:2, ip:3, udp:4, raw:5, ipv6:6, tcp:7 }">建議從此介面發出的封包使用的第一個首部。建立封包模板時可以使用。</ArgTableRow>
</ArgTable>
