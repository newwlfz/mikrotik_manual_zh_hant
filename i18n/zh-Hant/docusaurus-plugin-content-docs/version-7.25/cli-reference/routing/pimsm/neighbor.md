---
sidebar_key: "cli-reference/routing/pimsm/neighbor"
sidebar_position: 6
title: "neighbor"
sidebar_label: 'neighbor'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/routing/pimsm/neighbor
captured_at: '2026-11-01T21:25:16+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/pimsm/neighbor {#routingpimsmneighbor}
**條件：** !smips
**型別：** 目錄

neighbor 選單顯示所有檢測到的、正在執行 PIM 的鄰居及其狀態。此選單包含動態和只讀條目。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="R" typ="designated-router">該鄰居是網段上選舉出的指定路由器（DR）。</ArgTableRow>
<ArgTableRow arg="J" typ="join-tracking">該鄰居支援加入跟蹤。它會在其 Hello 訊息的 LAN Prune Delay 選項中設定 Tracking (T) 位。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="instance" typ="enum">檢測到該鄰居的 PIM 例項名稱。</ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46i)">顯示鄰居的 IP 地址以及檢測到該鄰居的本地介面。</ArgTableRow>
<ArgTableRow arg="priority" typ="num">表示鄰居的優先順序值。</ArgTableRow>
<ArgTableRow arg="timeout" typ="time">顯示在未收到新的 Hello 訊息時，鄰居從列表中移除前的剩餘時間。保持時間等於鄰居的 `hello-period * 3.5`。</ArgTableRow>
<ArgTableRow arg="propagation-delay" typ="time">表示鄰居在 Hello 訊息的 LAN Prune Delay 選項中的傳播延遲值。</ArgTableRow>
<ArgTableRow arg="override-interval" typ="time">表示鄰居在 Hello 訊息的 LAN Prune Delay 選項中的覆蓋間隔值。</ArgTableRow>
</ArgTable>
