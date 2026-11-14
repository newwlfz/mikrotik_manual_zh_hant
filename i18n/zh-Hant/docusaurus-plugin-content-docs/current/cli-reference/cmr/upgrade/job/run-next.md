---
sidebar_key: "cli-reference/cmr/upgrade/job/run-next"
sidebar_position: 1
title: "run-next"
sidebar_label: 'run-next'
source: https://manual.mikrotik.com/docs/cli-reference/cmr/upgrade/job/run-next
captured_at: '2026-11-09T11:35:47.715Z'
pagination_prev: "cli-reference/cmr/upgrade/job"
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## cmr/upgrade/job/run-next {#cmrupgradejobrun-next}
**軟體包：** cmr
**型別：** 命令

立即執行下一個已安排的升級任務。對於升級規則的任務，該任務會作為一次新的執行啟動，而原先安排的任務仍保持已安排狀態。透過 `/cmr/device/upgrade` 安排的任務沒有需要保留的計劃，因此該任務本身會啟動。同一時間只能執行一個升級任務，因此在另一個任務已在進行時啟動的任務會排隊等待，而不會將其中斷。
