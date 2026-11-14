---
sidebar_key: "cli-reference/interface/ethernet/switch/multicast-fdb"
sidebar_position: 11
title: "multicast-fdb"
sidebar_label: "multicast-fdb"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/ethernet/switch/multicast-fdb
captured_at: '2026-11-01T21:27:14+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/multicast-fdb {#interfaceethernetswitchmulticast-fdb}
**系統能力：** musicswitch
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="address" typ="alt { mac-address: macAddr
, ip-address: ipAddr
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="ports" typ="multi { array-id }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num"></ArgTableRow>
<ArgTableRow arg="svl" typ="bool"></ArgTableRow>
<ArgTableRow arg="bypass-vlan-filter" typ="bool"></ArgTableRow>
<ArgTableRow arg="qos-group" typ="enum (none) { none:0xffffffff }"></ArgTableRow>
</ArgTable>
