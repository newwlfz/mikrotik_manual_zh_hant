---
sidebar_key: "cli-reference/zerotier/index"
sidebar_position: 2
title: "zerotier"
sidebar_label: "zerotier"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/zerotier
captured_at: '2026-11-01T21:30:37+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## zerotier {#zerotier}
**軟體包：** zerotier
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="R" typ="online"></ArgTableRow>
<ArgTableRow arg="F" typ="tcp-fallback"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="disabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="identity" typ="string"></ArgTableRow>
<ArgTableRow arg="interfaces" typ="multi { array-id, interface: iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="route-distance" typ="num"></ArgTableRow>
<ArgTableRow arg="backup-priorities" typ="multi { array-id, array-id, backup-priority: composite { interface: iface_enum
, priority: num
 }
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="identity.public" typ="string"></ArgTableRow>
<ArgTableRow arg="state" typ="string"></ArgTableRow>
<ArgTableRow arg="moons" typ="multi { array-id, moon: string
 }"></ArgTableRow>
</ArgTable>
