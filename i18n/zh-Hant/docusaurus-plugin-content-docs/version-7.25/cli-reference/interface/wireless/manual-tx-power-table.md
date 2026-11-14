---
sidebar_key: "cli-reference/interface/wireless/manual-tx-power-table"
sidebar_position: 9
title: "manual-tx-power-table"
sidebar_label: 'manual-tx-power-table'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/wireless/manual-tx-power-table
captured_at: '2026-11-01T21:23:24+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/wireless/manual-tx-power-table {#interfacewirelessmanual-tx-power-table}
**軟體包：** wireless-rep
**型別：** 目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="manual-tx-powers" typ="multi { array-id, array-id, manual-tx-power: composite { rate: enum ()
, tx-power: num [-30 .. 40]
 }
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
</ArgTable>
