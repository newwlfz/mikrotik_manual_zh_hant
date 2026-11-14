---
sidebar_key: "cli-reference/tool/traffic-generator/stats/raw"
sidebar_position: 3
title: "raw"
sidebar_label: "raw"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/tool/traffic-generator/stats/raw
captured_at: '2026-11-01T21:30:27+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/traffic-generator/stats/raw {#tooltraffic-generatorstatsraw}
**型別：** 目錄

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="seq" typ="enum (TOT) { TOT:0xffffffff }"></ArgTableRow>
<ArgTableRow arg="port" typ="composite { p: enum (TOT) { TOT:0xffffffff }
, interface: iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="id" typ="enum (TOT) { TOT:0xffffffff }"></ArgTableRow>
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
