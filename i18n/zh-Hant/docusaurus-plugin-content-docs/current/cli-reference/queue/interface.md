---
sidebar_key: "cli-reference/queue/interface"
sidebar_position: 1
title: "interface"
sidebar_label: 'interface'
source: https://manual.mikrotik.com/docs/cli-reference/queue/interface
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## queue/interface {#queueinterface}
**型別：** 目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="queue" typ="enum (no-queue) { no-queue:0 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="default-queue" typ="enum (no-queue) { no-queue:0 }"></ArgTableRow>
<ArgTableRow arg="active-queue" typ="enum (no-queue | queue-tree) { no-queue:0, queue-tree:0xfffffff9 }"></ArgTableRow>
</ArgTable>
