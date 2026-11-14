---
sidebar_key: "cli-reference/ip/neighbor"
title: "neighbor"
sidebar_label: 'neighbor'
source: https://manual.mikrotik.com/docs/cli-reference/ip/neighbor
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/neighbor {#ipneighbor}
**型別：** 目錄

鄰居列表顯示二層廣播域中所有已發現的鄰居、每個鄰居所連線的介面、其 IP 和 MAC 地址以及其他相關引數。透過 MNDP、CDP 和 LLDP 發現的鄰居會一起顯示在這裡。要檢視 LLDP 發現的鄰居的完整 LLDP 詳細資訊，請使用 [`/ip/neighbor/lldp`](./lldp.md) 選單。

為避免記憶體耗盡，每個介面的鄰居條目數上限為（總記憶體 MB 數）* 16。

```ros
[admin@MikroTik] /ip/neighbor/print 
 # INTERFACE ADDRESS         MAC-ADDRESS       IDENTITY   VERSION    BOARD      
 0 ether13   192.168.33.2    00:0C:42:00:38:9F MikroTik   5.99       RB1100AHx2
 1 ether11   1.1.1.4         00:0C:42:40:94:25 test-host  5.8        RB1000   
 2 Local     10.0.11.203     00:02:B9:3E:AD:E0 c2611-r1   Cisco I...                    
 3 Local     10.0.11.47      00:0C:42:84:25:BA 11.47-750  5.7        RB750  
 4 Local     10.0.11.254     00:0C:42:70:04:83 tsys-sw1   5.8        RB750G    
 5 Local     10.0.11.202     00:17:5A:90:66:08 c7200      Cisco I...
```

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="multi { interface: iface_enum
 }">發現裝置所連線的介面名稱。同時顯示主介面和實際從介面。</ArgTableRow>
<ArgTableRow arg="address" typ="alt { address4: ipAddr
, address6: ip6Addr
 }">發現裝置上配置的最高 IP 地址。</ArgTableRow>
<ArgTableRow arg="address4" typ="ipAddr">發現裝置上配置的 IPv4 地址。</ArgTableRow>
<ArgTableRow arg="address6" typ="ip6Addr">發現裝置上配置的 IPv6 地址。</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">遠端裝置的 MAC 地址。可用於透過 mac-telnet 進行連線。</ArgTableRow>
<ArgTableRow arg="identity" typ="string">發現裝置所配置的系統標識。</ArgTableRow>
<ArgTableRow arg="platform" typ="string">平臺名稱，例如 "MikroTik"、"cisco"。</ArgTableRow>
<ArgTableRow arg="version" typ="string">遠端裝置上所安裝軟體的版本號。</ArgTableRow>
<ArgTableRow arg="unpack" typ="enum (none | simple | uncompress-headers | uncompress-all) { none:0x00, simple:0x01, uncompress-headers:0x03, uncompress-all:0x07 }">鄰居所通告的 [IP 打包](../../../system-information-and-utilities/ip-packing.md) 解包設定。只有當路由器通告解包時，它才會向該鄰居進行打包。`simple`、`uncompress-headers` 和 `uncompress-all` 分別對應 `unpacking` 的值 `simple`、`compress-headers` 和 `compress-all`。</ArgTableRow>
<ArgTableRow arg="age" typ="time">自上次收到發現報文以來經過的時間間隔。</ArgTableRow>
<ArgTableRow arg="uptime" typ="time">遠端裝置的執行時間。僅對安裝了 RouterOS 的裝置顯示。</ArgTableRow>
<ArgTableRow arg="software-id" typ="string">遠端裝置上的 RouterOS 軟體 ID。僅適用於安裝了 RouterOS 的裝置。</ArgTableRow>
<ArgTableRow arg="board" typ="string">RouterBoard 型號。僅對安裝了 RouterOS 的裝置顯示。</ArgTableRow>
<ArgTableRow arg="ipv6" typ="bool">該裝置是否啟用了 IPv6。</ArgTableRow>
<ArgTableRow arg="interface-name" typ="string">鄰居裝置上連線到該二層廣播域的介面名稱。適用於 CDP。</ArgTableRow>
<ArgTableRow arg="system-description" typ="string">鏈路層發現協定（LLDP）報告的系統描述。</ArgTableRow>
<ArgTableRow arg="system-caps" typ="ubit (other, repeater, bridge, wlan-ap, router, telephone, docsis-cable-device, station-only)">LLDP 報告的系統能力。</ArgTableRow>
<ArgTableRow arg="system-caps-enabled" typ="ubit (other, repeater, bridge, wlan-ap, router, telephone, docsis-cable-device, station-only)">LLDP 報告的已啟用系統能力。</ArgTableRow>
<ArgTableRow arg="discovered-by" typ="ubit (cdp, lldp, mndp)">發現該鄰居所使用的發現協定。</ArgTableRow>
<ArgTableRow arg="running" typ="multi { array-id, cap: string
 }" unset="1">鄰居裝置上正在執行的功能列表。目前僅列出 CAPsMAN 功能。</ArgTableRow>
</ArgTable>
