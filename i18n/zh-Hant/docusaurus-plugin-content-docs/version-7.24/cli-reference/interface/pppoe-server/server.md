---
sidebar_key: "cli-reference/interface/pppoe-server/server"
sidebar_position: 2
title: "server"
sidebar_label: "server"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/pppoe-server/server
captured_at: '2026-11-01T21:27:34+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/pppoe-server/server {#interfacepppoe-serverserver}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">無效</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="service-name" typ="string"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum { <l2tp>:0xfffffffe }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="max-mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="max-mru" typ="num"></ArgTableRow>
<ArgTableRow arg="mrru" typ="num"></ArgTableRow>
<ArgTableRow arg="authentication" typ="ubit (pap, chap, mschap1, mschap2)"></ArgTableRow>
<ArgTableRow arg="keepalive-timeout" typ="enum (disabled) { disabled:0 }"></ArgTableRow>
<ArgTableRow arg="one-session-per-host" typ="bool"></ArgTableRow>
<ArgTableRow arg="max-sessions" typ="num"></ArgTableRow>
<ArgTableRow arg="pado-delay" typ="num"></ArgTableRow>
<ArgTableRow arg="default-profile" typ="enum"></ArgTableRow>
<ArgTableRow arg="accept-empty-service" typ="bool">如果沒有匹配的 pppoe 服務可用，則接受服務名稱為空的 PADI</ArgTableRow>
<ArgTableRow arg="pppoe-over-vlan-range" typ="multi { vlan-range: range [1 .. 4094]
 }"></ArgTableRow>
<ArgTableRow arg="accept-untagged" typ="bool"></ArgTableRow>
</ArgTable>
