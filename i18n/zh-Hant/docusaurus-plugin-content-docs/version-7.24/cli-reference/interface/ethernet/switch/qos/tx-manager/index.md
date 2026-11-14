---
sidebar_key: "cli-reference/interface/ethernet/switch/qos/tx-manager/index"
sidebar_position: 1
title: "tx-manager"
sidebar_label: "tx-manager"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/ethernet/switch/qos/tx-manager
captured_at: '2026-11-01T21:27:17+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/qos/tx-manager {#interfaceethernetswitchqostx-manager}
**系統能力：** rbswitch 和 crs_prestera
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="*" typ="default"></ArgTableRow>
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1">Tx Manager 名稱</ArgTableRow>
<ArgTableRow arg="queue-buffers" typ="alt { queue-buffers-pct: num [ .. 100]
, queue-buffers-byte: num [1536 .. 67108864]
 }">專門為 Tx Manager 保留的位元組數（或百分比）。該值會按已分配埠的活動佇列進行拆分。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="hw-id" typ="num"></ArgTableRow>
</ArgTable>
