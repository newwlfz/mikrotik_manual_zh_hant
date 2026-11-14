---
sidebar_key: "cli-reference/ip/cloud/back-to-home-file/settings/remove-certificate"
sidebar_position: 1
title: "remove-certificate"
sidebar_label: 'remove-certificate'
source: https://manual.mikrotik.com/docs/cli-reference/ip/cloud/back-to-home-file/settings/remove-certificate
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/cloud/back-to-home-file/settings/remove-certificate {#ipcloudback-to-home-filesettingsremove-certificate}
**系統能力：** cloud-vpn
**型別：** 命令

從 `/certificate` 中刪除檔案共享證書。僅當不存在共享時該命令才有效；否則會失敗並顯示 `cannot remove certificate while file shares active`。下一次建立共享時會請求新證書。參見[停止檔案共享](../../../../../network-management/cloud/file-share.md#stop-file-share)。
