---
sidebar_key: "cli-reference/ip/media/settings"
sidebar_position: 1
title: "settings"
sidebar_label: 'settings'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/media/settings
captured_at: '2026-11-01T21:24:16+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/media/settings {#ipmediasettings}
**條件：** !smips
**型別：** 設定目錄

由 `/ip/media` 中所有 DLNA 媒體伺服器共享的設定。參見 [DLNA 媒體伺服器](./index.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="thumbnails" typ="string">逗號分隔的檔名列表（應以 .jpg 結尾）。如果目錄中某個檔案的名稱與該列表中的任何檔名匹配，則該檔案會被視為該目錄中任何媒體檔案的縮圖：它不再作為圖片列出，播放器會將其顯示為其他檔案的封面圖片。參見 [DLNA 媒體伺服器](../../../storage/dlna.md)。預設值：空。</ArgTableRow>
</ArgTable>
