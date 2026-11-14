---
title: "文件更新 - 2026年9月22日"
date: 2026-09-22
slug: /changelog-2026-09-22
source: https://manual.mikrotik.com/changelog/changelog-2026-09-22
captured_at: '2026-11-04T06:08:49+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026年9月22日的文件變更摘要。

## 容器 {#containers}

- **[Apps](/docs/containers/apps#yaml-field-reference)**：新增了用於編寫自定義應用的 YAML 欄位參考。其中涵蓋應用級和服務級欄位、健康檢查、執行時佔位符、卷、金鑰、配置和網路，每一項都附有示例。此外還修正了拼寫錯誤和示例格式。
- **[Apps](/docs/containers/apps#custom-app-store)**：新增了關於自定義應用商店的章節：在路由器可訪問的伺服器上託管一份應用定義的 YAML 列表，並給出了包含兩個應用的示例。

## 網橋與交換 {#bridging--switching}

- **[網橋與交換](/docs/bridging-and-switching#create-edge-ports-and-enable-bpdu-guard)**：將邊緣埠和 BPDU Guard 的示例合併為一個。新示例展示了埠收到 BPDU 時的日誌條目和非活動埠標誌，以及如何重新啟用該埠。刪除了使用交換器 ACL 規則丟棄 BPDU 的章節。
