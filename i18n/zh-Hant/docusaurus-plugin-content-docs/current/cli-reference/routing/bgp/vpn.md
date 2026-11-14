---
sidebar_key: "cli-reference/routing/bgp/vpn"
sidebar_position: 8
title: "vpn"
sidebar_label: 'vpn'
source: https://manual.mikrotik.com/docs/cli-reference/routing/bgp/vpn
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/bgp/vpn {#routingbgpvpn}
**條件：** !smips
**型別：** 目錄

L3VPN VPNv4/VPNv6 例項配置

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未啟用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="instance" typ="enum" mandatory="1">此 VPN 分配到的例項名稱。</ArgTableRow>
<ArgTableRow arg="route-distinguisher" typ="string" mandatory="1">指定附加到路由的值，以便接收路由器能夠區分否則可能看起來相同的通告。用於區分使用重疊 IP 範圍的租戶。還可用於簡化 Virtual Network 內的收斂和冗餘。來自 MLAG 對的 RD 也應唯一。</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum" mandatory="1">此 VPN 例項將使用的 VRF 表名稱。</ArgTableRow>
<ArgTableRow arg="label-allocation-policy" typ="enum (per-vrf | per-prefix)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="import.route-targets" typ="object { route-target: address (flags=R)
 }" unset="1">將用於匯入 VPNv4 路由的路由目標列表。接受的 RT 格式與路由區分符的格式類似。</ArgTableRow>
<ArgTableRow arg="export.route-targets" typ="object { route-target: address (flags=R)
 }" unset="1">匯出 VPNv4 路由時新增的路由目標列表。接受的 RT 格式與路由區分符的格式類似。</ArgTableRow>
<ArgTableRow arg="import.filter-chain" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="export.filter-select" typ="enum" unset="1">用於選擇要匯出的字首的 `routing/filter/select-chain` 名稱。</ArgTableRow>
<ArgTableRow arg="export.filter-chain" typ="enum" unset="1">用於在匯出前過濾字首的 `routing/filter/chain` 名稱。</ArgTableRow>
<ArgTableRow arg="export.redistribute" typ="ubit (connected, static, rip, ospf, isis, bgp, vpn, dhcp, fantasy, modem, slaac)" unset="1">啟用將指定路由型別從 VRF 重分發到 VPNv4。</ArgTableRow>
</ArgTable>
