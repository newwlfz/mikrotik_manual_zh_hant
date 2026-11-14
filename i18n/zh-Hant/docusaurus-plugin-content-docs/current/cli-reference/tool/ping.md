---
sidebar_key: "cli-reference/tool/ping"
sidebar_position: 16
title: "ping"
sidebar_label: 'ping'
source: https://manual.mikrotik.com/docs/cli-reference/tool/ping
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/ping {#toolping}
**型別：** 命令

向主機發送 ICMP 回顯請求（IPv4）或 ICMPv6 回顯請求（IPv6），並顯示每個應答及其往返時間、TTL 和狀態，最後給出彙總。`/ping` 是 `/tool/ping` 的簡寫形式。使用 `arp-ping` 或 `nd-ping` 時，路由器改為傳送 ARP 請求或 IPv6 鄰居請求；當 `address` 為 MAC 地址時，傳送 MAC ping。在指令碼中，該命令返回應答的數量。完整文件請參見 [Ping](../../diagnostics-monitoring-and-troubleshooting/ping.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="address" typ="address (flags=46v%Dm)">要 ping 的主機：IPv4 或 IPv6 地址、DNS 名稱，或用於 MAC ping 的 MAC 地址。路由器使用自身的 DNS 設定解析名稱。IPv6 鏈路本地地址和 MAC 地址以介面作為字尾，例如 `fe80::1%ether1` 或 `00:11:22:33:44:55%ether1`；不帶字尾的 MAC ping 會從每個介面發出。參見 [地址標誌](../index.md#address-flags)。</ArgTableRow>
<ArgTableRow arg="interval" typ="time">兩次請求之間的時間，`00:00:00.010..00:00:05`（10 毫秒到 5 秒）。晚於該間隔到達的應答計為超時。預設值：1s。</ArgTableRow>
<ArgTableRow arg="size" typ="num">每個請求的位元組大小，即包含 IP 頭的整個 IP 封包，IPv4 為 `28..65535`，IPv6 為 `48..65535`。在乙太網鏈路上，`size=1500` 是滿尺寸封包。大於出介面 MTU 的請求會被分片，除非設定了 `do-not-fragment`。預設值：56。</ArgTableRow>
<ArgTableRow arg="ttl" typ="num">IPv4 請求的 TTL 和 IPv6 請求的跳數限制，`1..255`。預設值：IPv4 為 255，IPv6 為 64。</ArgTableRow>
<ArgTableRow arg="dscp" typ="num">設定在請求 IP 頭中的差分服務程式碼點，`0..63`。例如，`dscp=46`（加速轉發）對應的 ToS 位元組為 `0xb8`。預設值：0。</ArgTableRow>
<ArgTableRow arg="do-not-fragment" typ="switch">在請求中設定“不分片”標誌，使其不被分片。大於路徑 MTU 的請求隨後會失敗：路徑上鍊路較小的路由器會以狀態 `fragmentation needed and DF set` 應答；大於出介面 MTU 或路由器已學到的路徑 MTU 的請求會以 `packet too large and cannot be fragmented` 失敗。可與 `size` 一起用於探測路徑 MTU。</ArgTableRow>
<ArgTableRow arg="src-address" typ="alt { ip-src-address: ipAddr
, ip6-src-address: ip6Addr
 }">請求的源地址。當測試需要特定地址時使用，例如用 LAN 地址測試 IPsec 站點到站點隧道。預設值：路由的 `pref-src`，否則為出介面的地址。</ArgTableRow>
<ArgTableRow arg="arp-ping" typ="bool">傳送 ARP 請求而不是 ICMP 回顯請求，以到達直接相連的 IPv4 子網上丟棄 ICMP 的主機。需要 `interface`；沒有該引數時命令會以 `interface needs to be specified for arp ping` 失敗。`host` 顯示應答主機的 MAC 地址。預設值：no。</ArgTableRow>
<ArgTableRow arg="count" typ="num">要傳送的請求數量。不使用該引數時，ping 會一直執行，直到你用 Ctrl-C 停止。在指令碼中，該命令返回應答的數量。預設值：無限。</ArgTableRow>
<ArgTableRow arg="nd-ping" typ="bool">使用 IPv6 鄰居發現而不是 ICMPv6 回顯：路由器傳送鄰居請求（NS），並將鄰居通告（NA）計為應答。僅對鏈路本地 IPv6 地址有效；全域性地址還需要 `interface`。預設值：no。</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum">請求發出的介面。當沒有經過該介面到達目標的路由時，路由器將目標視為在該介面上直接相連，併為其傳送 ARP 請求。`arp-ping`、對全域性地址的 `nd-ping` 以及 IPv6 鏈路本地地址都需要該引數（或者將介面作為地址字尾給出）。</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">ping 執行的 VRF。只接受 VRF；為策略路由而存在的路由表會被拒絕，並提示 `input does not match any value of vrf`。預設值：main。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="seq" typ="num">該行所對應應答的請求編號。對組播請求的應答共用一個編號。</ArgTableRow>
<ArgTableRow arg="host" typ="alt { ipv6-address: ip6Addr
, mac-address: macAddr
, ip-address: ipAddr
 }">應答來自的地址：主機，或路徑上傳送了 ICMP 錯誤的路由器（參見 `status`）。對於 ARP ping 和 MAC ping，為應答主機的 MAC 地址。</ArgTableRow>
<ArgTableRow arg="size" typ="num">收到的封包大小（位元組）。對於來自路由器的 ICMP 錯誤，為該報文的大小。</ArgTableRow>
<ArgTableRow arg="ttl" typ="num">收到的封包的 TTL（IPv4）或跳數限制（IPv6）。與傳送方所用值之差大致反映了應答經過的路由器數量。</ArgTableRow>
<ArgTableRow arg="time" typ="time">往返時間：從傳送請求到收到應答之間的時間。</ArgTableRow>
<ArgTableRow arg="status" typ="string">
IPv4 應答時為空，否則表示請求發生了什麼：
- `timeout` - 在 `interval` 內沒有收到應答。
- `net unreachable` - `host` 中的路由器沒有到達目標網路的路由，或者該處的防火牆規則以預設的 `reject` 動作拒絕了該封包。
- `host unreachable` - `host` 中的路由器報告無法到達該主機，或者該處的防火牆規則以 `icmp-host-unreachable` 拒絕了該封包。
- `admin prohibited` - `host` 中的路由器上的防火牆規則拒絕了該封包。
- `TTL exceeded` - 在 `host` 中的路由器上 TTL 耗盡，通常是由於路由環路。
- `fragmentation needed and DF set` - `host` 中的路由器有一條 MTU 更小的鏈路，且設定了 `do-not-fragment`。
- `packet too large and cannot be fragmented` - 請求大於出介面的 MTU 或已學到的路徑 MTU，且設定了 `do-not-fragment`。
- `no route to host` - 路由器沒有到達該地址的路由；對於 `nd-ping`，該地址不在直接相連的子網上。
- `echo reply` - IPv6 回顯應答。
</ArgTableRow>
<ArgTableRow arg="sent" typ="num">已傳送的請求數量。</ArgTableRow>
<ArgTableRow arg="received" typ="num">已收到的應答數量。</ArgTableRow>
<ArgTableRow arg="packet-loss" typ="num">無應答請求的佔比，以百分比表示。</ArgTableRow>
<ArgTableRow arg="min-rtt" typ="time">本次執行中最短的往返時間。</ArgTableRow>
<ArgTableRow arg="avg-rtt" typ="time">本次執行中的平均往返時間。</ArgTableRow>
<ArgTableRow arg="max-rtt" typ="time">本次執行中最長的往返時間。</ArgTableRow>
</ArgTable>
