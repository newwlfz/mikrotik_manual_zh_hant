---
sidebar_key: "virtual-private-networks/eoip"
sidebar_position: 2
title: "EoIP"
sidebar_label: "EoIP"
description: "MikroTik RouterOS 中的 Ethernet over IP (EoIP) 是一種二層隧道協定，它在 GRE 封包中於兩臺路由器之間傳輸完整的乙太網幀，從而將同一個廣播域擴充套件到任意 IP 網路——支援橋接、隧道上的 RSTP、MAC 地址控制、可選的 IPsec 加密，並且兩端需使用匹配的 tunnel-id。"
tags:
  - 'eoip'
  - 'bridging'
source: https://manual.mikrotik.com/docs/virtual-private-networks/eoip
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Ethernet over IP (EoIP) 是 MikroTik RouterOS 協定，它在 IP 網路上兩臺路由器之間建立乙太網隧道。它基於 GRE 封裝（RFC 1701 和 RFC 1702），透過路由 IP 基礎設施傳輸完整的乙太網幀，從而有效地在遠端站點之間擴充套件一個二層網路。EoIP 使用自己的 GRE 協定型別，因此 EoIP 隧道不會與通用 GRE 或 Ethernet-over-GRE 隧道互通。EoIP 是 MikroTik 協定，沒有公開規範。一些其他系統包含自己的非官方實現，例如 OpenBSD 中的 `eoip` 介面；MikroTik 不維護這些實現，也不保證與其相容。

EoIP 隧道介面在 RouterOS 中顯示為虛擬乙太網介面。加入網橋後，它會轉發所有乙太網流量——廣播、組播和非 IP 協定——就像端點透過物理乙太網鏈路連線一樣。RouterOS 透過任意 IP 傳輸（直接鏈路或網際網路）連線兩個端點，因此 EoIP 通常用於跨路由網路或無線鏈路橋接 LAN 網段，並與 IPsec 結合時用於跨加密隧道擴充套件 LAN。

EoIP 在 [`/interface/eoip`](../cli-reference/interface/eoip.md)（基於 IPv4）和 [`/interface/eoipv6`](../cli-reference/interface/eoipv6.md)（基於 IPv6）選單中配置。

## 隧道工作原理 {#how-the-tunnel-works}

在 IPv4 上，路由器將整個乙太網幀——目的和源 MAC 地址、EtherType 和有效載荷——放入 GRE 分組（外層 IP 協定 47）中，併發送到遠端隧道端點。接收路由器對其解封裝，並將原始幀注入其本地網橋。隧道承載另一端網橋傳送的任何內容：廣播、ARP、RSTP 和其他協定幀都透過隧道傳輸，因此橋接的網路表現得像一個乙太網段。

IPv6 上的 EoIP（`/interface/eoipv6`）使用不同的封裝，而不是 GRE：乙太網幀位於下一頭部為 97（EtherIP）的 IPv6 分組中，前面是一個攜帶隧道 ID 的 2 位元組頭部。頭部佈局與標準 EtherIP（RFC 3378）不同，因此 EoIPv6 隧道不會與標準 EtherIP 隧道或 IPv6 中承載的基於 GRE 的 EoIP 互通。

路由器在遠端應答後將隧道視為 **執行中**（`R` 標誌）。Keepalive 可保持此狀態：路由器每隔 keepalive 間隔探測遠端，當對端在 `interval × retries` 時間內沒有應答時，執行標誌被移除。Keepalive 預設啟用（`10s,10`）；最小間隔為 1 秒，將其設定為停用值（`0,0`、`off`、`none`）會被拒絕。可以透過取消設定 `keepalive` 屬性來關閉它（對於 IPv4 隧道為 `/interface/eoip/unset <name> keepalive`，或對 `/interface/eoipv6` 執行相同操作）——關閉 keepalive 後，當對端停止應答時不會移除執行標誌。為加快故障切換，請縮短間隔：使用 `keepalive=1s,2` 時，失效對端會在大約兩秒內被檢測到。

每個隧道由 `tunnel-id` 標識（任意 0 到 65535 的值）。兩端必須使用相同的 `tunnel-id` 流量才能透過——路由器會丟棄攜帶不同 id 的隧道幀和 keepalive。id 不匹配時執行標誌不會出現，並且在執行中的隧道一端 id 發生變化時，該標誌會在 `interval × retries` 後被移除。關閉 keepalive 後，無論 id 如何，執行標誌都保持存在。

