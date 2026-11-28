---
title: "layers"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/container/layers
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

-----------

## container/layers 
**套件：** container
**類型：** 目錄

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="layer-dir" typ="string"></ArgTableRow>
<ArgTableRow arg="size" typ="alt { size: num
, size-state: enum (unavailable | pending | done)
 }"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (layer | root-dir)"></ArgTableRow>
<ArgTableRow arg="containers" typ="multi { container: enum
 }"></ArgTableRow>
</ArgTable>
