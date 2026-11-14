---
sidebar_key: "cli-reference/system/history"
sidebar_position: 11
title: "history"
sidebar_label: 'history'
source: https://manual.mikrotik.com/docs/cli-reference/system/history
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/history {#systemhistory}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="U" typ="undoable"></ArgTableRow>
<ArgTableRow arg="R" typ="redoable"></ArgTableRow>
<ArgTableRow arg="F" typ="floating-undo"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="redo" typ="cfg"></ArgTableRow>
<ArgTableRow arg="undo" typ="cfg"></ArgTableRow>
<ArgTableRow arg="action" typ="string"></ArgTableRow>
<ArgTableRow arg="by" typ="string"></ArgTableRow>
<ArgTableRow arg="policy" typ="multi { array-id, policy: enum
 }"></ArgTableRow>
<ArgTableRow arg="time" typ="date"></ArgTableRow>
<ArgTableRow arg="trace" typ="string"></ArgTableRow>
</ArgTable>
