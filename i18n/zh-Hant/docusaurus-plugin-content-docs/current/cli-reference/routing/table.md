---
sidebar_key: "cli-reference/routing/table"
sidebar_position: 19
title: "table"
sidebar_label: 'table'
source: https://manual.mikrotik.com/docs/cli-reference/routing/table
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/table {#routingtable}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">無效</ArgTableRow>
<ArgTableRow arg="U" typ="used">已使用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">路由表的名稱。</ArgTableRow>
<ArgTableRow arg="fib" typ="switch" unset="1">標誌，指示此表中的路由是否會被安裝到 [FIB](../../user-guides/routing-and-networking-protocols/routing-decision.md#forwarding-information-base) 中。</ArgTableRow>
</ArgTable>
