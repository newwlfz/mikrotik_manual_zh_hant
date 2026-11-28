---
title: "vlan"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/ethernet/switch/vlan
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

-----------

## interface/ethernet/switch/vlan 
**Syscap:** musicswitch
**Type:** 目錄

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="vlan-id" typ="num" mandatory="1"></ArgTableRow>
<ArgTableRow arg="ports" typ="multi { array-id }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="svl" typ="bool"></ArgTableRow>
<ArgTableRow arg="learn" typ="bool"></ArgTableRow>
<ArgTableRow arg="flood" typ="bool"></ArgTableRow>
<ArgTableRow arg="ingress-mirror" typ="bool"></ArgTableRow>
<ArgTableRow arg="qos-group" typ="enum (none) { none:0xffffffff }"></ArgTableRow>
</ArgTable>

## interface/ethernet/switch/vlan 
**Syscap:** rbswitch 與 oldswitch
**Type:** 目錄

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="switch" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num" mandatory="1"></ArgTableRow>
<ArgTableRow arg="ports" typ="multi { array-id, port: enum
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="independent-learning" typ="bool"></ArgTableRow>
</ArgTable>
