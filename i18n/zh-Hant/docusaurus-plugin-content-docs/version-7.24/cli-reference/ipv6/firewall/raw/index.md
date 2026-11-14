---
sidebar_key: "cli-reference/ipv6/firewall/raw/index"
sidebar_position: 1
title: "raw"
sidebar_label: "raw"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ipv6/firewall/raw
captured_at: '2026-11-01T21:29:09+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ipv6/firewall/raw {#ipv6firewallraw}
**型別：** 目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="chain" typ="enum" mandatory="1">指定規則將被新增到哪個鏈。如果輸入與已定義鏈的名稱不匹配，則會建立一個新鏈。</ArgTableRow>
<ArgTableRow arg="action" typ="enum (accept | jump | return | log | passthrough | add-src-to-address-list | add-dst-to-address-list | drop | notrack) { accept:0, jump:1, return:2, log:3, passthrough:4, add-src-to-address-list:5, add-dst-to-address-list:6, drop:10, notrack:42 }">當封包被規則匹配時要執行的動作：`accept` - 接受該封包。封包不會傳遞給下一條防火牆規則。  `add-dst-to-address-list` - 將目標地址新增到由 `address-list` 引數指定的地址列表中。  `add-src-to-address-list` - 將源地址新增到由 `address-list` 引數指定的地址列表中。  `drop` - 丟棄該封包。  `jump` - 跳轉到由 `jump-target` 引數值指定的使用者定義鏈。  `log` - 向系統日誌新增一條訊息，其中包含以下資料：in-interface、out-interface、src-mac、protocol、src-ip:port->dst-ip:port 以及封包長度。封包被匹配後，會傳遞給列表中的下一條規則，類似 `passthrough`。  `notrack` - 跳過該封包的連線跟蹤。  `passthrough` - 如果封包被規則匹配，則增加計數器並轉到下一條規則（用於統計）。  `return` - 將控制權返回給發生跳轉的來源鏈。</ArgTableRow>
<ArgTableRow arg="jump-target" typ="enum ()">要跳轉到的目標鏈名稱。僅當 `action=jump` 時適用。</ArgTableRow>
<ArgTableRow arg="tls-host" typ="super { !
, tls-host: string
 }">基於 TLS SNI 主機名匹配 HTTPS 流量。接受 GLOB 語法進行萬用字元匹配。如果 TLS 握手幀被分片到多個 TCP 段中，則匹配器將無法匹配主機名。</ArgTableRow>
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
 }">如果入介面是網橋，則為封包進入路由器時實際經過的介面。僅當網橋設定中啟用了 `use-ip-firewall` 時有效。</ArgTableRow>
<ArgTableRow arg="out-bridge-port" typ="super { !
, interface: iface_enum
 }">如果出介面是網橋，則為封包離開路由器時實際經過的介面。僅當網橋設定中啟用了 `use-ip-firewall` 時有效。</ArgTableRow>
<ArgTableRow arg="in-bridge-port-list" typ="super { !
, interface-list: enum
 }">在介面列表中定義的介面集合。工作方式與 `in-bridge-port` 相同。</ArgTableRow>
<ArgTableRow arg="out-bridge-port-list" typ="super { !
, interface-list: enum
 }">在介面列表中定義的介面集合。工作方式與 `out-bridge-port` 相同。</ArgTableRow>
<ArgTableRow arg="packet-mark" typ="super { !
, mark: enum
 }">匹配由 mangle 設施使用特定封包標記所標記的封包。如果設定了 `no-mark`，則該規則將匹配任何未標記的封包。</ArgTableRow>
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
 }">如果任一（源或目標）埠與指定的埠或埠範圍列表匹配，則匹配。僅當 `protocol` 為 TCP 或 UDP 時適用。</ArgTableRow>
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
 }">匹配設定新優先順序之後的封包優先順序。優先順序可能來自 VLAN、WMM、DSCP、MPLS EXP 位，或來自透過 set-priority 動作設定的優先順序。</ArgTableRow>
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
匹配達到受限速率（封包速率或位元速率）的封包。具有此匹配器的規則將一直匹配，直到達到該限制。引數按以下格式編寫：`rate[/time],burst:mode`。
- `rate` - 每個時間間隔要匹配的封包數或位元數。
- `time` - 指定不能超過封包或位元速率的時間間隔（可選，未指定時將使用 1s）。
- `burst` - 初始要匹配的封包數或位元數：此數值每 10ms 重新補充，因此 burst 應至少為每秒速率值的 1/100。
-  `mode` - 封包或位元模式。
</ArgTableRow>
<ArgTableRow arg="dst-limit" typ="super { count: num
, [time] [ /time]
, [burst] ,num
, [mode] ,enum (dst-address | dst-address-and-port | src-address | src-and-dst-addresses | addresses-and-dst-port) { dst-address:1, dst-address-and-port:3, src-address:4, src-and-dst-addresses:5, addresses-and-dst-port:7 }
, [expire] [ /time]
 }">
