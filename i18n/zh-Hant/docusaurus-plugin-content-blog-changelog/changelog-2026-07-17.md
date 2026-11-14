---
title: "文件更新 - 2026年7月17日"
date: 2026-07-17
slug: /changelog-2026-07-17
source: https://manual.mikrotik.com/changelog/changelog-2026-07-17
captured_at: '2026-11-04T06:08:14+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026 年 7 月 17 日的文件變更摘要。

## 使用者指南 {#user-guides}

- **[PIM-SM](/docs/user-guides/routing-and-networking-protocols/multicast/pim-sm)**：重做了配置示例。基礎示例現在將 PIM 介面模板與面向用戶端介面的獨立 igmp-interface-template 分開，這樣 PIM 例項就能獲知本地組播組成員關係。靜態 RP 示例用內建的 lo 介面替換了 loopback 網橋，併為 R2 和 R3 添加了 IGMP 查詢器配置。
- **[IGMP proxy](/docs/user-guides/routing-and-networking-protocols/multicast/igmp-proxy)**：移除了 quick-leave 配置示例。

## 硬體指南 {#hardware-guides}

- **[hAP ax 2](/hardware/hap-ax-2) 和 [hAP ax 3](/hardware/hap-ax-3)**：重新命名了 hAP ax 頁面，使頁面名稱與產品一致 — 原先的 hap-ax 頁面現在是 hap-ax-3，而 hap-ax-2 現在存放 hAP ax 2 的內容。指向舊 hap-ax URL 的現有書籤需要更新。
- **[無線系統](/hardware/ldf-5-series)**：為 LDF 5、SXT SA 和 SXT SQ 系列頁面以及若干 LTE 套件頁面添加了來自 mikrotik.com 的產品圖片。
- **[硬體指南](/hardware/)**：176 個裝置頁面中的 WinBox 下載連結現在都使用 mt.lv/winbox 短連結，預設 IP 地址 192.168.88.1 現在透過顯式的 https:// 方案進行連結。
