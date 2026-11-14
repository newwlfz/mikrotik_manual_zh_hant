---
sidebar_key: "cli-reference/system/backup/cloud/remove-file"
sidebar_position: 2
title: "remove-file"
sidebar_label: 'remove-file'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/system/backup/cloud/remove-file
captured_at: '2026-11-01T21:25:25+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/backup/cloud/remove-file {#systembackupcloudremove-file}
**型別：** 命令

從雲伺服器上刪除備份，並釋放本裝置的槽位。透過備份在列表中的編號來指定備份，例如 `remove-file number=0`。

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="status" typ="string">命令的進度：執行期間為 `working...`，完成時為 `finished`，或為錯誤資訊，例如來自雲伺服器的錯誤資訊。</ArgTableRow>
</ArgTable>
