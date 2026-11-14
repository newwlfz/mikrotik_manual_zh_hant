---
sidebar_key: "cli-reference/interface/ethernet/switch/qos/tx-manager/queue"
sidebar_position: 1
title: "queue"
sidebar_label: 'queue'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/ethernet/switch/qos/tx-manager/queue
captured_at: '2026-11-01T21:22:41+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/qos/tx-manager/queue {#interfaceethernetswitchqostx-managerqueue}
**系統能力：** rbswitch 和 crs_prestera
**型別：** 目錄

每個埠有八個 Tx 佇列。分配的 Tx 管理器控制封包入隊並排程傳輸順序。每個佇列可以具有嚴格優先順序（其中具有最高流量類別的封包始終優先傳輸），也可以分組在一起進行加權輪詢 tx 排程。

建立 Tx 管理器會自動建立所有八個相應的佇列排程器。

:::danger
更改 Tx 管理器或佇列的任何屬性都會在解除安裝過程中完全停止流量入隊和傳輸。裝置轉發流量時預計會出現臨時丟包。
:::

:::danger
在某些裝置型號上，由於硬體限制，在一個佇列上啟用 ECN 會為所有佇列上支援 ECN 的封包開啟 CE 標記。在這種情況下，儘管 `ecn=no`，但 `ecn-actual=yes`。
:::

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="*" typ="default"></ArgTableRow>
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="schedule" typ="enum (strict-priority | low-priority-group | high-priority-group) { strict-priority:0, low-priority-group:1, high-priority-group:2 }">
根據流量類別的嚴格優先順序或組內輪詢來排程 Tx。
- strict-priority - 相應佇列中的封包總是先被排程，然後才轉到較低流量類別。在當前佇列清空之前，不會發送具有較低流量類別的封包。
- high-priority-group - 組內所有佇列透過加權輪詢原則一起排程。例如，如果 TC5 的權重為 4，TC4 為 3，TC3 為 2，則排程器在一輪中從 queue5 傳送 4 個數據包、從 Q4 傳送 3 個數據包、從 Q3 傳送 2 個數據包。為降低延遲，每一輪會在組內所有佇列之間進行“切片”。換言之，上述示例每一輪的封包順序為 “Q5, Q4, Q3, Q5, Q4, Q3, Q5, Q4, Q5”。
- low-priority-group - 邏輯與 high-priority-group 類似，但僅當 high-priority-group 中的所有佇列為空時，才會排程 low-priority-group。
</ArgTableRow>
<ArgTableRow arg="weight" typ="num">如果流量類別是排程組的成員，則為該流量類別的權重值。在嚴格優先順序排程的情況下不使用此欄位。</ArgTableRow>
<ArgTableRow arg="queue-buffers" typ="alt { queue-buffers-pct: num [ .. 100]
, queue-buffers-byte: num [1536 .. 67108864]
 }" syscap="!prestera-cpss">分配給此佇列的硬體 Tx 緩衝區數量。除 **auto** 外的任何值都不會按埠數量縮放，即該值會在連線到該 Tx Manager 的埠之間拆分。當以百分比給出時，它表示 tx-manager 的 queue-buffers 值的百分比。</ArgTableRow>
<ArgTableRow arg="use-shared-buffers" typ="bool" syscap="!prestera-cpss">允許佇列在 **queue-buffers** 已滿時使用共享緩衝區池。如果佇列已滿且共享緩衝區已停用，則封包會被丟棄。如果共享緩衝區已啟用，佇列最多可從共享池使用 **shared-packet-cap** 或 **shared-poolX-packet-cap** 個數據包（詳見 [QoS 設定](../settings.md)）。</ArgTableRow>
<ArgTableRow arg="wred" typ="bool" syscap="!prestera-ac3">為給定佇列啟用/停用[加權隨機早期檢測](../../../../../../bridging-and-switching/quality-of-service.md#weighted-random-early-detection-wred)。</ArgTableRow>
<ArgTableRow arg="ecn" typ="bool" syscap="!prestera-ac3">啟用/停用所傳送封包的 ECN 標記。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="tx-manager" typ="enum">關聯的 Tx Manager</ArgTableRow>
<ArgTableRow arg="traffic-class" typ="num">排程器控制的流量類別（tc0..tc7）及相應的埠佇列（queue0..queue7）。</ArgTableRow>
<ArgTableRow arg="wred-actual" typ="bool" syscap="!prestera-ac3">實際 WRED 值</ArgTableRow>
<ArgTableRow arg="ecn-actual" typ="bool" syscap="!prestera-ac3">實際 ECN 值</ArgTableRow>
</ArgTable>
