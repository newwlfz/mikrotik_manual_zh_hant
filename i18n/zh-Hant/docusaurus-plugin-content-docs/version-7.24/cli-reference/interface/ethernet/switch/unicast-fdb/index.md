---
sidebar_key: "cli-reference/interface/ethernet/switch/unicast-fdb/index"
sidebar_position: 2
title: "unicast-fdb"
sidebar_label: "unicast-fdb"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/ethernet/switch/unicast-fdb
captured_at: '2026-11-01T21:27:19+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/unicast-fdb {#interfaceethernetswitchunicast-fdb}
**系統能力：** musicswitch
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
<ArgTableRow arg="A" typ="active"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="mac-address" typ="macAddr" mandatory="1"></ArgTableRow>
<ArgTableRow arg="port" typ="alt { port: enum
, trunk: enum
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num"></ArgTableRow>
<ArgTableRow arg="action" typ="enum (forward | src-drop | dst-drop | src-and-dst-drop | ingress-port-policing-bypass | src-redirect-to-cpu | dst-redirect-to-cpu | src-and-dst-redirect-to-cpu) { forward:0, src-drop:1, dst-drop:2, src-and-dst-drop:3, ingress-port-policing-bypass:4, src-redirect-to-cpu:5, dst-redirect-to-cpu:6, src-and-dst-redirect-to-cpu:7 }"></ArgTableRow>
<ArgTableRow arg="mirror" typ="bool"></ArgTableRow>
<ArgTableRow arg="isolation-profile" typ="enum (promiscuous | isolated | community1 | community2) { promiscuous:0, isolated:1, community1:2, community2:3 }"></ArgTableRow>
<ArgTableRow arg="svl" typ="bool"></ArgTableRow>
<ArgTableRow arg="qos-group" typ="enum (none) { none:0xffffffff }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="age" typ="num"></ArgTableRow>
</ArgTable>
