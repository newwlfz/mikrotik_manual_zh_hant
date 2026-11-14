---
sidebar_key: "cli-reference/interface/ethernet/switch/qos/map/vlan"
sidebar_position: 2
title: "vlan"
sidebar_label: "vlan"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/ethernet/switch/qos/map/vlan
captured_at: '2026-11-01T21:27:17+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/qos/map/vlan {#interfaceethernetswitchqosmapvlan}
**系統能力：** rbswitch 和 crs_prestera
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="*" typ="default"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="map" typ="enum"></ArgTableRow>
<ArgTableRow arg="pcp" typ="multi { pcp-range: range [0 .. 7]
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="dei-only" typ="bool">僅當 DEI/CFI 位置位時才對映</ArgTableRow>
<ArgTableRow arg="profile" typ="enum" mandatory="1"></ArgTableRow>
</ArgTable>
