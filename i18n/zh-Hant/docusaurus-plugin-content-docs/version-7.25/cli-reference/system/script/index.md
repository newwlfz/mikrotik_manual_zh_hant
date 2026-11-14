---
sidebar_key: "cli-reference/system/script/index"
sidebar_position: 2
title: "script"
sidebar_label: 'script'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/system/script
captured_at: '2026-11-01T21:25:44+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/script {#systemscript}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="owner" typ="string"></ArgTableRow>
<ArgTableRow arg="policy" typ="multi { array-id, policy: enum
 }"></ArgTableRow>
<ArgTableRow arg="dont-require-permissions" typ="bool"></ArgTableRow>
<ArgTableRow arg="source" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="last-started" typ="date"></ArgTableRow>
<ArgTableRow arg="run-count" typ="num"></ArgTableRow>
</ArgTable>
