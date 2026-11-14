---
sidebar_key: "cli-reference/routing/bgp/connection"
sidebar_position: 2
title: "connection"
sidebar_label: 'connection'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/routing/bgp/connection
captured_at: '2026-11-01T21:25:04+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/bgp/connection {#routingbgpconnection}
**條件：** !smips
**型別：** 目錄

所有連線特定引數的列表見下表。

除了連線特定引數外，模板特定引數也直接在此選單中公開，以便在簡單場景（不需要模板時）中更容易配置。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未啟用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="instance" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="remote.address" typ="address (flags=46i/+:)" unset="1">用於連線和/或監聽的遠端地址。</ArgTableRow>
<ArgTableRow arg="remote.port" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="remote.as" typ="super { as: as
, [sub-as] [ /as]
 }" unset="1">遠端 AS 號。如果未指定，BGP 將根據 OPEN 訊息自動確定遠端 AS。</ArgTableRow>
<ArgTableRow arg="remote.ttl" typ="num">可接受的最小生存時間（Time To Live），即此 TCP 連線的跳數限制。例如，如果 'ttl=255'，則只有單跳鄰居能夠建立連線。此屬性僅影響 EBGP 對等體。</ArgTableRow>
<ArgTableRow arg="remote.allowed-as" typ="enum" unset="1">包含允許連線的遠端 AS 號的 num-list 名稱。適用於動態對等體配置。</ArgTableRow>
<ArgTableRow arg="local.address" typ="address (flags=46i:)" unset="1"></ArgTableRow>
<ArgTableRow arg="local.port" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="local.ttl" typ="num">將記錄在已傳送 TCP 封包中的生存時間（跳數限制）。</ArgTableRow>
<ArgTableRow arg="local.role" typ="enum (ibgp | ibgp-rr | ebgp | ebgp-provider | ebgp-rs | ebgp-rs-client | ebgp-customer | ebgp-peer)" mandatory="1">BGP 角色。在大多數場景中，設定為 iBGP 或 eBGP。有關 BGP 角色和路由洩漏防護的更多資訊，請參閱 [路由洩漏防護](../../../user-guides/routing-and-networking-protocols/unicast/bgp/route-leak-prevention.md) 以及相應的 [RFC 9234](https://tools.ietf.org/html/rfc9234)。</ArgTableRow>
<ArgTableRow arg="tcp-md5-key" typ="string" unset="1">用於透過 TCP MD5 簽名認證連線的金鑰，如 [RFC 2385](https://tools.ietf.org/html/rfc2385) 中所述。留空以停用認證。</ArgTableRow>
<ArgTableRow arg="connect" typ="bool">是否允許路由器發起連線。</ArgTableRow>
<ArgTableRow arg="listen" typ="bool">啟用對傳入連線的監聽。如果 `remote.address` 是主機地址且已啟用監聽，則在首次成功接受後關閉監聽套接字。如果 `remote.address` 是子網且已啟用監聽，則在首次成功接受後監聽套接字會保持開啟，並硬編碼限制為 256 個開啟連線。</ArgTableRow>
<ArgTableRow arg="routing-table" typ="enum" unset="1">用於安裝路由的路由表名稱。覆蓋 instance 引數。</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum" unset="1">BGP 連線所使用的 VRF 名稱。預設使用 "main" 路由表。</ArgTableRow>
<ArgTableRow arg="templates" typ="multi { template: enum
 }" unset="1">用於繼承引數值的模板名稱列表。這是一項有用的功能，可輕鬆配置具有重疊配置選項的組。</ArgTableRow>
<ArgTableRow arg="as" typ="as" unset="1">32 位 BGP 自治系統號。該值接受 AS-Plain 或 AS-Dot 格式。使用以下格式覆蓋 instance ASN 並配置 BGP 聯盟：_`confederation_as/as`_。例如，如果你的 AS 是 34，聯盟 AS 是 43，請設定 `as=43/34`。</ArgTableRow>
<ArgTableRow arg="nexthop-choice" typ="enum (default | force-self | propagate)" unset="1">影響出站 **NEXT\_HOP** 屬性的選擇。在過濾器中設定的下一跳始終優先，並且在路由反射時不會更改，除非該下一跳是在過濾器中設定的。   default - 按 [`RFC 4271`](https://tools.ietf.org/html/rfc4271) 中所述選擇下一跳   force-self - 使用連線到對等體的介面的本地地址作為下一跳   propagate - 傳播接收到的下一跳；如果路由具有 BGP **NEXT\_HOP** 屬性，則將其用作下一跳；否則回退到預設情況。</ArgTableRow>
<ArgTableRow arg="multihop" typ="bool" unset="1">當遠端對等體距離超過一跳時啟用。此選項會影響出站下一跳的選擇，如 [`RFC 4271`](https://tools.ietf.org/html/rfc4271) 中所述（僅適用於 eBGP，不包括聯盟本地的 iBGP 對等體）。它還會影響：是否接受來自不在同一網路中的對等體的連線（此檢查使用連線的遠端地址）是否接受其 NEXT\_HOP 屬性與用於建立連線的地址不在同一網路中的傳入路由從此對等體安裝的路由的目標作用域；來自多跳或 iBGP 對等體的路由預設透過 IGP 路由解析其下一跳</ArgTableRow>
<ArgTableRow arg="hold-time" typ="alt { special: enum (infinity) { infinity:0 }
, number: time [3 .. 65535]
 }" unset="1">指定用於與對等體協商的 BGP Hold Time 值。根據 BGP 規範，如果路由器在 **OPEN** 訊息的 Hold Time 欄位指定的時間段內未收到連續的 **KEEPALIVE** 和/或 **UPDATE** 和/或 **NOTIFICATION** 訊息，則與對等體的 BGP 連線將被關閉。將使用兩個對等體中最小的 `hold-time` 值（注意，特殊值 0 或 'infinity' 低於任何其他值）*   infinity \- 永不過期連線，也從不傳送 keepalive 訊息。</ArgTableRow>
<ArgTableRow arg="keepalive-time" typ="time" unset="1">keepalive 訊息之間的間隔；如果未設定，則預設 keepalive 為 `hold-time` 的 1/3。</ArgTableRow>
<ArgTableRow arg="afi" typ="ubit (ip, ipv6, l2vpn, l2vpn-cisco, vpnv4, vpnv6, evpn)" unset="1">此對等體可交換路由資訊的地址族列表。遠端對等體必須支援 BGP capabilities 可選引數（通常都支援），才能協商除 IP 以外的任何地址族。</ArgTableRow>
<ArgTableRow arg="cisco-vpls-nlri-len-fmt" typ="enum (auto-bits | auto-bytes | bits | bytes)" unset="1">VPLS NLRI 長度格式型別。用於與 Cisco VPLS 相容。\[\[閱讀更多>>\]\]。</ArgTableRow>
<ArgTableRow arg="output.remove-private-as" typ="bool" unset="1">如果設定，則當 BGP **AS-PATH** 屬性僅包含私有 AS 號時，在傳送路由更新之前會移除該屬性。移除過程發生在應用路由過濾器之前，以及在本地 AS 號被前置到 AS 路徑之前。</ArgTableRow>
<ArgTableRow arg="output.as-override" typ="bool" unset="1">如果設定，則在向該對等體傳送路由更新之前，BGP **AS-PATH** 屬性中遠端對等體 AS 號的所有例項都會替換為本地 AS 號。發生在路由過濾器和前置操作之前。</ArgTableRow>
<ArgTableRow arg="use-bfd" typ="bool" unset="1">是否使用 BFD 協定以更快檢測連線狀態。</ArgTableRow>
<ArgTableRow arg="save-to" typ="string" unset="1">用於將 BGP 協定特定的封包內容（Exported PDU）儲存為 pcap 格式的檔名。此方法可為偵錯目的提供更簡單的對等體特定封包捕獲。</ArgTableRow>
<ArgTableRow arg="output.add-path" typ="ubit (ip, ipv6)" unset="1">為指定的地址族啟用傳送額外路徑（BGP Addpath）。</ArgTableRow>
<ArgTableRow arg="output.affinity" typ="enum (main | alone | remote-as | instance | afi | vrf | input)" unset="1">配置輸出多核處理。請閱讀 [路由協定多核支援](../../../user-guides/routing-and-networking-protocols/routing-protocol-multi-core-support.md) 文章以瞭解更多資訊。   **alone** - 每個會話的輸入和輸出在各自獨立的程式中處理，當核心和對等體很多時，這很可能是最佳選項   **afi, instance, vrf, remote-as** - 嘗試在具有相似引數的程式中執行新會話的輸入/輸出   **main** - 在主程式中執行輸入/輸出（在單核上可能提升效能，甚至在核心數較少的多核裝置上也可能如此）   **input** - 在與輸入相同的程式中執行輸出（只能為輸出親和性設定）</ArgTableRow>
<ArgTableRow arg="output.redistribute" typ="ubit (connected, static, rip, ospf, isis, bgp, vpn, dhcp, fantasy, modem, bgp-mpls-vpn, slaac)" unset="1">啟用指定路由型別的重分發。</ArgTableRow>
<ArgTableRow arg="output.filter-select" typ="enum" unset="1">用於字首選擇的路由選擇鏈名稱。如果未指定，則使用預設選擇。</ArgTableRow>
<ArgTableRow arg="output.filter-chain" typ="enum" unset="1">用於輸出字首的路由過濾器鏈名稱。如果未指定鏈，則 BGP 預設接受所有內容。</ArgTableRow>
<ArgTableRow arg="output.network" typ="enum" unset="1">用於傳送本地網路的地址列表名稱。僅當路由表中存在匹配的 IGP 路由且其 **ORIGIN** 屬性設定為 IGP 時，才會傳送該網路；其他分發方法的 **ORIGIN** 屬性設定為 INCOMPLETE。</ArgTableRow>
<ArgTableRow arg="output.network-blackhole" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="output.default-originate" typ="enum (never | if-installed | always)" unset="1">指定預設路由 (0.0.0.0/0) 的分發方法。'if-installed' 選項可用於僅在路由表中存在相應 IGP 路由時才分發預設路由。</ArgTableRow>
<ArgTableRow arg="output.default-prepend" typ="num" unset="1">前置本地 ASN 的次數。</ArgTableRow>
<ArgTableRow arg="output.no-client-to-client-reflection" typ="bool" unset="1">在路由反射器設定中停用用戶端到用戶端的路由反射。</ArgTableRow>
<ArgTableRow arg="output.no-early-cut" typ="bool" unset="1">early cut 是一種機制，用於（基於預設 RFC 行為）推測傳送的 NLRI 在被遠端對等體接收時會發生什麼。如果演算法確定 NLRI 將被丟棄，對等體甚至不會嘗試傳送它。但是，在特定場景中可能不希望出現這種行為，此時應使用此選項來停用 early cut 功能。Early cut 適用於 eBGP 會話。</ArgTableRow>
<ArgTableRow arg="output.keep-sent-attributes" typ="bool" unset="1">在記憶體中儲存已傳送字首的屬性，`dump-saved-advertisements` 命令要正常工作需要此項。預設情況下，為節省路由器記憶體，不會儲存已傳送的字首。僅在偵錯目的且需要檢視當前通告的字首時，才應啟用此選項。</ArgTableRow>
<ArgTableRow arg="input.add-path" typ="ubit (ip, ipv6)" unset="1">為指定的地址族接受收到的額外路徑（BGP Addpath）。</ArgTableRow>
<ArgTableRow arg="input.attr-error-handling" typ="enum (default | revised)"></ArgTableRow>
<ArgTableRow arg="input.affinity" typ="enum (main | alone | remote-as | instance | afi | vrf)" unset="1">
配置輸入多核處理。請閱讀 [路由協定多核支援](../../../user-guides/routing-and-networking-protocols/routing-protocol-multi-core-support.md) 文章以瞭解更多資訊。
- **alone** - 每個會話的輸入和輸出在各自獨立的程式中處理，當核心和對等體很多時，這很可能是最佳選項。
- **afi, instance, vrf, remote-as** - 嘗試在具有相似引數的程式中執行新會話的輸入/輸出。
- **main** - 在主程式中執行輸入/輸出（在單核上可能提升效能，甚至在核心數較少的多核裝置上也可能如此）。
</ArgTableRow>
<ArgTableRow arg="input.filter" typ="enum" unset="1">用於輸入字首的路由過濾器鏈名稱。這在 NLRI 處理之後發生。如果未指定鏈，則 BGP 預設接受所有內容。</ArgTableRow>
<ArgTableRow arg="input.filter-nlri" typ="enum" unset="1">過濾器鏈名稱，該鏈會在傳入的 IPv4/IPv6 NLRI 被存入記憶體之前直接對其進行過濾，從而顯著減少記憶體佔用。常規輸入過濾器鏈只能拒絕字首，這意味著它仍會佔用記憶體，並且會在 /routing 路由表中顯示為 "not active, filtered"。應用更改需要重啟會話。</ArgTableRow>
<ArgTableRow arg="input.allow-as" typ="num" unset="1">指示在丟棄字首之前，允許你自己的 AS 號在 AS-PATH 中出現的次數。</ArgTableRow>
<ArgTableRow arg="input.accept-nlri" typ="enum" unset="1">ipv4/6 地址列表的名稱。使用特定 NLRI 過濾傳入更新的快捷方式。它允許在傳入訊息甚至被解析並存入記憶體之前直接進行過濾，從而顯著減少記憶體佔用。常規輸入過濾器鏈只能拒絕字首，這意味著它仍會佔用記憶體，並且會在 /routing 路由表中顯示為 "not active, filtered"。應用更改需要重啟會話。</ArgTableRow>
<ArgTableRow arg="input.filter-communities" typ="enum" unset="1">使用特定 community 過濾傳入更新的快捷方式。它允許在傳入訊息甚至被解析並存入記憶體之前直接進行過濾，從而顯著減少記憶體佔用。常規輸入過濾器鏈只能拒絕字首，這意味著它仍會佔用記憶體，並且會在 /routing 路由表中顯示為 "not active, filtered"。應用更改需要重新整理會話。</ArgTableRow>
<ArgTableRow arg="input.filter-ext-communities" typ="enum" unset="1">使用特定 extended community 過濾傳入更新的快捷方式。它允許在傳入訊息甚至被解析並存入記憶體之前直接進行過濾，從而顯著減少記憶體佔用。常規輸入過濾器鏈只能拒絕字首，這意味著它仍會佔用記憶體，並且會在 /routing 路由表中顯示為 "not active, filtered"。應用更改需要重新整理會話。</ArgTableRow>
<ArgTableRow arg="input.filter-large-communities" typ="enum" unset="1">使用特定 large community 過濾傳入更新的快捷方式。它允許在傳入訊息甚至被解析並存入記憶體之前直接進行過濾，從而顯著減少記憶體佔用。常規輸入過濾器鏈只能拒絕字首，這意味著它仍會佔用記憶體，並且會在 /routing 路由表中顯示為 "not active, filtered"。應用更改需要重新整理會話。</ArgTableRow>
<ArgTableRow arg="input.accept-communities" typ="enum" unset="1">使用特定 community 過濾傳入更新的快捷方式。它允許在傳入訊息甚至被解析並存入記憶體之前直接進行過濾，從而顯著減少記憶體佔用。常規輸入過濾器鏈只能拒絕字首，這意味著它仍會佔用記憶體，並且會在 /routing 路由表中顯示為 "not active, filtered"。應用更改需要重新整理會話。</ArgTableRow>
<ArgTableRow arg="input.accept-ext-communities" typ="enum" unset="1">使用特定 extended community 過濾傳入更新的快捷方式。它允許在傳入訊息甚至被解析並存入記憶體之前直接進行過濾，從而顯著減少記憶體佔用。常規輸入過濾器鏈只能拒絕字首，這意味著它仍會佔用記憶體，並且會在 /routing 路由表中顯示為 "not active, filtered"。應用更改需要重新整理會話。</ArgTableRow>
<ArgTableRow arg="input.accept-large-communities" typ="enum" unset="1">使用特定 large community 過濾傳入更新的快捷方式。它允許在傳入訊息甚至被解析並存入記憶體之前直接進行過濾，從而顯著減少記憶體佔用。常規輸入過濾器鏈只能拒絕字首，這意味著它仍會佔用記憶體，並且會在 /routing 路由表中顯示為 "not active, filtered"。應用更改需要重新整理會話。</ArgTableRow>
<ArgTableRow arg="input.filter-unknown" typ="enum" unset="1">使用特定 "unknown" 屬性過濾傳入更新的快捷方式。它允許在傳入訊息甚至被解析並存入記憶體之前直接進行過濾，從而顯著減少記憶體佔用。常規輸入過濾器鏈只能拒絕字首，這意味著它仍會佔用記憶體，並且會在 /routing 路由表中顯示為 "not active, filtered"。應用更改需要重新整理會話。</ArgTableRow>
<ArgTableRow arg="input.limit-process-routes-ipv4" typ="enum (10 | 100 | 1000 | 10000 | 100000 | 1000000 | 10000000) { 10:10, 100:100, 1000:1000, 10000:10000, 100000:100000, 1000000:1000000, 10000000:10000000 }" unset="1">嘗試將接收的 IPv4 路由數量限制為指定數目。此數目並不代表該對等體將要安裝到路由表中的確切路由數量。如果達到限制，必須使用 [BGP 會話 "clear"](./session/clear.md) 命令重設該標誌。</ArgTableRow>
<ArgTableRow arg="input.limit-process-routes-ipv6" typ="enum (10 | 100 | 1000 | 10000 | 100000 | 1000000 | 10000000) { 10:10, 100:100, 1000:1000, 10000:10000, 100000:100000, 1000000:1000000, 10000000:10000000 }" unset="1">嘗試將接收到的 IPv6 路由數量限制為指定數量。此數量並不表示對等體將要安裝到路由表中的確切路由數。如果達到限制，必須使用 BGP 會話 "clear" 命令來重設標誌。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="local.default-address" typ="address (flags=46i:)"></ArgTableRow>
</ArgTable>
