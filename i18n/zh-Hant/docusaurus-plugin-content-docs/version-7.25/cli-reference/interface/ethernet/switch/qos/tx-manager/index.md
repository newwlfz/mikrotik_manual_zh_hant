---
sidebar_key: "cli-reference/interface/ethernet/switch/qos/tx-manager/index"
sidebar_position: 1
title: "tx-manager"
sidebar_label: 'tx-manager'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/ethernet/switch/qos/tx-manager
captured_at: '2026-11-01T21:22:40+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/qos/tx-manager {#interfaceethernetswitchqostx-manager}
**系統能力：** rbswitch 和 crs_prestera
**型別：** 目錄

傳輸（Tx）管理器控制封包入隊傳輸和傳輸順序。不同的交換器埠可以分配到不同的 Tx 管理器。硬體 Tx 管理器的最大數量取決於交換晶片型號。

:::info
埠狀態不會影響已分配的資源。如果執行中的埠與斷開或停用的埠都分配到同一 Tx 管理器，則它們會獲得相同數量的佇列緩衝區。
:::

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="*" typ="default"></ArgTableRow>
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1">Tx Manager 名稱。</ArgTableRow>
<ArgTableRow arg="queue-buffers" typ="alt { queue-buffers-pct: num [ .. 100]
, queue-buffers-byte: num [1536 .. 67108864]
 }">分配給連結到此 Tx Manager 的所有埠的總硬體 Tx 緩衝區數量。除 **auto** 以外的任何值都不按埠數量進行縮放。例如，如果 queue-buffers=30%，且有 3 個埠使用此 Tx Manager，則每個相應埠獲得總可用資源的 10%。再向該 Tx Manager 新增兩個埠會使每埠緩衝區降至 6%（30/5）。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="hw-id" typ="num"></ArgTableRow>
</ArgTable>
