---
sidebar_key: "cli-reference/ip/service/index"
sidebar_position: 1
title: "service"
sidebar_label: "service"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/service
captured_at: '2026-11-01T21:28:56+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/service {#ipservice}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">無效</ArgTableRow>
<ArgTableRow arg="c" typ="connection">connection</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="address" typ="object { address: alt { address: ipPrefix
, address: ip6Prefix
 }
 }" deprecated="1"></ArgTableRow>
<ArgTableRow arg="available-from" typ="object { address: alt { address: ipPrefix
, address: ip6Prefix
 }
 }"></ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none) { none:0 }"></ArgTableRow>
<ArgTableRow arg="tls-version" typ="enum (any | only-1.2) { any:0, only-1.2:2 }"></ArgTableRow>
<ArgTableRow arg="vrf" typ="enum"></ArgTableRow>
<ArgTableRow arg="max-sessions" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="container" typ="enum () { :0 }"></ArgTableRow>
<ArgTableRow arg="netns" typ="num"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="proto" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="local" typ="ip6Addr"></ArgTableRow>
<ArgTableRow arg="remote" typ="composite { ip: ip6Addr
, port: num
 }"></ArgTableRow>
</ArgTable>
