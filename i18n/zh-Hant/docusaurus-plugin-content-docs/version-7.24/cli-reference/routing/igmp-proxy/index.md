---
sidebar_key: "cli-reference/routing/igmp-proxy/index"
sidebar_position: 1
title: "igmp-proxy"
sidebar_label: "igmp-proxy"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/routing/igmp-proxy
captured_at: '2026-11-01T21:29:32+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/igmp-proxy {#routingigmp-proxy}
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="quick-leave" typ="bool">指定收到 IGMP Leave 報文時採取的動作。如果 quick-leave 處於開啟狀態，那麼一旦從下游介面上的第一個用戶端收到 Leave 報文，就會立即向上遊傳送 IGMP Leave 報文。僅當下遊代理後面只有一個訂閱者時，才使用 `yes`。</ArgTableRow>
<ArgTableRow arg="query-interval" typ="time">透過下游介面傳送 IGMP Query 報文的頻率。</ArgTableRow>
<ArgTableRow arg="query-response-interval" typ="time">等待 IGMP Query 報文響應的時長。</ArgTableRow>
</ArgTable>
