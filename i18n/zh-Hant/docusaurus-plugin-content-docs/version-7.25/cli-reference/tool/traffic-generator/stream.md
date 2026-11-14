---
sidebar_key: "cli-reference/tool/traffic-generator/stream"
sidebar_position: 10
title: "stream"
sidebar_label: 'stream'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/tool/traffic-generator/stream
captured_at: '2026-11-01T21:26:05+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/traffic-generator/stream {#tooltraffic-generatorstream}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">無效</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="port" typ="enum"></ArgTableRow>
<ArgTableRow arg="id" typ="num"></ArgTableRow>
<ArgTableRow arg="packet-size" typ="range"></ArgTableRow>
<ArgTableRow arg="pps" typ="num"></ArgTableRow>
<ArgTableRow arg="mbps" typ="num"></ArgTableRow>
<ArgTableRow arg="packet-count" typ="num"></ArgTableRow>
<ArgTableRow arg="cpu-core" typ="range"></ArgTableRow>
<ArgTableRow arg="tx-template" typ="enum" mandatory="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="default-port" typ="enum"></ArgTableRow>
</ArgTable>
