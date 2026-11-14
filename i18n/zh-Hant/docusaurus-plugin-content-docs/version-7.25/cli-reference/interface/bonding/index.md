---
sidebar_key: "cli-reference/interface/bonding/index"
sidebar_position: 1
title: "bonding"
sidebar_label: 'bonding'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/bonding
captured_at: '2026-11-01T21:22:21+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/bonding {#interfacebonding}
**型別：** 目錄

[繫結](../../../high-availability-solutions/bonding.md) 用於高可用性解決方案。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">disabled.</ArgTableRow>
<ArgTableRow arg="R" typ="running">running.</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">Bonding 介面的名稱。</ArgTableRow>
<ArgTableRow arg="mtu" typ="num">最大傳輸單元，單位為位元組。必須小於或等於 bonding 從介面中最小的 L2MTU 值。</ArgTableRow>
<ArgTableRow arg="forced-mac-address" typ="macAddr">預設情況下，bonding 介面將使用第一個選定的從介面的 MAC 地址。此屬性允許為 bond 介面配置靜態 MAC 地址（全零、廣播或組播地址將不會生效）。RouterOS 會自動更改從介面的 MAC 地址，並且它將在 [`/interface/ethernet`](../ethernet/index.md) 配置匯出中可見</ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp) { disabled:0, enabled:1, proxy-arp:2, reply-only:3, local-proxy-arp:4 }">[地址解析協定](../../../getting-started/networking-fundamentals/index.md#arp-and-tying-it-all-together) 模式。</ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { arp-timeout: enum (auto) { auto:0 }
, arp-timeout: time
 }">在未收到來自 IP 的封包後，ARP 記錄在 ARP 表中保留多長時間。值 auto 等於 IP/Settings 中 arp-timeout 的值，預設為 30s。</ArgTableRow>
<ArgTableRow arg="slaves" typ="multi { array-id, slave: iface_enum
 }">至少兩個用逗號分隔的、類似乙太網的介面，將用於 bonding。</ArgTableRow>
<ArgTableRow arg="mode" typ="enum (balance-rr | active-backup | balance-xor | broadcast | 802.3ad | balance-tlb | balance-alb) { balance-rr:0, active-backup:1, balance-xor:2, broadcast:3, 802.3ad:4, balance-tlb:5, balance-alb:6 }">
指定一種 bonding 策略。
- `802.3ad` - LACP，IEEE 802.3ad 動態鏈路聚合。在此模式下，介面會聚合到一個組中，其中每個從介面具有相同的速率。它提供容錯和負載均衡。傳出流量的從介面選擇根據 `transmit-hash-policy` 進行。
- `active-backup` - 提供鏈路備份，同一時間只有一個從介面處於活動狀態。
- `balance-alb` - 自適應負載均衡，傳出和傳入流量均得到均衡。裝置驅動程式應支援更改其 MAC 地址。
- `balance-rr` - 輪詢負載均衡。bonding 介面中的從介面將按順序傳送和接收資料。它提供負載均衡和容錯。
- `balance-tlb` - 傳出流量根據當前負載進行分配。傳入流量不進行均衡，由當前從介面接收。如果接收從介面發生故障，則另一個從介面會接管故障從介面的 MAC 地址。
- `balance-xor` - 靜態 LAG，基於 `transmit-hash-policy` 進行傳輸。此模式提供負載均衡和容錯。
- `broadcast` - 在所有介面上廣播相同的資料。這提供容錯，但會在一些較慢的機器上降低流量吞吐量。

配備 Marvell Prestera 交換器和 88E6393X、88E6191X、88E6190 交換晶片的 MikroTik 裝置支援 bonding 介面的橋接硬體解除安裝。  
只有 `802.3ad`（LACP）、`balance-xor`（靜態 LAG）和 `active-backup` bonding 模式會進行硬體解除安裝，其他 bonding 模式將使用 CPU 資源。
</ArgTableRow>
<ArgTableRow arg="primary" typ="iface_enum { none:0 }">控制活動從埠之間的主介面，僅適用於 `active-backup`、`balance-tlb` 和 `balance-alb` 模式。對於 `active-backup` 模式，它控制哪個處於執行狀態的介面應傳送和接收流量。對於 `balance-tlb` 模式，它控制哪個處於執行狀態的介面應接收所有流量，而對於 `balance-alb` 模式，它控制哪個介面應接收未均衡的流量（非 IPv4 流量）。當沒有選擇任何介面作為主介面時，裝置將自動選擇配置為第一個的介面。</ArgTableRow>
<ArgTableRow arg="link-monitoring" typ="enum (none | arp | mii) { none:0, arp:1, mii:2 }">
用於監控鏈路的方法。某些 bonding 模式需要特定的鏈路監控才能正常工作。
- `arp` - 使用 ARP 判斷遠端介面是否可達。
- `mii` - 使用 Media Independent Interface 判斷鏈路狀態。鏈路狀態的判斷依賴於裝置驅動程式。
- `none` - 不進行鏈路監控。
</ArgTableRow>
<ArgTableRow arg="arp-interval" typ="time">以毫秒為單位的時間，定義監控 ARP 請求的頻率。</ArgTableRow>
<ArgTableRow arg="arp-ip-targets" typ="multi { array-id, arp-target: ipAddr
 }">如果 link-monitoring 設定為 arp，則將監控的 IP 目標地址。可以指定多個 IP 地址，用逗號分隔。</ArgTableRow>
