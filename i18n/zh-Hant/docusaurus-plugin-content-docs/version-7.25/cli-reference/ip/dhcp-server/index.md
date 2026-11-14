---
sidebar_key: "cli-reference/ip/dhcp-server/index"
sidebar_position: 3
title: "dhcp-server"
sidebar_label: 'dhcp-server'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/dhcp-server
captured_at: '2026-11-01T21:23:51+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/dhcp-server {#ipdhcp-server}
**型別：** 目錄

DHCP 伺服器為用戶端分配 IPv4 地址和網路設定。它從 IP 池中租出地址，傳送 `/ip/dhcp-server/network` 中匹配條目的設定，還可以分發靜態租約（`/ip/dhcp-server/lease`）。有關概述和配置示例，請參閱 [DHCP 伺服器](../../../network-management/dhcp/server.md)。有關 DHCP 的工作原理，請參閱 [DHCP](../../../network-management/dhcp/index.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="D" typ="dynamic">DHCP 伺服器是動態建立的。</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">DHCP 伺服器已停用。</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">DHCP 伺服器配置無效，例如其介面沒有 IP 地址。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">DHCP 伺服器的名稱。</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">DHCP 伺服器監聽的介面。該介面必須有 IP 地址，否則伺服器無效。一個介面上只能執行一個用於直連用戶端的伺服器；同一介面上的多個伺服器必須各自具有不同的 `relay` 地址。</ArgTableRow>
<ArgTableRow arg="relay" typ="ipAddr">
伺服器根據請求的閘道器地址（`giaddr`）決定應答哪些請求：
- `0.0.0.0`（預設）- 僅應答來自直連用戶端的請求，不應答中繼請求。
- `255.255.255.255` - 應答來自任何 DHCP 中繼的請求，但另一個伺服器已設定該中繼地址並應答的請求除外。
- IP 地址 - 僅應答由具有該地址的 DHCP 中繼轉發的請求，該地址是中繼的 `local-address`。
</ArgTableRow>
<ArgTableRow arg="lease-time" typ="time">租約的持續時間。用戶端在過半後續租，在達到 87.5% 後開始重新繫結。沒有自己的 `lease-time` 的靜態租約也使用此值。預設：30m。</ArgTableRow>
<ArgTableRow arg="address-pool" typ="enum (static-only)">用於分配動態地址的 IP 池。使用 `static-only` 時，伺服器僅應答擁有靜態租約的用戶端。預設：static-only。</ArgTableRow>
<ArgTableRow arg="dynamic-lease-identifiers" typ="ubit (client-mac, client-id, opt-82)">伺服器用於識別動態租約用戶端的識別符號：`client-mac`（硬體地址）、`client-id`（選項 61）和 `opt-82`（中繼代理資訊）。更改所選識別符號的用戶端會獲得新租約。預設：client-mac,client-id。</ArgTableRow>
<ArgTableRow arg="bootp-support" typ="enum (none | static | dynamic)">
伺服器如何應答 BOOTP 用戶端：
- `none` - 不應答 BOOTP 請求。
- `static`（預設）- 僅向 BOOTP 用戶端提供靜態租約。
- `dynamic` - 向 BOOTP 用戶端提供靜態和動態租約。
</ArgTableRow>
<ArgTableRow arg="bootp-lease-time" typ="alt { enum: enum (lease-time | forever) { lease-time:0, forever:0xffffffff }
, time: time
 }">BOOTP 用戶端的租約時間：`forever`（預設）表示永不過期的租約，`lease-time` 表示使用伺服器的 `lease-time`，或使用一個時間值。</ArgTableRow>
<ArgTableRow arg="delay-threshold" typ="alt { enum: enum (none) { none:0 }
, time: time
 }">請求必須具有的 seconds-elapsed 欄位（`secs`）最小值，達到該值才會被應答。用戶端將此欄位設定為自開始獲取或續租地址以來經過的時間，因此閾值使伺服器僅應答已嘗試該時長的用戶端，例如讓另一臺伺服器先應答。使用 `none` 時，所有請求都會被應答。預設：none。</ArgTableRow>
