---
sidebar_key: "cli-reference/routing/pimsm/bsr/index"
sidebar_position: 2
title: "bsr"
sidebar_label: "bsr"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/routing/pimsm/bsr
captured_at: '2026-11-01T21:29:35+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/pimsm/bsr {#routingpimsmbsr}
**條件：** !smips
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="instance" typ="enum"></ArgTableRow>
<ArgTableRow arg="scope4" typ="address (flags=4/)" unset="1"></ArgTableRow>
<ArgTableRow arg="scope6" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46)"></ArgTableRow>
<ArgTableRow arg="priority" typ="num"></ArgTableRow>
<ArgTableRow arg="hash-mask-length" typ="num"></ArgTableRow>
<ArgTableRow arg="state" typ="enum (accept-any | accept-preferred | candidate | pending | elected)"></ArgTableRow>
</ArgTable>
