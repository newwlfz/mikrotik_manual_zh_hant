---
title: "文件更新 - 2026年6月9日"
date: 2026-06-09
slug: /changelog-2026-06-09
source: https://manual.mikrotik.com/changelog/changelog-2026-06-09
captured_at: '2026-11-04T06:07:53+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026 年 6 月 9 日文件變更摘要。

## 硬體 {#hardware}

- **[硬體指南](/docs/hardware)**：新增了從 Confluence 匯入的硬體指南章節，涵蓋 60 GHz 產品、配件、室內無線、IoT 產品、LTE 產品、RouterBoard、交換器以及無線系統，所有頁面均採用統一的頁面結構並帶有認證徽章。

## 物聯網 {#internet-of-things}

- **[Bluetooth](/docs/internet-of-things/bluetooth)**：將 KNOT 和 Bluetooth 指南（通知指南、信標管理器應用、GPIO 脈衝輸入）從硬體章節移至 IoT，並刪除了由此產生的重複頁面。

## 行動網路 {#mobile-networking}

- **[BG77 Modem AT Commands](/docs/mobile-networking/bg77-modem-at-commands)**：將 BG77 調變解調器 AT 命令指南從硬體移至行動網路章節。

## CLI 參考 {#cli-reference}

- **[Netwatch](/docs/cli-reference/tool/netwatch)**：為所有 netwatch 探測引數添加了說明。
- 將原本單一的 MPLS 和佇列 CLI 參考頁面拆分為按子選單劃分的獨立頁面，並將連線跟蹤引數移至[專屬頁面](/docs/cli-reference/ip/firewall/connection/tracking)。

## 容器 {#containers}

- **[容器](/docs/containers)**：新增了一條警告：容器需要配置 DNS，否則容器將無法啟動。

## 診斷與監控 {#diagnostics--monitoring}

- **[Packet Sniffer](/docs/diagnostics-monitoring-and-troubleshooting/packet-sniffer)**：更正了流量生成器 PCAPNG 的資訊 —— 該格式從 RouterOS 7.21 開始支援。

## 入門 {#getting-started}

- **[軟體包](/docs/getting-started/installation-and-upgrade/packages)**：更新了軟體包列表 —— 新增 wifi-mediatek 和 wifi-qcom-be 驅動軟體包，並整理了架構列表和格式。同時更新了架構參考名稱，並修正了相關頁面上的拼寫錯誤。
