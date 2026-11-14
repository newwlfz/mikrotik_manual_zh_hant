---
sidebar_key: "cli-reference/ip/firewall/nat/index"
sidebar_position: 1
title: "nat"
sidebar_label: 'nat'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/firewall/nat
captured_at: '2026-11-01T21:24:00+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/firewall/nat {#ipfirewallnat}
**型別：** 目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="all" typ="switch"></ArgTableRow>
<ArgTableRow arg="static" typ="switch"></ArgTableRow>
<ArgTableRow arg="dynamic" typ="switch"></ArgTableRow>
<ArgTableRow arg="chain" typ="enum" mandatory="1">指定規則將新增到哪個鏈。如果輸入與已定義鏈的名稱不匹配，則會建立一個新鏈。</ArgTableRow>
<ArgTableRow arg="action" typ="enum (accept | jump | return | log | passthrough | add-src-to-address-list | add-dst-to-address-list | src-nat | masquerade | dst-nat | redirect | same | netmap | endpoint-independent-nat | socksify) { accept:0, jump:1, return:2, log:3, passthrough:4, add-src-to-address-list:5, add-dst-to-address-list:6, src-nat:20, masquerade:21, dst-nat:22, redirect:23, same:24, netmap:25, endpoint-independent-nat:26, socksify:27 }">
如果封包被規則匹配，則要執行的動作：
- `accept` - 接受封包。封包不會傳遞給下一條防火牆規則。
- `add-dst-to-address-list` - 將目標地址新增到由 `address-list` 引數指定的地址列表。
- `add-src-to-address-list` - 將源地址新增到由 `address-list` 引數指定的地址列表。
- `jump` - 跳轉到由 `jump-target` 引數值指定的使用者定義鏈。
- `log` - 向系統日誌新增一條包含以下資料的訊息：in-interface、out-interface、src-mac、protocol、src-ip:port-&gt;dst-ip:port 以及封包長度。封包匹配後，會傳遞給列表中的下一條規則，類似於 `passthrough`。
- `passthrough` - 如果封包被規則匹配，則增加計數器並轉到下一條規則（對統計有用）。
- `return` - 將控制權返回到發生跳轉的鏈。
- `src-nat` - 用 `to-addresses` 和 `to-ports` 引數指定的值替換 IP 封包的源地址。
- `masquerade` - 用 `to-ports` 引數指定的埠替換 IP 封包的源埠，並用路由設施確定的 IP 替換 IP 封包的源地址。
- `dst-nat` - 用 `to-addresses` 和 `to-ports` 引數指定的值替換 IP 封包的目標地址和/或埠。
- `redirect` - 用 `to-ports` 引數指定的埠替換 IP 封包的目標埠，並將目標地址替換為虛擬或物理入介面（接收封包的介面）的地址。
- `same` - 為特定用戶端在來自所提供範圍的每個連線中提供相同的源/目標 IP 地址。這最常用於期望同一用戶端的多個連線使用相同用戶端地址的服務。
- `netmap` - 建立一組 IP 地址到另一組 IP 地址的靜態 1:1 對映。常用於將公網 IP 地址分配給專用網路中的主機。
- `endpoint-independent-nat` - 使用端點無關對映和過濾。僅適用於 UDP 協定。
- `socksify` - 透過 SOCKS 代理伺服器路由防火牆規則指定的流量。需要 `socks5-server` 和 `socks5-port` 引數，或 `socksify-service` 引數。[相關 socksify 資訊](../../../../network-management/socks/socksify.md)
</ArgTableRow>
<ArgTableRow arg="jump-target" typ="enum ()">要跳轉到的目標鏈名稱。僅當 `action=jump` 時適用。</ArgTableRow>
<ArgTableRow arg="to-addresses" typ="super { min: ipRange
 }">用指定地址替換原始地址。當動作為 `dst-nat`、`netmap`、`same`、`src-nat` 時適用。</ArgTableRow>
<ArgTableRow arg="to-ports" typ="super { min: num [0 .. 65535]
, [max] -num [0 .. 65535]
 }">用指定埠替換原始埠。當動作為 `dst-nat`、`redirect`、`masquerade`、`netmap`、`same`、`src-nat` 時適用。</ArgTableRow>
