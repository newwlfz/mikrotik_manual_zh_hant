---
sidebar_key: "cli-reference/dude/ros/neighbor"
sidebar_position: 6
title: "neighbor"
sidebar_label: "neighbor"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/dude/ros/neighbor
captured_at: '2026-11-01T21:26:51+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## dude/ros/neighbor {#duderosneighbor}
**包：** dude
**型別：** 目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="device" typ="enum" mandatory="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="enum"></ArgTableRow>
<ArgTableRow arg="address" typ="alt { address4: ipAddr
, address6: ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="address4" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="address6" typ="ip6Addr"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="identity" typ="string"></ArgTableRow>
<ArgTableRow arg="platform" typ="string"></ArgTableRow>
<ArgTableRow arg="version" typ="string"></ArgTableRow>
<ArgTableRow arg="unpack" typ="enum (none | simple | uncompress-headers | uncompress-all) { none:0x00, simple:0x01, uncompress-headers:0x03, uncompress-all:0x07 }"></ArgTableRow>
<ArgTableRow arg="age" typ="time"></ArgTableRow>
<ArgTableRow arg="uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="software-id" typ="string"></ArgTableRow>
<ArgTableRow arg="board" typ="string"></ArgTableRow>
<ArgTableRow arg="ipv6" typ="bool"></ArgTableRow>
<ArgTableRow arg="interface-name" typ="string"></ArgTableRow>
</ArgTable>
