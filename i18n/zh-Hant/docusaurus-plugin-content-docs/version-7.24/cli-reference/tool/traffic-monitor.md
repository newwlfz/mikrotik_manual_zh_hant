---
sidebar_key: "cli-reference/tool/traffic-monitor"
sidebar_position: 26
title: "traffic-monitor"
sidebar_label: "traffic-monitor"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/tool/traffic-monitor
captured_at: '2026-11-01T21:30:27+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/traffic-monitor {#tooltraffic-monitor}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">無效</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="traffic" typ="enum (transmitted | received) { transmitted:1, received:2 }"></ArgTableRow>
<ArgTableRow arg="trigger" typ="enum (above | below | always) { above:1, below:2, always:3 }"></ArgTableRow>
<ArgTableRow arg="threshold" typ="num"></ArgTableRow>
<ArgTableRow arg="on-event" typ="alt { script: string
 }"></ArgTableRow>
</ArgTable>
