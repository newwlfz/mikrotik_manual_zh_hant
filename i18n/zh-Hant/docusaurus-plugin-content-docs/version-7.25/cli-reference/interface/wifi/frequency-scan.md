---
sidebar_key: "cli-reference/interface/wifi/frequency-scan"
sidebar_position: 10
title: "frequency-scan"
sidebar_label: 'frequency-scan'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/wifi/frequency-scan
captured_at: '2026-11-01T21:23:12+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/wifi/frequency-scan {#interfacewififrequency-scan}
**型別：** 命令

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="R" typ="radar">radar</ArgTableRow>
<ArgTableRow arg="P" typ="primary">primary</ArgTableRow>
<ArgTableRow arg="S" typ="secondary">secondary</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="rounds" typ="num"></ArgTableRow>
<ArgTableRow arg="save-file" typ="string"></ArgTableRow>
<ArgTableRow arg="frequency" typ="object" unset="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="channel" typ="string"></ArgTableRow>
<ArgTableRow arg="networks" typ="num"></ArgTableRow>
<ArgTableRow arg="load" typ="num"></ArgTableRow>
<ArgTableRow arg="nf" typ="num"></ArgTableRow>
<ArgTableRow arg="max-signal" typ="num"></ArgTableRow>
<ArgTableRow arg="min-signal" typ="num"></ArgTableRow>
<ArgTableRow arg="srp-networks" typ="num"></ArgTableRow>
<ArgTableRow arg="srp-load" typ="num"></ArgTableRow>
</ArgTable>
