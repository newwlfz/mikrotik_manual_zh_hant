---
sidebar_key: "cli-reference/routing/bgp/session/refresh"
sidebar_position: 3
title: "refresh"
sidebar_label: 'refresh'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/routing/bgp/session/refresh
captured_at: '2026-11-01T21:25:06+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/bgp/session/refresh {#routingbgpsessionrefresh}
**條件：** !smips
**型別：** 命令

向指定的 BGP 會話傳送路由重新整理。用於觸發從遠端對等體重新發送所有路由。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="afi" typ="enum (ip | ipv6 | l2vpn | vpnv4)">指定要為其傳送路由重新整理的地址族。</ArgTableRow>
</ArgTable>
