---
title: "monitor-slaves"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/bonding/monitor-slaves
captured_at: '2026-11-28T10:19:39.818Z'
pagination_prev: "cli-reference/interface/bonding"
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

-----------

## interface/bonding/monitor-slaves 
**類型：** Command

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="A" typ="active">active</ArgTableRow>
<ArgTableRow arg="P" typ="partner">partner</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="bond" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="once" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="port" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="key" typ="num"></ArgTableRow>
<ArgTableRow arg="flags" typ="string"></ArgTableRow>
<ArgTableRow arg="partner-sys-id" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="partner-sys-priority" typ="num"></ArgTableRow>
<ArgTableRow arg="partner-key" typ="num"></ArgTableRow>
<ArgTableRow arg="partner-flags" typ="string"></ArgTableRow>
</ArgTable>
