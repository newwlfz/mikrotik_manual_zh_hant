---
sidebar_key: "cli-reference/system/backup/load"
sidebar_position: 2
title: "load"
sidebar_label: 'load'
source: https://manual.mikrotik.com/docs/cli-reference/system/backup/load
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/backup/load {#systembackupload}
**型別：** 命令

從[備份檔案](../../../getting-started/configuration-management/backup.md)載入使用 `/system/backup/save` 儲存的配置，然後在確認後重啟路由器。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="file">備份檔案的名稱，與傳給 `save` 的名稱相同（不帶 `.backup` 副檔名）。</ArgTableRow>
<ArgTableRow arg="password" typ="string">用於解密備份檔案的密碼。省略時，RouterOS 會提示輸入。對於未加密的備份，任意密碼均可。</ArgTableRow>
<ArgTableRow arg="force-v6-to-v7-configuration-upgrade" typ="bool">是否載入在 RouterOS v6 上建立的備份並將其配置轉換為 v7。該標誌對在 v7 上建立的備份無效。</ArgTableRow>
</ArgTable>
