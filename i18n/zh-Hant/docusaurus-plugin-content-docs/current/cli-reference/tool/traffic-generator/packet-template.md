---
sidebar_key: "cli-reference/tool/traffic-generator/packet-template"
sidebar_position: 3
title: "packet-template"
sidebar_label: 'packet-template'
source: https://manual.mikrotik.com/docs/cli-reference/tool/traffic-generator/packet-template
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/traffic-generator/packet-template {#tooltraffic-generatorpacket-template}
**型別：** Directory
根據頭部引數構建流的報文內容：MAC、VLAN、IPv4/IPv6、UDP 和 TCP 欄位以及有效載荷。許多頭部值在可以推導時會被假定；假定值為只讀，並在編輯模板時重新推導。請參閱 [流量生成器](../../../diagnostics-monitoring-and-troubleshooting/traffic-generator.md) 指南。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">封包模板的描述性名稱。</ArgTableRow>
<ArgTableRow arg="header-stack" typ="multi { header: enum (mac | vlan | ip | udp | raw | ipv6 | tcp) { mac:1, vlan:2, ip:3, udp:4, raw:5, ipv6:6, tcp:7 }
 }">生成封包中的頭部序列：mac（Ethernet，14 位元組）、vlan（802.1Q 標籤，4 位元組）、ip（IPv4，20 位元組）、udp（UDP，8 位元組）、raw（以十六進位制字串表示的任意位元組）、ipv6（IPv6，40 位元組）、tcp（TCP）。大多數頭部型別可以出現多次；每個封包最多可以有兩個 IP 頭部和一個 UDP 頭部。序列限制遵循協定規則（例如，VLAN 頭部只能跟在 mac 頭部或其他 VLAN 頭部之後）。</ArgTableRow>
<ArgTableRow arg="port" typ="enum">傳送封包所經由的埠名稱（來自 port 選單）。與 interface 互斥；port 也可以在 stream 中設定。</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum">傳送封包所經由的介面。與 port 互斥；便於快速測試，因為隨後會動態建立 port 條目。</ArgTableRow>
<ArgTableRow arg="mac-src" typ="multi { array-id, array-id, mac-mask: composite { mac: macAddr
, mask: [ macAddr]
 }
 }">Ethernet 頭部的源 MAC 地址（可帶掩碼）。</ArgTableRow>
<ArgTableRow arg="mac-dst" typ="multi { array-id, array-id, mac-mask: composite { mac: macAddr
, mask: [ macAddr]
 }
 }">Ethernet 頭部的目的 MAC 地址（可帶掩碼）。</ArgTableRow>
<ArgTableRow arg="mac-protocol" typ="multi { protocol: alt { protocol-name: enum ()
, protocol-number: num [ .. 65535]
 }
 }">Ethernet 幀的 EtherType，可按名稱或協定號（0-65535）指定。</ArgTableRow>
<ArgTableRow arg="vlan-priority" typ="multi { priority: num [ .. 7]
 }">802.1Q 標籤的 VLAN 優先順序（0-7）。</ArgTableRow>
<ArgTableRow arg="vlan-id" typ="multi { id: num [ .. 4095]
 }">802.1Q 標籤的 VLAN ID（0-4095）。</ArgTableRow>
<ArgTableRow arg="vlan-protocol" typ="multi { protocol: alt { protocol-name: enum ()
, protocol-number: num [ .. 65535]
 }
 }">VLAN 協定，可按名稱或 EtherType 編號（0-65535）。</ArgTableRow>
<ArgTableRow arg="ip-dscp" typ="multi { dscp: num [ .. 255]
 }">IPv4 頭部的 DS Field 值（0-255）（DS Field 包含 DSCP 和 ECN 值）。</ArgTableRow>
<ArgTableRow arg="ip-id" typ="multi { id: num [ .. 65535]
 }">IPv4 標識值（0-65535）。</ArgTableRow>
<ArgTableRow arg="ip-frag-off" typ="multi { frag-off: num [ .. 65535]
 }">IPv4 分片偏移量（0-65535）。</ArgTableRow>