<ArgTableRow arg="same-not-by-dst" typ="bool">指定在選擇新源 IP 地址時是否考慮目標 IP 地址。僅當 `action=same` 時適用。</ArgTableRow>
<ArgTableRow arg="randomise-ports" typ="bool">隨機化埠轉換。</ArgTableRow>
<ArgTableRow arg="socksify-service" typ="enum">SOCKS 服務名稱。</ArgTableRow>
<ArgTableRow arg="socks5-server" typ="ipAddr">SOCKS5 伺服器的 IP 地址。</ArgTableRow>
<ArgTableRow arg="socks5-port" typ="num">SOCKS5 伺服器的埠。</ArgTableRow>
<ArgTableRow arg="connection-limit" typ="super { !
, limit: num
, [netmask] ,num
 }">在達到給定值後按地址或地址塊匹配連線。應將其與 `connection-state=new` 和/或 `tcp-flags=syn` 一起使用，因為該匹配器非常消耗資源。</ArgTableRow>
<ArgTableRow arg="layer7-protocol" typ="super { !
, protocol: enum
 }">在 layer7 協定選單中定義的 Layer7 過濾器名稱。</ArgTableRow>
<ArgTableRow arg="realm" typ="super { !
, realm: num
 }">匹配路由 realm。僅 IPv4。</ArgTableRow>
<ArgTableRow arg="protocol" typ="super { !
, protocol: enum ()
 }">匹配由協定名稱或編號指定的特定 IP 協定。</ArgTableRow>
<ArgTableRow arg="src-address" typ="super { !
, range: ipRange
 }">匹配源等於指定 IP 或落入指定 IP 範圍的封包。</ArgTableRow>
<ArgTableRow arg="dst-address" typ="super { !
, range: ipRange
 }">匹配目標等於指定 IP 或落入指定 IP 範圍的封包。</ArgTableRow>
<ArgTableRow arg="fragment" typ="super { fragment: bool
 }">匹配分片封包。第一個（起始）分片不計入。如果啟用了連線跟蹤，則不會出現分片，因為系統會自動重組每個封包。僅 IPv4。</ArgTableRow>
<ArgTableRow arg="psd" typ="super { weight-threshold: num
, [delay-threshold] ,time
, [low-port-weight] ,num
, [high-port-weight] ,num
 }">
嘗試檢測 TCP 和 UDP 掃描。引數採用以下格式：`WeightThreshold, DelayThreshold, LowPortWeight, HighPortWeight`。
- `WeightThreshold` - 來自同一主機、具有不同目標埠的最新 TCP/UDP 封包被視為埠掃描序列的總權重。
- `DelayThreshold` - 來自同一主機、具有不同目標埠的封包被視為可能的埠掃描子序列的延遲。
- `LowPortWeight` - 具有特權目標埠（&lt;1024）的封包的權重。
- `HighPortWeight` - 具有非特權目標埠的封包的權重。僅 IPv4。
</ArgTableRow>
<ArgTableRow arg="ipv4-options" typ="super { options: enum (strict-source-routing | loose-source-routing | no-source-routing | record-route | no-record-route | timestamp | no-timestamp | router-alert | no-router-alert | any | none) { strict-source-routing:0x1, loose-source-routing:0x2, no-source-routing:0x4, record-route:0x8, no-record-route:0x10, timestamp:0x20, no-timestamp:0x40, router-alert:0x80, no-router-alert:0x100, any:0x200, none:0x400 }
 }">
匹配 IPv4 報頭選項。
- `any` - 匹配至少帶有一個 IPv4 選項的封包。
- `loose-source-routing` - 匹配帶有寬鬆源路由選項的封包。
- `no-record-route` - 匹配不帶記錄路由選項的封包。
- `no-router-alert` - 匹配不帶路由器告警選項的封包。
- `no-source-routing` - 匹配不帶源路由選項的封包。
- `no-timestamp` - 匹配不帶時間戳選項的封包。
- `record-route` - 匹配帶有記錄路由選項的封包。
- `router-alert` - 匹配帶有路由器告警選項的封包。
- `strict-source-routing` - 匹配帶有嚴格源路由選項的封包。
- `timestamp` - 匹配帶有時間戳的封包。僅 IPv4。
</ArgTableRow>
<ArgTableRow arg="src-address-type" typ="super { !
, type: ubit (unicast, local, broadcast, multicast, blackhole)
 }">
