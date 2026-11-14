---
sidebar_key: "cli-reference/tool/flood-ping"
sidebar_position: 7
title: "flood-ping"
sidebar_label: "flood-ping"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/tool/flood-ping
captured_at: '2026-11-01T21:30:15+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/flood-ping {#toolflood-ping}
**條件：** !smips
**型別：** 命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="address" typ="alt { ipv6: ip6Addr
, ip: ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="count" typ="num"></ArgTableRow>
<ArgTableRow arg="size" typ="num"></ArgTableRow>
<ArgTableRow arg="timeout" typ="time"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="sent" typ="num"></ArgTableRow>
<ArgTableRow arg="received" typ="num"></ArgTableRow>
<ArgTableRow arg="min-rtt" typ="time"></ArgTableRow>
<ArgTableRow arg="avg-rtt" typ="time"></ArgTableRow>
<ArgTableRow arg="max-rtt" typ="time"></ArgTableRow>
</ArgTable>
