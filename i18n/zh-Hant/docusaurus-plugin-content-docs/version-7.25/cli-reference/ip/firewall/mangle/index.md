---
sidebar_key: "cli-reference/ip/firewall/mangle/index"
sidebar_position: 1
title: "mangle"
sidebar_label: 'mangle'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/firewall/mangle
captured_at: '2026-11-01T21:24:02+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/firewall/mangle {#ipfirewallmangle}
**型別：** 目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="all" typ="switch"></ArgTableRow>
<ArgTableRow arg="static" typ="switch"></ArgTableRow>
<ArgTableRow arg="dynamic" typ="switch"></ArgTableRow>
<ArgTableRow arg="chain" typ="enum" mandatory="1">指定規則將新增到哪個鏈。如果輸入與已定義鏈的名稱不匹配，則會建立一個新鏈。</ArgTableRow>
<ArgTableRow arg="action" typ="enum (accept | jump | return | log | passthrough | add-src-to-address-list | add-dst-to-address-list | sniff-tzsp | sniff-pc | drop | mark-packet | mark-connection | change-mss | change-dscp | strip-ipv4-options | change-ttl | mark-routing | set-priority | clear-df | fasttrack-connection | route) { accept:0, jump:1, return:2, log:3, passthrough:4, add-src-to-address-list:5, add-dst-to-address-list:6, sniff-tzsp:7, sniff-pc:8, drop:10, mark-packet:30, mark-connection:31, change-mss:32, change-dscp:33, strip-ipv4-options:34, change-ttl:35, mark-routing:36, set-priority:37, clear-df:39, fasttrack-connection:40, route:41 }">
如果封包被規則匹配，則要執行的動作：
- `accept` - 接受封包。封包不會傳遞給下一條防火牆規則。
- `add-dst-to-address-list` - 將目標地址新增到由 `address-list` 引數指定的地址列表。
- `add-src-to-address-list` - 將源地址新增到由 `address-list` 引數指定的地址列表。
- `jump` - 跳轉到由 `jump-target` 引數值指定的使用者定義鏈。
- `log` - 向系統日誌新增一條包含以下資料的訊息：in-interface、out-interface、src-mac、protocol、src-ip:port-&gt;dst-ip:port 以及封包長度。封包匹配後，會傳遞給列表中的下一條規則，類似於 `passthrough`。
- `passthrough` - 如果封包被規則匹配，則增加計數器並轉到下一條規則（對統計有用）。
- `return` - 將控制權返回到發生跳轉的鏈。
- `sniff-tzsp` - 將封包傳送到遠端 TZSP 相容系統（例如 Wireshark）。使用 `sniff-target` 和 `sniff-target-port` 引數設定遠端目標（Wireshark 建議使用埠 37008）。封包匹配後，會傳遞給列表中的下一條規則，類似於 `passthrough`。
- `sniff-pc` - 將封包傳送到遠端 RouterOS CALEA 伺服器。封包匹配後，會傳遞給列表中的下一條規則，類似於 `passthrough`。
- `drop` - 靜默丟棄封包。
- `mark-packet` - 使用指定的 `new-packet-mark` 標記封包。
- `mark-connection` - 使用指定的 `new-connection-mark` 標記連線。
- `change-mss` - 將封包的最大分段大小（MSS）欄位值更改為由 `new-mss` 引數指定的值。
- `change-dscp` - 更改由 `new-dscp` 引數指定的差分服務程式碼點（DSCP）欄位值。
- `change-ttl` - 將封包的生存時間（TTL）欄位值更改為由 `new-ttl` 引數指定的值。
- `mark-routing` - 在封包上放置由 `new-routing-mark` 引數指定的標記。此類標記僅用於策略路由目的。對於由 FastTrack 處理的封包，不要應用除 `main` 以外的任何其他路由標記，因為 FastTrack 只能在主路由表中工作。
- `set-priority` - 設定封包的優先順序。
- `clear-df` - 清除 Don't Fragment（不分片）標誌。
- `fasttrack-connection` - 標記連線以供 FastTrack 使用。封包匹配後，會傳遞給列表中的下一條規則，類似於 `passthrough`。
- `route` - 透過忽略正常路由決策，強制將封包傳送到由 'route-dst' 引數指定的閘道器 IP（僅限 prerouting 鏈）。
- `strip-ipv4-options` - 從 IP 頭部剝離 IPv4 選項欄位。該動作實際上並不會移除 IPv4 選項，而是將所有選項位元組替換為 NOP。後續使用 `ipv4-options=any` 的匹配器仍會匹配該封包。
</ArgTableRow>
<ArgTableRow arg="jump-target" typ="enum ()">要跳轉到的目標鏈名稱。僅當 `action=jump` 時適用。</ArgTableRow>
<ArgTableRow arg="new-packet-mark" typ="enum ()">設定新的封包標記值。</ArgTableRow>
<ArgTableRow arg="new-connection-mark" typ="enum ()">設定新的連線標記值。</ArgTableRow>
<ArgTableRow arg="new-routing-mark" typ="enum ()">設定新的 `routing-mark` 值。在 RouterOS v7 中，路由標記必須事先建立為新的 [路由表](../../../../user-guides/routing-and-networking-protocols/policy-routing.md)</ArgTableRow>
<ArgTableRow arg="new-mss" typ="alt { mss-action: enum (clamp-to-pmtu) { clamp-to-pmtu:65535 }
, mss-value: num [40 .. 65534]
 }">為封包設定新的 MSS。**重要：** Clamp-to-pmtu 功能會設定 IP 頭部中的 DF 位，以動態發現路徑的 PMTU。主機會在該路徑上傳送所有設定了 DF 位的封包，直到收到程式碼含義為“需要分片且設定了 DF”的 ICMP Destination Unreachable 訊息。收到此類訊息後，源主機會降低其對該路徑的假定 PMTU。</ArgTableRow>
