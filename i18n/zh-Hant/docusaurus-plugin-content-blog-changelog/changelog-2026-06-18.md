---
title: "文件更新 - 2026年6月18日"
date: 2026-06-18
slug: /changelog-2026-06-18
source: https://manual.mikrotik.com/changelog/changelog-2026-06-18
captured_at: '2026-11-04T06:08:01+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026 年 6 月 18 日文件變更摘要。

## 入門 {#getting-started}

- **[首次配置](/docs/getting-started/first-time-configuration)**：對指南進行了大幅精簡。整合了 WAN/網際網路部分，並加入 CLI 和 WinBox 的標籤頁示例；明確了執行預設配置的使用者在 NAT 與橋接行為上的區別；合併了驗證步驟；修正了若干命令錯誤。無線部分精簡至基礎內容，並提供了指向無線部分的連結；刪除了重複的 CLI 部分；修復了錯誤的步驟編號以及第 4 步的格式問題（現在已使用正確的標題）。入門側邊欄也已重新排序，以符合新使用者流程。
- **[手動網路設定](/docs/getting-started/manual-network-setup)**：新頁面。手動（no-default-config）設定流程已從首次配置指南中拆分出來，放入其專屬頁面。
- **[保護您的路由器](/docs/getting-started/securing-your-router)**：將去重後的安全和防火牆內容從首次配置指南移出，放入此專屬頁面。

## 橋接與交換 {#bridging--switching}

- **[SwOS 故障排除](/docs/bridging-and-switching/swos/troubleshooting)**：透過移除冗餘的“適用於”和“另請參閱”部分以及失效的外部 Confluence 交叉引用，並簡化韌體下載連結，清理了該頁面。[CSS106](/docs/bridging-and-switching/swos/css106) 和 [CSS610](/docs/bridging-and-switching/swos/css610) 頁面已更新為連結到內部 Neighbor Discovery 文件，而不是舊的外部幫助站點。
