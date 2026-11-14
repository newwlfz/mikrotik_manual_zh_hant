---
sidebar_key: "cli-reference/interface/wifi/datapath"
sidebar_position: 8
title: "datapath"
sidebar_label: 'datapath'
source: https://manual.mikrotik.com/docs/cli-reference/interface/wifi/datapath
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/wifi/datapath {#interfacewifidatapath}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="bridge" typ="iface_enum { none }" unset="1"></ArgTableRow>
<ArgTableRow arg="bridge-cost" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bridge-horizon" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="openflow-switch" typ="enum" unset="1" syscap="openflow"></ArgTableRow>
<ArgTableRow arg="client-isolation" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="traffic-processing" typ="enum (on-cap | on-capsman | on-capsman-secure)" unset="1"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="interface-list" typ="enum" unset="1"></ArgTableRow>
</ArgTable>
