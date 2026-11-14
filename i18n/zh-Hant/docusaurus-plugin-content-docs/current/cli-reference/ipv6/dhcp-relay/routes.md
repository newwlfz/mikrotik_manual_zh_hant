---
sidebar_key: "cli-reference/ipv6/dhcp-relay/routes"
sidebar_position: 4
title: "routes"
sidebar_label: 'routes'
source: https://manual.mikrotik.com/docs/cli-reference/ipv6/dhcp-relay/routes
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ipv6/dhcp-relay/routes {#ipv6dhcp-relayroutes}
**型別：** 目錄

DHCPv6 中繼在 `store-relayed-bindings=yes` 時於伺服器回覆中找到的繫結。中繼會為每個委派的字首新增一條經由用戶端的路由。有關詳細資訊，請參閱 [DHCP 中繼](../../../network-management/dhcp/relay.md)。

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="relay" typ="enum">看到該繫結的 DHCPv6 中繼。</ArgTableRow>
<ArgTableRow arg="prefix" typ="ip6Prefix">委派字首或分配的地址。</ArgTableRow>
<ArgTableRow arg="peer-address" typ="ip6Addr">用戶端的地址，通常是其鏈路本地地址，用作該路由的閘道器。</ArgTableRow>
<ArgTableRow arg="life-time" typ="time">繫結的生命週期。</ArgTableRow>
<ArgTableRow arg="last-seen" typ="time">自中繼上次在應答中看到該繫結以來經過的時間。</ArgTableRow>
</ArgTable>
