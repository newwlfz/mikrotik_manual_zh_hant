---
sidebar_key: "cli-reference/ip/cloud/force-update"
sidebar_position: 4
title: "force-update"
sidebar_label: 'force-update'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/cloud/force-update
captured_at: '2026-11-01T21:23:48+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/cloud/force-update {#ipcloudforce-update}
**型別：**命令

立即向雲伺服器傳送 DDNS 更新，例如在網際網路連線發生變化之後。當 DDNS 關閉時（`ddns-enabled=auto` 且未啟用 Back To Home（遠端回家）），它不會執行任何操作，也不會設定時鐘。
