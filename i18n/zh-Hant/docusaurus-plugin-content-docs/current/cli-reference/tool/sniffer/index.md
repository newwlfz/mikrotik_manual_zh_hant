---
sidebar_key: "cli-reference/tool/sniffer"
title: "sniffer"
sidebar_label: 'sniffer'
source: https://manual.mikrotik.com/docs/cli-reference/tool/sniffer
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/sniffer {#toolsniffer}
**型別：** 設定目錄

封包嗅探器的設定：捕獲哪些封包（`filter-*` 設定）、將它們儲存在哪裡（記憶體和檔案），以及是否將它們流式傳輸到 TZSP 接收方。[`start`](./start.md) 和 [`quick`](./quick.md) 在未提供過濾引數時使用已儲存的過濾器。提供過濾引數時，它們僅在該次執行中使用給定的過濾器；已儲存的過濾器不適用，也不會改變。請參閱[封包嗅探器](../../../diagnostics-monitoring-and-troubleshooting/packet-sniffer.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="only-headers" typ="bool">僅儲存並儲存封包頭，不儲存有效載荷。封包列表仍顯示原始封包大小。預設：否。</ArgTableRow>
<ArgTableRow arg="memory-limit" typ="num">捕獲封包所用記憶體，單位為 KiB（10..4294967295）。無法容納的內容按 `memory-scroll` 的規定處理。預設：100KiB。</ArgTableRow>
<ArgTableRow arg="memory-scroll" typ="bool">達到 `memory-limit` 時發生的情況：`yes` 會用新封包替換最舊的封包，因此記憶體中儲存最新封包；`no` 會保留最先的封包，不再儲存更多封包。預設：是。</ArgTableRow>
<ArgTableRow arg="file-name" typ="file">嗅探器執行期間將捕獲的封包寫入的檔案，格式為 pcapng。每次啟動都會覆蓋該檔案。其他磁碟上的路徑（例如 `usb1/capture.pcap`）會將檔案寫入該位置。為空（預設）時僅將封包保留在記憶體中；之後可使用 [`save`](./save.md) 將其寫入檔案。</ArgTableRow>
<ArgTableRow arg="file-limit" typ="num">`file-name` 的大小限制，單位為 KiB（10..4294967295）。當檔案達到該限制時，嗅探器停止寫入該檔案，但繼續執行。預設：1000KiB。</ArgTableRow>
<ArgTableRow arg="streaming-enabled" typ="bool">將每個捕獲的封包透過 UDP 以 TZSP（版本 1、Ethernet 封裝、整個幀）傳送到 `streaming-server`，例如傳送到 Wireshark。預設：否。</ArgTableRow>
<ArgTableRow arg="streaming-server" typ="composite { ip: ipAddr
, port: [ enum ()]
 }">TZSP 流的接收方：一個地址，或 `address:port`。未指定埠時，使用 37008。預設：0.0.0.0:37008。</ArgTableRow>
<ArgTableRow arg="max-packet-size" typ="num">最大封包大小，單位為位元組（2048..65536）。預設：2048。</ArgTableRow>
<ArgTableRow arg="filter-stream" typ="bool">為 `yes` 時，嗅探器不會捕獲其流式傳輸到 `streaming-server` 的封包，也不會捕獲發往 `streaming-server` 地址及來自該地址的 ICMP 封包，即使在流式傳輸關閉時也是如此。當嗅探朝向流接收方的介面時，請設定為 `yes`：為 `no` 時，流封包會被捕獲並再次流式傳輸，形成迴圈。預設：否。</ArgTableRow>
<ArgTableRow arg="filter-interface" typ="object { interface: iface_enum
 }">要嗅探的介面。為空（預設）時嗅探所有介面；此時經過網橋往返於路由器的封包會在網橋上顯示一次，並在網橋埠上再顯示一次。</ArgTableRow>
<ArgTableRow arg="filter-mac-address" typ="object { mac-address-element: super { !
, mac-address-with-mask: composite { mac: macAddr
, mask: [ macAddr]
 }
 }
 }">最多 16 個 MAC 地址，或帶掩碼的 MAC 地址；當幀的源 MAC 地址或目的 MAC 地址匹配時，該幀即匹配。在條目前面加上 `!` 可將其取反。為空（預設）表示不進行過濾。</ArgTableRow>
