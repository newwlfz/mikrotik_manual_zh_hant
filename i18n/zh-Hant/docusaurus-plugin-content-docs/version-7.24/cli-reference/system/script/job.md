---
sidebar_key: "cli-reference/system/script/job"
sidebar_position: 2
title: "job"
sidebar_label: "job"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/system/script/job
captured_at: '2026-11-01T21:30:07+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/script/job {#systemscriptjob}
**型別：** 目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="started" typ="date"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (command | login | api-login) { command:1, login:3, api-login:4 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="script" typ="enum"></ArgTableRow>
<ArgTableRow arg="owner" typ="string"></ArgTableRow>
<ArgTableRow arg="policy" typ="multi { array-id, policy: enum
 }"></ArgTableRow>
<ArgTableRow arg="parent" typ="num"></ArgTableRow>
<ArgTableRow arg="trace" typ="string"></ArgTableRow>
</ArgTable>
