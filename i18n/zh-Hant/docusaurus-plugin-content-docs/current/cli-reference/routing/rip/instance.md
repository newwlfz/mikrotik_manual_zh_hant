---
sidebar_key: "cli-reference/routing/rip/instance"
sidebar_position: 1
title: "instance"
sidebar_label: 'instance'
source: https://manual.mikrotik.com/docs/cli-reference/routing/rip/instance
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/rip/instance {#routingripinstance}
**型別：** 目錄

RIP 路由的最大度量值為 15。高於 15 的度量值會被視為 'infinity'，具有此類度量值的路由會被視為不可達。因此，RIP 不能用於任意兩臺路由器之間跳數超過 15 的網路，而使用大於 1 的 redistribute 度量值會進一步降低這一最大跳數。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">例項的名稱。</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">用於連線的 VRF 名稱。</ArgTableRow>
<ArgTableRow arg="afi" typ="enum (ip | ipv6)"></ArgTableRow>
<ArgTableRow arg="in-filter-chain" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="out-filter-select" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="out-filter-chain" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="redistribute" typ="ubit (connected, static, rip, ospf, isis, bgp, vpn, dhcp, fantasy, modem, bgp-mpls-vpn, slaac)" unset="1"></ArgTableRow>
<ArgTableRow arg="originate-default" typ="enum (never | always | if-installed)" unset="1">是否生成預設路由。</ArgTableRow>
<ArgTableRow arg="route-timeout" typ="num">指定路由被視為無效之前的時間間隔。</ArgTableRow>
<ArgTableRow arg="route-gc-timeout" typ="num"></ArgTableRow>
<ArgTableRow arg="update-interval" typ="num"></ArgTableRow>
<ArgTableRow arg="routing-table" typ="enum" unset="1">將安裝路由的路由表名稱。</ArgTableRow>
</ArgTable>