<ArgTableRow arg="filter-src-mac-address" typ="object { mac-address-element: super { !
, mac-address-with-mask: composite { mac: macAddr
, mask: [ macAddr]
 }
 }
 }">最多 16 個源 MAC 地址，或帶掩碼的 MAC 地址。在條目前面加上 `!` 可將其取反。為空（預設）表示不進行過濾。</ArgTableRow>
<ArgTableRow arg="filter-dst-mac-address" typ="object { mac-address-element: super { !
, mac-address-with-mask: composite { mac: macAddr
, mask: [ macAddr]
 }
 }
 }">最多 16 個目的 MAC 地址，或帶掩碼的 MAC 地址。在條目前面加上 `!` 可將其取反。為空（預設）表示不進行過濾。</ArgTableRow>
<ArgTableRow arg="filter-mac-protocol" typ="object { mac-protocol-element: super { !
, protocol: alt { mac-protocol: enum ()
, protocol-number: num [ .. 65535]
 }
 }
 }">最多 16 個 MAC（L2）協定，可透過 EtherType 編號（0..65535）或名稱指定：`802.2` (0x0004), `arp` (0x0806), `capsman` (0x88BB), `dot1x` (0x888E), `homeplug-av` (0x88E1), `ip` (0x0800), `ipv6` (0x86DD), `ipx` (0x8137), `lacp` (0x8809), `lldp` (0x88CC), `loop-protect` (0x9003), `macsec` (0x88E5), `mpls-multicast` (0x8848), `mpls-unicast` (0x8847), `mvrp` (0x88F5), `packing-compr`, `packing-simple`, `pppoe` (0x8864), `pppoe-discovery` (0x8863), `rarp` (0x8035), `romon` (0x88BF), `service-vlan` (0x88A8), `vlan` (0x8100)。帶 VLAN 標籤的幀匹配的是標籤內部的協定，而不是 `vlan`；使用 `filter-vlan` 選擇 VLAN。在條目前面加上 `!` 可將其取反。為空（預設）表示不進行過濾。</ArgTableRow>
<ArgTableRow arg="filter-ip-address" typ="object { ip-address-element: super { !
, ip-address-with-mask: composite { ip: ipAddr
, mask: [ num [ .. 32]]
 }
 }
 }">最多 16 個 IPv4 地址或字首；當封包的源地址或目的地址匹配時，該封包即匹配。在條目前面加上 `!` 可將其取反。為空（預設）表示不進行過濾。</ArgTableRow>
<ArgTableRow arg="filter-src-ip-address" typ="object { ip-address-element: super { !
, ip-address-with-mask: composite { ip: ipAddr
, mask: [ num [ .. 32]]
 }
 }
 }">最多 16 個源 IPv4 地址或字首。在條目前面加上 `!` 可將其取反。為空（預設）表示不進行過濾。</ArgTableRow>
<ArgTableRow arg="filter-dst-ip-address" typ="object { ip-address-element: super { !
, ip-address-with-mask: composite { ip: ipAddr
, mask: [ num [ .. 32]]
 }
 }
 }">最多 16 個目的 IPv4 地址或字首。在條目前面加上 `!` 可將其取反。為空（預設）表示不進行過濾。</ArgTableRow>
<ArgTableRow arg="filter-ipv6-address" typ="object { ipv6-address-element: super { !
, ipv6-prefix: ip6Prefix
 }
 }">最多 16 個 IPv6 字首；當封包的源地址或目的地址匹配時，該封包即匹配。在條目前面加上 `!` 可將其取反。為空（預設）表示不進行過濾。</ArgTableRow>
<ArgTableRow arg="filter-src-ipv6-address" typ="object { ipv6-address-element: super { !
, ipv6-prefix: ip6Prefix
 }
 }">最多 16 個源 IPv6 字首。在條目前面加上 `!` 可將其取反。為空（預設）表示不進行過濾。</ArgTableRow>
<ArgTableRow arg="filter-dst-ipv6-address" typ="object { ipv6-address-element: super { !
, ipv6-prefix: ip6Prefix
 }
 }">最多 16 個目的 IPv6 字首。在條目前面加上 `!` 可將其取反。為空（預設）表示不進行過濾。</ArgTableRow>
