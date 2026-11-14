---
sidebar_key: "cli-reference/zerotier/controller/index"
sidebar_position: 1
title: "controller"
sidebar_label: "controller"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/zerotier/controller
captured_at: '2026-11-01T21:30:38+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## zerotier/controller {#zerotiercontroller}
**包：** zerotier
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="disabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="instance" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="network" typ="string"></ArgTableRow>
<ArgTableRow arg="private" typ="bool"></ArgTableRow>
<ArgTableRow arg="broadcast" typ="bool"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="multicast-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="ip-range" typ="super { first: address (flags=4)
, [last] [ -address (flags=4)]
 }"></ArgTableRow>
<ArgTableRow arg="ip6-range" typ="super { first: address (flags=6)
, [last] [ -address (flags=6)]
 }"></ArgTableRow>
<ArgTableRow arg="ip6-rfc4193" typ="bool"></ArgTableRow>
<ArgTableRow arg="ip6-6plane" typ="bool"></ArgTableRow>
<ArgTableRow arg="routes" typ="object { route: super { dst: address (flags=46/)
, [gw] [ @address (flags=46)]
 }
 }"></ArgTableRow>
</ArgTable>
