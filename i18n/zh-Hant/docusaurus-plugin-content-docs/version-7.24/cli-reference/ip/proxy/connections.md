---
sidebar_key: "cli-reference/ip/proxy/connections"
sidebar_position: 5
title: "connections"
sidebar_label: "connections"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/proxy/connections
captured_at: '2026-11-01T21:28:54+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/proxy/connections {#ipproxyconnections}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="S" typ="server">server</ArgTableRow>
<ArgTableRow arg="C" typ="client">client</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="src-address" typ="alt { ip4: ipAddr
, ip6: ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="dst-address" typ="alt { ip4: ipAddr
, ip6: ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="last-protocol" typ="enum (HTTP/1.0 | HTTP/1.1 | FTP) { HTTP/1.0:1, HTTP/1.1:2, FTP:3 }"></ArgTableRow>
<ArgTableRow arg="state" typ="enum (rx-header | resolving | connecting | waiting | rx-body | tx-header | tx-body | idle) { rx-header:0, resolving:1, connecting:2, waiting:3, rx-body:4, tx-header:5, tx-body:6, idle:7 }"></ArgTableRow>
<ArgTableRow arg="tx-bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-bytes" typ="num"></ArgTableRow>
</ArgTable>
