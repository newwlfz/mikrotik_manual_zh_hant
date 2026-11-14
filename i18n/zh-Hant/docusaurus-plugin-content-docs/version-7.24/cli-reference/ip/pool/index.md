---
sidebar_key: "cli-reference/ip/pool/index"
sidebar_position: 1
title: "pool"
sidebar_label: "pool"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/pool
captured_at: '2026-11-01T21:28:51+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/pool {#ippool}
**型別：** 目錄

IP 池用於定義可供各種 RouterOS 工具使用的 IP 地址範圍，例如 DHCP 伺服器、Point-to-Point 伺服器等。提供獨立的 IPv4 和 IPv6 列表。只要有可能，就會向每個用戶端（OWNER/INFO 對）分配相同的 IP 地址。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">池的名稱。</ArgTableRow>
<ArgTableRow arg="ranges" typ="multi { range: ipRange
 }" mandatory="1">由不重疊 IP 地址範圍組成的 IP 地址列表，格式為：`from1-to1,from2-to2,...,fromN-toN`。例如，`10.0.0.1-10.0.0.27,10.0.0.32-10.0.0.47`。</ArgTableRow>
<ArgTableRow arg="next-pool" typ="enum (none) { none:0 }">當從一個沒有空閒地址的池中執行 IP 地址獲取，並且已設定 next-pool 屬性時，將從下一個池獲取 IP 地址。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="total" typ="num"></ArgTableRow>
<ArgTableRow arg="used" typ="num"></ArgTableRow>
<ArgTableRow arg="available" typ="num"></ArgTableRow>
</ArgTable>
