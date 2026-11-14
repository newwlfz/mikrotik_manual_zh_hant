---
title: "文件更新 - 2026年10月29日"
date: 2026-10-29T00:00:00.000Z
slug: /changelog-2026-10-29
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

# 文件更新 - 2026年10月29日 {#documentation-updates---october-29-2026}

October 29, 2026

2026年10月29日所做文件變更的摘要。

## 橋接與交換[​](#bridging--switching "Direct link to Bridging & Switching") {#bridging--switching}

-   **[其他交換晶片功能](/docs/bridging-and-switching/switch-chip-features#port-isolation)**: 埠隔離 `forwarding-override` 可以引用介面列表。其埠會被新增到顯式列出的埠，結果集合顯示在只讀的 `current-forwarding-override` 中，並且介面列表不能排除埠。該 [`/interface/ethernet/switch/port-isolation`](/docs/cli-reference/interface/ethernet/switch/port-isolation) 參考文件描述了其所有引數。

## 高可用性解決方案[​](#high-availability-solutions "Direct link to High Availability Solutions") {#high-availability-solutions}

-   **[多機箱鏈路聚合組](/docs/high-availability-solutions/multi-chassis-link-aggregation-group)**: 必須在整個交換器上停用 L3 硬體解除安裝（`/interface/ethernet/switch/set 0 l3-hw-offloading=no`）；僅在各個交換器埠上停用它是不夠的。

**Tags:**

-   [文件變更日誌](/changelog/tags/changelog "文件更新的每日摘要")
