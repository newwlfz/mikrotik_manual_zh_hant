---
sidebar_key: "cli-reference/interface/vpls/monitor"
sidebar_position: 1
title: "monitor"
sidebar_label: 'monitor'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/vpls/monitor
captured_at: '2026-11-01T21:23:03+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/vpls/monitor {#interfacevplsmonitor}
**條件：** !smips
**型別：** 命令

該命令顯示當前的 VPLS 介面狀態。

例如：

```ros
[admin@10.0.11.23] /interface/vpls> monitor vpls2
remote-label: 800000
local-label: 43
remote-status: 
transport: 10.255.11.201/32
transport-nexthop: 10.0.11.201
imposed-labels: 800000
```

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="remote-label" typ="num">由遠端對等體為此偽線分配的 MPLS 標籤（RFC 4447 第 5.1 節）。</ArgTableRow>
<ArgTableRow arg="local-label" typ="num">為此偽線在本地分配的 MPLS 標籤（RFC 4447 第 5.1 節）。</ArgTableRow>
<ArgTableRow arg="remote-status" typ="ubit (not-forwarding, attachment-circuit-rx-fault, attachment-circuit-tx-fault, pw-rx-fault, pw-tx-fault)">透過 LDP 狀態信令從遠端對等體接收到的偽線狀態（RFC 4447 第 5.4 節）。</ArgTableRow>
<ArgTableRow arg="remote-group" typ="num">遠端對等體的組 ID，用於 LDP 狀態撤銷聚合（RFC 4447 第 5.3 節）。</ArgTableRow>
<ArgTableRow arg="te-tunnel" typ="enum">傳輸介面的名稱。當 VPLS 執行在 [流量工程](../../../user-guides/routing-and-networking-protocols/mpls/traffic-eng.md) 隧道上時顯示。</ArgTableRow>
<ArgTableRow arg="nexthops" typ="object { label: enum (expl-null | alert | expl-null6 | impl-null) { expl-null:0, alert:1, expl-null6:2, impl-null:3 }
, nh: address
, interface: iface_enum
 }">正在使用的傳輸下一跳。</ArgTableRow>
</ArgTable>
