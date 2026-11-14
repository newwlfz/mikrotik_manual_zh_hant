---
sidebar_key: "cli-reference/interface/pwr-line/monitor"
sidebar_position: 5
title: "monitor"
sidebar_label: 'monitor'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/pwr-line/monitor
captured_at: '2026-11-01T21:23:00+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/pwr-line/monitor {#interfacepwr-linemonitor}
**系統能力：** pwrlink
**型別：** 命令

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="connection-to-plc" typ="enum (ok | no-link) { ok:1, no-link:2 }"></ArgTableRow>
<ArgTableRow arg="tx-flow-control" typ="bool"></ArgTableRow>
<ArgTableRow arg="rx-flow-control" typ="bool"></ArgTableRow>
<ArgTableRow arg="phy-regs" typ="multi { array-id, method: string
 }"></ArgTableRow>
<ArgTableRow arg="plc-actual-network-key" typ="string"></ArgTableRow>
<ArgTableRow arg="plc-hw-platform" typ="string"></ArgTableRow>
<ArgTableRow arg="plc-sw-platform" typ="string"></ArgTableRow>
<ArgTableRow arg="plc-fw-version" typ="string"></ArgTableRow>
<ArgTableRow arg="plc-line-freq" typ="enum (unknown | 50Hz | 60Hz) { unknown:0, 50Hz:1, 60Hz:2 }"></ArgTableRow>
<ArgTableRow arg="plc-zero-crossing" typ="enum (not-yet-detected | detected | missing) { not-yet-detected:0, detected:4, missing:8 }"></ArgTableRow>
<ArgTableRow arg="plc-role" typ="enum (station | proxy-coordinator | central-coordinator) { station:0, proxy-coordinator:1, central-coordinator:2 }"></ArgTableRow>
<ArgTableRow arg="plc-station-count" typ="num"></ArgTableRow>
<ArgTableRow arg="plc-mac" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="plc-cco-mac" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="plc-station-info" typ="string"></ArgTableRow>
</ArgTable>
