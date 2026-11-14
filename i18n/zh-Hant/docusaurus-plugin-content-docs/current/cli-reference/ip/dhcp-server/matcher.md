---
sidebar_key: "cli-reference/ip/dhcp-server/matcher"
sidebar_position: 4
title: "matcher"
sidebar_label: 'matcher'
source: https://manual.mikrotik.com/docs/cli-reference/ip/dhcp-server/matcher
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/dhcp-server/matcher {#ipdhcp-servermatcher}
**型別：** 目錄

從特定 IP 池向請求中包含匹配 DHCP 選項（例如供應商類識別符號或主機名）的用戶端分配地址。具有靜態租約的用戶端即使被匹配器匹配，也會保留其靜態租約。有關示例，請參見 [DHCP 伺服器](../../../network-management/dhcp/server.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">匹配器已停用。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1">匹配器的名稱。</ArgTableRow>
<ArgTableRow arg="server" typ="enum (all)" mandatory="1">匹配器適用的 DHCP 伺服器，或使用 `all` 表示所有伺服器。</ArgTableRow>
<ArgTableRow arg="address-pool" typ="enum (static-only)">用於為匹配用戶端分配地址的 IP 池。</ArgTableRow>
<ArgTableRow arg="option-set" typ="enum (none)">要傳送給匹配用戶端的選項集（`/ip/dhcp-server/option/sets`）。</ArgTableRow>
<ArgTableRow arg="code" typ="alt { number: num [1 .. 254]
, option: enum (vendor-specific) { vendor-specific:43 }
 }" mandatory="1">要匹配的 DHCP 選項程式碼（1-254）。</ArgTableRow>
<ArgTableRow arg="value" typ="string" mandatory="1">要在選項中查詢的值，可以是文字，也可以是帶 `0x` 字首的十六進位制值。</ArgTableRow>
<ArgTableRow arg="matching-type" typ="enum (exact | substring)" mandatory="1">
`value` 與選項的比較方式：
- `exact` - 選項必須等於 `value`。
- `substring` - `value` 可以出現在選項中的任意位置。

當兩個 substring 匹配器匹配同一個選項時，應用哪一個匹配器是隨機的。
</ArgTableRow>
</ArgTable>
