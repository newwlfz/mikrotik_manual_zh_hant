---
sidebar_key: "cli-reference/dude/ros/address"
sidebar_position: 1
title: "address"
sidebar_label: 'address'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/dude/ros/address
captured_at: '2026-11-01T21:22:14+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## dude/ros/address {#duderosaddress}
**包：** dude
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="device" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="address" typ="composite { address: ipAddr
, netmask: [ num [ .. 32]]
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="network" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="netmask" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="broadcast" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="interface" typ="enum" mandatory="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="actual-interface" typ="enum"></ArgTableRow>
</ArgTable>
