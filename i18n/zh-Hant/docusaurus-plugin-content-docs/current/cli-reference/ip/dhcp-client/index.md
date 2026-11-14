---
sidebar_key: "cli-reference/ip/dhcp-client"
title: "dhcp-client"
sidebar_label: 'dhcp-client'
source: https://manual.mikrotik.com/docs/cli-reference/ip/dhcp-client
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/dhcp-client {#ipdhcp-client}
**型別：** 目錄

DHCP 用戶端從 DHCP 伺服器獲取介面的 IPv4 地址和網路設定。有關概述和配置示例，請參閱 [DHCP 用戶端](../../../network-management/dhcp/client.md)。有關 DHCP 的工作原理，請參閱 [DHCP](../../../network-management/dhcp/index.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">DHCP 用戶端已停用。</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">DHCP 用戶端配置無效。</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">DHCP 用戶端是動態建立的。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">DHCP 用戶端的名稱。如果未設定，RouterOS 會生成一個名稱，例如 `client1`。</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">DHCP 用戶端執行的介面。收到的 IP 地址會作為動態地址新增到此介面。</ArgTableRow>
<ArgTableRow arg="add-default-route" typ="enum (no | yes | special-classless)">
要從 DHCP 伺服器接收並新增到路由表的路由。
- `yes`（預設） - 當伺服器傳送無類靜態路由（選項 121）時新增該路由，否則透過收到的閘道器（選項 3）新增預設路由。存在選項 121 時，將忽略選項 3 中的閘道器。
- `special-classless` - 同時新增無類靜態路由和透過收到的閘道器的預設路由。
- `no` - 不新增路由。
</ArgTableRow>
<ArgTableRow arg="default-route-distance" typ="num">用戶端新增的路由的距離。預設值：1。</ArgTableRow>
<ArgTableRow arg="default-route-tables" typ="object { table: alt { table-distance: composite { table: alt { table-default: enum (default) { default:0xffffffff }
, table: enum
 }
, distance: num [1 .. 255]
 }
, table: alt { table-default: enum (default) { default:0xffffffff }
, table: enum
 }
 }
 }">要將路由新增到的路由表，使用 `table` 或 `table:distance` 條目指定。此處給定的距離會覆蓋該表的 `default-route-distance`。`default` 是主路由表；當用戶端介面屬於某個 VRF 時，則是該 VRF 的路由表。預設值：default。</ArgTableRow>
<ArgTableRow arg="check-gateway" typ="enum (none | arp | ping | bfd)">在用戶端新增的路由上設定的閘道器檢查（`none`、`arp`、`ping` 或 `bfd`），因此只有當其閘道器響應時才會使用該路由。請參閱[閘道器可達性](../../../user-guides/routing-and-networking-protocols/routing-decision.md)。預設值：none。</ArgTableRow>
<ArgTableRow arg="use-peer-dns" typ="bool">是否使用從 DHCP 伺服器收到的 DNS 伺服器。它們會被新增到 DNS 解析器的動態伺服器（`/ip/dns`）。預設值：yes。</ArgTableRow>
<ArgTableRow arg="use-peer-ntp" typ="bool">是否使用從 DHCP 伺服器收到的 NTP 伺服器。它們會作為動態條目新增到 NTP 用戶端伺服器（`/system/ntp/client/servers`）。預設值：yes。</ArgTableRow>
<ArgTableRow arg="allow-reconfigure" typ="bool">是否接受來自 DHCP 伺服器的 Reconfigure（FORCERENEW）訊息。啟用後，用戶端在繫結時請求 reconfigure 金鑰，伺服器會在其回覆中傳送該金鑰。該金鑰用於驗證伺服器的 Reconfigure 訊息（RFC 6704、HMAC-MD5）。收到 Reconfigure 訊息時，用戶端會立即續租。伺服器只能向在啟用此設定的情況下完成繫結的用戶端傳送 Reconfigure 訊息。預設值：no。</ArgTableRow>
<ArgTableRow arg="vlan-priority" typ="num">用戶端傳送的封包的 VLAN 頭中設定的優先順序程式碼點（PCP，0-7）。僅當用戶端執行在 VLAN 介面上時適用。</ArgTableRow>
<ArgTableRow arg="dscp" typ="num">用戶端傳送的封包的 IP 頭中設定的 DSCP 值（0-63）。未設定時，封包以 DSCP 0 傳送。</ArgTableRow>
<ArgTableRow arg="use-broadcast" typ="enum (always | never | both)">
用戶端是否在 DHCPDISCOVER 和 DHCPREQUEST 訊息中設定廣播標誌，以要求伺服器廣播其回覆。續租請求以單播發送，並且從不設定該標誌。
- `both`（預設） - 在獲取地址的前 15 秒內設定該標誌，之後不再設定。
- `always` - 始終設定該標誌。
- `never` - 從不設定該標誌。
</ArgTableRow>
<ArgTableRow arg="dhcp-options" typ="multi { array-id, option: enum
 }">用戶端傳送到 DHCP 伺服器的選項，按名稱從 `/ip/dhcp-client/option` 中選擇。預定義的 `clientid` 和 `clientid_duid` 選項都使用程式碼 61：`clientid` 透過其介面的 MAC 地址標識用戶端，`clientid_duid` 透過路由器的 DUID（RFC 4361）標識用戶端，該 DUID 與 DHCPv6 用戶端使用的 DUID 相同。預設值：hostname,clientid。</ArgTableRow>