<ArgTableRow arg="ip-ttl" typ="multi { ttl: num [ .. 255]
 }">IPv4 生存時間值（0-255）。</ArgTableRow>
<ArgTableRow arg="ip-src" typ="multi { array-id, array-id, ip-range: ipRange
 }">IPv4 頭部的源 IPv4 地址，可帶可選掩碼。</ArgTableRow>
<ArgTableRow arg="ip-dst" typ="multi { array-id, array-id, ip-range: ipRange
 }">IPv4 頭部的目的 IPv4 地址，可帶可選掩碼。</ArgTableRow>
<ArgTableRow arg="ip-protocol" typ="multi { protocol-name: enum ()
 }">IPv4 協定，例如 tcp、udp 或 icmp。</ArgTableRow>
<ArgTableRow arg="ip-gateway" typ="ipAddr">下一跳 IPv4 地址。當傳送方與接收方為同一裝置時，無法從 ip-dst 推匯出下一跳；當設定了 ip-gateway 時，目的 MAC 由解析出的閘道器推斷。</ArgTableRow>
<ArgTableRow arg="udp-src-port" typ="multi { array-id, array-id, port-range: range [ .. 65535]
 }">UDP 源埠或埠範圍（0-65535）。</ArgTableRow>
<ArgTableRow arg="udp-dst-port" typ="multi { array-id, array-id, port-range: range [ .. 65535]
 }">UDP 目的埠或埠範圍（0-65535）。</ArgTableRow>
<ArgTableRow arg="udp-checksum" typ="multi { array-id, checksum: num [ .. 65535]
 }">UDP 校驗和值（0-65535）。</ArgTableRow>
<ArgTableRow arg="raw-header" typ="multi { raw-header: string
 }">以十六進位制字串表示的原始頭部位元組。</ArgTableRow>
<ArgTableRow arg="ipv6-src" typ="multi { array-id, array-id, ipv6-mask: ip6Prefix
 }">IPv6 頭部的源 IPv6 地址，可帶可選掩碼。</ArgTableRow>
<ArgTableRow arg="ipv6-dst" typ="multi { array-id, array-id, ipv6-mask: ip6Prefix
 }">IPv6 頭部的目的 IPv6 地址，可帶可選掩碼。</ArgTableRow>
<ArgTableRow arg="ipv6-next-header" typ="multi { protocol: enum ()
 }">IPv6 Next Header 協定。</ArgTableRow>
<ArgTableRow arg="ipv6-gateway" typ="ip6Addr">下一跳 IPv6 地址；目的 MAC 假定來自解析後的閘道器。</ArgTableRow>
<ArgTableRow arg="ipv6-traffic-class" typ="multi { traffic-class: num [ .. 255]
 }">IPv6 traffic class 值（0-255）。</ArgTableRow>
<ArgTableRow arg="ipv6-flow-label" typ="multi { flow-label: num [ .. 0xfffff]
 }">IPv6 flow label 值（0-1048575）。</ArgTableRow>
<ArgTableRow arg="ipv6-hop-limit" typ="multi { hop-limit: num [ .. 255]
 }">IPv6 hop limit 值（0-255）。</ArgTableRow>
<ArgTableRow arg="tcp-src-port" typ="multi { array-id, array-id, port-range: range [ .. 65535]
 }">TCP 源埠或埠範圍（0-65535）。</ArgTableRow>
<ArgTableRow arg="tcp-dst-port" typ="multi { array-id, array-id, port-range: range [ .. 65535]
 }">TCP 目的埠或埠範圍（0-65535）。</ArgTableRow>
<ArgTableRow arg="tcp-syn" typ="multi { array-id, array-id, syn-range: range
 }">TCP 序列號值，可以為範圍。</ArgTableRow>
<ArgTableRow arg="tcp-ack" typ="multi { array-id, array-id, ack-range: range
 }">TCP 確認號值，可以是範圍。</ArgTableRow>
<ArgTableRow arg="tcp-data-offset" typ="multi { data-offset: num [ .. 15]
 }">TCP 資料偏移（0-15，以 32 位字為單位）。</ArgTableRow>
