---
sidebar_key: "cli-reference/system/backup/save"
sidebar_position: 3
title: "save"
sidebar_label: 'save'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/system/backup/save
captured_at: '2026-11-01T21:25:24+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/backup/save {#systembackupsave}
**型別：** 命令

命令會將配置儲存為二進位制[備份檔案](../../../getting-started/configuration-management/backup.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="file">備份檔案的檔名。</ArgTableRow>
<ArgTableRow arg="password" typ="string">加密備份檔案的密碼。自 RouterOS v6.43 起，如果未提供密碼，則備份檔案不加密。</ArgTableRow>
<ArgTableRow arg="dont-encrypt" typ="bool">停用備份檔案加密。自 RouterOS v6.43 起，如果未提供密碼，則備份檔案不加密。</ArgTableRow>
<ArgTableRow arg="encryption" typ="enum (aes-sha256 | rc4) { aes-sha256:0, rc4:1 }">用於加密備份檔案的加密演算法。`rc4` 不是安全的加密方法，僅出於與舊版 RouterOS 相容的目的提供。</ArgTableRow>
</ArgTable>
