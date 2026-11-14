---
sidebar_key: "cli-reference/tool/traffic-generator/stats/port"
sidebar_position: 2
title: "port"
sidebar_label: 'port'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/tool/traffic-generator/stats/port
captured_at: '2026-11-01T21:26:03+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/traffic-generator/stats/port {#tooltraffic-generatorstatsport}
**型別：** 目錄

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="seq" typ="enum (TOT) { TOT:0xffffffff }"></ArgTableRow>
<ArgTableRow arg="port" typ="composite { p: enum (TOT) { TOT:0xffffffff }
, interface: iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="rx-unk-packet" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-unk-byte" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-unk-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-packet" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-byte" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-packet" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-byte" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-ooo" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-bad-csum" typ="num"></ArgTableRow>
<ArgTableRow arg="lost-packet" typ="num"></ArgTableRow>
<ArgTableRow arg="lost-byte" typ="num"></ArgTableRow>
<ArgTableRow arg="lost-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="lost-ratio" typ="string"></ArgTableRow>
<ArgTableRow arg="lat-min" typ="string"></ArgTableRow>
<ArgTableRow arg="lat-avg" typ="string"></ArgTableRow>
<ArgTableRow arg="lat-max" typ="string"></ArgTableRow>
<ArgTableRow arg="jitter" typ="string"></ArgTableRow>
</ArgTable>