<ArgTableRow arg="tcp-flags" typ="multi { flags: ubit (fin, syn, rst, psh, ack, urg, ece, cwr, ns, res0, res1, res2)
 }">要設定的 TCP 標誌位：fin, syn, rst, psh, ack, urg, ece, cwr, ns, res0, res1, res2。</ArgTableRow>
<ArgTableRow arg="tcp-window-size" typ="multi { window-size: num [ .. 65535]
 }">TCP 視窗大小值（0-65535）。</ArgTableRow>
<ArgTableRow arg="tcp-urgent-pointer" typ="multi { urgent-pointer: num [ .. 65535]
 }">TCP 緊急指標值（0-65535）。</ArgTableRow>
<ArgTableRow arg="data" typ="enum (uninitialized | random | specific-byte | incrementing) { uninitialized:0, random:1, specific-byte:2, incrementing:3 }">封包載荷（頭部之後的部分）的填充方式：uninitialized（不置零；最快）、specific-byte（使用 data-byte 填充）、incrementing（位元組 00 01 02 ...）、random（隨機位元組；最慢）。</ArgTableRow>
<ArgTableRow arg="data-byte" typ="num">當 data=specific-byte 時用於填充載荷的位元組。</ArgTableRow>
<ArgTableRow arg="random-byte-offsets-and-masks" typ="multi { array-id, array-id, offset-and-mask: composite { offset: num [ .. 256]
, mask: num [ .. 255]
 }
 }">封包中的位元組偏移量，每個都帶有一個位掩碼，這些位置將被填入隨機值。</ArgTableRow>
<ArgTableRow arg="random-ranges" typ="object { random-range: super { offset: num [ .. 256]
, [width] :enum (8 | 16 | 32) { 8:8, 16:16, 32:32 }
, [range] :range
 }
 }">位於給定位元組偏移處的欄位將被填入隨機值：`width` 設定欄位大小（8、16 或 32 位），`range` 設定取值範圍。</ArgTableRow>
<ArgTableRow arg="special-footer" typ="bool">是否在生成的封包後附加特殊尾部。</ArgTableRow>
<ArgTableRow arg="compute-checksum-from-offset" typ="num">計算 2 位元組校驗和的起始位元組偏移量；例如 14 表示跳過乙太網頭。no-checksum 表示停用校驗和。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="assumed-port" typ="enum (none) { none:0xffffffff }">報文傳送時所經過的假定埠；僅在設定了介面時推導得出。</ArgTableRow>
<ArgTableRow arg="assumed-interface" typ="iface_enum">報文傳送時所經過的假定介面。</ArgTableRow>
<ArgTableRow arg="assumed-mac-src" typ="multi { mac: macAddr
 }">假定的源 MAC 地址（介面的 MAC 地址）。</ArgTableRow>
<ArgTableRow arg="assumed-mac-dst" typ="multi { mac: macAddr
 }">假定的目的 MAC 地址，由 ip-dst 推導得出，或透過解析 ip-gateway 推導得出。</ArgTableRow>
<ArgTableRow arg="assumed-mac-protocol" typ="multi { protocol: alt { protocol-name: enum ()
, protocol-number: num
 }
 }">假定的 EtherType，由頭部棧推導得出（例如 ip）。</ArgTableRow>
<ArgTableRow arg="assumed-vlan-priority" typ="multi { priority: num
 }">假定的 802.1Q 標籤 VLAN 優先順序。</ArgTableRow>
<ArgTableRow arg="assumed-vlan-id" typ="multi { priority: num
 }">假定的 802.1Q 標籤 VLAN ID。</ArgTableRow>
<ArgTableRow arg="assumed-vlan-protocol" typ="multi { protocol: alt { protocol-name: enum ()
, protocol-number: num
 }
 }">假定的 802.1Q 標籤 VLAN 協定。</ArgTableRow>
<ArgTableRow arg="assumed-ip-dscp" typ="multi { dscp: num
 }">假定的 IPv4 DS 欄位值。</ArgTableRow>
