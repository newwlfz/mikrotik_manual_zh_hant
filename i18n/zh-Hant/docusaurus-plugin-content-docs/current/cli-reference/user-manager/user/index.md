---
sidebar_key: "cli-reference/user-manager/user"
title: "user"
sidebar_label: 'user'
source: https://manual.mikrotik.com/docs/cli-reference/user-manager/user
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## user-manager/user {#user-manageruser}
**軟體包：** userman-5
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="otp-secret" typ="string"></ArgTableRow>
<ArgTableRow arg="group" typ="enum"></ArgTableRow>
<ArgTableRow arg="shared-users" typ="enum (unlimited) { unlimited:0 }"></ArgTableRow>
<ArgTableRow arg="caller-id" typ="enum (bind)"></ArgTableRow>
<ArgTableRow arg="attributes" typ="object { attribute-value: super { attribute: enum
, [value] :string
 }
 }"></ArgTableRow>
</ArgTable>
