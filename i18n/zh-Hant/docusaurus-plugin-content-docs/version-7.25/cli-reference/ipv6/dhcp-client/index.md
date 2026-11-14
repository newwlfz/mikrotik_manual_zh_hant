---
sidebar_key: "cli-reference/ipv6/dhcp-client/index"
sidebar_position: 1
title: "dhcp-client"
sidebar_label: 'dhcp-client'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ipv6/dhcp-client
captured_at: '2026-11-01T21:24:30+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ipv6/dhcp-client {#ipv6dhcp-client}
**型別：** 目錄

DHCPv6 用戶端會向 DHCPv6 伺服器請求 IPv6 地址、委派字首（DHCPv6-PD）或其他設定。有關概述和配置示例，請參閱 [DHCPv6 用戶端](../../../network-management/dhcp/dhcpv6-client.md)。有關 DHCPv6 與 IPv4 的 DHCP 有何不同，請參閱 [DHCP](../../../network-management/dhcp/index.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="D" typ="dynamic">該 DHCPv6 用戶端是動態建立的。</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">該 DHCPv6 用戶端已停用。</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">該 DHCPv6 用戶端配置無效。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">用戶端執行的介面。收到的地址會作為動態 /128 地址新增到該介面。</ArgTableRow>
<ArgTableRow arg="request" typ="ubit (info, address, prefix)" mandatory="1">
用戶端向伺服器請求的內容。一個用戶端可以請求以下多項：
- `address` - IPv6 地址 (IA_NA)，會作為動態 /128 地址新增到用戶端介面。
- `prefix` - 委派字首 (IA_PD)，會新增到 `pool-name` 中設定的 IPv6 池。
- `info` - 僅其他設定，不包含地址或字首 (Information-request)。此時用戶端狀態為 `idle`。
</ArgTableRow>
<ArgTableRow arg="accept-prefix-without-address" typ="bool">當同時請求地址和字首時：是否接受包含字首但不包含地址的回覆。使用 `no` 時，用戶端會持續請求，直到伺服器同時提供兩者。預設值：yes。</ArgTableRow>
<ArgTableRow arg="add-default-route" typ="bool">是否透過 DHCPv6 伺服器新增預設路由 (`::/0`)，或者如果回覆經過中繼，則透過中繼新增。DHCPv6 本身不提供預設閘道器。預設值：no。</ArgTableRow>
<ArgTableRow arg="default-route-distance" typ="num">用戶端新增的預設路由的距離。預設值：1。</ArgTableRow>
<ArgTableRow arg="default-route-tables" typ="object { table: alt { table-distance: composite { table: alt { table-default: enum (default) { default:0xffffffff }
, table: enum
 }
, distance: num [1 .. 255]
 }
, table: alt { table-default: enum (default) { default:0xffffffff }
, table: enum
 }
 }
 }">要新增預設路由的路由表，以 `table` 或 `table:distance` 條目表示。`default` 是主路由表；當用戶端介面屬於某個 VRF 時，則是該 VRF 的路由表。預設值：default。</ArgTableRow>
<ArgTableRow arg="check-gateway" typ="enum (none | arp | ping | bfd)">在用戶端新增的預設路由上設定的閘道器檢查 (`none`、`arp`、`ping` 或 `bfd`)，因此僅當其閘道器響應時才會使用該路由。預設值：none。</ArgTableRow>
<ArgTableRow arg="use-peer-dns" typ="bool">是否接受 DHCPv6 伺服器通告的 DNS 伺服器。預設值：yes。</ArgTableRow>
<ArgTableRow arg="use-interface-duid" typ="bool">是否使用根據用戶端介面的 MAC 地址生成的 DUID，而不是路由器的其他 DHCPv6 用戶端及其 DHCPv6 伺服器所使用的路由器 DUID。預設值：no。</ArgTableRow>
<ArgTableRow arg="custom-duid" typ="string">要傳送的 DUID，代替生成的 DUID，以十六進位制表示，例如 `0x0003000102aabbccddee`。覆蓋 `use-interface-duid`。</ArgTableRow>
<ArgTableRow arg="validate-server-duid" typ="bool">是否檢查 DHCPv6 伺服器傳送的 DUID 格式是否正確。使用 `no` 時，會接受格式不正確的伺服器 DUID，但仍會檢查其最小長度。預設值：yes。</ArgTableRow>
<ArgTableRow arg="rapid-commit" typ="bool">是否使用 Rapid Commit 選項請求兩訊息交換 (Solicit 和 Reply)。如果伺服器不使用該選項，或使用 `no`，則使用四訊息交換 (Solicit、Advertise、Request、Reply)。預設值：yes。</ArgTableRow>
<ArgTableRow arg="allow-reconfigure" typ="bool">是否接受來自 DHCPv6 伺服器的 Reconfigure 訊息。啟用後，用戶端會在其 Solicit 中表明這一點，接收重新配置金鑰，並在伺服器傳送 Reconfigure 訊息時立即續租。RouterOS DHCPv6 伺服器會在其設定更改時，以及透過繫結的 `send-reconfigure` 命令傳送 Reconfigure 訊息。預設值：no。</ArgTableRow>
<ArgTableRow arg="dhcp-options" typ="multi { array-id, option: enum
 }">用戶端傳送的選項，按名稱從 `/ipv6/dhcp-client/option` 中選擇。預定義的 `fqdn` 選項會將路由器標識作為用戶端的 FQDN 傳送 (選項 39)。預設值：fqdn。</ArgTableRow>