:::tip
EoIP 會為其傳送的每個隧道幀增加 42 位元組（帶 key 的 8 位元組 GRE 頭、14 位元組內部 Ethernet 頭、20 位元組外部 IP 頭）。使用預設的 `mtu=auto` 時，路由器會相應調整隧道大小：對於 IPv4 上的 EoIP，在 1500 位元組路徑上，`actual-mtu` 為 1458。IPv6 上的 EoIP 會增加 56 位元組（2 位元組 EoIPv6 頭、14 位元組內部 Ethernet 頭、40 位元組 IPv6 頭），因此其 `actual-mtu` 為 1444。在這兩種情況下，`l2mtu` 都保持為 65535。使用預設的 `dont-fragment=no` 時，如果幀大於路徑可無分片承載的大小，該幀會在外部封包上被拆分為 IP 分片（使用 `dont-fragment=inherit` 且設定了 DF 位時，該幀反而會被丟棄）。網橋會轉發最大不超過 `l2mtu`（65535）的幀，因此超大幀會到達隧道並在外部封包上被分片——請讓底層路徑 MTU 足夠大，以容納你要橋接的幀，並且在巨型幀或全尺寸幀必須穿過隧道時，避免依賴分片。
:::

所有 EoIP 屬性在 [`/interface/eoip`](../cli-reference/interface/eoip.md) 和 [`/interface/eoipv6`](../cli-reference/interface/eoipv6.md) CLI 參考文件中均有描述。

## MAC 地址 {#mac-addresses}

為網橋上的每個隧道分配獨立的 MAC 地址 —— 生成樹和 MAC 學習都假定每個網橋埠具有互不相同的 MAC 地址。隧道的 MAC 地址會自動生成為本地管理地址（例如 `FE:...`），而 RouterOS 也接受你自行設定的任意值。自動生成的地址無法保證在各路由器之間唯一，因此在橋接環境中使用多個隧道時，請為每個隧道分配一個你自己指定的獨立地址：

```ros
/interface/eoip/set eoip-main mac-address=02:00:5E:80:00:01
```

在你自行分配的地址上設定本地管理位（第一個八位位元組的第二位，例如 `02:...` 中的形式）；IANA 保留範圍 **00:00:5E:80:00:00 - 00:00:5E:FF:FF:FF** 專為此類私有單播地址預留。更改執行中隧道的 MAC 地址會使 running 標誌短暫丟失，直到遠端再次響應為止。

## 加密隧道 {#encrypting-the-tunnel}

在兩端設定 `ipsec-secret`，即可使用預共享金鑰加密隧道 —— 隨後 RouterOS 會自動為該隧道建立動態 IPsec peer 和 policy。

在 `/interface/eoip`（IPv4）上，IPsec 與 fast path 互斥：請先在隧道上設定 `allow-fast-path=no`，否則路由器會拒絕 `ipsec-secret` 值。僅移除金鑰並不會重新啟用 fast path —— 該限制會一直存在，直到刪除隧道為止（刪除隧道同時也會移除動態 IPsec 物件）。`/interface/eoipv6` 沒有 `allow-fast-path` 屬性，因此 IPsec 無需該步驟即可工作。

## 示例：透過無線鏈路橋接兩個站點 {#example-bridge-two-sites-over-a-wireless-link}

本示例透過無線點對點鏈路橋接兩個站點的 LAN，使兩個站點共享同一個二層廣播域。無線 station 不能直接橋接；如果不使用 WDS，則可透過無線鏈路上的 EoIP 隧道實現相同結果。

![EoIP tunnel between two routers](/img/f10b94c88193db8a.webp)

假定路由器之間的無線鏈路已建立——此處僅展示 EoIP 和橋接配置。相同的命令也適用於路由器之間的任意 IP 鏈路，無論是有線還是透過網際網路。

在 AP 路由器上建立 EoIP 隧道：

```ros
/interface/eoip/add name=eoip-remote remote-address=10.0.0.2 tunnel-id=1
```

名稱是任意的（AP 上為 `eoip-remote`，station 上為 `eoip-main`）——關鍵在於兩個 `tunnel-id` 必須匹配，並且每個 `remote-address` 都指向另一臺路由器。

驗證隧道已建立——當遠端響應後，會出現 `R` 標誌：

```ros
/interface/eoip/print
```

執行中的隧道輸出如下所示（請核對 `R` 標誌、在 1500 位元組路徑上的 `mtu=auto` 與 `actual-mtu=1458`，以及本地管理的 `FE:...` MAC）：

