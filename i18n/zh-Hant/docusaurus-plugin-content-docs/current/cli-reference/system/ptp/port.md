---
sidebar_key: "cli-reference/system/ptp/port"
sidebar_position: 2
title: "port"
sidebar_label: 'port'
source: https://manual.mikrotik.com/docs/cli-reference/system/ptp/port
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/ptp/port {#systemptpport}
**條件：** !smips
**系統能力：** ptp
**型別：** 目錄
PTP 埠：加入某個 [`/system/ptp`](./index.md) 配置檔案例項的介面。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="I" typ="inactive">未啟用</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="ptp" typ="enum" mandatory="1">此埠加入的 [`/system/ptp`](./index.md) 配置檔案例項</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">用於 PTP 的介面（硬體必須支援 PTP 時間戳 — 請參閱[指南](../../../system-information-and-utilities/precision-time-protocol.md)中的受支援裝置列表）</ArgTableRow>
<ArgTableRow arg="role" typ="enum (bmca | master | slave)">埠角色選擇：`bmca`（由最佳主時鐘演算法在主時鐘和從時鐘之間決定），或固定的 `master` 或 `slave`</ArgTableRow>
<ArgTableRow arg="announce-interval" typ="num">announce 訊息間隔的 Log2 值（秒）（例如 -3...4 對應 0.125s-16s）</ArgTableRow>
<ArgTableRow arg="sync-interval" typ="num">sync 訊息間隔的 Log2 值（秒）</ArgTableRow>
<ArgTableRow arg="delay-interval" typ="num">delay request 訊息間隔的 Log2 值（秒）（E2E 模式）</ArgTableRow>
<ArgTableRow arg="pdelay-interval" typ="num">peer delay 訊息間隔的 Log2 值（秒）（P2P 模式）</ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num">當介面承載帶標籤的 PTP 流量時，埠在該 VLAN ID 下參與 PTP</ArgTableRow>
</ArgTable>
