---
sidebar_key: "cli-reference/container/layers"
sidebar_position: 4
title: "layers"
sidebar_label: 'layers'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/container/layers
captured_at: '2026-11-01T21:22:02+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## container/layers {#containerlayers}
**包：** container
**型別：** 目錄

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="layer-dir" typ="string"></ArgTableRow>
<ArgTableRow arg="size" typ="alt { size: num
, size-state: enum (unavailable | pending | done)
 }"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (layer | root-dir)"></ArgTableRow>
<ArgTableRow arg="containers" typ="multi { container: enum
 }"></ArgTableRow>
</ArgTable>
