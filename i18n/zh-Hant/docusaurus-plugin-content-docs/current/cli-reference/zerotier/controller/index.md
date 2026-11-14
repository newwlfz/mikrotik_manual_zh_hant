---
sidebar_key: "cli-reference/zerotier/controller"
title: "controller"
sidebar_label: 'controller'
source: https://manual.mikrotik.com/docs/cli-reference/zerotier/controller
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## zerotier/controller {#zerotiercontroller}
**包：** zerotier
**型別：** 目錄

Zerotier 配置控制器。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">專案是否被停用。</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">控制器是否處於非活動狀態。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="disabled" typ="bool">專案是否被停用。</ArgTableRow>
<ArgTableRow arg="instance" typ="enum" mandatory="1">ZeroTier 例項名稱。</ArgTableRow>
<ArgTableRow arg="name" typ="string" mandatory="1">此控制器的短名稱。</ArgTableRow>
<ArgTableRow arg="network" typ="string">16 位網路 ID。</ArgTableRow>
<ArgTableRow arg="private" typ="bool">啟用訪問控制。</ArgTableRow>
<ArgTableRow arg="broadcast" typ="bool">允許接收廣播 (FF:FF:FF:FF:FF:FF) 封包。</ArgTableRow>
<ArgTableRow arg="mtu" typ="num">網路 MTU。</ArgTableRow>
<ArgTableRow arg="multicast-limit" typ="num">多播封包的最大接收者數量。</ArgTableRow>
<ArgTableRow arg="ip-range" typ="super { first: address (flags=4)
, [last] [ -address (flags=4)]
 }">IP 範圍，例如 172.16.16.1-172.16.16.254。</ArgTableRow>
<ArgTableRow arg="ip6-range" typ="super { first: address (flags=6)
, [last] [ -address (flags=6)]
 }">IPv6 範圍，例如 `fd00:feed:feed:beef::-fd00:feed:feed:beef:ffff:ffff:ffff:ffff`。</ArgTableRow>
<ArgTableRow arg="ip6-rfc4193" typ="bool">rfc4193 模式為每個成員在 /88 網路上提供一個 /128。</ArgTableRow>
<ArgTableRow arg="ip6-6plane" typ="bool">在 /40 網路內為每個成員提供一個 /80，並使用 NDP 模擬將該 /80 下的所有 IP 路由到其所有者。</ArgTableRow>
<ArgTableRow arg="routes" typ="object { route: super { dst: address (flags=46/)
, [gw] [ @address (flags=46)]
 }
 }">按以下格式推送路由：`Routes ::= Route[,Routes] Route ::= Dst[@Gw]`。</ArgTableRow>
</ArgTable>
