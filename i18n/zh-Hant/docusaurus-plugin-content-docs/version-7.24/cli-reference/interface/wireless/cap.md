---
title: "cap"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/wireless/cap
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

-----------

## interface/wireless/cap 
**套件:** wireless-rep
**類型:** 設定目錄

<ArgTable c1="Argument" c2="Type" c3="Description">
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

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="requested-certificate" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="locked-caps-man-common-name" typ="string"></ArgTableRow>
</ArgTable>
