---
sidebar_key: "cli-reference/system/gps/monitor"
sidebar_position: 1
title: "monitor"
sidebar_label: 'monitor'
source: https://manual.mikrotik.com/docs/cli-reference/system/gps/monitor
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/gps/monitor {#systemgpsmonitor}
**軟體包：** gps
**型別：** 命令

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="date-and-time" typ="date"></ArgTableRow>
<ArgTableRow arg="latitude" typ="string"></ArgTableRow>
<ArgTableRow arg="longitude" typ="string"></ArgTableRow>
<ArgTableRow arg="altitude" typ="string"></ArgTableRow>
<ArgTableRow arg="speed" typ="string"></ArgTableRow>
<ArgTableRow arg="destination-bearing" typ="string"></ArgTableRow>
<ArgTableRow arg="true-bearing" typ="string"></ArgTableRow>
<ArgTableRow arg="magnetic-bearing" typ="string"></ArgTableRow>
<ArgTableRow arg="valid" typ="bool"></ArgTableRow>
<ArgTableRow arg="satellites" typ="num"></ArgTableRow>
<ArgTableRow arg="fix-quality" typ="num"></ArgTableRow>
<ArgTableRow arg="horizontal-dilution" typ="num"></ArgTableRow>
<ArgTableRow arg="data-age" typ="alt { never: enum (never) { never:0 }
, time: time
 }"></ArgTableRow>
</ArgTable>
