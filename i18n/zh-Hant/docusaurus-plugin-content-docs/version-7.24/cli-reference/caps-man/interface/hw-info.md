---
title: "hw-info"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/caps-man/interface/hw-info
captured_at: '2026-11-28T10:19:39.818Z'
pagination_prev: "cli-reference/caps-man/interface"
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

-----------

## caps-man/interface/hw-info 
**套件:** wireless-rep
**類型:** 指令

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="ranges" typ="multi { array-id, range: string
 }"></ArgTableRow>
<ArgTableRow arg="tx-chains" typ="ubit (0, 1, 2, 3)"></ArgTableRow>
<ArgTableRow arg="rx-chains" typ="ubit (0, 1, 2, 3)"></ArgTableRow>
<ArgTableRow arg="antenna-gain" typ="num"></ArgTableRow>
<ArgTableRow arg="locked-countries" typ="multi { array-id, country: enum
 }"></ArgTableRow>
</ArgTable>
