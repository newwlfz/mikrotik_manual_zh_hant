---
sidebar_key: "cli-reference/user-manager/profile"
sidebar_position: 9
title: "profile"
sidebar_label: 'profile'
source: https://manual.mikrotik.com/docs/cli-reference/user-manager/profile
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## user-manager/profile {#user-managerprofile}
**軟體包：** userman-5
**型別：** 目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="validity" typ="alt { validity: enum (unlimited) { unlimited:0 }
, validity: time
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="name-for-users" typ="string"></ArgTableRow>
<ArgTableRow arg="starts-when" typ="enum (first-auth | assigned)"></ArgTableRow>
<ArgTableRow arg="price" typ="num"></ArgTableRow>
<ArgTableRow arg="override-shared-users" typ="enum (off | unlimited) { off:-1, unlimited:0 }"></ArgTableRow>
</ArgTable>
