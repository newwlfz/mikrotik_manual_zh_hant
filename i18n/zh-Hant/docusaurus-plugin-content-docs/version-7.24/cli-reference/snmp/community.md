---
sidebar_key: "cli-reference/snmp/community"
sidebar_position: 1
title: "community"
sidebar_label: "community"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/snmp/community
captured_at: '2026-11-01T21:29:43+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## snmp/community {#snmpcommunity}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="*" typ="default">default</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="addresses" typ="object { address: alt { ipv6: ip6Prefix
, ip: ipPrefix
 }
 }"></ArgTableRow>
<ArgTableRow arg="security" typ="enum (none | authorized | private) { none:0, authorized:1, private:2 }"></ArgTableRow>
<ArgTableRow arg="read-access" typ="bool"></ArgTableRow>
<ArgTableRow arg="write-access" typ="bool"></ArgTableRow>
<ArgTableRow arg="authentication-protocol" typ="enum (MD5 | SHA1) { MD5:0, SHA1:1 }"></ArgTableRow>
<ArgTableRow arg="encryption-protocol" typ="enum (DES | AES)"></ArgTableRow>
<ArgTableRow arg="authentication-password" typ="string"></ArgTableRow>
<ArgTableRow arg="encryption-password" typ="string"></ArgTableRow>
</ArgTable>
