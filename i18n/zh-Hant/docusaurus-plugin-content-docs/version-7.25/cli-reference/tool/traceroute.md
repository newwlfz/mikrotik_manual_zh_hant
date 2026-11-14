---
sidebar_key: "cli-reference/tool/traceroute"
sidebar_position: 24
title: "traceroute"
sidebar_label: 'traceroute'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/tool/traceroute
captured_at: '2026-11-01T21:26:00+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/traceroute {#tooltraceroute}
**型別：** 命令

跟蹤到主機的路徑：傳送 TTL 逐漸增大的探測包，並列出做出應答的路由器，以及每一跳的丟包和往返統計資訊。跟蹤會每秒重複一次，直到你將其停止、完成 `count` 輪或 `duration` 結束。有關示例以及如何解讀結果，請參閱 [跟蹤路由](../../diagnostics-monitoring-and-troubleshooting/traceroute.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="address" typ="address (flags=46viD)">目標的 IP 或 IPv6 地址，或 DNS 名稱。名稱由路由器的 DNS 解析器解析。請參閱[地址標誌](../index.md#address-flags)。</ArgTableRow>
<ArgTableRow arg="port" typ="num">使用 `protocol=udp` 的探測包的目標 UDP 埠。每個探測包都使用同一埠。預設值：33434。</ArgTableRow>
<ArgTableRow arg="size" typ="num">每個探測包作為完整 IP 封包的大小，以位元組為單位，包括 IP 頭。預設值：28，即不帶負載的 IPv4 探測包。</ArgTableRow>
<ArgTableRow arg="dscp" typ="num">探測包 IP 頭中設定的 DSCP 值。</ArgTableRow>
<ArgTableRow arg="do-not-fragment" typ="switch">在探測包的 IP 頭中設定 Don't Fragment 標誌。當 `size` 較大時，路徑上鍊路較小的路由器會以 `fragmentation needed from <address>` 應答。</ArgTableRow>
<ArgTableRow arg="use-dns" typ="bool">顯示各跳的主機名而不是其地址。名稱透過路由器的 DNS 解析器以反向 DNS 查詢進行查詢；沒有反向 DNS 記錄的跳會保留其地址。預設值：no。</ArgTableRow>
<ArgTableRow arg="count" typ="num">要執行的輪數。未指定 `count` 時，跟蹤會每秒重複一次，直到你將其停止。預設值：unlimited。</ArgTableRow>
<ArgTableRow arg="max-hops" typ="num">要嘗試的最高 TTL：當目標不應答時，該輪會在經過這麼多跳後結束。預設值：30。</ArgTableRow>
<ArgTableRow arg="protocol" typ="enum (icmp | udp)">
探測包的型別。
- `icmp`（預設）- ICMP 回顯請求。目標以回顯應答進行應答。
- `udp` - 發往 `port` 的 UDP 封包。目標以 ICMP 埠不可達訊息進行應答。
</ArgTableRow>
<ArgTableRow arg="src-address" typ="alt { ipv6-address: ip6Addr
, ip-address: ipAddr
 }">探測包的源地址。與源地址匹配的路由規則會應用於探測包。預設值：路由的 `pref-src`，否則為出介面的地址。</ArgTableRow>
<ArgTableRow arg="timeout" typ="time">每個探測包在傳送下一個探測包之前等待其應答的時間。預設值：1s。</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">探測包使用的路由表所屬的 VRF。僅接受 VRF；為策略路由建立的路由表會被拒絕。預設值：main。</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum">傳送探測包所使用的介面。當透過該介面沒有覆蓋目標的路由時，路由器會將目標視為直接連線在該介面上，併為其傳送 ARP 請求。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="address" typ="object { address: alt { name: string
, address: ip6Addr
 }
 }">為此跳做出應答的路由器的地址，或當 `use-dns=yes` 時為其主機名。當發往該跳的探測包均未得到應答時為空。</ArgTableRow>
<ArgTableRow arg="loss" typ="num">發往該跳的探測包中未得到應答的百分比。</ArgTableRow>
<ArgTableRow arg="sent" typ="num">發往該跳的探測包數量。</ArgTableRow>
<ArgTableRow arg="last" typ="num">來自該跳的最後一個應答的往返時間。當最後一個探測包未得到應答時，列印的表格會顯示 `timeout`。</ArgTableRow>
<ArgTableRow arg="avg" typ="num">來自該跳的應答的平均往返時間。</ArgTableRow>
<ArgTableRow arg="best" typ="num">來自該跳的應答的最短往返時間。</ArgTableRow>
<ArgTableRow arg="worst" typ="num">來自該跳的應答的最長往返時間。</ArgTableRow>
<ArgTableRow arg="std-dev" typ="num">該跳往返時間的標準差：即各輪之間的變化程度。</ArgTableRow>
<ArgTableRow arg="status" typ="string">該跳以錯誤而不是 time exceeded 做出應答，例如 `network unreachable from 203.0.113.1`（無路由，或防火牆使用預設訊息執行 `reject`）、`host unreachable from 203.0.113.1`、`packet filtered from 203.0.113.1`（防火牆以管理禁止為由拒絕探測包）或 `fragmentation needed from 203.0.113.6`（在 `do-not-fragment` 下，探測包大於下一鏈路的 MTU）。該輪會在這樣的跳處結束。當該跳正常應答時為空。</ArgTableRow>
<ArgTableRow arg="error" typ="string"></ArgTableRow>
</ArgTable>
