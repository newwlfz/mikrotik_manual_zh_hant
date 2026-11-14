---
sidebar_key: "cli-reference/openflow/index"
sidebar_position: 3
title: "openflow"
sidebar_label: "openflow"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/openflow
captured_at: '2026-11-01T21:29:17+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## openflow {#openflow}
**軟體包：** openflow
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="datapath-id" typ="super { number: num [0 .. 65535]
, [mac-address] /macAddr
 }"></ArgTableRow>
<ArgTableRow arg="version" typ="enum (default | 1 | 1.3)"></ArgTableRow>
<ArgTableRow arg="passive-port" typ="num"></ArgTableRow>
<ArgTableRow arg="controllers" typ="object { contr: super { controler-protocol: enum (tcp | tls)
, [controller-address] /ip6Addr
, [controller-port] /num [1 .. 65535]
 }
 }"></ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none)" unset="1"></ArgTableRow>
<ArgTableRow arg="verify-peer" typ="enum (required | none | if-cert-present)" unset="1"></ArgTableRow>
<ArgTableRow arg="isolate-controllers" typ="bool" unset="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="openflow-fast-path-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="openflow-fast-path-bytes" typ="num"></ArgTableRow>
</ArgTable>
