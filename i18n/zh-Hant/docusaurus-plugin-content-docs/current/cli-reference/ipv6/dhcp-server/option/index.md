---
sidebar_key: "cli-reference/ipv6/dhcp-server/option"
title: "option"
sidebar_label: 'option'
source: https://manual.mikrotik.com/docs/cli-reference/ipv6/dhcp-server/option
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ipv6/dhcp-server/option {#ipv6dhcp-serveroption}
**型別：** 目錄

DHCPv6 伺服器可以傳送的附加選項，透過 `dhcp-option` 分配給伺服器或繫結，或分組到選項集中。詳情請參閱 [DHCPv6 伺服器](../../../../network-management/dhcp/dhcpv6-server.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1">選項的名稱，在分配選項時使用。</ArgTableRow>
<ArgTableRow arg="code" typ="num" mandatory="1">DHCPv6 選項程式碼，例如 23 表示 DNS 伺服器。</ArgTableRow>
<ArgTableRow arg="value" typ="string">選項的值，語法與 DHCP 伺服器選項值相同。帶引號的 IPv6 地址會以 16 位元組傳送，例如 `'2001:db8::53'`。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="raw-value" typ="string">傳送時的選項值，以十六進位制表示。</ArgTableRow>
</ArgTable>
