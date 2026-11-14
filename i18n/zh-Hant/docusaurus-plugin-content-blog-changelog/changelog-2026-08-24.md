---
title: "文件更新 - 2026年8月24日"
date: 2026-08-24
slug: /changelog-2026-08-24
source: https://manual.mikrotik.com/changelog/changelog-2026-08-24
captured_at: '2026-11-04T06:08:36+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026 年 8 月 24 日文件變更摘要。

## 入門 {#getting-started}

- **[Upgrade](/docs/getting-started/installation-and-upgrade/upgrade)**：將獨立的 Upgrade Server 頁面併入本頁面的 Standard Upgrade 部分，並將 system/package/update CLI 引數移入 CLI 參考。

## 硬體 {#hardware}

- **[RouterBOARD](/docs/hardware/routerboard)**：將 RouterBOARD 按鈕和設定引數移入 CLI 參考，並改寫了相關文字（同時相應更新了 [FlashFig](/docs/management-tools/flashfig)）。

## CLI 參考 {#cli-reference}

- **[CLI 參考](/docs/cli-reference)**：刪除了若干錯誤生成的存根頁面（例如 Bridge MSRP 子選單，它們在此處並不適用），並停止顯示空選單目錄，修復了由此產生的失效 switch 規則交叉引用。

## 使用者指南 {#user-guides}

- **[Route Distinguisher 與 Route Target](/docs/user-guides/routing-and-networking-protocols/route-distinguisher-and-route-target)**：更正了 Route Distinguisher 大小的描述（64-bit → 8-byte），並修復了一個格式錯誤的表格。
