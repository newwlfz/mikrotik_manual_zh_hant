---
sidebar_key: "cli-reference/dude/ros/health"
sidebar_position: 3
title: "health"
sidebar_label: "health"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/dude/ros/health
captured_at: '2026-11-01T21:26:51+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## dude/ros/health {#duderoshealth}
**包：** dude
**型別：** 目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="device" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="fan-mode" typ="enum (manual | auto) { manual:0, auto:1 }"></ArgTableRow>
<ArgTableRow arg="use-fan" typ="enum (auxiliary | main) { auxiliary:0, main:1 }"></ArgTableRow>
<ArgTableRow arg="use-fan2" typ="enum (auxiliary | main) { auxiliary:0, main:1 }"></ArgTableRow>
<ArgTableRow arg="fan-switch" typ="enum (auto | on | off) { auto:0, on:1, off:2 }"></ArgTableRow>
<ArgTableRow arg="fan-on-threshold" typ="num"></ArgTableRow>
<ArgTableRow arg="cpu-overtemp-check" typ="bool"></ArgTableRow>
<ArgTableRow arg="cpu-overtemp-threshold" typ="num"></ArgTableRow>
<ArgTableRow arg="cpu-overtemp-startup-delay" typ="time"></ArgTableRow>
<ArgTableRow arg="psu1-state" typ="enum (ok | fail) { ok:0, fail:1 }"></ArgTableRow>
<ArgTableRow arg="psu2-state" typ="enum (ok | fail) { ok:0, fail:1 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="active-fan" typ="enum (auxiliary | main | none) { auxiliary:0, main:1, none:2 }"></ArgTableRow>
<ArgTableRow arg="active-fan2" typ="enum (auxiliary | main | none) { auxiliary:0, main:1, none:2 }"></ArgTableRow>
<ArgTableRow arg="voltage" typ="num"></ArgTableRow>
<ArgTableRow arg="battery" typ="num"></ArgTableRow>
<ArgTableRow arg="current" typ="num"></ArgTableRow>
<ArgTableRow arg="fan-speed" typ="num"></ArgTableRow>
<ArgTableRow arg="fan-speed2" typ="num"></ArgTableRow>
<ArgTableRow arg="temperature" typ="num"></ArgTableRow>
<ArgTableRow arg="cpu-temperature" typ="num"></ArgTableRow>
<ArgTableRow arg="power-consumption" typ="num"></ArgTableRow>
<ArgTableRow arg="board-temperature1" typ="num"></ArgTableRow>
<ArgTableRow arg="board-temperature2" typ="num"></ArgTableRow>
<ArgTableRow arg="board-temperature3" typ="num"></ArgTableRow>
<ArgTableRow arg="psu1-voltage" typ="num"></ArgTableRow>
<ArgTableRow arg="psu2-voltage" typ="num"></ArgTableRow>
<ArgTableRow arg="psu1-current" typ="num"></ArgTableRow>
<ArgTableRow arg="psu2-current" typ="num"></ArgTableRow>
<ArgTableRow arg="fan1-speed" typ="num"></ArgTableRow>
<ArgTableRow arg="fan2-speed" typ="num"></ArgTableRow>
<ArgTableRow arg="fan3-speed" typ="num"></ArgTableRow>
<ArgTableRow arg="fan4-speed" typ="num"></ArgTableRow>
<ArgTableRow arg="fan5-speed" typ="num"></ArgTableRow>
<ArgTableRow arg="fan6-speed" typ="num"></ArgTableRow>
</ArgTable>
