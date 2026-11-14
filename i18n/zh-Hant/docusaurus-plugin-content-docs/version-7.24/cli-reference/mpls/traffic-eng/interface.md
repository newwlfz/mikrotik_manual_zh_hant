---
sidebar_key: "cli-reference/mpls/traffic-eng/interface"
sidebar_position: 2
title: "interface"
sidebar_label: "interface"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/mpls/traffic-eng/interface
captured_at: '2026-11-01T21:29:16+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## mpls/traffic-eng/interface {#mplstraffic-enginterface}
**條件：** !smips
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="bandwidth" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="k-factor" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="resource-class" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="refresh-time" typ="time" unset="1"></ArgTableRow>
<ArgTableRow arg="use-udp" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="blockade-k-factor" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="te-metric" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="igp-flood-period" typ="time" unset="1"></ArgTableRow>
<ArgTableRow arg="up-flood-thresholds" typ="multi { array-id, up-flood-threshold: num [0 .. 100]
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="down-flood-thresholds" typ="multi { array-id, down-flood-threshold: num [0 .. 100]
 }" unset="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="remaining-bw" typ="num"></ArgTableRow>
<ArgTableRow arg="remaining-bw-prios" typ="multi { array-id, remaining-bw-prio: num
 }"></ArgTableRow>
<ArgTableRow arg="lih" typ="num"></ArgTableRow>
<ArgTableRow arg="local-address-ip" typ="address (flags=46)"></ArgTableRow>
<ArgTableRow arg="local-address-ip6" typ="address (flags=46)"></ArgTableRow>
</ArgTable>