<ArgTableRow arg="script" typ="alt { script: string
 }">
當用戶端獲得租約以及丟失或釋放租約時要執行的指令碼。該指令碼會接收以下變數：
- `bound` - 獲得租約時為 `1`，丟失或釋放租約時為 `0`。
- `server-address` - DHCP 伺服器的 IP 地址。
- `lease-address` - 租約中的 IP 地址。
- `interface` - 用戶端介面的名稱。
- `gateway-address` - 從伺服器收到的閘道器。
- `vendor-specific` - 從伺服器收到的 vendor-specific 資訊選項（選項 43）的值。
- `lease-options` - 從伺服器收到的選項陣列，以選項程式碼為索引。二進位制選項的值為十六進位制字串。
</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="custom-source-mac-address" typ="macAddr">DHCP 用戶端使用的自定義源 MAC 地址。</ArgTableRow>
<ArgTableRow arg="custom-hostname-suffix" typ="string">追加到傳送給 DHCP 伺服器的主機名後的字尾。</ArgTableRow>
<ArgTableRow arg="status" typ="enum (stopped | searching... | requesting... | bound | renewing... | rebinding... | error) { stopped:0, searching...:1, requesting...:2, bound:3, renewing...:4, rebinding...:5, error:6 }">
用戶端當前狀態：
- `searching...` - 傳送 DHCPDISCOVER 訊息並等待 offer。
- `requesting...` - 請求已提供的地址。
- `bound` - 用戶端擁有租約。
- `renewing...` - 從租約時間過半時開始，向發放租約的伺服器續租。
- `rebinding...` - 伺服器未回應續租。從租約時間的 87.5% 開始，向任意伺服器請求租約。
- `stopped` - 用戶端已停用。
- `error` - 用戶端無法執行。
</ArgTableRow>
<ArgTableRow arg="address" typ="composite { address: ipAddr
, netmask: num [ .. 32]
 }">從 DHCP 伺服器收到的 IP 地址和字首長度。</ArgTableRow>
<ArgTableRow arg="netmask" typ="ipAddr">從 DHCP 伺服器收到的子網掩碼。</ArgTableRow>
<ArgTableRow arg="gateway" typ="ipAddr">從 DHCP 伺服器收到的閘道器（選項 3）。</ArgTableRow>
<ArgTableRow arg="dhcp-server" typ="ipAddr">發放該租約的 DHCP 伺服器的 IP 地址。</ArgTableRow>
<ArgTableRow arg="primary-dns" typ="ipAddr">從 DHCP 伺服器收到的第一個 DNS 伺服器。</ArgTableRow>
<ArgTableRow arg="secondary-dns" typ="ipAddr">從 DHCP 伺服器收到的第二個 DNS 伺服器。</ArgTableRow>
<ArgTableRow arg="primary-ntp" typ="ipAddr">從 DHCP 伺服器收到的第一個 NTP 伺服器。</ArgTableRow>
<ArgTableRow arg="secondary-ntp" typ="ipAddr">從 DHCP 伺服器收到的第二個 NTP 伺服器。</ArgTableRow>
<ArgTableRow arg="cmr-address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="caps-managers" typ="multi { ip: ipAddr
 }">從 DHCP 伺服器收到的 CAPsMAN 地址（選項 138）。</ArgTableRow>
<ArgTableRow arg="reconfigure-key" typ="string">從 DHCP 伺服器收到的金鑰，用於驗證其 Reconfigure 訊息（RFC 6704、HMAC-MD5）。僅在啟用 `allow-reconfigure` 時設定。</ArgTableRow>
<ArgTableRow arg="reconfigure-last-counter" typ="string">從 DHCP 伺服器接受的最後一條 Reconfigure 訊息的重放檢測計數器。用戶端繫結時從 0 開始，並隨每條 Reconfigure 訊息遞增。</ArgTableRow>
<ArgTableRow arg="expires-after" typ="time">租約到期前的時間。</ArgTableRow>
</ArgTable>
