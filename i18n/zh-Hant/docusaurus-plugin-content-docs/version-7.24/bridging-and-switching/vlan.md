---
title: "VLAN"
description: "本頁介紹 MikroTik RouterOS 中的 VLAN 功能，說明如何依據 IEEE 802.1Q 標準建立與管理 Virtual LAN，以有效率地進行網路區隔，並詳細說明 VLAN 介面、trunking、Q-in-Q 標記與介面屬性。"
tags:
  - 'vlan'
  - 'ieee-802-1q'
  - 'arp'
source: https://manual.mikrotik.com/docs/7.24/bridging-and-switching/vlan
captured_at: '2026-11-28T10:19:39.818Z'
pagination_next: "bridging-and-switching/swos"
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

**子選單：** `/interface/vlan`

**標準：** `IEEE 802.1Q, IEEE 802.1ad`

虛擬區域網路（VLAN）是一種第 2 層方法，可讓單一實體介面（乙太網路、無線等）上存在多個虛擬 LAN，並能有效區隔各個 LAN。

你可以使用 MikroTik RouterOS（以及 Cisco IOS、Linux 與其他路由器系統）標記這些封包，並接受與路由已標記的封包。

由於 VLAN 運作於 OSI 第 2 層，因此可以像任何其他網路介面一樣使用，沒有任何限制。VLAN 可以順利通過一般乙太網路橋接器。

你也可以透過無線鏈路傳輸 VLAN，並在單一無線介面上建立多個 VLAN 介面。請注意，由於 VLAN 並非完整的通道協定（也就是說，它沒有額外欄位來傳輸傳送者與接收者的 MAC 位址），因此透過 VLAN 進行橋接的限制，與橋接純無線介面的限制相同。換句話說，雖然無線用戶端可以參與建立在無線介面上的 VLAN，但無法將建立在 station 模式無線介面上的 VLAN 與任何其他介面橋接。

## 802.1Q

虛擬區域網路（VLAN）最常用的協定是 IEEE 802.1Q。這是一種標準化的封裝協定，定義如何將四位元組的 VLAN 識別碼插入乙太網路標頭。

每個 VLAN 都會被視為獨立的子網路。這表示預設情況下，特定 VLAN 中的主機無法與屬於另一個 VLAN 的主機通訊，即使它們連接到同一台交換器也是如此。因此，如果你想要進行 VLAN 間通訊，就需要路由器。RouterOS 每個介面最多支援 4094 個 VLAN 介面，每個介面都有唯一的 VLAN ID。VLAN 優先順序也可以使用與調整。

當 VLAN 跨越一個以上的交換器時，交換器之間的連結必須成為「trunk」，封包會加上標籤，以指出其屬於哪個 VLAN。trunk 會承載多個 VLAN 的流量；它就像點對點連結，在交換器之間或交換器與路由器之間傳遞已加上標籤的封包。

:::info
IEEE 802.1Q 標準保留了具有特殊用途的 VLAN ID；在一般 VLAN 設定中不應使用下列 VLAN ID：0、1、4095
:::

## Q-in-Q

原始 802.1Q 只允許一個 VLAN 標頭；另一方面，Q-in-Q 允許兩個或以上的 VLAN 標頭。在 RouterOS 中，可透過在另一個 VLAN 介面上新增一個 VLAN 介面來設定 Q-in-Q。範例：

```ros
/interface/vlan
add name=vlan1 vlan-id=11 interface=ether1
add name=vlan2 vlan-id=12 interface=vlan1
```

如果有任何封包透過 `vlan2` 介面傳送，乙太網路標頭會加上兩個 VLAN 標籤：`11` 與 `12`。

## 屬性 {#properties}

**子選單：** `/interface/vlan`

