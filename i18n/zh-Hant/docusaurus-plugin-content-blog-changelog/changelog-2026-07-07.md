---
title: "文件更新 - 2026年7月7日"
date: 2026-07-07
slug: /changelog-2026-07-07
source: https://manual.mikrotik.com/changelog/changelog-2026-07-07
captured_at: '2026-11-04T06:08:08+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026 年 7 月 7 日文件變更摘要。

## 入門 {#getting-started}

- **[預設配置密碼](/docs/getting-started/configuration-management/default-configuration-passwords)**：新增頁面，說明在哪裡可以找到裝置唯一的出廠預設密碼（序列號貼紙、包裝、快速指南、部分室內無線裝置上的產品資訊倉），以及找不到密碼時該怎麼辦。
- **[RouterOS 配置重設](/docs/getting-started/configuration-management/routeros-configuration-reset)**：使用搶救出的知識庫資料進行了擴充。
- **[升級伺服器](/docs/getting-started/installation-and-upgrade/upgrade#standard-upgrade)** 和 **[AWS 上的 CHR](/docs/getting-started/installation-and-upgrade/install/chr-installation/aws)**：新增頁面。

## 診斷與監控 {#diagnostics--monitoring}

- **[降級 RouterOS](/docs/diagnostics-monitoring-and-troubleshooting/downgrading-routeros)**：新增頁面，涵蓋出廠軟體版本下限、降級前檢查清單（二進位制備份加匯出），以及使用 /system/package/downgrade 的分步降級流程。

## 硬體 {#hardware}

- **[RMA 之前先嚐試](/docs/hardware/try-before-rma)**：從知識庫搶救資料中新增的頁面。

## 無線 {#wireless}

- **[WiFi](/docs/wireless/wifi)**：新增 "Network" 章節，記錄了 /interface/wifi/network 選單，該選單將 SSID、安全、資料路徑和無線引數捆綁為單一配置實體，並應用於匹配其標籤的介面，配置示例中包含多鏈路操作（MLO）。

## 全站 {#site-wide}

- **屬性表**：修復了在 11 個頁面中被 Confluence→Docusaurus 遷移壓平成單個表格單元格的圍欄程式碼塊（原本顯示為原始的 ```ros&lt;br/&gt; 文字），涉及 Disks、Scripting、Log、LTE/5G、NTP、L2TP、PPPoE 和 WiFi interworking。現在它們會正常渲染為行內程式碼。
