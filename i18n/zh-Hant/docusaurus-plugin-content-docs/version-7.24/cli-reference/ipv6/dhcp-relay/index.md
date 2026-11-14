---
sidebar_key: "cli-reference/ipv6/dhcp-relay/index"
sidebar_position: 1
title: "dhcp-relay"
sidebar_label: "dhcp-relay"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ipv6/dhcp-relay
captured_at: '2026-11-01T21:29:03+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ipv6/dhcp-relay {#ipv6dhcp-relay}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">無效</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">中繼將監聽來自此介面上用戶端的訊息</ArgTableRow>
<ArgTableRow arg="dhcp-server" typ="object { server: alt { interface-address: composite { address6: ip6Addr
, interface: iface_enum
 }
, address6: ip6Addr
 }
 }" mandatory="1">中繼訊息將被轉發到的伺服器</ArgTableRow>
<ArgTableRow arg="dhcp-options" typ="multi { array-id, option: enum
 }">新增到 Relay-Forward 訊息中的選項。注意，option 18 (interface-id) 會自動新增，以便中繼能夠正確中繼回覆訊息。</ArgTableRow>
<ArgTableRow arg="link-address" typ="ip6Addr"></ArgTableRow>
<ArgTableRow arg="delay-threshold" typ="alt { const: enum (none) { none:0 }
, time: time
 }">如果 DHCP 封包中的 secs 欄位小於 delay-threshold，則忽略此封包</ArgTableRow>
<ArgTableRow arg="store-relayed-bindings" typ="bool">將路由新增到回覆訊息中找到的有效繫結</ArgTableRow>
</ArgTable>
