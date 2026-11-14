---
sidebar_key: "cli-reference/file/index"
sidebar_position: 3
title: "file"
sidebar_label: "file"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/file
captured_at: '2026-11-01T21:26:52+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## file {#file}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="S" typ="shared"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="file" mandatory="1"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (file | directory)"></ArgTableRow>
<ArgTableRow arg="contents" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="size" typ="num"></ArgTableRow>
<ArgTableRow arg="last-modified" typ="date">最後修改日期和時間</ArgTableRow>
<ArgTableRow arg="package-name" typ="string"></ArgTableRow>
<ArgTableRow arg="package-version" typ="string"></ArgTableRow>
<ArgTableRow arg="package-build-time" typ="date"></ArgTableRow>
<ArgTableRow arg="package-architecture" typ="string"></ArgTableRow>
<ArgTableRow arg="url" typ="string" syscap="cloud-vpn"></ArgTableRow>
</ArgTable>
