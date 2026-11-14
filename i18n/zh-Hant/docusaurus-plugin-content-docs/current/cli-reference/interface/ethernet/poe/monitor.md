---
sidebar_key: "cli-reference/interface/ethernet/poe/monitor"
sidebar_position: 1
title: "monitor"
sidebar_label: 'monitor'
source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/poe/monitor
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/poe/monitor {#interfaceethernetpoemonitor}
**系統能力：**（poe 或 poe-in）
**型別：**命令

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="port-type" typ="enum (poe-out | poe-in | poe-in/poe-out) { poe-out:0, poe-in:1, poe-in/poe-out:2 }" syscap="(poe or poe-in)"></ArgTableRow>
<ArgTableRow arg="poe-out" typ="enum (off | auto-on | forced-on | forced-on-a | forced-on-bt) { off:0, auto-on:1, forced-on:2, forced-on-a:3, forced-on-bt:4 }" syscap="poe"></ArgTableRow>
<ArgTableRow arg="poe-voltage" typ="enum (auto | low | high) { auto:0, low:1, high:2 }" syscap="poe">PoE 輸出電壓選擇</ArgTableRow>
<ArgTableRow arg="poe-out-status" typ="enum (disabled | waiting-for-load | powered-on | overload | short-circuit | voltage-too-low | current-too-low | power-cycle | voltage-too-high | controller-error | controller-upgrade | voltage-on-poe-in | no-valid-PSU | controller-init | low-voltage-too-low | lldp-power-off | low-voltage-pd-detected) { disabled:1, waiting-for-load:2, powered-on:3, overload:4, short-circuit:5, voltage-too-low:6, current-too-low:7, power-cycle:8, voltage-too-high:9, controller-error:10, controller-upgrade:11, voltage-on-poe-in:12, no-valid-PSU:13, controller-init:14, low-voltage-too-low:15, lldp-power-off:16, low-voltage-pd-detected:17 }"></ArgTableRow>
<ArgTableRow arg="poe-out-voltage" typ="num"></ArgTableRow>
<ArgTableRow arg="poe-out-current" typ="num"></ArgTableRow>
<ArgTableRow arg="poe-out-power" typ="num"></ArgTableRow>
<ArgTableRow arg="poe-out-power-pair" typ="enum (b | a | bt) { b:0, a:1, bt:2 }"></ArgTableRow>
<ArgTableRow arg="power-cycle-host-alive" typ="bool"></ArgTableRow>
<ArgTableRow arg="power-cycle-after" typ="time"></ArgTableRow>
</ArgTable>
