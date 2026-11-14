---
sidebar_key: "cli-reference/tool/graphing"
title: "graphing"
sidebar_label: 'graphing'
source: https://manual.mikrotik.com/docs/cli-reference/tool/graphing
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/graphing {#toolgraphing}
**型別：** 設定目錄

常規 graphing 設定：收集的資料寫入系統儲存的頻率，以及 graph 網頁重新載入的頻率。繪製哪些內容以及誰可以檢視，由 [`interface`](./interface.md)、[`queue`](./queue.md) 和 [`resource`](./resource.md) 中的規則決定；路由器預設沒有任何規則。參見 [圖表](../../../diagnostics-monitoring-and-troubleshooting/graphing.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="store-every" typ="enum (5min | hour | 24hours) { 5min:1, hour:2, 24hours:3 }">
路由器將 `store-on-disk=yes` 的規則所收集的資料寫入系統儲存的頻率。間隔越長，寫入儲存的次數越少。從 RouterOS 重啟會保留自上次寫入以來收集的資料。
- `5min`（預設）- 每 5 分鐘。
- `hour` - 每小時。
- `24hours` - 每天一次。
</ArgTableRow>
<ArgTableRow arg="page-refresh" typ="enum (never) { never:0x0 }">HTML 頁面的重新整理頻率（以秒為單位）。Web 伺服器將該值作為 graph 頁面的 HTTP `refresh` 頭髮送，因此瀏覽器會重新載入這些頁面。`never` 會省略該頭，頁面不會自行重新載入。預設值：300。</ArgTableRow>
</ArgTable>
