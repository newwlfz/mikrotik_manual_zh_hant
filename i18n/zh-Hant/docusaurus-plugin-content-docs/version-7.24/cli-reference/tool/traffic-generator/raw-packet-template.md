---
sidebar_key: "cli-reference/tool/traffic-generator/raw-packet-template"
sidebar_position: 6
title: "raw-packet-template"
sidebar_label: "raw-packet-template"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/tool/traffic-generator/raw-packet-template
captured_at: '2026-11-01T21:30:27+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/traffic-generator/raw-packet-template {#tooltraffic-generatorraw-packet-template}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="port" typ="enum"></ArgTableRow>
<ArgTableRow arg="header" typ="string"></ArgTableRow>
<ArgTableRow arg="data" typ="enum (uninitialized | random | specific-byte | incrementing) { uninitialized:0, random:1, specific-byte:2, incrementing:3 }"></ArgTableRow>
<ArgTableRow arg="data-byte" typ="num"></ArgTableRow>
<ArgTableRow arg="random-byte-offsets-and-masks" typ="multi { array-id, array-id, offset-and-mask: composite { offset: num [ .. 256]
, mask: num [ .. 255]
 }
 }"></ArgTableRow>
<ArgTableRow arg="random-ranges" typ="object { random-range: super { offset: num [ .. 256]
, [width] :enum (8 | 16 | 32) { 8:8, 16:16, 32:32 }
, [range] :range
 }
 }"></ArgTableRow>
<ArgTableRow arg="ip-header-offset" typ="multi { ip-header-offset: num [ .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="ipv6-header-offset" typ="multi { ipv6-header-offset: num [ .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="udp-header-offset" typ="multi { udp-header-offset: num [ .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="udp-compute-checksum" typ="multi { udp-compute-checksum: bool
 }"></ArgTableRow>
<ArgTableRow arg="tcp-header-offset" typ="multi { tcp-header-offset: num [ .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="special-footer" typ="bool"></ArgTableRow>
<ArgTableRow arg="compute-checksum-from-offset" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="header-length" typ="num"></ArgTableRow>
</ArgTable>
