---
sidebar_key: "cli-reference/interface/ethernet/switch/qos/map/ip"
sidebar_position: 1
title: "ip"
sidebar_label: "ip"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/ethernet/switch/qos/map/ip
captured_at: '2026-11-01T21:27:15+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/qos/map/ip {#interfaceethernetswitchqosmapip}
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
<ArgTableRow arg="dscp" typ="multi { dscp-range: range [0 .. 63]
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="profile" typ="enum" mandatory="1"></ArgTableRow>
</ArgTable>
