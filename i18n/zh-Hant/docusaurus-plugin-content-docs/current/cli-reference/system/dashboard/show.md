---
sidebar_key: "cli-reference/system/dashboard/show"
sidebar_position: 2
title: "show"
sidebar_label: 'show'
source: https://manual.mikrotik.com/docs/cli-reference/system/dashboard/show
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/dashboard/show {#systemdashboardshow}
**型別：** 命令

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="model" typ="string"></ArgTableRow>
<ArgTableRow arg="board-name" typ="string"></ArgTableRow>
<ArgTableRow arg="identity" typ="string"></ArgTableRow>
<ArgTableRow arg="version" typ="string"></ArgTableRow>
<ArgTableRow arg="uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="cpu-usage" typ="num"></ArgTableRow>
<ArgTableRow arg="memory-usage" typ="composite { used: num
, total: num
 }"></ArgTableRow>
<ArgTableRow arg="hdd-usage" typ="composite { used: num
, total: num
 }"></ArgTableRow>
<ArgTableRow arg="ether" typ="super { running: num
, [enabled] /num
, [total] /num
 }"></ArgTableRow>
<ArgTableRow arg="wifi" typ="super { running: num
, [enabled] /num
, [total] /num
 }"></ArgTableRow>
<ArgTableRow arg="total-bw" typ="super { tx: num
, [rx] /num
 }"></ArgTableRow>
<ArgTableRow arg="uplink-bw" typ="super { tx: num
, [rx] /num
 }"></ArgTableRow>
<ArgTableRow arg="ether-bw" typ="super { tx: num
, [rx] /num
 }"></ArgTableRow>
<ArgTableRow arg="wifi-bw" typ="super { tx: num
, [rx] /num
 }"></ArgTableRow>
<ArgTableRow arg="lte-bw" typ="super { tx: num
, [rx] /num
 }"></ArgTableRow>
</ArgTable>
