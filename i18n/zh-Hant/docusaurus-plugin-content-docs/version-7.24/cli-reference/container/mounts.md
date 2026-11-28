---
title: "mounts"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/container/mounts
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

-----------

## container/mounts
**套件:** container
**類型:** 目錄

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="list" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="src" typ="file"></ArgTableRow>
<ArgTableRow arg="dst" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="mode" typ="enum (rw | ro | rw,noexec | ro,noexec)"></ArgTableRow>
</ArgTable>