匹配封包，直到超過給定速率。速率定義為每個時間間隔的封包數。與 `limit` 匹配器不同，每個流都有自己的限制。流由 mode 引數定義。引數按以下格式編寫：`rate[/time],burst,mode[/expire]`。
- `rate` - 每個時間間隔每個流要匹配的封包數。
- `time` - 指定每個流的封包計數速率不能超過的時間間隔（可選，未指定時將使用 1s）。
- `burst` - 每個流初始要匹配的封包數：此數值每隔 time/rate 增加一，直到達到此數值。
- `mode` - 指定哪些唯一欄位定義流（src-address、dst-address、src-and-dst-address、dst-address-and-port、addresses-and-dst-port）。
- `expire` - 指定經過多長時間後，允許刪除無封包的流（可選）。
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
 }">匹配每第 n 個數據包：`nth=2,1` 將匹配每 2 個數據包中的第 1 個，因此會匹配該規則所匹配全部流量的 50%。</ArgTableRow>
<ArgTableRow arg="tcp-mss" typ="super { !
, min: num [0 .. 65535]
, [max] -num [0 .. 65535]
 }">匹配 IP 封包的 TCP MSS 值。</ArgTableRow>
<ArgTableRow arg="per-connection-classifier" typ="super { !
, values-to-hash: enum (src-address | dst-address | both-addresses | src-port | src-address-and-port | dst-port | dst-address-and-port | both-ports | both-addresses-and-ports) { src-address:1, dst-address:2, both-addresses:3, src-port:4, src-address-and-port:5, dst-port:8, dst-address-and-port:10, both-ports:12, both-addresses-and-ports:15 }
, [denominator] :num [1 .. ]
, [remainder] /num [0 .. ]
 }">PCC 匹配器允許將流量劃分為相等的流，並能夠將具有特定選項集的封包保留在一個特定流中。</ArgTableRow>
<ArgTableRow arg="packet-size" typ="super { !
, min: num [ .. 65535]
, [max] -num [ .. 65535]
 }">匹配指定大小或大小範圍（以位元組為單位）的封包。</ArgTableRow>
<ArgTableRow arg="log" typ="bool">向系統日誌新增一條訊息，其中包含以下資料：in-interface、out-interface、src-mac、protocol、src-ip:port-&gt;dst-ip:port 以及封包長度。即使動作不是 `log` 也允許記錄封包，這對於偵錯防火牆很有用。</ArgTableRow>
<ArgTableRow arg="log-prefix" typ="string">在每條日誌訊息的開頭新增指定文字。如果配置了 `action=log` 或 `log=yes`，則適用。</ArgTableRow>
<ArgTableRow arg="ipsec-policy" typ="super { direction: enum (in | out) { in:0, out:1 }
, [policy] ,enum (none | ipsec) { none:0, ipsec:1 }
 }">
匹配 IPsec 使用的策略。值按以下格式編寫：`direction, policy`。
- `in` - 在 PREROUTING、INPUT 和 FORWARD 鏈中有效。
- `out` - 在 POSTROUTING、OUTPUT 和 FORWARD 鏈中有效。
- `ipsec` - 如果封包需要經過 IPsec 處理，則匹配。
- `none` - 匹配不經過 IPsec 處理的封包。
</ArgTableRow>
<ArgTableRow arg="protocol" typ="super { !
, protocol: enum (icmpv6) { icmpv6:58 }
 }">匹配由協定名稱或編號指定的特定 IP 協定。</ArgTableRow>
