---
sidebar_key: "cli-reference/routing/isis/instance"
sidebar_position: 1
title: "instance"
sidebar_label: 'instance'
source: https://manual.mikrotik.com/docs/cli-reference/routing/isis/instance
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/isis/instance {#routingisisinstance}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未啟用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="vrf" typ="enum"></ArgTableRow>
<ArgTableRow arg="afi" typ="ubit (ip, ipv6)"></ArgTableRow>
<ArgTableRow arg="system-id" typ="string"></ArgTableRow>
<ArgTableRow arg="areas" typ="multi { area: string
 }"></ArgTableRow>
<ArgTableRow arg="areas-max" typ="num"></ArgTableRow>
<ArgTableRow arg="in-filter-chain" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="metric-type" typ="enum (old | wide | both)" unset="1"></ArgTableRow>
<ArgTableRow arg="l1.redistribute" typ="ubit (connected, static, rip, ospf, bgp, vpn, dhcp, fantasy, modem, bgp-mpls-vpn, slaac)" unset="1"></ArgTableRow>
<ArgTableRow arg="l1.out-filter-select" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="l1.out-filter-chain" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="l1.originate-default" typ="enum (never | always | if-installed)" unset="1"></ArgTableRow>
<ArgTableRow arg="l1.lsp-max-size" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l1.lsp-max-age" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l1.lsp-update-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l1.lsp-refresh-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l2.redistribute" typ="ubit (connected, static, rip, ospf, bgp, vpn, dhcp, fantasy, modem, bgp-mpls-vpn, slaac)" unset="1"></ArgTableRow>
<ArgTableRow arg="l2.out-filter-select" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="l2.out-filter-chain" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="l2.originate-default" typ="enum (never | always | if-installed)" unset="1"></ArgTableRow>
<ArgTableRow arg="l2.lsp-max-size" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l2.lsp-max-age" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l2.lsp-update-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l2.lsp-refresh-interval" typ="num" unset="1"></ArgTableRow>
</ArgTable>
