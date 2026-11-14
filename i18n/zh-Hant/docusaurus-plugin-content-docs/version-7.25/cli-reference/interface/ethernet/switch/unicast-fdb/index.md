---
sidebar_key: "cli-reference/interface/ethernet/switch/unicast-fdb/index"
sidebar_position: 2
title: "unicast-fdb"
sidebar_label: 'unicast-fdb'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/ethernet/switch/unicast-fdb
captured_at: '2026-11-01T21:22:44+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/unicast-fdb {#interfaceethernetswitchunicast-fdb}
**系統能力：** musicswitch
**型別：** 目錄

單播轉發表資料庫最多支援 16K 個 MAC 條目。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
<ArgTableRow arg="A" typ="active"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="mac-address" typ="macAddr" mandatory="1">當目標 MAC 或源 MAC 與該條目匹配時，action 命令會作用於封包。</ArgTableRow>
<ArgTableRow arg="port" typ="alt { port: enum
, trunk: enum
 }" mandatory="1">單播 FDB 條目的匹配埠。</ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num">單播 FDB 查詢/學習的 VLAN ID。</ArgTableRow>
<ArgTableRow arg="action" typ="enum (forward | src-drop | dst-drop | src-and-dst-drop | ingress-port-policing-bypass | src-redirect-to-cpu | dst-redirect-to-cpu | src-and-dst-redirect-to-cpu) { forward:0, src-drop:1, dst-drop:2, src-and-dst-drop:3, ingress-port-policing-bypass:4, src-redirect-to-cpu:5, dst-redirect-to-cpu:6, src-and-dst-redirect-to-cpu:7 }">
UFDB 條目的動作。
- `dst-drop` - 當目標 MAC 與該條目匹配時，封包會被丟棄。
- `dst-redirect-to-cpu` - 當目標 MAC 與該條目匹配時，封包會被重定向到 CPU。
- `forward` - 封包會被轉發。
- `src-and-dst-drop` - 當源 MAC 或目標 MAC 與該條目匹配時，封包會被丟棄。
- `src-and-dst-redirect-to-cpu` - 當源 MAC 或目標 MAC 與該條目匹配時，封包會被重定向到 CPU。
- `src-drop` - 當源 MAC 與該條目匹配時，封包會被丟棄。
- `src-redirect-to-cpu` - 當源 MAC 與該條目匹配時，封包會被重定向到 CPU。
</ArgTableRow>
<ArgTableRow arg="mirror" typ="bool">啟用或停用基於源 MAC 或目標 MAC 的映象。</ArgTableRow>
<ArgTableRow arg="isolation-profile" typ="enum (promiscuous | isolated | community1 | community2) { promiscuous:0, isolated:1, community1:2, community2:3 }">MAC 級別隔離配置檔案。</ArgTableRow>
<ArgTableRow arg="svl" typ="bool">
單播 FDB 學習模式。
- `svl` - 共享 VLAN 學習，學習/查詢基於 MAC 地址，而不是 VLAN ID。
- `ivl` - 獨立 VLAN 學習，學習/查詢同時基於 MAC 地址和 VLAN ID。
</ArgTableRow>
<ArgTableRow arg="qos-group" typ="enum (none) { none:0xffffffff }">來自 QoS 組選單的已定義 QoS 組。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="age" typ="num"></ArgTableRow>
</ArgTable>
