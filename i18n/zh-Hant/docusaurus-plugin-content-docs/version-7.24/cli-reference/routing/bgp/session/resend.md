---
sidebar_key: "cli-reference/routing/bgp/session/resend"
sidebar_position: 4
title: "resend"
sidebar_label: "resend"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/routing/bgp/session/resend
captured_at: '2026-11-01T21:29:28+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/bgp/session/resend {#routingbgpsessionresend}
**條件：** !smips
**型別：** 命令

向指定的 BGP 會話重新發送字首。該命令接受兩個引數：

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="afi" typ="enum (ip | ipv6 | l2vpn | vpnv4)">指定要為其重新發送字首的地址族。</ArgTableRow>
</ArgTable>
