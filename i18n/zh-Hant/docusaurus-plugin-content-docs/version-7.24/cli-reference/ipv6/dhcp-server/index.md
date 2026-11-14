---
sidebar_key: "cli-reference/ipv6/dhcp-server/index"
sidebar_position: 2
title: "dhcp-server"
sidebar_label: "dhcp-server"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ipv6/dhcp-server
captured_at: '2026-11-01T21:29:05+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ipv6/dhcp-server {#ipv6dhcp-server}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">無效</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="prefix-pool" typ="alt { prefix-pool-static: enum (static-only) { static-only:0xffffffff }
, prefix-pool-name: enum
 }">動態字首繫結將從中獲取字首的地址池</ArgTableRow>
<ArgTableRow arg="address-pool" typ="alt { address-pool-static: enum (static-only) { static-only:0xffffffff }
, address-pool-name: enum
 }">動態地址繫結將從中獲取地址的地址池（池字首長度必須為 128）</ArgTableRow>
<ArgTableRow arg="lease-time" typ="time">新建和延長繫結的持續時間</ArgTableRow>
<ArgTableRow arg="rapid-commit" typ="bool">附加 Rapid Commit 選項，以使用兩包 Solicit-Reply 交換</ArgTableRow>
<ArgTableRow arg="use-radius" typ="enum (no | yes | accounting)">使用 RADIUS 伺服器進行認證</ArgTableRow>
<ArgTableRow arg="preference" typ="num">通告訊息優先順序，伺服器優先順序值最高者優先於其他所有伺服器</ArgTableRow>
<ArgTableRow arg="binding-script" typ="alt { script: string
 }"></ArgTableRow>
<ArgTableRow arg="dhcp-option" typ="multi { array-id, option: alt { option: enum
, option-set: enum
 }
 }"></ArgTableRow>
<ArgTableRow arg="insert-queue-before" typ="enum (first | bottom) { first:0, bottom:0xffffffff }"></ArgTableRow>
<ArgTableRow arg="parent-queue" typ="enum (none) { none:0 }"></ArgTableRow>
<ArgTableRow arg="route-distance" typ="num">路由表中下發的用戶端繫結的距離</ArgTableRow>
<ArgTableRow arg="allow-dual-stack-queue" typ="bool"></ArgTableRow>
<ArgTableRow arg="use-reconfigure" typ="bool"></ArgTableRow>
<ArgTableRow arg="address-lists" typ="multi { array-id, address-list: string
 }">繫結字首/地址將被新增到的地址列表（可由繫結 address-lists 引數覆蓋）</ArgTableRow>
<ArgTableRow arg="ignore-ia-na-bindings" typ="bool">伺服器將忽略用戶端傳送的訊息中的 IA_NA 選項，並視該訊息不包含這些選項</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="duid" typ="string"></ArgTableRow>
</ArgTable>
