---
sidebar_key: "cli-reference/interface/ethernet/switch/qos"
title: "qos"
sidebar_label: 'qos'
source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/qos
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/qos {#interfaceethernetswitchqos}
**系統能力：** rbswitch 和 crs_prestera
**型別：** 目錄

整個 QoS 硬體配置位於 `/in/eth/sw/qos` 下。這種集中式方法允許您將所有 QoS 相關配置項儲存在一個位置，便於使用 `/in/eth/sw/qos/export` 監控和匯出設定。

QoS 條目有兩個主要標誌指示符：

- **H** - 硬體解除安裝條目。
- **I** - 非活動條目。