<ArgTableRow arg="src-address" typ="super { !
, address: ip6Prefix
 }">匹配源地址等於指定 IP 或落在指定 IP 範圍內的封包。</ArgTableRow>
<ArgTableRow arg="dst-address" typ="super { !
, address: ip6Prefix
 }">匹配目標地址等於指定 IP 或落在指定 IP 範圍內的封包。</ArgTableRow>
<ArgTableRow arg="src-address-list" typ="super { !
, address-list: enum
 }">將封包的源地址與使用者定義的地址列表進行匹配。僅支援一個列表。</ArgTableRow>
<ArgTableRow arg="dst-address-list" typ="super { !
, address-list: enum
 }">將封包的目標地址與使用者定義的地址列表進行匹配。僅支援一個列表。</ArgTableRow>
<ArgTableRow arg="address-list" typ="enum ()">要使用的地址列表名稱。如果動作為 `add-dst-to-address-list` 或 `add-src-to-address-list`，則適用。</ArgTableRow>
<ArgTableRow arg="address-list-timeout" typ="alt { address-list-timeout: enum (none-dynamic | none-static) { none-dynamic:0, none-static:0xffffffff }
, address-list-timeout: time [ .. 21474836]
 }">地址從 `address-list` 引數指定的地址列表中移除之前的時間間隔。與 `add-dst-to-address-list` 或 `add-src-to-address-list` 動作一起使用。  `none-dynamic`（`00:00:00`）會將地址保留在地址列表中直到重啟。  `none-static` 會將地址永久保留在地址列表中，並會包含在配置匯出/備份中。</ArgTableRow>
<ArgTableRow arg="src-address-type" typ="super { !
, type: ubit (unicast, local, anycast, multicast, unreachable)
 }">匹配源地址型別：`unicast` - 用於點對點傳輸的 IP 地址。  `local` - 該地址分配給路由器的某個介面。  `anycast` - 傳送給組內最近節點的封包。  `multicast` - 封包被轉發給已定義的裝置組。  `unreachable` - 該地址不可達。</ArgTableRow>
<ArgTableRow arg="dst-address-type" typ="super { !
, type: ubit (unicast, local, anycast, multicast, unreachable)
 }">匹配目標地址型別：`unicast` - 用於點對點傳輸的 IP 地址。  `local` - 目標地址分配給路由器的某個介面。  `anycast` - 傳送給組內最近節點的封包。  `multicast` - 封包被轉發給已定義的裝置組。  `unreachable` - 該地址不可達。</ArgTableRow>
<ArgTableRow arg="headers" typ="super { !
, type: ubit (hop, dst, route, frag, ah, esp, none, proto)
, [mode] [ :enum (exact | contains) { exact:0, contains:1 }]
 }">匹配 IPv6 next-header。由 `mode` 引數控制，可以進行兩種型別的報頭匹配：`contains` - 軟匹配，至少匹配選定的報頭。  `exact` - 匹配選定報頭的精確集合。</ArgTableRow>
<ArgTableRow arg="tcp-flags" typ="super { !,
, flags: multi { array-id, array-id, flag: super { !
, flag: enum (fin | syn | rst | psh | ack | urg | ece | cwr) { fin:0, syn:1, rst:2, psh:3, ack:4, urg:5, ece:6, cwr:7 }
 }
 }
 }">匹配指定的 TCP 標誌：`ack` - 確認資料。  `cwr` - 擁塞視窗已減小。  `ece` - ECN 回顯標誌（顯式擁塞通知）。  `fin` - 關閉連線。  `psh` - 推送功能。  `rst` - 重設連線。  `syn` - 新連線。  `urg` - 緊急資料。</ArgTableRow>
<ArgTableRow arg="hop-limit" typ="super { mode: enum (equal | not-equal | less-than | greater-than) { equal:0, not-equal:1, less-than:2, greater-than:3 }
, [value] :num [0 .. 255]
 }">匹配 IPv6 頭中的跳數限制欄位。</ArgTableRow>
</ArgTable>
