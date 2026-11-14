---
sidebar_key: "cli-reference/ip/dhcp-server/network"
sidebar_position: 5
title: "network"
sidebar_label: "network"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/dhcp-server/network
captured_at: '2026-11-01T21:28:31+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/dhcp-server/network {#ipdhcp-servernetwork}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="address" typ="composite { address: ipAddr
, netmask: num [ .. 32]
 }"></ArgTableRow>
<ArgTableRow arg="gateway" typ="multi { address: ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="netmask" typ="num"></ArgTableRow>
<ArgTableRow arg="dns-server" typ="alt { server: multi { address: ipAddr
 }
 }"></ArgTableRow>
<ArgTableRow arg="dns-none" typ="bool">不會向用戶端傳送任何伺服器</ArgTableRow>
<ArgTableRow arg="wins-server" typ="multi { address: ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="ntp-server" typ="alt { server: multi { address: ipAddr
 }
 }"></ArgTableRow>
<ArgTableRow arg="ntp-none" typ="bool">不會向用戶端傳送任何伺服器</ArgTableRow>
<ArgTableRow arg="caps-manager" typ="multi { address: ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="domain" typ="string"></ArgTableRow>
<ArgTableRow arg="next-server" typ="ipAddr">用於下一個引導步驟的 siaddr</ArgTableRow>
<ArgTableRow arg="boot-file-name" typ="string"></ArgTableRow>
<ArgTableRow arg="dhcp-option" typ="multi { array-id, option: enum
 }"></ArgTableRow>
<ArgTableRow arg="dhcp-option-set" typ="enum (none)"></ArgTableRow>
</ArgTable>