<ArgTableRow arg="new-dscp" typ="enum (from-priority-to-high-3-bits | from-priority) { from-priority-to-high-3-bits:254, from-priority:255 }">設定新的 DSCP 值。</ArgTableRow>
<ArgTableRow arg="new-priority" typ="alt { new-priority: enum (from-dscp | from-ingress | from-dscp-high-3-bits) { from-dscp:65536, from-ingress:65537, from-dscp-high-3-bits:65538 }
, new-priority: num [0 .. 63]
 }">設定封包的新優先順序。這可以是 VLAN、WMM、DSCP 或 MPLS EXP 優先順序 [閱讀更多](../../../../bridging-and-switching/user-guides/wmm-and-vlan-priority.md)。此屬性也可用於設定內部優先順序。</ArgTableRow>
<ArgTableRow arg="new-ttl" typ="super { mode: enum (set | increment | decrement) { set:0, increment:1, decrement:2 }
, [value] :num [0 .. 255]
 }">設定新的 TTL 值。</ArgTableRow>
<ArgTableRow arg="passthrough" typ="bool">是否允許封包傳遞到下一條規則。</ArgTableRow>
<ArgTableRow arg="tcp-flags" typ="super { !,
, flags: multi { array-id, array-id, flag: super { !
, flag: enum (fin | syn | rst | psh | ack | urg | ece | cwr) { fin:0, syn:1, rst:2, psh:3, ack:4, urg:5, ece:6, cwr:7 }
 }
 }
 }">
匹配指定的 TCP 標誌：
- `ack` - 確認資料。
- `cwr` - 擁塞視窗已減小。
- `ece` - ECN-echo 標誌（顯式擁塞通知）。
- `fin` - 關閉連線。
- `psh` - 推送功能。
- `rst` - 重設連線。
- `syn` - 新建連線。
- `urg` - 緊急資料。
</ArgTableRow>
<ArgTableRow arg="p2p" typ="super { !
, p2p: enum (fasttrack | gnutella | direct-connect | edonkey | bit-torrent | blubster | soulseek | winmx | warez | all-p2p) { fasttrack:0x01, gnutella:0x02, direct-connect:0x03, edonkey:0x04, bit-torrent:0x05, blubster:0x06, soulseek:0x07, winmx:0x08, warez:0x09, all-p2p:0xFF }
 }">匹配某些未加密的 P2P 協定。已棄用，因為大多數流量都已加密，需要深度包檢測才能識別。僅限 IPv4。</ArgTableRow>
