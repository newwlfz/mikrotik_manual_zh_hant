---
sidebar_key: "cli-reference/user-manager/user-profile/index"
sidebar_position: 2
title: "user-profile"
sidebar_label: 'user-profile'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/user-manager/user-profile
captured_at: '2026-11-01T21:26:12+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## user-manager/user-profile {#user-manageruser-profile}
**包：** userman-5
**型別：** 目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="user" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="profile" typ="enum" mandatory="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="state" typ="enum (waiting | running | running-active | used)"></ArgTableRow>
<ArgTableRow arg="end-time" typ="alt { constant: enum (not-yet-running | unlimited)
, date: date
 }"></ArgTableRow>
</ArgTable>
