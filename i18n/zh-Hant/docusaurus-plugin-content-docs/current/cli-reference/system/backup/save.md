---
sidebar_key: "cli-reference/system/backup/save"
sidebar_position: 3
title: "save"
sidebar_label: 'save'
source: https://manual.mikrotik.com/docs/cli-reference/system/backup/save
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/backup/save {#systembackupsave}
**型別：** 命令

將整個路由器配置儲存為二進位制[備份檔案](../../../getting-started/configuration-management/backup.md)。備份檔案會出現在 `/file` 選單中，並且可以從路由器複製出來。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="file">備份檔案的名稱。檔案儲存為 `<name>.backup`，並出現在 `/file` 選單中。</ArgTableRow>
<ArgTableRow arg="password" typ="string">用於加密備份檔案的密碼。未提供密碼時，備份以未加密方式儲存。</ArgTableRow>
<ArgTableRow arg="dont-encrypt" typ="bool">即使已指定 `password`，也以未加密方式儲存備份。預設值：no。</ArgTableRow>
<ArgTableRow arg="encryption" typ="enum (aes-sha256 | rc4) { aes-sha256:0, rc4:1 }">
指定 `password` 時使用的加密演算法。
- `aes-sha256`（預設）- 使用 AES 和 SHA-256 加密。
- `rc4` - 舊式弱演算法，為相容較舊版本的 RouterOS 而保留。
</ArgTableRow>
</ArgTable>
