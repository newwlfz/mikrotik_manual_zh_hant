---
sidebar_key: "cli-reference/tool/sniffer/packet"
sidebar_position: 3
title: "packet"
sidebar_label: 'packet'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/tool/sniffer/packet
captured_at: '2026-11-01T21:25:59+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/sniffer/packet {#toolsnifferpacket}
**型別：** 目錄

上次執行 [`start`](./start.md) 捕獲的封包會保留在記憶體中，保留時間為嗅探器停止後 10 分鐘，或直到下一次啟動。`time` 以秒為單位計算從捕獲開始經過的時間，並顯示到微秒。參見[封包嗅探器](../../../diagnostics-monitoring-and-troubleshooting/packet-sniffer.md)。

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="time" typ="num">封包相對於捕獲開始的時間偏移，以秒為單位，精確到微秒。</ArgTableRow>
<ArgTableRow arg="num" typ="num">封包序列號，第一個捕獲的封包從 0 開始。</ArgTableRow>
<ArgTableRow arg="direction" typ="enum (rx | tx) { rx:0, tx:1 }">封包相對於路由器的方向，`rx` 表示接收，`tx` 表示傳送。</ArgTableRow>
<ArgTableRow arg="src-mac" typ="macAddr">幀的源 MAC 地址，僅對具有 MAC 地址的介面顯示，例如 Ethernet、WiFi、EoIP、VXLAN 或 VLAN。</ArgTableRow>
<ArgTableRow arg="dst-mac" typ="macAddr">幀的目的 MAC 地址，僅對具有 MAC 地址的介面顯示，例如 Ethernet、WiFi、EoIP、VXLAN 或 VLAN。</ArgTableRow>
<ArgTableRow arg="vlan" typ="object { vlan: composite { id: num
, prio: [ num]
 }
 }">幀的 VLAN 標籤，顯示為 `id:priority`。</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum">捕獲封包所在的介面。</ArgTableRow>
<ArgTableRow arg="src-address" typ="composite { address: alt { ip: ipAddr
, ipv6: ip6Addr
 }
, port: enum ()
 }">封包的源 IP 地址和源埠，顯示為 `address:port`。</ArgTableRow>
<ArgTableRow arg="dst-address" typ="composite { address: alt { ip: ipAddr
, ipv6: ip6Addr
 }
, port: enum ()
 }">封包的目的 IP 地址和目的埠，顯示為 `address:port`。</ArgTableRow>
<ArgTableRow arg="protocol" typ="enum ()">幀的 MAC（L2）協定，例如 `ip`、`arp` 或 `ipv6`。</ArgTableRow>
<ArgTableRow arg="ip-protocol" typ="enum (ip) { ip:0 }">封包的 IP 協定，例如 `icmp`、`tcp` 或 `udp`。</ArgTableRow>
<ArgTableRow arg="size" typ="num">幀總大小（以位元組計），包括 L2 頭。</ArgTableRow>
<ArgTableRow arg="cpu" typ="num">處理該封包的 CPU 核心。</ArgTableRow>
<ArgTableRow arg="ip-packet-size" typ="num">IP 封包的大小，以位元組為單位。</ArgTableRow>
<ArgTableRow arg="ip-header-size" typ="num">IP 頭的大小，以位元組為單位。</ArgTableRow>
<ArgTableRow arg="dscp" typ="num">IP 頭的 DSCP（區分服務程式碼點）欄位。</ArgTableRow>
<ArgTableRow arg="ecn" typ="num">IP 頭的 ECN（顯式擁塞通知）欄位。</ArgTableRow>
<ArgTableRow arg="identification" typ="num">IP 頭的標識欄位。</ArgTableRow>
<ArgTableRow arg="fragment-offset" typ="num">IP 頭的分片偏移欄位。</ArgTableRow>
<ArgTableRow arg="ttl" typ="num">IP 頭的生存時間欄位。</ArgTableRow>
<ArgTableRow arg="tcp-flags" typ="multi { array-id, flag: enum (fin | syn | rst | psh | ack | urg | ece | cwr) { fin:0, syn:1, rst:2, psh:3, ack:4, urg:5, ece:6, cwr:7 }
 }">封包的 TCP 標誌：`fin`、`syn`、`rst`、`psh`、`ack`、`urg`、`ece` 或 `cwr`。</ArgTableRow>
<ArgTableRow arg="data" typ="string">捕獲封包的內容，採用十六進位制格式。</ArgTableRow>
</ArgTable>
