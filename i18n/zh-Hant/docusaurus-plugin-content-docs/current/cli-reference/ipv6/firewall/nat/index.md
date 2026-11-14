---
sidebar_key: "cli-reference/ipv6/firewall/nat"
title: "nat"
sidebar_label: 'nat'
source: https://manual.mikrotik.com/docs/cli-reference/ipv6/firewall/nat
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ipv6/firewall/nat {#ipv6firewallnat}
**型別：** 目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="static" typ="switch"></ArgTableRow>
<ArgTableRow arg="dynamic" typ="switch"></ArgTableRow>
<ArgTableRow arg="chain" typ="enum" mandatory="1">指定規則將被新增到哪個鏈。如果輸入的內容與已定義鏈的名稱不匹配，則會建立一個新鏈。</ArgTableRow>
<ArgTableRow arg="action" typ="enum (accept | jump | return | log | passthrough | add-src-to-address-list | add-dst-to-address-list | src-nat | masquerade | dst-nat | redirect | netmap) { accept:0, jump:1, return:2, log:3, passthrough:4, add-src-to-address-list:5, add-dst-to-address-list:6, src-nat:20, masquerade:21, dst-nat:22, redirect:23, netmap:25 }">當封包與該規則匹配時要執行的動作：`accept` - 接受該封包。封包不會被傳遞給下一條防火牆規則。  `add-dst-to-address-list` - 把目標地址新增到由 `address-list` 引數指定的地址列表中。  `add-src-to-address-list` - 把源地址新增到由 `address-list` 引數指定的地址列表中。  `dst-nat` - 執行目標 NAT。  `jump` - 跳轉到由 `jump-target` 引數的值指定的使用者自定義鏈。  `log` - 向系統日誌新增一條訊息，包含以下資料：in-interface、out-interface、src-mac、protocol、src-ip:port->dst-ip:port 以及封包長度。封包匹配後會被傳遞到列表中的下一條規則，類似於 `passthrough`。  `masquerade` - 對源地址進行偽裝。  `netmap` - 建立靜態的 1:1 NAT 對映。  `passthrough` - 如果封包與該規則匹配，則增加計數器並轉到下一條規則（用於統計）。  `redirect` - 將封包重定向到路由器。  `return` - 將控制權交回發生跳轉的那個鏈。  `src-nat` - 執行源 NAT。</ArgTableRow>
<ArgTableRow arg="jump-target" typ="enum ()">要跳轉到的目標鏈的名稱。僅在 `action=jump` 時適用。</ArgTableRow>
<ArgTableRow arg="to-address" typ="super { address: ip6Prefix
 }">要轉換成的 IPv6 地址。</ArgTableRow>
<ArgTableRow arg="to-ports" typ="super { min: num [0 .. 65535]
, [max] -num [0 .. 65535]
 }">要轉換成的埠或埠範圍。</ArgTableRow>
<ArgTableRow arg="connection-state" typ="super { !
, state: ubit (invalid, established, related, new, untracked)
 }">解釋特定封包的連線跟蹤分析資料：`established` - 屬於已存在連線的封包。  `invalid` - 在連線跟蹤中沒有確定狀態的封包（通常是嚴重亂序的封包、序列號/ack 號錯誤的封包，或路由器資源過度使用的情況）。無效封包不會參與 NAT，並且在路由時仍會保留原始源 IP 地址。你應該在防火牆 filter 的 forward 和 input 鏈中丟棄所有 `connection-state=invalid` 的封包。  `new` - 該封包已開始一個新連線，或者以其他方式關聯到一個尚未在兩個方向上都看到封包的連線。  `related` - 與現有連線相關但不屬於該連線的封包，例如 ICMP 錯誤報文或開啟 FTP 資料連線的封包。  `untracked` - 在防火牆 RAW 表中被設定為繞過連線跟蹤的封包。</ArgTableRow>
<ArgTableRow arg="connection-limit" typ="super { !
, limit: num
, [prefix-len] ,num [0 .. 128]
 }">在達到給定值後，按地址或地址塊匹配連線數。應將其與 `connection-state=new` 和/或 `tcp-flags=syn` 一起使用，因為該匹配器非常消耗資源。</ArgTableRow>
<ArgTableRow arg="protocol" typ="super { !
, protocol: enum (icmpv6) { icmpv6:58 }
 }">匹配由協定名稱或編號指定的特定 IP 協定。</ArgTableRow>
<ArgTableRow arg="src-address" typ="super { !
, address: ip6Prefix
 }">匹配源等於指定 IP 或落在指定 IP 範圍內的封包。</ArgTableRow>
<ArgTableRow arg="dst-address" typ="super { !
, address: ip6Prefix
 }">匹配目標等於指定 IP 或落在指定 IP 範圍內的封包。</ArgTableRow>
