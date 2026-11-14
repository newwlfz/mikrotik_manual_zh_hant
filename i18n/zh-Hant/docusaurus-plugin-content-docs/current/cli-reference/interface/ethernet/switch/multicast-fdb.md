---
sidebar_key: "cli-reference/interface/ethernet/switch/multicast-fdb"
sidebar_position: 11
title: "multicast-fdb"
sidebar_label: 'multicast-fdb'
source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/multicast-fdb
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/multicast-fdb {#interfaceethernetswitchmulticast-fdb}
**系統能力：** musicswitch
**型別：** 目錄

CRS125 交換晶片在 MFDB 中最多支援 1024 個條目用於組播轉發。對於每個組播封包，在 MFDB 中執行目標 MAC 或目標 IP 查詢。MFDB 條目不會自動學習，只能配置。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="address" typ="alt { mac-address: macAddr
, ip-address: ipAddr
 }" mandatory="1">用於匹配組播封包的 IP 地址或 MAC 地址。</ArgTableRow>
<ArgTableRow arg="ports" typ="multi { array-id }" mandatory="1">組播流量的成員埠。</ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num">組播 FDB 查詢 VLAN ID。如果 VLAN 學習模式為 IVL，則 VLAN ID 為查詢 ID，否則 VLAN ID = 0。</ArgTableRow>
<ArgTableRow arg="svl" typ="bool">
組播 FDB 學習模式。
- `svl` - 共享 VLAN 學習，學習/查詢基於 MAC 地址，而不是 VLAN ID。
- `ivl` - 獨立 VLAN 學習，學習/查詢同時基於 MAC 地址和 VLAN ID。
</ArgTableRow>
<ArgTableRow arg="bypass-vlan-filter" typ="bool">允許匹配的組播封包繞過 VLAN 過濾。</ArgTableRow>
<ArgTableRow arg="qos-group" typ="enum (none) { none:0xffffffff }">從 QoS 組選單中定義的 QoS 組。</ArgTableRow>
</ArgTable>
