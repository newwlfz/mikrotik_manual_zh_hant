---
title: "scan"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/lte/scan
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

-----------

## interface/lte/scan 
**條件：** !smips
**類型：** Command

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="C" typ="current">current</ArgTableRow>
<ArgTableRow arg="A" typ="available">available</ArgTableRow>
<ArgTableRow arg="F" typ="forbidden">forbidden</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="operator" typ="string"></ArgTableRow>
<ArgTableRow arg="mcc-mnc" typ="string"></ArgTableRow>
<ArgTableRow arg="access-technology" typ="string"></ArgTableRow>
<ArgTableRow arg="rssi" typ="num"></ArgTableRow>
<ArgTableRow arg="rsrp" typ="num"></ArgTableRow>
<ArgTableRow arg="rsrq" typ="num"></ArgTableRow>
</ArgTable>
