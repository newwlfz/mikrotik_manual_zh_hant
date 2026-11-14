---
sidebar_key: "cli-reference/routing/ospf/instance"
sidebar_position: 2
title: "instance"
sidebar_label: "instance"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/routing/ospf/instance
captured_at: '2026-11-01T21:29:35+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/ospf/instance {#routingospfinstance}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未啟用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="version" typ="enum (2 | 3)">此例項將執行的 OSPF 版本（IPv4 使用 v2，IPv6 使用 v3）。</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">此 OSPF 例項所運作的 VRF 表。</ArgTableRow>
<ArgTableRow arg="router-id" typ="alt { ip: ipAddr
, id: enum
 }">OSPF Router ID。可以顯式設定為 IP 地址，或設定為 router-id 例項的名稱。</ArgTableRow>
<ArgTableRow arg="out-filter-select" typ="enum" unset="1">路由過濾器 select 鏈的名稱，用於輸出選擇。輸出僅作用於**外部**路由。</ArgTableRow>
<ArgTableRow arg="out-filter-chain" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="originate-default" typ="enum (never | always | if-installed)" unset="1">指定預設路由（`0.0.0.0/0`）的分發方式。</ArgTableRow>
<ArgTableRow arg="in-filter-chain" typ="enum" unset="1">用於傳入字首的 [路由過濾器](../../../user-guides/routing-and-networking-protocols/route-selection-and-filtering.md#route-filtering) 鏈的名稱。</ArgTableRow>
<ArgTableRow arg="routing-table" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="mpls-te-address" typ="address (flags=64)" unset="1"></ArgTableRow>
<ArgTableRow arg="mpls-te-area" typ="ipAddr" unset="1">用於 MPLS 流量工程的區域。TE Opaque LSA 會在此區域中生成。最多隻能有一個 OSPF 例項配置 `mpls-te-area`。</ArgTableRow>
<ArgTableRow arg="domain-id" typ="address (flags=R)" unset="1">MPLS 相關引數。用於標識該例項的 OSPF 域。此值會作為 BGP 擴展團體屬性附加到在 BGP 中作為 VPNv4 路由重新分發的 OSPF 路由上，並在 BGP VPNv4 路由重新分發回 OSPF 時使用，以確定是為該路由生成 `inter-area` LSA 還是 `AS-external` LSA。預設使用 Null domain-id，如 [RFC 4577](https://tools.ietf.org/html/rfc4577) 所述。</ArgTableRow>
<ArgTableRow arg="domain-tag" typ="num" unset="1">如果設定，則在路由重新分發中使用（作為此路由器生成的所有外部 LSA 中的 route-tag），並在路由計算中使用（所有帶有此路由標籤的外部 LSA 都會被忽略）。與較舊的 Cisco 系統互操作時需要此項。預設不設定。</ArgTableRow>
<ArgTableRow arg="use-dn" typ="bool" unset="1">強制使用或忽略 DN 位。在某些 CE-PE 場景中，可用於將 `intra-area` 路由注入 VRF。如果引數未設定，則按 RFC 規定使用 DN 位。</ArgTableRow>
<ArgTableRow arg="redistribute" typ="ubit (connected, static, rip, ospf, isis, bgp, vpn, dhcp, fantasy, modem, bgp-mpls-vpn, slaac)" unset="1">啟用特定路由型別的重新分發。</ArgTableRow>
</ArgTable>
