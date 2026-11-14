---
sidebar_key: "cli-reference/mpls/forwarding-table"
sidebar_position: 1
title: "forwarding-table"
sidebar_label: 'forwarding-table'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/mpls/forwarding-table
captured_at: '2026-11-01T21:24:46+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## mpls/forwarding-table {#mplsforwarding-table}
**條件：** !smips
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="L" typ="ldp"></ArgTableRow>
<ArgTableRow arg="P" typ="vpn"></ArgTableRow>
<ArgTableRow arg="T" typ="traffic-eng"></ArgTableRow>
<ArgTableRow arg="V" typ="vpls"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="label" typ="enum (expl-null | alert | expl-null6 | impl-null) { expl-null:0, alert:1, expl-null6:2, impl-null:3 }"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (ldp | vpn | traffic-eng | vpls)"></ArgTableRow>
<ArgTableRow arg="vrf" typ="enum"></ArgTableRow>
<ArgTableRow arg="prefix" typ="address (flags=46/)"></ArgTableRow>
<ArgTableRow arg="nexthops" typ="object { label: enum (expl-null | alert | expl-null6 | impl-null) { expl-null:0, alert:1, expl-null6:2, impl-null:3 }
, nh: address
, interface: iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="te-sender" typ="string"></ArgTableRow>
<ArgTableRow arg="te-session" typ="string"></ArgTableRow>
<ArgTableRow arg="vpls" typ="iface_enum"></ArgTableRow>
</ArgTable>
