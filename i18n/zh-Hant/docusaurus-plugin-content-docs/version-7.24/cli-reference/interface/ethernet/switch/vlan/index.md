---
sidebar_key: "cli-reference/interface/ethernet/switch/vlan/index"
sidebar_position: 27
title: "vlan"
sidebar_label: "vlan"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/ethernet/switch/vlan
captured_at: '2026-11-01T21:27:20+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/vlan {#interfaceethernetswitchvlan}
**系統能力：** musicswitch
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="vlan-id" typ="num" mandatory="1"></ArgTableRow>
<ArgTableRow arg="ports" typ="multi { array-id }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="svl" typ="bool"></ArgTableRow>
<ArgTableRow arg="learn" typ="bool"></ArgTableRow>
<ArgTableRow arg="flood" typ="bool"></ArgTableRow>
<ArgTableRow arg="ingress-mirror" typ="bool"></ArgTableRow>
<ArgTableRow arg="qos-group" typ="enum (none) { none:0xffffffff }"></ArgTableRow>
</ArgTable>

## interface/ethernet/switch/vlan {#interfaceethernetswitchvlan-1}
**系統能力：** rbswitch 和 oldswitch
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="switch" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num" mandatory="1"></ArgTableRow>
<ArgTableRow arg="ports" typ="multi { array-id, port: enum
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="independent-learning" typ="bool"></ArgTableRow>
</ArgTable>
