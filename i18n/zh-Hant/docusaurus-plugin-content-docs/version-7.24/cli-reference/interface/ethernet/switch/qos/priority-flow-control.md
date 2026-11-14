---
sidebar_key: "cli-reference/interface/ethernet/switch/qos/priority-flow-control"
sidebar_position: 4
title: "priority-flow-control"
sidebar_label: "priority-flow-control"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/ethernet/switch/qos/priority-flow-control
captured_at: '2026-11-01T21:27:17+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/qos/priority-flow-control {#interfaceethernetswitchqospriority-flow-control}
**系統能力：** rbswitch and crs_prestera and !prestera-ac3
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="*" typ="default"></ArgTableRow>
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1">PFC 配置檔名稱</ArgTableRow>
<ArgTableRow arg="traffic-class" typ="multi { array-id, tc: num [ .. 7]
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="rx" typ="bool">接收（並遵循）PFC 幀</ArgTableRow>
<ArgTableRow arg="tx" typ="bool">傳送 PFC 幀</ArgTableRow>
<ArgTableRow arg="pause-threshold" typ="alt { pause-threshold-pct: num [ .. 100]
, pause-threshold-byte: num [1536 .. ]
 }">當排隊報文的總大小達到此閾值時，傳送暫停幀（XOFF）</ArgTableRow>
<ArgTableRow arg="resume-threshold" typ="alt { resume-threshold-pct: num [ .. 100]
, resume-threshold-byte: num [256 .. ]
 }">當排隊報文的總大小降至此閾值時，傳送恢復幀（XON）</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="hw-id" typ="num"></ArgTableRow>
</ArgTable>
