---
sidebar_key: "cli-reference/system/ptp/port"
sidebar_position: 2
title: "port"
sidebar_label: 'port'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/system/ptp/port
captured_at: '2026-11-01T21:25:37+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/ptp/port {#systemptpport}
**條件：** !smips
**系統能力：** ptp
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="ptp" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="role" typ="enum (bmca | master | slave)"></ArgTableRow>
<ArgTableRow arg="announce-interval" typ="num"></ArgTableRow>
<ArgTableRow arg="sync-interval" typ="num"></ArgTableRow>
<ArgTableRow arg="delay-interval" typ="num"></ArgTableRow>
<ArgTableRow arg="pdelay-interval" typ="num"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num"></ArgTableRow>
</ArgTable>
