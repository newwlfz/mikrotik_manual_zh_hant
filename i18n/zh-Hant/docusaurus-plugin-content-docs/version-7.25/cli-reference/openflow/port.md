---
sidebar_key: "cli-reference/openflow/port"
sidebar_position: 4
title: "port"
sidebar_label: 'port'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/openflow/port
captured_at: '2026-11-01T21:24:54+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## openflow/port {#openflowport}
**包：** openflow
**型別：** 目錄

此選單列出由 OpenFlow 控制的埠。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="enum ()" mandatory="1">要由 OpenFlow 控制的介面名稱。</ArgTableRow>
<ArgTableRow arg="switch" typ="enum" mandatory="1">能夠控制該埠的交換器名稱。</ArgTableRow>
<ArgTableRow arg="port-id" typ="num">用於在流規則中標識該介面的埠 ID。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="tx-bytes" typ="num">在介面上傳輸的位元組數。</ArgTableRow>
<ArgTableRow arg="tx-packets" typ="num">在介面上傳輸的封包數。</ArgTableRow>
<ArgTableRow arg="rx-bytes" typ="num">在介面上接收的位元組數。</ArgTableRow>
<ArgTableRow arg="rx-packets" typ="num">在介面上接收的封包數。</ArgTableRow>
</ArgTable>