| Property | Description |
| :-- | :-- |
| **arp** (*disabled \| enabled \| local-proxy-arp \| proxy-arp \| reply-only*; Default: **enabled**) | Address Resolution Protocol 設定<ul><li><span className="ros-icon-success"><code>disabled</code></span> - 介面不會使用 ARP</li><li><span className="ros-icon-success"><code>enabled</code></span> - 介面會使用 ARP</li><li><span className="ros-icon-success"><code>local-proxy-arp</code></span> - 路由器會在介面上執行 proxy ARP，並將回覆傳送至同一介面</li><li><span className="ros-icon-success"><code>proxy-arp</code></span> - 路由器會在介面上執行 proxy ARP，並將回覆傳送至其他介面</li><li><span className="ros-icon-success"><code>reply-only</code></span> - 介面只會回覆來自相符 IP 位址／MAC 位址組合的要求，這些組合必須在 IP/ARP 表中輸入為靜態項目。IP/ARP 表中不會自動儲存動態項目。因此，若要成功通訊，必須已存在有效的靜態項目。</li></ul> |
| **arp-timeout** (*auto \| integer*; Default: **auto**) | 在沒有從 IP 收到任何封包後，ARP 記錄會在 ARP 表中保留多久。值 `auto` 等於 IP/Settings 中的 `arp-timeout` 值，預設為 30s。 |
| **disabled** (*yes \| no*; Default: **no**) | 變更介面是否停用。 |
| **interface** (*name*; Default: ) | VLAN 將在其上運作的介面名稱。 <br/><br/><strong>重要：</strong>將 VLAN 介面新增至已啟用 vlan-filtering 的 <a href="/docs/bridging-and-switching#bridge-vlan-filtering">bridge</a> 時，會自動將 bridge 介面標記為 member port。在 <code>/interface/bridge/vlan</code> 選單下會出現一筆註解為「added by vlan on bridge」的動態項目。 <br/> |
| **l3-hw-offloading** (*yes \| no*; Default: **yes**) | 針對每個 VLAN 介面啟用或停用 [L3HW](/docs/bridging-and-switching/l3-hardware-offloading)。此設定僅適用於支援 L3HW offloading 的設備，並從 RouterOS v7.21 開始提供。詳細資訊：[Per-VLAN offloading](/docs/bridging-and-switching/l3-hardware-offloading#per-vlan-offloading)。 |
| **mvrp** (*yes \| no*; Default: **no**) | 指定此 VLAN 是否應透過 Multiple VLAN Registration Protocol（MVRP）以 applicant 身分宣告其屬性。其主要用途是針對在乙太網路介面上建立的 VLAN（例如「router on a stick」設定），該介面連接到支援 [MVRP](/docs/bridging-and-switching/vlan#mvrp) 的 bridge。在已屬於啟用 MVRP 之 bridge 的 VLAN 介面上啟用此選項沒有作用，因為在此情況下 MVRP 由 bridge 管理。此屬性只有在 `use-service-tag` 停用時才會生效。 |
| **mtu** (*integer: 68..65535*; Default: **1500**) | Layer3 最大傳輸單位 |
| **name** (*string*; Default: ) | 介面名稱 |
| **use-service-tag** (*yes \| no*; Default: ) | 相容於 IEEE 802.1ad 的 Service Tag |
| **vlan-id** (*integer: 1..4094*; Default: **1**) | 用於區分 VLAN 的 Virtual LAN 識別碼或標籤。屬於同一 VLAN 的所有電腦都必須設定為相同值。 |

:::info
MTU 應設為 1500 bytes，與乙太網路介面相同。但某些乙太網路卡不支援接收／傳送加上 VLAN 標頭的完整大小乙太網路封包（1500 bytes 資料 + 4 bytes VLAN 標頭 + 14 bytes 乙太網路標頭），因此可能無法運作。在此情況下，可使用 MTU 1496，但請注意，若必須透過介面傳送較大的封包，這會造成封包分段。同時請記得，若來源與目的地之間的 path MTU discovery 未正常運作，MTU 1496 可能會造成問題。
:::

## 設定範例 {#setup-examples}

---

### 影片範例 {#video-examples}

[VLANs pt1](http://youtube.com/watch?v=US2EU6cgHQU), [VLANs pt2](http://youtube.com/watch?v=YMwOrc0LDP8), [VLANs pt3](http://youtube.com/watch?v=7a_z1jAdIME)

### Layer2 VLAN 範例 {#layer2-vlan-examples}

有多種可用的設定方式，但每種設定類型都是針對特定設備組合設計的，因為某些設定方法可以讓你利用內建交換器晶片的優勢，並獲得更高的吞吐量。請參閱 [Basic VLAN switching](/docs/bridging-and-switching/user-guides/basic-vlan-switching) 指南，瞭解每種設備類型應使用哪種設定，以獲得最大可能的吞吐量與相容性。該指南說明如何設定非常基本的 VLAN trunk/access 埠設定。

設定 VLAN 標記或 VLAN 交換還有其他方式，但建議使用 [Bridge VLAN Filtering](/docs/bridging-and-switching/vlan#bridge-vlan-filtering)。請確認你沒有使用任何 [known Layer2 misconfigurations](/docs/bridging-and-switching/user-guides/layer2-misconfiguration)。

### Layer3 VLAN 範例 {#layer3-vlan-examples}

#### 簡單 VLAN 路由 {#simple-vlan-routing}

假設有幾台 MikroTik 路由器連接到一個集線器。請記住，集線器是 OSI 實體層設備（如果路由器之間有集線器，則從 L3 的角度來看，這與它們之間的乙太網路纜線連線相同）。為簡化起見，假設所有路由器都使用 ether1 介面連接到集線器，並如下圖所示指派 IP 位址。然後在每台路由器上建立 VLAN 介面。

R2 與 R4 的設定如下所示：

R2:

```ros
[admin@MikroTik] /interface/vlan> add name=VLAN2 vlan-id=2 interface=ether1 disabled=no

[admin@MikroTik] /interface/vlan> print 
Flags: X - disabled, R - running, S - slave 
 #    NAME                  MTU   ARP        VLAN-ID INTERFACE                
0 R  VLAN2                 1500  enabled    2       ether1
```

R4:

```ros
[admin@MikroTik] /interface/vlan> add name=VLAN2 vlan-id=2 interface=ether1 disabled=no

[admin@MikroTik] /interface/vlan> print 
Flags: X - disabled, R - running, S - slave 
 #    NAME                  MTU   ARP        VLAN-ID INTERFACE                
0 R  VLAN2                 1500  enabled    2       ether1
```

下一步是將 IP 位址指派給 VLAN 介面。

R2:

```ros
 [admin@MikroTik] /ip/address> add address=10.10.10.3/24 interface=VLAN2
 [admin@MikroTik] /ip/address> print
 Flags: X - disabled, I - invalid, D - dynamic
   #   ADDRESS            NETWORK         BROADCAST       INTERFACE
   0   10.0.1.4/24        10.0.1.0        10.0.1.255      ether1
   1   10.20.0.1/24       10.20.0.0       10.20.0.255     pc1
   2   10.10.10.3/24      10.10.10.0      10.10.10.255    vlan2

 [admin@MikroTik] /ip/address> 
```

R4:

```ros
 [admin@MikroTik] /ip/address> add address=10.10.10.5/24 interface=VLAN2
 [admin@MikroTik] /ip/address> print
 Flags: X - disabled, I - invalid, D - dynamic
   #   ADDRESS            NETWORK         BROADCAST       INTERFACE
   0   10.0.1.5/24        10.0.1.0        10.0.1.255      ether1
   1   10.30.0.1/24       10.30.0.0       10.30.0.255     pc2
   2   10.10.10.5/24      10.10.10.0      10.10.10.255    vlan2

[admin@MikroTik] /ip/address> 
```

此時，應該可以從路由器 R2 ping 路由器 R4，反之亦然：

```ros
 "Ping from R2 to R4:"

 [admin@MikroTik] /ip/address> /ping 10.10.10.5

 10.10.10.5 64 byte ping: ttl=255 time=4 ms

 10.10.10.5 64 byte ping: ttl=255 time=1 ms

 2 packets transmitted, 2 packets received, 0% packet loss

 round-trip min/avg/max = 1/2.5/4 ms

 "From R4 to R2:"
 
 [admin@MikroTik] /ip/address> /ping 10.10.10.3
 10.10.10.3 64 byte ping: ttl=255 time=6 ms
 10.10.10.3 64 byte ping: ttl=255 time=1 ms
 2 packets transmitted, 2 packets received, 0% packet loss
 round-trip min/avg/max = 1/3.5/6 ms 
```

為確認 VLAN 設定正常運作，請嘗試從 R2 ping R1。如果 ping 逾時，表示 VLAN 已成功隔離。

```ros
 "From R2 to R1:"

 [admin@MikroTik] /ip/address> /ping 10.10.10.2
 10.10.10.2 ping timeout
 10.10.10.2 ping timeout
 3 packets transmitted, 0 packets received, 100% packet loss 
```

#### VLAN 間路由 {#intervlan-routing}

如果在交換器上實作不同的 VLAN，則需要路由器來提供 VLAN 之間的通訊。交換器運作於 OSI 第 2 層，因此只會使用 Ethernet 標頭進行轉送，不會檢查 IP 標頭。基於這個原因，我們必須使用作為每個 VLAN 閘道器的路由器。若沒有路由器，主機就無法與自身 VLAN 外部通訊。上述 VLAN 之間的路由程序稱為 VLAN 間通訊。

為了說明 VLAN 間通訊，我們將建立一個 trunk，讓三個 VLAN（VLAN2、VLAN3 與 VLAN4）的流量通過 Mikrotik 路由器與支援 VLAN trunking 的可管理交換器之間的單一連結。

如上圖所示，每個 VLAN 都有各自獨立的子網路（廣播網域）：

- VLAN 2 – 10.10.20.0/24。
- VLAN 3 – 10.10.30.0/24。
- VLAN 4 – 10.10.40.0/24。

大多數交換器的 VLAN 設定都很直接。我們需要定義哪些埠是 VLAN 的成員，並定義一個「trunk」埠，讓標記訊框可以在交換器與路由器之間傳送。

建立 VLAN 介面：

```ros
/interface/vlan
add name=VLAN2 vlan-id=2 interface=ether1 disabled=no
add name=VLAN3 vlan-id=3 interface=ether1 disabled=no
add name=VLAN4 vlan-id=4 interface=ether1 disabled=no
```

新增 IP 位址至 VLAN：

```ros
/ip/address 
add address=10.10.20.1/24 interface=VLAN2
add address=10.10.30.1/24 interface=VLAN3
add address=10.10.40.1/24 interface=VLAN4
```

#### RouterOS /32 與 IP unnumbered 位址 {#routeros-32-and-ip-unnumbered-addresses}

在 RouterOS 中，若要建立具有位址的點對點隧道，必須使用網路遮罩為 `/32` 的位址，這實際上可提供與某些廠商的 unnumbered IP 位址相同的功能。

其中有 2 台路由器，RouterA 與 RouterB，各自分別屬於網路 10.22.0.0/24 與 10.23.0.0/24，並使用 VLAN 作為載體，以下列設定連接這些路由器：

RouterA:

```ros
 /ip/address/add address=10.22.0.1/24 interface=ether1
 /interface/vlan/add interface=ether2 vlan-id=1 name=vlan1
 /ip/address/add address=10.22.0.1/32 interface=vlan1 network=10.23.0.1
 /ip/route/add gateway=10.23.0.1 dst-address=10.23.0.0/24 
```

RouterB:

```ros
 /ip/address/add address=10.23.0.1/24 interface=ether1
 /interface/vlan/add interface=ether2 vlan-id=1 name=vlan1
 /ip/address/add address=10.23.0.1/32 interface=vlan1 network=10.22.0.1
 /ip/route/add gateway=10.22.0.1 dst-address=10.22.0.0/24 
```
