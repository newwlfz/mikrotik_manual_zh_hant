---
sidebar_key: "cli-reference/interface/bonding/monitor-slaves"
sidebar_position: 1
title: "monitor-slaves"
sidebar_label: "monitor-slaves"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/bonding/monitor-slaves
captured_at: '2026-11-01T21:26:56+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/bonding/monitor-slaves {#interfacebondingmonitor-slaves}
**型別：** 命令

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="A" typ="active">已啟用</ArgTableRow>
<ArgTableRow arg="P" typ="partner">partner</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="bond" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="once" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="port" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="key" typ="num"></ArgTableRow>
<ArgTableRow arg="flags" typ="string"></ArgTableRow>
<ArgTableRow arg="partner-sys-id" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="partner-sys-priority" typ="num"></ArgTableRow>
<ArgTableRow arg="partner-key" typ="num"></ArgTableRow>
<ArgTableRow arg="partner-flags" typ="string"></ArgTableRow>
</ArgTable>
