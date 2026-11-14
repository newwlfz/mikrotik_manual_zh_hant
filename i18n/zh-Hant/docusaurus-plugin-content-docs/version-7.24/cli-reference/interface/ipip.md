---
sidebar_key: "cli-reference/interface/ipip"
sidebar_position: 12
title: "ipip"
sidebar_label: "ipip"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/ipip
captured_at: '2026-11-01T21:27:22+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ipip {#interfaceipip}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="local-address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="remote-address" typ="address (flags=4Dv)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="keepalive" typ="super { keepalive-interval: time [1 .. ]
, [keepalive-retries] [ ,num [1 .. ]]
 }"></ArgTableRow>
<ArgTableRow arg="dscp" typ="num"></ArgTableRow>
<ArgTableRow arg="clamp-tcp-mss" typ="bool"></ArgTableRow>
<ArgTableRow arg="dont-fragment" typ="bool"></ArgTableRow>
<ArgTableRow arg="ipsec-secret" typ="string" syscap="security"></ArgTableRow>
<ArgTableRow arg="allow-fast-path" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="actual-mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="current-remote-address" typ="ipAddr"></ArgTableRow>
</ArgTable>
