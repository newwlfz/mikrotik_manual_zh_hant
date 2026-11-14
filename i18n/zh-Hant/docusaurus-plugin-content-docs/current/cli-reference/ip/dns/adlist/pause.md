---
sidebar_key: "cli-reference/ip/dns/adlist/pause"
sidebar_position: 1
title: "pause"
sidebar_label: 'pause'
source: https://manual.mikrotik.com/docs/cli-reference/ip/dns/adlist/pause
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/dns/adlist/pause {#ipdnsadlistpause}
**型別：** 命令

在指定時間內停止所有 adlist 的攔截，例如 `/ip/dns/adlist/pause duration=10m`。時間結束後攔截會自動恢復。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="duration" typ="time">停止攔截的持續時間。`duration=0` 會結束當前暫停。</ArgTableRow>
</ArgTable>
