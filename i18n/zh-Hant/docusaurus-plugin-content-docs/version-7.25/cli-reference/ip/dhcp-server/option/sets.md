---
sidebar_key: "cli-reference/ip/dhcp-server/option/sets"
sidebar_position: 1
title: "sets"
sidebar_label: 'sets'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/dhcp-server/option/sets
captured_at: '2026-11-01T21:23:53+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/dhcp-server/option/sets {#ipdhcp-serveroptionsets}
**型別：** 目錄

DHCP 伺服器選項組可透過 `dhcp-option-set` 一起分配給網路、伺服器、租約或匹配器。詳情請參閱 [DHCP 伺服器](../../../../network-management/dhcp/server.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1">選項集的名稱。</ArgTableRow>
<ArgTableRow arg="options" typ="multi { array-id, option: enum
 }" mandatory="1">集合中的選項（`/ip/dhcp-server/option`）。</ArgTableRow>
</ArgTable>
