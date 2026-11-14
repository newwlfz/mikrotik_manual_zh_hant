---
sidebar_key: "cli-reference/system/swos"
title: "swos"
sidebar_label: 'swos'
source: https://manual.mikrotik.com/docs/cli-reference/system/swos
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/swos {#systemswos}
**條件：** !i386, !mmips, !powerpc, !tile, !smips
**系統能力：** swos
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="address-acquisition-mode" typ="enum (dhcp-with-fallback | static | dhcp-only) { dhcp-with-fallback:0, static:1, dhcp-only:2 }"></ArgTableRow>
<ArgTableRow arg="static-ip-address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="identity" typ="string"></ArgTableRow>
<ArgTableRow arg="allow-from" typ="composite { address: ipAddr
, netmask: [ num [ .. 32]]
 }"></ArgTableRow>
<ArgTableRow arg="allow-from-ports" typ="ubit (p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30, p31, p32)"></ArgTableRow>
<ArgTableRow arg="allow-from-vlan" typ="num"></ArgTableRow>
</ArgTable>
