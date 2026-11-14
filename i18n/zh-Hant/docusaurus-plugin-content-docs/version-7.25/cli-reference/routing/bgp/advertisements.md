---
sidebar_key: "cli-reference/routing/bgp/advertisements"
sidebar_position: 1
title: "advertisements"
sidebar_label: 'advertisements'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/routing/bgp/advertisements
captured_at: '2026-11-01T21:25:03+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/bgp/advertisements {#routingbgpadvertisements}
**條件：** !smips
**型別：** 目錄

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="peer" typ="enum"></ArgTableRow>
<ArgTableRow arg="dst" typ="address (flags=46/R)"></ArgTableRow>
<ArgTableRow arg="afi" typ="enum (ip | ipv6 | l2vpn | l2vpn-cisco | vpnv4 | vpnv6)"></ArgTableRow>
<ArgTableRow arg="local-pref" typ="num"></ArgTableRow>
<ArgTableRow arg="med" typ="num"></ArgTableRow>
<ArgTableRow arg="nexthop" typ="multi { prefix: address (flags=46)
 }"></ArgTableRow>
<ArgTableRow arg="nlri" typ="multi { prefix: address (flags=46i/SR)
 }"></ArgTableRow>
<ArgTableRow arg="withdrawn" typ="multi { prefix: address (flags=46i/SR)
 }"></ArgTableRow>
<ArgTableRow arg="origin" typ="num"></ArgTableRow>
<ArgTableRow arg="as-path" typ="multi { value: string
 }"></ArgTableRow>
<ArgTableRow arg="as4-path" typ="multi { value: string
 }"></ArgTableRow>
<ArgTableRow arg="communities" typ="multi { value: string
 }"></ArgTableRow>
<ArgTableRow arg="ext-communities" typ="multi { value: string
 }"></ArgTableRow>
<ArgTableRow arg="large-communities" typ="multi { value: string
 }"></ArgTableRow>
<ArgTableRow arg="atomic-aggregate" typ="bool"></ArgTableRow>
<ArgTableRow arg="aggregator" typ="string"></ArgTableRow>
<ArgTableRow arg="as4-aggregator" typ="string"></ArgTableRow>
<ArgTableRow arg="originator-id" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="cluster-list" typ="multi { value: ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="igp-metric" typ="num"></ArgTableRow>
<ArgTableRow arg="otc" typ="num"></ArgTableRow>
</ArgTable>
