---
title: "文件更新 - 2026年6月1日"
date: 2026-06-01
slug: /changelog-2026-06-01
source: https://manual.mikrotik.com/changelog/changelog-2026-06-01
captured_at: '2026-11-04T06:07:49+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026 年 6 月 1 日所做的文件變更摘要。

## 網路管理 {#network-management}

- **[反向代理](/docs/network-management/proxy/reverse-proxy)**：新增 `vrf` 引數，用於選擇反向代理記錄所使用的虛擬路由轉發例項。更新了 `ip-address` 屬性，說明現在同時支援 IPv4 和 IPv6 伺服器地址（此前僅支援 IPv4）。
- 將側邊欄分類 **IP Services** 重新命名為 **Network Services**。

## 橋接與交換 {#bridging--switching}

- **[L3 硬體解除安裝](/docs/bridging-and-switching/l3-hardware-offloading)**：從 Marvell 交換晶片能力表中刪除了重複的 **98DX8525** 行。

## CLI 參考 {#cli-reference}

- **[CLI 參考](/docs/cli-reference)**：在起始頁新增了引數型別參考。其中記錄了該參考使用的每一種引數型別，包括 address、enum、num、time、iface_enum 和 ipPrefix，以便你理解每個命令屬性所顯示的型別。
- **[CLI 參考](/docs/cli-reference)**：修復了該章節在資料夾結構調整後出現的失效交叉引用連結，包括 BGP 頁面上的橋接連結。