<ArgTableRow arg="assumed-ip-id" typ="multi { id: num
 }">假定的 IPv4 標識值。</ArgTableRow>
<ArgTableRow arg="assumed-ip-frag-off" typ="multi { frag-off: num
 }">假定的 IPv4 分片偏移。</ArgTableRow>
<ArgTableRow arg="assumed-ip-ttl" typ="multi { ttl: num
 }">假定的 IPv4 time-to-live 值（例如 64）。</ArgTableRow>
<ArgTableRow arg="assumed-ip-src" typ="multi { assumed-ip-src: ipAddr
 }">假定的源 IPv4 地址（介面的地址）。</ArgTableRow>
<ArgTableRow arg="assumed-ip-dst" typ="multi { assumed-ip-dst: ipAddr
 }">假定的目標 IPv4 地址。</ArgTableRow>
<ArgTableRow arg="assumed-ip-protocol" typ="multi { ip-protocol: enum ()
 }">假定的 IPv4 協定，由頭部棧推導得出（例如 udp）。</ArgTableRow>
<ArgTableRow arg="assumed-udp-src-port" typ="multi { port: num
 }">假定的 UDP 源埠。</ArgTableRow>
<ArgTableRow arg="assumed-udp-dst-port" typ="multi { port: num
 }">假定的 UDP 目標埠。</ArgTableRow>
<ArgTableRow arg="assumed-udp-checksum" typ="multi { checksum: num
 }">假定的 UDP 校驗和值。</ArgTableRow>
<ArgTableRow arg="assumed-raw-header" typ="multi { assumed-raw-header: string
 }">假定的原始頭部位元組，以十六進位制字串表示。</ArgTableRow>
<ArgTableRow arg="assumed-ipv6-src" typ="multi { ip: ip6Addr
 }">假定的源 IPv6 地址（介面的一個地址）。</ArgTableRow>
<ArgTableRow arg="assumed-ipv6-dst" typ="multi { ip: ip6Addr
 }">假定的目標 IPv6 地址。</ArgTableRow>
<ArgTableRow arg="assumed-ipv6-next-header" typ="multi { ip-protocol: enum ()
 }">假定的 IPv6 下一報頭協定。</ArgTableRow>
<ArgTableRow arg="assumed-ipv6-traffic-class" typ="multi { traffic-class: num
 }">假定的 IPv6 流量類別值。</ArgTableRow>
<ArgTableRow arg="assumed-ipv6-flow-label" typ="multi { flow-label: num
 }">假定的 IPv6 流標籤值。</ArgTableRow>
<ArgTableRow arg="assumed-ipv6-hop-limit" typ="multi { hop-limit: num
 }">假定的 IPv6 跳數限制值。</ArgTableRow>
<ArgTableRow arg="assumed-tcp-src-port" typ="multi { port: num
 }">假定的 TCP 源埠。</ArgTableRow>
<ArgTableRow arg="assumed-tcp-dst-port" typ="multi { port: num
 }">假定的 TCP 目的埠。</ArgTableRow>
<ArgTableRow arg="assumed-tcp-syn" typ="multi { syn: num
 }">假定的 TCP 序列號。</ArgTableRow>
<ArgTableRow arg="assumed-tcp-ack" typ="multi { ack: num
 }">假定的 TCP 確認號。</ArgTableRow>
<ArgTableRow arg="assumed-tcp-data-offset" typ="multi { data-offset: num
 }">假定的 TCP 資料偏移量。</ArgTableRow>
<ArgTableRow arg="assumed-tcp-flags" typ="multi { flags: num
 }">假定的 TCP 標誌。</ArgTableRow>
<ArgTableRow arg="assumed-tcp-window-size" typ="multi { window-size: num
 }">假定的 TCP 視窗大小。</ArgTableRow>
<ArgTableRow arg="assumed-tcp-urgent-pointer" typ="multi { urgent-pointer: num
 }">假定的 TCP 緊急指標值。</ArgTableRow>
</ArgTable>
