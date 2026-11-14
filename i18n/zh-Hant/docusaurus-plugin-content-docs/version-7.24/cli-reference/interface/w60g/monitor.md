---
sidebar_key: "cli-reference/interface/w60g/monitor"
sidebar_position: 2
title: "monitor"
sidebar_label: "monitor"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/w60g/monitor
captured_at: '2026-11-01T21:27:42+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/w60g/monitor {#interfacew60gmonitor}
**系統能力：** 60ghz
**軟體包：** wireless-rep
**型別：** 命令

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="connected" typ="bool"></ArgTableRow>
<ArgTableRow arg="frequency" typ="num"></ArgTableRow>
<ArgTableRow arg="remote-address" typ="multi { array-id, remote-address: macAddr
 }"></ArgTableRow>
<ArgTableRow arg="tx-mcs" typ="multi { array-id, tx-mcs: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-phy-rate" typ="multi { array-id, tx-phy-rate: num
 }"></ArgTableRow>
<ArgTableRow arg="signal" typ="multi { array-id, signal: num
 }"></ArgTableRow>
<ArgTableRow arg="rssi" typ="multi { array-id, rssi: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-sector" typ="multi { array-id, tx-sector: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-sector-info" typ="multi { array-id, tx-sector-info: string
 }"></ArgTableRow>
<ArgTableRow arg="distance" typ="multi { array-id, distance: num
 }"></ArgTableRow>
<ArgTableRow arg="baseband-temperature" typ="num"></ArgTableRow>
<ArgTableRow arg="rf-temperature" typ="multi { array-id, rf-temperature: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-packet-error-rate" typ="num"></ArgTableRow>
</ArgTable>
