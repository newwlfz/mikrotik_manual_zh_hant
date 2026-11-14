---
sidebar_key: "cli-reference/tool/graphing/queue"
sidebar_position: 2
title: "queue"
sidebar_label: 'queue'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/tool/graphing/queue
captured_at: '2026-11-01T21:25:54+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/graphing/queue {#toolgraphingqueue}
**型別：** 目錄

這些規則用於選擇哪些簡單佇列會被繪製成圖，以及哪些用戶端可以在路由器的 `/graphs/` 網頁上檢視這些佇列的流量圖（`/graphs/queue/<queue>/`，其中名稱經過 URL 編碼）。在新增規則之前，不會繪製任何圖形。當針對某個佇列的規則允許用戶端地址時，或者當 `allow-target=yes` 且用戶端地址位於該佇列的 `target` 中時，用戶端就能看到該佇列的圖形。佇列規則不會開啟介面或資源圖形。圖形中 `In` 表示發往目標（下載）的流量，`Out` 表示來自目標（上傳）的流量，同時也顯示為佇列 `max-limit` 的佔比。請參閱 [圖表](../../../diagnostics-monitoring-and-troubleshooting/graphing.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用的規則：不顯示其圖表。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="simple-queue" typ="enum (all) { all:0 }">要繪製圖形的簡單佇列，按名稱指定。`all` 會為每個簡單佇列繪製圖形，也包括之後新增的佇列以及 PPP 使用者的動態佇列。現有規則的佇列無法更改（`Can't change queue, please create new config`）：請刪除該規則並新增新規則。預設：all。</ArgTableRow>
<ArgTableRow arg="allow-address" typ="alt { ip-prefix: ipPrefix
, ipv6-prefix: ip6Prefix
 }">可以在路由器的 `/graphs/` 網頁上檢視此規則所對應佇列圖形的用戶端的 IPv4 或 IPv6 字首。這些頁面無需登入。更改會立即生效。要允許多個字首，請為每個字首新增一條規則。預設：0.0.0.0/0（所有 IPv4 地址）。</ArgTableRow>
<ArgTableRow arg="store-on-disk" typ="bool">
- `yes`（預設） - 將收集的資料儲存在系統儲存中：圖表在重啟後仍會保留。資料每隔 [`store-every`](./index.md) 寫入一次。
- `no` - 僅將資料儲存在 RAM 中：重啟後圖表會從空白開始。
</ArgTableRow>
<ArgTableRow arg="allow-target" typ="bool">
佇列的 `target` 中的地址是否也能看到該佇列的圖表，從而使 simple queue 的每個客戶都能看到自己的流量。只要任一規則允許，用戶端就能看到圖表，因此另一條設定為 `no` 的規則不會隱藏此規則所顯示的圖表。
- `yes`（預設）- target 中的每個地址除 `allow-address` 之外還能看到圖表。目標為子網的佇列會向整個子網顯示其圖表；目標為 0.0.0.0/0 或某個介面的佇列（例如 PPP 使用者的動態佇列）會向每個能訪問到 Web 伺服器的用戶端顯示其圖表。
- `no` - 只有 `allow-address` 能看到圖表。
</ArgTableRow>
</ArgTable>
