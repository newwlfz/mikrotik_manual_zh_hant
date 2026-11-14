---
sidebar_key: "bridging-and-switching/marvell-prestera-switch-chip-features"
sidebar_position: 1
title: "Marvell Prestera 交換晶片功能"
sidebar_label: "Marvell Prestera 交換晶片功能"
description: "搭載 Marvell Prestera 交換晶片的 MikroTik 裝置提供高效能的二層和三層功能，包括高階轉發、路由解除安裝、VLAN 支援、QoS、映象，以及用於精確計時的 PTP 同步。"
tags:
  - 'crs3xx'
  - 'crs5xx'
  - 'crs4xx'
  - 'crs8xx'
  - 'prestera'
source: https://manual.mikrotik.com/docs/7.25/bridging-and-switching/marvell-prestera-switch-chip-features
captured_at: '2026-11-04T11:14:26+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

---

部分 MikroTik 裝置使用高效能、功能豐富的 Marvell Prestera 乙太網交換器。這些裝置可設計用於各種乙太網應用，包括非管理型交換器、二層管理型交換器、運營商交換器、VLAN 間路由器和有線統一封包處理器。

:::warning
本文僅適用於配備 Marvell Prestera 交換器的 MikroTik 裝置，不適用於 [CRS1xx/CRS2xx 系列交換器](./user-guides/crs1xx-2xx-series-switches-examples.md)。
:::

### 功能 {#features}

<WideTable>

