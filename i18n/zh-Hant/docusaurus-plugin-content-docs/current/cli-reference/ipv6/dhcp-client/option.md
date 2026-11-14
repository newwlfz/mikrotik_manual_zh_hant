---
sidebar_key: "cli-reference/ipv6/dhcp-client/option"
sidebar_position: 1
title: "option"
sidebar_label: 'option'
source: https://manual.mikrotik.com/docs/cli-reference/ipv6/dhcp-client/option
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ipv6/dhcp-client/option {#ipv6dhcp-clientoption}
**型別：** 目錄

DHCPv6 用戶端可傳送給 DHCPv6 伺服器的選項。用戶端會發送其 `dhcp-options` 屬性中列出的選項。詳情請參見 [DHCPv6 用戶端](../../../network-management/dhcp/dhcpv6-client.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="*" typ="default">預定義選項。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1">選項的名稱，用於用戶端的 `dhcp-options` 屬性。</ArgTableRow>
<ArgTableRow arg="code" typ="num" mandatory="1">DHCPv6 選項程式碼。</ArgTableRow>
<ArgTableRow arg="value" typ="string">選項的值，語法與 DHCP 伺服器選項值相同。預定義的 `fqdn` 選項使用變數 `$(HOSTNAME)`（路由器的身份）和 `$(HOSTNAME_LEN)`（其長度）：`0x00$(HOSTNAME_LEN)$(HOSTNAME)`。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="raw-value" typ="string">傳送時的選項值，以十六進位制表示。</ArgTableRow>
</ArgTable>
