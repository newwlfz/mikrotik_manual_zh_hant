---
sidebar_key: "cli-reference/file/read"
sidebar_position: 3
title: "read"
sidebar_label: 'read'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/file/read
captured_at: '2026-11-01T21:22:17+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## file/read {#fileread}
**型別：** 命令

讀取檔案內容的一個塊，並將其作為字串返回到 `data` 中。適用於任意大小的檔案，不同於 `contents` 屬性，後者限制為略低於 60 KiB。請參閱 [檔案](../../system-information-and-utilities/files.md#read-file-contents) 指南。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="file" typ="file">要讀取的檔名稱。</ArgTableRow>
<ArgTableRow arg="chunk-size" typ="num">要從檔案讀取的塊大小。必填。範圍：1..32768。</ArgTableRow>
<ArgTableRow arg="offset" typ="num">開始讀取檔案的偏移量。若讀取的塊超出檔案末尾，則該塊會被截短；若偏移量超出末尾，則會失敗。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="data" typ="string">以字串形式返回的讀取資料。</ArgTableRow>
</ArgTable>
