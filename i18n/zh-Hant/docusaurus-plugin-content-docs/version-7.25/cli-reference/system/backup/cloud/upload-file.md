---
sidebar_key: "cli-reference/system/backup/cloud/upload-file"
sidebar_position: 3
title: "upload-file"
sidebar_label: 'upload-file'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/system/backup/cloud/upload-file
captured_at: '2026-11-01T21:25:24+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/backup/cloud/upload-file {#systembackupcloudupload-file}
**型別：** 命令

將 AES 加密的備份上傳到本裝置在雲伺服器上的槽位。當該槽位已被使用時，除非 `replace` 指定了已儲存的備份，否則上傳會失敗並顯示 `Server error: All slots used. Delete file to free up space.`。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="action" typ="enum (upload | create-and-upload)">
要上傳的內容：
- `create-and-upload` - 建立當前配置的備份，使用 `password` 加密並上傳。
- `upload` - 上傳 `src-file` 中指定的備份檔案。
</ArgTableRow>
<ArgTableRow arg="name" typ="string">雲列表中的備份名稱。它不必與檔名一致。</ArgTableRow>
<ArgTableRow arg="replace" typ="enum">要覆蓋的已儲存備份的名稱。新備份會獲得新的 `secret-download-key`。</ArgTableRow>
<ArgTableRow arg="src-file" typ="file">要使用 `action=upload` 上傳的備份檔案。該檔案必須使用密碼儲存（`/system/backup/save password=...`），否則命令會失敗並顯示 `src file must be AES encrypted`。</ArgTableRow>
<ArgTableRow arg="password" typ="string">`action=create-and-upload` 時用於加密備份的密碼。該操作需要此密碼；恢復備份時也需要它。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="status" typ="string">命令的進度：執行期間為 `working...`，完成時為 `finished`，或為錯誤資訊，例如來自雲伺服器的錯誤資訊。</ArgTableRow>
</ArgTable>
