---
sidebar_key: "cli-reference/app/network"
sidebar_position: 2
title: "network"
sidebar_label: "network"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/app/network
captured_at: '2026-11-01T21:26:17+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## app/network {#appnetwork}
**系統能力：** app
**軟體包：** container
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="e" typ="external"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="allow-outgoing-access" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="network" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="ip" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="status" typ="string"></ArgTableRow>
<ArgTableRow arg="used-ips" typ="multi { array-id, array-id, ip-and-name: composite { ip: ipAddr
, name: string
 }
 }"></ArgTableRow>
<ArgTableRow arg="bridge-interface" typ="iface_enum { none }"></ArgTableRow>
<ArgTableRow arg="cmds" typ="multi { cmd: string
 }"></ArgTableRow>
</ArgTable>
