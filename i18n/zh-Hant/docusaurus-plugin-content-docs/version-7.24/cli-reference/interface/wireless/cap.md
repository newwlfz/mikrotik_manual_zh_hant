---
sidebar_key: "cli-reference/interface/wireless/cap"
sidebar_position: 3
title: "cap"
sidebar_label: "cap"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/wireless/cap
captured_at: '2026-11-01T21:27:57+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/wireless/cap {#interfacewirelesscap}
**包：** wireless-rep
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="interfaces" typ="multi { array-id, interface: iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (request | none) { request:0 }"></ArgTableRow>
<ArgTableRow arg="lock-to-caps-man" typ="bool"></ArgTableRow>
<ArgTableRow arg="discovery-interfaces" typ="multi { array-id, interface: iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="caps-man-addresses" typ="multi { array-id, address: ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="caps-man-names" typ="multi { array-id, name: string
 }"></ArgTableRow>
<ArgTableRow arg="caps-man-certificate-common-names" typ="multi { array-id, common-name: string
 }"></ArgTableRow>
<ArgTableRow arg="bridge" typ="iface_enum { none:0xffffffff }"></ArgTableRow>
<ArgTableRow arg="static-virtual" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="requested-certificate" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="locked-caps-man-common-name" typ="string"></ArgTableRow>
</ArgTable>
