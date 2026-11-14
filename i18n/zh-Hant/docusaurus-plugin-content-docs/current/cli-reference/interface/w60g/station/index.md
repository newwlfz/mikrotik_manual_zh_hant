---
sidebar_key: "cli-reference/interface/w60g/station"
title: "station"
sidebar_label: 'station'
source: https://manual.mikrotik.com/docs/cli-reference/interface/w60g/station
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/w60g/station {#interfacew60gstation}
**系統能力：** 60ghz
**軟體包：** wireless-rep
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="R" typ="running"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="parent" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="remote-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp) { disabled:0, enabled:1, proxy-arp:2, reply-only:3, local-proxy-arp:4 }"></ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { arp-timeout: enum (auto) { auto:0 }
, arp-timeout: time
 }"></ArgTableRow>
<ArgTableRow arg="put-in-bridge" typ="iface_enum { none:0, parent:0xffffffff }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="default-name" typ="string"></ArgTableRow>
<ArgTableRow arg="beamforming-event" typ="num"></ArgTableRow>
</ArgTable>
