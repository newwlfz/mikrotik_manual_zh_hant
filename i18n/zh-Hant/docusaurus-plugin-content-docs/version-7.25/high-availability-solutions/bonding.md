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
source: https://manual.mikrotik.com/docs/7.25/high-availability-solutions/bonding
captured_at: '2026-11-04T11:17:42+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
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

對於 `802.3ad` bonding 模式，可以使用更詳細的監控選項。

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

要監控各個 bonding 埠，請使用 `monitor-slaves` 命令。

```text
/interface/bonding/monitor-slaves bond1
Flags: A - active, P - partner 
 AP port=ether4 key=17 flags="A-GSCD--" partner-sys-id=D4:CA:6D:12:06:65 partner-sys-priority=65535 partner-key=9 partner-flags="A-GSCD--" 

 AP port=ether5 key=17 flags="A-GSCD--" partner-sys-id=D4:CA:6D:12:06:65 partner-sys-priority=65535 partner-key=9 partner-flags="A-GSCD--" 
```

## 另請參閱 {#see-also}

- [配置示例 - 帶 bond 的 VLAN](../bridging-and-switching/marvell-prestera-switch-chip-features.md#configuration-example---vlans-with-bonds)
