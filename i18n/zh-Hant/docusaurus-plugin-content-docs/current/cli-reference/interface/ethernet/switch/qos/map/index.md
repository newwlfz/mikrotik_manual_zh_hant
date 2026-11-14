---
sidebar_key: "cli-reference/interface/ethernet/switch/qos/map"
title: "map"
sidebar_label: 'map'
source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/qos/map
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/qos/map {#interfaceethernetswitchqosmap}
**系統能力：** rbswitch and crs_prestera
**型別：** 目錄

用於受信任封包的優先順序到配置檔案對映表。所有交換晶片都有一個內建對映表 - **default**。此外，某些型號允許使用者定義自定義對映表，並透過 **qos-map** 屬性為不同交換器埠分配不同對映表：

- 基於 **Marvell Prestera **98DX224S、98DX226S**** 或 ****98DX3236**** 交換晶片型號的裝置僅支援一個對映表 - default。
- 基於 **Marvell Prestera 98DX8xxx**、**98DX4xxx** 交換晶片或 **98DX325x** 型號裝置的裝置最多支援 12 個對映表（預設 + 11 個使用者定義）。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="*" typ="default"></ArgTableRow>
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded"></ArgTableRow>
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1">對映表的使用者定義名稱。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="hw-id" typ="num"></ArgTableRow>
</ArgTable>
