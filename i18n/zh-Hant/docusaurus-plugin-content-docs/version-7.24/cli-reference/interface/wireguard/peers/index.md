---
sidebar_key: "cli-reference/interface/wireguard/peers/index"
sidebar_position: 1
title: "peers"
sidebar_label: "peers"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/wireguard/peers
captured_at: '2026-11-01T21:27:55+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/wireguard/peers {#interfacewireguardpeers}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="public-key" typ="string"></ArgTableRow>
<ArgTableRow arg="private-key" typ="alt { private-key: enum (none | auto) { none:0, auto:1 }
, private-key: string
 }"></ArgTableRow>
<ArgTableRow arg="endpoint-address" typ="address (flags=46D)"></ArgTableRow>
<ArgTableRow arg="endpoint-port" typ="num"></ArgTableRow>
<ArgTableRow arg="allowed-address" typ="multi { allowed-address: address (flags=46/)
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="preshared-key" typ="alt { preshared-key: enum (none | auto) { none:0, auto:1 }
, preshared-key: string
 }"></ArgTableRow>
<ArgTableRow arg="persistent-keepalive" typ="time"></ArgTableRow>
<ArgTableRow arg="client-address" typ="multi { client-address: address (flags=46/)
 }"></ArgTableRow>
<ArgTableRow arg="client-dns" typ="multi { client-dns: address (flags=46D)
 }"></ArgTableRow>
<ArgTableRow arg="client-endpoint" typ="address (flags=46D)"></ArgTableRow>
<ArgTableRow arg="client-keepalive" typ="time"></ArgTableRow>
<ArgTableRow arg="client-listen-port" typ="num"></ArgTableRow>
<ArgTableRow arg="client-allowed-address" typ="multi { client-allowed-address: address (flags=46/)
 }"></ArgTableRow>
<ArgTableRow arg="responder" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="current-endpoint-address" typ="address (flags=46)"></ArgTableRow>
<ArgTableRow arg="current-endpoint-port" typ="num"></ArgTableRow>
<ArgTableRow arg="rx" typ="num"></ArgTableRow>
<ArgTableRow arg="tx" typ="num"></ArgTableRow>
<ArgTableRow arg="last-handshake" typ="time"></ArgTableRow>
</ArgTable>
