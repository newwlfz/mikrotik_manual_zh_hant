---
sidebar_key: "cli-reference/interface/ethernet/switch/egress-vlan-tag"
sidebar_position: 4
title: "egress-vlan-tag"
sidebar_label: 'egress-vlan-tag'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/ethernet/switch/egress-vlan-tag
captured_at: '2026-11-01T21:22:32+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/egress-vlan-tag {#interfaceethernetswitchegress-vlan-tag}
**系統能力：** musicswitch
**型別：** 目錄

出站封包可被分配不同的 VLAN 標籤格式。當封包傳送到出站埠（目標埠）時，可以移除 VLAN 標籤、新增 VLAN 標籤或保持原樣。每個埠都獨立控制出站 VLAN 標籤格式。標籤格式包括：
- 無標籤
- 帶標籤
- 未修改

出站 VLAN 標籤表包含 4096 個條目，用於選擇 VLAN 標記。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="vlan-id" typ="num" mandatory="1">在出站時帶有標籤的 VLAN ID。</ArgTableRow>
<ArgTableRow arg="tagged-ports" typ="multi { array-id }">在出站時帶有標籤的埠。</ArgTableRow>
</ArgTable>
