---
sidebar_key: "cli-reference/snmp/index"
sidebar_position: 2
title: "snmp"
sidebar_label: 'snmp'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/snmp
captured_at: '2026-11-01T21:25:22+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## snmp {#snmp}
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="contact" typ="string"></ArgTableRow>
<ArgTableRow arg="location" typ="string"></ArgTableRow>
<ArgTableRow arg="engine-id-suffix" typ="string"></ArgTableRow>
<ArgTableRow arg="src-address" typ="alt { ip: ipAddr
, ip6: ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="trap-target" typ="object { ip-addresses: alt { ipv6: ip6Addr
, ip: ipAddr
 }
 }"></ArgTableRow>
<ArgTableRow arg="trap-community" typ="enum"></ArgTableRow>
<ArgTableRow arg="trap-version" typ="enum (1 | 2 | 3) { 1:0, 2:1, 3:3 }"></ArgTableRow>
<ArgTableRow arg="trap-generators" typ="multi { array-id, generator: enum
 }"></ArgTableRow>
<ArgTableRow arg="trap-interfaces" typ="object { interface: iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="vrf" typ="enum"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="engine-id" typ="string"></ArgTableRow>
</ArgTable>
