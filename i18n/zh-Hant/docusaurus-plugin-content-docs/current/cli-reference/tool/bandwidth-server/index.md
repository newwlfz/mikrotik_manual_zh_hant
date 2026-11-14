---
sidebar_key: "cli-reference/tool/bandwidth-server"
title: "bandwidth-server"
sidebar_label: 'bandwidth-server'
source: https://manual.mikrotik.com/docs/cli-reference/tool/bandwidth-server
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/bandwidth-server {#toolbandwidth-server}
**型別：** 設定目錄

頻寬測試伺服器的設定，用於響應其他 RouterOS 裝置透過 [`/tool/bandwidth-test`](../bandwidth-test.md) 和 [`/tool/speed-test`](../speed-test.md) 發起的測試。伺服器監聽 TCP 埠 2000（`/ip/service` 中的 `btest` 條目），並在從 `allocate-udp-ports-from` 起始的 UDP 埠上收發測試資料。正在執行的測試列在 [`session`](./session.md) 中。僅當 `bandwidth-test` 裝置模式開啟時才能工作（參見 [裝置模式](../../../system-information-and-utilities/device-mode.md)）。參見 [頻寬測試](../../../diagnostics-monitoring-and-troubleshooting/bandwidth-test.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="enabled" typ="bool">伺服器是否響應測試。預設值：yes。</ArgTableRow>
<ArgTableRow arg="authenticate" typ="bool">用戶端是否必須使用其所屬組具有 `test` 和 `winbox` 策略的使用者登入（參見 [`/user/group`](../../user/group.md)）。當設定為 `no` 時，任何能訪問 TCP 埠 2000 的人都可以執行會給路由器和其鏈路帶來負載的測試；對於可從網際網路訪問的路由器，不要關閉此選項。預設值：yes。</ArgTableRow>
<ArgTableRow arg="allocate-udp-ports-from" typ="num">UDP 埠範圍的起始值。伺服器和用戶端從該埠向上取用於測試資料的 UDP 埠，例如伺服器上的 2192，以及用戶端 20 個流的 2448 到 2467；防火牆必須在兩個方向上允許 UDP 流量到達這些埠。範圍 `1000..64000`。預設值：2000。</ArgTableRow>
<ArgTableRow arg="max-sessions" typ="num">同時執行的測試數量上限。計數的是測試數，而不是其連線數。當已執行這麼多測試時，新測試會收到 `can not connect`。單個測試使用的連線數也不能超過此值：當 `max-sessions=1` 時，只有 `connection-count=1` 的測試才能執行。範圍 `1..1000`。預設值：100。</ArgTableRow>
<ArgTableRow arg="allowed-addresses4" typ="object { address: ipPrefix
 }">允許執行測試的用戶端的 IPv4 地址或字首。留空則允許所有用戶端。列表之外的用戶端會收到 `can not connect`。使用此列表來限制用戶端：使用者自身的 `address` 設定不會限制頻寬測試登入。預設值：空。</ArgTableRow>
<ArgTableRow arg="allowed-addresses6" typ="object { address: ip6Prefix
 }">允許執行測試的用戶端的 IPv6 地址或字首，與 `allowed-addresses4` 相同。預設值：空。</ArgTableRow>
</ArgTable>
