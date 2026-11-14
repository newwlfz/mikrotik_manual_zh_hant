---
sidebar_key: "cli-reference/tool/romon/discover"
sidebar_position: 1
title: "discover"
sidebar_label: "discover"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/tool/romon/discover
captured_at: '2026-11-01T21:30:19+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/romon/discover {#toolromondiscover}
**型別：** 命令

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="A" typ="active">已啟用</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="cost" typ="num"></ArgTableRow>
<ArgTableRow arg="hops" typ="num"></ArgTableRow>
<ArgTableRow arg="path" typ="multi { array-id, path-hop: macAddr
 }"></ArgTableRow>
<ArgTableRow arg="l2mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="identity" typ="string"></ArgTableRow>
<ArgTableRow arg="version" typ="string"></ArgTableRow>
<ArgTableRow arg="board" typ="string"></ArgTableRow>
<ArgTableRow arg="uptime" typ="time"></ArgTableRow>
</ArgTable>
