---
sidebar_key: "cli-reference/ip/proxy/direct/index"
sidebar_position: 1
title: "direct"
sidebar_label: "direct"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/proxy/direct
captured_at: '2026-11-01T21:28:54+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/proxy/direct {#ipproxydirect}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="src-address" typ="super { !
, range: alt { ip4: ipRange
, ip6: ip6Prefix
 }
 }"></ArgTableRow>
<ArgTableRow arg="dst-address" typ="super { !
, range: alt { ip4: ipRange
, ip6: ip6Prefix
 }
 }"></ArgTableRow>
<ArgTableRow arg="dst-port" typ="super { !
, ports: multi { ports: range [ .. 65535]
 }
 }"></ArgTableRow>
<ArgTableRow arg="local-port" typ="super { !
, port: num [0 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="dst-host" typ="super { !
, host: string
 }"></ArgTableRow>
<ArgTableRow arg="path" typ="super { !
, path: string
 }"></ArgTableRow>
<ArgTableRow arg="method" typ="super { !
, method: enum (GET | HEAD | POST | PUT | CONNECT | OPTIONS | DELETE | TRACE)
 }"></ArgTableRow>
<ArgTableRow arg="action" typ="enum (allow | deny)"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="hits" typ="num"></ArgTableRow>
</ArgTable>
