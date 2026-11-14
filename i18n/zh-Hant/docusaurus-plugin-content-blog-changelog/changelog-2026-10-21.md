---
title: "文件更新 - 2026年10月21日"
date: 2026-10-21
slug: /changelog-2026-10-21
source: https://manual.mikrotik.com/changelog/changelog-2026-10-21
captured_at: '2026-11-04T06:09:04+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026 年 10 月 21 日所做的文件變更摘要。

## 管理工具 {#management-tools}

- **[CMR](/docs/management-tools/cmr)**：新增了當前 CMR 版本中的控制檯選項，每個選項都已對照 CMR 伺服器的控制檯進行核驗：用戶端與伺服器一樣接受 pairing-requirement=confirm，auto-labels 接受 ssid，port-labels 用一個埠的標籤之間用 / 分隔、各埠之間用 , 分隔，並且 /cmr/device/export 和 /cmr/device/add 會列印並建立裝置條目。[CMR-Client](/docs/management-tools/cmr/client) 頁面和 [/cmr/client](/docs/cli-reference/cmr/client) CLI 參考文件描述了用戶端側的 confirm。
