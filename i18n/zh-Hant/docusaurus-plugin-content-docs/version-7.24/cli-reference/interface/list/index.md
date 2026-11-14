---
sidebar_key: "cli-reference/interface/list/index"
sidebar_position: 1
title: "list"
sidebar_label: "list"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/list
captured_at: '2026-11-01T21:27:23+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/list {#interfacelist}
**型別：**目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="*" typ="builtin">builtin</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="include" typ="multi { include-list: enum
 }"></ArgTableRow>
<ArgTableRow arg="exclude" typ="multi { exclude-list: enum
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="dynamic" typ="bool"></ArgTableRow>
</ArgTable>
