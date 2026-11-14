---
sidebar_key: "cli-reference/system/scheduler"
sidebar_position: 26
title: "scheduler"
sidebar_label: "scheduler"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/system/scheduler
captured_at: '2026-11-01T21:30:06+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/scheduler {#systemscheduler}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="start-date" typ="date"></ArgTableRow>
<ArgTableRow arg="start-time" typ="alt { startup: enum (startup) { startup:0xffffffff }
, time: date
 }"></ArgTableRow>
<ArgTableRow arg="days" typ="alt { day: enum (never | always) { never:0, always:127 }
, day: ubit (sun, mon, tue, wed, thu, fri, sat)
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="interval" typ="time"></ArgTableRow>
<ArgTableRow arg="on-event" typ="alt { script: string
 }"></ArgTableRow>
<ArgTableRow arg="policy" typ="multi { array-id, policy: enum
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="owner" typ="string"></ArgTableRow>
<ArgTableRow arg="run-count" typ="num"></ArgTableRow>
<ArgTableRow arg="next-run" typ="date"></ArgTableRow>
</ArgTable>
