---
sidebar_key: "cli-reference/tool/snmp-walk"
sidebar_position: 21
title: "snmp-walk"
sidebar_label: "snmp-walk"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/tool/snmp-walk
captured_at: '2026-11-01T21:30:22+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/snmp-walk {#toolsnmp-walk}
**型別：** 命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="oid" typ="string"></ArgTableRow>
<ArgTableRow arg="address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="tries" typ="num"></ArgTableRow>
<ArgTableRow arg="try-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="version" typ="enum (1 | 2c | 3)"></ArgTableRow>
<ArgTableRow arg="community" typ="string"></ArgTableRow>
<ArgTableRow arg="security" typ="enum (none | authorized | private) { none:0, authorized:1, private:2 }"></ArgTableRow>
<ArgTableRow arg="authentication-password" typ="string"></ArgTableRow>
<ArgTableRow arg="authentication-protocol" typ="enum (MD5 | SHA1)"></ArgTableRow>
<ArgTableRow arg="encryption-password" typ="string"></ArgTableRow>
<ArgTableRow arg="encryption-protocol" typ="enum (DES | AES)"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="oid" typ="string"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (null | integer | counter | gauge | timeticks | unsigned-integer | octet-string | opaque | object-id | ip-address | counter-64bit | no-such-object | no-such-instance | end-of-mib-view)"></ArgTableRow>
<ArgTableRow arg="value" typ="string"></ArgTableRow>
</ArgTable>
