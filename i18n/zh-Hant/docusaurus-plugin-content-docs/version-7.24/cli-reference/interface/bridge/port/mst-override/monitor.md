---
sidebar_key: "cli-reference/interface/bridge/port/mst-override/monitor"
sidebar_position: 1
title: "monitor"
sidebar_label: "monitor"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/bridge/port/mst-override/monitor
captured_at: '2026-11-01T21:27:04+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/bridge/port/mst-override/monitor {#interfacebridgeportmst-overridemonitor}
**型別：** 命令

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="port" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="status" typ="enum (inactive | in-bridge | in-bridge | disabled)"></ArgTableRow>
<ArgTableRow arg="identifier" typ="num"></ArgTableRow>
<ArgTableRow arg="port-id" typ="composite { priority: num
, number: num
 }"></ArgTableRow>
<ArgTableRow arg="role" typ="enum (disabled-port | root-port | designated-port | alternate-port | backup-port | master-port) { disabled-port:0, root-port:1, designated-port:2, alternate-port:3, backup-port:4, master-port:5 }"></ArgTableRow>
<ArgTableRow arg="learning" typ="bool"></ArgTableRow>
<ArgTableRow arg="forwarding" typ="bool"></ArgTableRow>
<ArgTableRow arg="internal-root-path-cost" typ="num"></ArgTableRow>
<ArgTableRow arg="designated-bridge-id" typ="composite { number: num
, address: macAddr
 }"></ArgTableRow>
<ArgTableRow arg="designated-cost" typ="num"></ArgTableRow>
<ArgTableRow arg="designated-internal-cost" typ="num"></ArgTableRow>
<ArgTableRow arg="designated-port-id" typ="composite { priority: num
, number: num
 }"></ArgTableRow>
<ArgTableRow arg="designated-remaining-hops" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-rx-bpdu" typ="composite { tx: num
, rx: num
 }"></ArgTableRow>
<ArgTableRow arg="discard-transitions" typ="num"></ArgTableRow>
<ArgTableRow arg="forward-transitions" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-rx-tc" typ="composite { tx: num
, rx: num
 }"></ArgTableRow>
<ArgTableRow arg="topology-changes" typ="num"></ArgTableRow>
<ArgTableRow arg="last-topology-change" typ="time"></ArgTableRow>
</ArgTable>
