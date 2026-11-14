---
sidebar_key: "cli-reference/ip/proxy/monitor"
sidebar_position: 9
title: "monitor"
sidebar_label: "monitor"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/proxy/monitor
captured_at: '2026-11-01T21:28:55+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/proxy/monitor {#ipproxymonitor}
**型別：** 命令

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="status" typ="enum (stopped | running | invalid-address | building-cache | passthrough) { stopped:0, running:1, invalid-address:4, building-cache:5 }"></ArgTableRow>
<ArgTableRow arg="uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="client-connections" typ="num"></ArgTableRow>
<ArgTableRow arg="server-connections" typ="num"></ArgTableRow>
<ArgTableRow arg="requests" typ="num"></ArgTableRow>
<ArgTableRow arg="hits" typ="num"></ArgTableRow>
<ArgTableRow arg="cache-used" typ="num"></ArgTableRow>
<ArgTableRow arg="total-ram-used" typ="num"></ArgTableRow>
<ArgTableRow arg="received-from-servers" typ="num"></ArgTableRow>
<ArgTableRow arg="sent-to-clients" typ="num"></ArgTableRow>
<ArgTableRow arg="hits-sent-to-clients" typ="num"></ArgTableRow>
</ArgTable>
