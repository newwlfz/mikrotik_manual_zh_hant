---
sidebar_key: "cli-reference/tool/flood-ping"
sidebar_position: 8
title: "flood-ping"
sidebar_label: 'flood-ping'
source: https://manual.mikrotik.com/docs/cli-reference/tool/flood-ping
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/flood-ping {#toolflood-ping}
**條件：** !smips
**型別：** 命令

向一臺主機發送一系列 ICMP echo 請求，並且只顯示總計。在 SMIPS 裝置上不可用。需要 `traffic-gen` 裝置模式功能；如果沒有該功能，命令會失敗並顯示 `failure: not allowed by device-mode`。有關示例，請參閱 [泛洪 Ping](../../diagnostics-monitoring-and-troubleshooting/flood-ping.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="address" typ="alt { ipv6: ip6Addr
, ip: ipAddr
 }">要 ping 的主機的 IPv4 或 IPv6 地址。</ArgTableRow>
<ArgTableRow arg="count" typ="num">要傳送的請求數，`0..1000`。</ArgTableRow>
<ArgTableRow arg="size" typ="num">每個請求的大小，`10..1500`。</ArgTableRow>
<ArgTableRow arg="timeout" typ="time">等待每個回覆的時長，`00:00:00.010..00:00:05`（10 ms 到 5 s）。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="sent" typ="num">已傳送的請求數。</ArgTableRow>
<ArgTableRow arg="received" typ="num">已接收的回覆數。與 `sent` 的差值即為丟包數。</ArgTableRow>
<ArgTableRow arg="min-rtt" typ="time">本次執行的最短往返時間。</ArgTableRow>
<ArgTableRow arg="avg-rtt" typ="time">本次執行的平均往返時間。</ArgTableRow>
<ArgTableRow arg="max-rtt" typ="time">本次執行的最長往返時間。</ArgTableRow>
</ArgTable>
