---
sidebar_key: "cli-reference/interface/veth"
sidebar_position: 35
title: "veth"
sidebar_label: "veth"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/veth
captured_at: '2026-11-01T21:27:41+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/veth {#interfaceveth}
**條件：** !smips
**系統能力：** container
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="container-mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="address" typ="multi { address: address (flags=46/)
 }"></ArgTableRow>
<ArgTableRow arg="gateway" typ="address (flags=4)"></ArgTableRow>
<ArgTableRow arg="gateway6" typ="address (flags=6)"></ArgTableRow>
<ArgTableRow arg="dhcp" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="dhcp-address" typ="address (flags=46/)"></ArgTableRow>
</ArgTable>
