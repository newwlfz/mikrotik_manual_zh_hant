---
sidebar_key: "cli-reference/interface/wireless/access-list"
sidebar_position: 1
title: "access-list"
sidebar_label: 'access-list'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/wireless/access-list
captured_at: '2026-11-01T21:23:19+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/wireless/access-list {#interfacewirelessaccess-list}
**包：** wireless-rep
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum { any:0 }"></ArgTableRow>
<ArgTableRow arg="signal-range" typ="composite { min: num [-120 .. 120]
, max: num [-120 .. 120]
 }"></ArgTableRow>
<ArgTableRow arg="allow-signal-out-of-range" typ="alt { signal-out-of-range-always: enum (always) { always:0 }
, signal-out-of-range-time: time
 }"></ArgTableRow>
<ArgTableRow arg="authentication" typ="bool"></ArgTableRow>
<ArgTableRow arg="forwarding" typ="bool"></ArgTableRow>
<ArgTableRow arg="ap-tx-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="client-tx-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="private-algo" typ="enum (none | 40bit-wep | 104bit-wep | aes-ccm | tkip) { none:0, 40bit-wep:1, 104bit-wep:2, aes-ccm:3, tkip:4 }"></ArgTableRow>
<ArgTableRow arg="private-key" typ="string"></ArgTableRow>
<ArgTableRow arg="private-pre-shared-key" typ="string"></ArgTableRow>
<ArgTableRow arg="time" typ="super { start: time [0 .. 86400]
, [end] -time [0 .. 86400]
, [day] ,ubit (sun, mon, tue, wed, thu, fri, sat)
 }"></ArgTableRow>
<ArgTableRow arg="management-protection-key" typ="string"></ArgTableRow>
<ArgTableRow arg="vlan-mode" typ="enum (default | no-tag | use-tag | use-service-tag)"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num"></ArgTableRow>
</ArgTable>
