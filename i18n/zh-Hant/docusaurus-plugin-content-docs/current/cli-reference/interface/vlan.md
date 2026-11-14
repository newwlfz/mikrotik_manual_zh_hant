---
sidebar_key: "cli-reference/interface/vlan"
sidebar_position: 36
title: "vlan"
sidebar_label: 'vlan'
source: https://manual.mikrotik.com/docs/cli-reference/interface/vlan
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/vlan {#interfacevlan}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded">硬體解除安裝</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="forced-mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num" mandatory="1"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="use-service-tag" typ="bool"></ArgTableRow>
<ArgTableRow arg="mvrp" typ="bool"></ArgTableRow>
<ArgTableRow arg="l3-hw-offloading" typ="bool" syscap="crs_prestera">三層硬體解除安裝</ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp) { disabled:0, enabled:1, proxy-arp:2, reply-only:3, local-proxy-arp:4 }"></ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { arp-timeout: enum (auto) { auto:0 }
, arp-timeout: time
 }"></ArgTableRow>
<ArgTableRow arg="arp-accept" typ="bool">是否接受免費 ARP 回覆。</ArgTableRow>
<ArgTableRow arg="loop-protect" typ="enum (default | off | on) { default:0, off:1, on:2 }"></ArgTableRow>
<ArgTableRow arg="loop-protect-send-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="loop-protect-disable-time" typ="time"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="l2mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="loop-protect-status" typ="enum (off | on | disabled) { off:1, on:2, disabled:3 }"></ArgTableRow>
</ArgTable>
