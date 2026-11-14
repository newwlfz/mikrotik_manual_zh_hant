---
sidebar_key: "cli-reference/interface/ethernet/switch/trunk"
sidebar_position: 25
title: "trunk"
sidebar_label: 'trunk'
source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/trunk
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/trunk {#interfaceethernetswitchtrunk}
**系統能力：** musicswitch
**型別：** 目錄

Cloud Router Switch 中的 Trunking 提供具有硬體自動故障轉移和負載均衡的靜態鏈路聚合組。不支援 IEEE802.3ad 和 IEEE802.1ax 相容的鏈路聚合控制協定。最多支援 8 個 Trunk 組，每個 Trunk 組最多 8 個 Trunk 成員埠。CRS 埠 Trunking 根據以下所有引數計算 transmit-hash：L2 src-dst MAC + L3 src-dst IP + L4 src-dst Port。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">Trunk 組的名稱。</ArgTableRow>
<ArgTableRow arg="member-ports" typ="multi { array-id, port: enum
 }" mandatory="1">Trunk 組的成員埠。</ArgTableRow>
</ArgTable>