匹配源地址型別：
- `unicast` - 用於點對點傳輸的 IP 地址。
- `local` - 該地址分配給路由器的某個介面。
- `broadcast` - 封包傳送到子網中的所有裝置。
- `multicast` - 封包轉發到定義的裝置組。
</ArgTableRow>
<ArgTableRow arg="dst-address-type" typ="super { !
, type: ubit (unicast, local, broadcast, multicast, blackhole)
 }">
匹配目標地址型別：
- `unicast` - 用於點對點傳輸的 IP 地址。
- `local` - 目標地址分配給路由器的某個介面。
- `broadcast` - 封包傳送到子網中的所有裝置。
- `multicast` - 封包轉發到定義的裝置組。
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
- `auth` - 匹配已認證 HotSpot 用戶端的封包。
- `from-client` - 匹配來自 HotSpot 用戶端的封包。
- `http` - 匹配發送到 HotSpot 伺服器的 HTTP 請求。
- `local-dst` - 匹配發往 HotSpot 伺服器的封包。
- `to-client` - 匹配發送到 HotSpot 用戶端的封包。僅 IPv4。
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
 }">匹配封包 TTL 值。僅 IPv4。</ArgTableRow>
<ArgTableRow arg="connection-mark" typ="super { !
, mark: enum
 }">匹配由 mangle 功能用特定連線標記標記的封包。如果設定了 `no-mark`，該規則將匹配任何未標記的連線。</ArgTableRow>
<ArgTableRow arg="connection-type" typ="super { !
, type: enum (ftp | pptp | h323 | sip | irc | quake3 | tftp) { ftp:0, pptp:1, h323:2, sip:3, irc:4, quake3:5, tftp:6 }
 }">根據連線跟蹤 helper 提供的資訊，匹配來自相關連線的封包。必須在 `/ip/firewall/service-port` 下啟用相關的連線 helper。</ArgTableRow>
<ArgTableRow arg="connection-bytes" typ="super { from: num
, [to] -num
 }">僅當透過特定連線傳輸了給定數量的位元組時才匹配封包。0 表示無限，例如 `connection-bytes=2000000-0` 表示如果透過相關連線傳輸了超過 2MB，則規則匹配。</ArgTableRow>
<ArgTableRow arg="connection-rate" typ="super { !
, from: num
, [to] -num
 }">允許根據連線的當前速度捕獲流量。</ArgTableRow>
<ArgTableRow arg="routing-mark" typ="super { !
, mark: enum ()
 }">匹配由 mangle 功能用特定路由標記標記的封包。</ArgTableRow>
<ArgTableRow arg="in-interface" typ="super { !
, interface: iface_enum
 }">封包進入路由器時所經過的介面。</ArgTableRow>
<ArgTableRow arg="out-interface" typ="super { !
, interface: iface_enum
 }">封包離開路由器時所經過的介面。</ArgTableRow>
<ArgTableRow arg="in-interface-list" typ="super { !
, interface-list: enum
 }">在介面列表中定義的介面集合。工作方式與 `in-interface` 相同。</ArgTableRow>
<ArgTableRow arg="out-interface-list" typ="super { !
, interface-list: enum
 }">在介面列表中定義的介面集合。工作方式與 `out-interface` 相同。</ArgTableRow>
<ArgTableRow arg="in-bridge-port" typ="super { !
, interface: iface_enum
 }">如果入介面是網橋，則為封包進入路由器時實際經過的介面。僅當在網橋設定中啟用了 `use-ip-firewall` 時有效。</ArgTableRow>
<ArgTableRow arg="out-bridge-port" typ="super { !
, interface: iface_enum
 }">如果出介面是網橋，則為封包離開路由器時實際經過的介面。僅當在網橋設定中啟用了 `use-ip-firewall` 時有效。</ArgTableRow>
<ArgTableRow arg="in-bridge-port-list" typ="super { !
, interface-list: enum
 }">在介面列表中定義的介面集合。工作方式與 `in-bridge-port` 相同。</ArgTableRow>
<ArgTableRow arg="out-bridge-port-list" typ="super { !
, interface-list: enum
 }">在介面列表中定義的介面集合。工作方式與 `out-bridge-port` 相同。</ArgTableRow>
<ArgTableRow arg="packet-mark" typ="super { !
, mark: enum
 }">匹配由 mangle 功能用特定封包標記標記的封包。如果設定了 `no-mark`，該規則將匹配任何未標記的封包。</ArgTableRow>
