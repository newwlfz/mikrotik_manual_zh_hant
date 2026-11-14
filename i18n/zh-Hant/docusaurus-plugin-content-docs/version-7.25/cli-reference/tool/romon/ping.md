---
sidebar_key: "cli-reference/tool/romon/ping"
sidebar_position: 2
title: "ping"
sidebar_label: 'ping'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/tool/romon/ping
captured_at: '2026-11-01T21:25:57+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/romon/ping {#toolromonping}
**型別：** 命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="id" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="size" typ="num"></ArgTableRow>
<ArgTableRow arg="interval" typ="time"></ArgTableRow>
<ArgTableRow arg="count" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="seq" typ="num"></ArgTableRow>
<ArgTableRow arg="host" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="time" typ="time"></ArgTableRow>
<ArgTableRow arg="size" typ="num"></ArgTableRow>
<ArgTableRow arg="status" typ="string"></ArgTableRow>
<ArgTableRow arg="sent" typ="num"></ArgTableRow>
<ArgTableRow arg="received" typ="num"></ArgTableRow>
<ArgTableRow arg="packet-loss" typ="num"></ArgTableRow>
<ArgTableRow arg="min-rtt" typ="time"></ArgTableRow>
<ArgTableRow arg="avg-rtt" typ="time"></ArgTableRow>
<ArgTableRow arg="max-rtt" typ="time"></ArgTableRow>
</ArgTable>
