---
title: "文件更新 - 2026年6月10日"
date: 2026-06-10
slug: /changelog-2026-06-10
source: https://manual.mikrotik.com/changelog/changelog-2026-06-10
captured_at: '2026-11-04T06:07:57+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026 年 6 月 10 日文件變更彙總。

## 硬體 {#hardware}

- **[硬體指南](/docs/hardware)**：在 73 個硬體頁面上補錄了 MikroTik 官方產品簡短描述，內容取自公開的 products API 並按產品程式碼匹配。已在描述中新增指向對應 mikrotik.com 產品頁面的連結。
- **[硬體指南](/docs/hardware)**：為多型號產品頁面添加了 covers-box 與 photo-row 佈局，併為每個型號提供產品程式碼連結。統一了 18 個多產品頁面上 "This article covers" 開頭提示框的寫法。
- **[硬體指南](/docs/hardware)**：為步驟照片序列添加了並排的可點選縮圖畫廊 —— 章節內連續的圖片現在會以帶燈箱縮放的小縮圖呈現。
- **[硬體指南](/docs/hardware)**：大規模佈局清理：修復主圖，規範章節標題層級，將誤作標題的零散引導句降級，移除 Confluence 遺留標記（裸露星號、宏垃圾、損壞的目錄），併為未加圍欄的程式碼塊重新加上圍欄。刪除了已移至 IoT 章節的過時 KNOT 子頁面。
- 重新從 Confluence 匯入了 TG-LR 硬體頁面，並修復了匯出工具的問題。
- **[硬體指南](/docs/hardware)**：又用來自 products API 的 MikroTik 官方產品照片（WebP）替換了約 80 個頁面的首圖，包括在所有指南頁面中統一 LtAP 與 LtAP mini 的圖片。
- **[硬體指南](/docs/hardware)**：為另外 70 個頁面補上了缺失的 mikrotik.com 產品頁面連結，並將 wAP ax LTE7 kit 頁面移入 LTE Products 分類。
- **[硬體指南](/docs/hardware)**：第二輪 Confluence 清理：從 120 個頁面移除了外鏈圖示殘留，修復了 83 個頁面上破壞專案符號列表的孤立標題文字，移除了不換行空格和 WinBox URL 殘留，修復了拼接錯誤的 URL、損壞的產品程式碼以及合規性表格中語言相關幫助 URL 末尾多餘的 +，並修復了 hAP ax lite LTE6 與 hAP lite TC 頁面的結構。
- **[硬體指南](/docs/hardware)**：將全部 46 個失效的 wiki.mikrotik.com 連結替換為手冊內部頁面（SFP/有線介面相容性、LED、GPS、W60G、LTE/5G、LoRa、Serial Console、S+RJ10 指南）或 help.mikrotik.com 上現行的 SwOS 手冊。一次全站連結檢查還修復了其他章節中已遷移或失效的外部連結（ZeroTier、kernel NAPI、RFC 8092、Vultr、ThingsBoard、wi-fi.org），並取消了那些從未是網頁的佔位主機名的連結。

## 物聯網 {#internet-of-things}

- **[Modbus](/docs/internet-of-things/modbus)**：移除了頁面 slug（此前錯誤地指向某條硬體專用路徑）。添加了 KNOT 相容性警告，列出帶 RS-485 埠的受支援型號。修復了屬性表格格式，並重新整理了降級/取消章節。
- **[Bluetooth](/docs/internet-of-things/bluetooth)**：修復了 BLE 標籤郵件通知指南中的失效連結和圖片引用，添加了指向 MikroTik 標籤廣播格式頁面以及 iOS/Android beacon manager 指南的連結，並將舊式 &lt;note&gt; HTML 替換為規範的 Docusaurus :::info 提示框。
- **[Bluetooth](/docs/internet-of-things/bluetooth)**：補全並修復了 beacon manager 指南（索引、Android、iOS）。移除了 IoT Bluetooth 頁面中自定義的 /slug frontmatter 覆蓋項，使 URL 結構與檔案系統佈局保持一致。
- **[GPIO](/docs/internet-of-things/gpio)**：修復了 pulse-input 指南中一處損壞的圖片引用。
- **[Lora](/docs/internet-of-things/lora)**：將 "Setup" 章節重新命名為 "User Guides"，並把 TG-LR 裝置文件作為 [TG-LR 設定指南](/docs/internet-of-things/lora/user-guides/tg-lr-setup-guide) 移入其中，同時恢復了警告提示框和文件風格元資料。
- **[Bluetooth](/docs/internet-of-things/bluetooth)**：補全並修復了 BLE 標籤通知與遙測指南（MQTT 與 Azure、HTTPS POST 與 Azure、MQTT/HTTPS 與 AWS、IFTTT 應用通知、ThingsBoard 溫度讀數）：用可用的 Microsoft Learn 和廠商連結恢復了失效的 "follow this link" 引用，更新了截圖，並補充了缺失的配置步驟。

## CLI 參考 {#cli-reference}

- **[IP 設定](/docs/cli-reference/ip/settings)**：為 ipv4-high-fragment-thresh 引數（分片重組佇列的記憶體上限，並提供按 RAM 容量區分的預設值）和 ipv4-fragment-time 引數（分片生存時間，單位為秒）添加了說明。

## 入門 {#getting-started}

- **[軟體包](/docs/getting-started/installation-and-upgrade/packages)**：將 wifi-qcom-be 的架構支援列表由 arm、arm64 更正為僅 arm64，與實際 WiFi-7 802.11be 驅動的要求一致。