<ArgTableRow arg="src-address-list" typ="super { !
, address-list: enum
 }">將封包的源地址與使用者定義的地址列表進行匹配。僅支援一個列表。</ArgTableRow>
<ArgTableRow arg="dst-address-list" typ="super { !
, address-list: enum
 }">將封包的目標地址與使用者定義的地址列表進行匹配。僅支援一個列表。</ArgTableRow>
<ArgTableRow arg="address-list" typ="enum ()">要使用的地址列表的名稱。當動作為 `add-dst-to-address-list` 或 `add-src-to-address-list` 時適用。</ArgTableRow>
<ArgTableRow arg="address-list-timeout" typ="alt { address-list-timeout: enum (none-dynamic | none-static) { none-dynamic:0, none-static:0xffffffff }
, address-list-timeout: time [ .. 21474836]
 }">
在 `add-src-to-address-list` 或 `add-dst-to-address-list` 動作新增地址後，該地址在 `address-list` 中保留多長時間。指定時間時，規則會新增一個動態條目（`D`），路由器會在時間結束後將其移除；規則每次新的匹配都會將時間重設為其完整值。最大值為 `35w3d13h13m56s`。如果地址已經是列表中的靜態條目，則保持靜態。
- `none-dynamic` (`0s`) - 新增一個不帶超時的動態條目。它不會儲存到配置中，重啟後會清除。
- `none-static` - 新增一個靜態條目。它會儲存到配置和匯出中，並且在重啟後仍會保留，直到你將其移除。
</ArgTableRow>
<ArgTableRow arg="src-address-type" typ="super { !
, type: ubit (unicast, local, anycast, multicast, unreachable)
 }">匹配源地址型別：`unicast` - 用於點對點傳輸的 IP 地址。  `local` - 該地址被分配給路由器的某個介面。  `anycast` - 傳送到組內最近節點的封包。  `multicast` - 封包被轉發到一組已定義的裝置。  `unreachable` - 該地址不可達。</ArgTableRow>
<ArgTableRow arg="dst-address-type" typ="super { !
, type: ubit (unicast, local, anycast, multicast, unreachable)
 }">匹配目標地址型別：`unicast` - 用於點對點傳輸的 IP 地址。  `local` - 目標地址被分配給路由器的某個介面。  `anycast` - 傳送到組內最近節點的封包。  `multicast` - 封包被轉發到一組已定義的裝置。  `unreachable` - 該地址不可達。</ArgTableRow>
<ArgTableRow arg="headers" typ="super { !
, type: ubit (hop, dst, route, frag, ah, esp, none, proto)
, [mode] [ :enum (exact | contains) { exact:0, contains:1 }]
 }">匹配 IPv6 下一頭部。由 `mode` 引數控制，可以進行兩種型別的頭部匹配：`contains` - 軟匹配，至少匹配所選的頭部。  `exact` - 精確匹配所選頭部的集合。</ArgTableRow>
<ArgTableRow arg="tcp-flags" typ="super { !,
, flags: multi { array-id, array-id, flag: super { !
, flag: enum (fin | syn | rst | psh | ack | urg | ece | cwr) { fin:0, syn:1, rst:2, psh:3, ack:4, urg:5, ece:6, cwr:7 }
 }
 }
 }">匹配指定的 TCP 標誌：`ack` - 確認資料。  `cwr` - 擁塞視窗已減小。  `ece` - ECN-echo 標誌（顯式擁塞通知）。  `fin` - 關閉連線。  `psh` - 推送功能。  `rst` - 重設連線。  `syn` - 新連線。  `urg` - 緊急資料。</ArgTableRow>
<ArgTableRow arg="hop-limit" typ="super { mode: enum (equal | not-equal | less-than | greater-than) { equal:0, not-equal:1, less-than:2, greater-than:3 }
, [value] :num [0 .. 255]
 }">匹配 IPv6 頭部中的跳數限制欄位。</ArgTableRow>
<ArgTableRow arg="connection-mark" typ="super { !
, mark: enum
 }">匹配由 mangle 功能標記了特定連線標記的封包。如果設定了 `no-mark`，該規則將匹配任何未標記的連線。</ArgTableRow>
<ArgTableRow arg="connection-type" typ="super { !
, type: enum (ftp | pptp | h323 | sip | irc | quake3 | tftp) { ftp:0, pptp:1, h323:2, sip:3, irc:4, quake3:5, tftp:6 }
 }">基於連線跟蹤 helper 提供的資訊，匹配來自相關連線的封包。必須在 `/ip/firewall/service-port` 下啟用相關的連線 helper。</ArgTableRow>
