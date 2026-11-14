---
sidebar_key: "cli-reference/tool/sniffer/quick"
sidebar_position: 5
title: "quick"
sidebar_label: 'quick'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/tool/sniffer/quick
captured_at: '2026-11-01T21:26:02+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/sniffer/quick {#toolsnifferquick}
**型別：** 命令

即時顯示匹配的封包，直到您使用 <kbd>Q</kbd> 停止它，或直到 `duration` 中指定的時間結束。過濾引數是 [`/tool/sniffer`](./index.md) 的 `filter-*` 設定去掉 `filter-` 字首後的形式，以及用於 `filter-vlan` 的 `vlan-id`。不帶過濾引數時，將應用已儲存的過濾器；帶過濾引數時，僅應用給定的過濾器，並且已儲存的設定不會改變。當嗅探器執行時，`quick` 無法執行（`already running`）。`proplist` 用於選擇列，例如 `proplist=interface,time,dir,src-address,dst-address,protocol,size`。請參閱[封包嗅探器](../../../diagnostics-monitoring-and-troubleshooting/packet-sniffer.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="rows" typ="num">輸出中顯示的封包最大數量。預設值：`quick-rows` 設定（20）。</ArgTableRow>
<ArgTableRow arg="show-frame" typ="bool">是否在輸出中顯示原始幀內容。預設值：`quick-show-frame` 設定（no）。</ArgTableRow>
<ArgTableRow arg="interface" typ="object { interface: iface_enum
 }">要捕獲流量的介面或介面列表。當橋接介面和橋接埠都包含在內時，橋接封包會在橋上顯示一次，並在橋接埠上顯示一次。</ArgTableRow>
<ArgTableRow arg="mac-address" typ="object { mac-address-element: super { !
, mac-address-with-mask: composite { mac: macAddr
, mask: [ macAddr]
 }
 }
 }">過濾：僅捕獲具有匹配 MAC 地址或帶掩碼 MAC 地址的幀。</ArgTableRow>
<ArgTableRow arg="src-mac-address" typ="object { mac-address-element: super { !
, mac-address-with-mask: composite { mac: macAddr
, mask: [ macAddr]
 }
 }
 }">過濾：僅捕獲具有匹配源 MAC 地址或帶掩碼 MAC 地址的幀。</ArgTableRow>
<ArgTableRow arg="dst-mac-address" typ="object { mac-address-element: super { !
, mac-address-with-mask: composite { mac: macAddr
, mask: [ macAddr]
 }
 }
 }">過濾：僅捕獲具有匹配目標 MAC 地址或帶掩碼 MAC 地址的幀。</ArgTableRow>
<ArgTableRow arg="mac-protocol" typ="object { mac-protocol-element: super { !
, protocol: alt { mac-protocol: enum ()
, protocol-number: num [ .. 65535]
 }
 }
 }">過濾：僅捕獲具有匹配 MAC（L2）協定的幀。</ArgTableRow>
<ArgTableRow arg="ip-protocol" typ="object { ip-protocol-element: super { !
, ip-protocol: enum ()
 }
 }">過濾：僅捕獲具有匹配 IP 協定的封包。</ArgTableRow>
<ArgTableRow arg="ip-address" typ="object { ip-address-element: super { !
, ip-address-with-mask: composite { ip: ipAddr
, mask: [ num [ .. 32]]
 }
 }
 }">過濾：僅捕獲具有匹配 IP 地址或子網的封包。</ArgTableRow>
<ArgTableRow arg="src-ip-address" typ="object { ip-address-element: super { !
, ip-address-with-mask: composite { ip: ipAddr
, mask: [ num [ .. 32]]
 }
 }
 }">過濾：僅捕獲具有匹配源 IP 地址或子網的封包。</ArgTableRow>
<ArgTableRow arg="dst-ip-address" typ="object { ip-address-element: super { !
, ip-address-with-mask: composite { ip: ipAddr
, mask: [ num [ .. 32]]
 }
 }
 }">過濾：僅捕獲具有匹配目標 IP 地址或子網的封包。</ArgTableRow>
<ArgTableRow arg="ipv6-address" typ="object { ipv6-address-element: super { !
, ipv6-prefix: ip6Prefix
 }
 }">過濾：僅捕獲具有匹配 IPv6 地址或字首的封包。</ArgTableRow>
<ArgTableRow arg="src-ipv6-address" typ="object { ipv6-address-element: super { !
, ipv6-prefix: ip6Prefix
 }
 }">過濾：僅捕獲具有匹配源 IPv6 地址或字首的封包。</ArgTableRow>
<ArgTableRow arg="dst-ipv6-address" typ="object { ipv6-address-element: super { !
, ipv6-prefix: ip6Prefix
 }
 }">過濾：僅捕獲具有匹配目標 IPv6 地址或字首的封包。</ArgTableRow>
<ArgTableRow arg="port" typ="object { port-element: super { !
, port: enum ()
 }
 }">過濾：僅捕獲具有匹配源埠或目標埠的封包。</ArgTableRow>
<ArgTableRow arg="src-port" typ="object { port-element: super { !
, port: enum ()
 }
 }">過濾：僅捕獲具有匹配源埠的封包。</ArgTableRow>
<ArgTableRow arg="dst-port" typ="object { port-element: super { !
, port: enum ()
 }
 }">過濾：僅捕獲具有匹配目標埠的封包。</ArgTableRow>