```text
Flags: R - RUNNING
0 R name="eoip-remote" mtu=auto actual-mtu=1458 l2mtu=65535
    mac-address=FE:7D:4A:93:14:56 arp=enabled arp-timeout=auto arp-accept=no
    loop-protect=default loop-protect-status=off loop-protect-send-interval=5s
    loop-protect-disable-time=5m local-address=0.0.0.0 remote-address=10.0.0.2
    tunnel-id=1 keepalive=10s,10 dscp=inherit clamp-tcp-mss=yes
    dont-fragment=no allow-fast-path=yes
```

在 station 路由器上建立匹配的隧道——`tunnel-id` 和 `remote-address` 必須指向另一端：

```ros
/interface/eoip/add name=eoip-main remote-address=10.0.0.1 tunnel-id=1
```

用 EoIP 隧道橋接本地介面。檢查每臺路由器上哪個網橋已承載 LAN 埠：

```ros
/interface/bridge/port/print
```

在 AP 路由器上，把 EoIP 介面新增到承載本地 LAN 的網橋上——預設的 RouterOS 配置中已經存在這樣一個網橋：

```ros
/interface/bridge/port/add bridge=bridge1 interface=eoip-remote
```

在 station 路由器上，把 EoIP 隧道新增到同一個 LAN 網橋：

```ros
/interface/bridge/port/add bridge=bridge1 interface=eoip-main
```

:::note
在預設的 RouterOS 配置中，所有 LAN 埠都已經位於預設網橋中，因此 EoIP 隧道只會加入該網橋——一個介面只能屬於一個網橋，所以不要為它建立第二個網橋。如果路由器改為從空配置開始，則建立網橋並將 LAN 埠和 EoIP 隧道都新增到其中：

```ros
/interface/bridge/add name=bridge1
/interface/bridge/port/add bridge=bridge1 interface=ether2
/interface/bridge/port/add bridge=bridge1 interface=eoip-main
```

一旦兩個站點共享同一個廣播域，就只能有一臺路由器充當 DHCP 伺服器和閘道器 —— 預設的 RouterOS 配置會在其 LAN bridge 上執行 DHCP 伺服器，因此在第二臺路由器上要將其停用。
:::

兩個站點現在處於同一個二層廣播域中。透過給兩端的網橋分配同一子網內的地址並跨隧道互 ping 來驗證——在 AP 路由器上：

```ros
/ip/address/add address=10.1.1.10/24 interface=bridge1
```

以及在 station 路由器上：

```ros
/ip/address/add address=10.1.1.11/24 interface=bridge1
```

從 station 路由器上，ping AP 路由器的網橋地址即可穿越隧道：

```ros
/ping 10.1.1.10
```

## 故障排除 {#troubleshooting}

- **隧道沒有 running 標誌。** 對端沒有響應：用 `/ping <remote-address>` 檢查隧道端點是否可達、隧道是否在兩臺路由器上都存在，以及 `local-address` 是否設定正確。只有在遠端響應之後 running 標誌才會出現。常見原因是兩端 `tunnel-id` 值不匹配，因為 id 不同的 keepalive 會被丟棄：檢查兩臺路由器上的 `tunnel-id`（`/interface/eoip/print`，有效值為 0 到 65535）並使之一致。還要檢查端點之間沒有任何東西過濾 IP 協定 47（GRE），或 EoIPv6 的 IP 協定 97，並確認隧道流量沒有被 NAT。
- **running 標誌已 up 但資料無法透過。** 關閉 keepalive 後，即使 `tunnel-id` 值不匹配，running 標誌也會保持 up，所以要對比兩臺路由器上的該值。
- **大流量停滯或消失。** 如果端點之間的路徑無法不分片地承載全尺寸幀，隧道就會對外層封包進行分片，而某些路徑會丟棄分片或對其重排序。儘可能提高路徑 MTU（例如在連線鏈路上啟用 jumbo frame），並避免把隧道尺寸設定得高於路徑 MTU。
- **VLAN 標籤在大的帶標籤流量上表現異常。** 在 MTU 緊張的路徑之上，帶標籤的 VLAN 幀會在 EoIP 開銷之上再增加 4 位元組，而且在某些情況下 MSS clamp 不會作用於帶標籤流量，因此經隧道的大 TCP 連線可能停滯。只在路徑 MTU 留有餘量足以容納額外位元組的地方承載帶標籤流量，或在端點處降低 MSS。
- **網橋上出現重複、抖動或環路。** 橋接的隧道共享同一個 L2 域，因此每條隧道都需要自己的 MAC 地址；當多條隧道被橋接在一起時，生成樹（RSTP）必須能夠破除環路——它預設就在隧道上執行，所以不要停用它。
