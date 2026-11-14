---
sidebar_key: "cli-reference/container/mounts"
sidebar_position: 6
title: "mounts"
sidebar_label: 'mounts'
source: https://manual.mikrotik.com/docs/cli-reference/container/mounts
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## container/mounts {#containermounts}
**軟體包：** container
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="list" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="src" typ="file"></ArgTableRow>
<ArgTableRow arg="dst" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="mode" typ="enum (rw | ro | rw,noexec | ro,noexec)"></ArgTableRow>
</ArgTable>
