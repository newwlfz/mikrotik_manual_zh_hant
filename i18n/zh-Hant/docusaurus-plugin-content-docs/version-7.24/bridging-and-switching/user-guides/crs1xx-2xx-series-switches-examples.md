---
title: "CRS1xx/2xx 系列交換器範例"
description: "本頁提供 CRS1xx/2xx 系列交換器上 Cloud Router Switch 功能的設定範例與使用情境，涵蓋埠交換、搭配 VLAN 過濾的管理存取設定，以及以 IP 為基礎的存取安全考量。"
tags:
  - 'vlan'
  - 'bridge-hardware-offloading'
  - 'management-access'
source: https://manual.mikrotik.com/docs/7.24/bridging-and-switching/user-guides/crs1xx-2xx-series-switches-examples
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

---

Cloud Router Switch 功能的基本使用情境與設定範例。

:::info
本文適用於 CRS1xx 與 CRS2xx 系列交換器，不適用於 [MikroTik devices with Marvell Prestera switch](/docs/bridging-and-switching/marvell-prestera-switch-chip-features)（例如 CRS3xx 系列交換器）。
:::

## 埠交換 {#port-switching}

---

若要在 CRS1xx/2xx 系列交換器上設定埠交換，請參閱 [Bridge Hardware Offloading](/docs/bridging-and-switching#bridge-hardware-offloading) 頁面。

:::danger
使用多個已啟用硬體卸載的 bridge 可以建立多個隔離的交換器群組；這僅適用於 CRS1xx/2xx 系列交換器。對於更複雜的設定（例如 VLAN 過濾），應改用埠隔離功能。
:::

## 管理存取設定 {#management-access-configuration}

---

一般而言，交換器應只透過內建交換器晶片轉送封包，但基於安全考量，不應允許存取設備本身。可以使用設備的序列埠進行管理存取，但在大多數情況下，不建議使用這種存取方式，使用 IP 位址存取更為合適。在此類情況下，你需要設定管理存取。

在所有管理存取類型中，都假設埠必須交換在一起。使用下列指令將所需埠交換在一起：

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether3 hw=yes
add bridge=bridge1 interface=ether4 hw=yes
add bridge=bridge1 interface=ether5 hw=yes
```

您也應該為 bridge 介面指派 IP 位址，讓設備可透過 IP 位址連線（設備也可透過 MAC 位址連線）：

```ros
/ip/address
add address=192.168.88.1/24 interface=bridge1
```

### Untagged

若未啟用 invalid VLAN filtering，則從任何埠都已允許使用 tagged 或 untagged（**VLAN 0**）流量管理設備，但這不是良好的做法；這可能造成安全性問題，並在某些情況下導致設備的 CPU 過載（最常見於 broadcast 類型的流量）。

若您打算使用 invalid VLAN filtering（建議這麼做），則必須將您要從中存取交換器的埠加入 VLAN 表，以允許 untagged（**VLAN 0**）流量，例如，若您要從 **ether2** 存取交換器：

```ros
/interface/ethernet/switch/vlan
add vlan-id=0 ports=ether2,switch1-cpu  
```

### Tagged

只允許 tagged 流量透過特定埠管理設備，是更好的做法。例如，若只要允許 **VLAN99** 透過 **ether2** 存取設備，您應先在 VLAN 表中新增項目，讓所選埠與 CPU 埠（**switch1-cpu**）轉送所選 VLAN ID，因此允許管理存取：

```ros
/interface/ethernet/switch/vlan
add ports=ether2,switch1-cpu vlan-id=99
```

從 CPU 送出的封包（例如 ping 回應）不會帶有 VLAN tag，若要解決此問題，您需要指定哪些埠在特定 VLAN ID 下應一律送出帶有 VLAN tag 的封包：

```ros
/interface/ethernet/switch/egress-vlan-tag
add tagged-ports=ether2,switch1-cpu vlan-id=99
```

完成有效的 VLAN99 設定後，您可以啟用 unknown/invalid VLAN filtering，這將不允許透過 VLAN 表中指定以外的其他埠進行管理存取：

```ros
/interface/ethernet/switch
set drop-if-invalid-or-src-port-not-member-of-vlan-on-ports=ether2,ether3,ether4,ether5
```

在此範例中，VLAN99 將用於存取設備。必須在 bridge 上建立 VLAN 介面，並為其指派 IP 位址。

```ros
/interface/vlan
add interface=bridge1 name=MGMT vlan-id=99
/ip/address
add address=192.168.99.1/24 interface=MGMT
```

## VLAN

---

:::danger 鎖定風險
強烈建議在設定 VLAN 前，先準備並測試 Serial Console 纜線。設定錯誤可能輕易讓您無法存取 CPU 或所連接的埠。
:::

:::tip 疑難排解已快取的 MAC 位址
某些變更可能因為已學習到的 MAC 位址而延遲生效。如果變更後流量未如預期流動，請清除 Unicast Forwarding Database：
`/interface/ethernet/switch/unicast-fdb/flush`
:::

:::info 架構最佳實踐
使用多個硬體卸載橋接器是達成簡單埠隔離的快速方式，但會限制 CRS 交換器晶片上進階 VLAN 功能。若是進階設定，請對所有埠使用**單一橋接器**，設定 VLAN，並使用埠隔離設定檔隔離埠群組。
:::

### 以埠為基礎的 VLAN {#port-based-vlan}

:::warning
對於 CRS3xx 系列設備，必須使用 bridge VLAN filtering；你可以在 [Bridge VLAN Filtering](/docs/bridging-and-switching#bridge-vlan-filtering) 一節中閱讀更多相關資訊。
:::

#### 範例 1（Trunk 與 Access 埠） {#example-1-trunk-and-access-ports}

![Access Ports](/img/dcbdce357964f958.webp)

將所需的埠交換在一起：

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether6 hw=yes
add bridge=bridge1 interface=ether7 hw=yes
add bridge=bridge1 interface=ether8 hw=yes
```

指定交換器必須為每個 access 埠在未標記（VLAN0）流量上設定的 VLAN ID：

```ros
/interface/ethernet/switch/ingress-vlan-translation
add ports=ether6 customer-vid=0 new-customer-vid=200
add ports=ether7 customer-vid=0 new-customer-vid=300
add ports=ether8 customer-vid=0 new-customer-vid=400
```

:::warning
在 `/interface/ethernet/switch/ingress-vlan-translation` 下建立項目時，交換器晶片會在指定埠的 ingress 訊框上加入 VLAN 標籤。若要在同一埠上移除 egress 訊框的 VLAN 標籤，應針對相同的 VLAN ID 建立 `/interface/ethernet/switch/egress-vlan-tag` 項目，且其中只指定 tagged 埠。如果特定 VLAN 只在 access 埠之間轉送，仍應建立不含任何 tagged 埠的 `/interface/ethernet/switch/egress-vlan-tag` 項目。另一種做法是在 `/interface/ethernet/switch/egress-vlan-translation` 選單下建立額外項目，以設定未標記（VLAN0）流量。
:::

您也必須指定哪些 VLAN 應以 VLAN 標籤傳送至 trunk 埠。使用 tagged-ports 屬性設定 trunk 埠：

```ros
/interface/ethernet/switch/egress-vlan-tag
add tagged-ports=ether2 vlan-id=200
add tagged-ports=ether2 vlan-id=300
add tagged-ports=ether2 vlan-id=400
```

在 VLAN 表中新增項目，以指定每個埠與每個 VLAN ID 的 VLAN 成員資格：

```ros
/interface/ethernet/switch/vlan
add ports=ether2,ether6 vlan-id=200
add ports=ether2,ether7 vlan-id=300
add ports=ether2,ether8 vlan-id=400
```

設定有效的 VLAN 組態後，即可啟用 unknown/invalid VLAN 過濾：

```ros
/interface/ethernet/switch
set drop-if-invalid-or-src-port-not-member-of-vlan-on-ports=ether2,ether6,ether7,ether8
```

:::warning
可以同時使用內建交換器晶片與 CPU 建立 Switch-Router 架構，其中設備可同時作為交換器與路由器。
:::

#### 範例 2（Trunk 與 Hybrid 埠） {#example-2-trunk-and-hybrid-ports}

![Hybrid Ports](/img/90b987271e134d95.webp)

將所需的埠交換在一起：

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether6 hw=yes
add bridge=bridge1 interface=ether7 hw=yes
add bridge=bridge1 interface=ether8 hw=yes
```

指定交換器必須為每個 access 埠的未標籤（VLAN0）流量設定的 VLAN ID：

```ros
/interface/ethernet/switch/ingress-vlan-translation
add ports=ether6 customer-vid=0 new-customer-vid=200
add ports=ether7 customer-vid=0 new-customer-vid=300
add ports=ether8 customer-vid=0 new-customer-vid=400
```

藉由將埠指定為 tagged-ports，交換器將一律以帶有對應 VLAN ID 的標籤封包傳送封包。根據上圖新增適當的項目：

```ros
/interface/ethernet/switch/egress-vlan-tag
add tagged-ports=ether2,ether7,ether8 vlan-id=200
add tagged-ports=ether2,ether6,ether8 vlan-id=300
add tagged-ports=ether2,ether6,ether7 vlan-id=400
```

在 VLAN 表中新增項目，以指定每個埠與每個 VLAN ID 的 VLAN 成員資格：

```ros
/interface/ethernet/switch/vlan
add ports=ether2,ether6,ether7,ether8 vlan-id=200 learn=yes
add ports=ether2,ether6,ether7,ether8 vlan-id=300 learn=yes
add ports=ether2,ether6,ether7,ether8 vlan-id=400 learn=yes
```

在設定有效的 VLAN 組態後，可以啟用未知／無效 VLAN 過濾：

```ros
/interface/ethernet/switch
set drop-if-invalid-or-src-port-not-member-of-vlan-on-ports=ether2,ether6,ether7,ether8
```

### 以通訊協定為基礎的 VLAN {#protocol-based-vlan}

![Protocol Based VLAN](/img/279b50d6fabcdc21.webp)

將所需的埠交換在一起：

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether6 hw=yes
add bridge=bridge1 interface=ether7 hw=yes
add bridge=bridge1 interface=ether8 hw=yes
```

為 IP 與 ARP 通訊協定設定 VLAN：

```ros
/interface/ethernet/switch/protocol-based-vlan
add port=ether2 protocol=arp set-customer-vid-for=all new-customer-vid=0
add port=ether6 protocol=arp set-customer-vid-for=all new-customer-vid=200
add port=ether2 protocol=ip set-customer-vid-for=all new-customer-vid=0
add port=ether6 protocol=ip set-customer-vid-for=all new-customer-vid=200
```

為 IPX 通訊協定設定 VLAN：

```ros
/interface/ethernet/switch/protocol-based-vlan
add port=ether2 protocol=ipx set-customer-vid-for=all new-customer-vid=0
add port=ether7 protocol=ipx set-customer-vid-for=all new-customer-vid=300
```

為 AppleTalk AARP 與 AppleTalk DDP 通訊協定設定 VLAN：

```ros
/interface/ethernet/switch/protocol-based-vlan
add port=ether2 protocol=0x80F3 set-customer-vid-for=all new-customer-vid=0
add port=ether8 protocol=0x80F3 set-customer-vid-for=all new-customer-vid=400
add port=ether2 protocol=0x809B set-customer-vid-for=all new-customer-vid=0
add port=ether8 protocol=0x809B set-customer-vid-for=all new-customer-vid=400
```

### 以 MAC 為基礎的 VLAN {#mac-based-vlan}

:::danger
在內部，MAC-based VLAN 中的所有 MAC 位址都會經過雜湊。某些 MAC 位址可能有相同的雜湊值，若某個 MAC 位址的雜湊值與已載入至交換器晶片的 MAC 位址雜湊值相符，將導致該 MAC 位址無法載入，因此建議搭配 Port-based VLAN 使用 MAC-based VLAN。這是硬體限制。
:::

![MAC Based VLAN](/img/fb1b49b2f44e71a3.webp)

將所需的埠加入交換器：

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether7 hw=yes
```

在 access 埠上啟用 MAC-based VLAN 轉換：

```ros
/interface/ethernet/switch/port
set ether7 allow-fdb-based-vlan-translate=yes
```

在 MAC-based VLAN 表中新增 MAC-to-VLAN 對應項目：

```ros
/interface/ethernet/switch/mac-based-vlan
add src-mac=A4:12:6D:77:94:43 new-customer-vid=200
add src-mac=84:37:62:DF:04:20 new-customer-vid=300
add src-mac=E7:16:34:A1:CD:18 new-customer-vid=400
```

在 ether2 埠上新增 VLAN200、VLAN300 與 VLAN400 標記，以將其建立為 VLAN trunk 埠：

```ros
/interface/ethernet/switch/egress-vlan-tag
add tagged-ports=ether2 vlan-id=200
add tagged-ports=ether2 vlan-id=300
add tagged-ports=ether2 vlan-id=400
```

此外，在 VLAN 表中新增項目，為每個埠指定 VLAN 成員資格，並啟用 unknown/invalid VLAN 篩選，請參閱以下範例：Unknown/Invalid VLAN filtering。當 bridge 中加入更多介面時，這是必要的網路設定，因為它可讓你定義 VLAN 邊界。

### InterVLAN 路由 {#intervlan-routing}

![VLAN Routing](/img/f659d62947a98802.webp)

InterVLAN routing 設定包含兩個主要部分：交換器晶片中的 VLAN 標記，以及 RouterOS 中的路由。此設定可搭配 DHCP server、Hotspot、PPP 與其他功能，應用於每個 VLAN 的多種情境。

將所需的埠切換在一起：

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether6 hw=yes
add bridge=bridge1 interface=ether7 hw=yes
add bridge=bridge1 interface=ether8 hw=yes
```

設定 CPU 埠上所有 VLAN 的 VLAN 標記，讓封包在路由前先加上標記：

```ros
/interface/ethernet/switch/egress-vlan-tag
add tagged-ports=switch1-cpu vlan-id=200
add tagged-ports=switch1-cpu vlan-id=300
add tagged-ports=switch1-cpu vlan-id=400
```

新增 ingress VLAN 轉換規則，以確保在存取埠上完成正確的 VLAN ID 指派：

```ros
/interface/ethernet/switch/ingress-vlan-translation
add ports=ether6 customer-vid=0 new-customer-vid=200
add ports=ether7 customer-vid=0 new-customer-vid=300
add ports=ether8 customer-vid=0 new-customer-vid=400
```

在 bridge 介面上建立 VLAN 介面：

```ros
/interface/vlan
add name=VLAN200 interface=bridge1 vlan-id=200
add name=VLAN300 interface=bridge1 vlan-id=300
add name=VLAN400 interface=bridge1 vlan-id=400
```

:::danger
請確保 VLAN 介面建立在 bridge 介面上，而不是任何實體介面上。如果 VLAN 介面建立在 slave 介面上，封包可能無法正確接收，因此路由可能會失敗。更多詳細資訊請參閱 [VLAN interface on a slave interface](/docs/bridging-and-switching/user-guides/layer2-misconfiguration#vlan-interface-on-a-slave-interface) 手冊頁面。
:::

在已建立的 VLAN 介面上新增 IP 位址。在此範例中，會將三個 192.168.x.1 位址新增至 VLAN200、VLAN300 與 VLAN400 介面：

```ros
/ip/address
add address=192.168.20.1/24 interface=VLAN200
add address=192.168.30.1/24 interface=VLAN300
add address=192.168.40.1/24 interface=VLAN400
```

### 未知/無效的 VLAN 篩選 {#unknowninvalid-vlan-filtering}

VLAN 成員資格定義於 VLAN 表中。新增具有 VLAN ID 與埠的項目，會讓該 VLAN 流量在這些埠上成為有效流量。設定有效的 VLAN 組態後，即可啟用 unknown/invalid VLAN  filtering。此 VLAN filtering 組態範例適用於 InterVLAN Routing 設定。

```ros
/interface/ethernet/switch/vlan
add ports=switch1-cpu,ether6 vlan-id=200
add ports=switch1-cpu,ether7 vlan-id=300
add ports=switch1-cpu,ether8 vlan-id=400
```

- 選項 1：在特定埠上停用無效 VLAN 轉送（較常見）。

```ros
/interface/ethernet/switch
set drop-if-invalid-or-src-port-not-member-of-vlan-on-ports=ether6,ether7,ether8
```

- 選項 2：在所有埠上停用無效 VLAN 轉送。

```ros
/interface/ethernet/switch
set forward-unknown-vlan=no
```

:::danger
在單一交換器晶片上使用多個 bridge，並啟用 unknown/invalid VLAN filtering，可能導致非預期行為。使用 VLAN filtering 時，應一律使用單一 bridge 設定。如果需要連接埠隔離，應使用連接埠隔離功能，而不是使用多個 bridge。
:::

### VLAN 隧道（Q-in-Q） {#vlan-tunneling-q-in-q}

此範例說明典型的 VLAN 隧道使用情境，服務提供者設備會新增另一個 VLAN tag 以進行獨立轉送，同時允許客戶使用自己的 VLAN。

:::warning
此範例只包含 Service VLAN 標記部分。建議另外在埠上設定 Unknown/Invalid VLAN filtering 組態。
:::

![QinQ](/img/1f0680bc5266cc50.webp)

**CRS-1**：服務提供者網路邊緣的第一台交換器，必須正確識別埠上來自客戶 VLAN ID 的流量，並透過 ingress VLAN translation 規則指派新的服務 VLAN ID。服務提供者 VLAN tag 的 VLAN trunk 埠設定位於同一個 `egress-vlan-tag` 表中。與基本 Port-Based VLAN 設定的主要差異在於，CRS switch-chip 必須設定為根據服務（*outer*）VLAN ID 而非客戶（*inner*）VLAN ID 進行轉送。

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

**CRS-2**：服務提供者網路中的第二台交換器，只需要讓交換埠根據服務（*outer*）VLAN ID 而非客戶（*inner*）VLAN ID 進行轉送。

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether9 hw=yes
add bridge=bridge1 interface=ether10 hw=yes

/interface/ethernet/switch
set bridge-type=service-vid-used-as-lookup-vid
```

**CRS-3**: 第三台交換器的設定與 CRS-1 類似：

- 使用 bridge 將埠加入交換器群組。
- 使用 ingress VLAN 轉換規則，在埠上定義新的服務 VLAN 指派。
- 使用 tagged-ports 作為服務提供者 VLAN trunk。
- 將 CRS switch-chip 設定為在交換查詢中使用服務 VLAN ID。

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

可以使用 CRS1xx/CRS2xx 系列交換器進行 CVID Stacking 設定。CRS1xx/CRS2xx 系列交換器可根據具有兩個 CVID 標籤（double CVID tag）的標記封包外層標籤進行 VLAN 過濾。這些交換器也能在既有 CVID 標籤之上再加入另一個 CVID 標籤（CVID Stacking）。例如，在 **ether1** 接收帶有 CVID 10 的標記封包，但要求 **ether2** 以另一個 CVID 20 標籤送出這些封包（VLAN10 在 VLAN20 內），同時過濾掉其他 VLAN 的設定中，必須完成下列設定：

將 **ether1** 與 **ether2** 交換在一起：

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether1 hw=yes
add bridge=bridge1 interface=ether2 hw=yes
```

設定交換器根據服務標籤（0x88a8）過濾 VLAN：

```ros
/interface/ethernet/switch
set bridge-type=service-vid-used-as-lookup-vid
```

對 **ether1** 上帶有 CVID 10 標籤的封包加入服務標籤 SVID 20：

```ros
/interface/ethernet/switch/ingress-vlan-translation
add customer-vid=10 new-service-vid=20 ports=ether1
```

指定 **ether2** 為 SVID 20 的標記/trunk 埠：

```ros
/interface/ethernet/switch/egress-vlan-tag
add tagged-ports=ether2 vlan-id=20
```

允許 **ether1** 與 **ether2** 轉送 SVID 20：

```ros
/interface/ethernet/switch/vlan
add ports=ether1,ether2 vlan-id=20
```

覆寫 **ether2** 上的 SVID EtherType (0x88a8) 為 CVID EtherType (0x8100)：

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
由於交換器設定為根據 service tag 查閱 VLAN ID，而該 service tag 會被覆寫為不同的 EtherType，因此 VLAN 過濾只會對封包的外層標籤進行；內層標籤不會被檢查。
:::

## Mirroring

---

![Mirroring](/img/7c1963a9e5b62ba0.webp)

Cloud Router Switches 支援三種鏡像類型。以埠為基礎的鏡像可套用於任何 switch-chip 埠；以 VLAN 為基礎的鏡像適用於所有指定的 VLAN，不論其位於哪個 switch-chip 埠；以 MAC 為基礎的鏡像會複製從 Unicast Forwarding Database 中設定之埠可到達的特定設備所傳送或接收的流量。

### 以埠為基礎的鏡像 {#port-based-mirroring}

第一個設定會將 ether5 埠設為 mirror0 分析器埠，用於 ingress 與 egress 鏡像。鏡像流量將會傳送至這個埠。以埠為基礎的 ingress 與 egress 鏡像會從 ether6 埠啟用。

```ros
/interface/ethernet/switch
set ingress-mirror0=ether5 egress-mirror0=ether5

/interface/ethernet/switch/port
set ether6 ingress-mirror-to=mirror0 egress-mirror-to=mirror0
```

### 以 VLAN 為基礎的鏡像 {#vlan-based-mirroring}

第二個範例需要將埠切換為一個群組。鏡像設定會將 ether5 埠設為 mirror0 分析器埠，並設定從 VLAN 進行鏡像時要使用 mirror0 埠。VLAN 表項目只會針對 ether2 與 ether7 埠之間 VLAN 300 的流量啟用鏡像。

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

### 以 MAC 為基礎的鏡像 {#mac-based-mirroring}

第三個設定也需要將埠切換為一個群組。鏡像設定會將 ether5 埠設為 mirror0 分析器埠，並設定從 Unicast Forwarding database 進行鏡像時要使用 mirror0 埠。Unicast Forwarding database 中的項目會針對從 ether8 埠進入、來源或目的 MAC 位址為 E7:16:34:A1:CD:18 的封包啟用鏡像。

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

## Trunking

---

![Trunking 3](/img/601e6a4b07f4a6d0.webp)

Cloud Router Switches 中的 Trunking 提供具有硬體自動容錯移轉與負載平衡的靜態鏈路彙總群組。目前尚不支援與 IEEE802.3ad 和 IEEE802.1ax 相容的 Link Aggregation Control Protocol。最多支援 8 個 Trunk 群組，每個 Trunk 群組最多支援 8 個 Trunk 成員埠。

設定需要一組已切換的埠以及 Trunk 表中的一個項目：

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

此範例也顯示另一端在 RouterOS 中正確的 bonding 設定：

```ros
/interface/bonding
add name=bonding1 slaves=ether2,ether3,ether4 mode=balance-xor transmit-hash-policy=layer-2-and-3
```

:::danger
Bridge (R)STP 不會察覺底層交換器 trunking 設定，且部分 trunk 埠可能會進入 discarding 或 blocking 狀態。當 trunking 成員埠連接到其他橋接器時，您應該停用 (R)STP，或篩選掉 trunked 設備之間的任何 BPDU（例如使用 ACL 規則）。
:::

## 每個埠的有限 MAC 存取 {#limited-mac-access-per-port}

---

停用 MAC 學習並設定靜態 MAC 位址，可控制哪些設備能與 CRS1xx/2xx 交換器通訊，以及透過這些交換器通訊。

設定需要一組交換埠、在這些埠上停用 MAC 學習，以及靜態 FDB 項目：

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

CRS1xx/2xx 交換器也允許每個埠學習一個動態 MAC，以確保無論其 MAC 位址為何，都只連接一部終端使用者設備：

```ros
/interface/ethernet/switch/port
set ether6 learn-limit=1
set ether7 learn-limit=1
```

## Isolation

---

### 埠層級隔離 {#port-level-isolation}

![Port Level Isolation](/img/b0340fbe7ac5c7ee.webp)

埠層級隔離常用於 Private VLAN，其中：

- 一或多個 uplink 埠由所有使用者共用，用於存取閘道器或路由器。
- 埠群組 Isolated Ports 供訪客使用者使用。通訊只能透過 uplink 埠進行。
- 埠群組 Community 0 供部門 A 使用。群組成員之間以及透過 uplink 埠的通訊皆允許。
- 埠群組 Community X 供部門 X 使用。群組成員之間以及透過 uplink 埠的通訊皆允許。

Cloud Router Switches 使用埠層級隔離設定檔來實作 Private VLAN：

- Uplink 埠 – 埠層級隔離設定檔 0
- Isolated 埠 – 埠層級隔離設定檔 1
- Community 0 埠 - 埠層級隔離設定檔 2
- Community X (X \<= 30) 埠 - 埠層級隔離設定檔 X

**此範例需要一組已交換的埠。假設此範例中使用的所有埠都位於同一個交換器群組。**

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

埠隔離設定的第一部分是設定 Uplink 埠，將 ether2 的連接埠設定檔設為 0：

```ros
/interface/ethernet/switch/port
set ether2 isolation-leakage-profile-override=0
```

接著繼續在所有隔離埠上設定隔離設定檔 1，並新增埠隔離設定檔 1 的通訊埠：

```ros
/interface/ethernet/switch/port
set ether5 isolation-leakage-profile-override=1
set ether6 isolation-leakage-profile-override=1

/interface/ethernet/switch/port-isolation
add port-profile=1 ports=ether2 type=dst
```

設定 Community 2 與 Community 3 埠的設定方式類似：

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

### 通訊協定層級隔離 {#protocol-level-isolation}

![Protocol Level Isolation](/img/efafb0531d23c36a.webp)

CRS 交換器上的通訊協定層級隔離可用於增強網路安全性。例如，限制使用者（ether2、ether3、ether4、ether5）之間的 DHCP 流量，並只允許其流向受信任的 DHCP 伺服器埠（ether1），可防範 DHCP 偽造攻擊等安全風險。下列範例說明如何在 CRS 上進行設定。

將所需的埠交換在一起：

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

為所有 DHCP 用戶端埠設定相同的 Community 連接埠設定檔。Community 連接埠設定檔編號為 2 到 30。

```ros
/interface/ethernet/switch/port
set ether2 isolation-leakage-profile-override=2
set ether3 isolation-leakage-profile-override=2
set ether4 isolation-leakage-profile-override=2
set ether5 isolation-leakage-profile-override=2
```

並為選取的 Community (2) 設定連接埠隔離／洩漏設定檔，以允許僅目的地為信任 DHCP 伺服器所在連接埠的 DHCP 流量。Registration status 與 traffic-type 屬性必須設為空，才能僅對 DHCP 通訊協定套用限制。

```ros
/interface/ethernet/switch/port-isolation
add port-profile=2 protocol-type=dhcpv4 type=dst forwarding-type=bridged ports=ether1 registration-status="" traffic-type=""
```

## 服務品質（QoS） {#quality-of-service-qos}

---

**QoS 設定方案**

以 MAC 為基礎的流量排程與整形：[MAC address in UFDB] -> [QoS Group] -> [Priority] -> [Queue] -> [Shaper]

以 VLAN 為基礎的流量排程與整形：[VLAN id in VLAN table] -> [QoS Group] -> [Priority] -> [Queue] -> [Shaper]

以通訊協定為基礎的流量排程與整形：[Protocol in Protocol VLAN table] -> [QoS Group] -> [Priority] -> [Queue] -> [Shaper]

以 PCP/DEI 為基礎的流量排程與整形：[Switch port PCP/DEI mapping] -> [Priority] -> [Queue] -> [Shaper]

以 DSCP 為基礎的流量排程與整形：[QoS DSCP mapping] -> [Priority] -> [Queue] -> [Shaper]

### 使用內部 Priority 進行以 MAC 為基礎的流量排程 {#mac-based-traffic-scheduling-using-internal-priority}

在 Strict Priority 排程模式中，會先處理優先順序最高的佇列。佇列編號代表優先順序，佇列編號最大的佇列具有最高優先順序。流量會從最高優先順序的佇列開始傳送，直到該佇列清空為止，然後移至下一個較高優先順序的佇列，依此類推。如果 egress 埠沒有壅塞，封包會在收到時立即傳送。如果高優先順序流量持續進入的埠發生壅塞，較低優先順序的佇列將會餓死。

在所有 CRS 交換器上，根據內部 Priority 進行以 MAC 為基礎的 egress 流量排程，配置如下：[MAC address] -> [QoS Group] -> [Priority] -> [Queue]；  
在此範例中，host1 (E7:16:34:00:00:01) 與 host2 (E7:16:34:00:00:02) 的傳送流量在埠 ether7 上將具有較高的優先順序 1，其餘主機則具有較低的優先順序 0。請注意，CRS 每個埠最多有 8 個佇列。

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether6 hw=yes
add bridge=bridge1 interface=ether7 hw=yes
add bridge=bridge1 interface=ether8 hw=yes
```

建立要用於 UFDB 的 QoS 群組：

```ros
/interface/ethernet/switch/qos-group
add name=group1 priority=1
```

新增 UFDB 項目，以比對 ether7 上的特定 MAC，並套用 QoS group1：

```ros
/interface/ethernet/switch/unicast-fdb
add mac-address=E7:16:34:00:00:01 port=ether7 qos-group=group1 svl=yes
add mac-address=E7:16:34:00:00:02 port=ether7 qos-group=group1 svl=yes
```

設定 ether7 埠佇列僅針對目的地位址依照 Strict Priority 與 QoS 配置運作：

```ros
/interface/ethernet/switch/port
set ether7 per-queue-scheduling="strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0" priority-to-queue=0:0,1:1 qos-scheme-precedence=da-based
```

### 使用內部 Priority 進行以 MAC 為基礎的流量整形 {#mac-based-traffic-shaping-using-internal-priority}

根據內部 Priority 進行以 MAC 為基礎的流量整形，配置如下：[MAC address] -> [QoS Group] -> [Priority] -> [Queue] -> [Shaper]；  
在此範例中，未受限流量將具有優先順序 0，受限流量將具有優先順序 1，頻寬限制為 10Mbit。請注意，CRS 每個埠最多有 8 個佇列。

建立一組用於交換的埠：

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether6 hw=yes
add bridge=bridge1 interface=ether7 hw=yes
add bridge=bridge1 interface=ether8 hw=yes
```

建立一組 QoS 群組，供 UFDB 使用：

```ros
/interface/ethernet/switch/qos-group
add name=group1 priority=1
```

新增 UFDB 項目，以比對 ether8 上的特定 MAC，並套用 QoS group1：

```ros
/interface/ethernet/switch/unicast-fdb
add mac-address=E7:16:34:A1:CD:18 port=ether8 qos-group=group1 svl=yes
```

設定 ether8 埠佇列，使其僅依據 Strict Priority 與 QoS 配置目的地位址運作：

```ros
/interface/ethernet/switch/port
set ether8 per-queue-scheduling="strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0" priority-to-queue=0:0,1:1 qos-scheme-precedence=da-based
```

為 ether8 上的 queue1 套用頻寬限制：

```ros
/interface/ethernet/switch/shaper
add port=ether8 rate=10M target=queue1
```

如果 CRS 交換器支援 Access Control Lists，則此設定會更簡單：

```ros
/interface/ethernet/switch/acl/policer
add name=policer1 yellow-burst=100k yellow-rate=10M

/interface/ethernet/switch/acl
add mac-dst-address=E7:16:34:A1:CD:18 policer=policer1
```

### 使用內部優先權進行以 VLAN 為基礎的流量排程與整形 {#vlan-based-traffic-scheduling--shaping-using-internal-priorities}

最佳做法是為受 shaper 限制的流量指派較低的內部 QoS Priority，使其在 Strict Priority 排程器中也較不重要。（較高的優先權應代表較重要且不受限制）

在此範例中：  
交換器埠 ether6 使用 shaper 限制來自 ether7 與 ether8 的流量。  
當連結已達到其容量時，將先傳送優先順序最高的流量。  
VLAN10 -> QoS group0 = 最低優先順序  
VLAN20 -> QoS group1 = 一般優先順序  
VLAN30 -> QoS group2 = 最高優先順序

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether6 hw=yes
add bridge=bridge1 interface=ether7 hw=yes
add bridge=bridge1 interface=ether8 hw=yes
```

建立要用於 VLAN 表的 QoS 群組。

```ros
/interface/ethernet/switch/qos-group
add name=group0 priority=0
add name=group1 priority=1
add name=group2 priority=2
```

新增 VLAN 項目，以將 QoS 群組套用至特定 VLAN。

```ros
/interface/ethernet/switch/vlan
add ports=ether6,ether7,ether8 qos-group=group0 vlan-id=10
add ports=ether6,ether7,ether8 qos-group=group1 vlan-id=20
add ports=ether6,ether7,ether8 qos-group=group2 vlan-id=30
```

設定 ether6、ether7 與 ether8 埠佇列，使其僅針對以 VLAN 為基礎的 QoS，依照 Strict Priority 與 QoS 配置運作。

```ros
/interface/ethernet/switch/port
set ether6 per-queue-scheduling="strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0" priority-to-queue=0:0,1:1,2:2 qos-scheme-precedence=vlan-based
set ether7 per-queue-scheduling="strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0" priority-to-queue=0:0,1:1,2:2 qos-scheme-precedence=vlan-based
set ether8 per-queue-scheduling="strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0,strict-priority:0" priority-to-queue=0:0,1:1,2:2 qos-scheme-precedence=vlan-based
```

在 ether6 上套用頻寬限制。

```ros
/interface/ethernet/switch/shaper
add port=ether6 rate=10M
```

### 以 PCP 為基礎的流量排程 {#pcp-based-traffic-scheduling}

預設情況下，CRS1xx/CRS2xx 系列設備會忽略 PCP/CoS/802.1p 值，並以 FIFO（First-In-First-Out）方式轉送封包。當設備的內部佇列未滿時，封包會以 FIFO 方式傳送，但一旦佇列已滿，較高優先順序的流量就可以先傳送。讓我們考慮一個情境：**ether1** 與 **ether2** 正在將資料轉送至 **ether3**，但當 **ether3** 壅塞時，封包就會進行排程。我們可以設定交換器保留最低優先順序的封包，直到所有較高優先順序的封包都已傳送出去。這在 VoIP 類型的設定中是很常見的情境，因為某些流量需要優先處理。

為了達成這樣的行為，請將 **ether1**、**ether2,** 與 **ether3** 埠交換在一起：

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

為了方便起見，將每個 PCP 值對應至內部優先順序值，只需以 1 對 1 的方式將 PCP 對應至內部優先順序：

```ros
/interface/ethernet/switch/port
set ether1,ether2,ether3 pcp-based-qos-priority-mapping=0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7
```

由於交換器會先清空最大的佇列，而你需要最先處理最高優先順序，因此可以以 1 對 1 的方式將此內部優先順序指派給佇列：

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

Ingress Port policer 與 Shaper 都為 CRS 交換器提供頻寬限制功能。

- Ingress Port Policer 會在埠上設定 RX 限制：

```ros
/interface/ethernet/switch/ingress-port-policer
add port=ether5 meter-unit=bit rate=10M
```

- Shaper 會在埠上設定 TX 限制。

```ros
/interface/ethernet/switch/shaper
add port=ether5 meter-unit=bit rate=10M
```

## 流量風暴控制 {#traffic-storm-control}

---

相同的 Ingress Port policer 也可用於流量風暴控制，以避免 broadcast、multicast 或 unicast 流量風暴造成 Layer 2 埠中斷。

- 在 ether5 埠上啟用 broadcast 風暴控制，每秒限制 500 個封包的範例：

```ros
/interface/ethernet/switch/ingress-port-policer
add port=ether5 rate=500 meter-unit=packet packet-types=broadcast  
```

- 包含 ARP 與 ND 通訊協定，以及未註冊 multicast 流量等多種封包類型的範例。未註冊 multicast 是指未在 Multicast Forwarding Database 中定義的流量。

```ros
/interface/ethernet/switch/ingress-port-policer
add port=ether5 rate=5k meter-unit=packet packet-types=broadcast,arp-or-nd,unregistered-multicast
```

## 另請參閱 {#see-also}

---

- [Basic VLAN switching](/docs/bridging-and-switching/user-guides/basic-vlan-switching)
- [Bridge Hardware Offloading](/docs/bridging-and-switching#bridge-hardware-offloading)
- [Spanning Tree Protocol](/docs/bridging-and-switching/user-guides/spanning-tree-protocol)
- [IGMP Snooping](/docs/bridging-and-switching/user-guides/bridge-igmp-mld-snooping)
- [DHCP Snooping and Option 82](/docs/bridging-and-switching#dhcp-snooping-and-dhcp-option-82)
- [MTU on RouterBOARD](/docs/hardware/mtu-in-routeros)
- [Layer2 misconfiguration](/docs/bridging-and-switching/user-guides/layer2-misconfiguration)
