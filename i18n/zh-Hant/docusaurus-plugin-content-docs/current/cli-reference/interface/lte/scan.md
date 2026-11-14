---
sidebar_key: "cli-reference/interface/lte/scan"
sidebar_position: 8
title: "scan"
sidebar_label: 'scan'
source: https://manual.mikrotik.com/docs/cli-reference/interface/lte/scan
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/lte/scan {#interfaceltescan}
**條件：** !smips
**型別：** 命令

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="C" typ="current">current</ArgTableRow>
<ArgTableRow arg="A" typ="available">available</ArgTableRow>
<ArgTableRow arg="F" typ="forbidden">forbidden</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="operator" typ="string"></ArgTableRow>
<ArgTableRow arg="mcc-mnc" typ="string"></ArgTableRow>
<ArgTableRow arg="access-technology" typ="string"></ArgTableRow>
<ArgTableRow arg="rssi" typ="num"></ArgTableRow>
<ArgTableRow arg="rsrp" typ="num"></ArgTableRow>
<ArgTableRow arg="rsrq" typ="num"></ArgTableRow>
</ArgTable>
