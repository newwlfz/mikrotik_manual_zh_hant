---
title: "traceroute"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/mesh/traceroute
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

-----------

## interface/mesh/traceroute 
**類型：** 指令

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="mesh" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="hoplimit" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="time" typ="num"></ArgTableRow>
<ArgTableRow arg="status" typ="enum (success | ttl-exceeded | no-route | timeout) { success:1, ttl-exceeded:2, no-route:3, timeout:4 }"></ArgTableRow>
</ArgTable>
