---
sidebar_key: "cli-reference/ip/dhcp-server/lease/index"
sidebar_position: 2
title: "lease"
sidebar_label: 'lease'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/dhcp-server/lease
captured_at: '2026-11-01T21:23:53+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/dhcp-server/lease {#ipdhcp-serverlease}
**型別：** 目錄

DHCP 伺服器的租約。動態租約在用戶端從地址池獲取地址時建立；靜態租約可為特定用戶端提供固定地址、地址池或其自身設定。詳情請參閱 [DHCP 伺服器](../../../../network-management/dhcp/server.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">該租約已被停用。</ArgTableRow>
<ArgTableRow arg="R" typ="radius">該租約由 RADIUS 伺服器分配。</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">該租約是動態的：它是在用戶端從地址池獲取地址時建立的。使用 `make-static` 將其轉換為靜態租約。</ArgTableRow>
<ArgTableRow arg="B" typ="blocked">用戶端已被阻止（`block-access=yes`），不會收到伺服器的回覆。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="address" typ="alt { ip-address: ipAddr
, pool: enum
 }">靜態租約的 IP 地址，或用於向用戶端分配地址的 IP 地址池名稱。使用 `0.0.0.0` 時，將使用伺服器的地址池。</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">該靜態租約所針對用戶端的 MAC 地址。</ArgTableRow>
<ArgTableRow arg="use-src-mac" typ="bool">是否透過用戶端封包的源 MAC 地址而不是 DHCP 訊息的用戶端硬體地址欄位（`chaddr`）來識別用戶端。</ArgTableRow>
<ArgTableRow arg="client-id" typ="string">該靜態租約所針對用戶端的用戶端識別符號（選項 61），格式如 `active-client-id` 所示，例如 `1:4e:97:a1:4c:d1:38`。</ArgTableRow>
<ArgTableRow arg="rate-limit" typ="string">
用戶端的頻寬限制，格式為 `rx-rate[/tx-rate] [rx-burst-rate[/tx-burst-rate] [rx-burst-threshold[/tx-burst-threshold] [rx-burst-time[/tx-burst-time]]]]`。速率單位為位元每秒，可選 `k` 或 `M` 字尾，缺失的 tx 值取自 rx 值。只有靜態租約可以設定速率限制。

伺服器會為租約地址建立一個名為 `dhcp-ds<hostname/MAC>` 的動態簡單佇列，並將此限制作為 `limit-at` 和 `max-limit`。
</ArgTableRow>
<ArgTableRow arg="routes" typ="object { route: composite { dst-address: address (flags=4/)
, gateway: [ composite { gateway: address (flags=46ivL)
, distance: [ num [1 .. 255]]
 }]
 }
 }">租約繫結期間伺服器新增的路由，格式為以逗號分隔的 `dst-address/mask gateway distance` 條目，例如 `10.77.0.0/24 172.31.255.105 5`。</ArgTableRow>
<ArgTableRow arg="insert-queue-before" typ="enum (bottom | first) { bottom:0xffffffff, first:0 }">此租約建立的動態簡單佇列的放置位置：`first`（預設）放在 `/queue/simple` 頂部，`bottom` 放在末尾，或放在指定名稱的佇列之前。</ArgTableRow>
<ArgTableRow arg="parent-queue" typ="enum (none) { none:0 }">此租約建立的動態簡單佇列的父佇列。預設值：none。</ArgTableRow>
<ArgTableRow arg="queue-type" typ="enum">此租約建立的動態簡單佇列的佇列型別。</ArgTableRow>
<ArgTableRow arg="address-lists" typ="multi { array-id, address-list: string
 }">租約繫結期間，將租約地址新增到的防火牆地址列表。</ArgTableRow>
<ArgTableRow arg="server" typ="enum (all) { all:0 }">租約所屬的 DHCP 伺服器。使用 `all` 時，該靜態租約在所有伺服器上有效。</ArgTableRow>
<ArgTableRow arg="block-access" typ="bool">是否阻止用戶端：伺服器不響應用戶端，租約獲得 `B` 標誌。預設值：no。</ArgTableRow>
<ArgTableRow arg="allow-dual-stack-queue" typ="bool">此租約與同一用戶端的 DHCPv6 繫結是否共用一個動態簡單佇列，該佇列隨後同時包含 IPv4 和 IPv6 地址。預設值：yes。</ArgTableRow>
<ArgTableRow arg="lease-time" typ="time">此用戶端的租約時間。未設定或設定為 `0s` 時，使用伺服器的 `lease-time`。</ArgTableRow>
<ArgTableRow arg="always-broadcast" typ="bool">是否即使用戶端未設定廣播標誌，也向其廣播回覆。預設值：no。</ArgTableRow>
<ArgTableRow arg="dhcp-option" typ="multi { array-id, option: enum
 }">要傳送給此用戶端的選項（`/ip/dhcp-server/option`）。它們優先於伺服器和網路的選項。</ArgTableRow>
