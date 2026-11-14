---
sidebar_key: "bridging-and-switching/vlan"
sidebar_position: 8
title: "VLAN"
sidebar_label: "VLAN"
description: "本頁面介紹 MikroTik RouterOS 中的 VLAN 功能，說明如何使用 IEEE 802.1Q 標準建立和管理虛擬區域網路以實現高效的網路分段，並詳細講解 VLAN 介面、trunking、Q-in-Q 標記以及介面屬性。"
tags:
  - 'vlan'
  - 'ieee-802-1q'
  - 'arp'
source: https://manual.mikrotik.com/docs/7.25/bridging-and-switching/vlan
captured_at: '2026-11-04T11:14:46+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

**子選單：** `/interface/vlan`

**標準：** `IEEE 802.1Q, IEEE 802.1ad`

虛擬區域網路（VLAN）是一種二層方法，允許在單個物理介面（乙太網、無線等）上建立多個虛擬 LAN，從而能夠高效地隔離各區域網路。

您可以使用 MikroTik RouterOS（以及 Cisco IOS、Linux 和其他路由系統）為這些封包打上標記，並接收和路由帶標記的封包。

由於 VLAN 工作在 OSI 第二層，因此它可以像任何其他網路介面一樣使用，不受任何限制。VLAN 可以成功透過普通乙太網網橋。

您還可以透過無線鏈路傳輸 VLAN，並在單個無線介面上放置多個 VLAN 介面。請注意，由於 VLAN 並非完整的隧道協定（即它沒有用於傳輸傳送方和接收方 MAC 地址的額外欄位），因此透過 VLAN 進行橋接時，會存在與橋接普通無線介面相同的限制。換句話說，雖然無線用戶端可以加入放置在無線介面上的 VLAN，但無法將放置在 station 模式無線介面上的 VLAN 與任何其他介面進行橋接。

## 802.1Q {#8021q}

虛擬區域網路（VLAN）最常用的協定是 IEEE 802.1Q。它是一種標準化的封裝協定，定義瞭如何將四位元組的 VLAN 識別符號插入乙太網頭中。

每個 VLAN 都被視為一個單獨的子網。這意味著預設情況下，特定 VLAN 中的主機無法與屬於另一個 VLAN 的主機通訊，即使它們連線到同一臺交換器。因此，如果您需要 VLAN 間通訊，就需要一臺路由器。RouterOS 每個介面最多支援 4094 個 VLAN 介面，每個介面都有唯一的 VLAN ID。VLAN 優先順序也可以使用和調整。

當 VLAN 跨越一臺以上交換器時，交換器之間的鏈路必須成為 'trunk'，此時封包會被打上標籤以指示其所屬的 VLAN。trunk 承載多個 VLAN 的流量；它就像一條點對點鏈路，在交換器之間或交換器與路由器之間傳輸帶標籤的封包。

:::info
IEEE 802.1Q 標準保留了一些具有特殊用途的 VLAN ID；以下 VLAN ID 不應在常規 VLAN 配置中使用：0、1、4095
:::

## Q-in-Q {#q-in-q}

原始的 802.1Q 僅允許一個 VLAN 頭；而 Q-in-Q 則允許兩個或更多 VLAN 頭。在 RouterOS 中，可以透過在一個 VLAN 介面之上再新增一個 VLAN 介面來配置 Q-in-Q。例如：

```ros
/interface/vlan
add name=vlan1 vlan-id=11 interface=ether1
add name=vlan2 vlan-id=12 interface=vlan1
```

如果有任何封包透過 'vlan2' 介面傳送，則會在乙太網頭中新增兩個 VLAN 標籤 - '11' 和 '12'。

## 屬性 {#properties}

**子選單：** `/interface/vlan`

