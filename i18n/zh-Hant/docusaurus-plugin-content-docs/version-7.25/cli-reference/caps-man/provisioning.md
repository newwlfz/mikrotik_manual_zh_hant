---
sidebar_key: "cli-reference/caps-man/provisioning"
sidebar_position: 9
title: "provisioning"
sidebar_label: 'provisioning'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/caps-man/provisioning
captured_at: '2026-11-01T21:21:46+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## caps-man/provisioning {#caps-manprovisioning}
**包：** wireless-rep
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="radio-mac" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="hw-supported-modes" typ="multi { array-id, hw-supported-mode: enum (a | a-turbo | an | ac | b | g | g-turbo | gn) { a:1, a-turbo:2, an:3, ac:5, b:0x11, g:0x12, g-turbo:0x13, gn:0x14 }
 }"></ArgTableRow>
<ArgTableRow arg="identity-regexp" typ="string"></ArgTableRow>
<ArgTableRow arg="common-name-regexp" typ="string"></ArgTableRow>
<ArgTableRow arg="ip-address-ranges" typ="multi { ip-address-range: ipRange
 }"></ArgTableRow>
<ArgTableRow arg="action" typ="enum (none | create-enabled | create-disabled | create-dynamic-enabled)"></ArgTableRow>
<ArgTableRow arg="master-configuration" typ="enum"></ArgTableRow>
<ArgTableRow arg="slave-configurations" typ="multi { array-id, slave-configuration: enum
 }"></ArgTableRow>
<ArgTableRow arg="name-format" typ="enum (cap | prefix | identity | prefix-identity)"></ArgTableRow>
<ArgTableRow arg="name-prefix" typ="string"></ArgTableRow>
</ArgTable>
