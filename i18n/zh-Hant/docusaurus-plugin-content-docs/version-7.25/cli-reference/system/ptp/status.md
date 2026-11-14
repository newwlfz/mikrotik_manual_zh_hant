---
sidebar_key: "cli-reference/system/ptp/status"
sidebar_position: 3
title: "status"
sidebar_label: 'status'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/system/ptp/status
captured_at: '2026-11-01T21:25:37+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/ptp/status {#systemptpstatus}
**條件：** !smips
**系統能力：** ptp
**型別：** 目錄

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="state" typ="string"></ArgTableRow>
<ArgTableRow arg="delay" typ="num"></ArgTableRow>
<ArgTableRow arg="port-nr" typ="num"></ArgTableRow>
<ArgTableRow arg="as-capable" typ="bool"></ArgTableRow>
<ArgTableRow arg="neigh-freq-drift" typ="num"></ArgTableRow>
</ArgTable>
