---
sidebar_key: "cli-reference/interface/wireless/nstreme-dual/monitor"
sidebar_position: 1
title: "monitor"
sidebar_label: 'monitor'
source: https://manual.mikrotik.com/docs/cli-reference/interface/wireless/nstreme-dual/monitor
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/wireless/nstreme-dual/monitor {#interfacewirelessnstreme-dualmonitor}
**軟體包：** wireless-rep
**型別：** 命令

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="rx-signal-strength" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-signal-strength" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-rate" typ="string"></ArgTableRow>
<ArgTableRow arg="tx-rate" typ="string"></ArgTableRow>
<ArgTableRow arg="connected" typ="bool"></ArgTableRow>
<ArgTableRow arg="packets" typ="composite { tx: num
, rx: num
 }"></ArgTableRow>
<ArgTableRow arg="bytes" typ="composite { tx: num
, rx: num
 }"></ArgTableRow>
<ArgTableRow arg="frames" typ="composite { tx: num
, rx: num
 }"></ArgTableRow>
<ArgTableRow arg="frame-bytes" typ="composite { tx: num
, rx: num
 }"></ArgTableRow>
<ArgTableRow arg="hw-frames" typ="composite { tx: num
, rx: num
 }"></ArgTableRow>
<ArgTableRow arg="hw-frame-bytes" typ="composite { tx: num
, rx: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-retries-timeout" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-retries-lost" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-bad-seqs" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-duplicates" typ="num"></ArgTableRow>
</ArgTable>
