---
sidebar_key: "cli-reference/interface/bonding/monitor"
sidebar_position: 2
title: "monitor"
sidebar_label: 'monitor'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/bonding/monitor
captured_at: '2026-11-01T21:22:21+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/bonding/monitor {#interfacebondingmonitor}
**型別：** 命令

該命令用於監控 bonding 介面和 bonding 埠。

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="mode" typ="enum (balance-rr | active-backup | balance-xor | broadcast | 802.3ad | balance-tlb | balance-alb) { balance-rr:0, active-backup:1, balance-xor:2, broadcast:3, 802.3ad:4, balance-tlb:5, balance-alb:6 }">使用的 bonding 模式。</ArgTableRow>
<ArgTableRow arg="active-ports" typ="multi { array-id, port: iface_enum
 }">顯示活動的 bonding 埠。</ArgTableRow>
<ArgTableRow arg="inactive-ports" typ="multi { array-id, port: iface_enum
 }">顯示非活動的 bonding 埠（例如已停用或備份介面）。</ArgTableRow>
<ArgTableRow arg="lacp-system-id" typ="macAddr">顯示本地 LACP 系統 ID。</ArgTableRow>
<ArgTableRow arg="lacp-system-priority" typ="num">顯示本地 LACP 優先順序。</ArgTableRow>
<ArgTableRow arg="lacp-partner-system-id" typ="macAddr">顯示對端 LACP 系統 ID。</ArgTableRow>
</ArgTable>
