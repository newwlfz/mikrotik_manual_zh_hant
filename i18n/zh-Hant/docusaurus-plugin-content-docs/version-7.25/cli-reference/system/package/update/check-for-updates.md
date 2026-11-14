---
sidebar_key: "cli-reference/system/package/update/check-for-updates"
sidebar_position: 2
title: "check-for-updates"
sidebar_label: 'check-for-updates'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/system/package/update/check-for-updates
captured_at: '2026-11-01T21:25:38+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/package/update/check-for-updates {#systempackageupdatecheck-for-updates}
**型別：** 命令

在所選釋出通道中檢查 MikroTik 下載伺服器上是否有更新的 RouterOS 版本。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="fetch-changelog" typ="switch">是否在檢查更新的同時獲取變更日誌。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="changelog" typ="string">最新可用版本的變更日誌文字。</ArgTableRow>
</ArgTable>
