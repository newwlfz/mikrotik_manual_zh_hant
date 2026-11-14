---
sidebar_key: "cli-reference/interface/bridge/host"
sidebar_position: 3
title: "host"
sidebar_label: "host"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/bridge/host
captured_at: '2026-11-01T21:26:59+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/bridge/host {#interfacebridgehost}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">無效</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
<ArgTableRow arg="L" typ="local">local</ArgTableRow>
<ArgTableRow arg="E" typ="external">external</ArgTableRow>
<ArgTableRow arg="A" typ="aged">aged</ArgTableRow>
<ArgTableRow arg="a" typ="aged-peer">aged-peer</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="mac-address" typ="macAddr" mandatory="1"></ArgTableRow>
<ArgTableRow arg="vid" typ="num"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="bridge" typ="iface_enum" mandatory="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="on-interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="remote-ip" typ="alt { ipv4: ipAddr
, ipv6: ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="dhcpv4-ip" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="dhcpv4-server-id" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="dhcpv4-status" typ="enum (bound | requesting | searching | renewing | rebinding | expired | relay-agent)"></ArgTableRow>
<ArgTableRow arg="dhcpv4-expires-after" typ="time"></ArgTableRow>
</ArgTable>
