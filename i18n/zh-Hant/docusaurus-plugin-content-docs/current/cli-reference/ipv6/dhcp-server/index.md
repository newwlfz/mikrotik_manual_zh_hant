---
sidebar_key: "cli-reference/ipv6/dhcp-server"
title: "dhcp-server"
sidebar_label: 'dhcp-server'
source: https://manual.mikrotik.com/docs/cli-reference/ipv6/dhcp-server
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ipv6/dhcp-server {#ipv6dhcp-server}
**型別：** 目錄

DHCPv6 伺服器向用戶端委派 IPv6 字首（DHCPv6-PD）並分配 IPv6 地址。字首和地址來自 IPv6 地址池或靜態繫結（`/ipv6/dhcp-server/binding`）。有關概述和配置示例，請參閱 [DHCPv6 伺服器](../../../network-management/dhcp/dhcpv6-server.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="D" typ="dynamic">DHCPv6 伺服器是動態建立的。</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">DHCPv6 伺服器已停用。</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">DHCPv6 伺服器配置無效。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1">DHCPv6 伺服器的名稱。</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">DHCPv6 伺服器監聽的介面。</ArgTableRow>
<ArgTableRow arg="prefix-pool" typ="alt { prefix-pool-static: enum (static-only) { static-only:0xffffffff }
, prefix-pool-name: enum
 }">動態字首繫結從中獲取字首的 IPv6 地址池。使用 `static-only` 時，只下發靜態繫結。預設值：static-only。</ArgTableRow>
<ArgTableRow arg="address-pool" typ="alt { address-pool-static: enum (static-only) { static-only:0xffffffff }
, address-pool-name: enum
 }">動態地址繫結從中獲取地址的 IPv6 地址池。地址池字首長度必須為 128。使用 `static-only` 時，只下發靜態繫結。預設值：static-only。</ArgTableRow>
<ArgTableRow arg="lease-time" typ="time">新建和續租繫結的生存期。系統會告知用戶端在生存期過半後執行 renew，在達到 80% 後執行 rebind，首選生存期為其 90%。預設值：3d。</ArgTableRow>
<ArgTableRow arg="rapid-commit" typ="bool">是否對請求 Rapid Commit 的 Solicit 直接以 Reply 應答（兩訊息交換）。使用 `no` 時，伺服器始終先以 Advertise 應答。預設值：yes。</ArgTableRow>
<ArgTableRow arg="use-radius" typ="enum (no | yes | accounting)">是否對繫結使用 RADIUS 伺服器：`no`（預設）、`yes` 表示用於認證和計費，或 `accounting` 表示僅用於計費。</ArgTableRow>
<ArgTableRow arg="preference" typ="num">在 Advertise 訊息中傳送的 Preference 值。用戶端優先選擇該值最高的伺服器。預設值：255。</ArgTableRow>
<ArgTableRow arg="binding-script" typ="alt { script: string
 }">
在繫結被建立時和結束時執行的指令碼。它會為每個繫結單獨執行，並接收這些變數：
- `bindingBound` - 繫結已建立時為 `1`，否則為 `0`。
- `bindingServerName` - DHCPv6 伺服器的名稱。
- `bindingDUID` - 用戶端的 DUID。
- `bindingAddress` - 用戶端傳送時所使用的 IPv6 地址，通常是其鏈路本地地址。
- `bindingPrefix` - 委派的字首，或地址繫結所分配的地址。
</ArgTableRow>
<ArgTableRow arg="dns-none" typ="bool">不要將 DNS 伺服器新增到響應中</ArgTableRow>
<ArgTableRow arg="dhcp-option" typ="multi { array-id, option: alt { option: enum
, option-set: enum
 }
 }">要傳送給用戶端的選項（`/ipv6/dhcp-server/option`），例如 DNS 伺服器（選項 23）。</ArgTableRow>
<ArgTableRow arg="insert-queue-before" typ="enum (first | bottom) { first:0, bottom:0xffffffff }">對於帶 `rate-limit` 的繫結所建立的動態簡單佇列，將其放置在何處：`first`（預設）位於 `/queue/simple` 頂部，`bottom` 位於末尾，或位於指定佇列之前。</ArgTableRow>
<ArgTableRow arg="parent-queue" typ="enum (none) { none:0 }">對於帶 `rate-limit` 的繫結所建立的動態簡單佇列的父級。預設值：none。</ArgTableRow>
<ArgTableRow arg="route-distance" typ="num">伺服器為每個委派字首和已分配地址新增的路由的距離，這些路由經由用戶端的鏈路本地地址。預設值：1。</ArgTableRow>
<ArgTableRow arg="allow-dual-stack-queue" typ="bool">同一用戶端的繫結和 DHCP 租約是否共用一個動態簡單佇列，該佇列隨後同時包含 IPv6 和 IPv4 地址。用戶端透過其 MAC 地址和 DUID 識別。DHCP 伺服器也必須啟用此設定。預設值：yes。</ArgTableRow>
<ArgTableRow arg="use-reconfigure" typ="bool">是否傳送 Reconfigure 訊息。啟用後，接受這些訊息的用戶端會獲得一個 reconfigure key，伺服器會自行傳送 Reconfigure 訊息：當 `address-pool`、`lease-time` 或 `dhcp-option` 變化時傳送給其所有繫結，當繫結的設定變化時傳送給該繫結，以便用戶端續租；當伺服器或該繫結的伺服器被移除時，傳送 rebind 請求。繫結上的 `send-reconfigure` 命令會手動傳送一條。預設值：no。</ArgTableRow>
<ArgTableRow arg="address-lists" typ="multi { array-id, address-list: string
 }">每個繫結的字首或地址會被新增到的 IPv6 防火牆地址列表。繫結上的 `address-lists` 設定會覆蓋此項。</ArgTableRow>
<ArgTableRow arg="add-dns-entries" typ="bool">是否為每個地址繫結新增動態 DNS 條目（型別 AAAA）。條目名稱為用戶端傳送的 FQDN（選項 39）後跟 `add-dns-entries-suffix`，其 TTL 為租約時間。字首繫結不會獲得條目。預設值：no。</ArgTableRow>
<ArgTableRow arg="add-dns-entries-suffix" typ="string">在由 `add-dns-entries` 建立的 DNS 條目中追加到用戶端名稱後的域名，例如 `laptop.lan`。預設值：lan。</ArgTableRow>
<ArgTableRow arg="ignore-ia-na-bindings" typ="bool">是否忽略地址請求（IA_NA），並表現得如同用戶端訊息中不包含這些請求，從而只下發字首。若不啟用此項，沒有地址池的伺服器即使沒有可用地址，仍會應答每個地址請求，這可能會讓同時請求地址和字首的用戶端不斷重試。預設值：no。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="duid" typ="string">伺服器的 DUID。路由器為其 DHCPv6 用戶端使用相同的 DUID。</ArgTableRow>
</ArgTable>
