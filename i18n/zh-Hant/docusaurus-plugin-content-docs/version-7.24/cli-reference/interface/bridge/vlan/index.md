---
sidebar_key: "cli-reference/interface/bridge/vlan/index"
sidebar_position: 1
title: "vlan"
sidebar_label: "vlan"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/bridge/vlan
captured_at: '2026-11-01T21:27:10+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/bridge/vlan {#interfacebridgevlan}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="Y" typ="managed">managed</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="bridge" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="vlan-ids" typ="multi { vlan-range: range [1 .. 4094]
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="tagged" typ="multi { array-id, interface: alt { interface: iface_enum
, interface-list: enum
 }
 }"></ArgTableRow>
<ArgTableRow arg="untagged" typ="multi { array-id, interface: alt { interface: iface_enum
, interface-list: enum
 }
 }"></ArgTableRow>
<ArgTableRow arg="mvrp-forbidden" typ="multi { array-id, interface: alt { interface: iface_enum
, interface-list: enum
 }
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="current-tagged" typ="multi { array-id, interface: iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="current-untagged" typ="multi { array-id, interface: iface_enum
 }"></ArgTableRow>
</ArgTable>