| 屬性 | 描述 |
| :-- | :-- |
| **arp** (*disabled \| enabled \| local-proxy-arp \| proxy-arp \| reply-only*; 預設：**enabled**) | ARP 設定<ul><li><span className="ros-icon-success"><code>disabled</code></span> - 介面將不使用 ARP</li><li><span className="ros-icon-success"><code>enabled</code></span> - 介面將使用 ARP</li><li><span className="ros-icon-success"><code>local-proxy-arp</code></span> - 路由器在介面上執行代理 ARP，並向同一介面傳送回覆</li><li><span className="ros-icon-success"><code>proxy-arp</code></span> - 路由器在介面上執行代理 ARP，並向其他介面傳送回覆</li><li><span className="ros-icon-success"><code>reply-only</code></span> - 介面僅回覆來自與 IP/ARP 表中靜態條目匹配的 IP 地址/MAC 地址組合的請求。不會自動將動態條目儲存到 IP/ARP 表中。因此，為使通訊成功，必須已存在有效的靜態條目。</li></ul> |
| **arp-timeout**（*auto \| integer*；預設值：**auto**） | 在未從該 IP 收到封包後，ARP 記錄在 ARP 表中保有的時長。值 `auto` 等同於 IP/Settings 中的 `arp-timeout` 值，預設為 30s。 |
| **disabled** (*yes \| no*; 預設值: **no**) | 更改介面是否被停用。 |
| **interface** (*name*; 預設：) | VLAN 將在其上工作的介面名稱。 <br/><br/><strong>重要:</strong> 將 VLAN 介面新增到啟用了 [vlan-filtering 的網橋](./l3-hardware-offloading.md) 時，會自動將網橋介面標記為成員埠。帶有註釋 "added by vlan on bridge" 的動態條目將出現在 <code>/interface/bridge/vlan</code> 選單下。 <br/> |
| **l3-hw-offloading** (*yes \| no*; 預設：**yes**) | 啟用或停用每個 VLAN 介面上的 [L3HW](./l3-hardware-offloading.md#per-vlan-offloading)。此設定僅適用於支援 L3HW 解除安裝的裝置，並自 RouterOS v7.21 起可用。更多詳情 - [按 VLAN 解除安裝](./index.md#mvrp)。 |
| **mvrp** (*yes \| no*; 預設：**no**) | 指定此 VLAN 是否應作為申請者透過 Multiple VLAN Registration Protocol (MVRP) 宣告其屬性。其主要用例是建立在 Ethernet 介面上（例如 "router on a stick" 設定）並連線到支援 [MVRP](./index.md#mvrp) 的網橋的 VLAN。在已屬於啟用 MVRP 的網橋的 VLAN 介面上啟用此選項沒有效果，因為在這種情況下由網橋管理 MVRP。僅當 `use-service-tag` 被停用時，此屬性才有效。 |
| **mtu** (*integer: 68..65535*; 預設：**1500**) | Layer3 最大傳輸單元 |
| **name** (*string*；預設：) | 介面名稱 |
| **use-service-tag** (*yes \| no*; 預設：) | IEEE 802.1ad 相容的 Service Tag |
| **vlan-id** (*integer: 1..4094*; 預設：**1**) | 用於區分 VLAN 的虛擬 LAN 識別符號或標籤。屬於同一 VLAN 的所有計算機必須相同。 |

:::info
MTU 應設定為 1500 位元組，與乙太網介面上相同。但這可能不適用於某些乙太網卡，它們不支援接收/傳送添加了 VLAN 頭的全尺寸乙太網封包（1500 位元組資料 + 4 位元組 VLAN 頭 + 14 位元組乙太網頭）。在這種情況下，可以使用 MTU 1496，但請注意，如果必須透過介面傳送更大的封包，這將導致封包分片。同時請記住，如果源和目標之間的路徑 MTU 發現工作不正常，MTU 1496 可能會導致問題。
:::

## 配置示例 {#setup-examples}

---

### 影片示例 {#video-examples}

[VLAN 第 1 部分](http://youtube.com/watch?v=US2EU6cgHQU)、[VLAN 第 2 部分](http://youtube.com/watch?v=YMwOrc0LDP8)、[VLAN 第 3 部分](http://youtube.com/watch?v=7a_z1jAdIME)

### 二層 VLAN 示例 {#layer2-vlan-examples}

有多種可能的配置可供使用，但每種配置型別都是為特定的裝置集合而設計的，因為某些配置方法可以讓您獲得內建交換晶片的優勢，並取得更大的吞吐量。請檢視 [基礎 VLAN 交換](./user-guides/basic-vlan-switching.md) 指南，瞭解每種型別的裝置應使用哪種配置，以獲得最大的可能吞吐量和相容性。該指南展示瞭如何設定非常基本的 VLAN trunk/access 埠配置。

還有其他一些方式可以設定 VLAN 標記或 VLAN 交換，但推薦的方式是使用 [Bridge VLAN Filtering](./index.md#bridge-vlan-filtering)。請確保您沒有使用任何[已知的二層錯誤配置](./user-guides/layer2-misconfiguration.md)。

### 三層 VLAN 示例 {#layer3-vlan-examples}

#### 簡單的 VLAN 路由 {#simple-vlan-routing}

假設我們有多臺 MikroTik 路由器連線到一個集線器。請記住，集線器是 OSI 物理層裝置（如果路由器之間有一個集線器，那麼從 L3 的角度來看，它與在它們之間用乙太網線連線是一樣的）。為簡化起見，假設所有路由器都透過 ether1 介面連線到集線器，並且已按下圖所示分配了 IP 地址。然後在每臺路由器上建立 VLAN 介面。

R2 和 R4 的配置如下所示：

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

下一步是為 VLAN 介面分配 IP 地址。

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

此時，應該可以從路由器 R2 ping 通路由器 R4，反之亦然：

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

為確保 VLAN 配置正常工作，請嘗試從 R2 ping R1。如果 ping 超時，則說明 VLAN 已成功隔離。

```ros
 "From R2 to R1:"

 [admin@MikroTik] /ip/address> /ping 10.10.10.2
 10.10.10.2 ping timeout
 10.10.10.2 ping timeout
 3 packets transmitted, 0 packets received, 100% packet loss 
```

#### VLAN 間路由 {#intervlan-routing}

如果在交換器上實現了相互獨立的 VLAN，則需要一臺路由器來提供 VLAN 之間的通訊。交換器工作在 OSI 第二層，因此它僅使用乙太網頭進行轉發，而不檢查 IP 頭。因此，我們必須使用為每個 VLAN 充當閘道器的路由器。沒有路由器，主機無法與自身 VLAN 之外通訊。上述 VLAN 之間的路由過程稱為 VLAN 間通訊。

為了說明 VLAN 間通訊，我們將建立一個 trunk，它會在一條連線 MikroTik 路由器和一臺支援 VLAN trunk 的可管理交換器的鏈路上承載三個 VLAN（VLAN2、VLAN3 和 VLAN4）的流量。

如上圖所示，每個 VLAN 都有自己獨立的子網（廣播域）：

- VLAN 2 – 10.10.20.0/24。
- VLAN 3 – 10.10.30.0/24。
- VLAN 4 – 10.10.40.0/24。

在大多數交換器上配置 VLAN 都很簡單。我們需要定義哪些埠是 VLAN 的成員，並定義一個能在交換器和路由器之間承載帶標籤幀的 'trunk' 埠。

建立 VLAN 介面：

```ros
/interface/vlan
add name=VLAN2 vlan-id=2 interface=ether1 disabled=no
add name=VLAN3 vlan-id=3 interface=ether1 disabled=no
add name=VLAN4 vlan-id=4 interface=ether1 disabled=no
```

為 VLAN 新增 IP 地址：

```ros
/ip/address 
add address=10.10.20.1/24 interface=VLAN2
add address=10.10.30.1/24 interface=VLAN3
add address=10.10.40.1/24 interface=VLAN4
```

#### RouterOS /32 與 IP unnumbered 地址 {#routeros-32-and-ip-unnumbered-addresses}

在 RouterOS 中，要使用地址建立點到點隧道，您必須使用網路掩碼為 '/32' 的地址，這實際上為您提供了與某些廠商的 unnumbered IP 地址相同的功能。

有兩臺路由器 RouterA 和 RouterB，它們分別屬於網路 10.22.0.0/24 和 10.23.0.0/24，要使用 VLAN 作為承載連線這些路由器，配置如下：

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
