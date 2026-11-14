---
sidebar_key: "cli-reference/interface/macvlan"
sidebar_position: 20
title: "macvlan"
sidebar_label: 'macvlan'
source: https://manual.mikrotik.com/docs/cli-reference/interface/macvlan
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/macvlan {#interfacemacvlan}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum">macvlan 僅支援具有 MAC 地址的介面</ArgTableRow>
<ArgTableRow arg="mode" typ="enum (private | bridge) { private:1, bridge:4 }">在 bridge 模式下，允許 macvlan 介面相互通訊</ArgTableRow>
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
<ArgTableRow arg="loop-protect-status" typ="enum (off | on | disabled) { off:1, on:2, disabled:3 }"></ArgTableRow>
</ArgTable>