<ArgTableRow arg="connection-state" typ="super { !
, state: ubit (invalid, established, related, new, untracked)
 }">
解釋特定封包的連線跟蹤分析資料：
- `established` - 屬於現有連線的封包。
- `invalid` - 在連線跟蹤中沒有確定狀態的封包（通常是嚴重亂序的封包、序號/確認號錯誤的封包，或路由器資源過度使用的情況）。invalid 封包不會參與 NAT（因為只有 connection-state=new 封包會參與），並且在路由時仍會包含原始源 IP 地址。你應該在防火牆 filter 的 forward 和 input 鏈中丟棄所有 `connection-state=invalid` 封包。
- `new` - 封包已開始新連線，或者以其他方式關聯到尚未在兩個方向上看到封包的連線。
- `related` - 與現有連線相關但不屬於該連線的封包，例如 ICMP 錯誤，或開啟 FTP 資料連線的封包。
- `untracked` - 在防火牆 RAW 表中被設定為繞過連線跟蹤的封包。
</ArgTableRow>
<ArgTableRow arg="connection-nat-state" typ="super { !
, state: ubit (srcnat, dstnat)
 }">
匹配源 NAT、目標 NAT 或兩者兼有的連線。`connection-state=related` 連線的 connection-nat-state 由第一個封包的方向決定；如果連線跟蹤需要使用 dst-nat 將該連線傳遞到與主連線相同的主機，那麼即使完全沒有 dst-nat 規則，它也會處於 connection-nat-state=dstnat。
`ein-snat` 和 `ein-dnat` 是使用端點無關 NAT 時的源 NAT 和目標 NAT 連線。
</ArgTableRow>
<ArgTableRow arg="sniff-target" typ="ipAddr">要將嗅探到的封包傳送到的 IP 地址。</ArgTableRow>
<ArgTableRow arg="sniff-target-port" typ="num">要將嗅探到的封包傳送到的埠。</ArgTableRow>
<ArgTableRow arg="sniff-id" typ="num">嗅探會話的 ID。</ArgTableRow>
<ArgTableRow arg="route-dst" typ="ipAddr">指定 `route` 動作的路由目標。</ArgTableRow>
<ArgTableRow arg="tls-host" typ="super { !
, tls-host: string
 }">基於 TLS SNI 主機名匹配 HTTPS 流量。接受用於萬用字元匹配的 GLOB 語法。如果 TLS 握手幀被分片為多個 TCP 段，匹配器將無法匹配主機名。</ArgTableRow>
<ArgTableRow arg="connection-limit" typ="super { !
, limit: num
, [netmask] ,num
 }">在達到給定值後，按地址或地址塊匹配連線。應將其與 `connection-state=new` 和/或 `tcp-flags=syn` 一起使用，因為該匹配器非常消耗資源。</ArgTableRow>
<ArgTableRow arg="layer7-protocol" typ="super { !
, protocol: enum
 }">在 layer7 protocol 選單中定義的 Layer7 過濾器名稱。</ArgTableRow>
<ArgTableRow arg="realm" typ="super { !
, realm: num
 }">匹配路由 realm。僅限 IPv4。</ArgTableRow>
<ArgTableRow arg="protocol" typ="super { !
, protocol: enum ()
 }">匹配由協定名稱或編號指定的特定 IP 協定。</ArgTableRow>
<ArgTableRow arg="src-address" typ="super { !
, range: ipRange
 }">匹配源地址等於指定 IP 或落在指定 IP 範圍內的封包。</ArgTableRow>
<ArgTableRow arg="dst-address" typ="super { !
, range: ipRange
 }">匹配目標地址等於指定 IP 或落在指定 IP 範圍內的封包。</ArgTableRow>
<ArgTableRow arg="fragment" typ="super { fragment: bool
 }">匹配分片封包。第一個（起始）分片不計入。如果啟用了連線跟蹤，則不會有分片，因為系統會自動重組每個封包。僅限 IPv4。</ArgTableRow>
