---
sidebar_key: "cli-reference/routing/filter/filter-wizard"
sidebar_position: 5
title: "filter-wizard"
sidebar_label: 'filter-wizard'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/routing/filter/filter-wizard
captured_at: '2026-11-01T21:25:09+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/filter/filter-wizard {#routingfilterfilter-wizard}
**型別：** 命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="chain" typ="enum"></ArgTableRow>
<ArgTableRow arg="dst" typ="super { !
, dst: alt { dst-list: enum
, dst: address (flags=46/+)
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="dst-len" typ="super { !
, dst-len: range [ .. 128]
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="gateway" typ="super { !
, dst: alt { dst-list: enum
, dst: address (flags=46/+)
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="match-chain" typ="super { !
, chain: enum
 }" unset="1">如果提供的 chain 未拒絕，則返回 true</ArgTableRow>
<ArgTableRow arg="routing-table" typ="super { !
, table: enum
 }" unset="1">該路由匯入來源的路由表名稱</ArgTableRow>
<ArgTableRow arg="afi" typ="super { !
, afi: ubit (ip, ipv6, l2vpn, vpnv4, vpnv6, l2vpn-cisco)
 }" unset="1">路由的地址族</ArgTableRow>
<ArgTableRow arg="protocol" typ="super { !
, protocol: ubit (connected, static, rip, ospf, isis, bgp, vpn, dhcp, fantasy, modem, slaac, bgp-mpls-vpn)
 }" unset="1">路由匯入來源的協定型別</ArgTableRow>
<ArgTableRow arg="bgp-atomic-aggregate" typ="bool"></ArgTableRow>
<ArgTableRow arg="bgp-local-origin" typ="bool">如果字首為本地發起（例如 BGP network），則返回 true</ArgTableRow>
<ArgTableRow arg="suppress-hw-offload" typ="bool" syscap="crs_prestera"></ArgTableRow>
<ArgTableRow arg="use-te-nexthop" typ="bool"></ArgTableRow>
<ArgTableRow arg="blackhole" typ="bool">匹配 blackhole 路由</ArgTableRow>
<ArgTableRow arg="ospf-type" typ="super { !
, ospf-type: enum (intra | inter | ext1 | ext2 | nssa1 | nssa2) { intra:0, inter:1, ext1:2, ext2:3, nssa1:7, nssa2:8 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="rpki" typ="super { !
, rpki-type: enum (unknown | valid | invalid)
 }" unset="1">字首的 RPKI 驗證狀態</ArgTableRow>
<ArgTableRow arg="bgp-origin" typ="super { !
, bgp-origin: ubit (igp, egp, incomplete)
 }" unset="1">匹配 BGP Origin 屬性</ArgTableRow>