<ArgTableRow arg="connection-bytes" typ="super { from: num
, [to] -num
 }">僅當透過該特定連線傳輸的位元組數達到給定值時匹配封包。0 表示無窮大，例如 `connection-bytes=2000000-0` 表示如果透過相關連線傳輸超過 2MB，則該規則匹配。</ArgTableRow>
<ArgTableRow arg="connection-rate" typ="super { !
, from: num
, [to] -num
 }">允許基於連線的當前速度捕獲流量。</ArgTableRow>
<ArgTableRow arg="routing-mark" typ="super { !
, mark: enum ()
 }">匹配由 mangle 功能標記了特定路由標記的封包。</ArgTableRow>
<ArgTableRow arg="in-interface" typ="super { !
, interface: iface_enum
 }">封包進入路由器時所經過的介面。</ArgTableRow>
<ArgTableRow arg="out-interface" typ="super { !
, interface: iface_enum
 }">封包離開路由器時所經過的介面。</ArgTableRow>
<ArgTableRow arg="in-interface-list" typ="super { !
, interface-list: enum
 }">在介面列表中定義的介面集合。作用與 `in-interface` 相同。</ArgTableRow>
<ArgTableRow arg="out-interface-list" typ="super { !
, interface-list: enum
 }">在介面列表中定義的介面集合。作用與 `out-interface` 相同。</ArgTableRow>
<ArgTableRow arg="in-bridge-port" typ="super { !
, interface: iface_enum
 }">如果入介面是網橋，則表示封包進入路由器時實際使用的介面。僅在網橋設定中啟用了 `use-ip-firewall` 時有效。</ArgTableRow>
<ArgTableRow arg="out-bridge-port" typ="super { !
, interface: iface_enum
 }">如果出介面是網橋，則表示封包離開路由器時實際使用的介面。僅在網橋設定中啟用了 `use-ip-firewall` 時有效。</ArgTableRow>
<ArgTableRow arg="in-bridge-port-list" typ="super { !
, interface-list: enum
 }">在介面列表中定義的介面集合。作用與 `in-bridge-port` 相同。</ArgTableRow>
<ArgTableRow arg="out-bridge-port-list" typ="super { !
, interface-list: enum
 }">在介面列表中定義的介面集合。作用與 `out-bridge-port` 相同。</ArgTableRow>
<ArgTableRow arg="packet-mark" typ="super { !
, mark: enum
 }">匹配由 mangle 功能標記了特定封包標記的封包。如果設定了 `no-mark`，該規則將匹配任何未標記的封包。</ArgTableRow>
<ArgTableRow arg="src-port" typ="super { !
, port: multi { range: range [ .. 65535]
 }
 }">源埠及源埠範圍的列表。僅在協定為 TCP 或 UDP 時適用。</ArgTableRow>
<ArgTableRow arg="dst-port" typ="super { !
, port: multi { range: range [ .. 65535]
 }
 }">目標埠號或埠號範圍的列表。</ArgTableRow>
<ArgTableRow arg="port" typ="super { !
, port: multi { range: range [ .. 65535]
 }
 }">如果任意（源或目標）埠與指定的埠或埠範圍列表匹配，則匹配。僅在 `protocol` 為 TCP 或 UDP 時適用。</ArgTableRow>
<ArgTableRow arg="icmp-options" typ="super { !
, type: num [0 .. 255]
, [code] [ :range [ .. 255]]
 }">匹配 ICMP 的 type:code 欄位。</ArgTableRow>
<ArgTableRow arg="src-mac-address" typ="super { !
, address: macAddr
 }">匹配封包的源 MAC 地址。</ArgTableRow>
<ArgTableRow arg="content" typ="super { !
, content: string
 }">匹配包含指定文字的封包。</ArgTableRow>
<ArgTableRow arg="ingress-priority" typ="super { !
, ingress-priority: num [0 .. 63]
 }">匹配入向封包的優先順序。優先順序可能來自 VLAN、WMM、DSCP 或 MPLS EXP 位。</ArgTableRow>
<ArgTableRow arg="priority" typ="super { !
, priority: num [0 .. 63]
 }">在設定新優先順序之後匹配封包的優先順序。優先順序可能來自 VLAN、WMM、DSCP、MPLS EXP 位，或來自透過 set-priority 動作設定的優先順序。</ArgTableRow>
