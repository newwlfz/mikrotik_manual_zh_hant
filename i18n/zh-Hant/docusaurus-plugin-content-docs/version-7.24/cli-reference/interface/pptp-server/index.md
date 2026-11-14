---
sidebar_key: "cli-reference/interface/pptp-server/index"
sidebar_position: 1
title: "pptp-server"
sidebar_label: "pptp-server"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/pptp-server
captured_at: '2026-11-01T21:27:34+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/pptp-server {#interfacepptp-server}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="user" typ="string" mandatory="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="mru" typ="num"></ArgTableRow>
<ArgTableRow arg="client-address" typ="string"></ArgTableRow>
<ArgTableRow arg="uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="encoding" typ="string"></ArgTableRow>
</ArgTable>
