---
sidebar_key: "cli-reference/user-manager/attribute"
sidebar_position: 2
title: "attribute"
sidebar_label: 'attribute'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/user-manager/attribute
captured_at: '2026-11-01T21:26:07+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## user-manager/attribute {#user-managerattribute}
**包：** userman-5
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="*" typ="default"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="vendor-id" typ="enum (standard | Cisco | Microsoft | Mikrotik) { standard:0, Cisco:9, Microsoft:311, Mikrotik:14988 }"></ArgTableRow>
<ArgTableRow arg="type-id" typ="num" mandatory="1"></ArgTableRow>
<ArgTableRow arg="value-type" typ="enum (ip-address | string | uint32 | hex | ip6-prefix | macro)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="packet-types" typ="ubit (access-accept, access-challenge)"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="default-name" typ="string"></ArgTableRow>
<ArgTableRow arg="standard-name" typ="string"></ArgTableRow>
</ArgTable>
