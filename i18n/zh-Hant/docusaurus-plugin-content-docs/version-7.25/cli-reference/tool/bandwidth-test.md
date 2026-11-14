---
sidebar_key: "cli-reference/tool/bandwidth-test"
sidebar_position: 2
title: "bandwidth-test"
sidebar_label: 'bandwidth-test'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/tool/bandwidth-test
captured_at: '2026-11-01T21:25:53+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/bandwidth-test {#toolbandwidth-test}
**型別：** 命令

針對另一臺 RouterOS 裝置的頻寬測試伺服器（[`/tool/bandwidth-server`](./bandwidth-server/index.md)）執行頻寬測試，並每秒列印結果，直到 `duration` 結束或你停止它。該測試在一個或兩個方向上傳送 TCP 或 UDP 流量；伺服器必須已啟用，可透過 TCP 埠 2000 以及從其 `allocate-udp-ports-from` 開始的 UDP 埠訪問，並且必須開啟 `bandwidth-test` 裝置模式（參見[裝置模式](../../system-information-and-utilities/device-mode.md)）。伺服器在 [`/tool/bandwidth-server/session`](./bandwidth-server/session.md) 中列出正在執行的測試。要在一次執行中測量延遲以及 TCP 和 UDP 的兩個方向，請使用 [`/tool/speed-test`](./speed-test.md)。參見[頻寬測試](../../diagnostics-monitoring-and-troubleshooting/bandwidth-test.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="address" typ="address (flags=46viD)">伺服器的 IPv4 或 IPv6 地址。鏈路本地 IPv6 地址需要指定介面，例如 `fe80::1%ether1`。</ArgTableRow>
<ArgTableRow arg="protocol" typ="enum (udp | tcp) { udp:0, tcp:1 }">
要傳送的流量：
- `udp`（預設）- 大小為 `local-udp-tx-size` 和 `remote-udp-tx-size` 位元組的 UDP 封包；接收方統計丟失的封包。
- `tcp` - TCP 連線（`connection-count`）；TCP 會根據路徑調整其速率。
</ArgTableRow>
<ArgTableRow arg="local-udp-tx-size" typ="range">用戶端傳送的 UDP 封包大小，以整個 IP 封包的位元組數計：1500 會發送 1472 位元組的 UDP 有效載荷。小於 52 的值在 IPv4 上會失敗並顯示 `failure: size too small`。範圍 `28..64000`。預設值：1500。</ArgTableRow>
<ArgTableRow arg="remote-udp-tx-size" typ="range">伺服器傳送的 UDP 封包大小，計數方式與 `local-udp-tx-size` 相同。預設值：1500。</ArgTableRow>
<ArgTableRow arg="direction" typ="enum (receive | transmit | both) { receive:0x00000100, transmit:0x00000200, both:0x00000300 }">
哪一側傳送：
- `receive`（預設）- 伺服器傳送，用戶端接收（`rx-*` 值）。
- `transmit` - 用戶端傳送，伺服器接收（`tx-*` 值）。
- `both` - 兩側同時傳送。
</ArgTableRow>
<ArgTableRow arg="connection-count" typ="num">測試使用的 TCP 連線數，或使用各自埠的 UDP 流數量。範圍 `1..255`。預設值：20，或者在 CPU 核心數超過 20 的路由器上為 CPU 核心數。</ArgTableRow>
<ArgTableRow arg="local-tx-speed" typ="num">用戶端傳送的最大速率，單位為位元每秒（支援 `50M` 之類的字尾）。未設定時，用戶端會盡可能快地傳送：不限速的 UDP 測試在最初約一秒內會泛洪，之後傳送量會超過接收方報告的數量，因此 `lost-packets` 會保持大於零。</ArgTableRow>
<ArgTableRow arg="remote-tx-speed" typ="num">伺服器傳送的最大速率，單位為位元每秒（支援 `50M` 之類的字尾）。未設定時，伺服器會盡可能快地傳送。</ArgTableRow>
<ArgTableRow arg="user" typ="string">伺服器上的使用者名稱。該使用者所屬組需要同時具有 `test` 和 `winbox` 策略（參見 [`/user/group`](../user/group.md)）。當伺服器設定了 `authenticate=no` 時不需要。</ArgTableRow>
<ArgTableRow arg="password" typ="string">伺服器上 `user` 的密碼。</ArgTableRow>
<ArgTableRow arg="duration" typ="time">測試執行多長時間。未設定時，測試會一直執行，直到你停止它，例如使用 <kbd>Control</kbd>+<kbd>C</kbd>。</ArgTableRow>
<ArgTableRow arg="random-data" typ="bool">是否用隨機的、不可壓縮的資料填充有效載荷，以便壓縮流量的鏈路不會顯示出高於其實際承載能力的速率。這會增加雙方的 CPU 時間。預設值：no。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="status" typ="enum (connecting | can not start test | can not connect | remote is busy | test unsupported | running | disconnected | authentication failed | done testing) { connecting:0, can not start test:1, can not connect:2, remote is busy:3, test unsupported:4, running:5, disconnected:6, authentication failed:7, done testing:8 }">
測試狀態：
- `connecting` - 用戶端正在連線到伺服器。
- `running` - 測試正在執行。
- `done testing` - 測試在 `duration` 後結束。
- `authentication failed` - 伺服器拒絕了使用者名稱或密碼，或者在伺服器要求認證時未提供使用者。
- `can not connect` - 伺服器已停用或不可達，用戶端不在其 `allowed-addresses4`/`allowed-addresses6` 中，或者已達到 `max-sessions`。
- `disconnected` - 測試期間與伺服器的連線結束，測試使用的連線數超過伺服器的 `max-sessions` 時也會如此。

其他值表示伺服器拒絕或無法啟動測試。
</ArgTableRow>
<ArgTableRow arg="duration" typ="time">測試已執行多長時間。</ArgTableRow>
<ArgTableRow arg="tx-current" typ="num">用戶端在最後一秒傳送的速率。UDP 統計整個 IP 封包（包括 IP 和 UDP 頭部），TCP 僅統計 TCP 有效載荷。</ArgTableRow>
<ArgTableRow arg="tx-10-second-average" typ="num">用戶端在過去 10 秒內傳送的平均速率。</ArgTableRow>
<ArgTableRow arg="tx-total-average" typ="num">自測試開始以來用戶端傳送的平均速率。</ArgTableRow>
<ArgTableRow arg="rx-current" typ="num">用戶端在最後一秒接收的速率。UDP 統計整個 IP 封包（包括 IP 和 UDP 頭部），TCP 僅統計 TCP 有效載荷。</ArgTableRow>
<ArgTableRow arg="rx-10-second-average" typ="num">用戶端在過去 10 秒內接收的平均速率。</ArgTableRow>
<ArgTableRow arg="rx-total-average" typ="num">自測試開始以來用戶端接收的平均速率。</ArgTableRow>
<ArgTableRow arg="lost-packets" typ="num">最後一秒內丟失的 UDP 封包數量，不是自開始以來的總數。</ArgTableRow>
<ArgTableRow arg="random-data" typ="bool">測試是否使用隨機資料（`random-data`）。</ArgTableRow>
<ArgTableRow arg="direction" typ="enum (receive | transmit | both) { receive:0x00000100, transmit:0x00000200, both:0x00000300 }">測試的方向（`direction`）。</ArgTableRow>
<ArgTableRow arg="tx-size" typ="range">用戶端傳送的 UDP 封包大小，以整個 IP 封包的位元組數計。</ArgTableRow>
<ArgTableRow arg="rx-size" typ="range">用戶端接收的 UDP 封包大小，以整個 IP 封包的位元組數計。</ArgTableRow>
<ArgTableRow arg="connection-count" typ="num">測試使用的 TCP 連線數或 UDP 流數量。</ArgTableRow>
<ArgTableRow arg="local-cpu-load" typ="num">測試期間用戶端的 CPU 負載，在最初幾秒後顯示。</ArgTableRow>
<ArgTableRow arg="remote-cpu-load" typ="num">測試期間伺服器的 CPU 負載，在最初幾秒後顯示。</ArgTableRow>
<ArgTableRow arg="tcp-info" typ="multi { name: string
 }"></ArgTableRow>
</ArgTable>
