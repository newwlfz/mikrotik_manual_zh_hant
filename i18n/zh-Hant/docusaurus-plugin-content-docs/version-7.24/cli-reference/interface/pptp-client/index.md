---
sidebar_key: "cli-reference/interface/pptp-client/index"
sidebar_position: 1
title: "pptp-client"
sidebar_label: "pptp-client"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/pptp-client
captured_at: '2026-11-01T21:27:38+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/pptp-client {#interfacepptp-client}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="max-mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="max-mru" typ="num"></ArgTableRow>
<ArgTableRow arg="mrru" typ="num"></ArgTableRow>
<ArgTableRow arg="connect-to" typ="alt { address: ipAddr
, name: string
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="user" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="profile" typ="enum"></ArgTableRow>
<ArgTableRow arg="keepalive-timeout" typ="enum (disabled) { disabled:0 }"></ArgTableRow>
<ArgTableRow arg="use-peer-dns" typ="enum (no | yes | exclusively) { no:0, yes:1, exclusively:2 }"></ArgTableRow>
<ArgTableRow arg="add-default-route" typ="bool"></ArgTableRow>
<ArgTableRow arg="default-route-distance" typ="num"></ArgTableRow>
<ArgTableRow arg="dial-on-demand" typ="bool"></ArgTableRow>
<ArgTableRow arg="allow" typ="ubit (pap, chap, mschap1, mschap2)"></ArgTableRow>
</ArgTable>
