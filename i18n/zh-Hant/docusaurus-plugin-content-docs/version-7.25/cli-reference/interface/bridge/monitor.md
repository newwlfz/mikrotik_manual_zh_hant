---
sidebar_key: "cli-reference/interface/bridge/monitor"
sidebar_position: 5
title: "monitor"
sidebar_label: 'monitor'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/bridge/monitor
captured_at: '2026-11-01T21:22:25+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/bridge/monitor {#interfacebridgemonitor}
**型別：** 命令

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="state" typ="enum (disabled | disabled | enabled | enabled)"></ArgTableRow>
<ArgTableRow arg="current-mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="bridge-id" typ="composite { prio: num
, mac: macAddr
 }"></ArgTableRow>
<ArgTableRow arg="root-bridge" typ="bool"></ArgTableRow>
<ArgTableRow arg="root-bridge-id" typ="composite { prio: num
, mac: macAddr
 }"></ArgTableRow>
<ArgTableRow arg="regional-root-bridge-id" typ="composite { prio: num
, mac: macAddr
 }"></ArgTableRow>
<ArgTableRow arg="root-path-cost" typ="num"></ArgTableRow>
<ArgTableRow arg="root-port" typ="iface_enum { none:0 }"></ArgTableRow>
<ArgTableRow arg="port-count" typ="num"></ArgTableRow>
<ArgTableRow arg="designated-port-count" typ="num"></ArgTableRow>
<ArgTableRow arg="mst-config-digest" typ="string"></ArgTableRow>
<ArgTableRow arg="fast-forward" typ="bool"></ArgTableRow>
<ArgTableRow arg="multicast-router" typ="bool"></ArgTableRow>
<ArgTableRow arg="igmp-querier" typ="composite { interface: iface_enum { none:0 }
, ip-address: ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="mld-querier" typ="composite { interface: iface_enum { none:0 }
, ipv6-address: ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="declared-vlan-ids" typ="multi { vlan-range: range
 }"></ArgTableRow>
<ArgTableRow arg="registered-vlan-ids" typ="multi { vlan-range: range
 }"></ArgTableRow>
<ArgTableRow arg="mlag-state" typ="string">顯示 MLAG 連線狀態：當 ICCP 建立後為 `connected`，當對等體建立或重新建立連線時為 `connecting`，或者當配置的對等埠不可用時顯示諸如 `peer port not running` 之類的錯誤。</ArgTableRow>
<ArgTableRow arg="mlag-active-role" typ="enum (primary | secondary)">具有最低 `priority` 的對等體會充當主裝置。如果優先順序相同，則具有最低橋 MAC 地址的對等體成為主裝置。主裝置的 `system-id` 用於傳送 (R/M)STP BPDU 橋識別符號和 LACP 系統 ID。該角色在 MLAG 連線成功後會顯示。</ArgTableRow>
</ArgTable>
