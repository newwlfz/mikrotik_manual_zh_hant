---
sidebar_key: "cli-reference/interface/ethernet/switch/qos/priority-flow-control"
sidebar_position: 4
title: "priority-flow-control"
sidebar_label: 'priority-flow-control'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/ethernet/switch/qos/priority-flow-control
captured_at: '2026-11-01T21:22:41+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/qos/priority-flow-control {#interfaceethernetswitchqospriority-flow-control}
**系統能力：** rbswitch and crs_prestera and !prestera-ac3
**型別：** 目錄

[PFC](../../../../../bridging-and-switching/quality-of-service.md#priority-based-flow-control-pfc) 配置按配置檔案組織。不同的交換器埠可以分配到不同的 PFC 配置檔案。硬體 Tx 管理器的最大數量取決於交換晶片型號。名為“**disabled**”的內建配置檔案無法更改。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="*" typ="default"></ArgTableRow>
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1">PFC 配置檔案的使用者自定義名稱。</ArgTableRow>
<ArgTableRow arg="traffic-class" typ="multi { array-id, tc: num [ .. 7]
 }" mandatory="1">已啟用 PFC 的流量類別列表。</ArgTableRow>
<ArgTableRow arg="rx" typ="bool">啟用接收 PFC 幀。收到的 PFC 幀會在該 PFC 幀指定的持續時間內暫停接收到該 PFC 幀的埠上的特定優先順序佇列。停用 rx 會停用佇列暫停。</ArgTableRow>
<ArgTableRow arg="tx" typ="bool">啟用傳送 PFC 幀。</ArgTableRow>
<ArgTableRow arg="pause-threshold" typ="alt { pause-threshold-pct: num [ .. 100]
, pause-threshold-byte: num [1536 .. ]
 }">當入隊封包的總大小達到此閾值時，傳送暫停幀 (XOFF)。入隊封包按入埠計數。僅當 **tx=yes** 時生效。該值可以以位元組為單位顯式給出，或按相應共享池大小 (**shared-poolX-byte-cap**) 的百分比給出。</ArgTableRow>
<ArgTableRow arg="resume-threshold" typ="alt { resume-threshold-pct: num [ .. 100]
, resume-threshold-byte: num [256 .. ]
 }">當入隊封包的總大小降至此閾值時，傳送恢復幀 (XON)。入隊封包按入埠計數。僅當 **tx=yes** 時生效。該值可以以位元組為單位顯式給出，或按相應共享池大小 (**shared-poolX-byte-cap**) 的百分比給出。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="hw-id" typ="num"></ArgTableRow>
</ArgTable>
