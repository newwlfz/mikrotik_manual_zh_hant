---
sidebar_key: "cli-reference/system/gps"
title: "gps"
sidebar_label: 'gps'
source: https://manual.mikrotik.com/docs/cli-reference/system/gps
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/gps {#systemgps}
**軟體包：** gps
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="port" typ="alt { serial: enum (none)
, interface: iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="channel" typ="num"></ArgTableRow>
<ArgTableRow arg="init-channel" typ="num"></ArgTableRow>
<ArgTableRow arg="init-string" typ="multi { array-id, string: string
 }"></ArgTableRow>
<ArgTableRow arg="set-system-time" typ="bool"></ArgTableRow>
<ArgTableRow arg="coordinate-format" typ="enum (dms | dd | ddmm)"></ArgTableRow>
<ArgTableRow arg="gps-antenna-select" typ="enum (internal | external) { internal:0, external:1 }" syscap="rb-gps"></ArgTableRow>
</ArgTable>
