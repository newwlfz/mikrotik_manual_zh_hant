---
sidebar_key: "cli-reference/container/config"
sidebar_position: 1
title: "config"
sidebar_label: "config"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/container/config
captured_at: '2026-11-01T21:26:37+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## container/config {#containerconfig}
**包：** container
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="registry-url" typ="string"></ArgTableRow>
<ArgTableRow arg="username" typ="string"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="layer-dir" typ="file"></ArgTableRow>
<ArgTableRow arg="tmpdir" typ="file"></ArgTableRow>
<ArgTableRow arg="memory-high" typ="num"></ArgTableRow>
<ArgTableRow arg="memory-max" typ="num"></ArgTableRow>
<ArgTableRow arg="swap-max" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="assumed-registry-url" typ="string"></ArgTableRow>
<ArgTableRow arg="memory-current" typ="num"></ArgTableRow>
<ArgTableRow arg="swap-current" typ="num"></ArgTableRow>
</ArgTable>
