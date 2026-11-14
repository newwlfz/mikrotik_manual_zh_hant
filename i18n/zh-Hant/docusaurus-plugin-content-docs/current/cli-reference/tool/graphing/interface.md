---
sidebar_key: "cli-reference/tool/graphing/interface"
sidebar_position: 1
title: "interface"
sidebar_label: 'interface'
source: https://manual.mikrotik.com/docs/cli-reference/tool/graphing/interface
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/graphing/interface {#toolgraphinginterface}
**型別：** 目錄

這些規則用於選擇要繪製圖表的介面，以及哪些用戶端可以在路由器的 `/graphs/` 網頁（`/graphs/iface/<interface>/`）上檢視其流量圖表。在新增規則之前，不會繪製任何圖表。可以為同一個介面新增多條規則，每條規則都有自己的 `allow-address`；只要其中任意一條規則允許某個用戶端的地址，該用戶端就能看到圖表。介面規則不會開放資源圖表或佇列圖表。圖表中，`In` 表示介面接收的流量，`Out` 表示介面傳送的流量，單位為位元/秒。參見 [圖表](../../../diagnostics-monitoring-and-troubleshooting/graphing.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用的規則：不顯示其圖表。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum { all:0 }">要繪製圖表的介面。`all` 會為每個介面繪製圖表，也包括已停用的介面、迴環介面 `lo` 以及存在期間的動態介面，例如 PPPoE 使用者。針對某個動態介面的規則會在該介面重新建立時失去它，例如 PPPoE 使用者重新連線時（此時規則會顯示類似 `*F00000` 的 ID）；請改為繪製靜態 PPPoE 伺服器繫結的圖表。現有規則的介面無法更改（`Can't change interface, please create new config`）：請刪除該規則並新增新規則。預設：all。</ArgTableRow>
<ArgTableRow arg="allow-address" typ="alt { ip-prefix: ipPrefix
, ipv6-prefix: ip6Prefix
 }">可以在路由器 `/graphs/` 網頁上檢視此介面圖表的用戶端的 IPv4 或 IPv6 字首。這些頁面無需登入。更改會立即生效。要允許多個字首，請為每個字首新增一條規則。預設：0.0.0.0/0（每個 IPv4 地址）。</ArgTableRow>
<ArgTableRow arg="store-on-disk" typ="bool">
- `yes`（預設） - 將收集的資料儲存在系統儲存中：圖表在重啟後仍會保留。資料每隔 [`store-every`](./index.md) 寫入一次。
- `no` - 僅將資料儲存在 RAM 中：重啟後圖表會從空白開始。
</ArgTableRow>
</ArgTable>
