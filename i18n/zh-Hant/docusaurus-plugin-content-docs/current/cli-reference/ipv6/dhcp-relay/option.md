---
sidebar_key: "cli-reference/ipv6/dhcp-relay/option"
sidebar_position: 2
title: "option"
sidebar_label: 'option'
source: https://manual.mikrotik.com/docs/cli-reference/ipv6/dhcp-relay/option
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ipv6/dhcp-relay/option {#ipv6dhcp-relayoption}
**型別：** 目錄

DHCPv6 中繼可以新增到其傳送的 Relay-Forward 訊息中的選項。中繼會新增其 `dhcp-options` 屬性中列出的選項。有關詳細資訊，請參閱 [DHCP 中繼](../../../network-management/dhcp/relay.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="*" typ="default">預定義選項。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1">選項名稱，用於中繼的 `dhcp-options` 屬性。</ArgTableRow>
<ArgTableRow arg="code" typ="num" mandatory="1">DHCPv6 選項程式碼。</ArgTableRow>
<ArgTableRow arg="value" typ="string">選項的值，語法與 DHCP 伺服器選項值相同。預定義的 `client_mac` 選項（程式碼 79）使用 `0x0001$(CLIENT_MAC)`，即鏈路層型別 Ethernet 後跟用戶端的 MAC 地址。</ArgTableRow>
<ArgTableRow arg="only-if-mac-available" typ="bool">是否僅當訊息直接來自用戶端（而非來自另一箇中繼）且用戶端的 MAC 地址已知時，才新增該選項。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="raw-value" typ="string">傳送時的選項值，以十六進位制表示。</ArgTableRow>
</ArgTable>
