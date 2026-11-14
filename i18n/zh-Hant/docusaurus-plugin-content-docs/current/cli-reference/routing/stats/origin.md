---
sidebar_key: "cli-reference/routing/stats/origin"
sidebar_position: 2
title: "origin"
sidebar_label: 'origin'
source: https://manual.mikrotik.com/docs/cli-reference/routing/stats/origin
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/stats/origin {#routingstatsorigin}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="Y" typ="synthetic">synthetic</ArgTableRow>
<ArgTableRow arg="Z" typ="terminal">terminal</ArgTableRow>
<ArgTableRow arg="X" typ="stopping">stopping</ArgTableRow>
<ArgTableRow arg="A" typ="abandoned">abandoned</ArgTableRow>
<ArgTableRow arg="H" typ="hold">hold</ArgTableRow>
<ArgTableRow arg="U" typ="attrs-updated">attrs-updated</ArgTableRow>
<ArgTableRow arg="M" typ="attrs-merge">attrs-merge</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="type" typ="string"></ArgTableRow>
<ArgTableRow arg="instance-id" typ="num"></ArgTableRow>
<ArgTableRow arg="dealer-id" typ="num"></ArgTableRow>
<ArgTableRow arg="publisher-idx" typ="num"></ArgTableRow>
<ArgTableRow arg="route-type" typ="string"></ArgTableRow>
<ArgTableRow arg="pid" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="route-count" typ="multi { route-count: num
 }"></ArgTableRow>
<ArgTableRow arg="in-policy" typ="num"></ArgTableRow>
<ArgTableRow arg="update.in-policy" typ="num"></ArgTableRow>
<ArgTableRow arg="total-route-count" typ="num"></ArgTableRow>
</ArgTable>
