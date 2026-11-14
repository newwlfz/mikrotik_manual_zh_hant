---
sidebar_key: "cli-reference/caps-man/interface/hw-info"
sidebar_position: 1
title: "hw-info"
sidebar_label: 'hw-info'
source: https://manual.mikrotik.com/docs/cli-reference/caps-man/interface/hw-info
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## caps-man/interface/hw-info {#caps-maninterfacehw-info}
**軟體包：** wireless-rep
**型別：** 命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="ranges" typ="multi { array-id, range: string
 }"></ArgTableRow>
<ArgTableRow arg="tx-chains" typ="ubit (0, 1, 2, 3)"></ArgTableRow>
<ArgTableRow arg="rx-chains" typ="ubit (0, 1, 2, 3)"></ArgTableRow>
<ArgTableRow arg="antenna-gain" typ="num"></ArgTableRow>
<ArgTableRow arg="locked-countries" typ="multi { array-id, country: enum
 }"></ArgTableRow>
</ArgTable>