<ArgTableRow arg="bgp-as-path" typ="string">匹配 BGP AS-Path 屬性的正則表示式，更多詳情請參閱文件</ArgTableRow>
<ArgTableRow arg="bgp-communities-match" typ="super { !
, match: enum (any | any-list | equal | equal-list | includes | includes-list | subset | subset-list)
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-communities" typ="object" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-communities-list-name" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-ext-communities-match" typ="super { !
, match: enum (any | any-list | equal | equal-list | includes | includes-list | subset | subset-list)
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-ext-communities" typ="object" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-ext-communities-list-name" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-large-communities-match" typ="super { !
, match: enum (any | any-list | equal | equal-list | includes | includes-list | subset | subset-list)
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-large-communities" typ="object" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-large-communities-list-name" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="distance" typ="super { !
, value: alt { num-list: enum
, range: range [ .. 255]
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="scope" typ="super { !
, value: alt { num-list: enum
, range: range [ .. 255]
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="scope-target" typ="super { !
, value: alt { num-list: enum
, range: range [ .. 255]
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-weight" typ="super { !
, value: alt { num-list: enum
, range: range [ .. 65535]
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-local-pref" typ="super { !
, value: alt { num-list: enum
, range: range
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-med" typ="super { !
, value: alt { num-list: enum
, range: range
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-out-med" typ="super { !
, value: alt { num-list: enum
, range: range
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-as-path-length" typ="super { !
, value: alt { num-list: enum
, range: range
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="ospf-metric" typ="super { !
, value: alt { num-list: enum
, range: range
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="set-distance" typ="alt { num-props: enum (distance | scope | target-scope | dst-len | bgp-weight | bgp-med | bgp-out-med | bgp-local-pref | bgp-path-len | bgp-path-prepend | bgp-path-peer-prepend | bgp-input-local-as | bgp-input-remote-as | bgp-output-local-as | bgp-output-remote-as | ospf-metric | ospf-tag | ospf-ext-metric | ospf-ext-tag | rip-metric | rip-tag | rip-ext-metric | rip-ext-tag)
, val: num [1 .. 255]
, value: composite { inc: [ enum ( | add | sub)]
, val: num [1 .. 255]
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="set-scope" typ="alt { num-props: enum (distance | scope | target-scope | dst-len | bgp-weight | bgp-med | bgp-out-med | bgp-local-pref | bgp-path-len | bgp-path-prepend | bgp-path-peer-prepend | bgp-input-local-as | bgp-input-remote-as | bgp-output-local-as | bgp-output-remote-as | ospf-metric | ospf-tag | ospf-ext-metric | ospf-ext-tag | rip-metric | rip-tag | rip-ext-metric | rip-ext-tag)
, val: num [1 .. 255]
, value: composite { inc: enum ( | add | sub)
, val: num [1 .. 255]
 }
 }"></ArgTableRow>
<ArgTableRow arg="set-scope-target" typ="alt { num-props: enum (distance | scope | target-scope | dst-len | bgp-weight | bgp-med | bgp-out-med | bgp-local-pref | bgp-path-len | bgp-path-prepend | bgp-path-peer-prepend | bgp-input-local-as | bgp-input-remote-as | bgp-output-local-as | bgp-output-remote-as | ospf-metric | ospf-tag | ospf-ext-metric | ospf-ext-tag | rip-metric | rip-tag | rip-ext-metric | rip-ext-tag)
, val: num [1 .. 255]
, value: composite { inc: enum ( | add | sub)
, val: num [1 .. 255]
 }
 }"></ArgTableRow>
<ArgTableRow arg="set-bgp-weight" typ="alt { num-props: enum (distance | scope | target-scope | dst-len | bgp-weight | bgp-med | bgp-out-med | bgp-local-pref | bgp-path-len | bgp-path-prepend | bgp-path-peer-prepend | bgp-input-local-as | bgp-input-remote-as | bgp-output-local-as | bgp-output-remote-as | ospf-metric | ospf-tag | ospf-ext-metric | ospf-ext-tag | rip-metric | rip-tag | rip-ext-metric | rip-ext-tag)
, val: num [ .. 65535]
, value: composite { inc: enum ( | add | sub)
, val: num [ .. 65535]
 }
 }"></ArgTableRow>
<ArgTableRow arg="set-bgp-local-pref" typ="alt { num-props: enum (distance | scope | target-scope | dst-len | bgp-weight | bgp-med | bgp-out-med | bgp-local-pref | bgp-path-len | bgp-path-prepend | bgp-path-peer-prepend | bgp-input-local-as | bgp-input-remote-as | bgp-output-local-as | bgp-output-remote-as | ospf-metric | ospf-tag | ospf-ext-metric | ospf-ext-tag | rip-metric | rip-tag | rip-ext-metric | rip-ext-tag)
, val: num
, value: composite { inc: enum ( | add | sub)
, val: num
 }
 }">設定 BGP Local-Pref 屬性的值</ArgTableRow>
<ArgTableRow arg="set-bgp-med" typ="alt { num-props: enum (distance | scope | target-scope | dst-len | bgp-weight | bgp-med | bgp-out-med | bgp-local-pref | bgp-path-len | bgp-path-prepend | bgp-path-peer-prepend | bgp-input-local-as | bgp-input-remote-as | bgp-output-local-as | bgp-output-remote-as | ospf-metric | ospf-tag | ospf-ext-metric | ospf-ext-tag | rip-metric | rip-tag | rip-ext-metric | rip-ext-tag)
, val: num
, value: composite { inc: enum ( | add | sub)
, val: num
 }
 }"></ArgTableRow>
<ArgTableRow arg="set-bgp-out-med" typ="alt { num-props: enum (distance | scope | target-scope | dst-len | bgp-weight | bgp-med | bgp-out-med | bgp-local-pref | bgp-path-len | bgp-path-prepend | bgp-path-peer-prepend | bgp-input-local-as | bgp-input-remote-as | bgp-output-local-as | bgp-output-remote-as | ospf-metric | ospf-tag | ospf-ext-metric | ospf-ext-tag | rip-metric | rip-tag | rip-ext-metric | rip-ext-tag)
, val: num
, value: composite { inc: enum ( | add | sub)
, val: num
 }
 }"></ArgTableRow>
<ArgTableRow arg="set-suppress-hw-offload" typ="bool" syscap="crs_prestera"></ArgTableRow>
<ArgTableRow arg="set-use-te-nexthop" typ="bool"></ArgTableRow>
<ArgTableRow arg="set-blackhole" typ="bool"></ArgTableRow>
<ArgTableRow arg="set-gw-check" typ="enum (none | arp | ping | bfd)">設定閘道器檢查</ArgTableRow>
<ArgTableRow arg="set-gateway" typ="address (flags=46)"></ArgTableRow>
<ArgTableRow arg="set-comment" typ="string"></ArgTableRow>
<ArgTableRow arg="set-bgp-communities" typ="object">設定 BGP Communities 屬性的值</ArgTableRow>
<ArgTableRow arg="set-bgp-communities-list" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="set-bgp-ext-communities" typ="object"></ArgTableRow>
<ArgTableRow arg="set-bgp-large-communities" typ="object"></ArgTableRow>
<ArgTableRow arg="action" typ="enum (accept | reject | jump | return)" unset="1"></ArgTableRow>
<ArgTableRow arg="jump-target-chain" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="rpki-verify" typ="enum" unset="1">在當前 chain 中啟用來自指定 RPKI 組的 RPKI 驗證</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="result" typ="string"></ArgTableRow>
</ArgTable>
