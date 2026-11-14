---
sidebar_key: "cli-reference/ipv6/dhcp-server/binding"
title: "binding"
sidebar_label: 'binding'
source: https://manual.mikrotik.com/docs/cli-reference/ipv6/dhcp-server/binding
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ipv6/dhcp-server/binding {#ipv6dhcp-serverbinding}
**型別：** 目錄

DHCPv6 伺服器的繫結：分配給用戶端的字首和地址。動態繫結由伺服器的池建立；靜態繫結為用戶端（透過其 DUID 和 IAID 標識）提供固定的字首或地址。詳情請參閱 [DHCPv6 伺服器](../../../../network-management/dhcp/dhcpv6-server.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="I" typ="invalid">該繫結無效。</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">該繫結已停用。</ArgTableRow>
<ArgTableRow arg="R" typ="radius">該繫結由 RADIUS 伺服器分配。</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">該繫結是動態的。使用 `make-static` 將其轉換為靜態繫結。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="address" typ="alt { prefix: ip6Prefix
 }">分配給用戶端的字首或地址。</ArgTableRow>
<ArgTableRow arg="duid" typ="string" mandatory="1">用戶端的 DUID，以十六進位制表示，例如 `0x00030001dc2c6ee7106a`。它與 `iaid` 一起標識該繫結所響應的用戶端請求。</ArgTableRow>
<ArgTableRow arg="iaid" typ="num" mandatory="1">用戶端請求的身份關聯識別符號 (IAID)。它與 `duid` 一起標識該繫結。</ArgTableRow>
<ArgTableRow arg="ia-type" typ="enum (na | pd)">
繫結型別：
- `na` - 地址繫結 (IA_NA)。
- `pd` - 字首委派繫結 (IA_PD)。
</ArgTableRow>
<ArgTableRow arg="server" typ="enum (all)">可提供此繫結的 DHCPv6 伺服器名稱，或使用 `all` 表示所有伺服器。</ArgTableRow>
<ArgTableRow arg="life-time" typ="time">靜態繫結的生存時間。動態繫結使用伺服器的 `lease-time`。預設值：1w。</ArgTableRow>
<ArgTableRow arg="prefix-pool" typ="enum">繫結的字首或地址來自的 IPv6 池。對於地址，池字首長度為 128。</ArgTableRow>
<ArgTableRow arg="dhcp-option" typ="multi { array-id, option: alt { option: enum
, option-set: enum
 }
 }">要傳送給此用戶端的選項（`/ipv6/dhcp-server/option`）。</ArgTableRow>
<ArgTableRow arg="rate-limit" typ="string">用戶端的頻寬限制，格式與 DHCP 伺服器租約的 `rate-limit` 相同。伺服器會為繫結的字首或地址建立動態簡單佇列。</ArgTableRow>
<ArgTableRow arg="allow-dual-stack-queue" typ="bool">此繫結與同一用戶端的 DHCP 租約是否共享一個動態簡單佇列。預設值：yes。</ArgTableRow>
<ArgTableRow arg="address-lists" typ="multi { array-id, address-list: string
 }">要將繫結的字首或地址加入的 IPv6 防火牆地址列表。覆蓋伺服器的 `address-lists` 設定。</ArgTableRow>
<ArgTableRow arg="insert-queue-before" typ="enum (first | bottom) { first:0, bottom:0xffffffff }">為此繫結建立的動態簡單佇列的放置位置：`first`（預設）、`bottom`，或指定名稱的佇列之前。</ArgTableRow>
<ArgTableRow arg="parent-queue" typ="enum (none) { none:0 }">為此繫結建立的動態簡單佇列的父級。預設值：none。</ArgTableRow>
<ArgTableRow arg="queue-type" typ="enum">為此繫結建立的動態簡單佇列的佇列型別。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="active-server" typ="enum (none)">服務該繫結的 DHCPv6 伺服器。</ArgTableRow>
<ArgTableRow arg="status" typ="enum (waiting | offered | bound)">
繫結狀態：
- `waiting` - 未使用的靜態繫結，或之前使用過的動態繫結。伺服器會保留動態繫結 10 分鐘，以便舊用戶端可以重新獲得它；之後該字首可以分配給其他用戶端。
- `offered` - 伺服器已用 Advertise 響應 Solicit，但尚未收到 Request。用戶端有 2 分鐘時間來請求該繫結。
- `bound` - 用戶端正在使用該繫結。
</ArgTableRow>
<ArgTableRow arg="expires-after" typ="time">距離繫結過期的時間。</ArgTableRow>
<ArgTableRow arg="last-seen" typ="alt { symbolic-names: enum (never | sometime) { never:0xffffffff, sometime:0xfffffffe }
, time: time
 }">自伺服器上次收到用戶端訊息以來經過的時間，或 `never`。</ArgTableRow>
<ArgTableRow arg="client-address" typ="ip6Addr">用戶端傳送訊息所用的 IPv6 地址，通常是其鏈路本地地址。到該繫結的路由將其用作閘道器。</ArgTableRow>
<ArgTableRow arg="reconfigure-key" typ="string">伺服器提供給用戶端用於驗證 Reconfigure 訊息的金鑰（`use-reconfigure`）。</ArgTableRow>
<ArgTableRow arg="reconfigure-last-sent" typ="string">傳送給用戶端的最後一條 Reconfigure 訊息的重放檢測計數器。每傳送一條 Reconfigure 訊息，它都會增加。</ArgTableRow>
<ArgTableRow arg="reconfigure-status" typ="string"></ArgTableRow>
<ArgTableRow arg="fqdn" typ="string">用戶端傳送的 FQDN（選項 39）。</ArgTableRow>
</ArgTable>
