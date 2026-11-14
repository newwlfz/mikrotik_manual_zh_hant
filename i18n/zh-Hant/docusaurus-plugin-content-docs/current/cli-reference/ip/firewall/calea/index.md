---
sidebar_key: "cli-reference/ip/firewall/calea"
title: "calea"
sidebar_label: 'calea'
source: https://manual.mikrotik.com/docs/cli-reference/ip/firewall/calea
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/firewall/calea {#ipfirewallcalea}
**型別：** 目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="filter" typ="alt { all: enum (all) { all:0 }
, static: enum (static | dynamic)
, chain: enum (prerouting | input | forward | output | postrouting) { prerouting:1, input:2, forward:3, output:4, postrouting:5 }
 }">calea 規則的過濾配置。</ArgTableRow>
<ArgTableRow arg="chain" typ="enum (prerouting | input | forward | output | postrouting) { prerouting:1, input:2, forward:3, output:4, postrouting:5 }" mandatory="1">指定規則將新增到哪個鏈。如果輸入與已定義鏈的名稱不匹配，則會建立一個新鏈。</ArgTableRow>
<ArgTableRow arg="action" typ="enum (sniff | sniff-pc) { sniff:7, sniff-pc:8 }">
當封包與該規則匹配時要執行的操作：
- `sniff` - 嗅探該封包。
- `sniff-pc` - 嗅探該封包並將其傳送到指定的 Packet Capturer 目標。
</ArgTableRow>
<ArgTableRow arg="sniff-target" typ="ipAddr">將嗅探到的封包傳送到的 IP 地址。</ArgTableRow>
<ArgTableRow arg="sniff-target-port" typ="num">將嗅探到的封包傳送到的埠。</ArgTableRow>
<ArgTableRow arg="sniff-id" typ="num">嗅探會話的 ID。</ArgTableRow>
<ArgTableRow arg="tls-host" typ="super { !
, tls-host: string
 }">基於 TLS SNI 主機名匹配 HTTPS 流量。接受 GLOB 語法進行萬用字元匹配。如果 TLS 握手幀被分片為多個 TCP 段，匹配器將無法匹配主機名。</ArgTableRow>
<ArgTableRow arg="connection-limit" typ="super { !
, limit: num
, [netmask] ,num
 }">達到給定值後按地址或地址塊匹配連線。應將其與 `connection-state=new` 和/或 `tcp-flags=syn` 一起使用，因為該匹配器非常消耗資源。</ArgTableRow>
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
 }">匹配源等於指定 IP 或落在指定 IP 範圍內的封包。</ArgTableRow>
<ArgTableRow arg="dst-address" typ="super { !
, range: ipRange
 }">匹配目標等於指定 IP 或落在指定 IP 範圍內的封包。</ArgTableRow>
<ArgTableRow arg="fragment" typ="super { fragment: bool
 }">匹配分片封包。第一個（起始）分片不計入。如果啟用了連線跟蹤，則不會有分片，因為系統會自動組裝每個封包。僅限 IPv4。</ArgTableRow>
<ArgTableRow arg="psd" typ="super { weight-threshold: num
, [delay-threshold] ,time
, [low-port-weight] ,num
, [high-port-weight] ,num
 }">
嘗試檢測 TCP 和 UDP 掃描。引數採用以下格式：`WeightThreshold, DelayThreshold, LowPortWeight, HighPortWeight`。
- `WeightThreshold` - 來自同一主機、具有不同目標埠的最新 TCP/UDP 封包的總權重，達到該值即被視為埠掃描序列。
- `DelayThreshold` - 來自同一主機、具有不同目標埠的封包被視為可能埠掃描子序列的延遲。
- `LowPortWeight` - 具有特權目標埠（&lt;1024）的封包的權重。
- `HighPortWeight` - 具有非特權目標埠的封包的權重。僅限 IPv4。
</ArgTableRow>
<ArgTableRow arg="ipv4-options" typ="super { options: enum (strict-source-routing | loose-source-routing | no-source-routing | record-route | no-record-route | timestamp | no-timestamp | router-alert | no-router-alert | any | none) { strict-source-routing:0x1, loose-source-routing:0x2, no-source-routing:0x4, record-route:0x8, no-record-route:0x10, timestamp:0x20, no-timestamp:0x40, router-alert:0x80, no-router-alert:0x100, any:0x200, none:0x400 }
 }">
