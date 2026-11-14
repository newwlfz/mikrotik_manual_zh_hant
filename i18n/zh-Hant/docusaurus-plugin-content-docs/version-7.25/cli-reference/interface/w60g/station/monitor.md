---
sidebar_key: "cli-reference/interface/w60g/station/monitor"
sidebar_position: 1
title: "monitor"
sidebar_label: 'monitor'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/w60g/station/monitor
captured_at: '2026-11-01T21:23:04+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/w60g/station/monitor {#interfacew60gstationmonitor}
**系統能力：** 60ghz
**軟體包：** wireless-rep
**型別：** 命令

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="connected" typ="bool"></ArgTableRow>
<ArgTableRow arg="remote" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="tx-mode" typ="enum (dmg | edmg-cb1 | edmg-cb2 | edmg-cb1-long-ldpc | edmg-cb2-long-ldpc) { dmg:0, edmg-cb1:1, edmg-cb2:2, edmg-cb1-long-ldpc:3, edmg-cb2-long-ldpc:4 }"></ArgTableRow>
<ArgTableRow arg="tx-mcs" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-phy-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="signal" typ="num"></ArgTableRow>
<ArgTableRow arg="rssi" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-sector" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-sector-info" typ="string"></ArgTableRow>
<ArgTableRow arg="distance" typ="num"></ArgTableRow>
</ArgTable>
