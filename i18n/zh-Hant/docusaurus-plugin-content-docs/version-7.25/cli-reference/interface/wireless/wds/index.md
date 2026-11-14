---
sidebar_key: "cli-reference/interface/wireless/wds/index"
sidebar_position: 1
title: "wds"
sidebar_label: 'wds'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/wireless/wds
captured_at: '2026-11-01T21:23:31+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/wireless/wds {#interfacewirelesswds}
**軟體包：** wireless-rep
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="R" typ="running"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="l2mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp) { disabled:0, enabled:1, proxy-arp:2, reply-only:3, local-proxy-arp:4 }"></ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { arp-timeout: enum (auto) { auto:0 }
, arp-timeout: time
 }"></ArgTableRow>
<ArgTableRow arg="disable-running-check" typ="bool"></ArgTableRow>
<ArgTableRow arg="master-interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="wds-address" typ="macAddr"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
</ArgTable>
