---
sidebar_key: "cli-reference/ip/smb/users"
sidebar_position: 2
title: "users"
sidebar_label: "users"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/smb/users
captured_at: '2026-11-01T21:28:57+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/smb/users {#ipsmbusers}
**條件：** !smips
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="*" typ="default">default</ArgTableRow>
<ArgTableRow arg="r" typ="read-only">read-only</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="read-only" typ="bool"></ArgTableRow>
</ArgTable>
