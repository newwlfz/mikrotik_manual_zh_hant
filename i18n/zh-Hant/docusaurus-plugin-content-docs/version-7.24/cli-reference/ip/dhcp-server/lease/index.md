---
sidebar_key: "cli-reference/ip/dhcp-server/lease/index"
sidebar_position: 2
title: "lease"
sidebar_label: "lease"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/dhcp-server/lease
captured_at: '2026-11-01T21:28:27+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/dhcp-server/lease {#ipdhcp-serverlease}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="R" typ="radius">radius</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
<ArgTableRow arg="B" typ="blocked">blocked</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="address" typ="alt { ip-address: ipAddr
, pool: enum
 }"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="use-src-mac" typ="bool"></ArgTableRow>
<ArgTableRow arg="client-id" typ="string"></ArgTableRow>
<ArgTableRow arg="rate-limit" typ="string"></ArgTableRow>
<ArgTableRow arg="routes" typ="object { route: composite { dst-address: address (flags=4/)
, gateway: [ composite { gateway: address (flags=46ivL)
, distance: [ num [1 .. 255]]
 }]
 }
 }">用戶端連線時伺服器上顯示的路由</ArgTableRow>
<ArgTableRow arg="insert-queue-before" typ="enum (bottom | first) { bottom:0xffffffff, first:0 }"></ArgTableRow>
<ArgTableRow arg="parent-queue" typ="enum (none) { none:0 }"></ArgTableRow>
<ArgTableRow arg="queue-type" typ="enum"></ArgTableRow>
<ArgTableRow arg="address-lists" typ="multi { array-id, address-list: string
 }"></ArgTableRow>
<ArgTableRow arg="server" typ="enum (all) { all:0 }"></ArgTableRow>
<ArgTableRow arg="block-access" typ="bool"></ArgTableRow>
<ArgTableRow arg="allow-dual-stack-queue" typ="bool"></ArgTableRow>
<ArgTableRow arg="lease-time" typ="time"></ArgTableRow>
<ArgTableRow arg="always-broadcast" typ="bool"></ArgTableRow>
<ArgTableRow arg="dhcp-option" typ="multi { array-id, option: enum
 }"></ArgTableRow>
<ArgTableRow arg="dhcp-option-set" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="agent-circuit-id" typ="string">如果非空，則即使 MAC 或 client-id 不同，也用它透過 Option 82 匹配租約</ArgTableRow>
<ArgTableRow arg="agent-remote-id" typ="string">如果非空，則即使 MAC 或 client-id 不同，也用它透過 Option 82 匹配租約</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="status" typ="enum (waiting | testing | declined | offered | bound | authorizing | conflict) { waiting:0, testing:1, declined:2, offered:3, bound:4, authorizing:5 }"></ArgTableRow>
<ArgTableRow arg="expires-after" typ="time"></ArgTableRow>
<ArgTableRow arg="last-seen" typ="alt { symbolic-names: enum (never | sometime) { never:0xffffffff, sometime:0xfffffffe }
, time: time
 }"></ArgTableRow>
<ArgTableRow arg="age" typ="time"></ArgTableRow>
<ArgTableRow arg="active-address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="active-mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="active-client-id" typ="string"></ArgTableRow>
<ArgTableRow arg="active-server" typ="enum"></ArgTableRow>
<ArgTableRow arg="active-agent-circuit-id" typ="string"></ArgTableRow>
<ArgTableRow arg="active-agent-remote-id" typ="string"></ArgTableRow>
<ArgTableRow arg="host-name" typ="string"></ArgTableRow>
<ArgTableRow arg="class-id" typ="string">來自上次收到的 DHCP 請求的 DHCP option 60</ArgTableRow>
<ArgTableRow arg="src-mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="reconfigure-key" typ="string"></ArgTableRow>
<ArgTableRow arg="reconfigure-last-sent" typ="string"></ArgTableRow>
<ArgTableRow arg="reconfigure-status" typ="string"></ArgTableRow>
</ArgTable>
