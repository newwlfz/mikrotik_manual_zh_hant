---
sidebar_key: "cli-reference/tool/romon/ping"
sidebar_position: 2
title: "ping"
sidebar_label: 'ping'
source: https://manual.mikrotik.com/docs/cli-reference/tool/romon/ping
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/romon/ping {#toolromonping}
**型別：** 命令

透過 [RoMON](../../../management-tools/romon.md) 覆蓋網路，按路由器的 RoMON ID 對其執行 ping，無需任何 IP 連通性。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="id" typ="macAddr">要 ping 的路由器的 RoMON ID（MAC 地址）</ArgTableRow>
<ArgTableRow arg="size" typ="num">ping 封包負載大小（預設值：**32**）</ArgTableRow>
<ArgTableRow arg="interval" typ="time">ping 間隔（預設值：**1s**）</ArgTableRow>
<ArgTableRow arg="count" typ="num">要傳送的 ping 次數（預設值：**100**）</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="seq" typ="num">Ping 序列號</ArgTableRow>
<ArgTableRow arg="host" typ="macAddr">作出應答的路由器的 RoMON ID（MAC 地址）</ArgTableRow>
<ArgTableRow arg="time" typ="time">應答的往返時間</ArgTableRow>
<ArgTableRow arg="size" typ="num">應答大小</ArgTableRow>
<ArgTableRow arg="status" typ="string">失敗原因（例如 `timeout`）；成功時為空</ArgTableRow>
<ArgTableRow arg="sent" typ="num">已傳送的 ping 數量</ArgTableRow>
<ArgTableRow arg="received" typ="num">收到的回覆數量</ArgTableRow>
<ArgTableRow arg="packet-loss" typ="num">丟失 ping 的百分比</ArgTableRow>
<ArgTableRow arg="min-rtt" typ="time">最小往返時間</ArgTableRow>
<ArgTableRow arg="avg-rtt" typ="time">平均往返時間</ArgTableRow>
<ArgTableRow arg="max-rtt" typ="time">最大往返時間</ArgTableRow>
</ArgTable>
