---
sidebar_key: "cli-reference/routing/nexthop/index"
sidebar_position: 2
title: "nexthop"
sidebar_label: 'nexthop'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/routing/nexthop
captured_at: '2026-11-01T21:25:12+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/nexthop {#routingnexthop}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="I" typ="unresolved">unresolved</ArgTableRow>
<ArgTableRow arg="R" typ="reachable">reachable</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="afi" typ="enum (bad | ip | ipv6 | l2vpn | vpnv4 | vpnv6 | l2vpn-cisco | mip4 | mip6 | link)" unset="1"></ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46iv)"></ArgTableRow>
<ArgTableRow arg="gw-state" typ="enum (unreachable | reachable | recursive | inactive)"></ArgTableRow>
<ArgTableRow arg="prev-reachable" typ="bool"></ArgTableRow>
<ArgTableRow arg="scope" typ="num"></ArgTableRow>
<ArgTableRow arg="target-scope" typ="num"></ArgTableRow>
<ArgTableRow arg="check-gateway" typ="enum (none | arp | ping)"></ArgTableRow>
<ArgTableRow arg="gw-check-ok" typ="bool"></ArgTableRow>
<ArgTableRow arg="interface-ok" typ="bool"></ArgTableRow>
<ArgTableRow arg="bgp-vpn" typ="bool"></ArgTableRow>
<ArgTableRow arg="hops" typ="num"></ArgTableRow>
<ArgTableRow arg="routes" typ="num"></ArgTableRow>
<ArgTableRow arg="immediate-gw.address" typ="object { address: address (flags=64iv)
 }"></ArgTableRow>
<ArgTableRow arg="immediate-gw.weight" typ="object { weight: num
 }"></ArgTableRow>
<ArgTableRow arg="immediate-gw.flap-count" typ="object { flap-count: num
 }"></ArgTableRow>
<ArgTableRow arg="immediate-gw.interface-idx" typ="object { interface-idx: num
 }"></ArgTableRow>
<ArgTableRow arg="immediate-gw.mpls-peer-id" typ="object { mpls-peer-id: num
 }"></ArgTableRow>
<ArgTableRow arg="immediate-gw.mpls-label" typ="object { mpls-label: num
 }"></ArgTableRow>
<ArgTableRow arg="immediate-gw.blackhole" typ="object { type: bool
 }"></ArgTableRow>
<ArgTableRow arg="links" typ="object { link-type: enum (output | input)
, address: address (flags=46iv/)
, route-id: num
, fwp-id: num
, ok: switch
, cost: switch
, reach: switch
 }"></ArgTableRow>
</ArgTable>
