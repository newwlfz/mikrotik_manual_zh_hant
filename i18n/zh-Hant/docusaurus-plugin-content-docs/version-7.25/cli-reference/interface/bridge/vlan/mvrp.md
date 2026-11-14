---
sidebar_key: "cli-reference/interface/bridge/vlan/mvrp"
sidebar_position: 1
title: "mvrp"
sidebar_label: 'mvrp'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/bridge/vlan/mvrp
captured_at: '2026-11-01T21:22:26+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/bridge/vlan/mvrp {#interfacebridgevlanmvrp}
**型別：** 目錄

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="bridge" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="port" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num"></ArgTableRow>
<ArgTableRow arg="registrar-state" typ="enum (IN | LV | MT) { IN:1, LV:2, MT:3 }"></ArgTableRow>
<ArgTableRow arg="applicant-state" typ="enum (Very anxious Observer | Very anxious Passive | Very anxious New | Anxious New | Anxious Active | Quiet Active | Leaving Active | Anxious Observer | Quiet Observer | Anxious Passive | Quiet Passive | Leaving Observer) { Very anxious Observer:1, Very anxious Passive:2, Very anxious New:3, Anxious New:4, Anxious Active:5, Quiet Active:6, Leaving Active:7, Anxious Observer:8, Quiet Observer:9, Anxious Passive:10, Quiet Passive:11, Leaving Observer:12 }"></ArgTableRow>
<ArgTableRow arg="last-event" typ="enum (New | JoinIn | In | JoinEmpty | Empty | Leave) { New:0, JoinIn:1, In:2, JoinEmpty:3, Empty:4, Leave:5 }"></ArgTableRow>
</ArgTable>