<ArgTableRow arg="psd" typ="super { weight-threshold: num
, [delay-threshold] ,time
, [low-port-weight] ,num
, [high-port-weight] ,num
 }">
嘗試檢測 TCP 和 UDP 掃描。引數採用以下格式：`WeightThreshold, DelayThreshold, LowPortWeight, HighPortWeight`。
- `WeightThreshold` - 來自同一主機、具有不同目標埠的最近 TCP/UDP 封包被視為埠掃描序列的總權重。
- `DelayThreshold` - 來自同一主機、具有不同目標埠的封包被視為可能埠掃描子序列的延遲。
- `LowPortWeight` - 具有特權目標埠（&lt;1024）的封包的權重。
- `HighPortWeight` - 具有非特權目標埠的封包的權重。僅限 IPv4。
</ArgTableRow>
<ArgTableRow arg="ipv4-options" typ="super { options: enum (strict-source-routing | loose-source-routing | no-source-routing | record-route | no-record-route | timestamp | no-timestamp | router-alert | no-router-alert | any | none) { strict-source-routing:0x1, loose-source-routing:0x2, no-source-routing:0x4, record-route:0x8, no-record-route:0x10, timestamp:0x20, no-timestamp:0x40, router-alert:0x80, no-router-alert:0x100, any:0x200, none:0x400 }
 }">
匹配 IPv4 頭部選項。
- `any` - 匹配帶有至少一個 IPv4 選項的封包。
- `loose-source-routing` - 匹配帶有鬆散源路由選項的封包。
- `no-record-route` - 匹配不帶記錄路由選項的封包。
- `no-router-alert` - 匹配不帶路由器告警選項的封包。
- `no-source-routing` - 匹配不帶源路由選項的封包。
- `no-timestamp` - 匹配不帶時間戳選項的封包。
- `record-route` - 匹配帶有記錄路由選項的封包。
- `router-alert` - 匹配帶有路由器告警選項的封包。
- `strict-source-routing` - 匹配帶有嚴格源路由選項的封包。
- `timestamp` - 匹配帶有時間戳的封包。僅限 IPv4。
</ArgTableRow>
<ArgTableRow arg="src-address-type" typ="super { !
, type: ubit (unicast, local, broadcast, multicast, blackhole)
 }">
匹配源地址型別：
- `unicast` - 用於點對點傳輸的 IP 地址。
- `local` - 該地址分配給路由器的某個介面。
- `broadcast` - 封包傳送到子網中的所有裝置。
- `multicast` - 封包轉發到定義的一組裝置。
</ArgTableRow>
<ArgTableRow arg="dst-address-type" typ="super { !
, type: ubit (unicast, local, broadcast, multicast, blackhole)
 }">
匹配目標地址型別：
- `unicast` - 用於點對點傳輸的 IP 地址。
- `local` - 目標地址分配給路由器的某個介面。
- `broadcast` - 封包傳送到子網中的所有裝置。
- `multicast` - 封包轉發到定義的一組裝置。
</ArgTableRow>
<ArgTableRow arg="src-address-list" typ="super { !
, address-list: enum
 }">將封包的源地址與使用者定義的地址列表進行匹配。僅支援一個列表。</ArgTableRow>
<ArgTableRow arg="dst-address-list" typ="super { !
, address-list: enum
 }">將封包的目標地址與使用者定義的地址列表進行匹配。僅支援一個列表。</ArgTableRow>
<ArgTableRow arg="hotspot" typ="multi { array-id, array-id, flag: super { !
, flag: enum (from-client | auth | local-dst | to-client | http) { from-client:0, auth:1, local-dst:2, to-client:3, http:4 }
 }
 }">
