---
sidebar_key: "bridging-and-switching/user-guides/crs1xx-2xx-series-switches-examples"
sidebar_position: 4
title: "CRS1xx/2xx 系列交換器示例"
sidebar_label: "CRS1xx/2xx 系列交換器示例"
description: "本頁面提供 CRS1xx/2xx 系列交換器上 Cloud Router Switch 功能的配置示例和用例，涵蓋埠切換、帶 VLAN 過濾的管理訪問設定，以及基於 IP 訪問的安全注意事項。"
tags:
  - 'vlan'
  - 'bridge-hardware-offloading'
  - 'management-access'
source: https://manual.mikrotik.com/docs/7.25/bridging-and-switching/user-guides/crs1xx-2xx-series-switches-examples
captured_at: '2026-11-04T11:15:45+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Cloud Router Switch 系列是高度整合的交換器，配備高效能 MIPS CPU 和功能豐富的報文處理器。CRS 交換器可設計用於各種乙太網應用，包括非管理型交換器、二層管理型交換器、運營商交換器和有線/無線統一報文處理。

:::danger
本文適用於 CRS1xx 和 CRS2xx 系列交換器，不適用於搭載 Marvell Prestera 交換晶片的 MikroTik 裝置（例如 CRS3xx）。有關搭載 Marvell Prestera 交換晶片的 MikroTik 裝置，請參閱 [Marvell Prestera 交換晶片特性](../marvell-prestera-switch-chip-features.md)手冊。
:::

| 功能 | 描述 |
| :-- | :-- |
| **轉發** | <ul class="bullets"><li>可配置用於交換或路由的埠</li><li>完全非阻塞線速交換</li><li>在單播 FDB 中最多 16k 條 MAC 條目，用於第 2 層單播轉發</li><li>在組播 FDB 中最多 1k 條 MAC 條目，用於組播轉發</li><li>在保留 FDB 中最多 256 條 MAC 條目，用於控制和管理目的</li><li>所有轉發資料庫均支援 IVL 和 SVL</li><li>可配置的基於埠的 MAC 學習限制</li><li>巨型幀支援（CRS1xx/2xx：9204 位元組；CRS125/CRS109：4064 位元組）</li><li>支援 IGMP Snooping</li></ul> |
| **映象** | <ul class="bullets"><li>各種型別的映象：<ul class="bullets"><li>基於埠的映象</li><li>基於 VLAN 的映象</li><li>基於 MAC 的映象</li></ul></li><li>2 個獨立的映象分析埠</li></ul> |
| **VLAN** | <ul class="bullets"><li>完全相容 IEEE802.1Q 和 IEEE802.1ad VLAN</li><li>4k 個活動 VLAN</li><li>靈活的 VLAN 分配：<ul class="bullets"><li>基於埠的 VLAN</li><li>基於協定的 VLAN</li><li>基於 MAC 的 VLAN</li></ul></li><li>從任意到任意的 VLAN 轉換與交換</li><li>1:1 VLAN 交換 - VLAN 到埠對映</li><li>VLAN 過濾</li></ul> |
| **埠隔離與洩漏** | <ul class="bullets"><li>適用於 Private VLAN 實現</li><li>3 種埠配置型別：Promiscuous、Isolated 和 Community</li><li>最多 28 個 Community 配置</li><li>Leakage 配置允許繞過出方向 VLAN 過濾</li></ul> |
| **鏈路聚合** | <ul class="bullets"><li>支援靜態鏈路聚合組</li><li>最多 8 個 Port Trunk 組</li><li>每個 Port Trunk 組最多 8 個成員埠</li><li>硬體自動故障轉移和負載均衡</li></ul> |
| **服務質量（QoS）** | <ul class="bullets"><li>靈活的 QoS 分類和分配：<ul class="bullets"><li>基於埠</li><li>基於 MAC</li><li>基於 VLAN</li><li>基於協定</li><li>基於 PCP/DEI</li><li>基於 DSCP</li><li>基於 ACL</li></ul></li><li>用於服務提供商與用戶端網路之間 QoS 域轉換的 QoS 重標記和重對映</li><li>根據配置的優先順序覆蓋每個 QoS 分配</li></ul> |
| **整形與排程** | <ul class="bullets"><li>每個物理埠 8 個佇列</li><li>按埠、按佇列、按佇列組整形</li></ul> |
| **訪問控制列表** | <ul class="bullets"><li>入方向與出方向 ACL 表</li><li>最多 128 條 ACL 規則（受 RouterOS 限制）</li><li>基於埠、L2、L3、L4 協定頭欄位的分類</li><li>ACL 操作包括過濾、轉發和修改協定頭欄位</li></ul> |

### 適用的交換器型號 {#applicable-switch-models}

---

下表說明了 Cloud Router Switch 各型號之間的主要差異。

|  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| **型號** | **交換晶片** | **CPU** | **無線** | **SFP+ 埠** | **訪問控制列表** | **巨型幀（位元組）** |
| **CRS105-5S-FB** | QCA-8511 | 400MHz | - | - | + | 9204 |
| **CRS106-1C-5S** | QCA-8511 | 400MHz | - | - | + | 9204 |
| **CRS112-8G-4S** | QCA-8511 | 400MHz | - | - | + | 9204 |
| **CRS210-8G-2S+** | QCA-8519 | 400MHz | - | + | + | 9204 |
| **CRS212-1G-10S-1S+** | QCA-8519 | 400MHz | - | + | + | 9204 |
| **CRS226-24G-2S+** | QCA-8519 | 400MHz | - | + | + | 9204 |
| **CRS125-24G-1S** | QCA-8513L | 600MHz | - | - | - | 4064 |
| **CRS125-24G-1S-2HnD** | QCA-8513L | 600MHz | + | - | - | 4064 |
| **CRS109-8G-1S-2HnD** | QCA-8513L | 600MHz | + | - | - | 4064 |

### 縮寫與說明 {#abbreviations-and-explanations}

---

CVID - 客戶 VLAN ID：IEEE 802.1ad 幀的內層 VLAN 標籤 ID

