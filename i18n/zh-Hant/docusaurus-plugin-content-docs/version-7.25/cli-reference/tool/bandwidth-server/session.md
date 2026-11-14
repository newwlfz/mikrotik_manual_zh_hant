---
sidebar_key: "cli-reference/tool/bandwidth-server/session"
sidebar_position: 1
title: "session"
sidebar_label: 'session'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/tool/bandwidth-server/session
captured_at: '2026-11-01T21:25:51+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/bandwidth-server/session {#toolbandwidth-serversession}
**型別：** 目錄

此路由器頻寬測試伺服器（[`/tool/bandwidth-server`](./index.md)）上正在執行的測試，從伺服器的角度來看：`send` 表示伺服器傳送。測試結束後，會話就會消失。參見[頻寬測試](../../../diagnostics-monitoring-and-troubleshooting/bandwidth-test.md)。

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="client" typ="alt { ip: ipAddr
, ipv6: ip6Addr
 }">用戶端地址。IPv4 用戶端顯示為 IPv4 對映的 IPv6 地址，例如 `::ffff:192.0.2.1`。</ArgTableRow>
<ArgTableRow arg="protocol" typ="enum (udp | tcp) { udp:0, tcp:1 }">測試使用的協定，`udp` 或 `tcp`。</ArgTableRow>
<ArgTableRow arg="direction" typ="enum (receive | send | both) { receive:0x00000100, send:0x00000200, both:0x00000300 }">
從伺服器的角度來看，哪一側傳送：
- `receive` - 用戶端傳送，伺服器接收（用戶端的 `transmit`）。
- `send` - 伺服器傳送（用戶端的 `receive`）。
- `both` - 雙方都發送。
</ArgTableRow>
<ArgTableRow arg="user" typ="string">用戶端登入時使用的使用者；當伺服器設定了 `authenticate=no` 且用戶端未提供使用者時為空。</ArgTableRow>
<ArgTableRow arg="random-data" typ="bool">測試是否使用隨機資料。</ArgTableRow>
<ArgTableRow arg="tx-current" typ="num">伺服器在上一秒內的傳送速率。</ArgTableRow>
<ArgTableRow arg="tx-10-second-average" typ="num">伺服器在過去 10 秒內的平均傳送速率。</ArgTableRow>
<ArgTableRow arg="tx-total-average" typ="num">自測試開始以來伺服器的平均傳送速率。</ArgTableRow>
<ArgTableRow arg="rx-current" typ="num">伺服器在上一秒內的接收速率。</ArgTableRow>
<ArgTableRow arg="rx-10-second-average" typ="num">伺服器在過去 10 秒內的平均接收速率。</ArgTableRow>
<ArgTableRow arg="rx-total-average" typ="num">自測試開始以來伺服器的平均接收速率。</ArgTableRow>
<ArgTableRow arg="lost-packets" typ="num">伺服器在上一秒內發現丟失的 UDP 封包。</ArgTableRow>
<ArgTableRow arg="tx-size" typ="range">伺服器傳送的 UDP 封包大小，以整個 IP 封包的位元組數表示。</ArgTableRow>
<ArgTableRow arg="rx-size" typ="range">伺服器接收的 UDP 封包大小，以整個 IP 封包的位元組數表示。</ArgTableRow>
<ArgTableRow arg="tcp-connection-count" typ="num">測試的連線數（用戶端的 `connection-count`）；UDP 測試也會顯示。</ArgTableRow>
<ArgTableRow arg="local-tx-speed" typ="num">用戶端為其自身傳送設定的速度限制（`local-tx-speed`）。</ArgTableRow>
<ArgTableRow arg="remote-tx-speed" typ="num">用戶端為伺服器傳送設定的速度限制（`remote-tx-speed`）。</ArgTableRow>
</ArgTable>
