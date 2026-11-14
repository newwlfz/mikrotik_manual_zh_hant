---
sidebar_key: "cli-reference/ip/dhcp-server/option"
title: "option"
sidebar_label: 'option'
source: https://manual.mikrotik.com/docs/cli-reference/ip/dhcp-server/option
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/dhcp-server/option {#ipdhcp-serveroption}
**型別：** 目錄

DHCP 伺服器可以傳送的額外選項。使用 `dhcp-option` 將它們分配給網路、伺服器或租約，或將它們分組到選項集中。當在多個層級設定同一選項時，租約優先於伺服器，伺服器優先於網路。有關示例，請參閱 [DHCP 伺服器](../../../../network-management/dhcp/server.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1">選項的名稱，在分配選項時使用。</ArgTableRow>
<ArgTableRow arg="code" typ="alt { number: num [1 .. 254]
, option: enum (vendor-specific) { vendor-specific:43 }
 }" mandatory="1">DHCP 選項程式碼（1-254）。</ArgTableRow>
<ArgTableRow arg="value" typ="string">
選項的值。該值會根據其書寫方式轉換：
- `'test'` - 引號中的文字會作為文字傳送（`74657374`）。
- `'10.10.10.10'` - 引號中的 IP 地址會作為四個位元組傳送（`0a0a0a0a`）。
- `s'10.10.10.10'` - 使用 `s` 字首時，該值始終作為文字傳送（`31302e31302e31302e3130`）。
- `'10'` - 引號中的數字會作為一個位元組傳送（`0a`）。
- `0x0a0a` - 十六進位制值會按原樣傳送。

各部分可以組合，例如 `0x01'vards'$(HOSTNAME)`。可以使用以下變數：
- `$(HOSTNAME)` - 路由器的標識。
- `$(NETWORK_GATEWAY)` - 匹配網路（`/ip/dhcp-server/network`）的第一個閘道器，在傳送選項時填入。
- `$(RADIUS_MT_STR1)`、`$(RADIUS_MT_STR2)` - MikroTik RADIUS 屬性 24 和 25。
- `$(REMOTE_ID)` - 中繼代理資訊（選項 82）的遠端 ID。
</ArgTableRow>
<ArgTableRow arg="force" typ="bool">即使用戶端未在其引數請求列表（選項 55）中請求該選項，是否也傳送它。如果不啟用此項，則僅向請求該選項的用戶端傳送。預設：否。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="raw-value" typ="string">傳送時的選項值（十六進位制）。依賴用戶端或網路的變數僅在傳送該選項時填入。</ArgTableRow>
</ArgTable>
