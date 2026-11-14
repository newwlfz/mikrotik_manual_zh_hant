---
sidebar_key: "cli-reference/ip/dhcp-server/setup"
sidebar_position: 7
title: "setup"
sidebar_label: "setup"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/dhcp-server/setup
captured_at: '2026-11-01T21:28:30+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/dhcp-server/setup {#ipdhcp-serversetup}
**型別：** 命令

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="network" typ="composite { address: ipAddr
, netmask: num [ .. 32]
 }"></ArgTableRow>
<ArgTableRow arg="gateway" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="relay" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="ippool" typ="multi { range: composite { min: ipAddr
, max: ipAddr
 }
 }"></ArgTableRow>
<ArgTableRow arg="send-dns" typ="bool"></ArgTableRow>
<ArgTableRow arg="dns-servers" typ="multi { address: ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="lease-time" typ="time"></ArgTableRow>
</ArgTable>
