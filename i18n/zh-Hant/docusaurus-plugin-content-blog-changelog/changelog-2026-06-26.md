---
title: "文件更新 - 2026年6月26日"
date: 2026-06-26
slug: /changelog-2026-06-26
source: https://manual.mikrotik.com/changelog/changelog-2026-06-26
captured_at: '2026-11-04T06:08:02+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026 年 6 月 26 日文件變更摘要。

## 行動網路 {#mobile-networking}

- **[LTE/5G Interface](/docs/mobile-networking/lte-5g)**：新增 show-capabilities 命令文件，該命令用於顯示調變解調器的功能，例如支援的頻段、RAT 模式、APN 上限以及 passthrough 支援。
- **[LTE/5G Interface](/docs/mobile-networking/lte-5g)**：澄清了 network-mode 引數需要同時選中 lte 和 5g 才能使用 5G NSA；僅選擇 5g 只會連線到 5G SA。
- **[LTE/5G Interface](/docs/mobile-networking/lte-5g)**：重寫了監控部分，並更新了 /interface/lte/monitor 輸出示例，展示小區級資料和調變解調器元資料。
