---
title: "network"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/app/network
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

-----------

## app/network 
**Syscap:** app
**Package:** container
**Type:** 目錄

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="e" typ="external"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="allow-outgoing-access" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="network" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="ip" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="status" typ="string"></ArgTableRow>
<ArgTableRow arg="used-ips" typ="multi { array-id, array-id, ip-and-name: composite { ip: ipAddr
, name: string
 }
 }"></ArgTableRow>
<ArgTableRow arg="bridge-interface" typ="iface_enum { none }"></ArgTableRow>
<ArgTableRow arg="cmds" typ="multi { cmd: string
 }"></ArgTableRow>
</ArgTable>
