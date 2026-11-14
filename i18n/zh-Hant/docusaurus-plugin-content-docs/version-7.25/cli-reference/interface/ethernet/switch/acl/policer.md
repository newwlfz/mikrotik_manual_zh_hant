---
sidebar_key: "cli-reference/interface/ethernet/switch/acl/policer"
sidebar_position: 1
title: "policer"
sidebar_label: 'policer'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/ethernet/switch/acl/policer
captured_at: '2026-11-01T21:22:33+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/acl/policer {#interfaceethernetswitchaclpolicer}
**系統能力：** musicswitch
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">ACL 中使用的 Policer 名稱。</ArgTableRow>
<ArgTableRow arg="yellow-rate" typ="num" mandatory="1">黃色丟棄優先順序封包的最大資料速率限制。</ArgTableRow>
<ArgTableRow arg="yellow-burst" typ="num">對於黃色丟棄優先順序封包，在允許突發期間可傳輸的最大資料速率。</ArgTableRow>
<ArgTableRow arg="red-rate" typ="num">紅色丟棄優先順序封包的最大資料速率限制。</ArgTableRow>
<ArgTableRow arg="red-burst" typ="num">對於紅色丟棄優先順序封包，在允許突發期間可傳輸的最大資料速率。</ArgTableRow>
<ArgTableRow arg="meter-unit" typ="enum (bit | packet) { bit:0, packet:1 }">ACL 流量速率的計量單位。</ArgTableRow>
<ArgTableRow arg="meter-len" typ="enum (layer-1 | layer-2 | layer-3) { layer-1:0, layer-2:1, layer-3:2 }">
設定計量所用封包位元組長度的封包分類。
- `layer-1` - 包括整個 layer-2 幀 + FCS + 封包間間隔 + 前導碼。
- `layer-2` - 包括 layer-2 幀 + FCS。
- `layer-3` - 僅包括 layer-3 + ethernet 填充，不包括 layer-2 頭和 FCS。
</ArgTableRow>
<ArgTableRow arg="color-awareness" typ="bool">
`yes` - 使 policer 考慮預先著色的丟棄優先順序。
`no` - 忽略丟棄優先順序。
</ArgTableRow>
<ArgTableRow arg="bucket-coupling" typ="bool"></ArgTableRow>
<ArgTableRow arg="yellow-action" typ="enum (drop | forward | remark) { drop:0, forward:1, remark:2 }">對具有黃色丟棄優先順序的超額流量執行的操作。</ArgTableRow>
<ArgTableRow arg="new-dei-for-yellow" typ="alt { spcial-dei: enum (remap) { remap:0xffffffff }
, dei: num [ .. 1]
 }">黃色丟棄優先順序封包的新 DEI。</ArgTableRow>
<ArgTableRow arg="new-pcp-for-yellow" typ="alt { special-pcp: enum (remap) { remap:0xffffffff }
, pcp: num [ .. 7]
 }">黃色丟棄優先順序封包的新 PCP。</ArgTableRow>
<ArgTableRow arg="new-dscp-for-yellow" typ="alt { special-dscp: enum (remap) { remap:0xffffffff }
, dscp: num [ .. 63]
 }">黃色丟棄優先順序封包的新 DSCP。</ArgTableRow>
<ArgTableRow arg="red-action" typ="enum (drop | forward | remark) { drop:0, forward:1, remark:2 }">對具有紅色丟棄優先順序的超額流量執行的操作。</ArgTableRow>
<ArgTableRow arg="new-dei-for-red" typ="alt { spcial-dei: enum (remap) { remap:0xffffffff }
, dei: num [ .. 1]
 }">紅色丟棄優先順序封包的新 DEI。</ArgTableRow>
<ArgTableRow arg="new-pcp-for-red" typ="alt { special-pcp: enum (remap) { remap:0xffffffff }
, pcp: num [ .. 7]
 }">紅色丟棄優先順序封包的新 PCP。</ArgTableRow>
<ArgTableRow arg="new-dscp-for-red" typ="alt { special-dscp: enum (remap) { remap:0xffffffff }
, dscp: num [ .. 63]
 }">紅色丟棄優先順序封包的新 DSCP。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="green-counter" typ="num"></ArgTableRow>
<ArgTableRow arg="yellow-counter" typ="num"></ArgTableRow>
<ArgTableRow arg="red-counter" typ="num"></ArgTableRow>
</ArgTable>
