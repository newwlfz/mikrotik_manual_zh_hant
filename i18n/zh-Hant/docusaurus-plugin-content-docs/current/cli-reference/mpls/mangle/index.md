---
sidebar_key: "cli-reference/mpls/mangle"
title: "mangle"
sidebar_label: 'mangle'
source: https://manual.mikrotik.com/docs/cli-reference/mpls/mangle
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## mpls/mangle {#mplsmangle}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="chain" typ="ubit (forward, output)" unset="1"></ArgTableRow>
<ArgTableRow arg="exp" typ="ubit (0, 1, 2, 3, 4, 5, 6, 7)" unset="1"></ArgTableRow>
<ArgTableRow arg="set-exp" typ="enum (0 | 1 | 2 | 3 | 4 | 5 | 6 | 7) { 0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7 }" unset="1"></ArgTableRow>
<ArgTableRow arg="set-mark" typ="enum" unset="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="packets" typ="num"></ArgTableRow>
</ArgTable>
