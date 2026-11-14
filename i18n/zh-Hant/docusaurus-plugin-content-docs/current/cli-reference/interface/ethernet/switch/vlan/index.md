---
sidebar_key: "cli-reference/interface/ethernet/switch/vlan"
sidebar_position: 27
title: "vlan"
sidebar_label: 'vlan'
source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/vlan
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/vlan {#interfaceethernetswitchvlan}
**系統能力：** musicswitch
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="vlan-id" typ="num" mandatory="1">VLAN 成員條目的 VLAN ID。</ArgTableRow>
<ArgTableRow arg="ports" typ="multi { array-id }" mandatory="1">VLAN 的成員埠。</ArgTableRow>
<ArgTableRow arg="svl" typ="bool">
用於在 UFDB 和 MFDB 中查詢的 FDB 查詢模式。
- `svl` - 共享 VLAN 學習，學習和查詢基於 MAC 地址，而不是 VLAN ID。
- `ivl` - 獨立 VLAN 學習，學習和查詢同時基於 MAC 地址和 VLAN ID。
</ArgTableRow>
<ArgTableRow arg="learn" typ="bool">啟用或停用 VLAN 的源 MAC 學習。</ArgTableRow>
<ArgTableRow arg="flood" typ="bool">啟用或停用按 VLAN 的強制 VLAN 泛洪。如果啟用，將忽略在 UFDB 或 MFDB 中進行的目標 MAC 查詢結果，並強制封包在該 VLAN 中泛洪。</ArgTableRow>
<ArgTableRow arg="ingress-mirror" typ="bool">啟用按 VLAN 的入方向映象，以支援基於 VLAN 的映象功能。</ArgTableRow>
<ArgTableRow arg="qos-group" typ="enum (none) { none:0xffffffff }">QoS 組選單中定義的 QoS 組。</ArgTableRow>
</ArgTable>

## interface/ethernet/switch/vlan {#interfaceethernetswitchvlan-1}
**系統能力：** rbswitch 和 oldswitch
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="switch" typ="enum" mandatory="1">相應 VLAN 條目所針對的交換器名稱。</ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num" mandatory="1">VLAN 成員條目的 VLAN ID。</ArgTableRow>
<ArgTableRow arg="ports" typ="multi { array-id, port: enum
 }" mandatory="1">VLAN 的成員埠。</ArgTableRow>
<ArgTableRow arg="independent-learning" typ="bool">是否使用 shared-VLAN-learning (SVL) 或 independent-VLAN-learning (IVL)。</ArgTableRow>
</ArgTable>