SVID - 服務 VLAN ID：IEEE 802.1ad 幀的外層 VLAN 標籤 ID

IVL - 獨立 VLAN 學習 - 學習和查詢基於 MAC 地址和 VLAN ID 兩者。

SVL - 共享 VLAN 學習 - 學習和查詢基於 MAC 地址 - 而不是 VLAN ID。

TPID - 標籤協定識別符號

PCP - 優先順序程式碼點：一個 3 位欄位，表示 IEEE 802.1p 優先順序

DEI - 丟棄資格指示符

DSCP - 差分服務程式碼點

丟棄優先順序 - 一種內部 CRS 交換器 QoS 屬性，用於封包入隊或丟棄。

### 埠交換 {#port-switching}

---

要在 CRS1xx/2xx 系列交換器上設定埠交換，請參閱 [網橋硬體解除安裝](../index.md#bridge-hardware-offloading) 頁面。

:::warning
在建立啟用硬體解除安裝的網橋並新增交換埠組時，CRS 交換器會建立動態保留 VLAN 條目（VLAN4091；VLAN4090；VLAN4089 等）。這些 VLAN 是內部執行所必需的，其優先順序低於使用者配置的 VLAN。
:::

:::danger
透過使用多個啟用了硬體解除安裝的網橋，可以建立多個隔離的交換器組；這僅在 CRS1xx/2xx 系列交換器上可行。對於更復雜的設定（例如 VLAN 過濾），應改用埠隔離功能。
:::

#### 多個交換器組 {#multiple-switch-groups}

CRS1xx/2xx 系列交換器允許使用多個帶硬體解除安裝的網橋；這樣可以輕鬆隔離多個交換器組。只需建立多個網橋並啟用硬體解除安裝即可完成。

:::warning
多硬體解除安裝橋接配置被設計為一種快速且簡單的埠隔離解決方案，但它限制了 CRS 交換晶片所支援的部分 VLAN 功能。對於高階配置，請在 CRS 交換晶片內為所有埠使用一個橋接，配置 VLAN，並透過埠隔離配置檔案配置來隔離埠組。
:::

:::danger
CRS1xx/2xx 系列交換器可以執行多個啟用 (R)STP 的硬體解除安裝網橋，但不建議這樣做，因為裝置並非設計為在硬體層面執行多個 (R)STP 例項。要在啟用 (R)STP 的同時隔離多個交換器組，應透過埠隔離配置檔案配置來隔離埠組。
:::

## 管理訪問配置 {#management-access-configuration}

---

一般來說，出於安全原因，交換器只應使用內建交換晶片轉發封包，而不應允許訪問裝置本身。可以使用裝置的序列埠進行管理訪問，但在大多數情況下，這種訪問方式並不理想，使用 IP 地址訪問更合適。在這種情況下，你需要配置管理訪問。

在所有型別的管理訪問中，都假定必須將埠加入同一個交換組。使用以下命令將所需埠加入同一個交換組：

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether3 hw=yes
add bridge=bridge1 interface=ether4 hw=yes
add bridge=bridge1 interface=ether5 hw=yes
```

還應給網橋介面分配 IP 地址，以便可以透過 IP 地址訪問裝置（也可以透過 MAC 地址訪問裝置）：

```ros
/ip/address
add address=192.168.88.1/24 interface=bridge1
```

### 未標記 {#untagged}

如果未啟用無效 VLAN 過濾，則已經允許從任何埠透過帶標記或未標記（**VLAN 0**）流量對裝置進行管理訪問，但這不是良好實踐；這可能導致安全問題，並在某些情況下（最常見的是廣播型別流量）導致裝置 CPU 過載。

如果你打算使用無效 VLAN 過濾（你應該這樣做），則必須將要用於訪問交換器的埠新增到 VLAN 表中，以允許未標記（**VLAN 0**）流量，例如，如果你想從 **ether2** 訪問交換器：

```ros
/interface/ethernet/switch/vlan
add vlan-id=0 ports=ether2,switch1-cpu  
```

### 帶標記 {#tagged}

僅允許帶標記流量透過特定埠對裝置進行管理訪問是更好的做法。例如，要僅允許 **VLAN99** 透過 **ether2** 訪問裝置，應首先向 VLAN 表新增條目，這將允許所選埠和 CPU 埠（**switch1-cpu**）轉發所選 VLAN ID，從而允許管理訪問：

```ros
/interface/ethernet/switch/vlan
add ports=ether2,switch1-cpu vlan-id=99
```

從 CPU 發出的封包（例如 ping 應答）將不帶 VLAN 標記；要解決此問題，需要指定對於特定 VLAN ID，哪些埠應始終傳送帶 VLAN 標記的封包：

```ros
/interface/ethernet/switch/egress-vlan-tag
add tagged-ports=ether2,switch1-cpu vlan-id=99
```

在設定有效的 VLAN99 配置後，可以啟用未知/無效 VLAN 過濾，這將不允許透過 VLAN 表中指定埠以外的埠進行管理訪問：

```ros
/interface/ethernet/switch
set drop-if-invalid-or-src-port-not-member-of-vlan-on-ports=ether2,ether3,ether4,ether5
```

在此示例中，將使用 VLAN99 訪問裝置。必須在網橋上建立 VLAN 介面，併為其分配 IP 地址。

```ros
/interface/vlan
add interface=bridge1 name=MGMT vlan-id=99
/ip/address
add address=192.168.99.1/24 interface=MGMT
```

## VLAN {#vlan}

---

:::danger 
鎖定風險。
強烈建議在配置 VLAN 之前測試並準備好序列埠控制檯線纜。配置錯誤很容易使您無法透過 CPU 或已連線埠訪問裝置。
:::

:::tip
排查快取的 MAC 地址問題。
由於已學習的 MAC 地址，某些更改可能看起來有延遲。如果更改後流量未按預期流動，請重新整理單播轉發表：
`/interface/ethernet/switch/unicast-fdb/flush`
:::

:::info
架構最佳實踐。
使用多個硬體解除安裝網橋是實現簡單埠隔離的快速方法，但它限制了 CRS 交換晶片上的高階 VLAN 功能。對於高階設定，請為所有埠使用**單個網橋**，配置 VLAN，並使用埠隔離配置檔案隔離埠組。
:::

### 基於埠的 VLAN {#port-based-vlan}

:::warning
對於 CRS3xx 系列裝置，必須使用網橋 VLAN 過濾；更多資訊請參閱 [網橋 VLAN 過濾](../index.md#bridge-vlan-filtering) 小節。
:::

#### 示例 1（幹道埠和接入埠） {#example-1-trunk-and-access-ports}

![Access Ports](/img/dcbdce357964f958.webp)

將所需埠加入交換：

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether6 hw=yes
add bridge=bridge1 interface=ether7 hw=yes
add bridge=bridge1 interface=ether8 hw=yes
```

為每個接入埠指定交換器必須為未標記（VLAN0）流量設定的 VLAN ID：

```ros
/interface/ethernet/switch/ingress-vlan-translation
add ports=ether6 customer-vid=0 new-customer-vid=200
add ports=ether7 customer-vid=0 new-customer-vid=300
add ports=ether8 customer-vid=0 new-customer-vid=400
```

:::warning
當在 `/interface/ethernet/switch/ingress-vlan-translation` 下建立條目時，交換晶片會在指定埠的入站幀上新增 VLAN 標記。要為同一埠上的出站幀移除 VLAN 標記，應為同一 VLAN ID 建立一個 `/interface/ethernet/switch/egress-vlan-tag` 條目，並在其中僅指定帶標記埠。如果特定 VLAN 僅在接入埠之間轉發，仍應建立不帶任何帶標記埠的 `/interface/ethernet/switch/egress-vlan-tag` 條目。另一種選擇是在 `/interface/ethernet/switch/egress-vlan-translation` 選單下建立額外條目，以設定未標記（VLAN0）流量。
:::

還必須指定哪些 VLAN 應以帶 VLAN 標記的方式從幹道埠發出。使用 tagged-ports 屬性來設定幹道埠：

```ros
/interface/ethernet/switch/egress-vlan-tag
add tagged-ports=ether2 vlan-id=200
add tagged-ports=ether2 vlan-id=300
add tagged-ports=ether2 vlan-id=400
```

向 VLAN 表新增條目，為每個埠和每個 VLAN ID 指定 VLAN 成員關係：

```ros
/interface/ethernet/switch/vlan
add ports=ether2,ether6 vlan-id=200
add ports=ether2,ether7 vlan-id=300
add ports=ether2,ether8 vlan-id=400
```

在設定有效的 VLAN 配置後，可以啟用未知/無效 VLAN 過濾：

```ros
/interface/ethernet/switch
set drop-if-invalid-or-src-port-not-member-of-vlan-on-ports=ether2,ether6,ether7,ether8
```

:::warning
可以同時使用內建交換晶片和 CPU 來建立 Switch-Router 設定，使裝置同時充當交換器和路由器。
:::

#### 示例 2（幹道埠和混合埠） {#example-2-trunk-and-hybrid-ports}

![Hybrid Ports](/img/90b987271e134d95.webp)

將所需埠加入交換：

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether6 hw=yes
add bridge=bridge1 interface=ether7 hw=yes
add bridge=bridge1 interface=ether8 hw=yes
```

為每個接入埠指定交換器必須為未標記（VLAN0）流量設定的 VLAN ID：

```ros
/interface/ethernet/switch/ingress-vlan-translation
add ports=ether6 customer-vid=0 new-customer-vid=200
add ports=ether7 customer-vid=0 new-customer-vid=300
add ports=ether8 customer-vid=0 new-customer-vid=400
```

透過將埠指定為 tagged-ports，交換器會始終以帶對應 VLAN ID 標記的封包形式傳送封包。按上圖新增相應條目：

```ros
/interface/ethernet/switch/egress-vlan-tag
add tagged-ports=ether2,ether7,ether8 vlan-id=200
add tagged-ports=ether2,ether6,ether8 vlan-id=300
add tagged-ports=ether2,ether6,ether7 vlan-id=400
```

向 VLAN 表新增條目，為每個埠和每個 VLAN ID 指定 VLAN 成員關係：

```ros
/interface/ethernet/switch/vlan
add ports=ether2,ether6,ether7,ether8 vlan-id=200 learn=yes
add ports=ether2,ether6,ether7,ether8 vlan-id=300 learn=yes
add ports=ether2,ether6,ether7,ether8 vlan-id=400 learn=yes
```

在設定有效的 VLAN 配置後，可以啟用未知/無效 VLAN 過濾：

```ros
/interface/ethernet/switch
set drop-if-invalid-or-src-port-not-member-of-vlan-on-ports=ether2,ether6,ether7,ether8
```

### 基於協定的 VLAN {#protocol-based-vlan}

![Protocol Based VLAN](/img/279b50d6fabcdc21.webp)

將所需埠加入交換：

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether6 hw=yes
add bridge=bridge1 interface=ether7 hw=yes
add bridge=bridge1 interface=ether8 hw=yes
```

為 IP 和 ARP 協定設定 VLAN：

```ros
/interface/ethernet/switch/protocol-based-vlan
add port=ether2 protocol=arp set-customer-vid-for=all new-customer-vid=0
add port=ether6 protocol=arp set-customer-vid-for=all new-customer-vid=200
add port=ether2 protocol=ip set-customer-vid-for=all new-customer-vid=0
add port=ether6 protocol=ip set-customer-vid-for=all new-customer-vid=200
```

為 IPX 協定設定 VLAN：

```ros
/interface/ethernet/switch/protocol-based-vlan
add port=ether2 protocol=ipx set-customer-vid-for=all new-customer-vid=0
add port=ether7 protocol=ipx set-customer-vid-for=all new-customer-vid=300
```

為 AppleTalk AARP 和 AppleTalk DDP 協定設定 VLAN：

```ros
/interface/ethernet/switch/protocol-based-vlan
add port=ether2 protocol=0x80F3 set-customer-vid-for=all new-customer-vid=0
add port=ether8 protocol=0x80F3 set-customer-vid-for=all new-customer-vid=400
add port=ether2 protocol=0x809B set-customer-vid-for=all new-customer-vid=0
add port=ether8 protocol=0x809B set-customer-vid-for=all new-customer-vid=400
```

### 基於 MAC 的 VLAN {#mac-based-vlan}

:::danger
在內部，基於 MAC 的 VLAN 中的所有 MAC 地址都會進行雜湊。某些 MAC 地址可能具有相同的雜湊；如果該雜湊與已載入 MAC 地址的雜湊匹配，就會阻止某個 MAC 地址載入到交換晶片中。因此，建議將基於埠的 VLAN 與基於 MAC 的 VLAN 結合使用。這是硬體限制。
:::

![MAC Based VLAN](/img/fb1b49b2f44e71a3.webp)

將所需埠加入交換：

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether7 hw=yes
```

在接入埠上啟用基於 MAC 的 VLAN 轉換：

```ros
/interface/ethernet/switch/port
set ether7 allow-fdb-based-vlan-translate=yes
```

在基於 MAC 的 VLAN 表中新增 MAC 到 VLAN 的對映條目：

```ros
/interface/ethernet/switch/mac-based-vlan
add src-mac=A4:12:6D:77:94:43 new-customer-vid=200
add src-mac=84:37:62:DF:04:20 new-customer-vid=300
add src-mac=E7:16:34:A1:CD:18 new-customer-vid=400
```

在 ether2 埠上新增 VLAN200、VLAN300 和 VLAN400 標記，使其成為 VLAN 幹道埠：

```ros
/interface/ethernet/switch/egress-vlan-tag
add tagged-ports=ether2 vlan-id=200
add tagged-ports=ether2 vlan-id=300
add tagged-ports=ether2 vlan-id=400
```

此外，還要向 VLAN 表新增條目，為每個埠指定 VLAN 成員關係，並啟用未知/無效 VLAN 過濾，請參閱下面的示例——未知/無效 VLAN 過濾。對於向網橋添加了更多介面的網路設定，這是必需的，因為它允許定義 VLAN 邊界。

### VLAN 間路由 {#intervlan-routing}

![VLAN Routing](/img/f659d62947a98802.webp)

VLAN 間路由配置由兩個主要部分組成——交換晶片中的 VLAN 標記和 RouterOS 中的路由。透過將此配置與每個 VLAN 的 DHCP 伺服器、Hotspot、PPP 和其他功能結合使用，可將其應用於許多場景。

將所需埠加入交換：

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether6 hw=yes
add bridge=bridge1 interface=ether7 hw=yes
add bridge=bridge1 interface=ether8 hw=yes
```

在 CPU 埠上為所有 VLAN 設定 VLAN 標記，使封包在路由之前帶上標記：

```ros
/interface/ethernet/switch/egress-vlan-tag
add tagged-ports=switch1-cpu vlan-id=200
add tagged-ports=switch1-cpu vlan-id=300
add tagged-ports=switch1-cpu vlan-id=400
```

新增入站 VLAN 轉換規則，以確保在接入埠上正確分配 VLAN ID：

```ros
/interface/ethernet/switch/ingress-vlan-translation
add ports=ether6 customer-vid=0 new-customer-vid=200
add ports=ether7 customer-vid=0 new-customer-vid=300
add ports=ether8 customer-vid=0 new-customer-vid=400
```

在網橋介面之上建立 VLAN 介面：

```ros
/interface/vlan
add name=VLAN200 interface=bridge1 vlan-id=200
add name=VLAN300 interface=bridge1 vlan-id=300
add name=VLAN400 interface=bridge1 vlan-id=400
```

:::danger
確保 VLAN 介面建立在網橋介面之上，而不是建立在任何物理介面之上。如果 VLAN 介面建立在從屬介面上，則封包可能無法正確接收，從而導致路由失敗。更多詳細資訊可在 [從屬介面上的 VLAN 介面](./layer2-misconfiguration.md#vlan-interface-on-a-slave-interface) 手冊頁中找到。
:::

在已建立的 VLAN 介面上新增 IP 地址。在此示例中，向 VLAN200、VLAN300 和 VLAN400 介面新增三個 192.168.x.1 地址：

```ros
/ip/address
add address=192.168.20.1/24 interface=VLAN200
add address=192.168.30.1/24 interface=VLAN300
add address=192.168.40.1/24 interface=VLAN400
```

### 未知/無效 VLAN 過濾 {#unknowninvalid-vlan-filtering}

VLAN 成員關係在 VLAN 表中定義。新增包含 VLAN ID 和埠的條目會使該 VLAN 流量在這些埠上有效。設定有效的 VLAN 配置後，可以啟用未知/無效 VLAN 過濾。此 VLAN 過濾配置示例適用於 VLAN 間路由設定。

```ros
/interface/ethernet/switch/vlan
add ports=switch1-cpu,ether6 vlan-id=200
add ports=switch1-cpu,ether7 vlan-id=300
add ports=switch1-cpu,ether8 vlan-id=400
```

- 選項 1：在特定埠上停用無效 VLAN 轉發（更常見）。

```ros
/interface/ethernet/switch
set drop-if-invalid-or-src-port-not-member-of-vlan-on-ports=ether6,ether7,ether8
```

- 選項 2：在所有埠上停用無效 VLAN 轉發。

```ros
/interface/ethernet/switch
set forward-unknown-vlan=no
```

:::danger
在啟用了未知/無效 VLAN 過濾的單個交換晶片上使用多個網橋可能會導致意外行為。使用 VLAN 過濾時，應始終使用單個網橋配置。如果需要埠隔離，則應使用埠隔離功能，而不是使用多個網橋。
:::

### VLAN 隧道（Q-in-Q） {#vlan-tunneling-q-in-q}

此示例涵蓋典型的 VLAN 隧道用例：服務提供商裝置新增另一個 VLAN 標記以實現獨立轉發，同時允許客戶使用自己的 VLAN。

:::warning
此示例僅包含服務 VLAN 標記部分。建議另外在埠上設定未知/無效 VLAN 過濾配置。
:::

![QinQ](/img/1f0680bc5266cc50.webp)

**CRS-1**：服務提供商網路邊緣的第一臺交換器必須正確識別埠上來自客戶 VLAN ID 的流量，並使用入站 VLAN 轉換規則分配新的服務 VLAN ID。用於服務提供商 VLAN 標記的 VLAN 幹道埠配置在同一個 `egress-vlan-tag` 表中。與基本的基於埠 VLAN 配置的主要區別在於，必須將 CRS 交換晶片設定為根據服務（*外層*）VLAN ID 而不是客戶（*內層*）VLAN ID 進行轉發。

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether1 hw=yes
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether9 hw=yes

/interface/ethernet/switch/ingress-vlan-translation
add customer-vid=200 new-service-vid=400 ports=ether1
add customer-vid=300 new-service-vid=500 ports=ether2

/interface/ethernet/switch/egress-vlan-tag
add tagged-ports=ether9 vlan-id=400
add tagged-ports=ether9 vlan-id=500

/interface/ethernet/switch
set bridge-type=service-vid-used-as-lookup-vid
```

**CRS-2**：服務提供商網路中的第二臺交換器只需要將交換埠配置為根據服務（*外層*）VLAN ID 而不是客戶（*內層*）VLAN ID 進行轉發。

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether9 hw=yes
add bridge=bridge1 interface=ether10 hw=yes

/interface/ethernet/switch
set bridge-type=service-vid-used-as-lookup-vid
```

**CRS-3**：第三臺交換器的配置與 CRS-1 類似：

- 使用網橋的交換器組中的埠。
- 用於在埠上定義新服務 VLAN 分配的入站 VLAN 轉換規則。
- 用於服務提供商 VLAN 幹道的 tagged-ports。
- 將 CRS 交換晶片設定為在交換查詢中使用服務 VLAN ID。

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether3 hw=yes
add bridge=bridge1 interface=ether4 hw=yes
add bridge=bridge1 interface=ether10 hw=yes

/interface/ethernet/switch/ingress-vlan-translation
add customer-vid=200 new-service-vid=400 ports=ether3
add customer-vid=300 new-service-vid=500 ports=ether4

/interface/ethernet/switch/egress-vlan-tag
add tagged-ports=ether10 vlan-id=400
add tagged-ports=ether10 vlan-id=500

/interface/ethernet/switch
set bridge-type=service-vid-used-as-lookup-vid
```

### CVID 堆疊 {#cvid-stacking}

可以將 CRS1xx/CRS2xx 系列交換器用於 CVID 堆疊設定。CRS1xx/CRS2xx 系列交換器能夠基於帶有兩個 CVID 標記（雙 CVID 標記）的帶標記封包的外層標記進行 VLAN 過濾。這些交換器還能夠在現有 CVID 標記之上新增另一個 CVID 標記（CVID 堆疊）。例如，在 **ether1** 接收帶有 CVID 10 的帶標記封包，但要求 **ether2** 以另一個標記 CVID 20（VLAN10 位於 VLAN20 內）傳送這些封包，同時過濾掉任何其他 VLAN 的設定中，必須配置以下內容：

將 **ether1** 和 **ether2** 加入同一個交換組：

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether1 hw=yes
add bridge=bridge1 interface=ether2 hw=yes
```

將交換器設定為根據服務標記（0x88a8）過濾 VLAN：

```ros
/interface/ethernet/switch
set bridge-type=service-vid-used-as-lookup-vid
```

為 **ether1** 上帶有 CVID 10 標記的封包新增服務標記 SVID 20：

```ros
/interface/ethernet/switch/ingress-vlan-translation
add customer-vid=10 new-service-vid=20 ports=ether1
```

將 **ether2** 指定為 SVID 20 的帶標記/幹道埠：

```ros
/interface/ethernet/switch/egress-vlan-tag
add tagged-ports=ether2 vlan-id=20
```

允許 **ether1** 和 **ether2** 轉發 SVID 20：

```ros
/interface/ethernet/switch/vlan
add ports=ether1,ether2 vlan-id=20
```

在 **ether2** 上將 SVID EtherType（0x88a8）覆蓋為 CVID EtherType（0x8100）：

```ros
/interface/ethernet/switch/port
set ether2 egress-service-tpid-override=0x8100 ingress-service-tpid-override=0x8100
```

啟用未知/無效 VLAN 過濾：

```ros
/interface/ethernet/switch
set drop-if-invalid-or-src-port-not-member-of-vlan-on-ports=ether1,ether2
```

:::warning
由於交換器被設定為根據服務標記查詢 VLAN ID，而該服務標記已被覆蓋為不同的 EtherType，因此 VLAN 過濾僅針對封包的外層標記執行；不會檢查內層標記。
:::

## 映象 {#mirroring}

---

![Mirroring](/img/7c1963a9e5b62ba0.webp)

Cloud Router Switches 支援三種類型的映象。基於埠的映象可應用於任何交換晶片埠；基於 VLAN 的映象適用於所有指定 VLAN，與交換晶片埠無關；基於 MAC 的映象會複製從單播轉發表中配置的埠可到達的特定裝置傳送或接收的流量。

### 基於埠的映象 {#port-based-mirroring}

第一個配置將 ether5 埠設定為 mirror0 分析埠，用於入站和出站映象。映象流量將傳送到此埠。從 ether6 埠啟用基於埠的入站和出站映象。

```ros
/interface/ethernet/switch
set ingress-mirror0=ether5 egress-mirror0=ether5

/interface/ethernet/switch/port
set ether6 ingress-mirror-to=mirror0 egress-mirror-to=mirror0
```

### 基於 VLAN 的映象 {#vlan-based-mirroring}

第二個示例要求將埠加入同一個交換組。映象配置將 ether5 埠設定為 mirror0 分析埠，並設定當發生來自 VLAN 的映象時使用 mirror0 埠。VLAN 表條目僅為 ether2 和 ether7 埠之間的 VLAN 300 流量啟用映象。

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether7 hw=yes

/interface/ethernet/switch
set ingress-mirror0=ether5 vlan-uses=mirror0

/interface/ethernet/switch/vlan
add ports=ether2,ether7 vlan-id=300 learn=yes ingress-mirror=yes
```

### 基於 MAC 的映象 {#mac-based-mirroring}

第三個配置同樣要求將埠作為一個組加入交換。映象配置將 ether5 埠設定為 mirror0 分析埠，並設定當發生來自單播轉發表的映象時使用 mirror0 埠。單播轉發表中的條目為來自 ether8 埠、源 MAC 地址或目的 MAC 地址為 E7:16:34:A1:CD:18 的封包啟用映象。

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether8 hw=yes

/interface/ethernet/switch
set ingress-mirror0=ether5 fdb-uses=mirror0

/interface/ethernet/switch/unicast-fdb
add port=ether8 mirror=yes svl=yes mac-address=E7:16:34:A1:CD:18
```

## 幹道（Trunking） {#trunking}

---

![Trunking 3](/img/601e6a4b07f4a6d0.webp)

Cloud Router Switches 中的幹道提供靜態鏈路聚合組，並具有硬體自動故障轉移和負載均衡功能。尚不支援相容 IEEE802.3ad 和 IEEE802.1ax 的鏈路聚合控制協定。最多支援 8 個幹道組，每個幹道組最多支援 8 個幹道成員埠。

配置需要一組已加入交換的埠，以及在幹道表中的條目：

```ros
/interface/bridge
add name=bridge1 protocol-mode=none
/interface/bridge/port
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether6 hw=yes
add bridge=bridge1 interface=ether7 hw=yes
add bridge=bridge1 interface=ether8 hw=yes

/interface/ethernet/switch/trunk
add name=trunk1 member-ports=ether6,ether7,ether8
```

此示例還展示了另一端 RouterOS 中正確的繫結配置：

```ros
/interface/bonding
add name=bonding1 slaves=ether2,ether3,ether4 mode=balance-xor transmit-hash-policy=layer-2-and-3
```

:::danger
網橋 (R)STP 不知道底層交換器幹道配置，某些幹道埠可能會進入丟棄或阻塞狀態。當幹道成員埠連線到其他網橋時，應停用 (R)STP 或過濾掉幹道裝置之間的任何 BPDU（例如使用 ACL 規則）。
:::

## 每埠受限 MAC 訪問 {#limited-mac-access-per-port}

---

停用 MAC 學習並配置靜態 MAC 地址，可以控制哪些確切裝置能夠與 CRS1xx/2xx 交換器通訊以及透過它們通訊。

配置需要一組已加入交換的埠、在這些埠上停用 MAC 學習，以及靜態 FDB 條目：

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether6 hw=yes learn=no unknown-unicast-flood=no
add bridge=bridge1 interface=ether7 hw=yes learn=no unknown-unicast-flood=no

/interface/ethernet/switch/unicast-fdb
add mac-address=4C:5E:0C:00:00:01 port=ether6 svl=yes
add mac-address=D4:CA:6D:00:00:02 port=ether7 svl=yes

/interface/ethernet/switch/acl
add action=drop src-mac-addr-state=sa-not-found src-ports=ether6,ether7 table=egress
add action=drop src-mac-addr-state=static-station-move src-ports=ether6,ether7 table=egress
```

CRS1xx/2xx 交換器還允許每個埠學習一個動態 MAC，以確保無論其 MAC 地址是什麼，只連線一個終端使用者裝置：

```ros
/interface/ethernet/switch/port
set ether6 learn-limit=1
set ether7 learn-limit=1
```

## 隔離 {#isolation}

---

### 埠級隔離 {#port-level-isolation}

![Port Level Isolation](/img/b0340fbe7ac5c7ee.webp)

埠級隔離常用於 Private VLAN，其中：

- 一個或多個上行鏈路埠由所有使用者共享，用於訪問閘道器或路由器。
- 埠組 Isolated Ports 用於訪客使用者。只能透過上行鏈路埠進行通訊。
- 埠組 Community 0 用於部門 A。允許組成員之間以及透過上行鏈路埠進行通訊。
- 埠組 Community X 用於部門 X。允許組成員之間以及透過上行鏈路埠進行通訊。

Cloud Router Switches 使用埠級隔離配置模板來實現 Private VLAN：

- 上行鏈路埠——埠級隔離配置模板 0
- 隔離埠——埠級隔離配置模板 1
- Community 0 埠——埠級隔離配置模板 2
- Community X（X \<= 30）埠——埠級隔離配置模板 X

**此示例需要一組已加入交換的埠。假設此示例中使用的所有埠都在同一個交換器組中。**

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether6 hw=yes
add bridge=bridge1 interface=ether7 hw=yes
add bridge=bridge1 interface=ether8 hw=yes
add bridge=bridge1 interface=ether9 hw=yes
add bridge=bridge1 interface=ether10 hw=yes
```

埠隔離配置的第一部分是設定上行鏈路埠——為 ether2 將埠配置模板設定為 0：

```ros
/interface/ethernet/switch/port
set ether2 isolation-leakage-profile-override=0
```

然後繼續在所有隔離埠上設定隔離配置模板 1，併為埠隔離配置模板 1 新增通訊埠：

```ros
/interface/ethernet/switch/port
set ether5 isolation-leakage-profile-override=1
set ether6 isolation-leakage-profile-override=1

/interface/ethernet/switch/port-isolation
add port-profile=1 ports=ether2 type=dst
```

設定 Community 2 和 Community 3 埠的配置類似：

```ros
/interface/ethernet/switch/port
set ether7 isolation-leakage-profile-override=2
set ether8 isolation-leakage-profile-override=2

/interface/ethernet/switch/port-isolation
add port-profile=2 ports=ether2,ether7,ether8 type=dst

/interface/ethernet/switch/port
set ether9 isolation-leakage-profile-override=3
set ether10 isolation-leakage-profile-override=3

/interface/ethernet/switch/port-isolation
add port-profile=3 ports=ether2,ether9,ether10 type=dst
```

### 協定級隔離 {#protocol-level-isolation}

![Protocol Level Isolation](/img/efafb0531d23c36a.webp)

CRS 交換器上的協定級隔離可用於增強網路安全。例如，限制使用者（ether2、ether3、ether4、ether5）之間的 DHCP 流量，並僅允許其發往受信任的 DHCP 伺服器埠（ether1），可以防止 DHCP 欺騙攻擊等安全風險。以下示例展示瞭如何在 CRS 上配置。

將所需埠加入交換：

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether1 hw=yes
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether3 hw=yes
add bridge=bridge1 interface=ether4 hw=yes
add bridge=bridge1 interface=ether5 hw=yes
```

為所有 DHCP 用戶端埠設定相同的 Community 埠配置模板。Community 埠配置模板編號為 2 到 30。

```ros
/interface/ethernet/switch/port
set ether2 isolation-leakage-profile-override=2
set ether3 isolation-leakage-profile-override=2
set ether4 isolation-leakage-profile-override=2
set ether5 isolation-leakage-profile-override=2
```

併為選定的 Community（2）配置埠隔離/洩漏配置模板，以僅允許發往受信任 DHCP 伺服器所在埠的 DHCP 流量。必須將 registration-status 和 traffic-type 屬性設定為空，才能僅對 DHCP 協定應用限制。

```ros
/interface/ethernet/switch/port-isolation
add port-profile=2 protocol-type=dhcpv4 type=dst forwarding-type=bridged ports=ether1 registration-status="" traffic-type=""
```

## 服務質量（QoS） {#quality-of-service-qos}

---

**QoS 配置方案**

基於 MAC 的流量排程和整形：[UFDB 中的 MAC 地址] -> [QoS 組] -> [優先順序] -> [佇列] -> [整形器]

基於 VLAN 的流量排程和整形：[VLAN 表中的 VLAN ID] -> [QoS 組] -> [優先順序] -> [佇列] -> [整形器]

基於協定的流量排程和整形：[協定 VLAN 表中的協定] -> [QoS 組] -> [優先順序] -> [佇列] -> [整形器]

基於 PCP/DEI 的流量排程和整形：[交換器埠 PCP/DEI 對映] -> [優先順序] -> [佇列] -> [整形器]

基於 DSCP 的流量排程和整形：[QoS DSCP 對映] -> [優先順序] -> [佇列] -> [整形器]

### 使用內部優先順序的基於 MAC 的流量排程 {#mac-based-traffic-scheduling-using-internal-priority}

在嚴格優先順序排程模式中，最高優先順序佇列最先得到服務。佇列編號表示優先順序，佇列編號最高的佇列具有最高優先順序。流量從最高優先順序佇列傳送，直到該佇列為空，然後轉到下一個最高優先順序佇列，依此類推。如果出站埠沒有擁塞，封包一收到就會發送。如果高優先順序流量持續到來的埠發生擁塞，較低優先順序的佇列會得不到服務。

在所有 CRS 交換器上，根據內部優先順序進行基於 MAC 的出站流量排程的方案如下：[MAC 地址] -> [QoS 組] -> [優先順序] -> [佇列]；  
在此示例中，host1（E7:16:34:00:00:01）和 host2（E7:16:34:00:00:02）在 ether7 埠上的傳送流量將具有較高優先順序 1，其餘主機將具有較低優先順序 0。請注意，CRS 每個埠最多有 8 個佇列。

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether6 hw=yes
add bridge=bridge1 interface=ether7 hw=yes
add bridge=bridge1 interface=ether8 hw=yes
```

建立一個供 UFDB 使用的 QoS 組：

```ros
/interface/ethernet/switch/qos-group
add name=group1 priority=1
```

新增 UFDB 條目以匹配 ether7 上的特定 MAC，並應用 QoS group1：

```ros
/interface/ethernet/switch/unicast-fdb
add mac-address=E7:16:34:00:00:01 port=ether7 qos-group=group1 svl=yes
add mac-address=E7:16:34:00:00:02 port=ether7 qos-group=group1 svl=yes
```

配置 ether7 埠佇列，使其僅針對目的地址按嚴格優先順序和 QoS 方案工作：

```ros
/interface/ethernet/switch/port
set ether7 per-queue-scheduling="strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0" priority-to-queue=0:0,1:1 qos-scheme-precedence=da-based
```

### 使用內部優先順序的基於 MAC 的流量整形 {#mac-based-traffic-shaping-using-internal-priority}

根據內部優先順序進行基於 MAC 的流量整形的方案如下：[MAC 地址] -> [QoS 組] -> [優先順序] -> [佇列] -> [整形器]；  
在此示例中，不限速流量將具有優先順序 0，限速流量將具有優先順序 1，頻寬限制為 10Mbit。請注意，CRS 每個埠最多有 8 個佇列。

建立一組用於交換的埠：

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether6 hw=yes
add bridge=bridge1 interface=ether7 hw=yes
add bridge=bridge1 interface=ether8 hw=yes
```

建立一個供 UFDB 使用的 QoS 組：

```ros
/interface/ethernet/switch/qos-group
add name=group1 priority=1
```

新增 UFDB 條目以匹配 ether8 上的特定 MAC，並應用 QoS group1：

```ros
/interface/ethernet/switch/unicast-fdb
add mac-address=E7:16:34:A1:CD:18 port=ether8 qos-group=group1 svl=yes
```

配置 ether8 埠佇列，使其僅針對目的地址按嚴格優先順序和 QoS 方案工作：

```ros
/interface/ethernet/switch/port
set ether8 per-queue-scheduling="strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0" priority-to-queue=0:0,1:1 qos-scheme-precedence=da-based
```

在 ether8 上為 queue1 應用頻寬限制：

```ros
/interface/ethernet/switch/shaper
add port=ether8 rate=10M target=queue1
```

如果 CRS 交換器支援訪問控制列表，則此配置更簡單：

```ros
/interface/ethernet/switch/acl/policer
add name=policer1 yellow-burst=100k yellow-rate=10M

/interface/ethernet/switch/acl
add mac-dst-address=E7:16:34:A1:CD:18 policer=policer1
```

### 使用內部優先順序的基於 VLAN 的流量排程 + 整形 {#vlan-based-traffic-scheduling--shaping-using-internal-priorities}

最佳實踐是為受整形器限制的流量分配較低的內部 QoS 優先順序，從而使其在嚴格優先順序排程程式中也不那麼重要。（較高優先順序應更重要且不受限制）

在此示例中：  
交換器埠 ether6 使用整形器來限制來自 ether7 和 ether8 的流量。  
當鏈路達到容量時，具有最高優先順序的流量將首先發送。  
VLAN10 -> QoS group0 = 最低優先順序  
VLAN20 -> QoS group1 = 正常優先順序  
VLAN30 -> QoS group2 = 最高優先順序

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether6 hw=yes
add bridge=bridge1 interface=ether7 hw=yes
add bridge=bridge1 interface=ether8 hw=yes
```

建立供 VLAN 表使用的 QoS 組。

```ros
/interface/ethernet/switch/qos-group
add name=group0 priority=0
add name=group1 priority=1
add name=group2 priority=2
```

新增 VLAN 條目，為特定 VLAN 應用 QoS 組。

```ros
/interface/ethernet/switch/vlan
add ports=ether6,ether7,ether8 qos-group=group0 vlan-id=10
add ports=ether6,ether7,ether8 qos-group=group1 vlan-id=20
add ports=ether6,ether7,ether8 qos-group=group2 vlan-id=30
```

配置 ether6、ether7 和 ether8 埠佇列，使其僅針對基於 VLAN 的 QoS 按嚴格優先順序和 QoS 方案工作。

```ros
/interface/ethernet/switch/port
set ether6 per-queue-scheduling="strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0" priority-to-queue=0:0,1:1,2:2 qos-scheme-precedence=vlan-based
set ether7 per-queue-scheduling="strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0" priority-to-queue=0:0,1:1,2:2 qos-scheme-precedence=vlan-based
set ether8 per-queue-scheduling="strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0" priority-to-queue=0:0,1:1,2:2 qos-scheme-precedence=vlan-based
```

在 ether6 上應用頻寬限制。

```ros
/interface/ethernet/switch/shaper
add port=ether6 rate=10M
```

### 基於 PCP 的流量排程 {#pcp-based-traffic-scheduling}

預設情況下，CRS1xx/CRS2xx 系列裝置會忽略 PCP/CoS/802.1p 值，並以 FIFO（先進先出）方式轉發封包。當裝置內部佇列未滿時，封包以 FIFO 方式傳送；但一旦某個佇列被填滿，較高優先順序的流量可以先發送。讓我們考慮一個場景：**ether1** 和 **ether2** 正在向 **ether3** 轉發資料，但當 **ether3** 擁塞時，封包將被排程。我們可以配置交換器保留最低優先順序的封包，直到所有更高優先順序的封包都發送完畢。這是 VoIP 型別設定中非常常見的場景，其中某些流量需要優先處理。

要實現這種行為，請將 **ether1**、**ether2,** 和 **ether3** 埠加入同一個交換組：

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether1 hw=yes
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether3 hw=yes
```

為每個埠上的每個內部佇列啟用 **Strict Policy**：

```ros
/interface/ethernet/switch/port
set ether1,ether2,ether3 per-queue-scheduling="strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0"
```

將每個 PCP 值對映到內部優先順序值；為方便起見，只需將 PCP 一對一對映到內部優先順序：

```ros
/interface/ethernet/switch/port
set ether1,ether2,ether3 pcp-based-qos-priority-mapping=0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7
```

由於交換器會先清空最大的佇列，而你需要最高優先順序先得到服務，因此可以將此內部優先順序一對一分配到佇列：

```ros
/interface/ethernet/switch/port
set ether1,ether2,ether3 priority-to-queue=0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7
```

最後，將每個交換器埠設定為根據 PCP 值排程封包：

```ros
/interface/ethernet/switch/port
set ether1,ether2,ether3 qos-scheme-precedence=pcp-based
```

## 頻寬限制 {#bandwidth-limiting}

---

入口埠策略器和整形器都為 CRS 交換器提供頻寬限制功能。

- 入口埠策略器在埠上設定 RX 限制：

```ros
/interface/ethernet/switch/ingress-port-policer
add port=ether5 meter-unit=bit rate=10M
```

- 整形器在埠上設定 TX 限制。

```ros
/interface/ethernet/switch/shaper
add port=ether5 meter-unit=bit rate=10M
```

## 流量風暴控制 {#traffic-storm-control}

---

同一個入口埠策略器還可用於流量風暴控制，以防止廣播、組播或單播流量風暴對二層埠造成中斷。

- 在 ether5 埠上進行廣播風暴控制的示例，限制為每秒 500 個數據包：

```ros
/interface/ethernet/switch/ingress-port-policer
add port=ether5 rate=500 meter-unit=packet packet-types=broadcast  
```

- 包含多種封包型別的示例，其中包括 ARP 和 ND 協定以及未註冊組播流量。未註冊組播是未在組播轉發表中定義的流量。

```ros
/interface/ethernet/switch/ingress-port-policer
add port=ether5 rate=5k meter-unit=packet packet-types=broadcast,arp-or-nd,unregistered-multicast
```

## 另請參閱 {#see-also}

---

- [基本 VLAN 交換](./basic-vlan-switching.md)
- [網橋硬體解除安裝](../index.md#bridge-hardware-offloading)
- [生成樹協定](./spanning-tree-protocol.md)
- [IGMP 偵聽](./bridge-igmp-mld-snooping.md)
- [DHCP 偵聽和 Option 82](../index.md#dhcp-snooping-and-dhcp-option-82)
- [RouterBOARD 上的 MTU](../../hardware/mtu-in-routeros.md)
- [二層錯誤配置](./layer2-misconfiguration.md)
