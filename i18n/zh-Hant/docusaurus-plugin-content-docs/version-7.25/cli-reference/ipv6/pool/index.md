---
sidebar_key: "cli-reference/ipv6/pool/index"
sidebar_position: 1
title: "pool"
sidebar_label: 'pool'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ipv6/pool
captured_at: '2026-11-01T21:24:43+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ipv6/pool {#ipv6pool}
**型別：** 目錄

IP 池用於定義可供各種 RouterOS 工具（例如 DHCP 伺服器、Point-to-Point 伺服器等）使用的 IPv6 字首。在可能的情況下，會向每個用戶端（OWNER/INFO 對）分配相同的 IPv6 字首。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未啟用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1">池的名稱。</ArgTableRow>
<ArgTableRow arg="prefix" typ="ip6Prefix"></ArgTableRow>
<ArgTableRow arg="from-pool" typ="enum">另一個池的名稱，用於從中動態獲取字首。</ArgTableRow>
<ArgTableRow arg="prefix-length" typ="num" mandatory="1">該選項表示將分配給用戶端的字首大小。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="actual-prefix" typ="ip6Prefix"></ArgTableRow>
<ArgTableRow arg="valid-lifetime" typ="time"></ArgTableRow>
<ArgTableRow arg="preferred-lifetime" typ="time"></ArgTableRow>
</ArgTable>
