---
sidebar_key: "cli-reference/file/sync/index"
sidebar_position: 1
title: "sync"
sidebar_label: "sync"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/file/sync
captured_at: '2026-11-01T21:26:53+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## file/sync {#filesync}
**軟體包：** rose-storage
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="remote-address" typ="multi { array-id, address: string
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="mode" typ="enum (upload | download)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="local-path" typ="file"></ArgTableRow>
<ArgTableRow arg="remote-path" typ="string"></ArgTableRow>
<ArgTableRow arg="user" typ="string"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
</ArgTable>