<ArgTableRow arg="dscp" typ="super { !
, dscp: num [0 .. 63]
 }">匹配 DSCP IP 頭部欄位。</ArgTableRow>
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
以受限的速率（封包速率或位元速率）匹配封包。帶有此匹配器的規則會一直匹配，直到達到該限制。引數採用以下格式書寫：`rate[/time],burst:mode`。
- `rate` - 每個時間間隔要匹配的封包數或位元數。
- `time` - 指定封包速率或位元速率不能超過的時間間隔（可選，未指定時使用 1s）。
- `burst` - 初始要匹配的封包數或位元數：該數值每 10ms 重新充填一次，因此 burst 至少應為每秒速率的 1/100。
-  `mode` - 封包或位元模式。
</ArgTableRow>
<ArgTableRow arg="dst-limit" typ="super { count: num
, [time] [ /time]
, [burst] ,num
, [mode] ,enum (dst-address | dst-address-and-port | src-address | src-and-dst-addresses | addresses-and-dst-port) { dst-address:1, dst-address-and-port:3, src-address:4, src-and-dst-addresses:5, addresses-and-dst-port:7 }
, [expire] [ /time]
 }">
匹配封包，直到超過給定速率。速率定義為每個時間間隔的封包數。與 `limit` 匹配器不同，每條流都有各自的限制。流由 mode 引數定義。引數採用以下格式書寫：`rate[/time],burst,mode[/expire]`。
- `rate` - 每條流每個時間間隔要匹配的封包數。
- `time` - 指定每條流的包計數速率不能超過的時間間隔（可選，未指定時使用 1s）。
- `burst` - 每條流初始要匹配的封包數：該數值每隔 time/rate 增加一，直到達到此數目。
- `mode` - 指定由哪些唯一欄位定義流（src-address、dst-address、src-and-dst-address、dst-address-and-port、addresses-and-dst-port）。
- `expire` - 指定在經過多長時間後，沒有封包的流將被允許刪除（可選）。
</ArgTableRow>
<ArgTableRow arg="time" typ="super { !
, start: time [0 .. 86400]
, [end] -time [0 .. 86400]
, [day] ,ubit (sun, mon, tue, wed, thu, fri, sat)
 }">根據封包的到達時間和日期（對於本機產生的封包，則為離開時間和日期）建立過濾條件。該匹配器會考慮路由器上配置的時間和時區。</ArgTableRow>
<ArgTableRow arg="random" typ="super { percent: num [1 .. 99]
 }">按給定機率隨機匹配封包。</ArgTableRow>
<ArgTableRow arg="nth" typ="super { !
, every: num [1 .. ]
, [packet] [ ,num [1 .. ]]
 }">匹配每第 n 個數據包：`nth=2,1` 將匹配每 2 個數據包中的第 1 個，因此會匹配該規則所處理全部流量的 50%。</ArgTableRow>
<ArgTableRow arg="tcp-mss" typ="super { !
, min: num [0 .. 65535]
, [max] -num [0 .. 65535]
 }">匹配 IP 封包的 TCP MSS 值。</ArgTableRow>
<ArgTableRow arg="per-connection-classifier" typ="super { !
, values-to-hash: enum (src-address | dst-address | both-addresses | src-port | src-address-and-port | dst-port | dst-address-and-port | both-ports | both-addresses-and-ports) { src-address:1, dst-address:2, both-addresses:3, src-port:4, src-address-and-port:5, dst-port:8, dst-address-and-port:10, both-ports:12, both-addresses-and-ports:15 }
, [denominator] :num [1 .. ]
, [remainder] /num [0 .. ]
 }">PCC 匹配器允許將流量劃分為均等的流，並能夠把具有特定選項集的封包保留在某一特定流中。</ArgTableRow>
<ArgTableRow arg="packet-size" typ="super { !
, min: num [ .. 65535]
, [max] -num [ .. 65535]
 }">匹配指定大小或大小範圍（以位元組為單位）的封包。</ArgTableRow>
<ArgTableRow arg="log" typ="bool">向系統日誌新增一條訊息，包含以下資料：in-interface、out-interface、src-mac、protocol、src-ip:port-&gt;dst-ip:port 以及封包長度。即使動作不是 `log` 也允許記錄封包日誌，對於偵錯防火牆很有用。</ArgTableRow>
<ArgTableRow arg="log-prefix" typ="string">在每條日誌訊息的開頭新增指定文字。在配置了 `action=log` 或 `log=yes` 時適用。</ArgTableRow>
<ArgTableRow arg="ipsec-policy" typ="super { direction: enum (in | out) { in:0, out:1 }
, [policy] ,enum (none | ipsec) { none:0, ipsec:1 }
 }">
匹配 IPsec 使用的策略。值採用以下格式書寫：`direction, policy`。
- `in` - 在 PREROUTING、INPUT 和 FORWARD 鏈中有效。
- `out` - 在 POSTROUTING、OUTPUT 和 FORWARD 鏈中有效。
- `ipsec` - 如果封包需要經過 IPsec 處理則匹配。
- `none` - 匹配不經過 IPsec 處理的封包。
</ArgTableRow>
</ArgTable>
