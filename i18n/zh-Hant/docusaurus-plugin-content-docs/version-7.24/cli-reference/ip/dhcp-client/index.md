---
sidebar_key: "cli-reference/ip/dhcp-client/index"
sidebar_position: 1
title: "dhcp-client"
sidebar_label: "dhcp-client"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/dhcp-client
captured_at: '2026-11-01T21:28:25+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/dhcp-client {#ipdhcp-client}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">無效</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="add-default-route" typ="enum (no | yes | special-classless)"></ArgTableRow>
<ArgTableRow arg="default-route-distance" typ="num"></ArgTableRow>
<ArgTableRow arg="default-route-tables" typ="object { table: alt { table-distance: composite { table: alt { table-default: enum (default) { default:0xffffffff }
, table: enum
 }
, distance: num [1 .. 255]
 }
, table: alt { table-default: enum (default) { default:0xffffffff }
, table: enum
 }
 }
 }"></ArgTableRow>
<ArgTableRow arg="check-gateway" typ="enum (none | arp | ping | bfd)"></ArgTableRow>
<ArgTableRow arg="use-peer-dns" typ="bool"></ArgTableRow>
<ArgTableRow arg="use-peer-ntp" typ="bool"></ArgTableRow>
<ArgTableRow arg="allow-reconfigure" typ="bool"></ArgTableRow>
<ArgTableRow arg="vlan-priority" typ="num">傳出封包的優先順序；僅適用於 VLAN 介面</ArgTableRow>
<ArgTableRow arg="dscp" typ="num">傳出封包的 DSCP</ArgTableRow>
<ArgTableRow arg="use-broadcast" typ="enum (always | never | both)">控制 DHCPDISCOVER 和 DHCPREQUEST 訊息的 BROADCAST 標誌（僅在請求和重新繫結期間）</ArgTableRow>
<ArgTableRow arg="dhcp-options" typ="multi { array-id, option: enum
 }"></ArgTableRow>
<ArgTableRow arg="script" typ="alt { script: string
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="custom-source-mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="custom-hostname-suffix" typ="string"></ArgTableRow>
<ArgTableRow arg="status" typ="enum (stopped | searching... | requesting... | bound | renewing... | rebinding... | error) { stopped:0, searching...:1, requesting...:2, bound:3, renewing...:4, rebinding...:5, error:6 }"></ArgTableRow>
<ArgTableRow arg="address" typ="composite { address: ipAddr
, netmask: num [ .. 32]
 }"></ArgTableRow>
<ArgTableRow arg="netmask" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="gateway" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="dhcp-server" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="primary-dns" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="secondary-dns" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="primary-ntp" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="secondary-ntp" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="caps-managers" typ="multi { ip: ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="reconfigure-key" typ="string"></ArgTableRow>
<ArgTableRow arg="reconfigure-last-counter" typ="string"></ArgTableRow>
<ArgTableRow arg="expires-after" typ="time"></ArgTableRow>
</ArgTable>
