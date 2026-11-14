---
sidebar_key: "cli-reference/ipv6/dhcp-relay/index"
sidebar_position: 1
title: "dhcp-relay"
sidebar_label: 'dhcp-relay'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ipv6/dhcp-relay
captured_at: '2026-11-01T21:24:32+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ipv6/dhcp-relay {#ipv6dhcp-relay}
**型別：** 目錄

DHCPv6 中繼會將其介面上來自用戶端的 DHCPv6 訊息封裝在 Relay-Forward 訊息中轉發給 DHCPv6 伺服器，並將伺服器的 Relay-Reply 訊息傳回用戶端。有關概述，請參閱 [DHCP 中繼](../../../network-management/dhcp/relay.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">中繼已停用。</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">中繼配置無效。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1">中繼的名稱。</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">中繼用於偵聽用戶端訊息的介面。</ArgTableRow>
<ArgTableRow arg="dhcp-server" typ="object { server: alt { interface-address: composite { address6: ip6Addr
, interface: iface_enum
 }
, address6: ip6Addr
 }
 }" mandatory="1">要將 Relay-Forward 訊息轉發到的 DHCPv6 伺服器。鏈路本地地址需與其介面一起指定，例如 `fe80::1%ether1`。</ArgTableRow>
<ArgTableRow arg="dhcp-options" typ="multi { array-id, option: enum
 }">新增到 Relay-Forward 訊息的選項（`/ipv6/dhcp-relay/option`）。始終會新增 Interface-ID 選項 (18)。預設值：client_mac，即用戶端鏈路層地址（選項 79）。</ArgTableRow>
<ArgTableRow arg="link-address" typ="ip6Addr">在 Relay-Forward 訊息的 link-address 欄位中傳送的地址，伺服器可用它來識別用戶端所在的鏈路。使用 `::` 時不傳送地址。預設值：::。</ArgTableRow>
<ArgTableRow arg="delay-threshold" typ="alt { const: enum (none) { none:0 }
, time: time
 }">訊息要被轉發所必須具有的 elapsed-time 欄位最小值。使用 `none` 時，所有訊息都會被轉發。預設值：none。</ArgTableRow>
<ArgTableRow arg="store-relayed-bindings" typ="bool">是否保留伺服器回覆中找到的繫結，並透過用戶端為其新增路由，以便發往中繼後面委派字首的流量能夠被路由。這些繫結列在 `/ipv6/dhcp-relay/routes` 中。預設值：no。</ArgTableRow>
</ArgTable>
