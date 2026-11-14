---
sidebar_key: "cli-reference/ip/smb/shares"
sidebar_position: 1
title: "shares"
sidebar_label: "shares"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/smb/shares
captured_at: '2026-11-01T21:28:56+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/smb/shares {#ipsmbshares}
**條件：** !smips
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="*" typ="default">default</ArgTableRow>
<ArgTableRow arg="r" typ="read-only">read-only</ArgTableRow>
<ArgTableRow arg="c" typ="require-encryption">require-encryption</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="directory" typ="file"></ArgTableRow>
<ArgTableRow arg="read-only" typ="bool"></ArgTableRow>
<ArgTableRow arg="require-encryption" typ="bool"></ArgTableRow>
<ArgTableRow arg="valid-users" typ="multi { array-id, user: enum
 }"></ArgTableRow>
<ArgTableRow arg="invalid-users" typ="multi { array-id, user: enum
 }"></ArgTableRow>
</ArgTable>
