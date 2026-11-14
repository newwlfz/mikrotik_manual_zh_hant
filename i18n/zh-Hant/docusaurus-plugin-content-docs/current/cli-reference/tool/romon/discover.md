---
sidebar_key: "cli-reference/tool/romon/discover"
sidebar_position: 1
title: "discover"
sidebar_label: 'discover'
source: https://manual.mikrotik.com/docs/cli-reference/tool/romon/discover
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/romon/discover {#toolromondiscover}
**型別：** 命令

發現透過 [RoMON](../../../management-tools/romon.md) 覆蓋網路可訪問的路由器。表格會持續重新整理（按 `q` 停止）；`duration` 會在給定時間後停止。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="A" typ="active">已啟用</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="address" typ="macAddr">發現的路由器的 RoMON ID（MAC 地址）</ArgTableRow>
<ArgTableRow arg="cost" typ="num">到該路由器的 RoMON 路徑累計開銷（由 `/tool/romon/port` 配置的各埠開銷之和）</ArgTableRow>
<ArgTableRow arg="hops" typ="num">本路由器與發現的路由器之間的 RoMON 跳數</ArgTableRow>
<ArgTableRow arg="path" typ="multi { array-id, path-hop: macAddr
 }">發現應答所經過的 RoMON ID（MAC 地址）路徑</ArgTableRow>
<ArgTableRow arg="l2mtu" typ="num">RoMON 路徑上最小的 L2 MTU</ArgTableRow>
<ArgTableRow arg="identity" typ="string">發現的路由器的 RouterOS 系統標識</ArgTableRow>
<ArgTableRow arg="version" typ="string">發現的路由器的 RouterOS 版本</ArgTableRow>
<ArgTableRow arg="board" typ="string">發現的路由器的板卡名稱</ArgTableRow>
<ArgTableRow arg="uptime" typ="time">發現的路由器的執行時間</ArgTableRow>
</ArgTable>
