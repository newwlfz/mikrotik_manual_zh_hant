---
sidebar_key: "cli-reference/ipv6/dhcp-client/index"
sidebar_position: 1
title: "dhcp-client"
sidebar_label: "dhcp-client"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ipv6/dhcp-client
captured_at: '2026-11-01T21:29:03+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ipv6/dhcp-client {#ipv6dhcp-client}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">無效</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="request" typ="ubit (info, address, prefix)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="accept-prefix-without-address" typ="bool">即使未提供地址也接受字首（僅在同時請求了地址和字首時應用）</ArgTableRow>
<ArgTableRow arg="add-default-route" typ="bool">定義是否將預設路由新增到 DHCP 伺服器（如果響應經過中繼，則新增到直接中繼）</ArgTableRow>
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
<ArgTableRow arg="use-peer-dns" typ="bool">是否接受 DHCP 伺服器通告的 DNS 設定</ArgTableRow>
<ArgTableRow arg="use-interface-duid" typ="bool">使用根據當前介面 MAC 生成的 DUID</ArgTableRow>
<ArgTableRow arg="custom-duid" typ="string">用作用戶端 DUID，覆蓋 use-interface-duid</ArgTableRow>
<ArgTableRow arg="validate-server-duid" typ="bool"></ArgTableRow>
<ArgTableRow arg="rapid-commit" typ="bool">如有可能，使用 Rapid Commit</ArgTableRow>
<ArgTableRow arg="allow-reconfigure" typ="bool"></ArgTableRow>
<ArgTableRow arg="dhcp-options" typ="multi { array-id, option: enum
 }"></ArgTableRow>
<ArgTableRow arg="pool-name" typ="string">從接收到的字首建立的地址池名稱（僅在請求了字首時應用）</ArgTableRow>
<ArgTableRow arg="pool-prefix-length" typ="num">從接收到的字首建立的地址池的字首長度（僅在請求了字首時應用）；如果未設定，將自動確定字首長度</ArgTableRow>
<ArgTableRow arg="prefix-hint" typ="ip6Prefix"></ArgTableRow>
<ArgTableRow arg="prefix-address-lists" typ="multi { array-id, prefix-address-list: string
 }">接收到的字首將新增到的地址列表（僅在請求了字首時應用）</ArgTableRow>
<ArgTableRow arg="script" typ="alt { script: string
 }"></ArgTableRow>
<ArgTableRow arg="custom-iapd-id" typ="num"></ArgTableRow>
<ArgTableRow arg="custom-iana-id" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="status" typ="enum (stopped | searching... | requesting... | bound | renewing... | rebinding... | stopping... | declining... | error | idle | requesting-info... | confirming...)"></ArgTableRow>
<ArgTableRow arg="duid" typ="string"></ArgTableRow>
<ArgTableRow arg="dhcp-server-v6" typ="ip6Addr"></ArgTableRow>
<ArgTableRow arg="prefix" typ="composite { prefix: ip6Prefix
, expires-after: time
 }"></ArgTableRow>
<ArgTableRow arg="address" typ="composite { address: ip6Addr
, expires-after: time
 }"></ArgTableRow>
<ArgTableRow arg="reconfigure-key" typ="string"></ArgTableRow>
<ArgTableRow arg="reconfigure-last-counter" typ="string"></ArgTableRow>
</ArgTable>
