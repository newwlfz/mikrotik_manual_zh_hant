---
sidebar_key: "cli-reference/certificate/scep-server/index"
sidebar_position: 1
title: "scep-server"
sidebar_label: "scep-server"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/certificate/scep-server
captured_at: '2026-11-01T21:26:26+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## certificate/scep-server {#certificatescep-server}
**型別：**目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="ca-cert" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="next-ca-cert" typ="enum (none) { none:0 }"></ArgTableRow>
<ArgTableRow arg="path" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="days-valid" typ="num"></ArgTableRow>
<ArgTableRow arg="request-lifetime" typ="time"></ArgTableRow>
</ArgTable>
