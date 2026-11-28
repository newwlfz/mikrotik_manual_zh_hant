---
title: "Marvell Prestera 交換器晶片功能"
description: "搭載 Marvell Prestera 交換器晶片的 MikroTik 設備提供高效能的 Layer 2 與 Layer 3 功能，包括進階轉送、路由卸載、VLAN 支援、QoS、鏡像，以及用於精確時間同步的 PTP 同步。"
tags:
  - 'crs3xx'
  - 'crs5xx'
  - 'crs4xx'
  - 'crs8xx'
  - 'prestera'
source: https://manual.mikrotik.com/docs/7.24/bridging-and-switching/marvell-prestera-switch-chip-features
captured_at: '2026-11-28T10:19:39.818Z'
pagination_prev: "bridging-and-switching"
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

---

部分 MikroTik 設備使用高效能且功能豐富的 Marvell Prestera Ethernet 交換器。這些設備可設計用於各種 Ethernet 應用，包括非網管交換器、Layer 2 網管交換器、電信業者交換器、VLAN 間路由器，以及有線統一封包處理器。

:::warning
本文僅適用於搭載 Marvell Prestera 交換器的 MikroTik 設備，不適用於 [CRS1xx/CRS2xx 系列交換器](/docs/bridging-and-switching/crs1xx-and-2xx-series-switches)。
:::

### 功能 {#features}

<WideTable>

| 功能 | 說明 |
| :-- | :-- |
| **轉送** | <ul class="bullets"><li>可設定埠用於交換或路由</li><li>完整非阻塞線速交換</li><li>用於 Layer 2 unicast 轉送的大型 Unicast FDB</li><li>Forwarding Databases 依據 IVL 運作</li><li>支援 Jumbo frame</li><li>支援 IGMP/MLD Snooping</li><li>支援 DHCP Snooping，並可使用自訂 Option 82（Circuit ID、Remote ID）</li><li>支援 DHCPv6 Snooping，並可使用自訂 Option 18（Interface ID）與 Option 37（Remote ID）</li><li>支援 RA Guard</li></ul> |
| **路由** | <ul><li>Layer 3 硬體卸載：<ul><li>IPv4、IPv6 Unicast Routing</li><li>支援 Ethernet、Bridge、Bonding 與 VLAN 介面</li><li>ECMP</li><li>Blackholes</li><li>已卸載的 Fasttrack 連線 <sup>1</sup></li><li>已卸載的 Fasttrack 連線 NAT <sup>1</sup></li><li>硬體卸載 VRF <sup>1</sup></li><li>多個 MTU 設定檔</li></ul></li></ul><br/><strong>重要：</strong> 1. 僅適用於<a href="/docs/bridging-and-switching/l3-hardware-offloading#l3hw-device-support">特定交換器型號</a><br/> |
| **Spanning Tree Protocol** | <ul class="bullets"><li>STP</li><li>RSTP</li><li>MSTP</li><li>Edge port、BPDU Guard、Root Guard</li></ul> |
| **鏡像** | <ul class="bullets"><li>多種鏡像類型：<ul class="bullets"><li>以埠為基礎的鏡像</li><li>以 VLAN 為基礎的鏡像</li><li>以 MAC 為基礎的鏡像</li><li>Remote Switch Port Analyzer（RSPAN）</li></ul></li></ul> |
| **VLAN** | <ul class="bullets"><li>與 IEEE802.1Q 及 IEEE802.1ad VLAN 完全相容</li><li>4k 個作用中 VLAN</li><li>彈性 VLAN 指派：<ul class="bullets"><li>以埠為基礎的 VLAN</li><li>以通訊協定為基礎的 VLAN</li><li>以 MAC 為基礎的 VLAN</li></ul></li><li>VLAN 篩選</li><li>Ingress VLAN translation</li><li>Multiple VLAN Registration protocol（MVRP）</li></ul> |
| **Bonding** | <ul class="bullets"><li>支援 802.3ad（LACP）、balance-xor 與 active-backup 模式</li><li>每個 bonding 介面最多 8 個成員埠</li><li>硬體自動容錯移轉與負載平衡</li><li>MLAG</li></ul> |
| **服務品質（QoS）** | <ul class="bullets"><li>每個埠八個輸出佇列</li><li>DSCP 與 802.1p PCP 對應</li><li>以埠為基礎的 Layer2 與 Layer3 trust 設定</li><li>以埠與佇列為基礎的 egress 速率限制器</li><li>透過 ACL 規則實作的以政策為基礎 QoS</li><li>Strict Priority（SP）與 Shaped Deficit Weighted Round Robin（SDWRR）佇列</li><li>Enhanced Transmission Selection（ETS）排程</li><li>Weighted Random Early Detection（WRED） <sup>1</sup></li><li>Explicit Congestion Notification（ECN） <sup>1</sup></li><li>Priority-based Flow Control（PFC） <sup>1</sup></li><li>資源配置控制（以佇列、shared-pool 與 multicast 為基礎），並提供廣泛的監控功能</li><li>相容於 Dante 環境</li><li>相容於 RDMA over Converged Ethernet（RoCE）環境 <sup>1</sup></li><li>Ingress 流量限制（以埠為基礎或透過 ACL 規則）</li><li>流量風暴控制</li></ul><br/><strong>重要：</strong> 1. 僅適用於<a href="/docs/bridging-and-switching/quality-of-service#qos-device-support">特定交換器型號</a><br/> |
| **埠隔離** | <ul class="bullets"><li>適用於 Private VLAN 實作</li></ul> |
| **存取控制清單** | <ul class="bullets"><li>Ingress ACL 表</li><li>依據埠、L2、L3、L4 通訊協定標頭欄位進行分類</li><li>ACL 動作包括篩選、轉送及修改通訊協定標頭欄位</li></ul> |
| **PTP** | <ul class="alternate"><li>Two-step Ordinary Clock 與 Boundary Clock。</li><li>硬體時間戳記，確保奈秒（ns）範圍內的時脈同步。</li><li>IPv4 與 Layer 2（L2）multicast 傳輸模式。</li><li>End-to-End（E2E）與 Peer-to-Peer（P2P）延遲機制。</li><li>IEEE 1588-2008（PTPv2）。</li><li>支援設定檔：<ul><li>802.1AS：Audio Video Bridging（AVB）與 Time-Sensitive Networking（TSN）的計時與同步。</li><li>AES67：高效能 audio-over-IP 互通性。</li><li>G.8275.1：支援 PTP 網路中的頻率與相位同步。</li><li>SMPTE：專業廣播環境中的音訊／影片同步。</li></ul></li></ul><br/><strong>重要：</strong> PTP 支援取決於硬體，請參閱<a href="/docs/system-information-and-utilities/precision-time-protocol#supported-devices">支援設備</a>清單。<br/> |