<ArgTableRow arg="dhcp-option-set" typ="enum (none)">要傳送給此用戶端的選項集（`/ip/dhcp-server/option/sets`）。它優先於伺服器和網路的選項。</ArgTableRow>
<ArgTableRow arg="agent-circuit-id" typ="string">設定後，即使 MAC 地址或用戶端 ID 不同，租約也會匹配其內中繼代理資訊包含此電路 ID 的請求。</ArgTableRow>
<ArgTableRow arg="agent-remote-id" typ="string">設定後，即使 MAC 地址或用戶端 ID 不同，租約也會匹配其內中繼代理資訊包含此遠端 ID 的請求。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="status" typ="enum (waiting | testing | declined | offered | bound | authorizing | conflict) { waiting:0, testing:1, declined:2, offered:3, bound:4, authorizing:5 }">
租約狀態：
- `waiting` - 未使用的靜態租約。
- `testing` - 伺服器正在檢查地址衝突（`conflict-detection`）。
- `offered` - 伺服器已提供地址，並等待用戶端的請求。
- `bound` - 用戶端正在使用該地址。
- `authorizing` - 伺服器正在等待 RADIUS 伺服器的回覆。
- `conflict` - 另一臺主機已在使用該地址。租約會在租約時間內保留該地址不使用；當另一臺主機不再響應時，`check-status` 會釋放它。
- `declined` - 用戶端透過 DHCPDECLINE 訊息拒絕了該地址。
</ArgTableRow>
<ArgTableRow arg="expires-after" typ="time">租約到期前的時間。</ArgTableRow>
<ArgTableRow arg="last-seen" typ="alt { symbolic-names: enum (never | sometime) { never:0xffffffff, sometime:0xfffffffe }
, time: time
 }">自伺服器上次收到用戶端請求以來經過的時間，或 `never`。</ArgTableRow>
<ArgTableRow arg="age" typ="time">自租約建立以來經過的時間。</ArgTableRow>
<ArgTableRow arg="active-address" typ="ipAddr">用戶端使用的 IP 地址。</ArgTableRow>
<ArgTableRow arg="active-mac-address" typ="macAddr">使用該租約的用戶端的 MAC 地址。</ArgTableRow>
<ArgTableRow arg="active-client-id" typ="string">使用該租約的用戶端的用戶端識別符號（選項 61）。</ArgTableRow>
<ArgTableRow arg="active-server" typ="enum">為該用戶端提供服務的 DHCP 伺服器。</ArgTableRow>
<ArgTableRow arg="active-agent-circuit-id" typ="string">用戶端請求的中繼代理資訊（選項 82）中的電路 ID，十六進位制表示。</ArgTableRow>
<ArgTableRow arg="active-agent-remote-id" typ="string">用戶端請求的中繼代理資訊（選項 82）中的遠端 ID，十六進位制表示。</ArgTableRow>
<ArgTableRow arg="active-agent-circuit-id-ascii" typ="string">用戶端請求的中繼代理資訊（選項 82）中的電路 ID，文字形式。</ArgTableRow>
<ArgTableRow arg="active-agent-remote-id-ascii" typ="string">用戶端請求的中繼代理資訊（選項 82）中的遠端 ID，文字形式。</ArgTableRow>
<ArgTableRow arg="host-name" typ="string">用戶端傳送的主機名（選項 12）。</ArgTableRow>
<ArgTableRow arg="class-id" typ="string">上次收到的 DHCP 請求中的 DHCP 選項 60。</ArgTableRow>
<ArgTableRow arg="src-mac-address" typ="macAddr">用戶端上次請求的源 MAC 地址。</ArgTableRow>
<ArgTableRow arg="reconfigure-key" typ="string">伺服器在用戶端繫結時的回覆中提供給用戶端的金鑰，用於驗證 Reconfigure 訊息（RFC 6704、HMAC-MD5）。需要在伺服器上啟用 `use-reconfigure`。</ArgTableRow>
<ArgTableRow arg="reconfigure-last-sent" typ="string">傳送給用戶端的最後一條 Reconfigure 訊息的重放檢測計數器。每傳送一條 Reconfigure 訊息，它都會增加。</ArgTableRow>
<ArgTableRow arg="reconfigure-status" typ="string"></ArgTableRow>
</ArgTable>
