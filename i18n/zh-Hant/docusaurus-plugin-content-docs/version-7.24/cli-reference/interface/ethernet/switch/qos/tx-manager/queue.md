---
sidebar_key: "cli-reference/interface/ethernet/switch/qos/tx-manager/queue"
sidebar_position: 1
title: "queue"
sidebar_label: "queue"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/ethernet/switch/qos/tx-manager/queue
captured_at: '2026-11-01T21:27:18+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/qos/tx-manager/queue {#interfaceethernetswitchqostx-managerqueue}
**系統能力：** rbswitch 和 crs_prestera
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="*" typ="default"></ArgTableRow>
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="schedule" typ="enum (strict-priority | low-priority-group | high-priority-group) { strict-priority:0, low-priority-group:1, high-priority-group:2 }">按流量類的嚴格優先順序或組內輪詢來排程 tx</ArgTableRow>
<ArgTableRow arg="weight" typ="num">優先順序組的權重值</ArgTableRow>
<ArgTableRow arg="queue-buffers" typ="alt { queue-buffers-pct: num [ .. 100]
, queue-buffers-byte: num [1536 .. 67108864]
 }" syscap="!prestera-cpss">每佇列保留緩衝區。專用於該佇列的位元組數（或 tx-manager 的百分比）。</ArgTableRow>
<ArgTableRow arg="use-shared-buffers" typ="bool" syscap="!prestera-cpss">當埠或佇列緩衝區已滿時，允許使用共享緩衝池</ArgTableRow>
<ArgTableRow arg="wred" typ="bool" syscap="!prestera-ac3">加權隨機早期檢測</ArgTableRow>
<ArgTableRow arg="ecn" typ="bool" syscap="!prestera-ac3">顯式擁塞通知 - ECN 標記</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="tx-manager" typ="enum"></ArgTableRow>
<ArgTableRow arg="traffic-class" typ="num"></ArgTableRow>
<ArgTableRow arg="wred-actual" typ="bool" syscap="!prestera-ac3">實際 WRED 值</ArgTableRow>
<ArgTableRow arg="ecn-actual" typ="bool" syscap="!prestera-ac3">實際 ECN 值</ArgTableRow>
</ArgTable>
