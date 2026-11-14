---
sidebar_key: "cli-reference/routing/pimsm/interface-template"
sidebar_position: 4
title: "interface-template"
sidebar_label: "interface-template"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/routing/pimsm/interface-template
captured_at: '2026-11-01T21:29:37+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/pimsm/interface-template {#routingpimsminterface-template}
**條件：** !smips
**型別：** 目錄

介面模板選單定義哪些介面將參與 PIM，以及將使用什麼逐介面配置。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未啟用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="instance" typ="enum" mandatory="1">此介面模板所屬的 PIM 例項名稱。</ArgTableRow>
<ArgTableRow arg="interfaces" typ="object { interface: iface_enum
 }" unset="1">將參與 PIM 的介面列表。</ArgTableRow>
<ArgTableRow arg="hello-period" typ="time">Hello 訊息的週期間隔。</ArgTableRow>
<ArgTableRow arg="hello-delay" typ="time">介面啟動或檢測到新鄰居時，初始 Hello 訊息的隨機間隔。</ArgTableRow>
<ArgTableRow arg="priority" typ="num">指定路由器（DR）優先順序。每個網路選舉一個指定路由器。僅當所有鄰居都通告了優先順序選項時才使用優先順序。數值最大的優先順序優先。如果出現平局或未使用優先順序，則數值最大的 IP 地址優先。</ArgTableRow>
<ArgTableRow arg="join-prune-period" typ="time"></ArgTableRow>
<ArgTableRow arg="propagation-delay" typ="time">設定 prune pending 計時器的值。上游路由器用它來確定在修剪啟用了 Join 抑制的介面之前，應等待 Join 覆蓋訊息多長時間。</ArgTableRow>
<ArgTableRow arg="override-interval" typ="time">設定最大時間段，用於在啟用了 Join 抑制的網路上排程延遲的 Join 覆蓋訊息時進行隨機化。</ArgTableRow>
<ArgTableRow arg="join-tracking-support" typ="bool">設定 Hello 訊息中 LAN Prune Delay 選項的 Tracking (T) 位的值。啟用後，路由器會通告其停用 Join 抑制的意願。如果停用了 Join 抑制，上游路由器可以顯式跟蹤各個下游路由器的加入成員關係。除非鏈路中的所有 PIM 路由器都協商此能力，否則無法進行顯式跟蹤，也無法停用 Join 抑制機制。</ArgTableRow>
<ArgTableRow arg="source-addresses" typ="object { address: address (flags=46)
 }" unset="1"></ArgTableRow>
</ArgTable>
