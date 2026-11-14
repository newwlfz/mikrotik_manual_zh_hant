---
sidebar_key: "cli-reference/task/add"
sidebar_position: 1
title: "add"
sidebar_label: "add"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/task/add
captured_at: '2026-11-01T21:30:12+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## task/add {#taskadd}
**型別：** 命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="source" typ="string">應在後臺執行的命令</ArgTableRow>
<ArgTableRow arg="switch-to" typ="switch">立即切換到後臺檢視</ArgTableRow>
<ArgTableRow arg="append" typ="switch">將輸出追加到檔案</ArgTableRow>
<ArgTableRow arg="file-name" typ="file">輸出的預設檔名</ArgTableRow>
<ArgTableRow arg="save-interval" typ="time">設定檔名後的自動儲存間隔</ArgTableRow>
<ArgTableRow arg="max-lines" typ="num">最大緩衝區行數</ArgTableRow>
<ArgTableRow arg="save-timestamp" typ="switch">為儲存的檔案新增時間戳</ArgTableRow>
<ArgTableRow arg="no-header-paging" typ="switch">不將標題分頁到輸出</ArgTableRow>
<ArgTableRow arg="max-size" typ="num">最大儲存檔案大小</ArgTableRow>
</ArgTable>
