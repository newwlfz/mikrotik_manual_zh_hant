---
title: "文件更新 - 2026 年 10 月 14 日"
date: 2026-10-14
slug: /changelog-2026-10-14
source: https://manual.mikrotik.com/changelog/changelog-2026-10-14
captured_at: '2026-11-04T06:09:01+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026 年 10 月 14 日所做的文件變更摘要。

## 系統 {#system}

- **[Device mode](/docs/system-information-and-utilities/device-mode)**：在 RouterOS 7.26beta1 上重寫並測試。所有示例與輸出均已更新，並驗證了其工作機制：透過 reset 或 mode 按鈕或重新上電進行確認（普通重啟不會完成確認）、模式替換與按功能單獨更新、print config 僅顯示非預設設定、更新嘗試計數器及其重設視窗（activation-timeout），以及已停用功能的配置會以未啟用狀態建立。

## CLI 參考 {#cli-reference}

- **[/system/device-mode](/docs/cli-reference/system/device-mode)**、**[/system/device-mode/update](/docs/cli-reference/system/device-mode/update)**：選單簡介和所有引數說明均已補全，包括每個功能開關所控制的工具和選單（bandwidth-test 下的 speed-test、traffic-gen 下的 ping-speed）以及嘗試計數器的重設視窗。
