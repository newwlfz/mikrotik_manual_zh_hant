---
sidebar_key: "cli-reference/system/backup/load"
sidebar_position: 2
title: "load"
sidebar_label: 'load'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/system/backup/load
captured_at: '2026-11-01T21:25:24+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/backup/load {#systembackupload}
**型別：** 命令

該命令從[備份檔案](../../../getting-started/configuration-management/backup.md)載入配置。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="file">備份檔案的檔名。</ArgTableRow>
<ArgTableRow arg="password" typ="string">加密備份檔案的密碼。</ArgTableRow>
<ArgTableRow arg="force-v6-to-v7-configuration-upgrade" typ="bool">此設定會在載入配置後（如果備份包含 ROSv6 配置）強制執行配置轉換為 v7。</ArgTableRow>
</ArgTable>
