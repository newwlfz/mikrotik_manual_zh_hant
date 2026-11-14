---
sidebar_key: "cli-reference/ip/route/index"
sidebar_position: 2
title: "route"
sidebar_label: 'route'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/route
captured_at: '2026-11-01T21:24:24+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/route {#iproute}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未啟用</ArgTableRow>
<ArgTableRow arg="A" typ="active">已啟用</ArgTableRow>
<ArgTableRow arg="c" typ="connect">connect</ArgTableRow>
<ArgTableRow arg="s" typ="static">static</ArgTableRow>
<ArgTableRow arg="r" typ="rip">rip</ArgTableRow>
<ArgTableRow arg="b" typ="bgp">bgp</ArgTableRow>
<ArgTableRow arg="o" typ="ospf">ospf</ArgTableRow>
<ArgTableRow arg="i" typ="is-is">is-is</ArgTableRow>
<ArgTableRow arg="d" typ="dhcp">dhcp</ArgTableRow>
<ArgTableRow arg="v" typ="vpn">vpn</ArgTableRow>
<ArgTableRow arg="m" typ="modem">modem</ArgTableRow>
<ArgTableRow arg="y" typ="bgp-mpls-vpn">bgp-mpls-vpn</ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded">硬體解除安裝</ArgTableRow>
<ArgTableRow arg="+" typ="ecmp">ecmp</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="dst-address" typ="address (flags=4/)"></ArgTableRow>
<ArgTableRow arg="routing-table" typ="enum"></ArgTableRow>
<ArgTableRow arg="pref-src" typ="address (flags=4)" unset="1"></ArgTableRow>
<ArgTableRow arg="gateway" typ="address (flags=46ivL)" unset="1"></ArgTableRow>
<ArgTableRow arg="blackhole" typ="switch"></ArgTableRow>
<ArgTableRow arg="check-gateway" typ="enum (none | arp | ping | bfd)" unset="1"></ArgTableRow>
<ArgTableRow arg="distance" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="scope" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="target-scope" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="vrf-interface" typ="iface_enum" unset="1"></ArgTableRow>
<ArgTableRow arg="suppress-hw-offload" typ="bool" syscap="crs_prestera"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="immediate-gw" typ="multi { gw: address (flags=46i)
 }"></ArgTableRow>
<ArgTableRow arg="local-address" typ="address (flags=4iv)"></ArgTableRow>
</ArgTable>
