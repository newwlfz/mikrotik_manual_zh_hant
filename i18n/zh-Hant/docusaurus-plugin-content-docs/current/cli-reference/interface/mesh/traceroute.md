---
sidebar_key: "cli-reference/interface/mesh/traceroute"
sidebar_position: 3
title: "traceroute"
sidebar_label: 'traceroute'
source: https://manual.mikrotik.com/docs/cli-reference/interface/mesh/traceroute
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/mesh/traceroute {#interfacemeshtraceroute}
**型別：**命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="mesh" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="hoplimit" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="time" typ="num"></ArgTableRow>
<ArgTableRow arg="status" typ="enum (success | ttl-exceeded | no-route | timeout) { success:1, ttl-exceeded:2, no-route:3, timeout:4 }"></ArgTableRow>
</ArgTable>
