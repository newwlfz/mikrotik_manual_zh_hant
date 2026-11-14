---
sidebar_key: "cli-reference/interface/ethernet/switch/qos/map/vlan"
sidebar_position: 2
title: "vlan"
sidebar_label: 'vlan'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/ethernet/switch/qos/map/vlan
captured_at: '2026-11-01T21:22:38+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/qos/map/vlan {#interfaceethernetswitchqosmapvlan}
**系統能力：** rbswitch 和 crs_prestera
**型別：** 目錄

將 VLAN 優先順序（802.1p PCP/DEI 欄位）匹配到 QoS 配置檔案。預設情況下，所有值都匹配到預設 QoS 配置檔案。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="*" typ="default"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="map" typ="enum">對映表的名稱。</ArgTableRow>
<ArgTableRow arg="pcp" typ="multi { pcp-range: range [0 .. 7]
 }" mandatory="1">用於查詢的 VLAN 優先順序（PCP）值。</ArgTableRow>
<ArgTableRow arg="dei-only" typ="bool">僅對映 VLAN 頭中設定了 DEI（原為 CFI）位的報文。</ArgTableRow>
<ArgTableRow arg="profile" typ="enum" mandatory="1">要分配給匹配報文的 QoS 配置檔案的名稱。</ArgTableRow>
</ArgTable>