<ArgTableRow arg="filter-ip-protocol" typ="object { ip-protocol-element: super { !
, ip-protocol: enum ()
 }
 }">最多 16 個 IP 或 IPv6 協定，可透過編號或名稱指定：`dccp`, `ddp`, `egp`, `encap`, `etherip`, `ggp`, `gre`, `hmp`, `icmp`, `icmpv6`, `idpr-cmtp`, `igmp`, `ipencap`, `ipip`, `ipsec-ah`, `ipsec-esp`, `ipv6-encap`, `ipv6-frag`, `ipv6-nonxt`, `ipv6-opts`, `ipv6-route`, `iso-tp4`, `l2tp`, `ospf`, `pim`, `pup`, `rdp`, `rspf`, `rsvp`, `sctp`, `st`, `tcp`, `udp`, `udp-lite`, `vmtp`, `vrrp`, `xns-idp`, `xtp`。在條目前面加上 `!` 可將其取反。為空（預設）表示不進行過濾。</ArgTableRow>
<ArgTableRow arg="filter-port" typ="object { port-element: super { !
, port: enum ()
 }
 }">最多 16 個埠，可透過編號或名稱指定，例如 `ssh`、`dns`、`bootps`（67）或 `bootpc`（68）；當封包的源埠或目的埠匹配時，該封包即匹配。在條目前面加上 `!` 可將其取反。為空（預設）表示不進行過濾。</ArgTableRow>
<ArgTableRow arg="filter-src-port" typ="object { port-element: super { !
, port: enum ()
 }
 }">最多 16 個源埠，可透過編號或名稱指定。在條目前面加上 `!` 可將其取反。為空（預設）表示不進行過濾。</ArgTableRow>
<ArgTableRow arg="filter-dst-port" typ="object { port-element: super { !
, port: enum ()
 }
 }">最多 16 個目的埠，可透過編號或名稱指定。在條目前面加上 `!` 可將其取反。為空（預設）表示不進行過濾。</ArgTableRow>
<ArgTableRow arg="filter-vlan" typ="object { cpu-element: super { !
, vlan: num [ .. 4095]
 }
 }">最多 16 個 VLAN ID（0..4095）。它匹配承載這些標籤的介面（例如 trunk 埠）上的帶標籤幀；IP 和 MAC 過濾器匹配標籤內部的封包。在 VLAN 介面本身上，封包不帶標籤，因此不會匹配。在條目前面加上 `!` 可將其取反。為空（預設）表示不進行過濾。</ArgTableRow>
<ArgTableRow arg="filter-cpu" typ="object { cpu-element: super { !
, cpu: num
 }
 }">處理該封包的 CPU 核心。在條目前面加上 `!` 可將其取反。為空（預設）表示不進行過濾。</ArgTableRow>
<ArgTableRow arg="filter-size" typ="object { size-element: super { !
, size-range: range [0 .. 65535]
 }
 }">封包大小或大小範圍，單位為位元組（0..65535），例如 `1000-1500`。在條目前面加上 `!` 可將其取反。為空（預設）表示不進行過濾。</ArgTableRow>
<ArgTableRow arg="filter-direction" typ="enum (any | tx | rx) { any:0, tx:1, rx:2 }">
要捕獲的方向。
- `any`（預設）- 接收和傳送的封包。
- `rx` - 接收的封包。它們在防火牆之前被捕獲，因此被防火牆規則丟棄的封包仍會被捕獲。
- `tx` - 傳送的封包，在防火牆之後捕獲。
</ArgTableRow>
<ArgTableRow arg="filter-operator-between-entries" typ="enum (or | and) { or:0, and:1 }">
一個過濾器的各個條目如何組合。不同過濾器始終組合：封包必須匹配所有已設定的過濾器。
- `or`（預設）- 當封包匹配過濾器中的任意一個條目時，該封包即匹配該過濾器。
- `and` - 僅當封包匹配過濾器中的所有條目（例如 `filter-ip-address=192.168.88.10/32,192.168.88.1/32` 中的兩個地址）時，該封包才匹配該過濾器。
</ArgTableRow>
<ArgTableRow arg="quick-rows" typ="num">當未指定 [`quick`](./quick.md) 的 `rows` 引數時，顯示的報文數量。預設值：20。</ArgTableRow>
<ArgTableRow arg="quick-show-frame" typ="bool">當未指定 [`quick`](./quick.md) 的 `show-frame` 引數時，是否顯示幀內容。預設值：no。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="running" typ="bool">嗅探器執行時為 `yes`。</ArgTableRow>
</ArgTable>
