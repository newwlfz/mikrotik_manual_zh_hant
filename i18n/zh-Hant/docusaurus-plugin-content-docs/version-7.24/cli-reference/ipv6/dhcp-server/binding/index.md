---
sidebar_key: "cli-reference/ipv6/dhcp-server/binding/index"
sidebar_position: 1
title: "binding"
sidebar_label: "binding"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ipv6/dhcp-server/binding
captured_at: '2026-11-01T21:29:04+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ipv6/dhcp-server/binding {#ipv6dhcp-serverbinding}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="I" typ="invalid">無效</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="R" typ="radius">radius</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="address" typ="alt { prefix: ip6Prefix
 }">為用戶端分配單個地址或字首</ArgTableRow>
<ArgTableRow arg="duid" typ="string" mandatory="1">十六進位制字串</ArgTableRow>
<ArgTableRow arg="iaid" typ="num" mandatory="1"></ArgTableRow>
<ArgTableRow arg="ia-type" typ="enum (na | pd)"></ArgTableRow>
<ArgTableRow arg="server" typ="enum (all)">可向用戶端提供此繫結的伺服器名稱</ArgTableRow>
<ArgTableRow arg="life-time" typ="time"></ArgTableRow>
<ArgTableRow arg="prefix-pool" typ="enum">對於地址，使用字首長度為 128 的地址池</ArgTableRow>
<ArgTableRow arg="dhcp-option" typ="multi { array-id, option: alt { option: enum
, option-set: enum
 }
 }"></ArgTableRow>
<ArgTableRow arg="rate-limit" typ="string">用戶端的位元率限制</ArgTableRow>
<ArgTableRow arg="allow-dual-stack-queue" typ="bool"></ArgTableRow>
<ArgTableRow arg="address-lists" typ="multi { array-id, address-list: string
 }">將把繫結字首/地址新增到的地址列表（覆蓋伺服器的 address-lists 引數）</ArgTableRow>
<ArgTableRow arg="insert-queue-before" typ="enum (first | bottom) { first:0, bottom:0xffffffff }"></ArgTableRow>
<ArgTableRow arg="parent-queue" typ="enum (none) { none:0 }"></ArgTableRow>
<ArgTableRow arg="queue-type" typ="enum"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="active-server" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="status" typ="enum (waiting | offered | bound)"></ArgTableRow>
<ArgTableRow arg="expires-after" typ="time"></ArgTableRow>
<ArgTableRow arg="last-seen" typ="alt { symbolic-names: enum (never | sometime) { never:0xffffffff, sometime:0xfffffffe }
, time: time
 }"></ArgTableRow>
<ArgTableRow arg="client-address" typ="ip6Addr"></ArgTableRow>
<ArgTableRow arg="reconfigure-key" typ="string"></ArgTableRow>
<ArgTableRow arg="reconfigure-last-sent" typ="string"></ArgTableRow>
<ArgTableRow arg="reconfigure-status" typ="string"></ArgTableRow>
</ArgTable>