<ArgTableRow arg="mii-interval" typ="time">監控鏈路故障的頻率（僅在 link-monitoring 為 mii 時使用）。</ArgTableRow>
<ArgTableRow arg="down-delay" typ="time">如果檢測到鏈路故障，bonding 介面會在 down-delay 時間內被停用。僅在 link-monitoring 設定為 mii 時生效。</ArgTableRow>
<ArgTableRow arg="up-delay" typ="time">如果鏈路已恢復，bonding 介面會在 up-delay 時間內被停用。僅在 link-monitoring 設定為 mii 時生效。</ArgTableRow>
<ArgTableRow arg="lacp-rate" typ="enum (30secs | 1sec) { 30secs:0, 1sec:1 }">LACP 速率指定 bonding 對等體之間交換 LACPDU 的頻率。`1sec` - 短超時。`30secs` - 長超時。</ArgTableRow>
<ArgTableRow arg="transmit-hash-policy" typ="enum (layer-2 | layer-3-and-4 | layer-2-and-3 | encap-2-and-3 | encap-3-and-4) { layer-2:0, layer-3-and-4:1, layer-2-and-3:2, encap-2-and-3:3, encap-3-and-4:4 }">
選擇在 balance-xor 和 802.3ad 模式下用於從介面選擇的傳輸雜湊策略。
- `layer-2` - 使用硬體 MAC 地址的 XOR 來生成雜湊。此演算法會將發往特定網路對等體的所有流量放在同一個從介面上。此演算法符合 802.3ad。
- `layer-2-and-3` - 此策略使用 layer2 和 layer3 協定資訊的組合來生成雜湊。使用硬體 MAC 地址和 IP 地址的 XOR 來生成雜湊。此演算法會將發往特定網路對等體的所有流量放在同一個從介面上。對於非 IP 流量，公式與 layer2 傳輸雜湊策略相同。此策略旨在提供比僅使用 layer2 更均衡的流量分佈，尤其是在需要 layer3 閘道器裝置才能到達大多數目標的環境中。此演算法符合 802.3ad。
- `layer-3-and-4` - 此策略在可用時使用上層協定資訊來生成雜湊。這允許發往特定網路對等體的流量跨越多個從介面，儘管單個連線不會跨越多個從介面。對於分片的 TCP 或 UDP 封包以及所有其他 IP 協定流量，會省略源埠和目標埠資訊。對於非 IP 流量，公式與 layer2 傳輸雜湊策略相同。此演算法不完全符合 802.3ad。
- `encap-2-and-3` - 此策略在流量分配方面類似於 layer-2-and-3 方法，但使用一個過程來同時分析封裝的封包頭部。如果使用封裝協定（如隧道），它可能會選擇內部頭部而不是外部頭部。當 6to4、GRE、GRE6、IPIP、IPIP6、PPPoE 或 PPTP 等隧道執行在 bonding 介面上時，RouterOS 可以使用此功能。
- `encap-3-and-4` - 此策略在流量分配方面類似於 layer-3-and-4 方法，但使用一個過程來同時分析封裝的封包頭部。如果使用封裝協定（如隧道），它可能會選擇內部頭部而不是外部頭部。當 6to4、GRE、GRE6、IPIP、IPIP6、PPPoE 或 PPTP 等隧道執行在 bonding 介面上時，RouterOS 可以使用此功能。
</ArgTableRow>
<ArgTableRow arg="min-links" typ="num">bonding 變為活動狀態需要多少個活動從鏈路。</ArgTableRow>
<ArgTableRow arg="mlag-id" typ="num">更改 bonding 介面的 [MLAG](../../../high-availability-solutions/multi-chassis-link-aggregation-group.md) ID。兩個對等裝置上應使用相同的 MLAG ID 才能成功建立單個 MLAG。 不應將 [`mlag-peer-port`](../bridge/index.md#mlag-peer-port) 與 MLAG ID 一起配置。</ArgTableRow>
<ArgTableRow arg="lacp-user-key" typ="num">指定埠鍵的高 10 位。低 6 位會根據各個埠的鏈路速率和雙工模式自動分配。</ArgTableRow>
<ArgTableRow arg="lacp-mode" typ="enum (passive | active) { passive:0, active:1 }">
指定埠是主動還是被動參與 LACP。
- `active` - 埠主動發起 LACP 通訊。
- `passive` - 埠僅響應 LACP 訊息。
</ArgTableRow>
<ArgTableRow arg="lacp-system-id" typ="macAddr">指定用於 LACP 協商的 LACP 系統 ID。</ArgTableRow>
<ArgTableRow arg="lacp-system-priority" typ="num">指定用於 LACP 協商的 LACP 系統優先順序。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="mac-address" typ="macAddr">bonding 介面的 MAC 地址。</ArgTableRow>
</ArgTable>
