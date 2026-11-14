---
sidebar_key: "cli-reference/queue/tree/index"
sidebar_position: 1
title: "tree"
sidebar_label: 'tree'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/queue/tree
captured_at: '2026-11-01T21:24:59+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## queue/tree {#queuetree}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">無效</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="parent" typ="enum (global) { global:0xfffff4 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="packet-mark" typ="multi { array-id, packet-mark: enum
 }"></ArgTableRow>
<ArgTableRow arg="limit-at" typ="num"></ArgTableRow>
<ArgTableRow arg="queue" typ="enum"></ArgTableRow>
<ArgTableRow arg="priority" typ="num"></ArgTableRow>
<ArgTableRow arg="max-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="burst-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="burst-threshold" typ="num"></ArgTableRow>
<ArgTableRow arg="burst-time" typ="time"></ArgTableRow>
<ArgTableRow arg="bucket-size" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="packets" typ="num"></ArgTableRow>
<ArgTableRow arg="dropped" typ="num"></ArgTableRow>
<ArgTableRow arg="rate" typ="num"></ArgTableRow>
<ArgTableRow arg="packet-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="queued-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="queued-bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="pcq-queues" typ="num"></ArgTableRow>
</ArgTable>
