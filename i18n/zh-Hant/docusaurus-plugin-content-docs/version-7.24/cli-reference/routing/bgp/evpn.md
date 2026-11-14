---
sidebar_key: "cli-reference/routing/bgp/evpn"
sidebar_position: 3
title: "evpn"
sidebar_label: "evpn"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/routing/bgp/evpn
captured_at: '2026-11-01T21:29:27+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/bgp/evpn {#routingbgpevpn}
**條件：** !smips
**型別：** 目錄

請參閱 EVPN 文件。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="instance" typ="enum" mandatory="1">此 EVPN 分配到的 BGP 例項。</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum" unset="1">此 EVPN 例項將使用的 VRF 表的名稱。</ArgTableRow>
<ArgTableRow arg="rd" typ="address (flags=R)" unset="1">指定附加到路由的值，以便接收路由器能夠區分在其他情況下可能看起來相同的通告。用於區分使用重疊 IP 範圍的租戶。還可用於簡化虛擬網路內的收斂和冗餘。來自 MLAG 對的 RD 也必須唯一。</ArgTableRow>
<ArgTableRow arg="vni" typ="object { range: range
 }" unset="1">虛擬網路識別符號的範圍。</ArgTableRow>
<ArgTableRow arg="import.route-targets" typ="object { route-target: address (flags=R)
 }" unset="1">將用於匯入 EVPN 路由的路由目標列表。</ArgTableRow>
<ArgTableRow arg="export.route-targets" typ="object { route-target: address (flags=R)
 }" unset="1">匯出時將新增到 EVPN 路由的路由目標列表。</ArgTableRow>
</ArgTable>
