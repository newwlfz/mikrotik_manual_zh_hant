---
sidebar_key: "cli-reference/interface/ethernet/switch/one2one-vlan-switching"
sidebar_position: 12
title: "one2one-vlan-switching"
sidebar_label: 'one2one-vlan-switching'
source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/one2one-vlan-switching
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/one2one-vlan-switching {#interfaceethernetswitchone2one-vlan-switching}
**系統能力：** musicswitch
**型別：** 目錄

1:1 VLAN 交換可用於替換匹配封包的常規 L2 橋接。當封包命中 1:1 VLAN 交換表條目時，該條目中的目標埠資訊會分配給該封包。UFDB 和 MFDB 條目中匹配的目標資訊不再適用於該封包。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="dst-port" typ="alt { port: enum
, trunk: enum
 }" mandatory="1">匹配的 1:1 VLAN 交換封包的目標埠。</ArgTableRow>
<ArgTableRow arg="service-vid" typ="num">用於 1:1 VLAN 交換的匹配服務 VLAN ID。</ArgTableRow>
<ArgTableRow arg="customer-vid" typ="num">用於 1:1 VLAN 交換的匹配客戶 VLAN ID。</ArgTableRow>
</ArgTable>
