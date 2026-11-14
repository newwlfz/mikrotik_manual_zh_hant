---
sidebar_key: "cli-reference/system/ups/monitor"
sidebar_position: 2
title: "monitor"
sidebar_label: "monitor"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/system/ups/monitor
captured_at: '2026-11-01T21:30:11+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/ups/monitor {#systemupsmonitor}
**軟體包：** ups
**型別：** 命令

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="on-line" typ="bool"></ArgTableRow>
<ArgTableRow arg="on-battery" typ="bool"></ArgTableRow>
<ArgTableRow arg="transfer-cause" typ="string"></ArgTableRow>
<ArgTableRow arg="rtc-running" typ="bool"></ArgTableRow>
<ArgTableRow arg="runtime-left" typ="time"></ArgTableRow>
<ArgTableRow arg="offline-after" typ="time"></ArgTableRow>
<ArgTableRow arg="battery-charge" typ="num"></ArgTableRow>
<ArgTableRow arg="battery-voltage" typ="num"></ArgTableRow>
<ArgTableRow arg="line-voltage" typ="num"></ArgTableRow>
<ArgTableRow arg="output-voltage" typ="num"></ArgTableRow>
<ArgTableRow arg="load" typ="num"></ArgTableRow>
<ArgTableRow arg="temperature" typ="num"></ArgTableRow>
<ArgTableRow arg="frequency" typ="num"></ArgTableRow>
<ArgTableRow arg="replace-battery" typ="bool"></ArgTableRow>
<ArgTableRow arg="smart-boost" typ="bool"></ArgTableRow>
<ArgTableRow arg="smart-trim" typ="bool"></ArgTableRow>
<ArgTableRow arg="overload" typ="bool"></ArgTableRow>
<ArgTableRow arg="low-battery" typ="bool"></ArgTableRow>
<ArgTableRow arg="self-test" typ="string"></ArgTableRow>
<ArgTableRow arg="hid-self-test" typ="enum (done-and-passed | done-and-warning | done-and-error | aborted | in-progress | no-test-initiated) { done-and-passed:1, done-and-warning:2, done-and-error:3, aborted:4, in-progress:5, no-test-initiated:6 }"></ArgTableRow>
</ArgTable>
