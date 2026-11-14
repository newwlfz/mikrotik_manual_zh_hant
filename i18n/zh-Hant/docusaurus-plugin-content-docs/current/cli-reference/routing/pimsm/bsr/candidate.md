---
sidebar_key: "cli-reference/routing/pimsm/bsr/candidate"
sidebar_position: 1
title: "candidate"
sidebar_label: 'candidate'
source: https://manual.mikrotik.com/docs/cli-reference/routing/pimsm/bsr/candidate
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/pimsm/bsr/candidate {#routingpimsmbsrcandidate}
**條件：** !smips
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未啟用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="instance" typ="enum"></ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46i)"></ArgTableRow>
<ArgTableRow arg="scope4" typ="address (flags=4/)" unset="1"></ArgTableRow>
<ArgTableRow arg="scope6" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="priority" typ="num"></ArgTableRow>
<ArgTableRow arg="hash-mask-length" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="state" typ="enum (candidate | pending | elected)"></ArgTableRow>
</ArgTable>
