---
sidebar_key: "cli-reference/routing/igmp-proxy"
title: "igmp-proxy"
sidebar_label: 'igmp-proxy'
source: https://manual.mikrotik.com/docs/cli-reference/routing/igmp-proxy
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/igmp-proxy {#routingigmp-proxy}
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="robustness" typ="num">IGMP 代理的 robustness 值，用作查詢的重傳次數以及丟包容忍度。沒有自己的 robustness 設定的介面會繼承該值。</ArgTableRow>
<ArgTableRow arg="query-interval" typ="time">透過下游介面傳送 IGMP Query 訊息的頻率。</ArgTableRow>
<ArgTableRow arg="query-response-interval" typ="time">等待對 IGMP Query 訊息的響應的時間。</ArgTableRow>
<ArgTableRow arg="last-member-query-interval" typ="time">在 Leave 訊息之後為驗證沒有組成員殘留而傳送的組特定查詢的超時時間。</ArgTableRow>
</ArgTable>
