---
sidebar_key: "cli-reference/user-manager/router/index"
sidebar_position: 1
title: "router"
sidebar_label: 'router'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/user-manager/router
captured_at: '2026-11-01T21:26:09+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## user-manager/router {#user-managerrouter}
**軟體包：** userman-5
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46/)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="protocol" typ="enum (udp | radsec)"></ArgTableRow>
<ArgTableRow arg="shared-secret" typ="string"></ArgTableRow>
<ArgTableRow arg="coa-port" typ="num"></ArgTableRow>
</ArgTable>