| 功能 | 描述 |
| :-- | :-- |
| **轉發** | <ul class="bullets"><li>可配置埠用於交換或路由</li><li>全非阻塞線速交換</li><li>用於二層單播轉發的大型單播 FDB</li><li>轉發資料庫基於 IVL 工作</li><li>支援巨型幀</li><li>支援 IGMP/MLD Snooping</li><li>支援 DHCP Snooping，帶有自定義 Option 82（Circuit ID、Remote ID）</li><li>支援 DHCPv6 Snooping，帶有自定義 Option 18（Interface ID）和 Option 37（Remote ID）</li><li>支援 RA Guard</li></ul> |
| **路由** | 三層硬體解除安裝：IPv4、IPv6 單播路由支援乙太網、網橋、鏈路聚合和 VLAN 介面ECMP黑洞解除安裝的 Fasttrack 連線 <sup>1</sup>用於 Fasttrack 連線的解除安裝 NAT <sup>1</sup>硬體解除安裝 VRF <sup>1</sup>多個 MTU 配置檔案**重要：** 1. 僅適用於[某些交換器型號](./l3-hardware-offloading.md#l3hw-device-support)  |
| **生成樹協定** | <ul class="bullets"><li>STP</li><li>RSTP</li><li>MSTP</li><li>Edge port、BPDU Guard、Root Guard</li></ul> |
| **映象** | <ul class="bullets"><li>多種映象型別：<ul class="bullets"><li>基於埠的映象</li><li>基於 VLAN 的映象</li><li>基於 MAC 的映象</li><li>Remote Switch Port Analyzer (RSPAN)</li></ul></li></ul> |
| **VLAN** | <ul class="bullets"><li>完全相容 IEEE802.1Q 和 IEEE802.1ad VLAN</li><li>4k 活動 VLAN</li><li>靈活的 VLAN 分配：<ul class="bullets"><li>基於埠的 VLAN</li><li>基於協定的 VLAN</li><li>基於 MAC 的 VLAN</li></ul></li><li>VLAN 過濾</li><li>入向 VLAN 轉換</li><li>Multiple VLAN Registration protocol (MVRP)</li></ul> |
| **Bonding** | <ul class="bullets"><li>支援 802.3ad (LACP)、balance-xor 和 active-backup 模式</li><li>每個 Bonding 介面最多 8 個成員埠</li><li>硬體自動故障轉移和負載均衡</li><li>MLAG</li></ul> |
| **服務質量 (QoS)** | <ul class="bullets"><li>每埠八個輸出佇列</li><li>DSCP 和 802.1p PCP 對映</li><li>基於埠的二層和三層信任設定</li><li>基於埠和佇列的出向速率限制器</li><li>透過 ACL 規則實現基於策略的 QoS</li><li>Strict Priority (SP) 和 Shaped Deficit Weighted Round Robin (SDWRR) 排隊</li><li>Enhanced Transmission Selection (ETS) 排程</li><li>Weighted Random Early Detection (WRED) <sup>1</sup></li><li>Explicit Congestion Notification (ECN) <sup>1</sup></li><li>Priority-based Flow Control (PFC) <sup>1</sup></li><li>資源分配控制（基於佇列、shared-pool 和組播）並提供廣泛的監控能力</li><li>相容 Dante 環境</li><li>相容 RDMA over Converged Ethernet (RoCE) 環境 <sup>1</sup></li><li>入向流量限制（基於埠或透過 ACL 規則）</li><li>流量風暴控制</li></ul><br/><strong>重要：</strong> 1. 僅適用於[某些交換器型號](./quality-of-service.md#qos-device-support)<br/> |
| **埠隔離** | <ul class="bullets"><li>適用於 Private VLAN 實施</li></ul> |
| **訪問控制列表** | <ul class="bullets"><li>入向 ACL 表</li><li>基於埠、L2、L3、L4 協定頭欄位進行分類</li><li>ACL 操作包括過濾、轉發和修改協定頭欄位</li></ul> |
| **PTP** | <ul class="alternate"><li>兩步 Ordinary Clock 和 Boundary Clock。</li><li>硬體時間戳，確保納秒(ns)範圍內的時鐘同步。</li><li>IPv4 和二層 (L2) 組播傳輸模式。</li><li>End-to-End (E2E) 和 Peer-to-Peer (P2P) 延遲機制。</li><li>IEEE 1588-2008 (PTPv2)。</li><li>支援的 Profile：<ul><li>802.1AS：用於 Audio Video Bridging (AVB) 和 Time-Sensitive Networking (TSN) 的定時與同步。</li><li>AES67：高效能 audio-over-IP 互操作性。</li><li>G.8275.1：在 PTP-aware 網路中的頻率和相位同步。</li><li>SMPTE：專業廣播環境中的音訊/影片同步。</li></ul></li></ul><br/><strong>重要：</strong> PTP 支援取決於硬體，請參閱[支援的裝置](../system-information-and-utilities/precision-time-protocol.md#supported-devices)列表。<br/> |

:::info
有關三層硬體解除安裝功能支援和硬體限制，請參閱[功能支援](./l3-hardware-offloading.md#l3hw-device-support)使用者手冊。
:::

:::note
有關 QoS 硬體解除安裝功能支援和硬體限制，請參閱[服務質量（QoS）](./quality-of-service.md)使用者手冊。
:::

</WideTable>

### 型號 {#models}

下表說明了 Cloud Router Switch 型號與 CCR 路由器之間的主要差異。

<WideTable>

|  |  |  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| **型號** | **交換晶片** | **CPU** | **記憶體大小** | **乙太網** | **[PoE 輸出](../hardware/poe-out.md)** | **ACL 規則** | **單播 FDB 條目** | **巨型幀（位元組）** |
| **CRS318-1Fi-15Fr-2S-OUT (netPower 15FR)** | Marvell-98DX224S | ARM 2-core 800MHz | 256 MB | 16x 10/100M 乙太網  2x 1G SFP | 1x passive | 128 | 最高 16K | 10218 |
| **CRS318-16P-2S+OUT (netPower 16P)** | Marvell-98DX226S | ARM 2-core 800MHz | 256 MB | 16x 10/100/1000M 乙太網  2x 10G SFP+ | 16x 802.3af/at | 128 | 最高 16K | 10218 |
| **CRS310-1G-5S-4S+ (netFiber 9/IN)** | Marvell-98DX226S | ARM 2-core 800MHz | 256 MB | 1x 10/100/1000M 乙太網  5x 1G SFP  4x 10G SFP+ |  | 128 | 最高 16K | 10218 |
| **CRS310-8G+2S+IN** | Marvell-98DX226S | ARM 2-core 800MHz | 256 MB | 8x 2.5G 乙太網  2x 10G SFP+ |  | 128 | 最高 16K | 10218 |
| **CRS320-8P-8B-4S+RM** | Marvell-98DX226S | ARM 2-core 800MHz | 256 MB | 16x 10/100/1000M 乙太網  4x 10G SFP+ | 8x 802.3af/at  8x 802.3bt | 128 | 最高 16K | 10218 |
| **CRS304-4XG-IN** | Marvell-98DX2528 | ARM64 2-core 1200MHz | 512 MB | 4x 1/2.5/5/10G 乙太網 |  | 128 | 最高 16K | 10218 |
| **CRS326-24G-2S+ (RM/IN)** | Marvell-98DX3236 | ARM 2-core 800MHz | 512 MB | 24x 10/100/1000M 乙太網  2x 10G SFP+ |  | 128 | 最高 16K | 10218 |
| **CRS328-24P-4S+RM** | Marvell-98DX3236 | ARM 1-core 800MHz | 512 MB | 24x 10/100/1000M 乙太網  4x 10G SFP+ | 24x 802.3af/at | 128 | 最高 16K | 10218 |
| **CRS328-4C-20S-4S+RM** | Marvell-98DX3236 | ARM 2-core 800MHz | 512 MB | 20x 1G SFP  4x 1G combo  4x 10G SFP+ |  | 128 | 最高 16K | 10218 |
| **CRS305-1G-4S+IN** | Marvell-98DX3236 | ARM 2-core 800MHz | 512 MB | 1x 10/100/1000M 乙太網  4x 10G SFP+ |  | 128 | 最高 16K | 10218 |
| **CRS305-1G-4S+OUT (FiberBox Plus)** | Marvell-98DX226S | ARM 2-core 800MHz | 256 MB | 1x 10/100/1000M 乙太網  4x 10G SFP+ |  | 128 | 最高 16K | 10218 |
| **CRS309-1G-8S+IN** | Marvell-98DX8208 | ARM 2-core 800MHz | 512 MB | 1x 10/100/1000M 乙太網  8x 10G SFP+ |  | 1024 | 最高 32K | 10218 |
| **CRS317-1G-16S+RM** | Marvell-98DX8216 | ARM 2-core 800MHz | 1 GB | 1x 10/100/1000M 乙太網  16x 10G SFP+ |  | 1024 | 最高 128K | 10218 |
| **CRS312-4C+8XG-RM** | Marvell-98DX8212 | MIPSBE 1-core 650MHz | 64 MB | 4x 10G combo  8x 1/2.5/5/10G 乙太網 |  | 512 | 最高 32K | 10218 |
| **CRS326-24S+2Q+RM** | Marvell-98DX8332 | MIPSBE 1-core 650MHz | 128 MB | 24x 10G SFP+  2x 40G QSFP+ |  | 256 | 最高 32K | 10218 |
| **CRS326-4C+20G+2Q+RM** | Marvell-98DX8332 | MIPSBE 1-core 650MHz | 128 MB | 4x 2.5G 乙太網/10G SFP+ combo  20x 2.5G 乙太網  2x 40G QSFP+ |  | 256 | 最高 32K | 10218 |
| **CRS354-48G-4S+2Q+RM** | Marvell-98DX3257 | MIPSBE 1-core 650MHz | 128 MB | 48x 10/100/1000M 乙太網  4x 10G SFP+  2x 40G QSFP+ |  | 170 | 最高 32K | 10218 |
| **CRS354-48P-4S+2Q+RM** | Marvell-98DX3257 | MIPSBE 1-core 650MHz | 128 MB | 48x 10/100/1000M 乙太網  4x 10G SFP+  2x 40G QSFP+ | 48x 802.3af/at | 170 | 最高 32K | 10218 |
| **CRS418-8P-8G-2S+RM**  **CRS418-8P-8G-2S+5axQ2axQ-RM** | Marvell-98DX226S | ARM64 4-core 2208MHz | 1 GB | 16x 10/100/1000M 乙太網  2x 10G SFP+ | 8x 802.3af/at | 128 | 最高 16K | 10218 |
| **CRS504-4XQ (IN/OUT)** | Marvell-98DX4310 | MIPSBE 1-core 650MHz | 64 MB | 4x 100G QSFP28 |  | 1024 | 最高 128K | 10218 |
| **CRS510-8XS-2XQ-IN** | Marvell-98DX4310 | MIPSBE 1-core 650MHz | 128 MB | 8x 25G SFP28  2x 100G QSFP28 |  | 1024 | 最高 128K | 10218 |
| **CRS518-16XS-2XQ-RM** | Marvell-98DX8525 | MIPSBE 1-core 650MHz | 64 MB | 16x 25G SFP28  2x 100G QSFP28 |  | 1024 | 最高 128K | 10218 |
| **CRS520-4XS-16XQ-RM** | Marvell-98CX8410 | ARM64 4-core 2000MHz | 4 GB | 4x 25G SFP28  16x 100G QSFP28 |  | 682 | 最高 256K | 9570 |
| **CRS812-8DS-2DQ-2DDQ-RM** | Marvell-98DX7335 | ARM64 4-core 2000MHz | 4 GB | 8x 50G SFP56  2x 200G QSFP56  2x 400G QSFP56-DD |  | 1365 | 最高 128K | 9570 |
| **CRS804-4DDQ-hRM** | Marvell-98DX7335 | ARM64 4-core 2000MHz | 4 GB | 4x 400G QSFP56-DD |  | 1365 | 最高 128K | 9570 |
| **CCR2116-12G-4S+** | Marvell-98DX3255 | ARM64 16-core 2000MHz | 16 GB | 12x 10/100/1000M 乙太網  4x 10G SFP+ |  | 512 | 最高 32K | 9570 |
| **CCR2216-1G-12XS-2XQ** | Marvell-98DX8525 | ARM64 16-core 2000MHz | 16 GB | 12x 25G SFP28  2x 100G QSFP28 |  | 1024 | 最高 128K | 9570 |
| **RDS2216-2XG-4S+4XS-2XQ** | Marvell-98DX4310 | ARM64 16-core 2000MHz | 32 GB | 2x 1/2.5/5/10G 乙太網  4x 10G SFP+  4x 25G SFP28  2x 100G QSFP28 |  | 1024 | 最高 128K | 9570 |

</WideTable>

### 縮寫 {#abbreviations}

- FDB - 轉發資料庫。
- MDB - 組播資料庫。
- SVL - 共享 VLAN 學習。
- IVL - 獨立 VLAN 學習。
- PVID - 埠 VLAN ID。
- ACL - 訪問控制列表。
- CVID - 客戶 VLAN ID。
- SVID - 服務 VLAN ID。

## 埠交換 {#port-switching}

---

要設定埠交換，請參閱[網橋硬體解除安裝](./index.md#bridge-hardware-offloading)頁面。

:::danger
目前只能建立一個啟用硬體解除安裝的網橋。使用 `hw=yes/no` 引數選擇哪個網橋將使用硬體解除安裝。
:::

:::warning
網橋 STP/RSTP/MSTP、IGMP Snooping 和 VLAN 過濾設定不會影響硬體解除安裝。自 RouterOS v6.42 起，Bonding 介面也支援硬體解除安裝。
:::

## VLAN {#vlan}

---

自 RouterOS 6.41 起，網橋在網橋內提供 VLAN 感知的二層轉發和 VLAN 標籤修改。這組功能使網橋操作更像傳統乙太網交換器，並且與將隧道式 VLAN 介面加入網橋的配置相比，可克服生成樹相容性問題。強烈建議配置網橋 VLAN 過濾，以符合 STP（802.1D）、RSTP（802.1w）標準；在 RouterOS 中啟用 MSTP（802.1s）支援則是強制要求。

### VLAN 過濾 {#vlan-filtering}

詳細的架構概念和配置步驟請參閱主要的[網橋 VLAN 過濾](./index.md#bridge-vlan-filtering)章節。

#### 支援的 VLAN 實現 {#supported-vlan-implementations}

根據網路設計，您可以實施多種硬體解除安裝的 VLAN 拓撲：

- **基於埠的 VLAN：** 請參閱[網橋 VLAN 過濾](./index.md#bridge-vlan-filtering)章節中的分步配置指南。
- **基於協定的 VLAN：** 透過交換器規則表進行配置，以對映特定網路協定。
- **基於 MAC 的 VLAN：** 將特定源 MAC 地址對映到指定的 VLAN ID。

---

### 基於 MAC 的 VLAN 配置 {#mac-based-vlan-configuration}

:::warning 硬體與轉發限制

- **規則容量：** 此功能使用硬體交換器規則表。請參閱[交換晶片型號容量表](./marvell-prestera-switch-chip-features.md#models)以確認您的特定裝置支援多少條規則。
- **CPU 轉發限制：** 基於 MAC 的 VLAN 嚴格適用於在硬體埠之間交換的流量。如果封包被路由或轉發到 CPU，則強制執行網橋埠的預設 `pvid`，而不是 ACL 規則中定義的 `new-vlan-id` 動作。
- **DHCP 衝突：** 如果網橋上啟用了 `dhcp-snooping=yes`，基於 MAC 的 VLAN 匹配將無法處理 DHCP 封包。
:::

#### 配置示例 {#configuration-example}

透過建立啟用硬體解除安裝的網橋來啟用埠交換：

```ros
/interface/bridge
add name=bridge1 vlan-filtering=yes
/interface/bridge/port
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether7 hw=yes
```

在網橋 VLAN 表中新增 VLAN 並指定埠：

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=ether2 untagged=ether7 vlan-ids=200,300,400
```

新增根據 MAC 地址分配 VLAN ID 的交換器規則：

```ros
/interface/ethernet/switch/rule
add switch=switch1 ports=ether7 src-mac-address=A4:12:6D:77:94:43/FF:FF:FF:FF:FF:FF new-vlan-id=200
add switch=switch1 ports=ether7 src-mac-address=84:37:62:DF:04:20/FF:FF:FF:FF:FF:FF new-vlan-id=300
add switch=switch1 ports=ether7 src-mac-address=E7:16:34:A1:CD:18/FF:FF:FF:FF:FF:FF new-vlan-id=400
```

#### 基於協定的 VLAN {#protocol-based-vlan}

:::warning

- 交換器規則表用於基於協定的 VLAN 功能，請參閱[此表](./marvell-prestera-switch-chip-features.md#models)瞭解每臺裝置支援多少條規則。
- 基於協定的 VLAN 僅在交換器埠之間正常工作，而在交換器埠與 CPU 之間不能正常工作。當封包被轉發到 CPU 時，將始終使用網橋埠的 `pvid` 屬性，而不是 ACL 規則中的 `new-vlan-id`。
- 啟用 DHCP snooping 時，基於協定的 VLAN 將不適用於 DHCP 封包。

:::

透過建立啟用硬體解除安裝的網橋來啟用埠交換：

```ros
/interface/bridge
add name=bridge1 vlan-filtering=yes
/interface/bridge/port
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether6 hw=yes
add bridge=bridge1 interface=ether7 hw=yes
add bridge=bridge1 interface=ether8 hw=yes
```

在網橋 VLAN 表中新增 VLAN 並指定埠：

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=ether2 untagged=ether6 vlan-ids=200
add bridge=bridge1 tagged=ether2 untagged=ether7 vlan-ids=300
add bridge=bridge1 tagged=ether2 untagged=ether8 vlan-ids=400
```

新增根據 MAC 協定分配 VLAN ID 的交換器規則：

```ros
/interface/ethernet/switch/rule
add mac-protocol=ip new-vlan-id=200 ports=ether6 switch=switch1
add mac-protocol=ipx new-vlan-id=300 ports=ether7 switch=switch1
add mac-protocol=0x80F3 new-vlan-id=400 ports=ether8 switch=switch1
```

#### VLAN 隧道（Q-in-Q） {#vlan-tunneling-q-in-q}

自 RouterOS v6.43 起，可以同時使用提供商網橋（IEEE 802.1ad）和標籤堆疊 VLAN 過濾以及硬體解除安裝。配置在[網橋 VLAN 隧道（Q-in-Q）](./vlan.md#q-in-q)章節中描述。

:::danger
使用 Marvell-98DX3257 交換晶片的裝置（例如 CRS354 系列）在 1Gbps 乙太網介面上不支援其他 VLAN 型別（`0x88a8` 和 `0x9100`）的 VLAN 過濾。
:::

### 入口 VLAN 轉換 {#ingress-vlan-translation}

可以使用入口埠上的 ACL 規則將某個 VLAN ID 轉換為不同的 VLAN ID。在此示例中，我們建立兩條 ACL 規則，以允許雙向通訊。可按以下步驟完成。

建立新網橋並向其中新增啟用硬體解除安裝的埠：

```ros
/interface/bridge
add name=bridge1 vlan-filtering=no
/interface/bridge/port
add interface=ether1 bridge=bridge1 hw=yes
add interface=ether2 bridge=bridge1 hw=yes
```

新增 ACL 規則以在每個方向上轉換 VLAN ID：

```ros
/interface/ethernet/switch/rule
add new-dst-ports=ether2 new-vlan-id=20 ports=ether1 switch=switch1 vlan-id=10
add new-dst-ports=ether1 new-vlan-id=10 ports=ether2 switch=switch1 vlan-id=20
```

將兩個 VLAN ID 都新增到網橋 VLAN 表：

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=ether1 vlan-ids=10
add bridge=bridge1 tagged=ether2 vlan-ids=20
```

啟用網橋 VLAN 過濾：

```ros
/interface/bridge/set bridge1 vlan-filtering=yes
```

:::warning
雙向通訊僅限於兩個交換器埠之間。在更多埠之間轉換 VLAN ID 可能導致流量泛洪或同一 VLAN 埠之間的錯誤轉發。

**注意：** 啟用 `vlan-filtering` 後，您將過濾掉髮往 CPU 的流量。在啟用 VLAN 過濾之前，應確保已設定[管理埠](./index.md#management-access-configuration)。
:::

## (R/M)STP {#rmstp}

---

配備 Marvell Prestera 交換器的 MikroTik 裝置能夠在硬體層面執行 STP、RSTP 和 MSTP。有關更多詳細資訊，請檢視[生成樹協定](./user-guides/spanning-tree-protocol.md)手冊頁；有關相關配置/監控選項，請參閱[網橋與交換](./index.md)頁面。

## 鏈路聚合 {#bonding}

---

配備 Marvell Prestera 交換器的 MikroTik 裝置支援鏈路聚合介面的硬體解除安裝。僅 `802.3ad`（LACP）、`balance-xor`（靜態 LAG）和 `active-backup` 鏈路聚合模式支援硬體解除安裝；其他鏈路聚合模式將使用 CPU 資源。有關鏈路聚合介面的更多資訊，請參閱[鏈路聚合介面](../high-availability-solutions/bonding.md)章節。

要建立硬體解除安裝的鏈路聚合介面，必須使用受支援的鏈路聚合模式建立鏈路聚合介面：

```ros
/interface/bonding
add mode=802.3ad name=bond1 slaves=ether1,ether2
```

此介面可與其他介面一起新增到網橋：

```ros
/interface/bridge
add name=bridge
/interface/bridge/port
add bridge=bridge interface=bond1 hw=yes
add bridge=bridge interface=ether3 hw=yes
add bridge=bridge interface=ether4 hw=yes
```

:::warning
不要將已在 bond 中的介面新增到網橋；RouterOS 不允許將已是鏈路聚合從埠的介面新增到網橋。
:::

透過檢查 "H" 標誌，確保鏈路聚合介面已硬體解除安裝：

```text
/interface/bridge/port/print 
Flags: X - disabled, I - inactive, D - dynamic, H - hw-offload 
 #     INTERFACE                                 BRIDGE                                 HW
 0   H bond1                                     bridge                                 yes
 1   H ether3                                    bridge                                 yes
 2   H ether4                                    bridge                                 yes
```

:::warning
對於硬體解除安裝的鏈路聚合介面，內建交換晶片將始終使用 Layer2+Layer3+Layer4 作為傳送雜湊策略；手動更改傳送雜湊策略將不會生效。
:::

### 配置示例 - 使用鏈路聚合的 VLAN {#configuration-example---vlans-with-bonds}

本節將展示如何配置多臺交換器以使用鏈路聚合介面和基於埠的 VLAN，並展示一個包含 DHCP 伺服器、VLAN 間路由、管理 IP 和無效 VLAN 過濾配置的完整示例。

對於此網路拓撲，我們將使用兩臺 CRS326-24G-2S+、一臺 CRS317-1G-16S+ 和一臺 CCR1072-1G-8S+。

![CRS3xx VLANs with Bonds](/img/4664a0d68abb9987.webp)

在此設定中，SwitchA 和 SwitchC 會將來自埠 ether1-ether8 的所有流量標記為 VLAN ID 10，將 ether9-ether16 標記為 VLAN ID 20，並將 ether17-ether24 標記為 VLAN ID 30。只有當用戶從 SwitchA 或 SwitchB 上的 ether1 使用 VLAN ID 99 的帶標籤流量連線時，才能進行管理。也可以從路由器使用 VLAN ID 99 的帶標籤流量連線到所有裝置。此設定中的 SFP+ 埠將用作 VLAN 幹道埠，同時處於 bond 中以建立 LAG 介面。

#### 配置鏈路聚合 {#configure-bonding}

當需要更大頻寬時，使用鏈路聚合介面。這透過建立鏈路聚合組來完成，該組還為交換器提供硬體自動故障轉移和負載均衡。透過將兩個 10Gbps 介面加入鏈路聚合，可以將理論頻寬上限提高到 20Gbps。請確保所有聚合介面都以相同速率連線。

:::info
使用硬體解除安裝網橋時，交換器使用內建交換晶片聚合流量，而不佔用 CPU 資源。
:::

要在 SwitchA 與 SwitchB 之間以及 SwitchC 與 SwitchB 之間，使用 sfp-sfpplus1 和 sfp-sfpplus2 建立 20Gbps 鏈路聚合介面，請在 **SwitchA** 和 **SwitchC** 上使用以下命令：

```ros
/interface/bonding
add mode=802.3ad name=bond_1-2 slaves=sfp-sfpplus1,sfp-sfpplus2
```

要在 SwitchB 與路由器之間建立 40Gbps 鏈路聚合介面，並在 SwitchA 與 SwitchC 之間建立 20Gbps 鏈路聚合介面，請在 **SwitchB** 上使用以下命令：

```ros
/interface/bonding
add mode=802.3ad name=bond_1-2 slaves=sfp-sfpplus1,sfp-sfpplus2
add mode=802.3ad name=bond_3-4 slaves=sfp-sfpplus3,sfp-sfpplus4
add mode=802.3ad name=bond_5-6-7-8 slaves=sfp-sfpplus5,sfp-sfpplus6,sfp-sfpplus7,sfp-sfpplus8
```

在我們的場景中，路由器需要基於軟體的鏈路聚合介面。請在**路由器**上使用以下命令：

```ros
/interface/bonding
add mode=802.3ad name=bond_1-2-3-4 slaves=sfp-sfpplus1,sfp-sfpplus2,sfp-sfpplus3,sfp-sfpplus4
```

:::info
介面聚合不會建立具有更大鏈路速度的介面。介面聚合會建立一個虛擬介面，可以在多個介面上對流量進行負載均衡。更多詳細資訊請參閱 [LAG 介面與負載均衡](./user-guides/layer2-misconfiguration.md#lag-interfaces-and-load-balancing)頁面。
:::

#### 配置埠交換 {#configure-port-switching}

此設定中的所有交換器都要求將所有使用的埠一起交換。對於鏈路聚合，應將鏈路聚合介面作為網橋埠新增，而不是新增各個聚合埠。請在 **SwitchA** 和 **SwitchC** 上使用以下命令：

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

使用以下命令在 **SwitchB** 上將所有鏈路聚合介面新增到單個網橋：

```ros
/interface/bridge
add name=bridge vlan-filtering=no
/interface/bridge/port
add bridge=bridge interface=bond_1-2
add bridge=bridge interface=bond_3-4
add bridge=bridge interface=bond_5-6-7-8
```

#### 配置管理 IP {#configure-management-ip}

建立管理介面併為其分配 IP 地址以保留對交換器的訪問非常有用。這在更新交換器時也非常有用，因為啟用無效 VLAN 過濾時，發往交換器的此類流量將被阻止。

在 **SwitchA**、**SwitchB** 和 **SwitchC** 上建立可路由的 VLAN 介面：

```ros
/interface/vlan
add interface=bridge name=MGMT vlan-id=99
```

路由器需要在鏈路聚合介面上建立可路由的 VLAN 介面。使用以下命令在**路由器**上建立 VLAN 介面：

```ros
/interface/vlan
add interface=bond_1-2-3-4 name=MGMT vlan-id=99
```

本指南將為每臺裝置使用以下地址：

| 裝置 | 地址 |
| :-- | :-- |
| 路由器 | 192.168.99.1 |
| SwitchA | 192.168.99.2 |
| SwitchB | 192.168.99.3 |
| SwitchC | 192.168.99.4 |

在 VLAN 介面上為每臺交換器裝置新增 IP 地址（將 X 改為相應的數字）：

```ros
/ip/address
add address=192.168.99.X/24 interface=MGMT
```

不要忘記在交換器裝置上新增預設閘道器並指定 DNS 伺服器：

```ros
/ip/route
add gateway=192.168.99.1
/ip/dns
set servers=192.168.99.1
```

在**路由器**上新增 IP 地址：

```ros
/ip/address
add address=192.168.99.1/24 interface=MGMT
```

#### 配置無效 VLAN 過濾 {#configure-invalid-vlan-filtering}

由於 SwitchA 和 SwitchC 上的大多數埠將作為接入埠，您可以將所有埠設定為僅接受特定型別的封包；在本例中，我們希望 SwitchA 和 SwitchC 僅接受未標記封包。請在 **SwitchA** 和 **SwitchC** 上使用以下命令：

```ros
/interface/bridge/port
set [ find ] frame-types=admit-only-untagged-and-priority-tagged
```

SwitchA 和 SwitchC 上的幀型別有一個例外。在此設定中，需要從 ether1 和鏈路聚合介面訪問管理。它們要求可以轉發帶標籤流量。請在 **SwitchA** 和 **SwitchC** 上使用以下命令：

```ros
/interface/bridge/port
set [find where interface=ether1] frame-types=admit-all
set [find where interface=bond_1-2] frame-types=admit-only-vlan-tagged
```

在 SwitchB 上應僅轉發帶標籤封包，請在 **SwitchB** 上使用以下命令：

```ros
/interface/bridge/port
set [ find ] frame-types=admit-only-vlan-tagged
```

可選步驟是在網橋介面上設定 `frame-types=admit-only-vlan-tagged`，以停用預設的未標記 VLAN 1（`pvid=1`）。我們使用網橋上的帶標籤 VLAN 進行管理訪問，因此無需在網橋上接受未標記流量。請在 **SwitchA**、**SwitchB** 和 **SwitchC** 上使用以下命令：

```ros
/interface/bridge/set [find name=bridge] frame-types=admit-only-vlan-tagged
```

需要設定網橋 VLAN 表。在此網路設定中，我們需要在 ether1-ether8 上允許 VLAN 10，在 ether9-ether16 上允許 VLAN 20，在 ether17-ether24 上允許 VLAN 30，在 bond\_1-2 上允許 VLAN 10、20、30、99，並且對 ether1 做特殊處理，以允許在 SwitchA 和 SwitchC 上轉發 VLAN 99。請在 **SwitchA** 和 **SwitchC** 上使用以下命令：

```ros
/interface/bridge/vlan
add bridge=bridge tagged=bond_1-2 vlan-ids=10
add bridge=bridge tagged=bond_1-2 vlan-ids=20
add bridge=bridge tagged=bond_1-2 vlan-ids=30
add bridge=bridge tagged=bridge,bond_1-2,ether1 vlan-ids=99
```

:::warning
將 `frame-types` 設定為 `admit-all` 或 `admit-only-untagged-and-priority-tagged` 的網橋埠會自動新增為 `pvid` VLAN 的未標記埠。
:::

同樣，需要為 SwitchB 設定網橋 VLAN 表。請在 **SwitchB** 上使用以下命令：

```ros
/interface/bridge/vlan
add bridge=bridge tagged=bond_1-2,bond_3-4,bond_5-6-7-8 vlan-ids=10,20,30
add bridge=bridge tagged=bond_1-2,bond_3-4,bond_5-6-7-8,bridge vlan-ids=99
```

配置完成後，即可啟用 VLAN 過濾。請在 **SwitchA**、**SwitchB** 和 **SwitchC** 上使用以下命令：

```ros
/interface/bridge
set bridge vlan-filtering=yes
```

:::danger
請仔細檢查基於埠的 VLAN 是否設定正確。如果出錯，您可能會失去對交換器的訪問許可權，只能透過重設配置或使用序列控制檯來恢復連線。
:::

:::note
VLAN 過濾在[網橋 VLAN 過濾](./index.md#bridge-vlan-filtering)章節中有更詳細的描述。
:::

#### 配置 VLAN 間路由 {#configure-intervlan-routing}

要建立 VLAN 間路由，必須在路由器上為每個客戶 VLAN ID 建立 VLAN 介面，並且必須為其分配 IP 地址。VLAN 介面必須建立在先前建立的鏈路聚合介面上。

請在**路由器**上使用以下命令：

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
這些命令是 DHCP 伺服器設定所必需的。如果不希望進行 VLAN 間路由，但需要在單臺路由器上使用 DHCP 伺服器，請使用[防火牆過濾](../firewall-and-quality-of-service/firewall/filter.md)規則阻止不同子網之間的通訊。
:::

:::note
自 RouterOS v7 起，可以在受支援的硬體上使用三層硬體解除安裝來路由流量。更多詳細資訊請參閱[三層硬體解除安裝](./l3-hardware-offloading.md)章節。
:::

#### 配置 DHCP 伺服器 {#configure-dhcp-server}

要讓 DHCP 伺服器為每個 VLAN ID 工作，必須在先前建立的 VLAN 介面上設定伺服器（每個 VLAN ID 一個伺服器）。最好每個 VLAN ID 都有自己的子網和自己的 IP 池。DNS 伺服器可以指定為特定 VLAN ID 的路由器 IP 地址，也可以使用全域性 DNS 伺服器，但該地址必須可達。

要設定 DHCP 伺服器，請在**路由器**上使用以下命令：

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

如果使用路由器的 DNS 伺服器，請不要忘記允許遠端請求，並確保在路由器上配置了 DNS 伺服器。請在**路由器**上使用以下命令：

```ros
/ip/dns
set allow-remote-requests=yes servers=8.8.8.8
```

:::danger
當將 `allow-remote-requests` 設定為 `yes` 時，請確保使用防火牆從外部保護本地 DNS 伺服器，因為如果任何人都可以從 Internet 訪問您的 DNS 伺服器，它可能被用於 DDoS 攻擊。
:::

不要忘記建立 NAT；假設 sfp-sfpplus8 用作 WAN 埠，請在**路由器**上使用以下命令：

```ros
/ip/firewall/nat
add action=masquerade chain=srcnat out-interface=sfp-sfpplus8
```

#### 配置巨型幀 {#configure-jumbo-frames}

在這樣的設定中，可以透過啟用巨型幀來提高總吞吐量。這透過增加最大傳輸單元（MTU）來減少封包開銷。如果網路中的某臺裝置不支援巨型幀，則它不會從更大的 MTU 中受益。通常，整個網路並不都支援巨型幀，但在支援巨型幀的裝置之間傳送資料時（包括路徑中的所有交換器），您仍然可以受益。

在這種情況下，如果 SwitchA 後面的用戶端和 SwitchC 後面的用戶端支援巨型幀，那麼啟用巨型幀將是有益的。在啟用巨型幀之前，使用以下命令確定 MAX-L2MTU：

```ros
[admin@SwitchA] > interface print 
Flags: R - RUNNING
Columns: NAME, TYPE, ACTUAL-MTU, L2MTU, MAX-L2MTU, MAC-ADDRESS
 #   NAME           TYPE   ACTUAL-MTU  L2MTU  MAX-L2MTU  MAC-ADDRESS      
 1 R sfp-sfpplus1   ether        1500   1584      10218  64:D1:54:FF:E3:7F

```

:::info
更多資訊請參閱 [MTU 手冊](../hardware/mtu-in-routeros.md)頁面。
:::

確定 MAX-L2MTU 後，根據網路上的流量選擇 MTU 大小，並在 **SwitchA**、**SwitchB** 和 **SwitchC** 上使用以下命令：

```ros
/interface/ethernet
set [ find ] l2mtu=10218 mtu=10218
```

:::info
不要忘記也更改用戶端裝置上的 MTU，否則上述設定將不會生效。
:::

## 多機箱鏈路聚合組 {#multi-chassis-link-aggregation-group}

---

RouterOS 中的 MLAG（多機箱鏈路聚合組）實現允許在兩臺獨立裝置上配置 LACP bond，而用戶端裝置認為它連線到同一臺機器。這在交換器故障時提供物理冗餘。配備 Marvell Prestera 交換器的 MikroTik 裝置可以配置硬體解除安裝的 MLAG。更多資訊請閱讀[此處](../high-availability-solutions/multi-chassis-link-aggregation-group.md)。

## 三層硬體解除安裝 {#l3-hardware-offloading}

---

三層硬體解除安裝（也稱為 IP 交換或硬體路由）允許將部分路由器功能解除安裝到交換晶片上。這使得在路由封包時能夠達到線速，而這僅靠 CPU 是不可能實現的。

解除安裝功能集取決於所使用的晶片組。更多資訊請閱讀[此處](./l3-hardware-offloading.md)。

## 埠隔離 {#port-isolation}

---

自 RouterOS v6.43 起，可以建立私有 VLAN 設定，示例可在[交換晶片埠隔離](./switch-chip-features.md#port-isolation)手冊頁中找到。硬體解除安裝的鏈路聚合介面不包括在交換器埠隔離選單中，但仍可以在鏈路的每個輔助介面上單獨配置埠隔離。

:::warning
埠隔離可與啟用 vlan-filtering 的網橋一起使用，並且可以隔離屬於同一 VLAN 的埠。隔離按埠生效；無法按 VLAN 隔離埠。
:::

## IGMP/MLD 監聽 {#igmpmld-snooping}

---

配備 Marvell Prestera 交換器的 MikroTik 裝置能夠在硬體層面使用 IGMP/MLD Snooping。要檢視更詳細的資訊，請檢視 [網橋 IGMP/MLD 偵聽](./user-guides/bridge-igmp-mld-snooping.md)手冊頁。

## DHCP Snooping 與 DHCP Option 82 {#dhcp-snooping-and-dhcp-option-82}

---

配備 Marvell Prestera 交換器的 MikroTik 裝置能夠在硬體層面使用帶自定義 Option 82（Circuit ID、Remote ID）的 DHCP Snooping。交換器會建立動態 ACL 規則來捕獲 DHCP 封包，並將其重定向到主 CPU 以進行進一步處理。要檢視更詳細的資訊，請訪問 [DHCP Snooping 與 DHCP Option 82](./index.md#dhcp-snooping-and-dhcp-option-82)手冊頁。

:::info
從 RouterOS v7.17 開始，DHCP snooping 支援硬體解除安裝的鏈路聚合介面。
:::

## DHCPv6 Snooping 與 DHCP Option 18、Option 37 {#dhcpv6-snooping-and-dhcp-option-18-option-37}

---

自 RouterOS v7.23 起，配備 Marvell Prestera 交換器的 MikroTik 裝置能夠在硬體層面使用帶自定義 Option 18（Interface ID）和 Option 37（Remote ID）的 DHCPv6 Snooping。交換器會建立動態 ACL 規則來捕獲 DHCPv6 封包，並將其重定向到主 CPU 以進行進一步處理。要檢視更詳細的資訊，請訪問 [DHCPv6 Snooping / DHCPv6 Shield](./index.md#dhcpv6-snooping--dhcpv6-shield)手冊頁。

## RA 防護 {#ra-guard}

---

自 RouterOS v7.22 起，配備 Marvell Prestera 交換器的 MikroTik 裝置能夠在硬體層面使用 RA Guard。交換器會建立動態 ACL 規則來捕獲相關 IPv6 封包，並將其重定向到主 CPU 以進行進一步處理。要檢視更詳細的資訊，請訪問 [RA Guard](./index.md#ra-guard)手冊頁。

## 映象 {#mirroring}

---

映象是允許網路交換器複製透過它的所有資料，並將副本傳送到另一個指定埠（稱為 `mirror-target`）的功能。此功能對於設定分流裝置很有用，可透過單獨的裝置分析網路流量。您可以透過指定源埠以簡單方式設定映象（請參閱 `/interface/ethernet/switch/port` 中的 `mirror-egress` 和 `mirror-ingress`），也可以根據不同條件配置更高階的映象（請參閱 `/interface/ethernet/switch/rule` 中的 `mirror`）。

需要注意的是，`mirror-target` 埠必須位於同一交換器上。您可以檢視裝置框圖，或導航到 `/interface/ethernet` 選單，以確定哪些介面連線到哪裡。在設定配置時，不必將 `mirror-target` 介面新增到設定源埠的同一硬體解除安裝網橋。`mirror-target` 埠可以是獨立介面（未配置為網橋埠），也可以位於網橋設定中。在將 `mirror-target` 與網橋一起使用時，請注意資料和映象流量可能都在同一 LAN 上傳輸。在這種情況下，請考慮使用 RSPAN（遠端交換器埠分析器），其中映象流量在透過網路傳輸之前被封裝到單獨的 VLAN 中。

此外，您可以將 `mirror-target` 埠設定為特殊值 "cpu"，這意味著複製的封包將被髮送到交換晶片的 CPU 埠。

### 配置示例 {#configuration-examples}

---

#### 基於埠的映象 {#port-based-mirroring}

從 RouterOS 7.15 版本開始，可以配置多個源埠，並選擇性選擇映象傳入流量、傳出流量或兩者。在此示例中，來自 **ether2** 介面的傳入和傳出流量都將被複制併發送到 **ether3** 介面以進行監控或分析。

```ros
# 自 RouterOS v7.15 起
/interface/ethernet/switch/port
set ether2 mirror-egress=yes mirror-ingress=yes
/interface/ethernet/switch
set switch1 mirror-target=ether3

# 较旧的 RouterOS：
/interface/ethernet/switch
set switch1 mirror-source=ether2 mirror-target=ether3
```

#### 基於 VLAN 的映象 {#vlan-based-mirroring}

使用 ACL 規則，可以透過 `ports` 設定映象來自多個介面的封包。此外，還可以指定更詳細的條件，例如 VLAN ID、MAC/IP 地址或 TCP/UDP 埠。只有**入口**封包會被映象到 `mirror-target` 介面。此示例將映象來自 **ether2** 介面的傳入 VLAN 11 流量，並將副本傳送到 **ether3** 介面。要使用帶 `vlan-id` 匹配器的 ACL 規則，需要啟用[網橋 vlan-filtering](./index.md#bridge-vlan-filtering)。

```ros
/interface/bridge
set bridge1 vlan-filtering=yes
/interface/ethernet/switch
set switch1 mirror-target=ether3
/interface/ethernet/switch/rule
add mirror=yes ports=ether1 switch=switch1 vlan-id=11
```

#### 基於 MAC 的映象 {#mac-based-mirroring}

此示例將映象來自 **ether1** 介面且具有 64:D1:54:D9:27:E6 MAC 目標地址或源地址的傳入流量，並將副本傳送到 **ether3** 介面。

```ros
/interface/ethernet/switch
set switch1 mirror-target=ether3
/interface/ethernet/switch/rule
add mirror=yes ports=ether1 switch=switch1 dst-mac-address=64:D1:54:D9:27:E6/FF:FF:FF:FF:FF:FF
add mirror=yes ports=ether1 switch=switch1 src-mac-address=64:D1:54:D9:27:E6/FF:FF:FF:FF:FF:FF
```

#### 基於 IP 的映象 {#ip-based-mirroring}

此示例將映象來自 **ether1** 介面且 IP 目標地址或源地址為 192.168.88.0/24 的傳入流量，並將副本傳送到 **ether3** 介面。

```ros
/interface/ethernet/switch
set switch1 mirror-target=ether3 mirror-source=none
/interface/ethernet/switch/rule
add mirror=yes ports=ether1 switch=switch1 src-address=192.168.88.0/24
add mirror=yes ports=ether1 switch=switch1 dst-address=192.168.88.0/24
```

還有其他選項，請檢視 [ACL 章節](./marvell-prestera-switch-chip-features.md#switch-rules-acl)以瞭解可用於匹配封包的所有可能引數。

#### 遠端交換器埠分析器 {#remote-switch-port-analyzer}

此示例將映象來自 **ether2** 介面的傳入和傳出流量，副本將使用 999 作為 VLAN ID 封裝在 802.1Q VLAN 中，封包將被髮送到 **ether3** 介面。如果原始流量已帶有 VLAN 標籤，RSPAN 將再新增一層 VLAN 標籤作為外層標籤。這會導致映象流量被標記兩次。如果 `mirror-target` 埠包含在啟用 vlan-filtering 的網橋中，則無需在 RSPAN 的 `/interface/bridge/vlan` 選單下將該介面設為帶標籤 VLAN 成員。

```ros
/interface/ethernet/switch/port
set ether2 mirror-egress=yes mirror-ingress=yes
/interface/ethernet/switch
set switch1 mirror-target=ether3 rspan=yes rspan-egress-vlan-id=999 rspan-ingress-vlan-id=999
```

### 屬性參考 {#property-reference}

**子選單：** `/interface/ethernet/switch`

| 屬性 | 描述 |
| :-- | :-- |
| **mirror-target** (*cpu \| name \| none*; 預設值：**none**) | 選擇單個映象目標埠。來自 `mirror-egress` 和 `mirror-ingress`（`/interface/ethernet/switch/port`）以及 mirror（`/interface/ethernet/switch/rule`）的封包將被髮送到所選埠。 |
| **rspan** (*no \| yes*; 預設值：**no**) | 在 `mirror-target` 上啟用遠端交換器埠分析器（RSPAN）功能。標記為入口或出口映象的流量透過指定的遠端分析器 VLAN 承載 - `rspan-egress-vlan-id` 和 `rspan-ingress-vlan-id`。 |
| **rspan-egress-vlan-id** (*integer: 1..4095*; 預設值：**1**) | 選擇標記的出口流量的 VLAN ID。僅在啟用 `rspan` 時適用。 |
| **rspan-ingress-vlan-id** (*integer: 1..4095*; 預設值：**1**) | 選擇標記的入口流量的 VLAN ID。僅在啟用 `rspan` 時適用。 |

**子選單：** `/interface/ethernet/switch/port`

| 屬性 | 描述 |
| :-- | :-- |
| **mirror-egress** (*no \| yes*; 預設值：**no**) | 是否將出口封包副本傳送到 `mirror-target` 埠。 |
| **mirror-ingress** (*no \| yes*; 預設值：**no**) | 是否將入口封包副本傳送到 `mirror-target` 埠。 |

**子選單：** `/interface/ethernet/switch/rule`

| 屬性 | 描述 |
| :-- | :-- |
| **mirror** (*no \| yes*; 預設值：**no**) | 是否將封包副本傳送到 `mirror-target` 埠。 |

## 流量整形 {#traffic-shaping}

---

可以使用 ACL 規則限制匹配特定引數的入口流量，也可以按埠限制入口/出口流量。策略器用於入口流量，整形器用於出口流量。入口策略器透過丟棄封包來控制接收的流量。所有超過定義限制的內容都會被丟棄。這可能影響端主機上的 TCP 擁塞控制機制，實際達到的頻寬可能小於定義值。出口整形器會嘗試將超過限制的封包排隊，而不是丟棄它們。最終，當輸出佇列滿時它也會丟棄封包；不過，它應能更好地利用定義的吞吐量。

### 基於埠的流量策略和整形 {#port-based-traffic-police-and-shaper}

```ros
/interface/ethernet/switch/port
set ether1 ingress-rate=10M egress-rate=5M
```

### 基於 MAC 的流量策略器 {#mac-based-traffic-policer}

```ros
/interface/ethernet/switch/rule
add ports=ether1 switch=switch1 src-mac-address=64:D1:54:D9:27:E6/FF:FF:FF:FF:FF:FF rate=10M
```

### 基於 VLAN 的流量策略器 {#vlan-based-traffic-policer}

```ros
/interface/bridge
set bridge1 vlan-filtering=yes
/interface/ethernet/switch/rule
add ports=ether1 switch=switch1 vlan-id=11 rate=10M
```

:::danger
啟用 `vlan-filtering` 後，您將過濾掉髮往 CPU 的流量。在啟用 VLAN 過濾之前，應確保已設定[管理埠](./index.md#management-access-configuration)。
:::

### 基於協定的流量策略器 {#protocol-based-traffic-policer}

```ros
/interface/ethernet/switch/rule
add ports=ether1 switch=switch1 mac-protocol=ipx rate=10M
```

還有其他選項，請檢視 [ACL 章節](./marvell-prestera-switch-chip-features.md#switch-rules-acl)以瞭解可用於匹配封包的所有可能引數。

:::warning
交換器規則表用於 QoS 功能。請參閱[此表](./marvell-prestera-switch-chip-features.md#models)瞭解每臺裝置支援多少條規則。
:::

:::danger
由於硬體限制，當 10Gbps 交換器埠以 10/100Mbps、1/2.5/5Gbps 連線時，`egress-rate` 和 `storm-rate` 設定無法正常工作。這適用於 98DX224S、98DX226S、98DX2528、98DX3236 交換晶片。
:::

## 流量風暴控制 {#traffic-storm-control}

---

自 RouterOS v6.42 起，可以啟用流量風暴控制。當某些幀在網路中被持續泛洪時，可能出現流量風暴。風暴控制設定通常配置在非上行埠上，以限制這些特定埠上的傳入風暴流量。這透過最小化流量風暴對整個網路的影響來幫助保護整個交換器及其連線的埠。

例如，如果建立了網路環路且未使用環路避免機制（例如[生成樹協定](./user-guides/spanning-tree-protocol.md)），廣播或組播幀可能迅速淹沒網路，導致網路效能下降甚至網路完全崩潰。使用配備 Marvell Prestera 交換器的 MikroTik 裝置，可以限制廣播、未知組播和未知單播流量。當交換器不包含目標 MAC 地址的主機條目時，視為未知單播流量。當交換器在 `/interface/bridge/mdb` 選單中不包含組播組條目時，視為未知組播流量。風暴控制設定應應用於入口埠；出口流量將受到限制。

![Traffic Storm](/img/f275b4060eca4083.webp)

:::warning
風暴控制引數指定為鏈路速度的百分比（%）。如果鏈路速度為 1Gbps，則將 `storm-rate` 指定為 `10` 將僅允許 100Mbps 的廣播、未知組播和/或未知單播流量被轉發。
:::

**子選單：** `/interface/ethernet/switch/port`

| 屬性 | 描述 |
| :-- | :-- |
| **limit-broadcasts** (*yes \| no*; 預設值：**yes**) | 限制交換器埠上的廣播流量。 |
| **limit-unknown-multicasts** (*yes \| no*; 預設值：**no**) | 限制交換器埠上的未知組播流量。 |
| **limit-unknown-unicasts** (*yes \| no*; 預設值：**no**) | 限制交換器埠上的未知單播流量。 |
| **storm-rate** (*integer 0..100*; 預設值：**100**) | 廣播、未知組播和/或未知單播流量限制為鏈路速度的百分比。 |

:::danger
配備 98DX224S、98DX226S、98DX2528、98DX3236 交換晶片的裝置無法區分未知組播流量與所有組播流量。例如，CRS326-24G-2S+ 在使用 `limit-unknown-multicasts` 和 `storm-rate` 時將限制所有組播流量。對於其他裝置，例如 CRS317-1G-16S+，`limit-unknown-multicasts` 引數將僅限制未知組播流量（地址未出現在 `/interface/bridge/mdb` 中）。
:::

例如，要將 ether1（1Gbps）上的廣播和未知單播流量限制為 1%（10Mbps），請使用以下命令：

```ros
/interface/ethernet/switch/port
set ether1 storm-rate=1 limit-broadcasts=yes limit-unknown-unicasts=yes
```

:::warning
由於硬體限制，當 10Gbps 交換器埠以 10/100Mbps、1/2.5/5Gbps 連線時，`egress-rate` 和 `storm-rate` 設定無法正常工作。這適用於 98DX224S、98DX226S、98DX2528、98DX3236 交換晶片。
:::

## MPLS 硬體解除安裝 {#mpls-hardware-offloading}

---

自 RouterOS v6.41 起，可以將某些 MPLS 功能解除安裝到交換晶片。交換器必須在 PE-P-PE 設定中作為 Provider 路由器，才能實現硬體解除安裝。設定示例可在 [LDP 示例設定](../user-guides/routing-and-networking-protocols/mpls/ldp.md#example-setup)中找到。僅當 LDP 介面配置為物理交換器介面（例如乙太網、SFP、SFP+）時，才會進行硬體解除安裝。

:::warning
目前，只有使用 RouterOS v6.41 及更新版本的 `CRS317-1G-16S+` 和 `CRS309-1G-8S+` 能夠硬體解除安裝某些 MPLS 功能。`CRS317-1G-16S+` 和 `CRS309-1G-8S+` 的內建交換晶片無法從封包中彈出 MPLS 標籤；在 PE-P-PE 設定中，您必須使用顯式 null 或停用 MPLS 網路中的 TTL 傳播，才能實現硬體解除安裝。

**注意：** 自 RouterOS v7 起，MPLS 硬體解除安裝已被移除。
:::

## 交換器規則（ACL） {#switch-rules-acl}

---

訪問控制列表包含入口策略引擎和出口策略引擎。請參閱[此表](./marvell-prestera-switch-chip-features.md#models)瞭解每臺裝置支援多少條規則。它是一種高階工具，可基於二層、三層和四層協定頭欄位條件進行線速封包過濾、轉發和修改。

對每個接收到的封包檢查 ACL 規則，直到找到匹配項。如果有多個規則可以匹配，則只會觸發第一個規則。沒有任何動作引數的規則是接受封包的規則。

啟用 IGMP snooping、DHCP snooping、RoMON、PTP 或 loop-protect 等功能會自動建立動態 ACL 規則。新增新的 ACL 條目時應考慮這些規則。建立新規則時使用 `place-before` 屬性，或使用 `move` 命令調整 ACL 規則順序。

:::warning
使用 L3 或 L4 匹配器時，不需要將 `mac-protocol` 設定為特定 IP 版本；但是，在過濾任何 IP 封包時，建議設定 `mac-protocol=ip` 或 `mac-protocol=ipv6`。
:::

:::danger
修改交換器 ACL 規則時（例如新增、刪除、停用、啟用或移動），現有交換器規則會在短時間內處於非活動狀態。這可能在 ACL 規則修改期間導致一些封包洩漏。
:::

**子選單：** `/interface/ethernet/switch/rule`

| 屬性 | 描述 |
| :-- | :-- |
| **copy-to-cpu** (*no \| yes*; Default: **no**) | 克隆匹配的封包並將其傳送到 CPU。 |
| **disabled** (*yes \| no*; Default: **no**) | 啟用或停用 ACL 條目。 |
| **dscp** (*0..63*) | 匹配封包的 DSCP 欄位（僅適用於 IPv4 封包）。 |
| **dst-address** (*IP address/Mask*) | 匹配目標 IPv4 地址和掩碼。如果指定了 `mac-protocol=arp`，則匹配 ARP 封包中的目標 IP。未指定 `mac-protocol` 時，僅匹配 IPv4 封包。 |
| **dst-address6** (*IPv6 address/Mask*) | 匹配目標 IPv6 地址和掩碼。 |
| **dst-mac-address** (*MAC address/Mask*) | 匹配目標 MAC 地址和掩碼。 |
| **dst-port** (*0..65535*) | 匹配目標協定埠號（如果未指定 `mac-protocol`，則適用於 IPv4 和 IPv6 封包）。 |
| **flow-label** (*0..1048575*) | 匹配 IPv6 流標籤。 |
| **mac-protocol** (*802.2 \| arp \| capsman \| dot1x \| homeplug-av \| ip \| ipv6 \| ipx \| lacp \| lldp \| loop-protect \| macsec \| mpls-multicast \| mpls-unicast \| mvrp \| packing-compr \| packing-simple \| pppoe \| pppoe-discovery \| rarp \| romon \| service-vlan \| vlan \| or 0..65535 \| or 0x0000-0xffff*) | 匹配由協定名稱或編號指定的特定 MAC 協定 |
| **mirror** (*no \| yes*) | 克隆匹配的封包並將其傳送到 mirror-target 埠。 |
| **new-dst-ports** (*ports \| bond \| all*) | 將目標埠更改為指定值： <br/><ul><li>如果該設定為空（例如 <code>new-dst-ports=""</code>），封包將被丟棄；</li><li>如果指定了埠或 [ hardware-offloaded bonding ](./marvell-prestera-switch-chip-features.md)介面，封包將被重定向到該埠。僅支援單個埠或 bond 介面；</li><li>如果使用 <code>all</code> 引數，將允許封包進入出口處理而不會被丟棄；</li><li>如果未使用此引數，封包將按原樣接受。</li></ul> |
| **new-vlan-id** (*0..4095*) | 將 VLAN ID 更改為指定值。需要 `vlan-filtering=yes`。 |
| **new-vlan-priority** (*0..7*) | 更改 VLAN 優先順序（優先順序程式碼點）。需要 `vlan-filtering=yes`。 |
| **new-vrf** (*vrf name*) | 將入口流量分配到指定的 VRF。需要交換器晶片支援 [硬體解除安裝 VRF](./l3-hardware-offloading.md#l3hw-feature-support)。在 VRF-unaware 交換器（98DX3xxx 和 98DX2xxx 系列）上，將 `new-vrf` 設定為 `main` 以外的任何值都將被視為 `redirect-to-cpu=yes`。 |
| **ports** (*ports \| bond*) | 匹配規則將應用於入站流量的交換器介面。可以選擇多個埠和 [hardware-offloaded bonding](./marvell-prestera-switch-chip-features.md#bonding) 介面。請注意，無法選擇 `switch1-cpu` 埠。如果 `ports` 屬性留空，則規則將應用於所有交換器介面。 |
| **protocol** (*dccp \| ddp \| egp \| encap \| etherip \| ggp \| gre \| hmp \| icmp \| icmpv6 \| idpr-cmtp \| igmp \| ipencap \| ipip \| ipsec-ah \| ipsec-esp \| ipv6 \| ipv6-frag \| ipv6-nonxt \| ipv6-opts \| ipv6-route \| iso-tp4 \| l2tp \| ospf \| pim \| pup \| rdp \| rspf \| rsvp \| sctp \| st \| tcp \| udp \| udp-lite \| vmtp \| vrrp \| xns-idp \| xtp \| or 0..255*) | 匹配由協定名稱或編號指定的特定 IP 協定。僅在未指定 `mac-protocol` 時適用於 IPv4 封包。要匹配某些 IPv6 協定，請使用 `mac-protocol=ipv6` 設定。 |
| **rate** (*0..4294967295*) | 為匹配的流量設定入口流量限制（位元每秒）。 |
| **redirect-to-cpu** (*no \| yes*) | 將匹配封包的目標埠更改為 CPU。 |
| **src-address** (*IP address/Mask*) | 匹配源 IPv4 地址和掩碼。如果指定了 `mac-protocol=arp`，則匹配 ARP 封包中的源 IP。未指定 `mac-protocol` 時，僅匹配 IPv4 封包。 |
| **src-address6** (*IPv6 address/Mask*) | 匹配源 IPv6 地址和掩碼。 |
| **src-mac-address** (*MAC address/Mask*) | 匹配源 MAC 地址和掩碼。 |
| **src-port** (*0..65535*) | 匹配源協定埠號（如果未指定 `mac-protocol`，則適用於 IPv4 和 IPv6 封包）。 |
| **switch** (*switch group*) | 匹配規則將應用於的交換器組。 |
| **traffic-class** (*0..255*) | 匹配 IPv6 流量類別。 |
| **vlan-id** (*0..4095*) | 匹配 VLAN ID。需要 `vlan-filtering=yes`。 |
| **vlan-header** (*not-present \| present*) | 匹配 VLAN 頭，無論 VLAN 頭是否存在。需要 `vlan-filtering=yes`。 |
| **vlan-priority** (*0..7*) | 匹配 VLAN 優先順序（優先順序程式碼點）。 |

### 動作引數 {#action-parameters}

- copy-to-cpu
- redirect-to-cpu
- mirror
- new-dst-ports（可用於丟棄封包）
- new-vlan-id
- new-vlan-priority
- new-vrf
- rate

### 二層條件引數 {#layer2-condition-parameters}

- dst-mac-address
- mac-protocol
- src-mac-address
- vlan-id
- vlan-header
- vlan-priority

### 三層條件引數 {#layer3-condition-parameters}

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

### 四層條件引數 {#layer4-condition-parameters}

- dst-port
- src-port

:::warning
要使 VLAN 相關匹配器或 VLAN 相關動作引數生效，需要在網橋介面上啟用 `vlan-filtering`，並確保這些埠上啟用了硬體解除安裝，否則這些引數將不會產生任何效果。
:::
:::warning
當網橋介面 `ether-type` 設定為 `0x8100` 時，VLAN 相關 ACL 規則適用於使用常規/客戶 VLAN（TPID 0x8100）標記的幀；這包括 `vlan-id` 和 `new-vlan-id`。當網橋介面 `ether-type` 設定為 `0x88a8` 時，ACL 規則適用於帶有 802.1ad 服務標籤（TPID 0x88a8）的幀。
:::

### 規則計數器 {#rule-counters}

每條 ACL 規則都會統計其匹配的封包和位元組數。這些計數器可用於驗證規則是否按預期工作以及它處理多少流量。

預設 `print` 命令不會顯示計數器，請在 `/interface/ethernet/switch/rule` 選單中使用 `print stats` 顯示它們：

```ros
[admin@MikroTik] > /interface/ethernet/switch/rule/print stats
Columns: SWITCH, COPY-TO-CPU, REDIRECT-TO-CPU, BYTES, PACKETS
# SWITCH   COPY-TO-CPU  REDIRECT-TO-CPU  BYTES  PACKETS
;;; count incoming ICMP
0 switch1  yes          no               68716      366
;;; drop ICMP to 192.168.99.1
1 switch1  no           no                   0        0
```

在本示例中，第一條規則已匹配 366 個數據包（68716 位元組），而第二條規則尚未匹配任何流量。

使用 `reset-counters` 命令清除所選規則的計數器，或使用 `reset-counters [find]` 一次性清除所有規則的計數器：

```ros
[admin@MikroTik] > /interface/ethernet/switch/rule/reset-counters 0
```

## 埠安全 {#port-security}

---

可以限制單個交換器埠上允許的 MAC 地址。例如，要允許交換器埠上的 64:D1:54:81:EF:8E MAC 地址，首先將多個埠交換在一起。在此示例中，64:D1:54:81:EF:8E 將位於 **ether1** 後面。

建立 ACL 規則以允許給定 MAC 地址，並丟棄 **ether1** 上的所有其他流量（對於入口流量）：

```ros
/interface/ethernet/switch/rule
add ports=ether1 src-mac-address=64:D1:54:81:EF:8E/FF:FF:FF:FF:FF:FF switch=switch1
add new-dst-ports="" ports=ether1 switch=switch1
```

出口流量仍可能包含不應到達未知 MAC 地址裝置的資訊。  
假設埠已交換，請在 **ether1** 上停用 MAC 學習和未知單播泛洪：

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether1 hw=yes learn=no unknown-unicast-flood=no
add bridge=bridge1 interface=ether2 hw=yes
```

停用 MAC 學習後，需要為 64:D1:54:81:EF:8E 新增靜態主機條目（用於出口流量）：

```ros
/interface/bridge/host
add bridge=bridge1 interface=ether1 mac-address=64:D1:54:81:EF:8E
```

:::warning
廣播和組播流量仍會從 **ether1** 發出。您可以使用 `broadcast-flood` 和 `unknown-multicast-flood` 引數來阻止它。請注意，某些解決方案可能依賴這些設定，例如流媒體協定和 DHCP。
:::

## 雙啟動 {#dual-boot}

---

“雙啟動”功能允許您選擇希望在 CRS3xx 系列交換器上使用的作業系統：RouterOS 或 SwOS。可以使用以下方式更改裝置作業系統：

- 命令列（`/system/routerboard/settings/set boot-os=swos`）
- Winbox
- Webfig
- 序列控制檯

有關 SwOS 的更多詳細資訊，請參見：[SwOS 手冊](https://help.mikrotik.com/docs/display/SWOS/SwOS)。

:::warning
要檢查某型號是否支援啟動到 SwOS，請參閱 [SwOS 型號表](https://help.mikrotik.com/docs/spaces/SWOS/pages/76415036/CRS3xx+and+CSS3xx+series+Manual#CRS3xxandCSS3xxseriesManual-Models)以及產品頁面“規格”下的“作業系統”。
:::

## 使用 RouterOS 配置 SwOS {#configuring-swos-using-routeros}

---

自 RouterOS 6.43 起，可以使用 RouterOS 為 CRS3xx 系列交換器載入、儲存和重設 SwOS 配置，以及升級 SwOS 和設定 IP 地址：

- 使用 `/system/swos/save-config` 儲存配置。

:::warning
配置將儲存在同一裝置上，檔名為 `swos.config`。請確保從裝置下載該檔案，因為配置檔案將在重啟後被刪除。
:::

- 使用 `/system/swos/load-config` 載入配置。
- 使用 `/system/swos/password` 更改密碼。
- 使用 `/system/swos/reset-config` 重設配置。
- 使用 `/system/swos/upgrade` 從 RouterOS 升級 SwOS。

:::warning
升級命令將自動安裝最新的可用 SwOS 主備份版本；請確保您的裝置可以訪問 Internet，以便升級過程正常執行。當裝置啟動到 SwOS 時，版本號將包含字母 "p"，表示主備份版本。然後，您可以從 SwOS 的“升級”選單安裝最新的可用 SwOS 次主版本。
:::

:::warning
從 RouterOS 7.17 版本開始，device-mode 限制雙啟動的 SwOS/RouterOS 切換；要啟用：`/system/device-mode/update routerboard=yes`
:::

| 屬性 | 描述 |
| :-- | :-- |
| **address-acquisition-mode** (*dhcp-only \| dhcp-with-fallback \| static*; 預設值：**dhcp-with-fallback**) | 更改地址獲取方法：dhcp-only - 僅使用 DHCP 用戶端獲取地址  dhcp-with-fallback - 在前 10 秒內，它將嘗試使用 DHCP 用戶端獲取地址。如果請求不成功，則地址回退到由 static-ip-address 屬性定義的靜態地址  static - 地址按 static-ip-address 屬性定義設定 |
| **allow-from** (*IP/Mask*; 預設值：**0.0.0.0/0**) | 可訪問交換器的 IP 地址或網路。預設情況下，交換器可由任何 IP 地址訪問。 |
| **allow-from-ports** (*name*; 預設值：) | 可訪問裝置的交換器埠列表。預設情況下，允許所有埠訪問交換器 |
| **allow-from-vlan** (*integer: 0..4094*; 預設值：**0**) | 可訪問裝置的 VLAN ID。預設情況下，允許所有 VLAN |
| **identity** (*name*; 預設值：**Mikrotik**) | 交換器名稱（用於 Mikrotik 鄰居發現協定） |
| **static-ip-address** (*IP*; 預設值：**192.168.88.1**) | 當 address-acquisition-mode 設定為 dhcp-with-fallback 或 static 時交換器的 IP 地址。透過設定靜態 IP 地址，地址獲取過程不會改變，預設仍為帶回退的 DHCP。這意味著配置的靜態 IP 地址僅在同一個廣播域中沒有 DHCP 伺服器時才會生效 |

## 另請參閱 {#see-also}

[基本 VLAN 交換](./user-guides/basic-vlan-switching.md)

[網橋硬體解除安裝](./index.md#bridge-hardware-offloading)

[L3HW 路由硬體解除安裝](./l3-hardware-offloading.md)

[服務質量](./quality-of-service.md)

[生成樹協定](./user-guides/spanning-tree-protocol.md)

[RouterBOARD 上的 MTU](../hardware/mtu-in-routeros.md)

[二層錯誤配置](./user-guides/layer2-misconfiguration.md)

[網橋 VLAN 表](./user-guides/bridge-vlan-table.md)

[網橋 IGMP/MLD snooping](./user-guides/bridge-igmp-mld-snooping.md)

[多機箱鏈路聚合組](../high-availability-solutions/multi-chassis-link-aggregation-group.md)
