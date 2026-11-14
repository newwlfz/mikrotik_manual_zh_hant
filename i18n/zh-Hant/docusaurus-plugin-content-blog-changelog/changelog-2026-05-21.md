---
title: "文件更新 - 2026年5月21日"
date: 2026-05-21
slug: /changelog-2026-05-21
source: https://manual.mikrotik.com/changelog/changelog-2026-05-21
captured_at: '2026-11-04T06:07:44+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026 年 5 月 21 日文件變更摘要。

## 橋接與交換 {#bridging--switching}

- **[橋接與交換](/docs/bridging-and-switching)**：恢復了整個 Bridge 主題中的插圖 —— 交換器晶片特性、VLAN、QoS、CRS1xx/2xx 示例、二層錯誤配置、生成樹以及無線 VLAN 幹道頁面上的示意圖現在均可正常顯示。
- **[交換器晶片特性](/docs/bridging-and-switching/switch-chip-features)**：修復了此前無法正常顯示的特性對比表腳註。關於 RouterOS v7 中的頻寬限制、2048 條目主機表上的共享 VLAN 學習（Shared VLAN Learning）以及 Switch 選單中受限的 VLAN 支援的註釋，現在會顯示在表格下方。若干內聯的 "Caution"/"Important" 段落已轉換為規範的提示塊。
- **[服務質量](/docs/bridging-and-switching/quality-of-service)**：修復了交換器晶片 QoS 表格中損壞的腳註標記，涉及 max-fill 統計、當前值報告以及 98CX8410 上不可用的統計資訊。
- **[Marvell Prestera 交換器晶片特性](/docs/bridging-and-switching/marvell-prestera-switch-chip-features)**：修正了若干格式錯誤的提示塊，使 L3 硬體解除安裝說明、10Gbps 埠上 egress-rate/storm-rate 的硬體限制以及交換器 ACL 修改警告能夠正確顯示。同時還改寫了 VLAN 間路由和 DHCP 伺服器的相關說明。

## 容器 {#containers}

- **[容器](/docs/containers)**：擴充了 stop-signal 的說明，解釋不同的 Linux 訊號可實現優雅關閉、立即終止或應用特定的操作，並整理了 memory-max 條目。
