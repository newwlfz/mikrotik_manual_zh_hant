---
sidebar_key: "cli-reference/interface/detect-internet/state"
sidebar_position: 1
title: "state"
sidebar_label: "state"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/detect-internet/state
captured_at: '2026-11-01T21:27:03+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/detect-internet/state {#interfacedetect-internetstate}
**型別：** 目錄

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="state" typ="enum (no-link | unknown | lan | wan | internet | slave) { no-link:0, unknown:1, lan:2, wan:3, internet:4, slave:5 }"></ArgTableRow>
<ArgTableRow arg="state-change-time" typ="date"></ArgTableRow>
<ArgTableRow arg="cloud-rtt" typ="time"></ArgTableRow>
</ArgTable>
