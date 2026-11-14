---
sidebar_key: "cli-reference/interface/wifi/steering/index"
sidebar_position: 1
title: "steering"
sidebar_label: 'steering'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/wifi/steering
captured_at: '2026-11-01T21:23:17+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/wifi/steering {#interfacewifisteering}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="neighbor-group" typ="multi { array-id, neighbor-group: string
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="rrm" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="wnm" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="2g-probe-delay" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="transition-threshold" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="transition-threshold-time" typ="time" unset="1"></ArgTableRow>
<ArgTableRow arg="transition-request-period" typ="time" unset="1"></ArgTableRow>
<ArgTableRow arg="transition-request-count" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="transition-time" typ="alt { value: enum (unlimited | immediate) { unlimited:-1, immediate:0 }
, time: time
 }" unset="1"></ArgTableRow>
</ArgTable>
