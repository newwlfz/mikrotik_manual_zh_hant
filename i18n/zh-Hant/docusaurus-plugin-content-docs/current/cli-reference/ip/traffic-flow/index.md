---
sidebar_key: "cli-reference/ip/traffic-flow"
title: "traffic-flow"
sidebar_label: 'traffic-flow'
source: https://manual.mikrotik.com/docs/cli-reference/ip/traffic-flow
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/traffic-flow {#iptraffic-flow}
**型別：** 設定目錄
Traffic-Flow（相容 NetFlow/IPFIX）配置。使用 `enabled=yes` 將其開啟，並在 [`target`](./target.md) 下新增匯出目標。流量僅透過路由器的 CPU 路徑，因此經硬體解除安裝的流量無法被匯出。請參閱 [流量監控](../../../diagnostics-monitoring-and-troubleshooting/traffic-flow/index.md) 指南。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="enabled" typ="bool">啟用或停用 Traffic-Flow 服務</ArgTableRow>
<ArgTableRow arg="interfaces" typ="multi { array-id, interface-or-list: alt { interface: iface_enum { local:0, all:0xFFFFFFFF }
, interface-list: enum
 }
 }">以逗號分隔的介面名稱（或 `all`），其轉發的流量將被統計</ArgTableRow>
<ArgTableRow arg="cache-entries" typ="enum (1k | 2k | 4k | 8k | 16k | 32k | 64k | 128k | 256k | 512k | 1M | 2M | 4M | 8M | 16M | 32M) { 1k:0x400, 2k:0x800, 4k:0x1000, 8k:0x2000, 16k:0x4000, 32k:0x8000, 64k:0x10000, 128k:0x20000, 256k:0x40000, 512k:0x80000, 1M:0x100000, 2M:0x200000, 4M:0x400000, 8M:0x800000, 16M:0x1000000, 32M:0x2000000 }">一次儲存在記憶體中的流記錄數量（預設值取決於裝置記憶體：較大的板卡上為 256k，最小的板卡上低至 4k）</ArgTableRow>
<ArgTableRow arg="active-flow-timeout" typ="time">流的最大生存時間，即使封包持續匹配該流也是如此；超過此時間後該流會過期並被匯出。預設值：30m</ArgTableRow>
<ArgTableRow arg="inactive-flow-timeout" typ="time">如果某個流在這麼長時間內沒有收到任何封包，就會過期並被匯出；下一個封包將開始一個新流。如果超時時間太短，可能會產生大量流並使緩衝區溢位。預設值：15s</ArgTableRow>
<ArgTableRow arg="packet-sampling" typ="bool">啟用封包取樣：僅按照 `sampling-interval` 和 `sampling-space` 統計封包</ArgTableRow>
<ArgTableRow arg="sampling-interval" typ="num">每個取樣週期中被取樣的連續封包數量</ArgTableRow>
<ArgTableRow arg="sampling-space" typ="num">每個取樣週期中被省略的連續封包數量</ArgTableRow>
</ArgTable>
