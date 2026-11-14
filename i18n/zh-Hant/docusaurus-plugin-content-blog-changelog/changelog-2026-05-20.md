---
title: "文件更新 - 2026 年 5 月 20 日"
date: 2026-05-20
slug: /changelog-2026-05-20
source: https://manual.mikrotik.com/changelog/changelog-2026-05-20
captured_at: '2026-11-04T06:07:44+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026年5月20日文件變更摘要。

## 入門 {#getting-started}

- **[RouterOS 授權](/docs/getting-started/routeros-licensing)**：重組了授權文件。x86 授權內容已合併到單個 [x86 授權](/docs/getting-started/routeros-licensing/x86) 頁面中，而不是單獨的子頁面，並且隨附的截圖已重新整理。

## 容器 {#containers}

- **[容器](/docs/containers)**：記錄了使用 devices=serial0:"" 將序列終端透傳到容器，包括一條說明：必須先釋放 /system/console 下的 RouterOS 序列控制檯。

## 無線 {#wireless}

- **[Nv2](/docs/wireless/abgn/nv2)**：透過移除冗餘的子標題，將協定概述重組為連續的行文，並整理了同步和配置示例部分。
- **[頻譜掃描](/docs/wireless/abgn/spectral-scan)**：更正了範圍選項列表的格式，並將不受支援的晶片組提示框從 danger 降級為 warning 提示框。
