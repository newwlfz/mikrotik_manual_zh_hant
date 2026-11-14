---
sidebar_key: "cli-reference/ip/cloud/back-to-home-file/index"
sidebar_position: 1
title: "back-to-home-file"
sidebar_label: "back-to-home-file"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/cloud/back-to-home-file
captured_at: '2026-11-01T21:28:25+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/cloud/back-to-home-file {#ipcloudback-to-home-file}
**系統能力：** cloud-vpn
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">無效</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="path" typ="file"></ArgTableRow>
<ArgTableRow arg="allow-uploads" typ="bool"></ArgTableRow>
<ArgTableRow arg="expires" typ="alt { expires: enum (never) { never:0xFFFFFFFF }
, interval: time
, date-time: date
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="key" typ="string"></ArgTableRow>
<ArgTableRow arg="url" typ="string"></ArgTableRow>
<ArgTableRow arg="direct-url" typ="string"></ArgTableRow>
<ArgTableRow arg="downloads" typ="num"></ArgTableRow>
</ArgTable>
