---
title: "vlan"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/ethernet/switch/qos/map/vlan
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

-----------

## interface/ethernet/switch/qos/map/vlan 
**Syscap:** rbswitch 與 crs_prestera
**Type:** 目錄

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="map" typ="enum"></ArgTableRow>
<ArgTableRow arg="pcp" typ="multi { pcp-range: range [0 .. 7]
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="dei-only" typ="bool">Map only if DEI/CFI bit is set</ArgTableRow>
<ArgTableRow arg="profile" typ="enum" mandatory="1"></ArgTableRow>
</ArgTable>
