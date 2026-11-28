---
title: "list"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/list
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

-----------

## interface/list 
**類型：** 目錄

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="builtin">builtin</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="include" typ="multi { include-list: enum
 }"></ArgTableRow>
<ArgTableRow arg="exclude" typ="multi { exclude-list: enum
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="dynamic" typ="bool"></ArgTableRow>
</ArgTable>
