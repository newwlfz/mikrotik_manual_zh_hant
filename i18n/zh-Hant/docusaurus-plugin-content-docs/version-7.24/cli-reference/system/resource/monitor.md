---
sidebar_key: "cli-reference/system/resource/monitor"
sidebar_position: 4
title: "monitor"
sidebar_label: "monitor"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/system/resource/monitor
captured_at: '2026-11-01T21:30:05+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/resource/monitor {#systemresourcemonitor}
**型別：** 命令

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="cpu-used" typ="num"></ArgTableRow>
<ArgTableRow arg="cpu-used-per-core" typ="multi { cpu-used: num
 }" syscap="smp"></ArgTableRow>
<ArgTableRow arg="free-memory" typ="num"></ArgTableRow>
</ArgTable>
