---
sidebar_key: "cli-reference/zerotier/interface"
sidebar_position: 2
title: "interface"
sidebar_label: "interface"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/zerotier/interface
captured_at: '2026-11-01T21:30:37+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## zerotier/interface {#zerotierinterface}
**包：** zerotier
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="R" typ="running"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { arp-timeout: enum (auto) { auto:0 }
, arp-timeout: time
 }"></ArgTableRow>
<ArgTableRow arg="disable-running-check" typ="bool"></ArgTableRow>
<ArgTableRow arg="network" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="instance" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="allow-managed" typ="bool"></ArgTableRow>
<ArgTableRow arg="allow-global" typ="bool"></ArgTableRow>
<ArgTableRow arg="allow-default" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="bridge" typ="bool"></ArgTableRow>
<ArgTableRow arg="dhcp" typ="bool"></ArgTableRow>
<ArgTableRow arg="network-name" typ="string"></ArgTableRow>
<ArgTableRow arg="status" typ="string"></ArgTableRow>
<ArgTableRow arg="type" typ="string"></ArgTableRow>
</ArgTable>
