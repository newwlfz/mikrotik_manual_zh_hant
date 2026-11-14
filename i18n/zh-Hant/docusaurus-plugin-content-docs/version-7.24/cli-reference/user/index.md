---
sidebar_key: "cli-reference/user/index"
sidebar_position: 5
title: "user"
sidebar_label: "user"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/user
captured_at: '2026-11-01T21:30:28+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## 使用者 {#user}

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="E" typ="expired">已過期</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="group" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="password" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="inactivity-timeout" typ="time">超過該時間段後應用無活動策略</ArgTableRow>
<ArgTableRow arg="inactivity-policy" typ="enum (none | logout | lockscreen)">指定無活動超時後執行的操作</ArgTableRow>
<ArgTableRow arg="address" typ="object { address: alt { address: ipPrefix
, address: ip6Prefix
 }
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="last-logged-in" typ="date"></ArgTableRow>
</ArgTable>
