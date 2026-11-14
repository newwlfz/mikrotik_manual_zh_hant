---
sidebar_key: "cli-reference/system/resource/irq/index"
sidebar_position: 1
title: "irq"
sidebar_label: 'irq'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/system/resource/irq
captured_at: '2026-11-01T21:25:40+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/resource/irq {#systemresourceirq}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="o" typ="read-only"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="cpu" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="irq" typ="num"></ArgTableRow>
<ArgTableRow arg="users" typ="object { user: alt { interface: iface_enum
, other: string
 }
 }"></ArgTableRow>
<ArgTableRow arg="active-cpu" typ="num"></ArgTableRow>
<ArgTableRow arg="count" typ="num"></ArgTableRow>
<ArgTableRow arg="per-cpu-count" typ="multi { count: num
 }"></ArgTableRow>
</ArgTable>
