---
sidebar_key: "cli-reference/system/script/job"
sidebar_position: 2
title: "job"
sidebar_label: 'job'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/system/script/job
captured_at: '2026-11-01T21:25:45+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/script/job {#systemscriptjob}
**型別：** 目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="started" typ="date"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (command | login | api-login)"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="script" typ="enum"></ArgTableRow>
<ArgTableRow arg="owner" typ="string"></ArgTableRow>
<ArgTableRow arg="policy" typ="multi { array-id, policy: enum
 }"></ArgTableRow>
<ArgTableRow arg="parent" typ="num"></ArgTableRow>
<ArgTableRow arg="trace" typ="string"></ArgTableRow>
</ArgTable>
