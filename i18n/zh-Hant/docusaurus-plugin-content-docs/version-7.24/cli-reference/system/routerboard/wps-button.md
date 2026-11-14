---
sidebar_key: "cli-reference/system/routerboard/wps-button"
sidebar_position: 6
title: "wps-button"
sidebar_label: "wps-button"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/system/routerboard/wps-button
captured_at: '2026-11-01T21:30:05+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/routerboard/wps-button {#systemrouterboardwps-button}
**條件：** !i386
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="hold-time" typ="composite { min: time [0 .. 60]
, max: time [0 .. 60]
 }"></ArgTableRow>
<ArgTableRow arg="on-event" typ="alt { script: string
 }"></ArgTableRow>
</ArgTable>
