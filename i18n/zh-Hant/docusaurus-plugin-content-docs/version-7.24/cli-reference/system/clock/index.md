---
sidebar_key: "cli-reference/system/clock/index"
sidebar_position: 1
title: "clock"
sidebar_label: "clock"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/system/clock
captured_at: '2026-11-01T21:29:46+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/clock {#systemclock}
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="time" typ="date"></ArgTableRow>
<ArgTableRow arg="date" typ="date"></ArgTableRow>
<ArgTableRow arg="time-zone-autodetect" typ="bool"></ArgTableRow>
<ArgTableRow arg="time-zone-name" typ="enum"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="gmt-offset" typ="timezone"></ArgTableRow>
<ArgTableRow arg="dst-active" typ="bool"></ArgTableRow>
</ArgTable>
