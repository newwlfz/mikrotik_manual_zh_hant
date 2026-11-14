---
sidebar_key: "cli-reference/ip/hotspot/setup"
sidebar_position: 8
title: "setup"
sidebar_label: 'setup'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/hotspot/setup
captured_at: '2026-11-01T21:24:04+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/hotspot/setup {#iphotspotsetup}
**型別：** 命令

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="alt { interface1: iface_enum
, interface2: iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="address" typ="composite { address: ipAddr
, netmask: num
 }"></ArgTableRow>
<ArgTableRow arg="masq" typ="bool"></ArgTableRow>
<ArgTableRow arg="pool" typ="multi { range: composite { min: ipAddr
, max: ipAddr
 }
 }"></ArgTableRow>
<ArgTableRow arg="ssl-cert" typ="enum (import-other-certificate | none) { import-other-certificate:0, none:0xffffffff }"></ArgTableRow>
<ArgTableRow arg="passphrase" typ="string"></ArgTableRow>
<ArgTableRow arg="smtp-server" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="use-dnscache" typ="bool"></ArgTableRow>
<ArgTableRow arg="dns-server" typ="multi { address: ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="dns-name" typ="string"></ArgTableRow>
<ArgTableRow arg="username" typ="string"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
</ArgTable>
