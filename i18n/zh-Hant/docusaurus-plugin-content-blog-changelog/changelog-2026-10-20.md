---
title: "文件更新 - 2026年10月20日"
date: 2026-10-20
slug: /changelog-2026-10-20
source: https://manual.mikrotik.com/changelog/changelog-2026-10-20
captured_at: '2026-11-04T06:09:05+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026 年 10 月 20 日所做的文件變更摘要。

## 管理工具 {#management-tools}

- **[CMR](/docs/management-tools/cmr)**：已對照 CMR 伺服器檢查了裝置選擇、儀表板和 WiFi 日誌示例。[/cmr/device/dashboard](/docs/cli-reference/cmr/device/dashboard) 和 [/cmr/device/wifi-logs](/docs/cli-reference/cmr/device/wifi-logs) 命令接受 labels，並且 labels 會將 WiFi 日誌條目限制為所選裝置。裝置列表過濾器示例對 labels 使用 ~，因為 labels= 只匹配整個標籤列表。layout 連結輸出示例已重新排版。CLI 應用流量檢視會顯示流量計數器，並且 place-before 說明已恢復，因為測試表明該引數仍會將規則新增到末尾。在透過 CMR 升級的裝置群上重新檢查：處於最新狀態或離線的受覆蓋裝置會在任何升級發生之前停止 fail-policy=stop 作業；升級和重啟日誌訊息來自新的 Example rules 部分；rebooted 也會在 upgrade 和 reboot 命令重啟時觸發；WiFi 日誌監視器具有 clients 檢視；指令碼中使用 labels 的 as-value 已被記錄。
