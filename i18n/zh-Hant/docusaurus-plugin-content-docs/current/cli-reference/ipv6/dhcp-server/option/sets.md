---
sidebar_key: "cli-reference/ipv6/dhcp-server/option/sets"
sidebar_position: 1
title: "sets"
sidebar_label: 'sets'
source: https://manual.mikrotik.com/docs/cli-reference/ipv6/dhcp-server/option/sets
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ipv6/dhcp-server/option/sets {#ipv6dhcp-serveroptionsets}
**型別：** 目錄

可一起分配的 DHCPv6 伺服器選項組。詳情請參閱 [DHCPv6 伺服器](../../../../network-management/dhcp/dhcpv6-server.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1">選項集的名稱。</ArgTableRow>
<ArgTableRow arg="options" typ="multi { array-id, option: enum
 }" mandatory="1">集合中的選項（`/ipv6/dhcp-server/option`）。</ArgTableRow>
</ArgTable>
