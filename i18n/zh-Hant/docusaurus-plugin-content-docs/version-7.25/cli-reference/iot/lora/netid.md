---
sidebar_key: "cli-reference/iot/lora/netid"
sidebar_position: 3
title: "netid"
sidebar_label: 'netid'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/iot/lora/netid
captured_at: '2026-11-01T21:23:38+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## iot/lora/netid {#iotloranetid}
**包：** iot
**型別：** 目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="logging" typ="bool"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (whitelist | blacklist) { whitelist:1, blacklist:2 }"></ArgTableRow>
<ArgTableRow arg="netids" typ="object { range: composite { min: string
, max: string
 }
 }"></ArgTableRow>
</ArgTable>