<ArgTableRow arg="server-address" typ="ipAddr">伺服器用作其標識的地址：回覆從此地址傳送，並將其作為伺服器識別符號（選項 54）攜帶。未設定時，使用伺服器介面的地址。當介面有多個地址時設定此項。</ArgTableRow>
<ArgTableRow arg="add-arp" typ="bool">是否為每個已繫結租約的地址新增永久 ARP 表項，並在 `/ip/arp` 中透過 `H` 標誌顯示。當介面自身不解析 ARP 時使用它，例如 ARP 模式為 `reply-only` 時。預設值：no.</ArgTableRow>
<ArgTableRow arg="add-dns-entries" typ="bool">是否為每個已繫結租約的地址新增動態 DNS 條目（`/ip/dns/static`，型別 A）。條目名是用戶端傳送的主機名（選項 12）後跟 `add-dns-entries-suffix`，其 TTL 為租約時間。路由器的 DNS 解析器會應答這些名稱。預設：no。</ArgTableRow>
<ArgTableRow arg="add-dns-entries-suffix" typ="string">在由 `add-dns-entries` 建立的 DNS 條目中追加到用戶端主機名的域，例如 `laptop.lan`。僅在 `add-dns-entries=yes` 時使用。當網路沒有 `domain` 時，伺服器還會將此後綴作為域名（選項 15）傳送。它不能為空。預設：lan。</ArgTableRow>
<ArgTableRow arg="authoritative" typ="enum (no | after-10sec-delay | after-2sec-delay | yes)">
伺服器如何應答對其無法提供的地址的請求，以便此類用戶端更早重新開始：
- `yes`（預設）- 使用 DHCPNAK 應答。
- `no` - 忽略針對此類地址的廣播請求，例如來自重新繫結用戶端的請求，以便另一臺伺服器可以應答它們。
- `after-2sec-delay`、`after-10sec-delay` - 對於廣播請求，在請求的 `secs` 欄位低於 2 或 10 秒時表現為 `no`，之後表現為 `yes`。要忽略低於閾值的所有請求，請使用 `delay-threshold`。

單播續租請求始終會被應答：當無法提供所請求的地址時，使用 DHCPNAK 應答；或者當該地址在地址池中空閒時，使用新租約應答。
</ArgTableRow>
<ArgTableRow arg="always-broadcast" typ="bool">即使用戶端未設定廣播標誌，是否也廣播回覆。使用 `no` 時，回覆遵循用戶端的廣播標誌。預設：no。</ArgTableRow>
<ArgTableRow arg="use-radius" typ="enum (no | yes | accounting)">
是否使用 RADIUS 伺服器（`/radius` 條目，`service=dhcp`）處理租約：
- `no`（預設）- 不使用 RADIUS。
- `yes` - 透過 RADIUS 授權租約併發送計費。伺服器在等待 RADIUS 回覆期間，租約具有 `authorizing` 狀態，用戶端不會獲得地址。
- `accounting` - 僅將 RADIUS 用於計費。
</ArgTableRow>
<ArgTableRow arg="client-mac-limit" typ="enum (unlimited) { unlimited:0xffffffff }">具有相同 MAC 地址的用戶端可以獲得的租約最大數量。預設：unlimited。</ArgTableRow>
<ArgTableRow arg="conflict-detection" typ="bool">是否在提供地址前使用 ARP 和 ICMP 檢查該地址。當另一臺主機應答時，伺服器記錄警告，將該地址保留為具有 `conflict` 狀態的租約直到租約時間結束，並提供另一個空閒地址。不檢查靜態租約的地址。預設：yes。</ArgTableRow>
<ArgTableRow arg="use-framed-as-classless" typ="bool">是否將從 RADIUS 收到的 Framed-Route 屬性作為無類靜態路由（選項 121）傳送給用戶端。當同時收到 Framed-Route 和 Classless-Static-Route 時，使用 Classless-Static-Route。預設：yes。</ArgTableRow>
<ArgTableRow arg="use-reconfigure" typ="bool">伺服器是否支援 Reconfigure（FORCERENEW）訊息。啟用後，伺服器會向請求該金鑰的用戶端提供重新配置金鑰，例如使用 `allow-reconfigure=yes` 的 RouterOS DHCP 用戶端，租約的 `send-reconfigure` 命令會使此類用戶端續租。重新配置訊息僅由該命令傳送，伺服器或網路設定更改時不會發送。未啟用此設定時，用戶端不會獲得金鑰，且 `send-reconfigure` 會被拒絕。預設：no。</ArgTableRow>
<ArgTableRow arg="lease-script" typ="alt { script: string
 }">