匹配 IPv4 首部選項。
- `any` - 匹配至少包含一個 IPv4 選項的封包。
- `loose-source-routing` - 匹配帶有鬆散源路由選項的封包。
- `no-record-route` - 匹配不帶記錄路由選項的封包。
- `no-router-alert` - 匹配不帶路由器警報選項的封包。
- `no-source-routing` - 匹配不帶源路由選項的封包。
- `no-timestamp` - 匹配不帶時間戳選項的封包。
- `record-route` - 匹配帶有記錄路由選項的封包。
- `router-alert` - 匹配帶有路由器警報選項的封包。
- `strict-source-routing` - 匹配帶有嚴格源路由選項的封包。
- `timestamp` - 匹配帶有時間戳的封包。僅限 IPv4。
</ArgTableRow>
<ArgTableRow arg="src-address-type" typ="super { !
, type: ubit (unicast, local, broadcast, multicast, blackhole)
 }">
匹配源地址型別：
- `unicast` - 用於點對點傳輸的 IP 地址。
- `local` - 該地址分配給路由器的某個介面。
- `broadcast` - 封包被髮送到子網中的所有裝置。
- `multicast` - 封包被轉發到定義的裝置組。
</ArgTableRow>
<ArgTableRow arg="dst-address-type" typ="super { !
, type: ubit (unicast, local, broadcast, multicast, blackhole)
 }">
匹配目標地址型別：
- `unicast` - 用於點對點傳輸的 IP 地址。
- `local` - 目標地址分配給路由器的某個介面。
- `broadcast` - 封包被髮送到子網中的所有裝置。
- `multicast` - 封包被轉發到定義的裝置組。
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
- `auth` - 匹配經過認證的 HotSpot 用戶端封包。
- `from-client` - 匹配來自 HotSpot 用戶端的封包。
- `http` - 匹配發送到 HotSpot 伺服器的 HTTP 請求。
- `local-dst` - 匹配發往 HotSpot 伺服器的封包。
- `to-client` - 匹配發送到 HotSpot 用戶端的封包。僅限 IPv4。
</ArgTableRow>
<ArgTableRow arg="address-list" typ="enum ()">要使用的地址列表名稱。當動作為 `add-dst-to-address-list` 或 `add-src-to-address-list` 時適用。</ArgTableRow>
<ArgTableRow arg="address-list-timeout" typ="alt { address-list-timeout: enum (none-dynamic | none-static) { none-dynamic:0, none-static:0xffffffff }
, address-list-timeout: time [ .. 21474836]
 }">
經過該時間間隔後，地址將從 `address-list` 引數指定的地址列表中移除。與 `add-dst-to-address-list` 或 `add-src-to-address-list` 動作一起使用。
- `none-dynamic` (`00:00:00`) 會將地址保留在地址列表中直到重啟。
- `none-static` 會將地址永久保留在地址列表中，並會包含在配置匯出/備份中。
</ArgTableRow>
<ArgTableRow arg="ttl" typ="super { mode: enum (equal | not-equal | less-than | greater-than) { equal:0, not-equal:1, less-than:2, greater-than:3 }
, [value] :num [0 .. 255]
 }">匹配封包的 TTL 值。僅限 IPv4。</ArgTableRow>
<ArgTableRow arg="connection-mark" typ="super { !
, mark: enum
 }">匹配由 mangle 設施使用特定連線標記標記的封包。如果設定了 `no-mark`，該規則將匹配任何未標記的連線。</ArgTableRow>
<ArgTableRow arg="connection-type" typ="super { !
, type: enum (ftp | pptp | h323 | sip | irc | quake3 | tftp) { ftp:0, pptp:1, h323:2, sip:3, irc:4, quake3:5, tftp:6 }
 }">根據連線跟蹤 helper 的資訊匹配來自相關連線的封包。必須在 `/ip/firewall/service-port` 下啟用相關的連線 helper。</ArgTableRow>
