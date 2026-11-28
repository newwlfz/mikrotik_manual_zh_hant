---
title: "veth"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/veth
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

-----------

## interface/veth 
**條件：** !smips
**Syscap：** container
**類型：** 目錄

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="container-mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="address" typ="multi { address: address (flags=46/)
 }"></ArgTableRow>
<ArgTableRow arg="gateway" typ="address (flags=4)"></ArgTableRow>
<ArgTableRow arg="gateway6" typ="address (flags=6)"></ArgTableRow>
<ArgTableRow arg="dhcp" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="dhcp-address" typ="address (flags=46/)"></ArgTableRow>
</ArgTable>
