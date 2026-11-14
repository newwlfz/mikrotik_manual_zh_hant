---
sidebar_key: "cli-reference/interface/ethernet/switch/ingress-port-policer"
sidebar_position: 7
title: "ingress-port-policer"
sidebar_label: 'ingress-port-policer'
source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/ingress-port-policer
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/ingress-port-policer {#interfaceethernetswitchingress-port-policer}
**系統能力：** musicswitch
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="port" typ="enum" mandatory="1">用於入口埠 policer 條目的物理埠或 trunk。</ArgTableRow>
<ArgTableRow arg="rate" typ="num" mandatory="1">最大資料速率限制。</ArgTableRow>
<ArgTableRow arg="burst" typ="num">在允許 burst 時能夠傳輸的最大資料速率。</ArgTableRow>
<ArgTableRow arg="meter-unit" typ="enum (bit | packet) { bit:0, packet:1 }">流量入口埠 policer rate 的計量單位。</ArgTableRow>
<ArgTableRow arg="meter-len" typ="enum (layer-1 | layer-2 | layer-3) { layer-1:0, layer-2:1, layer-3:2 }">
設定用於計量的封包位元組長度的封包分類。
- `layer-1` - 包括整個 layer-2 幀 + FCS + 包間間隔 + 前導碼。
- `layer-2` - 包括 layer-2 幀 + FCS。
- `layer-3` - 僅包括 layer-3 + Ethernet 填充，不包括 layer-2 頭和 FCS。
</ArgTableRow>
<ArgTableRow arg="yellow-action" typ="enum (drop | forward | remark) { drop:0, forward:1, remark:2 }">對超出流量執行的動作。</ArgTableRow>
<ArgTableRow arg="new-dei-for-yellow" typ="alt { spcial-dei: enum (remap) { remap:0xffffffff }
, dei: num [ .. 1]
 }">如果 yellow-action 為 remark，則為超出流量重標記的 DEI。</ArgTableRow>
<ArgTableRow arg="new-pcp-for-yellow" typ="alt { special-pcp: enum (remap) { remap:0xffffffff }
, pcp: num [ .. 7]
 }">如果 yellow-action 為 remark，則為超出流量重標記的 PCP。</ArgTableRow>
<ArgTableRow arg="new-dscp-for-yellow" typ="alt { special-dscp: enum (remap) { remap:0xffffffff }
, dscp: num [ .. 63]
 }">如果 yellow-action 為 remark，則為超出流量重標記的 DSCP。</ArgTableRow>
<ArgTableRow arg="packet-types" typ="ubit (arp-or-nd, tcp-control, broadcast, unregistered-multicast, registered-multicast, unknown-unicast, known-unicast)">該入口埠 policer 條目所適用的匹配封包型別。</ArgTableRow>
</ArgTable>