租約繫結、釋放或過期時要執行的指令碼。指令碼接收以下變數：
- `leaseBound` - 租約繫結時為 `1`，釋放或過期時為 `0`。
- `leaseServerName` - DHCP 伺服器名稱。
- `leaseActMAC` - 用戶端的 MAC 地址。
- `leaseActIP` - 租約的 IP 地址。
- `lease-hostname` - 用戶端傳送的主機名。
- `lease-options` - 傳送給用戶端的選項陣列，按選項程式碼索引。
- `lease-agent-circuit-id`、`lease-agent-remote-id` - 來自中繼代理資訊選項（選項 82）的 Circuit ID 和 Remote ID，當請求經過會新增該選項的中繼時。
</ArgTableRow>
<ArgTableRow arg="insert-queue-before" typ="enum (first | bottom) { first:0, bottom:0xffffffff }">為具有 `rate-limit` 的租約建立的動態簡單佇列的放置位置：`first`（預設）放在 `/queue/simple` 的頂部，`bottom` 放在末尾，或放在指定佇列之前。</ArgTableRow>
<ArgTableRow arg="parent-queue" typ="enum (none) { none:0 }">為具有 `rate-limit` 的租約建立的動態簡單佇列的父佇列。預設：none。</ArgTableRow>
<ArgTableRow arg="dhcp-option-set" typ="enum (none)">要傳送給此伺服器用戶端的選項集（`/ip/dhcp-server/option/sets`）。租約的選項優先於伺服器的選項，伺服器的選項優先於網路的選項。預設：none。</ArgTableRow>
<ArgTableRow arg="address-lists" typ="multi { array-id, address-list: string
 }">防火牆地址列表，每個已繫結租約的地址會作為動態條目新增到這些列表中。租約結束時條目會被移除。</ArgTableRow>
<ArgTableRow arg="allow-dual-stack-queue" typ="bool">同一用戶端的租約和 DHCPv6 繫結是否共享一個動態簡單佇列，該佇列隨後同時包含 IPv4 和 IPv6 地址。用戶端透過其 MAC 地址和 DUID 識別。DHCPv6 伺服器也必須啟用此設定。預設：yes。</ArgTableRow>
<ArgTableRow arg="support-broadband-tr101" typ="bool">按照 RFC 4679 和 The Broadband Forum TR-101 所述，向 RADIUS 伺服器傳遞額外的 Option 82 子選項。</ArgTableRow>
<ArgTableRow arg="ipv6-only-preferred" typ="bool">是否向請求該選項的用戶端傳送 IPv6-Only Preferred 選項（選項 108，RFC 8925）。請求該選項的用戶端隨後不會獲得 IPv4 地址：offer 中包含該選項但不包含地址，因此支援該選項的用戶端僅使用 IPv6。該選項攜帶 0 秒的等待時間，RFC 8925 用戶端會在再次嘗試 IPv4 之前將其提高到至少 300 秒。預設：no。</ArgTableRow>
</ArgTable>
