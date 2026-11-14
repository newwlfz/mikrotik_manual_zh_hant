---
sidebar_key: "cli-reference/zerotier/controller/member"
sidebar_position: 1
title: "member"
sidebar_label: "member"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/zerotier/controller/member
captured_at: '2026-11-01T21:30:40+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## zerotier/controller/member {#zerotiercontrollermember}
**包：** zerotier
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
<ArgTableRow arg="A" typ="authorized"></ArgTableRow>
<ArgTableRow arg="B" typ="bridge"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="disabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="network" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="zt-address" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="authorized" typ="bool"></ArgTableRow>
<ArgTableRow arg="bridge" typ="bool"></ArgTableRow>
<ArgTableRow arg="ip-address" typ="multi { array-id, addr: address (flags=46)
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="lost" typ="bool"></ArgTableRow>
<ArgTableRow arg="last-seen" typ="time"></ArgTableRow>
</ArgTable>
