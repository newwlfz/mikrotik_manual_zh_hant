---
sidebar_key: "cli-reference/ip/dns"
title: "dns"
sidebar_label: 'dns'
source: https://manual.mikrotik.com/docs/cli-reference/ip/dns
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/dns {#ipdns}
**型別：** 設定目錄

DNS 解析器和快取的設定。路由器將它們用於自身的查詢，並且在 `allow-remote-requests=yes` 時，應答來自用戶端的 DNS 查詢。此選單中的更改會立即生效；在那一刻到達的查詢可能會得不到應答，用戶端會重新發送它。快取會保留。有關概述和示例，請參閱 [DNS](../../../network-management/dns.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="servers" typ="multi { servers: address (flags=46v)
 }">上游 DNS 伺服器，IPv4 或 IPv6 地址，可選帶 `@<vrf>` 以訪問另一個 VRF 中的伺服器。路由器按列出的順序先嚐試這些伺服器，再嘗試 `dynamic-servers`。它會等待 `query-server-timeout` 以獲得應答，然後嘗試下一個伺服器。當某個伺服器應答後，路由器會在後續查詢中繼續使用它。</ArgTableRow>
<ArgTableRow arg="use-doh-server" typ="string">DNS over HTTPS (DoH) 伺服器的 URL，例如 `https://cloudflare-dns.com/dns-query`。設定後，路由器會透過一條複用的 HTTPS 連線（TCP 埠 443）把所有查詢傳送到該伺服器，而 `servers` 和 `dynamic-servers` 僅用於查詢 DoH 伺服器的主機名（透過 UDP 埠 53 進行 A 和 AAAA 查詢）；為該主機名配置靜態條目也可以。路由器不會回退到普通 DNS：當 DoH 伺服器不應答時，用戶端會在 `query-total-timeout` 後收到 SERVFAIL，日誌會顯示 `dns,error DoH server connection error: ...`，例如 `Connection refused` 或 `timeout connecting`。靜態 `FWD` 條目仍會透過普通 DNS 使用它們自己的伺服器。只能設定一個 DoH 伺服器。ARM64 和 x86 裝置（包括 CHR）使用 HTTP/2；其他架構使用 HTTP/1.1，因此要求 HTTP/2 的 DoH 服務（例如 Quad9）僅在 ARM64 和 x86 上可用。預設值：空。</ArgTableRow>
<ArgTableRow arg="verify-doh-cert" typ="bool">路由器是否使用 `/certificate` 和內建信任儲存來驗證 DoH 伺服器的證書。預設值：否。</ArgTableRow>
<ArgTableRow arg="doh-max-server-connections" typ="num">到 DoH 伺服器的最大 HTTPS 連線數。預設值：5。</ArgTableRow>
<ArgTableRow arg="doh-max-concurrent-queries" typ="num">同時進行的 DoH 查詢最大數量。預設值：50。</ArgTableRow>
<ArgTableRow arg="doh-timeout" typ="time">路由器等待 DoH 伺服器應答的時間。預設值：5s。</ArgTableRow>
<ArgTableRow arg="allow-remote-requests" typ="bool">路由器是否在其地址的 UDP 和 TCP 埠 53 上應答來自其他裝置的 DNS 查詢。設為 `no` 時，只有路由器自身使用解析器。預設防火牆會丟棄來自 WAN 側的連線；僅允許來自你自己網路的埠 53，這樣路由器就不會應答來自網際網路的查詢。預設值：否。</ArgTableRow>
<ArgTableRow arg="max-udp-packet-size" typ="num">UDP 上 DNS 訊息的最大大小，單位為位元組。預設值：4096。</ArgTableRow>
<ArgTableRow arg="query-server-timeout" typ="time">路由器在嘗試下一個上游伺服器之前，等待某個上游伺服器應答的時間。預設值：2s。</ArgTableRow>
<ArgTableRow arg="query-total-timeout" typ="time">路由器嘗試解析一個查詢的總時長。如果在此時間內沒有伺服器應答，用戶端會收到 SERVFAIL 應答。請結合 `query-server-timeout` 和伺服器數量進行設定。預設值：10s。</ArgTableRow>
<ArgTableRow arg="max-concurrent-queries" typ="num">可同時等待上游應答的最大查詢數。達到該限制時，路由器會丟棄新查詢，包括它本可從快取中應答的查詢，直到某個等待中的查詢完成。預設值：100。</ArgTableRow>
<ArgTableRow arg="max-concurrent-tcp-sessions" typ="num">同時來自用戶端的 TCP 連線最大數量。預設值：20。</ArgTableRow>
<ArgTableRow arg="cache-size" typ="num">DNS 快取的大小，單位為 KiB。Adlist 條目也會儲存在快取中。預設值：2048。</ArgTableRow>
<ArgTableRow arg="cache-max-ttl" typ="time">路由器將上游應答保留在快取中的最長時間。來自上游伺服器的更長 TTL 會被縮短為此值，用戶端會獲得剩餘時間。靜態條目保留自己的 `ttl`。預設值：1w。</ArgTableRow>
<ArgTableRow arg="address-list-extra-time" typ="time">在路由器刪除由帶 `address-list` 的靜態條目建立的動態地址列表條目之前，加到應答 TTL 上的時間。預設值：0s。</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">當 `allow-remote-requests=yes` 時，解析器為用戶端提供應答所在的 VRF。其他 VRF 中的用戶端不會得到應答；路由器自身的查詢仍可正常工作。不帶 VRF 字尾的上游伺服器透過主路由表訪問；要訪問另一個 VRF 中的伺服器，請在 `servers` 中將其寫為 `address@vrf`，例如 `servers=10.0.0.1@vrf1,1.1.1.1`。預設值：main.</ArgTableRow>
<ArgTableRow arg="mdns-repeat-ifaces" typ="multi { iface_enum
 }">路由器在其間重複多播 DNS (mDNS) 的介面。路由器會在每個列出的介面上接收 IPv4 mDNS 封包（UDP 埠 5353 發往 224.0.0.251），並從其在其他列出介面上的自身地址再次傳送這些封包，以便不同網路中的裝置能夠相互發現。IPv6 mDNS (ff02::fb) 不會被重複。路由器會自行處理這些封包，因此它們會經過防火牆的 input 鏈：input 規則不得在這些介面上丟棄 UDP 埠 5353（預設防火牆會在 `LAN` 介面上接受它）。請使用承載多播的介面，例如 Ethernet、VLAN、bridge 或 EoIP 介面；WireGuard 等三層隧道不承載多播。預設值：空（不重複）。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="dynamic-servers" typ="multi { dynamic-servers: address (flags=46v)
 }">從其他服務學習到的 DNS 伺服器，例如透過 `use-peer-dns=yes` 從 DHCP 用戶端學習到的伺服器。路由器會在 `servers` 之後嘗試它們。</ArgTableRow>
<ArgTableRow arg="cache-used" typ="num">`cache-size` 中已使用的部分，單位為 KiB。</ArgTableRow>
</ArgTable>