:::info
如需 L3 硬體卸載功能支援與硬體限制，請參閱 [Feature Support](/docs/bridging-and-switching/l3-hardware-offloading#l3hw-device-support) 使用手冊。
:::

:::note
如需 QoS 硬體卸載功能支援與硬體限制，請參閱 [Quality of Service（QoS）](/docs/bridging-and-switching/quality-of-service) 使用手冊。
:::

</WideTable>

### Models

此表格說明 Cloud Router Switch 型號與 CCR 路由器之間的主要差異。

<WideTable>

|  |  |  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| **型號** | **交換器晶片** | **CPU** | **RAM 大小** | **Ethernet** | **[PoE out](/docs/hardware/poe-out)** | **ACL 規則** | **Unicast FDB 項目** | **Jumbo Frame（Bytes）** |
| **CRS318-1Fi-15Fr-2S-OUT (netPower 15FR)** | Marvell-98DX224S | ARM 2-core 800MHz | 256 MB | 16x 10/100M Ethernet <br/> 2x 1G SFP | 1x passive | 128 | up to 16K | 10218 |
| **CRS318-16P-2S+OUT (netPower 16P)** | Marvell-98DX226S | ARM 2-core 800MHz | 256 MB | 16x 10/100/1000M Ethernet <br/> 2x 10G SFP+ | 16x 802.3af/at | 128 | up to 16K | 10218 |
| **CRS310-1G-5S-4S+ (netFiber 9/IN)** | Marvell-98DX226S | ARM 2-core 800MHz | 256 MB | 1x 10/100/1000M Ethernet <br/> 5x 1G SFP <br/> 4x 10G SFP+ |  | 128 | up to 16K | 10218 |
| **CRS310-8G+2S+IN** | Marvell-98DX226S | ARM 2-core 800MHz | 256 MB | 8x 2.5G Ethernet <br/> 2x 10G SFP+ |  | 128 | up to 16K | 10218 |
| **CRS320-8P-8B-4S+RM** | Marvell-98DX226S | ARM 2-core 800MHz | 256 MB | 16x 10/100/1000M Ethernet <br/> 4x 10G SFP+ | 8x 802.3af/at <br/> 8x 802.3bt | 128 | up to 16K | 10218 |
| **CRS304-4XG-IN** | Marvell-98DX2528 | ARM64 2-core 1200MHz | 512 MB | 4x 1/2.5/5/10G Ethernet |  | 128 | up to 16K | 10218 |
| **CRS326-24G-2S+ (RM/IN)** | Marvell-98DX3236 | ARM 2-core 800MHz | 512 MB | 24x 10/100/1000M Ethernet <br/> 2x 10G SFP+ |  | 128 | up to 16K | 10218 |
| **CRS328-24P-4S+RM** | Marvell-98DX3236 | ARM 1-core 800MHz | 512 MB | 24x 10/100/1000M Ethernet <br/> 4x 10G SFP+ | 24x 802.3af/at | 128 | up to 16K | 10218 |
| **CRS328-4C-20S-4S+RM** | Marvell-98DX3236 | ARM 2-core 800MHz | 512 MB | 20x 1G SFP <br/> 4x 1G combo <br/> 4x 10G SFP+ |  | 128 | up to 16K | 10218 |
| **CRS305-1G-4S+IN** | Marvell-98DX3236 | ARM 2-core 800MHz | 512 MB | 1x 10/100/1000M Ethernet <br/> 4x 10G SFP+ |  | 128 | up to 16K | 10218 |
| **CRS305-1G-4S+OUT (FiberBox Plus)** | Marvell-98DX226S | ARM 2-core 800MHz | 256 MB | 1x 10/100/1000M Ethernet <br/> 4x 10G SFP+ |  | 128 | up to 16K | 10218 |
| **CRS309-1G-8S+IN** | Marvell-98DX8208 | ARM 2-core 800MHz | 512 MB | 1x 10/100/1000M Ethernet <br/> 8x 10G SFP+ |  | 1024 | up to 32K | 10218 |
| **CRS317-1G-16S+RM** | Marvell-98DX8216 | ARM 2-core 800MHz | 1 GB | 1x 10/100/1000M Ethernet <br/> 16x 10G SFP+ |  | 1024 | up to 128K | 10218 |
| **CRS312-4C+8XG-RM** | Marvell-98DX8212 | MIPSBE 1-core 650MHz | 64 MB | 4x 10G combo <br/> 8x 1/2.5/5/10G Ethernet |  | 512 | up to 32K | 10218 |
| **CRS326-24S+2Q+RM** | Marvell-98DX8332 | MIPSBE 1-core 650MHz | 128 MB | 24x 10G SFP+ <br/> 2x 40G QSFP+ |  | 256 | up to 32K | 10218 |
| **CRS326-4C+20G+2Q+RM** | Marvell-98DX8332 | MIPSBE 1-core 650MHz | 128 MB | 4x 2.5G Ethernet/10G SFP+ combo <br/> 20x 2.5G Ethernet <br/> 2x 40G QSFP+ |  | 256 | up to 32K | 10218 |
| **CRS354-48G-4S+2Q+RM** | Marvell-98DX3257 | MIPSBE 1-core 650MHz | 128 MB | 48x 10/100/1000M Ethernet <br/> 4x 10G SFP+ <br/> 2x 40G QSFP+ |  | 170 | up to 32K | 10218 |
| **CRS354-48P-4S+2Q+RM** | Marvell-98DX3257 | MIPSBE 1-core 650MHz | 128 MB | 48x 10/100/1000M Ethernet <br/> 4x 10G SFP+ <br/> 2x 40G QSFP+ | 48x 802.3af/at | 170 | up to 32K | 10218 |
| <strong>CRS418-8P-8G-2S+RM</strong><br/><strong>CRS418-8P-8G-2S+5axQ2axQ-RM</strong> | Marvell-98DX226S | ARM64 4-core 2208MHz | 1 GB | 16x 10/100/1000M Ethernet <br/> 2x 10G SFP+ | 8x 802.3af/at | 128 | up to 16K | 10218 |
| **CRS504-4XQ (IN/OUT)** | Marvell-98DX4310 | MIPSBE 1-core 650MHz | 64 MB | 4x 100G QSFP28 |  | 1024 | up to 128K | 10218 |
| **CRS510-8XS-2XQ-IN** | Marvell-98DX4310 | MIPSBE 1-core 650MHz | 128 MB | 8x 25G SFP28 <br/> 2x 100G QSFP28 |  | 1024 | up to 128K | 10218 |
| **CRS518-16XS-2XQ-RM** | Marvell-98DX8525 | MIPSBE 1-core 650MHz | 64 MB | 16x 25G SFP28 <br/> 2x 100G QSFP28 |  | 1024 | up to 128K | 10218 |
| **CRS520-4XS-16XQ-RM** | Marvell-98CX8410 | ARM64 4-core 2000MHz | 4 GB | 4x 25G SFP28 <br/> 16x 100G QSFP28 |  | 682 | up to 256K | 9570 |
| **CRS812-8DS-2DQ-2DDQ-RM** | Marvell-98DX7335 | ARM64 4-core 2000MHz | 4 GB | 8x 50G SFP56 <br/> 2x 200G QSFP56 <br/> 2x 400G QSFP56-DD |  | 1365 | up to 128K | 9570 |
| **CRS804-4DDQ-hRM** | Marvell-98DX7335 | ARM64 4-core 2000MHz | 4 GB | 4x 400G QSFP56-DD |  | 1365 | up to 128K | 9570 |
| **CCR2116-12G-4S+** | Marvell-98DX3255 | ARM64 16-core 2000MHz | 16 GB | 12x 10/100/1000M Ethernet <br/> 4x 10G SFP+ |  | 512 | up to 32K | 9570 |
| **CCR2216-1G-12XS-2XQ** | Marvell-98DX8525 | ARM64 16-core 2000MHz | 16 GB | 12x 25G SFP28 <br/> 2x 100G QSFP28 |  | 1024 | up to 128K | 9570 |
| **RDS2216-2XG-4S+4XS-2XQ** | Marvell-98DX4310 | ARM64 16-core 2000MHz | 32 GB | 2x 1/2.5/5/10G Ethernet <br/> 4x 10G SFP+ <br/> 4x 25G SFP28 <br/> 2x 100G QSFP28 |  | 1024 | up to 128K | 9570 |

</WideTable>

### Abbreviations

- FDB - 轉送資料庫（Forwarding Database）。
- MDB - 多播資料庫（Multicast Database）。
- SVL - 共用 VLAN 學習（Shared VLAN Learning）。
- IVL - 獨立 VLAN 學習（Independent VLAN Learning）。
- PVID - 埠 VLAN ID（Port VLAN ID）。
- ACL - 存取控制清單（Access Control List）。
- CVID - 客戶 VLAN ID（Customer VLAN ID）。
- SVID - 服務 VLAN ID（Service VLAN ID）。

## 埠交換 {#port-switching}

---

若要設定埠交換，請查看 [Bridge Hardware Offloading](/docs/bridging-and-switching/marvell-prestera-switch-chip-features#bridge-hardware-offloading) 頁面。

:::danger
目前只能建立一個啟用硬體卸載的 bridge。請使用 `hw=yes/no` 參數選擇要啟用硬體卸載的 bridge。
:::

:::warning
Bridge STP/RSTP/MSTP、IGMP Snooping 與 VLAN filtering 設定不會影響硬體卸載。自 RouterOS v6.42 起，Bonding 介面也會進行硬體卸載。
:::

## VLAN

---

自 RouterOS 6.41 版起，bridge 提供 VLAN 感知的 Layer2 轉送，以及 bridge 內的 VLAN 標記修改。這組功能讓 bridge 的運作更接近傳統乙太網路交換器，並可克服與橋接類似隧道的 VLAN 介面組態相比所產生的 Spanning Tree 相容性問題。強烈建議使用 Bridge VLAN Filtering 設定，以符合 STP (802.1D)、RSTP (802.1w) 標準，且在 RouterOS 中啟用 MSTP (802.1s) 支援時為必要設定。

### VLAN 篩選 {#vlan-filtering}

主要 [Bridge VLAN Filtering](/docs/bridging-and-switching/marvell-prestera-switch-chip-features#bridge-vlan-filtering) 章節涵蓋詳細的架構概念與設定步驟。

#### 支援的 VLAN 實作 {#supported-vlan-implementations}

視你的網路設計而定，可以實作多種由硬體卸載的 VLAN 拓撲：

- **Port-Based VLAN：** 請參閱 [Bridge VLAN Filtering](/docs/bridging-and-switching/marvell-prestera-switch-chip-features#bridge-vlan-filtering) 一節中的逐步設定指南。
- **Protocol-Based VLAN：** 透過交換器規則表設定，以對應特定網路通訊協定。
- **MAC-Based VLAN：** 將特定來源 MAC 位址對應至指定的 VLAN ID。

---

### MAC-Based VLAN 設定 {#mac-based-vlan-configuration}

:::warning 硬體與轉送限制

- **規則容量：** 此功能會使用硬體 Switch Rule 表。請參閱 [Switch Chip Model Capacity Table](/docs/bridging-and-switching/marvell-prestera-switch-chip-features#models)，確認你的特定設備支援多少條規則。
- **CPU 轉送限制：** MAC-based VLAN 僅適用於在硬體埠之間交換的流量。若封包被路由或轉送至 CPU，則會強制使用橋接器埠的預設 `pvid`，而不是 ACL 規則中定義的 `new-vlan-id` 動作。
- **DHCP 衝突：** 若橋接器上啟用 `dhcp-snooping=yes`，MAC-based VLAN 比對將無法處理 DHCP 封包。
:::

#### 設定範例 {#configuration-example}

建立啟用 hw-offloading 的橋接器，以在埠上啟用交換功能：

```ros
/interface/bridge
add name=bridge1 vlan-filtering=yes
/interface/bridge/port
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether7 hw=yes
```

在 Bridge VLAN 表中新增 VLAN，並指定埠：

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=ether2 untagged=ether7 vlan-ids=200,300,400
```

新增 Switch 規則，依 MAC 位址指派 VLAN id：

```ros
/interface/ethernet/switch/rule
add switch=switch1 ports=ether7 src-mac-address=A4:12:6D:77:94:43/FF:FF:FF:FF:FF:FF new-vlan-id=200
add switch=switch1 ports=ether7 src-mac-address=84:37:62:DF:04:20/FF:FF:FF:FF:FF:FF new-vlan-id=300
add switch=switch1 ports=ether7 src-mac-address=E7:16:34:A1:CD:18/FF:FF:FF:FF:FF:FF new-vlan-id=400
```

#### 以通訊協定為基礎的 VLAN {#protocol-based-vlan}

:::warning

- Switch Rule 表用於 Protocol Based VLAN 功能，請參閱[此表](/docs/bridging-and-switching/marvell-prestera-switch-chip-features#models)，瞭解每個設備支援多少規則。
- Protocol-based VLAN 僅能在交換器埠之間正常運作，無法在交換器埠與 CPU 之間運作。封包轉送至 CPU 時，將一律使用 bridge 埠的 `pvid` 屬性，而非 ACL 規則中的 `new-vlan-id`。
- 啟用 DHCP snooping 時，Protocol-based VLAN 不適用於 DHCP 封包。
:::

透過建立啟用 hw-offloading 的 bridge，在埠上啟用交換功能：

```ros
/interface/bridge
add name=bridge1 vlan-filtering=yes
/interface/bridge/port
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether6 hw=yes
add bridge=bridge1 interface=ether7 hw=yes
add bridge=bridge1 interface=ether8 hw=yes
```

在 Bridge VLAN 表中新增 VLAN，並指定埠：

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=ether2 untagged=ether6 vlan-ids=200
add bridge=bridge1 tagged=ether2 untagged=ether7 vlan-ids=300
add bridge=bridge1 tagged=ether2 untagged=ether8 vlan-ids=400
```

新增 Switch 規則，依 MAC protocol 指派 VLAN ID：

```ros
/interface/ethernet/switch/rule
add mac-protocol=ip new-vlan-id=200 ports=ether6 switch=switch1
add mac-protocol=ipx new-vlan-id=300 ports=ether7 switch=switch1
add mac-protocol=0x80F3 new-vlan-id=400 ports=ether8 switch=switch1
```

#### VLAN 隧道（Q-in-Q） {#vlan-tunneling-q-in-q}

自 RouterOS v6.43 起，可以同時使用 provider bridge（IEEE 802.1ad）、Tag Stacking VLAN filtering 與硬體卸載。設定方式請參閱 [Bridge VLAN Tunneling (Q-in-Q)](/docs/bridging-and-switching/vlan#q-in-q) 章節。

:::danger
搭載 Marvell-98DX3257 交換器晶片的設備（例如 CRS354 系列）不支援在 1Gbps Ethernet 介面上對其他 VLAN 類型（`0x88a8` 與 `0x9100`）進行 VLAN 過濾。
:::

### 入口 VLAN 轉換 {#ingress-vlan-translation}

可以使用 ACL 規則在 ingress 埠上將特定 VLAN ID 轉換為不同的 VLAN ID。在此範例中，我們建立兩條 ACL 規則，以允許雙向通訊。請依照下列方式完成。

建立新的 bridge，並以硬體卸載方式將埠加入其中：

```ros
/interface/bridge
add name=bridge1 vlan-filtering=no
/interface/bridge/port
add interface=ether1 bridge=bridge1 hw=yes
add interface=ether2 bridge=bridge1 hw=yes
```

新增 ACL 規則，以在每個方向轉換 VLAN ID：

```ros
/interface/ethernet/switch/rule
add new-dst-ports=ether2 new-vlan-id=20 ports=ether1 switch=switch1 vlan-id=10
add new-dst-ports=ether1 new-vlan-id=10 ports=ether2 switch=switch1 vlan-id=20
```

將兩個 VLAN ID 加入 bridge VLAN 表：

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=ether1 vlan-ids=10
add bridge=bridge1 tagged=ether2 vlan-ids=20
```

啟用 bridge VLAN 過濾：

```ros
/interface/bridge/set bridge1 vlan-filtering=yes
```

:::warning
雙向通訊僅限於兩個交換器埠之間。在更多埠之間轉換 VLAN ID 可能會造成流量氾濫，或在相同 VLAN 的埠之間發生不正確的轉送。

**注意：** 啟用 `vlan-filtering` 時，將會過濾掉目的地為 CPU 的流量。啟用 VLAN 過濾前，請確認你已設定 [Management port](/docs/bridging-and-switching/marvell-prestera-switch-chip-features#management-access-configuration)。
:::

## (R/M)STP

---

搭載 Marvell Prestera 交換器的 MikroTik 設備可在硬體層級執行 STP、RSTP 與 MSTP。如需更詳細的資訊，請參閱 [Spanning Tree Protocol](/docs/bridging-and-switching/user-guides/spanning-tree-protocol) 手冊頁面；如需相關設定／監控選項，請參閱 [Bridging and Switching](/docs/bridging-and-switching) 頁面。

## Bonding

---

搭載 Marvell Prestera 交換器的 MikroTik 設備支援 bonding 介面的硬體卸載。只有 `802.3ad` (LACP)、`balance-xor` (static LAG) 與 `active-backup` bonding 模式會進行硬體卸載；其他 bonding 模式會使用 CPU 資源。你可以在 [Bonding Interface](/docs/high-availability-solutions/bonding) 章節找到 bonding 介面的更多資訊。

若要建立硬體卸載的 bonding 介面，必須使用支援的 bonding 模式建立 bonding 介面：

```ros
/interface/bonding
add mode=802.3ad name=bond1 slaves=ether1,ether2
```

此介面可以與其他介面一起加入 bridge：

```ros
/interface/bridge
add name=bridge
/interface/bridge/port
add bridge=bridge interface=bond1 hw=yes
add bridge=bridge interface=ether3 hw=yes
add bridge=bridge interface=ether4 hw=yes
```

:::warning
請勿將已經在 bond 中的介面加入 bridge，RouterOS 不允許你將已經是 bonding slave port 的介面加入 bridge。
:::

請檢查「H」旗標，確認 bonding 介面已進行硬體卸載：

```text
/interface/bridge/port/print 
Flags: X - disabled, I - inactive, D - dynamic, H - hw-offload 
 #     INTERFACE                                 BRIDGE                                 HW
 0   H bond1                                     bridge                                 yes
 1   H ether3                                    bridge                                 yes
 2   H ether4                                    bridge                                 yes
```

:::warning
使用硬體卸載的 bonding 介面時，內建交換器晶片一律會使用 Layer2+Layer3+Layer4 作為 transmit hash policy；手動變更 transmit hash policy 不會生效。
:::

### 設定範例 - 使用 Bond 的 VLAN {#configuration-example---vlans-with-bonds}

本節將說明如何設定多部交換器使用 bonding 介面與連接埠型 VLAN，並展示一個包含 DHCP-Server、VLAN 間路由、管理 IP 及無效 VLAN 過濾設定的可行範例。

在此網路拓撲中，我們將使用兩部 CRS326-24G-2S+、一部 CRS317-1G-16S+ 及一部 CCR1072-1G-8S+。

![CRS3xx VLANs with Bonds](/img/4664a0d68abb9987.webp)

在此設定中，SwitchA 與 SwitchC 會將來自 ether1-ether8 連接埠的所有流量標記為 VLAN ID 10，將 ether9-ether16 標記為 VLAN ID 20，並將 ether17-ether24 標記為 VLAN ID 30。只有當使用者從 SwitchA 或 SwitchB 的 ether1 以 VLAN ID 99 的標記流量連線時，才能進行管理。也可以從路由器使用 VLAN ID 99 的標記流量連線到所有設備。此設定中的 SFP+ 連接埠將作為 VLAN trunk 連接埠，同時加入 bond 以建立 LAG 介面。

#### 設定 Bonding {#configure-bonding}

當需要更大的頻寬時，會使用 bonding 介面。作法是建立 link aggregation group，這也為交換器提供硬體自動容錯移轉與負載平衡。透過將兩個 10Gbps 介面加入 bonding，可以將理論頻寬上限提高到 20Gbps。請確認所有 bonded 介面都以相同的速度連線。

:::info
使用硬體卸載 bridge 時，交換器會使用內建 switch chip 彙總流量，而不會使用 CPU 資源。
:::

若要從 sfp-sfpplus1 與 sfp-sfpplus2 建立 SwitchA 與 SwitchB 之間，以及 SwitchC 與 SwitchB 之間的 20Gbps bonding 介面，請在 **SwitchA** 與 **SwitchC** 上使用以下指令：

```ros
/interface/bonding
add mode=802.3ad name=bond_1-2 slaves=sfp-sfpplus1,sfp-sfpplus2
```

若要在 SwitchB 與 Router 之間建立 40Gbps bonding 介面，並在 SwitchA 與 SwitchC 之間建立 20Gbps bonding 介面，請在 **SwitchB** 上使用下列指令：

```ros
/interface/bonding
add mode=802.3ad name=bond_1-2 slaves=sfp-sfpplus1,sfp-sfpplus2
add mode=802.3ad name=bond_3-4 slaves=sfp-sfpplus3,sfp-sfpplus4
add mode=802.3ad name=bond_5-6-7-8 slaves=sfp-sfpplus5,sfp-sfpplus6,sfp-sfpplus7,sfp-sfpplus8
```

在我們的案例中，Router 需要以軟體為基礎的 bonding 介面。請在 **Router** 上使用下列指令：

```ros
/interface/bonding
add mode=802.3ad name=bond_1-2-3-4 slaves=sfp-sfpplus1,sfp-sfpplus2,sfp-sfpplus3,sfp-sfpplus4
```

:::info
介面 bonding 不會建立具有更大鏈路速度的介面。介面 bonding 會建立一個虛擬介面，可將流量負載平衡到多個介面。更多詳細資訊請參閱 [LAG 介面與負載平衡](/docs/bridging-and-switching/user-guides/layer2-misconfiguration#lag-interfaces-and-load-balancing) 頁面。
:::

#### 設定埠交換 {#configure-port-switching}

此設定中的所有交換器都需要將所有使用的埠交換在一起。對於 bonding，請將 bonding 介面新增為 bridge 埠，而不是個別的 bonding 埠。請在 **SwitchA** 與 **SwitchC** 上使用下列指令：

```ros
/interface/bridge
add name=bridge vlan-filtering=no
/interface/bridge/port
add bridge=bridge interface=ether1 pvid=10
add bridge=bridge interface=ether2 pvid=10
add bridge=bridge interface=ether3 pvid=10
add bridge=bridge interface=ether4 pvid=10
add bridge=bridge interface=ether5 pvid=10
add bridge=bridge interface=ether6 pvid=10
add bridge=bridge interface=ether7 pvid=10
add bridge=bridge interface=ether8 pvid=10
add bridge=bridge interface=ether9 pvid=20
add bridge=bridge interface=ether10 pvid=20
add bridge=bridge interface=ether11 pvid=20
add bridge=bridge interface=ether12 pvid=20
add bridge=bridge interface=ether13 pvid=20
add bridge=bridge interface=ether14 pvid=20
add bridge=bridge interface=ether15 pvid=20
add bridge=bridge interface=ether16 pvid=20
add bridge=bridge interface=ether17 pvid=30
add bridge=bridge interface=ether18 pvid=30
add bridge=bridge interface=ether19 pvid=30
add bridge=bridge interface=ether20 pvid=30
add bridge=bridge interface=ether21 pvid=30
add bridge=bridge interface=ether22 pvid=30
add bridge=bridge interface=ether23 pvid=30
add bridge=bridge interface=ether24 pvid=30
add bridge=bridge interface=bond_1-2
```

請在 **SwitchB** 上使用下列指令，將所有 bonding 介面新增到單一 bridge：

```ros
/interface/bridge
add name=bridge vlan-filtering=no
/interface/bridge/port
add bridge=bridge interface=bond_1-2
add bridge=bridge interface=bond_3-4
add bridge=bridge interface=bond_5-6-7-8
```

#### 設定管理 IP {#configure-management-ip}

建立管理介面並為其指派 IP 位址非常有用，可保留對交換器的存取。這在更新交換器時也非常有用，因為啟用無效的 VLAN 篩選時，此類前往交換器的流量將會被封鎖。

在 **SwitchA**、**SwitchB** 與 **SwitchC** 上建立可路由的 VLAN 介面：

```ros
/interface/vlan
add interface=bridge name=MGMT vlan-id=99
```

Router 需要在 bonding 介面上建立可路由的 VLAN 介面。使用下列指令在 **Router** 上建立 VLAN 介面：

```ros
/interface/vlan
add interface=bond_1-2-3-4 name=MGMT vlan-id=99
```

在本指南中，我們將為每部設備使用下列位址：

| 設備 | 位址 |
| :-- | :-- |
| Router | 192.168.99.1 |
| SwitchA | 192.168.99.2 |
| SwitchB | 192.168.99.3 |
| SwitchC | 192.168.99.4 |

在每部交換器的 VLAN 介面上新增 IP 位址（將 X 變更為適當的數字）：

```ros
/ip/address
add address=192.168.99.X/24 interface=MGMT
```

別忘了在交換器設備上新增預設閘道並指定 DNS 伺服器：

```ros
/ip/route
add gateway=192.168.99.1
/ip/dns
set servers=192.168.99.1
```

在 **Router** 上新增 IP 位址：

```ros
/ip/address
add address=192.168.99.1/24 interface=MGMT
```

#### 設定無效的 VLAN 過濾 {#configure-invalid-vlan-filtering}

由於 SwitchA 與 SwitchC 上的大部分埠都將作為 access 埠，你可以設定所有埠只接受特定類型的封包。在此例中，我們希望 SwitchA 與 SwitchC 只接受未標記的封包。在 **SwitchA** 與 **SwitchC** 上使用這些指令：

```ros
/interface/bridge/port
set [ find ] frame-types=admit-only-untagged-and-priority-tagged
```

SwitchA 與 SwitchC 上的訊框類型有一個例外。在此設定中，需要從 ether1 與 bonding 介面存取管理功能。它們需要能夠轉送已標記的流量。在 **SwitchA** 與 **SwitchC** 上使用這些指令：

```ros
/interface/bridge/port
set [find where interface=ether1] frame-types=admit-all
set [find where interface=bond_1-2] frame-types=admit-only-vlan-tagged
```

在 SwitchB 上只應轉送已標記的封包，在 **SwitchB** 上使用這些指令：

```ros
/interface/bridge/port
set [ find ] frame-types=admit-only-vlan-tagged
```

一個選擇性步驟是在 bridge 介面上設定 `frame-types=admit-only-vlan-tagged`，以停用預設的未標記 VLAN 1（`pvid=1`）。我們使用 bridge 上已標記的 VLAN 進行管理存取，因此不需要在 bridge 上接受未標記的流量。在 **SwitchA**、**SwitchB** 與 **SwitchC** 上使用這些指令：

```ros
/interface/bridge/set [find name=bridge] frame-types=admit-only-vlan-tagged
```

必須設定 bridge VLAN 表。在此網路設定中，我們需要允許 VLAN 10 通過 ether1-ether8、VLAN 20 通過 ether9-ether16、VLAN 30 通過 ether17-ether24、VLAN 10,20,30,99 通過 bond\_1-2，並且針對 ether1 設定特殊情況，以允許在 SwitchA 與 SwitchC 上轉送 VLAN 99。在 **SwitchA** 與 **SwitchC** 上使用這些指令：

```ros
/interface/bridge/vlan
add bridge=bridge tagged=bond_1-2 vlan-ids=10
add bridge=bridge tagged=bond_1-2 vlan-ids=20
add bridge=bridge tagged=bond_1-2 vlan-ids=30
add bridge=bridge tagged=bridge,bond_1-2,ether1 vlan-ids=99
```

:::warning
`frame-types` 設為 `admit-all` 或 `admit-only-untagged-and-priority-tagged` 的 bridge 埠，會自動新增為 `pvid` VLAN 的未標記埠。
:::

同樣地，必須為 SwitchB 設定 bridge VLAN 表。在 **SwitchB** 上使用這些指令：

```ros
/interface/bridge/vlan
add bridge=bridge tagged=bond_1-2,bond_3-4,bond_5-6-7-8 vlan-ids=10,20,30
add bridge=bridge tagged=bond_1-2,bond_3-4,bond_5-6-7-8,bridge vlan-ids=99
```

當所有設定完成後，即可啟用 VLAN 過濾。在 **SwitchA**、**SwitchB,** 與 **SwitchC** 上使用這些指令：

```ros
/interface/bridge
set bridge vlan-filtering=yes
```

:::danger
請再次確認以埠為基礎的 VLAN 是否設定正確。如果發生錯誤，您可能會失去對交換器的存取，而只能透過重設設定或使用序列主控台來恢復連線。
:::

:::note
VLAN 過濾在 [Bridge VLAN Filtering](/docs/bridging-and-switching/marvell-prestera-switch-chip-features#bridge-vlan-filtering) 一節中有更詳細的說明。
:::

#### 設定 InterVLAN 路由 {#configure-intervlan-routing}

若要建立 InterVLAN 路由，必須在路由器上為每個客戶 VLAN ID 建立 VLAN 介面，並為其指派 IP 位址。VLAN 介面必須建立在先前建立的 bonding 介面上。

在 **Router** 上使用下列指令：

```ros
/interface/vlan
add interface=bond_1-2-3-4 name=VLAN10 vlan-id=10
add interface=bond_1-2-3-4 name=VLAN20 vlan-id=20
add interface=bond_1-2-3-4 name=VLAN30 vlan-id=30
/ip/address
add address=192.168.10.1/24 interface=VLAN10
add address=192.168.20.1/24 interface=VLAN20
add address=192.168.30.1/24 interface=VLAN30
```

:::info
這些指令是 DHCP Server 設定所需的。如果不需要 VLAN 間路由，但需要在單一路由器上執行 DHCP Server，請使用 [Firewall Filter](/docs/firewall-and-quality-of-service/firewall/filter) 規則封鎖不同子網路之間的通訊。
:::

:::note
自 RouterOS v7 起，可以在支援的硬體上使用 L3 HW offloading 路由流量。詳情請參閱 [L3 Hardware Offloading](/docs/bridging-and-switching/l3-hardware-offloading) 一節。
:::

#### 設定 DHCP 伺服器 {#configure-dhcp-server}

若要讓 DHCP-Server 對每個 VLAN ID 運作，必須在先前建立的 VLAN 介面上設定伺服器（每個 VLAN ID 一個伺服器）。最好讓每個 VLAN ID 都有自己的子網路與自己的 IP 集區。DNS Server 可以指定為特定 VLAN ID 的路由器 IP 位址，也可以使用全域 DNS Server，但該位址必須可連達。

若要設定 DHCP-Server，請在 **Router** 上使用下列指令：

```ros
/ip/pool
add name=VLAN10_POOL ranges=192.168.10.100-192.168.10.200
add name=VLAN20_POOL ranges=192.168.20.100-192.168.20.200
add name=VLAN30_POOL ranges=192.168.30.100-192.168.30.200
/ip/dhcp-server
add address-pool=VLAN10_POOL disabled=no interface=VLAN10 name=VLAN10_DHCP
add address-pool=VLAN20_POOL disabled=no interface=VLAN20 name=VLAN20_DHCP
add address-pool=VLAN30_POOL disabled=no interface=VLAN30 name=VLAN30_DHCP
/ip/dhcp-server/network
add address=192.168.10.0/24 dns-server=192.168.10.1 gateway=192.168.10.1
add address=192.168.20.0/24 dns-server=192.168.20.1 gateway=192.168.20.1
add address=192.168.30.0/24 dns-server=192.168.30.1 gateway=192.168.30.1
```

若使用路由器的 DNS Server，請勿忘記允許遠端要求，並確認路由器上已設定 DNS Server。請在 **Router** 上使用下列指令：

```ros
/ip/dns
set allow-remote-requests=yes servers=8.8.8.8
```

:::danger
當 `allow-remote-requests` 設為 `yes` 時，請務必使用 Firewall 保護本機 DNS Server 不受外部存取，因為若任何人都能從 Internet 存取您的 DNS Server，該伺服器可能被用於 DDoS 攻擊。
:::

請勿忘記建立 NAT，假設 sfp-sfpplus8 用作 WAN 埠，請在 **Router** 上使用下列指令：

```ros
/ip/firewall/nat
add action=masquerade chain=srcnat out-interface=sfp-sfpplus8
```

#### 設定巨型訊框 {#configure-jumbo-frames}

在此類設定中，可透過啟用巨型訊框來提高總吞吐量。這會透過增加最大傳輸單位（MTU）來降低封包額外負擔。若網路中的設備不支援巨型訊框，就不會從較大的 MTU 獲益。通常整個網路並不支援巨型訊框，但在支援巨型訊框的設備之間傳送資料時仍可獲益，包括路徑中的所有交換器。

在此例中，若 SwitchA 後方的用戶端與 SwitchC 後方的用戶端支援巨型訊框，則啟用巨型訊框將會有利。在啟用巨型訊框之前，請使用下列指令判斷 MAX-L2MTU：

```ros
[admin@SwitchA] > interface print 
Flags: R - RUNNING
Columns: NAME, TYPE, ACTUAL-MTU, L2MTU, MAX-L2MTU, MAC-ADDRESS
 #   NAME           TYPE   ACTUAL-MTU  L2MTU  MAX-L2MTU  MAC-ADDRESS      
 1 R sfp-sfpplus1   ether        1500   1584      10218  64:D1:54:FF:E3:7F

```

:::info
更多資訊請參閱 [MTU 手冊](/docs/hardware/mtu-in-routeros) 頁面。
:::

判斷 MAX-L2MTU 後，請依據網路中的流量選擇 MTU 大小，並在 **SwitchA**、**SwitchB,** 與 **SwitchC** 上使用此指令：

```ros
/interface/ethernet
set [ find ] l2mtu=10218 mtu=10218
```

:::info
別忘了也變更用戶端設備上的 MTU，否則上述設定不會生效。
:::

## 多機箱鏈路聚合群組 {#multi-chassis-link-aggregation-group}

---

RouterOS 中的 MLAG (Multi-chassis Link Aggregation Group) 實作可讓你在兩台不同的設備上設定 LACP bond，而用戶端設備會認為其連接到同一台機器。這可在交換器故障時提供實體備援。搭載 Marvell Prestera 交換器的 MikroTik 設備可設定為硬體卸載 MLAG。請閱讀[此處](/docs/high-availability-solutions/multi-chassis-link-aggregation-group)以取得更多資訊。

## L3 硬體卸載 {#l3-hardware-offloading}

---

Layer3 硬體卸載（也稱為 IP switching 或 HW routing）可讓部分路由器功能卸載到交換器晶片上。這使得路由封包時能達到線速，而這僅靠 CPU 是無法達成的。

可卸載的功能集取決於所使用的晶片組。請閱讀[此處](/docs/bridging-and-switching/l3-hardware-offloading)以取得更多資訊。

## 埠隔離 {#port-isolation}

---

自 RouterOS v6.43 起，可以建立 Private VLAN 設定，範例請參閱 [Switch chip port isolation](/docs/bridging-and-switching/switch-chip-features#port-isolation) 手冊頁面。硬體卸載的 bonding 介面不會包含在 switch port-isolation 選單中，但仍可在 bonding 的每個 secondary 介面上個別設定 port-isolation。

:::warning
埠隔離可與啟用 vlan-filtering 的 bridge 搭配使用，並可隔離屬於同一 VLAN 的埠。隔離是以埠為單位運作，無法以 VLAN 為單位隔離埠。
:::

## IGMP/MLD Snooping

---

配備 Marvell Prestera 交換器晶片的 MikroTik 設備可在硬體層級使用 IGMP/MLD Snooping。若要查看更詳細的資訊，請參閱 [IGMP/MLD snooping](/docs/bridging-and-switching/user-guides/bridge-igmp-mld-snooping) 手冊頁面。

## DHCP Snooping 與 DHCP Option 82 {#dhcp-snooping-and-dhcp-option-82}

---

配備 Marvell Prestera 交換器晶片的 MikroTik 設備可在硬體層級使用 DHCP Snooping，並搭配自訂 Option 82（Circuit ID、Remote ID）。交換器會建立動態 ACL 規則，以擷取 DHCP 封包並將其重新導向至主 CPU 進行後續處理。若要查看更詳細的資訊，請參閱 [DHCP Snooping and DHCP Option 82](/docs/bridging-and-switching/marvell-prestera-switch-chip-features#dhcp-snooping-and-dhcp-option-82) 手冊頁面。

:::info
自 RouterOS v7.17 起，DHCP snooping 支援硬體卸載的 bonding 介面。
:::

## DHCPv6 Snooping 與 DHCP Option 18、Option 37 {#dhcpv6-snooping-and-dhcp-option-18-option-37}

---

自 RouterOS v7.23 起，搭載 Marvell Prestera 交換器晶片的 MikroTik 設備可在硬體層級使用 DHCPv6 Snooping，並搭配自訂 Option 18（Interface ID）與 Option 37（Remote ID）。交換器會建立動態 ACL 規則，以擷取 DHCPv6 封包並將其重新導向至主 CPU 進行後續處理。如需更詳細的資訊，請參閱 [DHCPv6 Snooping / DHCPv6 Shield](/docs/bridging-and-switching#dhcpv6-snooping--dhcpv6-shield) 手冊頁面。

## RA Guard

---

自 RouterOS v7.22 起，搭載 Marvell Prestera 交換器晶片的 MikroTik 設備可在硬體層級使用 RA Guard。交換器會建立動態 ACL 規則，以擷取相關 IPv6 封包並將其重新導向至主 CPU 進行後續處理。如需更詳細的資訊，請參閱 [RA Guard](/docs/bridging-and-switching#ra-guard) 手冊頁面。

## Mirroring

---

Mirroring 是一項功能，可讓網路交換器複製通過它的所有資料，並將副本傳送至另一個指定的埠，即 `mirror-target`。這項功能適用於設定 tap 設備，讓你可以使用另一台設備分析網路流量。你可以透過指定來源埠來簡單設定 mirroring（請參閱 `/interface/ethernet/switch/port` 中的 `mirror-egress` 與 `mirror-ingress`），也可以依據不同條件設定更進階的 mirroring（請參閱 `/interface/ethernet/switch/rule` 中的 `mirror`）。

請注意，`mirror-target` 埠必須位於同一台交換器上。你可以檢查設備的區塊圖，或前往 `/interface/ethernet` 選單，以識別哪些介面連接到哪裡。設定組態時，並不強制要求將 `mirror-target` 介面加入與來源埠相同的硬體卸載橋接器。`mirror-target` 埠可以是獨立介面（未設定為橋接器埠），也可以位於橋接器組態中。搭配橋接器使用 `mirror-target` 時，請注意資料與鏡像流量可能會在同一個 LAN 上傳輸。在此情況下，請考慮採用 RSPAN（Remote Switch Port Analyzer），在將鏡像流量透過網路傳送前，先將其封裝至獨立的 VLAN。

此外，你可以將 `mirror-target` 埠設為特殊值「cpu」，這表示複製的封包將會傳送至交換器晶片的 CPU 埠。

### 設定範例 {#configuration-examples}

---

#### 以埠為基礎的鏡像 {#port-based-mirroring}

從 RouterOS 7.15 版開始，可以設定多個來源埠，並選擇要鏡像傳入流量、傳出流量或兩者。在此範例中，來自 **ether2** 介面的傳入與傳出流量都會被複製並傳送至 **ether3** 介面，以進行監控或分析。

```ros
# Since RouterOS v7.15
/interface/ethernet/switch/port
set ether2 mirror-egress=yes mirror-ingress=yes
/interface/ethernet/switch
set switch1 mirror-target=ether3

# Older RouterOS:
/interface/ethernet/switch
set switch1 mirror-source=ether2 mirror-target=ether3
```

#### 以 VLAN 為基礎的鏡像 {#vlan-based-mirroring}

使用 ACL 規則時，可以透過 `ports` 設定從多個介面鏡像封包。此外，你也可以指定更詳細的條件，例如 VLAN ID、MAC/IP 位址或 TCP/UDP 埠。只有 **ingress** 封包會被鏡像至 `mirror-target` 介面。此範例會鏡像來自 **ether2** 介面的傳入 VLAN 11 流量，並將複本傳送至 **ether3** 介面。若要使用具有 `vlan-id` 比對條件的 ACL 規則，你需要啟用 [bridge vlan-filtering](/docs/bridging-and-switching/marvell-prestera-switch-chip-features#bridge-vlan-filtering)。

```ros
/interface/bridge
set bridge1 vlan-filtering=yes
/interface/ethernet/switch
set switch1 mirror-target=ether3
/interface/ethernet/switch/rule
add mirror=yes ports=ether1 switch=switch1 vlan-id=11
```

#### 以 MAC 為基礎的鏡像 {#mac-based-mirroring}

此範例會鏡像來自 **ether1** 介面，且目的或來源 MAC 位址為 64:D1:54:D9:27:E6 的傳入流量，並將複本傳送至 **ether3** 介面。

```ros
/interface/ethernet/switch
set switch1 mirror-target=ether3
/interface/ethernet/switch/rule
add mirror=yes ports=ether1 switch=switch1 dst-mac-address=64:D1:54:D9:27:E6/FF:FF:FF:FF:FF:FF
add mirror=yes ports=ether1 switch=switch1 src-mac-address=64:D1:54:D9:27:E6/FF:FF:FF:FF:FF:FF
```

#### 以 IP 為基礎的鏡像 {#ip-based-mirroring}

此範例會鏡像來自 **ether1** 介面，且目的或來源 IP 位址為 192.168.88.0/24 的傳入流量，並將複本傳送至 **ether3** 介面。

```ros
/interface/ethernet/switch
set switch1 mirror-target=ether3 mirror-source=none
/interface/ethernet/switch/rule
add mirror=yes ports=ether1 switch=switch1 src-address=192.168.88.0/24
add mirror=yes ports=ether1 switch=switch1 dst-address=192.168.88.0/24
```

還有其他選項，請查看 [ACL 章節](/docs/bridging-and-switching/marvell-prestera-switch-chip-features#switch-rules-acl)，以瞭解可用於比對封包的所有可能參數。

#### 遠端交換器埠分析器 {#remote-switch-port-analyzer}

此範例會鏡像來自 **ether2** 介面的傳入與傳出流量，複本會封裝在 802.1Q VLAN 中，並使用 999 作為 VLAN ID，封包會傳送至 **ether3** 介面。如果原始流量已加上 VLAN 標籤，RSPAN 會再加上一層 VLAN 標籤作為外層標籤。這會讓鏡像流量被加上兩次標籤。如果 `mirror-target` 埠包含在啟用 vlan-filtering 的橋接器中，則 RSPAN 不需要在 `/interface/bridge/vlan` 選單下將該介面設為已標記 VLAN 成員。

```ros
/interface/ethernet/switch/port
set ether2 mirror-egress=yes mirror-ingress=yes
/interface/ethernet/switch
set switch1 mirror-target=ether3 rspan=yes rspan-egress-vlan-id=999 rspan-ingress-vlan-id=999
```

### 屬性參考 {#property-reference}

**子選單：** `/interface/ethernet/switch`

| 屬性 | 說明 |
| :-- | :-- |
| **mirror-target** (*cpu \| name \| none*；預設：**none**) | 選取單一鏡像目標埠。來自 `mirror-egress` 與 `mirror-ingress` (`/interface/ethernet/switch/port`) 以及 mirror (`/interface/ethernet/switch/rule`) 的封包將會傳送至所選埠。 |
| **rspan** (*no \| yes*；預設：**no**) | 在 `mirror-target` 上啟用遠端交換器埠分析器 (RSPAN) 功能。標記為傳入或傳出鏡像的流量會透過指定的遠端分析器 VLAN 傳送：`rspan-egress-vlan-id` 與 `rspan-ingress-vlan-id`。 |
| **rspan-egress-vlan-id** (*integer: 1..4095*；預設：**1**) | 選取標記傳出流量的 VLAN ID。僅在啟用 `rspan` 時適用。 |
| **rspan-ingress-vlan-id** (*integer: 1..4095*；預設：**1**) | 選取標記傳入流量的 VLAN ID。僅在啟用 `rspan` 時適用。 |

**子選單：** `/interface/ethernet/switch/port`

| 屬性 | 說明 |
| :-- | :-- |
| **mirror-egress** (*no \| yes*；預設：**no**) | 是否將傳出封包複本傳送至 `mirror-target` 埠。 |
| **mirror-ingress** (*no \| yes*；預設：**no**) | 是否將傳入封包複本傳送至 `mirror-target` 埠。 |

**子選單：** `/interface/ethernet/switch/rule`

| 屬性 | 說明 |
| :-- | :-- |
| **mirror** (*no \| yes*；預設：**no**) | 是否將封包副本傳送至 `mirror-target` 埠。 |

## 流量整形 {#traffic-shaping}

---

可以使用 ACL 規則限制符合特定參數的入口流量，也可以依埠限制入口與出口流量。policer 用於入口流量，shaper 用於出口流量。入口 policer 會以丟棄封包的方式控制接收的流量。超過定義限制的所有流量都會被丟棄。這可能會影響終端主機上的 TCP 壅塞控制機制，實際達成的頻寬可能低於定義值。出口 shaper 會嘗試將超過限制的封包排入佇列，而不是直接丟棄。最終，當輸出佇列已滿時，它仍會丟棄封包；不過，這應可更有效地利用定義的輸送量。

### 以埠為基礎的流量 policer 與 shaper {#port-based-traffic-police-and-shaper}

```ros
/interface/ethernet/switch/port
set ether1 ingress-rate=10M egress-rate=5M
```

### 以 MAC 為基礎的流量 policer {#mac-based-traffic-policer}

```ros
/interface/ethernet/switch/rule
add ports=ether1 switch=switch1 src-mac-address=64:D1:54:D9:27:E6/FF:FF:FF:FF:FF:FF rate=10M
```

### 以 VLAN 為基礎的流量 policer {#vlan-based-traffic-policer}

```ros
/interface/bridge
set bridge1 vlan-filtering=yes
/interface/ethernet/switch/rule
add ports=ether1 switch=switch1 vlan-id=11 rate=10M
```

:::danger
啟用 `vlan-filtering` 時，將會過濾掉目的地為 CPU 的流量。啟用 VLAN  filtering 之前，請確認已設定 [Management port](/docs/bridging-and-switching/marvell-prestera-switch-chip-features#management-access-configuration)。
:::

### 以通訊協定為基礎的流量管制器 {#protocol-based-traffic-policer}

```ros
/interface/ethernet/switch/rule
add ports=ether1 switch=switch1 mac-protocol=ipx rate=10M
```

也有其他選項，請查看 [ACL 章節](/docs/bridging-and-switching/marvell-prestera-switch-chip-features#switch-rules-acl)，以瞭解可用於比對封包的所有可能參數。

:::warning
Switch Rule 表用於 QoS 功能。請參閱[此表](/docs/bridging-and-switching/marvell-prestera-switch-chip-features#models)，瞭解每個設備支援多少規則。
:::

:::danger
受限於硬體限制，當 10Gbps 交換器埠以 10/100Mbps、1/2.5/5Gbps 連線時，`egress-rate` 與 `storm-rate` 設定無法正確運作。這適用於 98DX224S、98DX226S、98DX2528、98DX3236 交換器晶片。
:::

## 流量風暴控制 {#traffic-storm-control}

---

自 RouterOS v6.42 起，可以啟用流量風暴控制。當特定訊框在網路上持續氾濫時，就可能產生流量風暴。風暴控制設定通常設定在非上行埠上，以限制這些特定埠上的傳入風暴流量。這可藉由降低流量風暴在整個網路中的影響，保護整個交換器與其連接的埠。

例如，若已產生網路迴圈，且未使用任何迴圈避免機制（例如 [Spanning Tree Protocol](/docs/bridging-and-switching/user-guides/spanning-tree-protocol)），廣播或群播訊框可能迅速淹沒網路，造成網路效能降低，甚至導致網路完全中斷。使用搭載 Marvell Prestera 交換器的 MikroTik 設備時，可以限制廣播、未知群播與未知單播流量。當交換器沒有目的 MAC 位址的主機項目時，即視為未知單播流量。當交換器在 `/interface/bridge/mdb` 選單中沒有群播群組項目時，即視為未知群播流量。風暴控制設定應套用於 ingress 埠；egress 流量將會受到限制。

![Traffic Storm](/img/f275b4060eca4083.webp)

:::warning
風暴控制參數以鏈路速度的百分比（%）指定。若鏈路速度為 1Gbps，則將 `storm-rate` 指定為 `10` 時，只會允許 100Mbps 的廣播、未知群播及／或未知單播流量轉送。
:::

**子選單：** `/interface/ethernet/switch/port`

| 屬性 | 說明 |
| :-- | :-- |
| **limit-broadcasts** (*yes \| no*；預設：**yes**) | 限制交換器埠上的廣播流量。 |
| **limit-unknown-multicasts** (*yes \| no*；預設：**no**) | 限制交換器埠上的未知群播流量。 |
| **limit-unknown-unicasts** (*yes \| no*；預設：**no**) | 限制交換器埠上的未知單播流量。 |
| **storm-rate** (*integer 0..100*；預設：**100**) | 廣播、未知群播及／或未知單播流量會被限制為鏈路速度的百分比。 |

:::danger
搭載 98DX224S、98DX226S、98DX2528、98DX3236 交換器晶片的設備無法區分未知群播流量與所有群播流量。例如，CRS326-24G-2S+ 在使用 `limit-unknown-multicasts` 與 `storm-rate` 時，會限制所有群播流量。對於其他設備，例如 CRS317-1G-16S+，`limit-unknown-multicasts` 參數只會限制未知群播流量（未出現在 `/interface/bridge/mdb` 中的位址）。
:::

例如，若要在 ether1（1Gbps）上限制 1%（10Mbps）的廣播與未知單播流量，請使用下列指令：

```ros
/interface/ethernet/switch/port
set ether1 storm-rate=1 limit-broadcasts=yes limit-unknown-unicasts=yes
```

:::warning
受限於硬體限制，當 10Gbps 交換器埠以 10/100Mbps、1/2.5/5Gbps 連線時，`egress-rate` 與 `storm-rate` 設定無法正確運作。這適用於 98DX224S、98DX226S、98DX2528、98DX3236 交換器晶片。
:::

## MPLS 硬體卸載 {#mpls-hardware-offloading}

---

自 RouterOS v6.41 起，可以將特定 MPLS 功能卸載到交換器晶片。交換器必須是 PE-P-PE 架構中的 (P)rovider 路由器，才能達成硬體卸載。設定範例請參閱 [LDP 設定範例](/docs/user-guides/routing-and-networking-protocols/mpls/ldp#example-setup)。只有當 LDP 介面設定為實體交換器介面時才會進行硬體卸載（例如 Ethernet、SFP、SFP+）。

:::warning
目前只有使用 RouterOS v6.41 及以上版本的 `CRS317-1G-16S+` 與 `CRS309-1G-8S+` 能夠卸載特定 MPLS 功能。`CRS317-1G-16S+` 與 `CRS309-1G-8S+` 內建交換器晶片無法從封包中移除 MPLS 標籤，在 PE-P-PE 架構中，您必須使用 explicit null 或停用 MPLS 網路中的 TTL 傳播，才能達成硬體卸載。

**注意：** 自 RouterOS v7 起，MPLS 硬體卸載已移除。
:::

## 交換器規則（ACL） {#switch-rules-acl}

---

存取控制清單包含 ingress 政策引擎與 egress 政策引擎。請參閱[此表格](/docs/bridging-and-switching/marvell-prestera-switch-chip-features#models)，瞭解每項設備支援的規則數量。這是一項進階工具，可根據 Layer2、Layer3 與 Layer4 協定標頭欄位條件，進行線速封包過濾、轉送與修改。

ACL 規則會針對每個接收到的封包進行檢查，直到找到相符項目為止。如果有多個規則可以相符，則只會觸發第一個規則。沒有任何動作參數的規則，代表接受該封包。

啟用 IGMP snooping、DHCP snooping、RoMON、PTP 或 loop-protect 等功能時，可能會自動建立動態 ACL 規則。新增 ACL 項目時，應考量這些規則。建立新規則時，請使用 `place-before` 屬性，或使用 `move` 指令調整 ACL 規則順序。

:::warning
使用 L3 或 L4 比對條件時，不需要將 `mac-protocol` 設為特定 IP 版本，不過在過濾任何 IP 封包時，建議設定 `mac-protocol=ip` 或 `mac-protocol=ipv6`。
:::

:::danger
當交換器 ACL 規則被修改時（例如新增、移除、停用、啟用或移動），現有的交換器規則會在短時間內失效。這可能在 ACL 規則修改期間造成部分封包外洩。
:::

**子選單：** `/interface/ethernet/switch/rule`

| 屬性 | 說明 |
| :-- | :-- |
| **copy-to-cpu** (*no \| yes*；預設：**no**) | 複製相符的封包並傳送至 CPU。 |
| **disabled** (*yes \| no*；預設：**no**) | 啟用或停用 ACL 項目。 |
| **dscp** (*0..63*) | 比對封包的 DSCP 欄位（僅適用於 IPv4 封包）。 |
| **dst-address** (*IP address/Mask*) | 比對目的 IPv4 位址與遮罩。若指定 `mac-protocol=arp`，則比對 ARP 封包中的目的 IP。若未指定 `mac-protocol`，則只比對 IPv4 封包。 |
| **dst-address6** (*IPv6 address/Mask*) | 比對目的 IPv6 位址與遮罩。 |
| **dst-mac-address** (*MAC address/Mask*) | 比對目的 MAC 位址與遮罩。 |
| **dst-port** (*0..65535*) | 比對目的協定埠號（若未指定 `mac-protocol`，則適用於 IPv4 與 IPv6 封包）。 |
| **flow-label** (*0..1048575*) | 比對 IPv6 flow label。 |
| **mac-protocol** (*802.2 \| arp \| capsman \| dot1x \| homeplug-av \| ip \| ipv6 \| ipx \| lacp \| lldp \| loop-protect \| macsec \| mpls-multicast \| mpls-unicast \| mvrp \| packing-compr \| packing-simple \| pppoe \| pppoe-discovery \| rarp \| romon \| service-vlan \| vlan \| or 0..65535 \| or 0x0000-0xffff*) | 比對由協定名稱或號碼指定的特定 MAC 協定。 |
| **mirror** (*no \| yes*) | 複製相符的封包並傳送至 mirror-target 埠。 |
| **new-dst-ports** (*ports \| bond \| all*) | 將目的埠變更為指定值：<br/><ul><li>若將設定留空（例如 <code>new-dst-ports=""</code>），封包將被丟棄；</li><li>若指定某個埠或<a href="/docs/bridging-and-switching/marvell-prestera-switch-chip-features#bonding" rel="nofollow"> 硬體卸載 bonding </a>介面，封包將被重新導向至該埠。僅支援單一埠或 bond 介面；</li><li>若使用 <code>all</code> 引數，封包將被允許通過 egress 處理而不會被丟棄；</li><li>若未使用此參數，封包將依原樣接受。</li></ul> |
| **new-vlan-id** (*0..4095*) | 將 VLAN ID 變更為指定值。需要 `vlan-filtering=yes`。 |
| **new-vlan-priority** (*0..7*) | 變更 VLAN 優先順序（priority code point）。需要 `vlan-filtering=yes`。 |
| **new-vrf** (*vrf name*) | 將 ingress 流量指派至指定的 VRF。需要交換器晶片支援[硬體卸載 VRF](/docs/bridging-and-switching/l3-hardware-offloading#l3hw-feature-support)。在不支援 VRF 的交換器（98DX3xxx 與 98DX2xxx 系列）上，將 `new-vrf` 設為 `main` 以外的值時，應搭配 `redirect-to-cpu=yes`。 |
| **ports** (*ports \| bond*) | 比對規則將套用於傳入流量的交換器介面。可選取多個埠與[硬體卸載 bonding](/docs/bridging-and-switching/marvell-prestera-switch-chip-features#bonding)介面。請注意，無法選取 `switch1-cpu` 埠。若 `ports` 屬性留空，規則將套用於所有交換器介面。 |
| **protocol** (*dccp \| ddp \| egp \| encap \| etherip \| ggp \| gre \| hmp \| icmp \| icmpv6 \| idpr-cmtp \| igmp \| ipencap \| ipip \| ipsec-ah \| ipsec-esp \| ipv6 \| ipv6-frag \| ipv6-nonxt \| ipv6-opts \| ipv6-route \| iso-tp4 \| l2tp \| ospf \| pim \| pup \| rdp \| rspf \| rsvp \| sctp \| st \| tcp \| udp \| udp-lite \| vmtp \| vrrp \| xns-idp \| xtp \| or 0..255*) | 比對由協定名稱或號碼指定的特定 IP 協定。若未指定 `mac-protocol`，則僅適用於 IPv4 封包。若要比對特定 IPv6 協定，請使用 `mac-protocol=ipv6` 設定。 |
| **rate** (*0..4294967295*) | 為相符的流量設定 ingress 流量限制（位元每秒）。 |
| **redirect-to-cpu** (*no \| yes*) | 將相符封包的目的埠變更為 CPU。 |
| **src-address** (*IP address/Mask*) | 比對來源 IPv4 位址與遮罩。若指定 `mac-protocol=arp`，則比對 ARP 封包中的來源 IP。若未指定 `mac-protocol`，則只比對 IPv4 封包。 |
| **src-address6** (*IPv6 address/Mask*) | 比對來源 IPv6 位址與遮罩。 |
| **src-mac-address** (*MAC address/Mask*) | 比對來源 MAC 位址與遮罩。 |
| **src-port** (*0..65535*) | 比對來源協定埠號（若未指定 `mac-protocol`，則適用於 IPv4 與 IPv6 封包）。 |
| **switch** (*switch group*) | 比對規則將套用的交換器群組。 |
| **traffic-class** (*0..255*) | 比對 IPv6 traffic class。 |
| **vlan-id** (*0..4095*) | 比對 VLAN ID。需要 `vlan-filtering=yes`。 |
| **vlan-header** (*not-present \| present*) | 比對 VLAN 標頭，判斷 VLAN 標頭是否存在。需要 `vlan-filtering=yes`。 |
| **vlan-priority** (*0..7*) | 比對 VLAN 優先順序（priority code point）。 |

### Action 參數 {#action-parameters}

- copy-to-cpu
- redirect-to-cpu
- mirror
- new-dst-ports（可用於丟棄封包）
- new-vlan-id
- new-vlan-priority
- new-vrf
- rate

### Layer2 條件參數 {#layer2-condition-parameters}

- dst-mac-address
- mac-protocol
- src-mac-address
- vlan-id
- vlan-header
- vlan-priority

### Layer3 條件參數 {#layer3-condition-parameters}

- dscp
- protocol
- IPv4 條件：
  - dst-address
  - src-address
- IPv6 條件：
  - dst-address6
  - flow-label
  - src-address6
  - traffic-class

### Layer4 條件參數 {#layer4-condition-parameters}

- dst-port
- src-port

:::warning
若要讓 VLAN 相關比對條件或 VLAN 相關動作參數生效，必須在 bridge 介面上啟用 `vlan-filtering`，並確認這些埠已啟用硬體卸載，否則這些參數不會有任何作用。
:::
:::warning
當 bridge 介面的 `ether-type` 設為 `0x8100` 時，VLAN 相關 ACL 規則適用於使用一般／客戶 VLAN 標記的訊框（TPID 0x8100）；這包括 `vlan-id` 與 `new-vlan-id`。當 bridge 介面的 `ether-type` 設為 `0x88a8` 時，ACL 規則適用於使用 802.1ad service tag 標記的訊框（TPID 0x88a8）。
:::

## 埠安全性 {#port-security}

---

可以限制單一交換器埠上允許的 MAC 位址。例如，若要允許 64:D1:54:81:EF:8E MAC 位址通過交換器埠，請先將多個埠切換在一起。在此範例中，64:D1:54:81:EF:8E 將位於 **ether1** 後方。

建立 ACL 規則，以允許指定的 MAC 位址，並丟棄 **ether1** 上的所有其他流量（針對 ingress 流量）：

```ros
/interface/ethernet/switch/rule
add ports=ether1 src-mac-address=64:D1:54:81:EF:8E/FF:FF:FF:FF:FF:FF switch=switch1
add new-dst-ports="" ports=ether1 switch=switch1
```

Egress 流量仍可能包含不應送達 MAC 位址未知設備的資訊。  
假設埠已切換，請停用 MAC 學習，並停用 **ether1** 上的未知 unicast flooding：

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether1 hw=yes learn=no unknown-unicast-flood=no
add bridge=bridge1 interface=ether2 hw=yes
```

停用 MAC 學習後，需要為 64:D1:54:81:EF:8E 新增靜態 host 項目（針對 egress 流量）：

```ros
/interface/bridge/host
add bridge=bridge1 interface=ether1 mac-address=64:D1:54:81:EF:8E
```

:::warning
Broadcast 與 multicast 流量仍會從 **ether1** 送出。你可以使用 `broadcast-flood` 與 `unknown-multicast-flood` 參數來避免這種情況。請注意，某些解決方案可能依賴這些設定，例如串流協定與 DHCP。
:::

## 雙重開機 {#dual-boot}

---

「雙重開機」功能可讓你選擇要在 CRS3xx 系列交換器上使用哪種作業系統，RouterOS 或 SwOS。可使用下列方式變更設備的作業系統：

- 指令列 (`/system/routerboard/settings/set boot-os=swos`)
- Winbox
- Webfig
- 序列主控台

更多關於 SwOS 的詳細資訊請參閱：[SwOS 手冊](https://help.mikrotik.com/docs/display/SWOS/SwOS)。

:::warning
若要確認某個型號是否支援開機進入 SwOS，請參閱 [SwOS 型號表](https://help.mikrotik.com/docs/spaces/SWOS/pages/76415036/CRS3xx+and+CSS3xx+series+Manual#CRS3xxandCSS3xxseriesManual-Models) 以及產品頁面中「Specifications」下的「Operating System」。
:::

## 使用 RouterOS 設定 SwOS {#configuring-swos-using-routeros}

---

自 RouterOS 6.43 起，可透過 RouterOS 載入、儲存及重設 SwOS 設定，也可以升級 SwOS，並為 CRS3xx 系列交換器設定 IP 位址：

- 使用 `/system/swos/save-config` 儲存設定。

:::warning
設定會以 `swos.config` 作為檔名儲存在同一台設備上。請務必從設備下載該檔案，因為重新開機後設定檔將會被移除。
:::

- 使用 `/system/swos/load-config` 載入設定。
- 使用 `/system/swos/password` 變更密碼。
- 使用 `/system/swos/reset-config` 重設設定。
- 使用 `/system/swos/upgrade` 從 RouterOS 升級 SwOS。

:::warning
升級指令會自動安裝最新可用的 SwOS primary backup 版本，請確認你的設備可以存取網際網路，讓升級程序正常運作。當設備開機進入 SwOS 時，版本號碼會包含字母「p」，表示這是 primary backup 版本。接著可以從 SwOS 的「Upgrade」選單安裝最新可用的 SwOS secondary main 版本。
:::

:::warning
從 RouterOS 7.17 版開始，device-mode 會限制雙重開機的 SwOS/RouterOS 切換；若要啟用：`/system/device-mode/update` routerboard=yes
:::

| Property | Description |
| :-- | :-- |
| **address-acquisition-mode** (*dhcp-only \| dhcp-with-fallback \| static*; Default: **dhcp-with-fallback**) | 變更位址取得方式：dhcp-only - 僅使用 DHCP 用戶端取得位址 <br/> dhcp-with-fallback - 前 10 秒會嘗試使用 DHCP 用戶端取得位址。若要求失敗，則會回退到 static-ip-address 屬性所定義的靜態位址 <br/> static - 位址會依照 static-ip-address 屬性所定義的方式設定 |
| **allow-from** (*IP/Mask*; Default: **0.0.0.0/0**) | 可存取交換器的 IP 位址或網路。預設情況下，任何 IP 位址都可以存取交換器。 |
| **allow-from-ports** (*name*; Default: ) | 可存取設備的交換器埠清單。預設情況下，所有埠都可以存取交換器 |
| **allow-from-vlan** (*integer: 0..4094*; Default: **0**) | 可存取設備的 VLAN ID。預設情況下，所有 VLAN 都允許存取 |
| **identity** (*name*; Default: **Mikrotik**) | 交換器名稱（用於 Mikrotik Neighbor Discovery 協定） |
| **static-ip-address** (*IP*; Default: **192.168.88.1**) | 當 address-acquisition-mode 設為 dhcp-with-fallback 或 static 時，交換器的 IP 位址。設定靜態 IP 位址不會變更位址取得程序，預設為 DHCP with fallback。這表示所設定的靜態 IP 位址只會在同一廣播網域內沒有 DHCP 伺服器時才會生效 |

## 另請參閱 {#see-also}

[Basic VLAN switching](/docs/bridging-and-switching/user-guides/basic-vlan-switching)

[Bridge Hardware Offloading](/docs/bridging-and-switching/marvell-prestera-switch-chip-features#bridge-hardware-offloading)

[L3HW Route Hardware Offloading](/docs/bridging-and-switching/l3-hardware-offloading)

[Quality of Service](/docs/bridging-and-switching/quality-of-service)

[Spanning Tree Protocol](/docs/bridging-and-switching/user-guides/spanning-tree-protocol)

[MTU on RouterBOARD](/docs/hardware/mtu-in-routeros)

[Layer2 misconfiguration](/docs/bridging-and-switching/user-guides/layer2-misconfiguration)

[Bridge VLAN Table](/docs/bridging-and-switching/user-guides/bridge-vlan-table)

[Bridge IGMP/MLD snooping](/docs/bridging-and-switching/user-guides/bridge-igmp-mld-snooping)

[Multi-chassis Link Aggregation Group](/docs/high-availability-solutions/multi-chassis-link-aggregation-group)
