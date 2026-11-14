---
sidebar_key: "cli-reference/ip/cloud/back-to-home-file"
title: "back-to-home-file"
sidebar_label: 'back-to-home-file'
source: https://manual.mikrotik.com/docs/cli-reference/ip/cloud/back-to-home-file
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/cloud/back-to-home-file {#ipcloudback-to-home-file}
**系統能力：** cloud-vpn
**型別：** 目錄

與 File Share 共享的目錄和檔案。每個共享都會在 `<serial>.routingthecloud.net` 下獲得一個私密連結，並且只要至少存在一個共享，該服務就會執行。有關示例，請參見 [檔案共享](../../../../network-management/cloud/file-share.md)。服務狀態位於 [`settings`](./settings/index.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">此共享已停用，其連結返回 HTTP 404。</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">此共享尚無法提供訪問，例如路由器正在請求證書時。註釋行會顯示原因，例如 `getting cert status: requesting SSL certificate`。</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="path" typ="file">要共享的目錄或檔案，以 `/file/print` 顯示的形式，例如 `usb1/photos`。路由器顯示它時會帶前導 `/`。</ArgTableRow>
<ArgTableRow arg="allow-uploads" typ="bool">目錄共享的訪問者是否可以在其中上傳檔案並建立資料夾。未啟用時，路由器會以 HTTP 403 拒絕上傳。預設值：no。</ArgTableRow>
<ArgTableRow arg="expires" typ="alt { expires: enum (never) { never:0xFFFFFFFF }
, interval: time
, date-time: date
 }">共享何時停止工作：`never`、日期和時間（例如 `"2026-10-01 00:00:00"`）或時間間隔（例如 `1h`）。路由器會將時間間隔轉換為日期。`never` 會保留共享，直到你將其刪除。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="key" typ="string">共享的隨機金鑰，即 `url` 的最後一部分。</ArgTableRow>
<ArgTableRow arg="url" typ="string">指向共享頁面的連結：`https://<serial>.routingthecloud.net/s/<key>`。目錄共享會列出其檔案；任何擁有該連結的人都可以開啟它。</ArgTableRow>
<ArgTableRow arg="direct-url" typ="string">`url` 加上 `?dl`。它會下載共享檔案，或將整個目錄下載為 `download.zip`。</ArgTableRow>
<ArgTableRow arg="downloads" typ="num">共享的直接下載次數。開啟共享頁面不計入。</ArgTableRow>
</ArgTable>
