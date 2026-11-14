---
sidebar_key: "cli-reference/interface/ethernet/switch/qos/map/ip"
sidebar_position: 1
title: "ip"
sidebar_label: 'ip'
source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/qos/map/ip
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/qos/map/ip {#interfaceethernetswitchqosmapip}
**系統能力：** rbswitch 和 crs_prestera
**型別：** 目錄

將 DSCP 值匹配到 QoS 配置檔案。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="*" typ="default"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="map" typ="enum">對映表的名稱。如果未設定，則會修改標準（內建）對映表。</ArgTableRow>
<ArgTableRow arg="dscp" typ="multi { dscp-range: range [0 .. 63]
 }" mandatory="1">用於查詢的 DSCP 值。</ArgTableRow>
<ArgTableRow arg="profile" typ="enum" mandatory="1">要分配給匹配封包的 QoS 配置檔案的名稱。</ArgTableRow>
</ArgTable>
