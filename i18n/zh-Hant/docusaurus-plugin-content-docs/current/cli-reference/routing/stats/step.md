---
sidebar_key: "cli-reference/routing/stats/step"
sidebar_position: 5
title: "step"
sidebar_label: 'step'
source: https://manual.mikrotik.com/docs/cli-reference/routing/stats/step
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/stats/step {#routingstatsstep}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="context" typ="string"></ArgTableRow>
<ArgTableRow arg="pid" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="order" typ="num"></ArgTableRow>
<ArgTableRow arg="runs" typ="num"></ArgTableRow>
<ArgTableRow arg="targets" typ="num"></ArgTableRow>
<ArgTableRow arg="max-time" typ="time"></ArgTableRow>
<ArgTableRow arg="cur-time" typ="time"></ArgTableRow>
<ArgTableRow arg="state" typ="enum (off | on | once) { off:0, on:1, once:2 }"></ArgTableRow>
<ArgTableRow arg="sched" typ="time"></ArgTableRow>
</ArgTable>
