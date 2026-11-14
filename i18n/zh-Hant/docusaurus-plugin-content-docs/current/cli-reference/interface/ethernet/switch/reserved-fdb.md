---
sidebar_key: "cli-reference/interface/ethernet/switch/reserved-fdb"
sidebar_position: 20
title: "reserved-fdb"
sidebar_label: 'reserved-fdb'
source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/reserved-fdb
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/reserved-fdb {#interfaceethernetswitchreserved-fdb}
**系統能力：** musicswitch
**型別：** 目錄

Cloud Router Switch 支援 256 個 RFDB 條目。每個 RFDB 條目可以儲存具有特定命令的二層單播或組播 MAC 地址。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="mac-address" typ="macAddr" mandatory="1">用於 Reserved FDB 條目的匹配 MAC 地址。</ArgTableRow>
<ArgTableRow arg="action" typ="enum (forward | redirect-to-cpu | copy-to-cpu | drop) { forward:0, redirect-to-cpu:1, copy-to-cpu:2, drop:3 }">
RFDB 條目的動作。
- `copy-to-cpu` - 當封包的目標 MAC 地址與該條目匹配時，封包會被複制到 CPU。
- `drop` - 當封包的目標 MAC 地址與該條目匹配時，封包會被丟棄。
- `forward` - 當封包的目標 MAC 地址與該條目匹配時，封包會被轉發。
- `redirect-to-cpu` - 當封包的目標 MAC 地址與該條目匹配時，封包會被重定向到 CPU。
</ArgTableRow>
<ArgTableRow arg="bypass-ingress-vlan-filter" typ="bool">允許對匹配的封包繞過 VLAN 過濾。</ArgTableRow>
<ArgTableRow arg="bypass-ingress-port-policing" typ="bool">允許對匹配的封包繞過 Ingress Port Policer。</ArgTableRow>
<ArgTableRow arg="qos-group" typ="enum (none) { none:0xffffffff }">在 QoS group 選單中定義的 QoS 組。</ArgTableRow>
</ArgTable>
