---
sidebar_key: "high-availability-solutions/bonding"
sidebar_position: 1
title: "繫結"
sidebar_label: "繫結"
description: "Bonding 可以將多個 ethernet 介面組合成一條虛擬鏈路，以獲得更高的頻寬和故障轉移能力，MikroTik RouterOS 支援多種模式，包括 LACP 以及針對特定晶片的硬體解除安裝。"
tags:
  - 'bonding'
  - 'link-aggregation'
  - 'arp-monitoring'
source: https://manual.mikrotik.com/docs/7.24/high-availability-solutions/bonding
captured_at: '2026-11-04T11:29:47+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 概述 {#summary}

---

Bonding 是一種技術，可將多個類似乙太網的介面聚合成單個虛擬鏈路，從而獲得更高的資料速率並提供故障轉移。

:::warning
介面 bonding 不會建立具有更大鏈路速度的介面。介面 bonding 會建立一個虛擬介面，可在多個介面上對流量進行負載均衡。更多詳細資訊可在 [LAG 介面與負載均衡](../bridging-and-switching/user-guides/layer2-misconfiguration.md#lag-interfaces-and-load-balancing) 頁面中找到。

:::

:::info
帶有 Marvell Prestera 交換器以及 88E6393X、88E6191X、88E6190 交換晶片的 MikroTik 裝置支援 bonding 介面的橋接硬體解除安裝。

只有 `802.3ad`（LACP）、`balance-xor`（靜態 LAG）和 `active-backup` bonding 模式會進行硬體解除安裝；其他 bonding 模式將使用 CPU 的資源。

帶有 Marvell Prestera 交換器的 MikroTik 裝置將始終使用 Layer2+Layer3+Layer4 作為傳送雜湊策略，而 88E6393X、88E6191X、88E6190 交換晶片僅限於 Layer2 傳送雜湊。在使用硬體解除安裝時手動更改傳送雜湊策略將不會產生效果。

更多詳細資訊請參見 [Marvell Prestera 交換晶片特性](../bridging-and-switching/marvell-prestera-switch-chip-features.md)。

:::

## 快速設定指南 {#quick-setup-guide}

---

假設每個路由器（Router1 和 Router2）上都有兩個乙太網介面，並且希望在這兩個路由器之間獲得最大資料速率。為此，請按照以下步驟操作：

1. 確保將要作為 bonding 介面從屬介面的介面上沒有 IP 地址。
2. 在 Router1 上新增 bonding 介面和 IP 地址：

   ```ros
   /interface/bonding/add slaves=ether1,ether2 name=bond1
   /ip/address/add address=172.16.0.1/24 interface=bond1
   ```

3. 在 Router2 上執行相同操作：

   ```ros
   /interface/bonding/add slaves=ether1,ether2 name=bond1
   /ip/address/add address=172.16.0.2/24 interface=bond1
   ```

4. 從 Router1 測試鏈路：

   ```ros
   [admin@Router1] > ping 172.16.0.2
     SEQ HOST                                 SIZE TTL TIME  STATUS                   
       0 172.16.0.2                             56  64 0ms  
       1 172.16.0.2                             56  64 0ms  
       2 172.16.0.2                             56  64 0ms  
       sent=3 received=3 packet-loss=0% min-rtt=0ms avg-rtt=0ms max-rtt=0ms
   ```

:::warning
bonding 介面需要幾秒鐘才能與其對端建立連線。

:::

## 鏈路監控 {#link-monitoring}

---

啟用一種可用的鏈路監控選項至關重要。在上面的示例中，如果其中一個 bonding 鏈路發生故障，bonding 驅動程式將繼續透過故障鏈路傳送封包，從而導致網路效能下降。RouterOS bonding 目前支援兩種監控從屬裝置鏈路狀態的方法：MII 和 ARP 監控。由於 bonding 驅動程式的限制，無法同時使用這兩種方法。

### ARP 監控 {#arp-monitoring}

ARP 監控透過傳送 ARP 查詢並將響應作為鏈路正常執行的指示來確定鏈路狀態。ARP 回覆不會經過驗證——從屬介面收到的任何封包都會將該介面標記為活動。此方法可確保流量確實在鏈路上傳輸。

使用 balance-rr 或 balance-xor 模式時，連線的交換器必須配置為在所有鏈路路徑上均勻分發封包。否則，來自目標的所有 ARP 回覆都將在同一個從屬介面上收到，這可能導致其他 bonding 鏈路看起來已故障。

ARP 監控透過配置三個屬性啟用：link-monitoring、arp-ip-targets 和 arp-interval。可以指定多個 ARP 目標地址，這在高可用性設定中特別有用。依賴單個目標會形成潛在故障點——配置額外目標可提高 ARP 監控機制的可靠性。

要在 Router1 上啟用 ARP 監控：

```ros
/interface/bonding/set [find name=bond1] link-monitoring=arp arp-ip-targets=172.16.0.2
```

在 Router2 上：

```ros
/interface/bonding/set [find name=bond1] link-monitoring=arp arp-ip-targets=172.16.0.1
```

在 RouterOS 中，arp-interval 值預設為 100ms，在此示例中無需修改。要驗證鏈路監控是否正常工作，請斷開其中一個線纜鏈路。在 ARP 監控檢測到鏈路故障之前，可能會觀察到一些 ping 超時。

```text
[admin@MikroTik] > /ping 172.16.0.2
  SEQ HOST                                     SIZE TTL TIME  STATUS                                 
    0 172.16.0.2                                 56  64 0ms  
    1 172.16.0.2                                 56  64 0ms  
    2 172.16.0.2                                 56  64 0ms  
    3 172.16.0.2                                 56  64 0ms  
    4 172.16.0.2                                              timeout                                
    5 172.16.0.2                                 56  64 0ms  
    6 172.16.0.2                                 56  64 0ms  
    sent=7 received=6 packet-loss=14% min-rtt=0ms avg-rtt=0ms max-rtt=0ms
```

:::note
ARP 監控不需要在裝置上配置 IP 地址——無論任何介面上設定的 IP 地址如何，它都能正常工作。

:::

:::danger
當 ARP 監控處於活動狀態時，即使在與 arp-ip-targets 地址處於同一子網的 VLAN 介面上配置了 IP 地址，bonding 從屬介面也會發送不帶 VLAN 標籤的 ARP 請求。

:::

### MII 監控 {#mii-monitoring}

MII 監控僅監控本地介面的狀態。MII Type 1 是一種由裝置驅動程式確定鏈路是 up 還是 down 的方法。如果裝置驅動程式不支援此選項，鏈路將始終顯示為 up。MII 監控的主要缺點在於，即使鏈路被檢測為 up，它也無法確定鏈路是否真的能夠傳遞封包流量。MII 監控透過設定 link-monitoring 和 mii-interval 引數進行配置。

要在 Router1 和 Router2 上啟用 MII Type1 監控：

```ros
/interface/bonding/set [find name=bond1] link-monitoring=mii
```

我們將 mii-interval 保留為預設值（100ms）。當拔掉其中一個線纜時，與 ARP 鏈路監控相比，故障幾乎會立即被檢測到。

## Bonding 模式 {#bonding-modes}

---

### 802.3ad {#8023ad}

802.3ad 模式是一種 IEEE 標準，也稱為 LACP（鏈路聚合控制協定）。它提供聚合的自動配置，所需的交換器配置最少。該標準還要求幀按順序交付，因此連線不應出現數據包亂序。此外，聚合中的所有裝置必須以相同的速度和雙工模式執行。

LACP 根據雜湊後的協定頭資訊在活動埠之間對傳出流量進行負載均衡，並接受來自任何活動埠的傳入流量。雜湊包括乙太網源地址和目標地址、VLAN 標籤（如果可用）以及 IPv4/IPv6 源地址和目標地址。計算方法取決於 transmit-hash-policy 引數。不建議使用 ARP 鏈路監控，因為由於 LACP 對端裝置上的傳送雜湊策略，ARP 回覆封包可能只到達一個從屬埠。這可能導致傳輸流量不均衡，因此建議使用 MII 鏈路監控。

:::warning
layer-3-and-4 傳送雜湊模式與 LACP 不完全相容。更多詳細資訊可在 https://www.kernel.org/doc/Documentation/networking/bonding.txt 中找到

:::

### balance-xor {#balance-xor}

此模式使用雜湊後的協定頭在活動埠之間對傳出流量進行負載均衡，並接受來自任何活動埠的傳入流量。該模式與 LACP 非常相似，只是它未標準化。此模式可與連線的交換器上的靜態鏈路聚合組（LAG）介面配置一起使用。

### balance-rr {#balance-rr}

設定此模式後，封包將按順序從第一個可用從屬介面傳送到最後一個從屬介面。balance-rr 模式是唯一一種可以透過屬於同一 TCP/IP 連線的多個介面傳送封包的 bonding 模式。當使用多個傳送鏈路和多個接收鏈路時，封包通常會亂序到達，從而導致分段重傳。對於 UDP 等其他協定，如果用戶端軟體能夠容忍亂序封包，則這不是問題。如果使用交換器將鏈路聚合在一起，則需要適當的交換器埠配置；然而，許多交換器不支援 balance-rr。[快速設定指南](#quick-setup-guide) 演示了 balance-rr bonding 模式的用法。如您所見，設定相當簡單。balance-rr 也可用於繫結多個無線鏈路；但是，它要求所有 bonding 鏈路的頻寬相等。如果其中一個 bonding 鏈路的頻寬下降，則 bond 的總頻寬將等於最慢 bonding 鏈路的頻寬。

### active-backup {#active-backup}

此模式僅使用一個活動從屬介面傳送封包。輔助從屬介面僅在主從屬介面失敗時才變為活動狀態。bonding 介面的 MAC 地址會顯示在活動埠上，以防止交換器混淆。Active-backup 是使用多個互連交換器的高可用性設定的最佳選擇。

:::warning
當兩個路由器裝置直接連線時，ARP 監控無法正常工作。在此類設定中，必須使用 MII 監控，或者應在路由器裝置及其對端之間放置交換器。

:::

### broadcast {#broadcast}

當埠配置為 broadcast 模式時，所有從屬埠都會向目標傳送相同的資料。此模式提供容錯，但不提供負載均衡。

### balance-tlb {#balance-tlb}

此模式按對端對傳出流量進行負載均衡。每個 bonding 鏈路可以以不同的速度和雙工設定執行，並且與其他 bonding 模式不同，不需要特定的交換器配置。此模式的限制在於它僅支援 MII 鏈路監控——配置了 ARP 監控時會被忽略——並且傳入流量不會進行負載均衡。傳入流量將使用指定為“主”介面的鏈路。

#### 配置示例 {#configuration-example}

假設路由器有兩個鏈路——**ether1** 最大頻寬為 10Mbps，**ether2** 最大頻寬為 5Mbps。第一個鏈路具有更多頻寬，因此我們將其設定為主鏈路：

```ros
/interface/bonding/add mode=balance-tlb slaves=ether1,ether2 primary=ether1
```

![](/img/b5887323292b3cec.webp)

交換器不需要額外配置。上圖說明了 balance-tlb 模式的工作方式。如您所見，路由器可以與連線到交換器的所有用戶端通訊，總頻寬為兩個鏈路的總和（15Mbps）。但如您所知，balance-tlb 不會對傳入流量進行負載均衡。在我們的示例中，用戶端與路由器通訊的總頻寬為主鏈路的頻寬，在我們的配置中為 10Mbps。

### balance-alb {#balance-alb}

該模式基本上與 balance-tlb 相同，但傳入 IPv4 流量也會進行負載均衡。接收負載均衡透過 ARP 協商實現。bonding 驅動程式會攔截本地生成的 ARP 訊息，並在其發出時用 bond 中某個從屬介面的唯一地址覆蓋源硬體地址，從而使不同對端使用不同的硬體地址。僅支援 MII 鏈路監控（配置了 ARP 鏈路監控時會被忽略）。此模式的另一個缺點是它需要裝置驅動程式具備更改 MAC 地址的能力。該模式與 local-proxy-arp 設定不相容。

![](/img/177dba8c86cfc7f2.webp)  
上圖說明了 balance-alb 模式的工作方式。與 balance-tlb 模式相比，來自用戶端的流量還可以使用輔助鏈路與路由器通訊。

## Bonding 監控 {#bonding-monitoring}

---

從 RouterOS 6.48 版本開始，可以監控 bonding 介面和 bonding 埠。對於 `802.3ad` bonding 模式，可以使用更詳細的監控選項。

```text
/interface/bonding/monitor [find] 
                      mode: 802.3ad           active-backup
              active-ports: ether4            ether6
                            ether5            
            inactive-ports:                   ether7
            lacp-system-id: CC:2D:E0:11:22:33 
      lacp-system-priority: 65535             
    lacp-partner-system-id: B8:69:F4:44:55:66
```

| 屬性 | 描述 |
| :-- | :-- |
| **mode** (*802.3ad \| active-backup \| balance-alb \| balance-rr \| balance-tlb \| balance-xor \| broadcast*) | 使用的 bonding 模式 |
| **active-ports** (*interface*) | 顯示活動的 bonding 埠 |
| **inactive-ports**(*interface*) | 顯示非活動的 bonding 埠（例如已停用或備份介面） |
| **lacp-system-id** (*MAC address*) | 顯示本地 LACP 系統 ID |
| **lacp-system-priority** (*integer*) | 顯示本地 LACP 優先順序 |
| **lacp-partner-system-id** (*MAC address*) | 顯示對端 LACP 系統 ID |

要監控各個 bonding 埠，請使用 `monitor-slaves` 命令。

```text
/interface/bonding/monitor-slaves bond1
Flags: A - active, P - partner 
 AP port=ether4 key=17 flags="A-GSCD--" partner-sys-id=D4:CA:6D:12:06:65 partner-sys-priority=65535 partner-key=9 partner-flags="A-GSCD--" 

 AP port=ether5 key=17 flags="A-GSCD--" partner-sys-id=D4:CA:6D:12:06:65 partner-sys-priority=65535 partner-key=9 partner-flags="A-GSCD--" 
```

| 屬性 | 描述 |
| :-- | :-- |
| **port** (*interface*) | 使用的 bonding 埠 |
| **key** (*integer*) | 顯示本地 LACP 聚合鍵。低 6 位根據各個埠的鏈路速率和雙工模式自動分配。高 10 位可使用 `lacp-user-key` 設定手動指定（僅從 RouterOS v7.3 起可用）。 |
| **flags** (*string*) | 顯示本地 LACP 標誌：A - activity（鏈路處於活動狀態，否則為 passive）T - timeout（鏈路使用 1 秒短超時，否則使用 30 秒超時）G - aggregation（鏈路可聚合）S - synchronization（鏈路已同步）C - collecting（鏈路能夠收集傳入幀）D - distributing（鏈路能夠分發傳出幀）F - defaulted（鏈路正在使用預設的對端資訊，表示尚未從對端收到 LACPDU）E - expired（鏈路處於過期狀態） |
| **partner-sys-id** (*MAC address*) | 顯示對端 LACP 系統 ID |
| **partner-sys-priority** (*integer*) | 顯示對端 LACP 優先順序 |
| **partner-key** (*integer*) | 顯示對端 LACP 聚合鍵 |
| **partner-flags** (*string*) | 顯示對端 LACP 標誌 |

## 屬性說明 {#property-description}

---

本節介紹可用的 bonding 設定。

| 屬性 | 描述 |
| :-- | :-- |
| **arp** (*disabled \| enabled \| proxy-arp \| reply-only*; 預設值: **enabled**) | 介面使用的 Address Resolution Protocol。<code>disabled</code> - 介面將不使用 ARP<code>enabled</code> - 介面將使用 ARP<code>proxy-arp</code> - 介面將使用 ARP 代理功能<code>reply-only</code> - 介面僅回覆來自與 `/ip/arp` 表中靜態條目匹配的 IP 地址/MAC 地址組合的請求。動態條目不會自動儲存在 `/ip/arp` 表中。因此，為使通訊成功，必須已存在有效的靜態條目。 |
| **arp-interval** (*time*; 預設值: **00:00:00.100**) | 以毫秒為單位的時間，定義監控 ARP 請求的頻率 |
| **arp-ip-targets** (*IP address*; 預設值: ) | 如果 link-monitoring 設定為 arp，則將監控的 IP 目標地址。可以指定多個 IP 地址，用逗號分隔 |
| **comment** (*string*; Default: ) | 介面的簡短描述 |
| **disabled** (*yes \| no*; 預設值: **no**) | 更改 bonding 介面是否被停用 |
| **down-delay** (*time*; 預設值: **00:00:00**) | 如果檢測到鏈路故障，bonding 介面會在 down-delay 時間內被停用。該值應為 mii-interval 的倍數，否則將向下舍入到最接近的值。僅當 `link-monitoring` 設定為 `mii` 時，此屬性才生效。 |
| **forced-mac-address** (*MAC address*; 預設值: **none**) | 預設情況下，bonding 介面將使用第一個選定從屬介面的 MAC 地址。此屬性允許為 bond 介面配置靜態 MAC 地址（全零、廣播或多播地址將不適用）。RouterOS 將自動更改從屬介面的 MAC 地址，並且它將在 `/interface/ethernet` 配置匯出中可見 |
| **lacp-mode** (*active \| passive*; 預設值: **active**) | 指定埠是主動還是被動參與 LACP：<code>active</code> - 埠主動發起 LACP 通訊，無論對端的 LACP 模式如何（即即使對端靜默，它也會“發言”），<code>passive</code> - 埠僅響應 LACP 訊息，並且除非對端處於 active 模式，否則不會主動發起（即它“監聽”，並且僅在收到發言時才響應）。 |
| **lacp-rate** (*1sec \| 30secs*; 預設值: **30secs**) | 鏈路聚合控制協定速率指定 bonding 對端之間交換 LACPDU 的頻率。用於確定鏈路是否 up 或網路中是否發生了其他變化。LACP 會嘗試適應這些變化以提供故障轉移。 |
| **lacp-user-key**(*integer: 0..1023*; 預設值: **0**) | 指定埠鍵的高 10 位。低 6 位根據各個埠的鏈路速率和雙工模式自動分配。該設定僅從 RouterOS v7.3 起可用。 |
| **link-monitoring** (*arp \| mii \| none*; 預設值: **mii**) | 用於監控鏈路（鏈路是 up 還是 down）的方法<code>arp</code> - 使用 Address Resolution Protocol 判斷遠端介面是否可達<code>mii</code> - 使用 Media Independent Interface 確定鏈路狀態。鏈路狀態判斷依賴於裝置驅動程式。<code>none</code> - 不使用鏈路監控方法。**警告：** 某些 bonding 模式需要特定的鏈路監控才能正常工作。  |
| **min-links** (*integer: 0..4294967295*; 預設值: **0**) | bonding 變為活動狀態需要多少個活動從屬鏈路 |
| **mii-interval** (*time*; 預設值: **00:00:00.100**) | 監控鏈路故障的頻率（僅當 link-monitoring 為 mii 時使用該引數） |
| **mlag-id** (*integer: 0..4294967295*; 預設值: ) | 更改 bonding 介面的 MLAG ID。應在兩個對端裝置上使用相同的 MLAG ID，才能成功建立單個 MLAG。更多詳細資訊請參見 [MLAG](./multi-chassis-link-aggregation-group.md)。 |
| **mode** (*802.3ad \| active-backup \| balance-alb \| balance-rr \| balance-tlb \| balance-xor \| broadcast*; 預設值: **balance-rr**) | 指定 bonding 策略之一<code>802.3ad</code> - LACP，IEEE 802.3ad 動態鏈路聚合。在此模式下，介面聚合為一個組，其中每個從屬介面共享相同速率。它提供容錯和負載均衡。傳出流量的從屬介面選擇根據 transmit-hash-policy 進行。<code>active-backup</code> - 提供鏈路備份。同一時間只能有一個從屬介面處於活動狀態。另一個從屬介面僅在第一個失敗時才會變為活動狀態。<code>balance-alb</code> - 自適應負載均衡。與 balance-tlb 相同，但接收流量也會進行負載均衡。裝置驅動程式應支援更改其 MAC 地址。<code>balance-rr</code> - 輪詢負載均衡。bonding 介面中的從屬介面將按順序傳送和接收資料。它提供負載均衡和容錯。<code>balance-tlb</code> - 傳出流量根據每個從屬介面的當前負載進行分發。傳入流量不進行負載均衡，並由當前從屬介面接收。如果接收從屬介面失敗，則另一個從屬介面接管失敗從屬介面的 MAC 地址。<code>balance-xor</code> - 靜態 LAG，根據選定的 transmit-hash-policy 傳送。此模式提供負載均衡和容錯。<code>broadcast</code> - 在所有介面上同時廣播相同資料。這提供容錯，但會在某些較慢的機器上降低流量吞吐量。**重要：** 帶有 Marvell Prestera 交換器和 88E6393X、88E6191X、88E6190 交換晶片的 MikroTik 裝置支援 bonding 介面的橋接硬體解除安裝。只有 `802.3ad`（LACP）、`balance-xor`（靜態 LAG）和 `active-backup` bonding 模式會進行硬體解除安裝，其他 bonding 模式將使用 CPU 的資源。  |
| **mtu** (*integer*; 預設值: **1500**) | 最大傳輸單元，以位元組為單位。必須小於或等於 bonding 從屬介面的最小 L2MTU 值。bonding 介面的 L2MTU 由其從屬介面中的最低 L2MTU 值決定 |
| **name** (*string*; 預設值: ) | bonding 介面的名稱 |
| **primary** (*string*; 預設值: **none**) | 控制活動從屬埠之間的主介面，僅適用於 active-backup、balance-tlb 和 balance-alb 模式。對於 active-backup 模式，它控制哪個執行中的介面負責傳送和接收流量。對於 balance-tlb 模式，它控制哪個執行中的介面負責接收所有流量，而對於 balance-alb 模式，它控制哪個介面負責接收非均衡流量（非 IPv4 流量）。當未選擇任何介面作為 primary 時，裝置將自動選擇配置為第一個的介面。 |
| **slaves** (*string*; 預設值: **none**) | 至少兩個類似乙太網的介面，用逗號分隔，將用於 bonding |
| **up-delay** (*time*; 預設值: **00:00:00**) | 如果鏈路已啟用，bonding 介面會在 up-delay 時間內被停用，之後啟用。該值應為 mii-interval 的倍數，否則將向下舍入到最接近的值。僅當 `link-monitoring` 設定為 `mii` 時，此屬性才生效。 |
| **transmit-hash-policy** (*encap-2-and-3 \| encap-3-and-4 \| layer-2 \| layer-2-and-3 \| layer-3-and-4*; 預設值: **layer-2**) | 選擇在 balance-xor 和 802.3ad 模式下用於從屬介面選擇的傳送雜湊策略 <code>encap-2-and-3</code> - 此策略的工作方式類似於 layer-2-and-3 流量分發方法，但使用一個過程來同時分析封裝的封包頭部。如果使用封裝協定（如隧道），它可能會選擇內部頭部而不是外部頭部。當 6to4、GRE、GRE6、IPIP、IPIP6、PPPoE 或 PPTP 等隧道執行在 bonding 介面上時，RouterOS 可以使用此功能。<code>encap-3-and-4</code> - 此策略的工作方式類似於 layer-3-and-4 流量分發方法，但使用一個過程來同時分析封裝的封包頭部。如果使用封裝協定（如隧道），它可能會選擇內部頭部而不是外部頭部。當 6to4、GRE、GRE6、IPIP、IPIP6、PPPoE 或 PPTP 等隧道執行在 bonding 介面上時，RouterOS 可以使用此功能。<code>layer-2</code> - 使用硬體 MAC 地址的 XOR 生成雜湊。此演算法會將發往特定網路對端的所有流量放在同一個從屬介面上。此演算法符合 802.3ad。<code>layer-2-and-3</code> - 此策略使用 layer2 和 layer3 協定資訊的組合生成雜湊。使用硬體 MAC 地址和 IP 地址的 XOR 生成雜湊。此演算法會將發往特定網路對端的所有流量放在同一個從屬介面上。對於非 IP 流量，公式與 layer2 傳送雜湊策略相同。此策略旨在提供比單獨 layer2 更均衡的流量分佈，尤其是在需要 layer3 閘道器裝置才能到達大多數目的地的環境中。此演算法符合 802.3ad。<code>layer-3-and-4</code> - 此策略在可用時使用上層協定資訊生成雜湊。這允許發往特定網路對端的流量跨越多個從屬介面，儘管單個連線不會跨越多個從屬介面。對於分片的 TCP 或 UDP 封包以及所有其他 IP 協定流量，將省略源埠和目標埠資訊。對於非 IP 流量，公式與 layer2 傳送雜湊策略相同。此演算法不完全符合 802.3ad。**重要：** 帶有 Marvell Prestera 交換器的 MikroTik 裝置將始終使用 Layer2+Layer3+Layer4 作為傳送雜湊策略，而 88E6393X、88E6191X、88E6190 交換晶片僅限於 Layer2 傳送雜湊。在使用硬體解除安裝時手動更改傳送雜湊策略將不會產生效果。  |

## 另請參閱 {#see-also}

- [配置示例 - 帶 bond 的 VLAN](../bridging-and-switching/marvell-prestera-switch-chip-features.md#configuration-example---vlans-with-bonds)
