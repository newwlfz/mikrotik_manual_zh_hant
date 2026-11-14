---
sidebar_key: "cli-reference/system/ptp/monitor"
sidebar_position: 1
title: "monitor"
sidebar_label: 'monitor'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/system/ptp/monitor
captured_at: '2026-11-01T21:25:37+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/ptp/monitor {#systemptpmonitor}
**條件：** !smips
**系統能力：** ptp
**型別：** 命令

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="clock-id" typ="string"></ArgTableRow>
<ArgTableRow arg="priority1" typ="num"></ArgTableRow>
<ArgTableRow arg="priority2" typ="num"></ArgTableRow>
<ArgTableRow arg="i-am-gm" typ="bool"></ArgTableRow>
<ArgTableRow arg="gm-clock-id" typ="string"></ArgTableRow>
<ArgTableRow arg="gm-priority1" typ="num"></ArgTableRow>
<ArgTableRow arg="gm-priority2" typ="num"></ArgTableRow>
<ArgTableRow arg="master-clock-id" typ="string"></ArgTableRow>
<ArgTableRow arg="slave-port" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="freq-drift" typ="num"></ArgTableRow>
<ArgTableRow arg="offset" typ="num"></ArgTableRow>
<ArgTableRow arg="slave-port-delay" typ="num"></ArgTableRow>
</ArgTable>