<ArgTableRow arg="vlan-id" typ="object { vlan-element: super { !
, vlan: num [ .. 4095]
 }
 }">過濾：僅捕獲具有匹配 VLAN ID 的幀。</ArgTableRow>
<ArgTableRow arg="direction" typ="enum (any | tx | rx) { any:0, tx:1, rx:2 }">
過濾：要捕獲的方向。
- `any`（預設） - 接收和傳送的封包。
- `rx` - 接收的封包。它們在防火牆之前被捕獲，因此被防火牆規則丟棄的封包仍會被捕獲。
- `tx` - 傳送的封包，在防火牆之後捕獲。
</ArgTableRow>
<ArgTableRow arg="operator-between-entries" typ="enum (or | and) { or:0, and:1 }">
一個過濾器的條目如何組合。
- `or`（預設） - 當封包匹配過濾器的任一條目時，該封包就匹配該過濾器。
- `and` - 只有當封包匹配過濾器的所有條目時，該封包才匹配該過濾器。
</ArgTableRow>
<ArgTableRow arg="cpu" typ="object { cpu-element: super { !
, cpu: num
 }
 }">過濾：僅捕獲由指定 CPU 核心處理的封包。</ArgTableRow>
<ArgTableRow arg="size" typ="object { size-element: super { !
, size-range: range [0 .. 65535]
 }
 }">過濾：僅捕獲大小或大小範圍（以位元組為單位）匹配的封包。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum">捕獲該封包的介面。</ArgTableRow>
<ArgTableRow arg="time" typ="num">封包相對於捕獲開始時間的時間偏移，以秒為單位，精度為微秒。</ArgTableRow>
<ArgTableRow arg="num" typ="num">封包序列號，第一個捕獲的封包從 0 開始。</ArgTableRow>
<ArgTableRow arg="dir" typ="enum (<- | ->) { <-:0, ->:1 }">封包方向，`<-` 表示接收，`->` 表示傳送。</ArgTableRow>
<ArgTableRow arg="src-mac" typ="macAddr">幀的源 MAC 地址，僅對具有 MAC 地址的介面顯示，例如 Ethernet、WiFi、EoIP、VXLAN 或 VLAN。</ArgTableRow>
<ArgTableRow arg="dst-mac" typ="macAddr">幀的目標 MAC 地址，僅對具有 MAC 地址的介面顯示，例如 Ethernet、WiFi、EoIP、VXLAN 或 VLAN。</ArgTableRow>
<ArgTableRow arg="vlan" typ="composite { id: num [ .. 4095]
, priority: num [ .. 7]
 }">幀的 VLAN 標籤，顯示為 `id:priority`。</ArgTableRow>
<ArgTableRow arg="src-address" typ="composite { address: alt { ip: ipAddr
, ipv6: ip6Addr
, descr: string
 }
, port: enum ()
 }">封包的源 IP 地址和源埠，顯示為 `address:port`。</ArgTableRow>
<ArgTableRow arg="dst-address" typ="composite { address: alt { ip: ipAddr
, ipv6: ip6Addr
 }
, port: enum ()
 }">封包的目標 IP 地址和目標埠，顯示為 `address:port`。</ArgTableRow>
<ArgTableRow arg="protocol" typ="composite { mac-protocol: enum ()
, ip-protocol: enum (ip) { ip:0 }
 }">幀的 MAC（L2）協定及其 IP 協定，例如 `ip:icmp`。</ArgTableRow>
<ArgTableRow arg="size" typ="num">幀的總大小（以位元組為單位），包括 L2 頭。</ArgTableRow>
<ArgTableRow arg="cpu" typ="num">處理該封包的 CPU 核心。</ArgTableRow>
<ArgTableRow arg="fp" typ="bool">封包是否在快速路徑中處理。</ArgTableRow>
<ArgTableRow arg="raw" typ="string">十六進位制格式的原始幀內容，在啟用 `show-frame` 引數時顯示。</ArgTableRow>
<ArgTableRow arg="dscp" typ="num">IP 頭的 DSCP（差異化服務程式碼點）欄位。</ArgTableRow>
<ArgTableRow arg="ecn" typ="num">IP 頭的 ECN（顯式擁塞通知）欄位。</ArgTableRow>
<ArgTableRow arg="fragment-offset" typ="num">IP 頭的分片偏移欄位。</ArgTableRow>
<ArgTableRow arg="identification" typ="num">IP 頭的標識欄位。</ArgTableRow>
<ArgTableRow arg="ip-header-size" typ="num">IP 頭的大小（以位元組為單位）。</ArgTableRow>
<ArgTableRow arg="ip-packet-size" typ="num">IP 封包的大小（以位元組為單位）。</ArgTableRow>
<ArgTableRow arg="tcp-flags" typ="super { tcp-flags: multi { array-id, flag: enum (fin | syn | rst | psh | ack | urg | ece | cwr) { fin:0, syn:1, rst:2, psh:3, ack:4, urg:5, ece:6, cwr:7 }
 }
 }">封包的 TCP 標誌：`fin`、`syn`、`rst`、`psh`、`ack`、`urg`、`ece` 或 `cwr`。</ArgTableRow>
<ArgTableRow arg="ttl" typ="num">IP 頭的生存時間欄位。</ArgTableRow>
</ArgTable>
