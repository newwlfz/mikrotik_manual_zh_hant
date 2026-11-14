---
sidebar_key: "cli-reference/ip/dhcp-server/network"
sidebar_position: 5
title: "network"
sidebar_label: 'network'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/dhcp-server/network
captured_at: '2026-11-01T21:23:52+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/dhcp-server/network {#ipdhcp-servernetwork}
**型別：** 目錄

傳送給 DHCP 用戶端的設定。伺服器會把包含用戶端地址的網路條目的設定傳送給用戶端。詳情請參閱 [DHCP 伺服器](../../../network-management/dhcp/server.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="D" typ="dynamic">該網路是動態建立的。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="address" typ="composite { address: ipAddr
, netmask: num [ .. 32]
 }">此條目適用的網路，例如 `192.168.88.0/24`。</ArgTableRow>
<ArgTableRow arg="gateway" typ="multi { address: ipAddr
 }">傳送給用戶端的預設閘道器（選項 3）。可以列出多個閘道器。</ArgTableRow>
<ArgTableRow arg="netmask" typ="num">當子網掩碼需要與 `address` 的掩碼不同時，以字首長度形式傳送給用戶端的子網掩碼。使用 `0` 時，將使用 `address` 的掩碼。</ArgTableRow>
<ArgTableRow arg="dns-server" typ="alt { server: multi { address: ipAddr
 }
 }">傳送給用戶端的 DNS 伺服器（選項 6）。未設定時，伺服器會發送路由器自身使用的 DNS 伺服器（`/ip/dns`）。</ArgTableRow>
<ArgTableRow arg="dns-none" typ="bool">是否完全不傳送 DNS 伺服器，連路由器自身的 DNS 伺服器也不傳送。預設值：no。</ArgTableRow>
<ArgTableRow arg="wins-server" typ="multi { address: ipAddr
 }">傳送給用戶端的 WINS 伺服器（選項 44）。</ArgTableRow>
<ArgTableRow arg="ntp-server" typ="alt { server: multi { address: ipAddr
 }
 }">傳送給用戶端的 NTP 伺服器（選項 42）。未設定時，伺服器會發送路由器自身使用的 NTP 伺服器。</ArgTableRow>
<ArgTableRow arg="ntp-none" typ="bool">是否完全不傳送 NTP 伺服器，連路由器自身的 NTP 伺服器也不傳送。預設值：no。</ArgTableRow>
<ArgTableRow arg="caps-manager" typ="multi { address: ipAddr
 }">傳送給用戶端的 CAPsMAN 地址（選項 138）。</ArgTableRow>
<ArgTableRow arg="domain" typ="string">傳送給用戶端的域名（選項 15）。</ArgTableRow>
<ArgTableRow arg="next-server" typ="ipAddr">用於網路引導下一步的伺服器地址，在 `siaddr` 欄位中傳送，例如 TFTP 伺服器。未設定時，將傳送 DHCP 伺服器的地址。</ArgTableRow>
<ArgTableRow arg="boot-file-name" typ="string">用於網路引導的引導檔名，在 `file` 欄位中傳送。</ArgTableRow>
<ArgTableRow arg="dhcp-option" typ="multi { array-id, option: enum
 }">在此網路中傳送給用戶端的選項（`/ip/dhcp-server/option`）。伺服器和租約的選項優先。</ArgTableRow>
<ArgTableRow arg="dhcp-option-set" typ="enum (none)">在此網路中傳送給用戶端的選項集（`/ip/dhcp-server/option/sets`）。伺服器和租約的選項優先。</ArgTableRow>
</ArgTable>
