---
sidebar_key: "cli-reference/ip/dhcp-relay/index"
sidebar_position: 1
title: "dhcp-relay"
sidebar_label: "dhcp-relay"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/dhcp-relay
captured_at: '2026-11-01T21:28:27+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/dhcp-relay {#ipdhcp-relay}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">無效</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="dhcp-server-vrf" typ="enum"></ArgTableRow>
<ArgTableRow arg="dhcp-server" typ="multi { address: ipAddr
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="delay-threshold" typ="alt { const: enum (none) { none:0 }
, time: time
 }"></ArgTableRow>
<ArgTableRow arg="local-address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="add-relay-info" typ="bool"></ArgTableRow>
<ArgTableRow arg="relay-info-remote-id" typ="string"></ArgTableRow>
<ArgTableRow arg="local-address-as-src-ip" typ="bool"></ArgTableRow>
</ArgTable>
