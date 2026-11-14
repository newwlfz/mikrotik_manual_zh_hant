---
sidebar_key: "cli-reference/interface/bridge/port/mst-override/index"
sidebar_position: 1
title: "mst-override"
sidebar_label: "mst-override"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/bridge/port/mst-override
captured_at: '2026-11-01T21:27:01+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/bridge/port/mst-override {#interfacebridgeportmst-override}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="identifier" typ="num" mandatory="1"></ArgTableRow>
<ArgTableRow arg="priority" typ="enum (0x00 | 0x10 | 0x20 | 0x30 | 0x40 | 0x50 | 0x60 | 0x70 | 0x80 | 0x90 | 0xa0 | 0xb0 | 0xc0 | 0xd0 | 0xe0 | 0xf0) { 0x00:0x00, 0x10:0x10, 0x20:0x20, 0x30:0x30, 0x40:0x40, 0x50:0x50, 0x60:0x60, 0x70:0x70, 0x80:0x80, 0x90:0x90, 0xa0:0xa0, 0xb0:0xb0, 0xc0:0xc0, 0xd0:0xd0, 0xe0:0xe0, 0xf0:0xf0 }"></ArgTableRow>
<ArgTableRow arg="internal-path-cost" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="debug-info" typ="string"></ArgTableRow>
</ArgTable>