將來自 HotSpot 用戶端的封包與各種 HotSpot 匹配器進行匹配。
- `auth` - 匹配已認證的 HotSpot 用戶端封包。
- `from-client` - 匹配來自 HotSpot 用戶端的封包。
- `http` - 匹配發送到 HotSpot 伺服器的 HTTP 請求。
- `local-dst` - 匹配發往 HotSpot 伺服器的封包。
- `to-client` - 匹配發送到 HotSpot 用戶端的封包。僅限 IPv4。
</ArgTableRow>
<ArgTableRow arg="address-list" typ="enum ()">要使用的地址列表名稱。當動作為 `add-dst-to-address-list` 或 `add-src-to-address-list` 時適用。</ArgTableRow>
<ArgTableRow arg="address-list-timeout" typ="alt { address-list-timeout: enum (none-dynamic | none-static) { none-dynamic:0, none-static:0xffffffff }
, address-list-timeout: time [ .. 21474836]
 }">
在 `add-src-to-address-list` 或 `add-dst-to-address-list` 動作新增地址後，該地址在 `address-list` 中保留多長時間。指定時間時，規則會新增一個動態條目（`D`），路由器會在時間結束後將其移除；規則每次新的匹配都會將時間重設為其完整值。最大值為 `35w3d13h13m56s`。如果地址已經是列表中的靜態條目，則保持靜態。
- `none-dynamic` (`0s`) - 新增一個不帶超時的動態條目。它不會儲存到配置中，重啟後會清除。
- `none-static` - 新增一個靜態條目。它會儲存到配置和匯出中，並且在重啟後仍會保留，直到你將其移除。
</ArgTableRow>
<ArgTableRow arg="ttl" typ="super { mode: enum (equal | not-equal | less-than | greater-than) { equal:0, not-equal:1, less-than:2, greater-than:3 }
, [value] :num [0 .. 255]
 }">匹配封包的 TTL 值。僅限 IPv4。</ArgTableRow>
<ArgTableRow arg="connection-mark" typ="super { !
, mark: enum
 }">匹配由 mangle 功能使用特定連線標記進行標記的封包。如果設定了 `no-mark`，則規則將匹配任何未標記的連線。</ArgTableRow>
<ArgTableRow arg="connection-type" typ="super { !
, type: enum (ftp | pptp | h323 | sip | irc | quake3 | tftp) { ftp:0, pptp:1, h323:2, sip:3, irc:4, quake3:5, tftp:6 }
 }">基於連線跟蹤 helper 的資訊，匹配來自相關連線的封包。必須在 `/ip/firewall/service-port` 下啟用相關的連線 helper。</ArgTableRow>
<ArgTableRow arg="connection-bytes" typ="super { from: num
, [to] -num
 }">僅當透過特定連線傳輸了給定數量的位元組時，才匹配封包。0 表示無限，例如 `connection-bytes=2000000-0` 表示如果透過相關連線傳輸了超過 2MB，則規則匹配。</ArgTableRow>
<ArgTableRow arg="connection-rate" typ="super { !
, from: num
, [to] -num
 }">允許根據連線的當前速度捕獲流量。</ArgTableRow>
<ArgTableRow arg="routing-mark" typ="super { !
, mark: enum ()
 }">匹配由 mangle 功能使用特定路由標記進行標記的封包。</ArgTableRow>
<ArgTableRow arg="in-interface" typ="super { !
, interface: iface_enum
 }">封包進入路由器時所經過的介面。</ArgTableRow>
<ArgTableRow arg="out-interface" typ="super { !
, interface: iface_enum
 }">封包離開路由器時所經過的介面。</ArgTableRow>
<ArgTableRow arg="in-interface-list" typ="super { !
, interface-list: enum
 }">介面列表中定義的介面集合。工作方式與 `in-interface` 相同。</ArgTableRow>
<ArgTableRow arg="out-interface-list" typ="super { !
, interface-list: enum
 }">介面列表中定義的介面集合。工作方式與 `out-interface` 相同。</ArgTableRow>
<ArgTableRow arg="in-bridge-port" typ="super { !
, interface: iface_enum
 }">當入介面是網橋時，封包進入路由器所經過的實際介面。僅在網橋設定中啟用了 `use-ip-firewall` 時有效。</ArgTableRow>
