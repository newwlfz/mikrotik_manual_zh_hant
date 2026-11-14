---
sidebar_key: "cli-reference/tool/speed-test"
sidebar_position: 22
title: "speed-test"
sidebar_label: 'speed-test'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/tool/speed-test
captured_at: '2026-11-01T21:26:00+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/speed-test {#toolspeed-test}
**型別：** 命令

在一次執行中測量到另一臺 MikroTik 路由器的鏈路：ping 往返時間、抖動和丟包，然後透過遠端路由器的頻寬測試伺服器（`/tool/bandwidth-server`）測量雙向的 TCP 和 UDP 吞吐量。測試執行五個部分，每部分持續 `test-duration`，各部分之間暫停約一秒，並在吞吐量結果旁顯示路由器的 CPU 負載。遠端路由器需要啟用伺服器、一個位於具有 `test` 和 `winbox` 策略的組中的使用者，以及允許 TCP 埠 2000 和伺服器 UDP 埠的防火牆。需要 `bandwidth-test` device-mode 功能。有關示例，請參見 [速度測試](../../diagnostics-monitoring-and-troubleshooting/speed-test.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="address" typ="address (flags=46viD)">遠端路由器的 IPv4 或 IPv6 地址，該路由器執行頻寬測試伺服器。請使用要測量的路徑上該路由器的地址，例如用其隧道地址來測試 VPN。</ArgTableRow>
<ArgTableRow arg="connection-count" typ="num">測試的 TCP 部分使用的 TCP 連線數，`1..255`。遠端伺服器的會話列表將其顯示為 `tcp-connection-count`。預設值：20；如果執行測試的路由器 CPU 核心數超過 20，則為該核心數（例如 64 核路由器上為 64）。</ArgTableRow>
<ArgTableRow arg="test-duration" typ="time">測試的五個部分中每一部分的持續時間，至少 5 秒。路由器在各部分之間暫停約一秒，因此預設測試大約需要 55 秒。預設值：10s。</ArgTableRow>
<ArgTableRow arg="user" typ="string">遠端路由器上的使用者名稱。其所屬組需要具有 `test` 和 `winbox` 策略，與預設的 `read` 和 `full` 組相同。沒有 `user` 時，該命令不傳送使用者名稱，並且每條吞吐量行都會顯示 `authentication failed`，除非伺服器設定了 `authenticate=no`。使用者的 `address` 設定不會限制頻寬測試登入；伺服器的 `allowed-addresses4` 和 `allowed-addresses6` 會限制哪些路由器可以連線。</ArgTableRow>
<ArgTableRow arg="password" typ="string">遠端路由器上 `user` 的密碼。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="status" typ="string">
正在執行的測試部分：
- `ping` - 執行 Ping 以測量延遲、抖動和丟包。
- `tcp download` - 從遠端路由器到本路由器的 TCP。
- `tcp upload` - 從本路由器到遠端路由器的 TCP。
- `udp download` - 從遠端路由器到本路由器的 UDP。
- `udp upload` - 從本路由器到遠端路由器的 UDP。
- `done` - 測試已結束。
</ArgTableRow>
<ArgTableRow arg="time-remaining" typ="time">測試結束前的剩餘時間。</ArgTableRow>
<ArgTableRow arg="ping-min-avg-max" typ="string">Ping 的最短、平均和最長往返時間。Ping 部分每秒傳送 20 個 ICMP 回顯請求。</ArgTableRow>
<ArgTableRow arg="jitter-min-avg-max" typ="string">各次 Ping 之間往返時間的變化：最小值、平均值和最大值。</ArgTableRow>
<ArgTableRow arg="loss" typ="string">丟失 Ping 的百分比，後跟丟失和傳送的 Ping 數，例如 `0% (0/100)`。</ArgTableRow>
<ArgTableRow arg="tcp-download" typ="string">從遠端路由器到本路由器的 TCP 吞吐量，並帶有 `local-cpu-load`，即本路由器的 CPU 負載。當遠端伺服器拒絕該使用者時顯示 `authentication failed`。</ArgTableRow>
<ArgTableRow arg="tcp-upload" typ="string">從本路由器到遠端路由器的 TCP 吞吐量，並帶有 `local-cpu-load` 和 `remote-cpu-load`，即本路由器和遠端路由器的 CPU 負載。當遠端伺服器拒絕該使用者時顯示 `authentication failed`。</ArgTableRow>
<ArgTableRow arg="udp-download" typ="string">從遠端路由器到本路由器的 UDP 吞吐量，並帶有 `local-cpu-load` 和 `remote-cpu-load`。當遠端伺服器拒絕該使用者時顯示 `authentication failed`。</ArgTableRow>
<ArgTableRow arg="udp-upload" typ="string">從本路由器到遠端路由器的 UDP 吞吐量，並帶有 `local-cpu-load` 和 `remote-cpu-load`。當遠端伺服器拒絕該使用者時顯示 `authentication failed`。</ArgTableRow>
</ArgTable>
