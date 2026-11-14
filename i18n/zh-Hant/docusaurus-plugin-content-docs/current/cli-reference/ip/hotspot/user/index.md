---
sidebar_key: "cli-reference/ip/hotspot/user"
title: "user"
sidebar_label: 'user'
source: https://manual.mikrotik.com/docs/cli-reference/ip/hotspot/user
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/hotspot/user {#iphotspotuser}
**型別：**目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="*" typ="default">default</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="server" typ="enum (all) { all:0 }"></ArgTableRow>
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="otp-secret" typ="string"></ArgTableRow>
<ArgTableRow arg="address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="profile" typ="enum"></ArgTableRow>
<ArgTableRow arg="routes" typ="string"></ArgTableRow>
<ArgTableRow arg="email" typ="string"></ArgTableRow>
<ArgTableRow arg="limit-uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="limit-bytes-in" typ="num"></ArgTableRow>
<ArgTableRow arg="limit-bytes-out" typ="num"></ArgTableRow>
<ArgTableRow arg="limit-bytes-total" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="bytes-in" typ="num"></ArgTableRow>
<ArgTableRow arg="bytes-out" typ="num"></ArgTableRow>
<ArgTableRow arg="packets-in" typ="num"></ArgTableRow>
<ArgTableRow arg="packets-out" typ="num"></ArgTableRow>
</ArgTable>
