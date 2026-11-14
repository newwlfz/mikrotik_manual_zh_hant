---
sidebar_key: "cli-reference/system/backup/cloud/download-file"
sidebar_position: 1
title: "download-file"
sidebar_label: 'download-file'
source: https://manual.mikrotik.com/docs/cli-reference/system/backup/cloud/download-file
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/backup/cloud/download-file {#systembackupclouddownload-file}
**型別：** 命令

從雲伺服器下載備份：本裝置在列表中的備份（透過其編號 `number=0`），或透過 `secret-download-key` 下載任意備份。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="secret-download-key" typ="string">要下載的備份金鑰，在上傳該備份的路由器上顯示為 `secret-download-key`。可用它把該備份下載到另一臺路由器。</ArgTableRow>
<ArgTableRow arg="action" typ="enum (download | download-and-apply)">
對備份執行的操作：
- `download` - 將備份檔案儲存到路由器的儲存中。
- `download-and-apply` - 儲存備份檔案，使用 `password` 從該檔案恢復配置，然後重啟。
</ArgTableRow>
<ArgTableRow arg="dst-file" typ="string">儲存的檔名；會自動新增 `.backup`。不指定時，檔案儲存為 `<name>.backup`。</ArgTableRow>
<ArgTableRow arg="password" typ="string">備份的密碼，用於 `action=download-and-apply`。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="status" typ="string">命令的進度：執行期間為 `working...`，完成時為 `finished`，或為錯誤資訊，例如來自雲伺服器的錯誤資訊。</ArgTableRow>
</ArgTable>