<ArgTableRow arg="out-bridge-port" typ="super { !
, interface: iface_enum
 }">當出介面是網橋時，封包離開路由器所經過的實際介面。僅在網橋設定中啟用了 `use-ip-firewall` 時有效。</ArgTableRow>
<ArgTableRow arg="in-bridge-port-list" typ="super { !
, interface-list: enum
 }">介面列表中定義的介面集合。工作方式與 `in-bridge-port` 相同。</ArgTableRow>
<ArgTableRow arg="out-bridge-port-list" typ="super { !
, interface-list: enum
 }">介面列表中定義的介面集合。工作方式與 `out-bridge-port` 相同。</ArgTableRow>
<ArgTableRow arg="packet-mark" typ="super { !
, mark: enum
 }">匹配由 mangle 功能使用特定封包標記進行標記的封包。如果設定了 `no-mark`，則規則將匹配任何未標記的封包。</ArgTableRow>
<ArgTableRow arg="src-port" typ="super { !
, port: multi { range: range [ .. 65535]
 }
 }">源埠和源埠範圍列表。僅當協定為 TCP 或 UDP 時適用。</ArgTableRow>
<ArgTableRow arg="dst-port" typ="super { !
, port: multi { range: range [ .. 65535]
 }
 }">目標埠號或埠號範圍列表。</ArgTableRow>
<ArgTableRow arg="port" typ="super { !
, port: multi { range: range [ .. 65535]
 }
 }">如果任一（源或目標）埠匹配指定的埠或埠範圍列表，則匹配。僅當 `protocol` 為 TCP 或 UDP 時適用。</ArgTableRow>
<ArgTableRow arg="icmp-options" typ="super { !
, type: num [0 .. 255]
, [code] [ :range [ .. 255]]
 }">匹配 ICMP type:code 欄位。</ArgTableRow>
<ArgTableRow arg="src-mac-address" typ="super { !
, address: macAddr
 }">匹配封包的源 MAC 地址。</ArgTableRow>
<ArgTableRow arg="content" typ="super { !
, content: string
 }">匹配包含指定文字的封包。</ArgTableRow>
<ArgTableRow arg="ingress-priority" typ="super { !
, ingress-priority: num [0 .. 63]
 }">匹配入站封包的優先順序。優先順序可能來自 VLAN、WMM、DSCP 或 MPLS EXP 位。</ArgTableRow>
<ArgTableRow arg="priority" typ="super { !
, priority: num [0 .. 63]
 }">匹配設定新優先順序之後的封包優先順序。優先順序可能來自 VLAN、WMM、DSCP、MPLS EXP 位，或來自使用 set-priority 動作設定的優先順序。</ArgTableRow>
<ArgTableRow arg="dscp" typ="super { !
, dscp: num [0 .. 63]
 }">匹配 DSCP IP 頭欄位。</ArgTableRow>
<ArgTableRow arg="tos" typ="super { !
, tos: num [0 .. 255]
, [mask] [ /num [0 .. 255]]
 }"></ArgTableRow>
<ArgTableRow arg="limit" typ="super { !
, count: num [1 .. 32000000000]
, [time] [ /time [1 .. ]]
, [burst] ,num [ .. 2000000000]
, [mode] [ :enum (packet | bit) { packet:0, bit:1 }]
 }">
匹配封包，直到達到限制速率（封包速率或位速率）。帶有此匹配器的規則會一直匹配，直到達到該限制。引數採用以下格式：`rate[/time],burst:mode`。
- `rate` - 每個時間間隔內要匹配的封包或位計數。
- `time` - 指定不能超過封包或位速率的時間間隔（可選，如果未指定則使用 1s）。
- `burst` - 要匹配的初始封包或位數量：該數量每 10ms 重新充填，因此 burst 至少應為每秒速率的 1/100。
-  `mode` - 封包或位模式。
</ArgTableRow>
<ArgTableRow arg="dst-limit" typ="super { count: num
, [time] [ /time]
, [burst] ,num
, [mode] ,enum (dst-address | dst-address-and-port | src-address | src-and-dst-addresses | addresses-and-dst-port) { dst-address:1, dst-address-and-port:3, src-address:4, src-and-dst-addresses:5, addresses-and-dst-port:7 }
, [expire] [ /time]
 }">
