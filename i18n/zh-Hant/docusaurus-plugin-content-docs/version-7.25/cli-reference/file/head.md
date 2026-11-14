---
sidebar_key: "cli-reference/file/head"
sidebar_position: 2
title: "head"
sidebar_label: 'head'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/file/head
captured_at: '2026-11-01T21:22:18+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## file/head {#filehead}
**型別：** 命令

列印檔案內容的前幾行。使用 `as-value` 時，這些行會以字串陣列的形式返回到 `lines` 中。請參閱 [檔案](../../system-information-and-utilities/files.md#head-or-tail-a-file) 指南。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="n" typ="num" unset="1">要從檔案開頭輸出的行數。範圍：1..1000。預設值：10。</ArgTableRow>
<ArgTableRow arg="numbered" typ="switch">在每行前面顯示行號。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="lines" typ="object { line: string
 }">以字串陣列形式返回的輸出行。</ArgTableRow>
</ArgTable>
