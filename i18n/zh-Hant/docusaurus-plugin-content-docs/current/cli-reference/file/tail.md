---
sidebar_key: "cli-reference/file/tail"
sidebar_position: 6
title: "tail"
sidebar_label: 'tail'
source: https://manual.mikrotik.com/docs/cli-reference/file/tail
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## file/tail {#filetail}
**型別：** 命令

列印檔案內容的最後幾行。使用 `as-value` 時，這些行會以字串陣列的形式在 `lines` 中返回。請參閱 [檔案](../../system-information-and-utilities/files.md#head-or-tail-a-file) 指南。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="n" typ="num" unset="1">從檔案末尾輸出的行數。範圍：1..1000。預設值：10。</ArgTableRow>
<ArgTableRow arg="numbered" typ="switch">在每一行前面顯示行號。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="lines" typ="object { line: string
 }">以字串陣列形式返回的輸出行。</ArgTableRow>
</ArgTable>