<ArgTableRow arg="connection-bytes" typ="super { from: num
, [to] -num
 }">僅當透過特定連線傳輸了給定數量的位元組時才匹配封包。0 表示無限，例如 `connection-bytes=2000000-0` 表示如果透過相關連線傳輸了超過 2MB 的資料，則規則匹配。</ArgTableRow>
<ArgTableRow arg="connection-rate" typ="super { !
, from: num
, [to] -num
 }">允許基於連線的當前速度捕獲流量。</ArgTableRow>
<ArgTableRow arg="routing-mark" typ="super { !
, mark: enum ()
 }">匹配由 mangle 設施使用特定路由標記標記的封包。</ArgTableRow>
<ArgTableRow arg="in-interface" typ="super { !
, interface: iface_enum
 }">封包進入路由器時所使用的介面。</ArgTableRow>
<ArgTableRow arg="out-interface" typ="super { !
, interface: iface_enum
 }">封包離開路由器時所使用的介面。</ArgTableRow>
<ArgTableRow arg="in-interface-list" typ="super { !
, interface-list: enum
 }">介面列表中定義的介面集合。作用與 `in-interface` 相同。</ArgTableRow>
<ArgTableRow arg="out-interface-list" typ="super { !
, interface-list: enum
 }">介面列表中定義的介面集合。作用與 `out-interface` 相同。</ArgTableRow>
<ArgTableRow arg="in-bridge-port" typ="super { !
, interface: iface_enum
 }">如果傳入介面是網橋，則為封包進入路由器時實際使用的介面。僅在橋接設定中啟用了 `use-ip-firewall` 時有效。</ArgTableRow>
<ArgTableRow arg="out-bridge-port" typ="super { !
, interface: iface_enum
 }">如果傳出介面是網橋，則為封包離開路由器時實際使用的介面。僅在橋接設定中啟用了 `use-ip-firewall` 時有效。</ArgTableRow>
<ArgTableRow arg="in-bridge-port-list" typ="super { !
, interface-list: enum
 }">介面列表中定義的介面集合。作用與 `in-bridge-port` 相同。</ArgTableRow>
<ArgTableRow arg="out-bridge-port-list" typ="super { !
, interface-list: enum
 }">介面列表中定義的介面集合。作用與 `out-bridge-port` 相同。</ArgTableRow>
<ArgTableRow arg="packet-mark" typ="super { !
, mark: enum
 }">匹配由 mangle 設施使用特定封包標記標記的封包。如果設定了 `no-mark`，該規則將匹配任何未標記的封包。</ArgTableRow>
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
 }">匹配入口封包的優先順序。優先順序可能來自 VLAN、WMM、DSCP 或 MPLS EXP 位。</ArgTableRow>
<ArgTableRow arg="priority" typ="super { !
, priority: num [0 .. 63]
 }">匹配設定新優先順序後封包的優先順序。優先順序可能來自 VLAN、WMM、DSCP、MPLS EXP 位，或來自使用 set-priority 動作設定的優先順序。</ArgTableRow>
<ArgTableRow arg="dscp" typ="super { !
, dscp: num [0 .. 63]
 }">匹配 DSCP IP 首部欄位。</ArgTableRow>
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
匹配封包，直到達到有限速率（封包速率或位元速率）。帶有此匹配器的規則將一直匹配，直到達到該限制。引數採用以下格式：`rate[/time],burst:mode`。
- `rate` - 每個時間間隔要匹配的封包數或位元數。
- `time` - 指定不能超過封包或位元速率的時間間隔（可選，如果未指定則使用 1s）。
- `burst` - 要匹配的初始封包數或位元數：該數字每 10ms 補充一次，因此 burst 應至少為每秒速率的 1/100。
-  `mode` - 封包或位元模式。
</ArgTableRow>
<ArgTableRow arg="dst-limit" typ="super { count: num
, [time] [ /time]
, [burst] ,num
, [mode] ,enum (dst-address | dst-address-and-port | src-address | src-and-dst-addresses | addresses-and-dst-port) { dst-address:1, dst-address-and-port:3, src-address:4, src-and-dst-addresses:5, addresses-and-dst-port:7 }
, [expire] [ /time]
 }">
