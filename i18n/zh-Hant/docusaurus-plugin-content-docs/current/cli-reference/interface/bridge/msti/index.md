---
sidebar_key: "cli-reference/interface/bridge/msti"
title: "msti"
sidebar_label: 'msti'
source: https://manual.mikrotik.com/docs/cli-reference/interface/bridge/msti
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/bridge/msti {#interfacebridgemsti}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="identifier" typ="num" mandatory="1"></ArgTableRow>
<ArgTableRow arg="bridge" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="priority" typ="alt { priority: enum (0x0000 | 0x1000 | 0x2000 | 0x3000 | 0x4000 | 0x5000 | 0x6000 | 0x7000 | 0x8000 | 0x9000 | 0xa000 | 0xb000 | 0xc000 | 0xd000 | 0xe000 | 0xf000) { 0x0000:0x0000, 0x1000:0x1000, 0x2000:0x2000, 0x3000:0x3000, 0x4000:0x4000, 0x5000:0x5000, 0x6000:0x6000, 0x7000:0x7000, 0x8000:0x8000, 0x9000:0x9000, 0xa000:0xa000, 0xb000:0xb000, 0xc000:0xc000, 0xd000:0xd000, 0xe000:0xe000, 0xf000:0xf000 }
, priority: num [0 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="vlan-mapping" typ="multi { vlan-range: range [1 .. 4094]
 }" mandatory="1"></ArgTableRow>
</ArgTable>
