---
sidebar_key: "cli-reference/iot/lora/servers"
title: "servers"
sidebar_label: 'servers'
source: https://manual.mikrotik.com/docs/cli-reference/iot/lora/servers
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## iot/lora/servers {#iotloraservers}
**軟體包：** iot
**型別：** 目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="address" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="up-port" typ="num"></ArgTableRow>
<ArgTableRow arg="down-port" typ="num"></ArgTableRow>
<ArgTableRow arg="key" typ="string"></ArgTableRow>
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="interval" typ="num"></ArgTableRow>
<ArgTableRow arg="ssl" typ="bool"></ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="protocol" typ="enum (UDP | LNS | CUPS)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="netid" typ="multi { netid: enum
 }"></ArgTableRow>
<ArgTableRow arg="joineui" typ="multi { joineui: enum
 }"></ArgTableRow>
</ArgTable>
