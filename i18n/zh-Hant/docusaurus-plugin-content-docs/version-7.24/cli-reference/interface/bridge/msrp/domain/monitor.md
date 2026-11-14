---
sidebar_key: "cli-reference/interface/bridge/msrp/domain/monitor"
sidebar_position: 2
title: "monitor"
sidebar_label: "monitor"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/bridge/msrp/domain/monitor
captured_at: '2026-11-02T09:09:04+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/bridge/msrp/domain/monitor {#interfacebridgemsrpdomainmonitor}
**條件：** MSRP_ENABLE
**型別：** 命令

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="bridge" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="id" typ="num"></ArgTableRow>
<ArgTableRow arg="priority" typ="num"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num"></ArgTableRow>
<ArgTableRow arg="core-ports" typ="multi { array-id, interface: iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="boundary-ports" typ="multi { array-id, interface: iface_enum
 }"></ArgTableRow>
</ArgTable>
