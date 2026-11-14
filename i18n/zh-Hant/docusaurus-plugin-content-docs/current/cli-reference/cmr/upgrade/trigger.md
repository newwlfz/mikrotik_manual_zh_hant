---
sidebar_key: "cli-reference/cmr/upgrade/trigger"
sidebar_position: 3
title: "trigger"
sidebar_label: 'trigger'
source: https://manual.mikrotik.com/docs/cli-reference/cmr/upgrade/trigger
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## cmr/upgrade/trigger {#cmrupgradetrigger}
**軟體包：** cmr
**型別：** 命令

立即啟動所選規則的任務，而無需等待 schedule-time。同一時間只執行一個升級任務；如果在有任務正在進行時觸發另一條規則，則新任務會進入[排隊狀態](./job.md#cmr-upgrade-job)，直到當前任務完成。

觸發會強制提前升級該規則涵蓋的裝置：任務立即執行，並升級每個有較新版本可用的涵蓋裝置，而無需等待 schedule-time。已是最新版本的涵蓋裝置會被跳過，因此本次執行的計數器只統計已升級的裝置。要升級單個裝置而不考慮其規則，請參閱 [`/cmr/device/upgrade`](../device/upgrade.md)。
