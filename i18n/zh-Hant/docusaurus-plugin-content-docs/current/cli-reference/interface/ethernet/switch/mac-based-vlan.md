---
sidebar_key: "cli-reference/interface/ethernet/switch/mac-based-vlan"
sidebar_position: 10
title: "mac-based-vlan"
sidebar_label: 'mac-based-vlan'
source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/mac-based-vlan
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/mac-based-vlan {#interfaceethernetswitchmac-based-vlan}
**系統能力：** musicswitch
**型別：** 目錄

基於 MAC 的 VLAN 表用於根據源 MAC 分配 VLAN。

所有 CRS1xx/2xx 系列交換器最多支援 1024 條基於 MAC 的 VLAN 表項。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="src-mac-address" typ="macAddr" mandatory="1">用於基於 MAC 的 VLAN 規則的匹配源 MAC 地址。</ArgTableRow>
<ArgTableRow arg="new-service-vid" typ="num">新的服務 VLAN ID 會替換匹配封包的原始服務 VLAN ID。</ArgTableRow>
<ArgTableRow arg="new-customer-vid" typ="num">新的客戶 VLAN ID 會替換匹配封包的原始服務 VLAN ID。如果設定為 4095，則丟棄流量。</ArgTableRow>
</ArgTable>