匹配封包，直到超過給定速率。速率定義為每個時間間隔的封包數。與 `limit` 匹配器不同，每個流都有自己的限制。流由 mode 引數定義。引數採用以下格式：`rate[/time],burst,mode[/expire]`。
- `rate` - 每個流每個時間間隔要匹配的封包計數。
- `time` - 指定每個流的封包計數速率不能超過的時間間隔（可選，如果未指定則使用 1s）。
- `burst` - 每個流要匹配的初始封包數量：每次 time/rate 增加 1，直到達到該數量。
- `mode` - 指定哪些唯一欄位定義流（src-address、dst-address、src-and-dst-address、dst-address-and-port、addresses-and-dst-port）。
- `expire` - 指定無封包的流在多久之後允許被刪除的時間間隔（可選）。
</ArgTableRow>
<ArgTableRow arg="time" typ="super { !
, start: time [0 .. 86400]
, [end] -time [0 .. 86400]
, [day] ,ubit (sun, mon, tue, wed, thu, fri, sat)
 }">根據封包的到達時間和日期建立過濾器；對於本地生成的封包，則根據離開時間和日期建立。匹配器會考慮路由器上配置的時間和時區。</ArgTableRow>
<ArgTableRow arg="random" typ="super { percent: num [1 .. 99]
 }">以給定機率隨機匹配封包。</ArgTableRow>
<ArgTableRow arg="nth" typ="super { !
, every: num [1 .. ]
, [packet] [ ,num [1 .. ]]
 }">匹配每第 n 個數據包：`nth=2,1` 將匹配每 2 個數據包中的第 1 個，因此會匹配規則所處理全部流量的 50%。</ArgTableRow>
<ArgTableRow arg="tcp-mss" typ="super { !
, min: num [0 .. 65535]
, [max] -num [0 .. 65535]
 }">匹配 IP 封包的 TCP MSS 值。</ArgTableRow>
<ArgTableRow arg="per-connection-classifier" typ="super { !
, values-to-hash: enum (src-address | dst-address | both-addresses | src-port | src-address-and-port | dst-port | dst-address-and-port | both-ports | both-addresses-and-ports) { src-address:1, dst-address:2, both-addresses:3, src-port:4, src-address-and-port:5, dst-port:8, dst-address-and-port:10, both-ports:12, both-addresses-and-ports:15 }
, [denominator] :num [1 .. ]
, [remainder] /num [0 .. ]
 }">PCC 匹配器允許將流量劃分為相等的流，並能夠將具有特定選項集的封包保留在同一個特定流中。</ArgTableRow>
<ArgTableRow arg="packet-size" typ="super { !
, min: num [ .. 65535]
, [max] -num [ .. 65535]
 }">匹配指定大小或大小範圍（以位元組為單位）的封包。</ArgTableRow>
<ArgTableRow arg="log" typ="bool">向系統日誌新增一條包含以下資料的訊息：in-interface、out-interface、src-mac、protocol、src-ip:port-&gt;dst-ip:port 以及封包長度。即使動作不是 `log`，也允許記錄封包，這對於偵錯防火牆很有用。</ArgTableRow>
<ArgTableRow arg="log-prefix" typ="string">在每條日誌訊息的開頭新增指定文字。僅在配置了 `action=log` 或 `log=yes` 時適用。</ArgTableRow>
<ArgTableRow arg="ipsec-policy" typ="super { direction: enum (in | out) { in:0, out:1 }
, [policy] ,enum (none | ipsec) { none:0, ipsec:1 }
 }">
匹配 IPsec 使用的策略。值採用以下格式：`direction, policy`。
- `in` - 在 PREROUTING、INPUT 和 FORWARD 鏈中有效。
- `out` - 在 POSTROUTING、OUTPUT 和 FORWARD 鏈中有效。
- `ipsec` - 如果封包經過 IPsec 處理，則匹配。
- `none` - 匹配不經過 IPsec 處理的封包。
</ArgTableRow>
</ArgTable>
