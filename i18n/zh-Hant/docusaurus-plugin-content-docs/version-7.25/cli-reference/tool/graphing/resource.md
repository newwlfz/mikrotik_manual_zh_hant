---
sidebar_key: "cli-reference/tool/graphing/resource"
sidebar_position: 3
title: "resource"
sidebar_label: 'resource'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/tool/graphing/resource
captured_at: '2026-11-01T21:25:55+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/graphing/resource {#toolgraphingresource}
**型別：** 目錄

用於控制 CPU、記憶體和磁碟使用率圖表（路由器網頁上的 `/graphs/cpu/`、`/graphs/ram/` 和 `/graphs/hdd/`）的規則，以及哪些用戶端可以檢視這些圖表。新增規則之前不會繪製任何圖表。你可以新增多條規則，每條規則都有自己的 `allow-address`；只要其中任意一條規則允許某個用戶端的地址，該用戶端就能看到圖表。資源規則不會開啟介面或佇列圖表。請參閱[圖表](../../../diagnostics-monitoring-and-troubleshooting/graphing.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用的規則：不顯示其圖表。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="allow-address" typ="alt { ip-prefix: ipPrefix
, ipv6-prefix: ip6Prefix
 }">可在路由器 `/graphs/` 網頁上檢視 CPU、記憶體和磁碟圖表的用戶端的 IPv4 或 IPv6 字首。這些頁面無需登入。更改會立即生效。要允許多個字首，請為每個字首新增一條規則。預設：0.0.0.0/0（所有 IPv4 地址）。</ArgTableRow>
<ArgTableRow arg="store-on-disk" typ="bool">
- `yes`（預設） - 將收集的資料儲存在系統儲存中：圖表在重啟後仍會保留。資料每隔 [`store-every`](./index.md) 寫入一次。
- `no` - 僅將資料儲存在 RAM 中：重啟後圖表會從空白開始。
</ArgTableRow>
</ArgTable>