匹配封包，直到超過給定速率。速率定義為每個時間間隔的封包數。與 `limit` 匹配器不同，每個流都有自己的限制。流由 mode 引數定義。引數採用以下格式：`rate[/time],burst,mode[/expire]`。
- `rate` - 每個流每個時間間隔要匹配的封包數。
- `time` - 指定每個流的封包計數速率不能超過的時間間隔（可選，如果未指定則使用 1s）。
- `burst` - 每個流要匹配的初始封包數：該數字每 time/rate 增加一，直到達到此數字。
- `mode` - 指定哪些唯一欄位定義流（src-address、dst-address、src-and-dst-address、dst-address-and-port、addresses-and-dst-port）。
- `expire` - 指定無封包的流在多長時間後允許被刪除（可選）。
</ArgTableRow>
<ArgTableRow arg="time" typ="super { !
, start: time [0 .. 86400]
, [end] -time [0 .. 86400]
, [day] ,ubit (sun, mon, tue, wed, thu, fri, sat)
 }">根據封包的到達時間和日期建立過濾器；對於本地生成的封包，則根據離開時間和日期建立。該匹配器會考慮路由器上配置的時間和時區。</ArgTableRow>
<ArgTableRow arg="random" typ="super { percent: num [1 .. 99]
 }">以給定機率隨機匹配封包。</ArgTableRow>
<ArgTableRow arg="nth" typ="super { !
, every: num [1 .. ]
, [packet] [ ,num [1 .. ]]
 }">匹配每第 n 個數據包：`nth=2,1` 將匹配每 2 個數據包中的第一個，因此會匹配規則所匹配全部流量的 50%。</ArgTableRow>
<ArgTableRow arg="tcp-mss" typ="super { !
, min: num [0 .. 65535]
, [max] -num [0 .. 65535]
 }">匹配 IP 封包的 TCP MSS 值。</ArgTableRow>
<ArgTableRow arg="per-connection-classifier" typ="super { !
, values-to-hash: enum (src-address | dst-address | both-addresses | src-port | src-address-and-port | dst-port | dst-address-and-port | both-ports | both-addresses-and-ports) { src-address:1, dst-address:2, both-addresses:3, src-port:4, src-address-and-port:5, dst-port:8, dst-address-and-port:10, both-ports:12, both-addresses-and-ports:15 }
, [denominator] :num [1 .. ]
, [remainder] /num [0 .. ]
 }">PCC 匹配器允許將流量劃分為相等的流，並能夠將具有特定選項集的封包保留在某個特定流中。</ArgTableRow>
<ArgTableRow arg="packet-size" typ="super { !
, min: num [ .. 65535]
, [max] -num [ .. 65535]
 }">匹配指定大小或大小範圍（以位元組為單位）的封包。</ArgTableRow>
<ArgTableRow arg="log" typ="bool">向系統日誌新增一條訊息，其中包含以下資料：in-interface、out-interface、src-mac、protocol、src-ip:port-&gt;dst-ip:port 以及封包長度。即使動作不是 `log`，也允許記錄封包，這對於偵錯防火牆很有用。</ArgTableRow>
<ArgTableRow arg="log-prefix" typ="string">在每條日誌訊息的開頭新增指定文字。當配置了 `action=log` 或 `log=yes` 時適用。</ArgTableRow>
<ArgTableRow arg="ipsec-policy" typ="super { direction: enum (in | out) { in:0, out:1 }
, [policy] ,enum (none | ipsec) { none:0, ipsec:1 }
 }">
匹配 IPsec 使用的策略。值採用以下格式：`direction, policy`。
- `in` - 在 PREROUTING、INPUT 和 FORWARD 鏈中有效。
- `out` - 在 POSTROUTING、OUTPUT 和 FORWARD 鏈中有效。
- `ipsec` - 如果封包需要經過 IPsec 處理，則匹配。
- `none` - 匹配不經過 IPsec 處理的封包。
</ArgTableRow>
</ArgTable>
