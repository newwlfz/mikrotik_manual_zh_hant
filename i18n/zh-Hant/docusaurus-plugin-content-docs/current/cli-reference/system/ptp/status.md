---
sidebar_key: "cli-reference/system/ptp/status"
sidebar_position: 3
title: "status"
sidebar_label: 'status'
source: https://manual.mikrotik.com/docs/cli-reference/system/ptp/status
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/ptp/status {#systemptpstatus}
**Conditions：** !smips
**系統能力：** ptp
**型別：** Directory
每個例項和介面的當前 PTP 埠狀態。

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum">PTP 埠的介面</ArgTableRow>
<ArgTableRow arg="state" typ="string">當前埠狀態（例如 `listening`、`master` 或 `slave`）</ArgTableRow>
<ArgTableRow arg="delay" typ="num">從埠上測得的路徑延遲，以納秒為單位</ArgTableRow>
<ArgTableRow arg="port-nr" typ="num">此埠在 PTP 資料集中的埠號</ArgTableRow>
<ArgTableRow arg="as-capable" typ="bool">該埠是否符合 IEEE 802.1AS 的 asCapable 要求</ArgTableRow>
<ArgTableRow arg="neigh-freq-drift" typ="num">測得的鄰居時鐘頻率漂移，以十億分之一為單位</ArgTableRow>
</ArgTable>
