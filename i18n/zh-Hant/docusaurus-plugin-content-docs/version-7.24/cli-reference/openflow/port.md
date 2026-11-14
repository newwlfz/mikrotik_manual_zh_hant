---
sidebar_key: "cli-reference/openflow/port"
sidebar_position: 4
title: "port"
sidebar_label: "port"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/openflow/port
captured_at: '2026-11-01T21:29:19+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## openflow/port {#openflowport}
**包：** openflow
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="enum ()" mandatory="1"></ArgTableRow>
<ArgTableRow arg="switch" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="port-id" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="tx-bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-packets" typ="num"></ArgTableRow>
</ArgTable>
