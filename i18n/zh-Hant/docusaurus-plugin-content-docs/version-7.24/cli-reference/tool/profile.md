---
sidebar_key: "cli-reference/tool/profile"
sidebar_position: 16
title: "profile"
sidebar_label: "profile"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/tool/profile
captured_at: '2026-11-01T21:30:19+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/profile {#toolprofile}
**型別：**命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="cpu" typ="enum (all | total) { all:0xfffffffe, total:0xfffffffd }" syscap="smp"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="cpu" typ="num" syscap="smp"></ArgTableRow>
<ArgTableRow arg="usage" typ="num"></ArgTableRow>
</ArgTable>
