---
sidebar_key: "cli-reference/interface/wireless/channels"
sidebar_position: 4
title: "channels"
sidebar_label: "channels"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/wireless/channels
captured_at: '2026-11-01T21:27:59+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/wireless/channels {#interfacewirelesschannels}
**包：** wireless-rep
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="list" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="frequency" typ="num" mandatory="1"></ArgTableRow>
<ArgTableRow arg="width" typ="num" mandatory="1"></ArgTableRow>
<ArgTableRow arg="band" typ="enum (2ghz-b | 2ghz-onlyg | 2ghz-b/g | 5ghz-a | 5ghz-onlyn | 5ghz-a/n | 2ghz-onlyn | 2ghz-b/g/n | 2ghz-g/n | 5ghz-a/n/ac | 5ghz-n/ac | 5ghz-onlyac)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="extension-channel" typ="enum (disabled | Ce | eC | Ceee | eCee | eeCe | eeeC)"></ArgTableRow>
</ArgTable>
