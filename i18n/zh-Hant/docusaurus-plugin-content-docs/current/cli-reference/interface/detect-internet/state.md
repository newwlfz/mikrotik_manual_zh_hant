---
sidebar_key: "cli-reference/interface/detect-internet/state"
sidebar_position: 1
title: "state"
sidebar_label: 'state'
source: https://manual.mikrotik.com/docs/cli-reference/interface/detect-internet/state
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/detect-internet/state {#interfacedetect-internetstate}
**型別：** 目錄

Detect Internet 所監視的每個介面的只讀狀態（即 [`/interface/detect-internet`](./index.md) 中 `detect-interface-list` 的介面）。參見 [檢測網際網路](../../../diagnostics-monitoring-and-troubleshooting/detect-internet.md)。

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="iface_enum">被監視的介面。</ArgTableRow>
<ArgTableRow arg="state" typ="enum (no-link | unknown | lan | wan | internet | slave) { no-link:0, unknown:1, lan:2, wan:3, internet:4, slave:5 }">
介面狀態：
- `no-link` - 介面沒有鏈路。
- `unknown` - 路由器正在檢查該介面，大約 6 秒。
- `lan` - 二層介面的起始狀態，以及鏈路變化後的狀態。保持為 `lan` 一小時的介面會被鎖定，直到下一次鏈路變化。
- `wan` - 路由器到 8.8.8.8 的活動路由經過該介面。三層隧道在其鏈路接通時變為 `wan`。`wan` 介面只有在鏈路變化後才會回到 `lan`。
- `internet` - 一個 `wan` 介面，路由器透過它到達 UDP 埠 30000 上的 `cloud.mikrotik.com`。
- `slave` - 該介面是網橋或其他介面的埠。
</ArgTableRow>
<ArgTableRow arg="state-change-time" typ="date">介面獲得當前狀態的時間。</ArgTableRow>
<ArgTableRow arg="cloud-rtt" typ="time">透過該介面進行的最後一次雲檢查的往返時間。當介面不是 `internet` 時為空。</ArgTableRow>
</ArgTable>