<ArgTableRow arg="src-port" typ="super { !
, port: multi { range: range [ .. 65535]
 }
 }">源埠和源埠範圍的列表。僅當協定為 TCP 或 UDP 時適用。</ArgTableRow>
<ArgTableRow arg="dst-port" typ="super { !
, port: multi { range: range [ .. 65535]
 }
 }">目標埠號或埠號範圍的列表。</ArgTableRow>
<ArgTableRow arg="port" typ="super { !
, port: multi { range: range [ .. 65535]
 }
 }">如果任何（源或目標）埠匹配指定的埠或埠範圍列表，則匹配。僅當 `protocol` 為 TCP 或 UDP 時適用。</ArgTableRow>
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
 }">匹配入站封包的優先順序。優先順序可來自 VLAN、WMM、DSCP 或 MPLS EXP 位。</ArgTableRow>
<ArgTableRow arg="priority" typ="super { !
, priority: num [0 .. 63]
 }">匹配設定新優先順序後的封包優先順序。優先順序可來自 VLAN、WMM、DSCP、MPLS EXP 位，或來自透過 set-priority 動作設定的優先順序。</ArgTableRow>
<ArgTableRow arg="dscp" typ="super { !
, dscp: num [0 .. 63]
 }">匹配 DSCP IP 報頭欄位。</ArgTableRow>
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
匹配不超過限制速率（封包速率或位元速率）的封包。帶有此匹配器的規則會一直匹配，直到達到該限制。引數採用以下格式：`rate[/time],burst:mode`。
- `rate` - 每個時間間隔要匹配的封包數或位元數。
- `time` - 指定不能超過封包速率或位元速率的時間間隔（可選，未指定時將使用 1s）。
- `burst` - 要匹配的初始封包數或位元數：該數值每 10ms 重新補充，因此 burst 應至少為每秒速率的 1/100。
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
- `time` - 指定每個流的封包計數速率不能超過的時間間隔（可選，未指定時將使用 1s）。
- `burst` - 每個流要匹配的初始封包數：該數值每隔 time/rate 增加一，直到達到該數值。
- `mode` - 指定哪些唯一欄位定義流（src-address、dst-address、src-and-dst-address、dst-address-and-port、addresses-and-dst-port）。
- `expire` - 指定無封包的流在多長時間後允許被刪除（可選）。
</ArgTableRow>
<ArgTableRow arg="time" typ="super { !
, start: time [0 .. 86400]
, [end] -time [0 .. 86400]
, [day] ,ubit (sun, mon, tue, wed, thu, fri, sat)
 }">根據封包的到達時間和日期建立過濾器；對於本地生成的封包，則根據離開時間和日期建立。該匹配器會考慮路由器上配置的時間和時區。</ArgTableRow>
<ArgTableRow arg="random" typ="super { percent: num [1 .. 99]
 }">按給定機率隨機匹配封包。</ArgTableRow>
<ArgTableRow arg="nth" typ="super { !
, every: num [1 .. ]
, [packet] [ ,num [1 .. ]]
 }">匹配每第 n 個數據包：`nth=2,1` 將匹配每 2 個數據包中的第 1 個，因此匹配該規則的所有流量中的 50%。</ArgTableRow>
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
<ArgTableRow arg="log" typ="bool">向系統日誌新增一條包含以下資料的訊息：in-interface、out-interface、src-mac、protocol、src-ip:port-&gt;dst-ip:port 以及封包長度。即使動作不是 `log` 也允許記錄封包日誌，這對於偵錯防火牆很有用。</ArgTableRow>
<ArgTableRow arg="log-prefix" typ="string">在每條日誌訊息開頭新增指定文字。當配置了 `action=log` 或 `log=yes` 時適用。</ArgTableRow>
<ArgTableRow arg="ipsec-policy" typ="super { direction: enum (in | out) { in:0, out:1 }
, [policy] ,enum (none | ipsec) { none:0, ipsec:1 }
 }">
匹配 IPsec 使用的策略。值採用以下格式：`direction, policy`。
- `in` - 在 PREROUTING、INPUT 和 FORWARD 鏈中有效。
- `out` - 在 POSTROUTING、OUTPUT 和 FORWARD 鏈中有效。
- `ipsec` - 如果封包需要經過 IPsec 處理，則匹配。
- `none` - 匹配不需要經過 IPsec 處理的封包。
</ArgTableRow>
</ArgTable>
