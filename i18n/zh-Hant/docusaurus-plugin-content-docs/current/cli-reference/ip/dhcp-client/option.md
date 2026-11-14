---
sidebar_key: "cli-reference/ip/dhcp-client/option"
sidebar_position: 1
title: "option"
sidebar_label: 'option'
source: https://manual.mikrotik.com/docs/cli-reference/ip/dhcp-client/option
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/dhcp-client/option {#ipdhcp-clientoption}
**型別：** 目錄

DHCP 用戶端可以傳送給 DHCP 伺服器的選項。用戶端會發送其 `dhcp-options` 屬性中列出的選項。詳情請參閱 [DHCP 用戶端](../../../network-management/dhcp/client.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="*" typ="default">預定義選項。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1">選項的名稱，用於用戶端的 `dhcp-options` 屬性。</ArgTableRow>
<ArgTableRow arg="code" typ="alt { number: num [1 .. 254]
, option: enum (hostname | vendor-specific | vendor-class-id | client-id) { hostname:12, vendor-specific:43, vendor-class-id:60, client-id:61 }
 }" mandatory="1">DHCP 選項程式碼（1-254），或以下名稱之一：`hostname` (12)、`vendor-specific` (43)、`vendor-class-id` (60) 或 `client-id` (61)。</ArgTableRow>
<ArgTableRow arg="value" typ="string">
選項的值，語法與 DHCP 伺服器選項值相同。該值可以包含這些變數：
- `$(HOSTNAME)` - 路由器的標識。
- `$(CLIENT_MAC)` - 用戶端介面的 MAC 地址。
- `$(CLIENT_DUID)` - 路由器的 DUID，與 DHCPv6 用戶端使用的 DUID 相同。
</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="raw-value" typ="string">傳送時的選項值，以十六進位制表示。</ArgTableRow>
</ArgTable>
