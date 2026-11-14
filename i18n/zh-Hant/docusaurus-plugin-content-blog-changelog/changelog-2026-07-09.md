---
title: "文件更新 - 2026 年 7 月 9 日"
date: 2026-07-09
slug: /changelog-2026-07-09
source: https://manual.mikrotik.com/changelog/changelog-2026-07-09
captured_at: '2026-11-04T06:08:11+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026 年 7 月 9 日文件變更摘要。

## 橋接與交換 {#bridging--switching}

- **[Bridge IGMP/MLD 監聽](/docs/bridging-and-switching/user-guides/bridge-igmp-mld-snooping)**：新增 querier-uses-bridge-address 橋接設定（預設 yes），該設定使橋接 IGMP 查詢器使用橋介面自身的 IPv4 地址作為查詢報文的源地址，而不是 0.0.0.0。某些組播用戶端會拒絕來自 0.0.0.0 的查詢，當監聽條目超時時，這可能會中斷組播流。它僅在啟用 igmp-snooping 和 multicast-querier 且橋接具有 IPv4 地址時適用於 IPv4 (IGMP)；MLD 查詢始終使用橋接的 IPv6 鏈路本地地址。
