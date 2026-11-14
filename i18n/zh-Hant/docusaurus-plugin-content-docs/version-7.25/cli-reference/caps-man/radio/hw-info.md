---
sidebar_key: "cli-reference/caps-man/radio/hw-info"
sidebar_position: 1
title: "hw-info"
sidebar_label: 'hw-info'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/caps-man/radio/hw-info
captured_at: '2026-11-01T21:21:46+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## caps-man/radio/hw-info {#caps-manradiohw-info}
**包：** wireless-rep
**型別：** 命令

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="ranges" typ="multi { array-id, range: string
 }"></ArgTableRow>
<ArgTableRow arg="tx-chains" typ="ubit (0, 1, 2, 3)"></ArgTableRow>
<ArgTableRow arg="rx-chains" typ="ubit (0, 1, 2, 3)"></ArgTableRow>
<ArgTableRow arg="antenna-gain" typ="num"></ArgTableRow>
<ArgTableRow arg="locked-countries" typ="multi { array-id, country: enum
 }"></ArgTableRow>
</ArgTable>