<ArgTableRow arg="pool-name" typ="string">用戶端根據收到的字首建立動態 IPv6 池的名稱；可以從該池向其他介面分配地址。池的生存時間跟隨字首，並在每次續租時延長。僅在請求字首時應用。</ArgTableRow>
<ArgTableRow arg="pool-prefix-length" typ="num">池分配的字首長度，例如 `64`。它必須等於或長於收到的字首。未設定時，長度會自動選擇，例如收到 /56 時選擇 64。僅在請求字首時應用。</ArgTableRow>
<ArgTableRow arg="prefix-hint" typ="ip6Prefix">向伺服器建議的字首或字首長度，例如 `::/60` 表示請求一個 /60。伺服器不必遵循該建議。`::/0` 表示不傳送提示。預設值：::/0。</ArgTableRow>
<ArgTableRow arg="prefix-address-lists" typ="multi { array-id, prefix-address-list: string
 }">將收到的字首作為動態條目新增到的 IPv6 防火牆地址列表。僅在請求字首時應用。</ArgTableRow>
<ArgTableRow arg="script" typ="alt { script: string
 }">
當用戶端獲取、續租或丟失地址或字首時要執行的指令碼。它會分別針對字首和地址執行，並接收以下變數：
- `pd-valid` - 獲取到字首時為 `1`，丟失字首時為 `0`；當本次運行針對地址時為空。
- `pd-prefix` - 字首及其長度。
- `na-valid` - 獲取到地址時為 `1`，丟失地址時為 `0`；當本次運行針對字首時為空。
- `na-address` - 地址。
- `options` - 從伺服器收到的選項陣列，按選項程式碼索引。
</ArgTableRow>
<ArgTableRow arg="custom-iapd-id" typ="num">用於字首請求 (IA_PD) 的身份關聯識別符號 (IAID)，代替從用戶端介面派生的識別符號。</ArgTableRow>
<ArgTableRow arg="custom-iana-id" typ="num">用於地址請求 (IA_NA) 的身份關聯識別符號 (IAID)，代替從用戶端介面派生的識別符號。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="status" typ="enum (stopped | searching... | requesting... | bound | renewing... | rebinding... | stopping... | declining... | error | idle | requesting-info... | confirming...)">
用戶端當前狀態：
- `searching...` - 傳送 Solicit 訊息並等待伺服器。
- `requesting...` - 請求提供的地址或字首。
- `bound` - 用戶端已獲得其地址或字首。
- `renewing...` - 向提供該地址或字首的伺服器續租。
- `rebinding...` - 伺服器未應答續租；向任意伺服器詢問。
- `requesting-info...` - 等待 Information-request 的回覆 (`request=info`)。
- `idle` - Information-request 已得到應答 (`request=info`)。
- `confirming...` - 向伺服器確認該地址或字首對此鏈路仍然有效。
- `declining...` - 拒絕某個地址。
- `stopping...` - 傳送 Release 訊息。
- `stopped` - 用戶端已停用。
- `error` - 用戶端無法執行。
</ArgTableRow>
<ArgTableRow arg="duid" typ="string">用戶端傳送的 DUID。</ArgTableRow>
<ArgTableRow arg="dhcp-server-v6" typ="ip6Addr">伺服器回覆的來源地址，通常是 DHCPv6 伺服器的鏈路本地地址。</ArgTableRow>
<ArgTableRow arg="prefix" typ="composite { prefix: ip6Prefix
, expires-after: time
 }">收到的字首及其到期剩餘時間。</ArgTableRow>
<ArgTableRow arg="address" typ="composite { address: ip6Addr
, expires-after: time
 }">收到的地址及其到期剩餘時間。</ArgTableRow>
<ArgTableRow arg="reconfigure-key" typ="string">從 DHCPv6 伺服器收到的金鑰，用於驗證其 Reconfigure 訊息。僅在啟用 `allow-reconfigure` 時設定。</ArgTableRow>
<ArgTableRow arg="reconfigure-last-counter" typ="string">從 DHCPv6 伺服器接受的上一條 Reconfigure 訊息的重放檢測計數器。每收到一條 Reconfigure 訊息都會增加。</ArgTableRow>
</ArgTable>
