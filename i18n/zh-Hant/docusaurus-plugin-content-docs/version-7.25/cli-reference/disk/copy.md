---
sidebar_key: "cli-reference/disk/copy"
sidebar_position: 4
title: "copy"
sidebar_label: 'copy'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/disk/copy
captured_at: '2026-11-01T21:22:09+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## disk/copy {#diskcopy}
**條件：** !smips
**型別：** 命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="src" typ="enum">源磁碟、分割區或檔案。</ArgTableRow>
<ArgTableRow arg="dst" typ="enum">目標磁碟、分割區或檔案。其大小必須至少與被複制的資料一樣大。</ArgTableRow>
<ArgTableRow arg="src-offset" typ="num">源中開始複製的位元組偏移量。預設值：0。</ArgTableRow>
<ArgTableRow arg="dst-offset" typ="num">目標中寫入資料的位元組偏移量。預設值：0。</ArgTableRow>
<ArgTableRow arg="size" typ="num">要複製的位元組數。未指定時，將複製整個源。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="status" typ="string">複製進度：`<bytes copied> / <total bytes> (<percent>%)`。</ArgTableRow>
</ArgTable>
