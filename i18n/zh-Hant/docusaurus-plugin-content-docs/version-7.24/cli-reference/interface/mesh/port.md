---
sidebar_key: "cli-reference/interface/mesh/port"
sidebar_position: 2
title: "port"
sidebar_label: "port"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/mesh/port
captured_at: '2026-11-01T21:27:31+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/mesh/port {#interfacemeshport}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未啟用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="mesh" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="path-cost" typ="num"></ArgTableRow>
<ArgTableRow arg="hello-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="port-type" typ="enum (auto | WDS | wireless | ethernet) { auto:0, WDS:1, wireless:2, ethernet:3 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="active-port-type" typ="enum (wireless | WDS | ethernet-mesh | ethernet-bridge | ethernet-mixed) { wireless:1, WDS:2, ethernet-mesh:3, ethernet-bridge:4, ethernet-mixed:5 }"></ArgTableRow>
<ArgTableRow arg="dr-address" typ="macAddr"></ArgTableRow>
</ArgTable>
