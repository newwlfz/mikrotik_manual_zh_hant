---
sidebar_key: "cli-reference/system/health/index"
sidebar_position: 1
title: "health"
sidebar_label: "health"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/system/health
captured_at: '2026-11-01T21:29:52+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/health {#systemhealth}
**條件：** i386
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="state-after-reboot" typ="enum (disabled | enabled)"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="core" typ="num"></ArgTableRow>
<ArgTableRow arg="3.3v" typ="num"></ArgTableRow>
<ArgTableRow arg="5v" typ="num"></ArgTableRow>
<ArgTableRow arg="12v" typ="num"></ArgTableRow>
<ArgTableRow arg="lm87-temp" typ="num"></ArgTableRow>
<ArgTableRow arg="cpu-temp" typ="num"></ArgTableRow>
<ArgTableRow arg="board-temp" typ="num"></ArgTableRow>
<ArgTableRow arg="voltage1" typ="num"></ArgTableRow>
<ArgTableRow arg="voltage2" typ="num"></ArgTableRow>
<ArgTableRow arg="voltage3" typ="num"></ArgTableRow>
<ArgTableRow arg="voltage4" typ="num"></ArgTableRow>
<ArgTableRow arg="voltage5" typ="num"></ArgTableRow>
<ArgTableRow arg="voltage6" typ="num"></ArgTableRow>
<ArgTableRow arg="voltage7" typ="num"></ArgTableRow>
<ArgTableRow arg="voltage8" typ="num"></ArgTableRow>
<ArgTableRow arg="voltage9" typ="num"></ArgTableRow>
<ArgTableRow arg="voltage10" typ="num"></ArgTableRow>
<ArgTableRow arg="temp1" typ="num"></ArgTableRow>
<ArgTableRow arg="temp2" typ="num"></ArgTableRow>
<ArgTableRow arg="temp3" typ="num"></ArgTableRow>
<ArgTableRow arg="fan1" typ="num"></ArgTableRow>
<ArgTableRow arg="fan2" typ="num"></ArgTableRow>
<ArgTableRow arg="fan3" typ="num"></ArgTableRow>
<ArgTableRow arg="state" typ="enum (disabled | enabled)"></ArgTableRow>
</ArgTable>

## system/health {#systemhealth-1}
**條件：** !i386
**系統能力：** health
**型別：** 目錄

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="value" typ="alt { valuet: num
, valuer: num
, valuev: num
, valuea: num
, valuew: num
, valueb: enum (ok | fail | not-present | idle | no-input) { ok:0, fail:1, not-present:2, idle:3, no-input:4 }
, values: string
 }"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (C | RPM | V | A | W |  | )"></ArgTableRow>
</ArgTable>
