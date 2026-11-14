---
sidebar_key: "cli-reference/tool/romon/port"
sidebar_position: 3
title: "port"
sidebar_label: "port"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/tool/romon/port
captured_at: '2026-11-01T21:30:19+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/romon/port {#toolromonport}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="*" typ="default">default</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum { all }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="forbid" typ="bool"></ArgTableRow>
<ArgTableRow arg="cost" typ="num"></ArgTableRow>
<ArgTableRow arg="secrets" typ="multi { array-id, name: string
 }"></ArgTableRow>
</ArgTable>
