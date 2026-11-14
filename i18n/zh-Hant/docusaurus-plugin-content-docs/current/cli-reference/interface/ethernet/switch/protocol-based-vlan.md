---
sidebar_key: "cli-reference/interface/ethernet/switch/protocol-based-vlan"
sidebar_position: 17
title: "protocol-based-vlan"
sidebar_label: 'protocol-based-vlan'
source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/protocol-based-vlan
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/protocol-based-vlan {#interfaceethernetswitchprotocol-based-vlan}
**系統能力：** musicswitch
**型別：**目錄

基於協定的 VLAN 表用於按埠為相關協定封包分配 VID 和 QoS 屬性。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="frame-type" typ="enum (ethernet | rfc-1042 | llc) { ethernet:0, rfc-1042:1, llc:2 }">匹配幀的封裝型別。</ArgTableRow>
<ArgTableRow arg="protocol" typ="alt { protocol: enum ()
, protocol-number: num [ .. 65535]
 }">基於協定的 VLAN 規則所匹配的協定。</ArgTableRow>
<ArgTableRow arg="ports" typ="multi { array-id }" mandatory="1">基於協定的 VLAN 規則所匹配的交換器埠。</ArgTableRow>
<ArgTableRow arg="set-service-vid-for" typ="enum (none | untagged-or-priority-tagged | tagged | all) { none:0, untagged-or-priority-tagged:1, tagged:2, all:3 }">針對不同封包型別的服務 VLAN ID 分配命令。</ArgTableRow>
<ArgTableRow arg="new-service-vid" typ="num">新的服務 VLAN ID 會替換指定協定的原始服務 VLAN ID。</ArgTableRow>
<ArgTableRow arg="set-customer-vid-for" typ="enum (none | untagged-or-priority-tagged | tagged | all) { none:0, untagged-or-priority-tagged:1, tagged:2, all:3 }">針對不同封包型別的客戶 VLAN ID 分配命令。</ArgTableRow>
<ArgTableRow arg="new-customer-vid" typ="num">新的客戶 VLAN ID 會替換指定協定的原始客戶 VLAN ID。如果設定為 4095，則流量會被丟棄。</ArgTableRow>
<ArgTableRow arg="set-qos-for" typ="enum (none | untagged-or-priority-tagged | tagged | all) { none:0, untagged-or-priority-tagged:1, tagged:2, all:3 }">QoS 分配命令適用的幀型別。</ArgTableRow>
<ArgTableRow arg="qos-group" typ="enum (none) { none:0xffffffff }">從 QoS 組選單中定義的 QoS 組。</ArgTableRow>
</ArgTable>
