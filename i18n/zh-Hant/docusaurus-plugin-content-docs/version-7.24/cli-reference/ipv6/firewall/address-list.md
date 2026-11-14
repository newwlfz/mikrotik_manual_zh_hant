---
sidebar_key: "cli-reference/ipv6/firewall/address-list"
sidebar_position: 1
title: "address-list"
sidebar_label: "address-list"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ipv6/firewall/address-list
captured_at: '2026-11-01T21:29:05+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ipv6/firewall/address-list {#ipv6firewalladdress-list}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="list" typ="enum" mandatory="1">要新增 IP 地址的地址列表名稱。</ArgTableRow>
<ArgTableRow arg="address" typ="alt { address: ip6Prefix
, dns-name: string
 }">要新增到地址列表的單個 IPv6 地址或字首，或 DNS 名稱。</ArgTableRow>
<ArgTableRow arg="timeout" typ="time">在該時間之後，地址將從地址列表中移除。如果未指定 timeout，地址將永久儲存在地址列表中。</ArgTableRow>
<ArgTableRow arg="dynamic" typ="bool">條目是否為動態建立。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="creation-time" typ="date">建立該條目的時間。</ArgTableRow>
</ArgTable>
