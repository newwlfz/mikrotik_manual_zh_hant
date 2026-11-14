---
sidebar_key: "cli-reference/zerotier/peer/hint"
sidebar_position: 1
title: "hint"
sidebar_label: "hint"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/zerotier/peer/hint
captured_at: '2026-11-01T21:30:37+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## zerotier/peer/hint {#zerotierpeerhint}
**包：** zerotier
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="instance" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="identity" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="addresses" typ="multi { array-id, array-id, address: composite { addr: address (flags=46)
, port: num [1 .. 65535]
 }
 }" mandatory="1"></ArgTableRow>
</ArgTable>
