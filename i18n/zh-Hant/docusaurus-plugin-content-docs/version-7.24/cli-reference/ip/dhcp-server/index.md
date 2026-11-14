---
sidebar_key: "cli-reference/ip/dhcp-server/index"
sidebar_position: 3
title: "dhcp-server"
sidebar_label: "dhcp-server"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/dhcp-server
captured_at: '2026-11-01T21:28:26+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/dhcp-server {#ipdhcp-server}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">無效</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="relay" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="lease-time" typ="time"></ArgTableRow>
<ArgTableRow arg="address-pool" typ="enum (static-only)"></ArgTableRow>
<ArgTableRow arg="dynamic-lease-identifiers" typ="ubit (client-mac, client-id, opt-82)"></ArgTableRow>
<ArgTableRow arg="bootp-support" typ="enum (none | static | dynamic)"></ArgTableRow>
<ArgTableRow arg="bootp-lease-time" typ="alt { enum: enum (lease-time | forever) { lease-time:0, forever:0xffffffff }
, time: time
 }"></ArgTableRow>
<ArgTableRow arg="delay-threshold" typ="alt { enum: enum (none) { none:0 }
, time: time
 }"></ArgTableRow>
<ArgTableRow arg="server-address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="add-arp" typ="bool"></ArgTableRow>
<ArgTableRow arg="add-dns-entries" typ="bool"></ArgTableRow>
<ArgTableRow arg="add-dns-entries-suffix" typ="string">僅當 add-dns-entries=yes 時使用。若非空，則會將字尾追加到 DNS 條目，並在響應中新增 Option 15（Domain Name）。</ArgTableRow>
<ArgTableRow arg="authoritative" typ="enum (no | after-10sec-delay | after-2sec-delay | yes)"></ArgTableRow>
<ArgTableRow arg="always-broadcast" typ="bool"></ArgTableRow>
<ArgTableRow arg="use-radius" typ="enum (no | yes | accounting)"></ArgTableRow>
<ArgTableRow arg="client-mac-limit" typ="enum (unlimited) { unlimited:0xffffffff }">一個用戶端 MAC 可獲取的最大租約數</ArgTableRow>
<ArgTableRow arg="conflict-detection" typ="bool">在發放租約前使用 ARP 和 ICMP 檢測 IP 衝突</ArgTableRow>
<ArgTableRow arg="use-framed-as-classless" typ="bool"></ArgTableRow>
<ArgTableRow arg="use-reconfigure" typ="bool"></ArgTableRow>
<ArgTableRow arg="lease-script" typ="alt { script: string
 }"></ArgTableRow>
<ArgTableRow arg="insert-queue-before" typ="enum (first | bottom) { first:0, bottom:0xffffffff }"></ArgTableRow>
<ArgTableRow arg="parent-queue" typ="enum (none) { none:0 }"></ArgTableRow>
<ArgTableRow arg="dhcp-option-set" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="address-lists" typ="multi { array-id, address-list: string
 }"></ArgTableRow>
<ArgTableRow arg="allow-dual-stack-queue" typ="bool"></ArgTableRow>
<ArgTableRow arg="support-broadband-tr101" typ="bool">按照 RFC 4679 和 The Broadband Forum TR-101 中的描述，將額外的 Option 82 子選項傳遞給 RADIUS 伺服器</ArgTableRow>
</ArgTable>
