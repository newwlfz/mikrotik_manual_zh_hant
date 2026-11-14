---
sidebar_key: "cli-reference/ip/hotspot/walled-garden"
title: "walled-garden"
sidebar_label: 'walled-garden'
source: https://manual.mikrotik.com/docs/cli-reference/ip/hotspot/walled-garden
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/hotspot/walled-garden {#iphotspotwalled-garden}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="server" typ="super { !
, server: enum
 }"></ArgTableRow>
<ArgTableRow arg="src-address" typ="super { !
, range: ipRange
 }"></ArgTableRow>
<ArgTableRow arg="method" typ="super { !
, method: enum (GET | HEAD | POST | PUT | CONNECT | OPTIONS | DELETE | TRACE)
 }"></ArgTableRow>
<ArgTableRow arg="dst-host" typ="super { !
, host: string
 }"></ArgTableRow>
<ArgTableRow arg="dst-port" typ="super { !
, ports: multi { ports: range [ .. 65535]
 }
 }"></ArgTableRow>
<ArgTableRow arg="path" typ="super { !
, path: string
 }"></ArgTableRow>
<ArgTableRow arg="action" typ="enum (allow | deny)"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="dst-address" typ="super { !
, range: ipRange
 }"></ArgTableRow>
<ArgTableRow arg="hits" typ="num"></ArgTableRow>
</ArgTable>
