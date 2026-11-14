---
sidebar_key: "cli-reference/system/backup/cloud"
title: "cloud"
sidebar_label: 'cloud'
source: https://manual.mikrotik.com/docs/cli-reference/system/backup/cloud
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/backup/cloud {#systembackupcloud}
**型別：** 目錄

儲存於 MikroTik 雲伺服器上的本裝置備份。每臺裝置只有一個槽位。此選單中的每條命令（包括 `print`）都會連線到 `cloud2.mikrotik.com`。有關示例，請參見 [雲備份](../../../../network-management/cloud/cloud-backup.md)。

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">備份的名稱，在 `upload-file` 中透過 `name` 設定。除非指定了 `dst-file`，否則 `download-file` 會將備份儲存為 `<name>.backup`。</ArgTableRow>
<ArgTableRow arg="size" typ="num">加密備份檔案的大小。</ArgTableRow>
<ArgTableRow arg="ros-version" typ="string">建立該備份的 RouterOS 版本。</ArgTableRow>
<ArgTableRow arg="date" typ="date">上傳時間。</ArgTableRow>
<ArgTableRow arg="status" typ="string">所儲存備份的狀態。當備份可以被下載時為 `ok`。</ArgTableRow>
<ArgTableRow arg="secret-download-key" typ="string">可在任意路由器上透過 `download-file secret-download-key=<key>` 下載此備份的金鑰。替換備份會生成新的金鑰。任何持有該金鑰的人都可以下載該檔案，但沒有備份密碼則無法讀取它。</ArgTableRow>
</ArgTable>
