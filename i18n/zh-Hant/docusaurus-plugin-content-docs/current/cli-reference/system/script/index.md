---
sidebar_key: "cli-reference/system/script"
title: "script"
sidebar_label: 'script'
source: https://manual.mikrotik.com/docs/cli-reference/system/script
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
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
