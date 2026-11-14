---
sidebar_key: "bridging-and-switching/switch-chip-features"
sidebar_position: 7
title: "交換器晶片功能"
sidebar_label: "交換器晶片功能"
description: "本頁介紹 MikroTik RouterOS 交換器晶片功能，詳細說明各型號所支援的功能（如埠交換和映象），以及在頻寬控制和 VLAN 配置方面的限制。"
tags:
  - 'switch-chip'
  - 'port-mirroring'
  - 'vlan'
source: https://manual.mikrotik.com/docs/7.25/bridging-and-switching/switch-chip-features
captured_at: '2026-11-04T11:14:31+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

---

有多種型別的 RouterBOARD 上的交換晶片，它們具有不同的功能集。

:::info
Cloud Router Switch (CRS) 系列裝置內建了非常先進的交換晶片。它們支援多種功能。對於搭載 Marvell Prestera 交換晶片的 MikroTik 裝置（例如 CRS3xx），請參閱 [Marvell Prestera 交換晶片功能](./marvell-prestera-switch-chip-features.md) 手冊。有關 CRS1xx/CRS2xx 系列裝置交換晶片功能的更多詳細資訊，請檢視 [CRS1xx/CRS2xx 系列交換器](./user-guides/crs1xx-2xx-series-switches-examples.md) 手冊。
:::

| 交換晶片 | 埠交換 | 埠映象 | TX 限制¹ | RX 限制¹ | 主機表 | VLAN 表² | 規則表 |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 88E6393X | ✓ | ✓ | ✓ | ✓ | 最多 16K | 最多 4K | 最多 256 條規則 |
| 88E6191X, 88E6190 | ✓ | ✓ | ✓ | ✓ | 最多 16K | 最多 4K | ✗ |
| MT7621, MT7531, RTL8367 | ✓ | ✓ | ✓ | ✓ | 最多 2K | 最多 4K | ✗ |
| EN7523 | ✓ | ✓ | ✓ | ✓ | 最多 1K | 最多 4K | ✗ |
| QCA8337, Atheros8327 | ✓ | ✓ | ✓ | ✓ | 最多 2K | 最多 4K | 最多 92 條規則 |
| Atheros8316 | ✓ | ✓ | ✓ | ✗ | 最多 2K | 最多 4K | 最多 32 條規則 |
| Atheros8227 | ✓ | ✓ | ✓ | ✗ | 最多 1K | 最多 4K | ✗ |
| Atheros7240 | ✓ | ✓ | ✓ | ✗ | 最多 2K | 16 | ✗ |
| ICPlus175D | ✓ | ✓ | ✗ | ✗ | 最多 2K | ✗ | ✗ |
| IPQ-PPE | ✓ | ✗ | ✗ | ✗ | 最多 2K | ✗ | ✗ |
| PIPE 98PX1012, QCA8386 | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |

1. 對於 RTL8367、88E6393X、88E6191X、88E6190、MT7621、MT7531 和 EN7523，可透過 `/interface/ethernet/switch/port` 選單中的 `egress-rate` 和 `ingress-rate` 屬性更改 Tx/Rx 速率限制。對於 QCA8337、Atheros8327、Atheros8316、Atheros8227 和 Atheros7240，可透過 `/interface/ethernet` 選單中的 `bandwidth` 屬性更改 Tx/Rx 速率限制，更多詳細資訊請參閱 [Ethernet 手冊](../wired-connections/ethernet.md)。
2. 對於 88E6393X、88E6191X、88E6190、MT7621、MT7531、EN7523、RTL8367 交換晶片，VLAN 表透過 `/interface/bridge` 選單使用 [網橋硬體 vlan-filtering](./index.md#bridge-vlan-filtering) 進行配置。對於其他支援 VLAN 表的交換器，請參閱 [VLAN 表](./switch-chip-features.md#vlan-table)，並使用 `/interface/ethernet/switch/vlan` 選單配置 VLAN 表。

| RouterBoard | 交換晶片說明 |
| :-- | :-- |
| **MA53UG+HbeH (hAP be³ Media)** | QCA8386 (ether2-ether5) |
| **C52iG-5HaxD2HaxD-TC (hAP ax²), C53UiG+5HPaxD2HPaxD (hAP ax³), Chateau ax 系列** | IPQ-PPE (ether1-ether5) |
| **cAPGi-5HaxD2HaxD (cAP ax)** | IPQ-PPE (ether1-ether2) |
| **L009 系列** | 88E6190 (ether2-ether8, sfp1) |
| **RB5009 系列** | 88E6393X (ether1-ether8, sfp-sfpplus1) |
| **CCR2004-16G-2S+** | 88E6191X (ether1-ether8); 88E6191X (ether9-ether16); |
| **RB4011iGS+** | RTL8367 (ether1-ether5); RTL8367 (ether6-ether10); |
| **RB1100AHx4** | RTL8367 (ether1-ether5); RTL8367 (ether6-ether10); RTL8367 (ether11-ether13) |
| **L41G-2axD (hAP ax lite)** | MT7531 (ether1-ether4) |
| **RB750Gr3 (hEX), RB760iGS (hEX S)** | MT7621 (ether1-ether5) |
| **E50UG (hEX Refresh)** | EN7523 (ether2-ether5) |
| **RBM33G** | MT7621 (ether1-ether3) |
| **RB3011 系列** | QCA8337 (ether1-ether5); QCA8337 (ether6-ether10) |
| **RB OmniTik ac 系列** | QCA8337 (ether1-ether5) |
| **RBwsAP-5Hac2nD (wsAP ac lite)** | Atheros8227 (ether1-ether3) |
| **RB941-2nD (hAP lite)** | Atheros8227 (ether1-ether4) |
| **RB951Ui-2nD (hAP); RB952Ui-5ac2nD (hAP ac lite); RB750r2 (hEX lite); RB750UPr2 (hEX PoE lite); RB750P-PBr2 (PowerBox); RB750P r2; RBOmniTikU-5HnDr2 (OmniTIK 5); RBOmniTikUPA-5HnDr2 (OmniTIK 5 PoE)** | Atheros8227 (ether1-ether5) |
| **RB750Gr2 (hEX); RB962UiGS-5HacT2HnT (hAP ac); RB960PGS (hEX PoE); RB960PGS-PB (PowerBox Pro)** | QCA8337 (ether1-ether5) |
| **RB953GS** | Atheros8327 (ether1-ether3+sfp1) |
| **RB850Gx2** | Atheros8327 (ether1-ether5)，ether1 可選 |
| **RB2011 系列** | Atheros8327 (ether1-ether5+sfp1); Atheros8227 (ether6-ether10) |
| **RB750GL; RB751G-2HnD; RB951G-2HnD; RBD52G-5HacD2HnD (hAP ac²), RBD53iG-5HacD2HnD (hAP ac³), RBD53GR-5HacD2HnD&R11e-LTE6 (hAP ac³ LTE6 kit), RBD53G-5HacD2HnD-TC&EG12-EA (Chateau LTE12)** | Atheros8327 (ether1-ether5) |
| **RBcAPGi-5acD2nD (cAP ac), RBwAPGR-5HacD2HnD (wAP R ac 和 wAP ac LTE 系列), RBwAPG-5HacD2HnD (wAP ac), RBD25G-5HPacQD2HPnD (Audience), RBD25GR-5HPacQD2HPnD&R11e-LTE6 (Audience LTE6 kit),** | Atheros8327 (ether1-ether2) |
| **RBD22UGS-5HPacD2HnD (mANTBox 52 15s)** | Atheros8327 (ether1-sfp1) |
| **RB1100AH** | Atheros8327 (ether1-ether5); Atheros8327 (ether6-ether10) |
| **RB1100AHx2** | Atheros8327 (ether1-ether5); Atheros8327 (ether6-ether10) |
| **CCR1009-8G-1S-1S+; CCR1009-8G-1S** | Atheros8327 (ether1-ether4) |
| **RB493G** | Atheros8316 (ether1+ether6-ether9); Atheros8316 (ether2-ether5) |
| **RB435G** | Atheros8316 (ether1-ether3)，ether1 可選 |
| **RB450G** | Atheros8316 (ether1-ether5)，ether1 可選 |
| **RB450Gx4** | Atheros8327 (ether1-ether5) |
| **RB433GL** | Atheros8327 (ether1-ether3) |
| **RB750G** | Atheros8316 (ether1-ether5) |
| **RB1200** | Atheros8316 (ether1-ether5) |
| **RB1100** | Atheros8316 (ether1-ether5); Atheros8316 (ether6-ether10) |
| **DISC Lite5** | Atheros8227 (ether1) |
| **RBmAP2nD** | Atheros8227 (ether1-ether2) |
| **RBmAP2n** | Atheros7240 (ether1-ether2) |
| **RB750** | Atheros7240 (ether2-ether5) |
| **RB750UP** | Atheros7240 (ether2-ether5) |
| **RB751U-2HnD** | Atheros7240 (ether2-ether5) |
| **RB951-2n** | Atheros7240 (ether2-ether5) |
| **RB951Ui-2HnD** | Atheros8227 (ether1-ether5) |
| **RB433 系列** | ICPlus175D (ether2-ether3)；較舊型號使用 ICPlus175C |
| **RB450** | ICPlus175D (ether2-ether5)；較舊型號使用 ICPlus175C |
| **RB493 系列** | ICPlus178C (ether2-ether9) |
| **RB816** | ICPlus178C (ether1-ether16) |

命令列配置位於 switch 選單下。該選單包含系統中存在的所有交換晶片的列表，以及一些子選單。

```ros
[admin@MikroTik] > /interface/ethernet/switch/print 
Flags: I - invalid 
 #   NAME         TYPE             MIRROR-SOURCE       MIRROR-TARGET       SWITCH-ALL-PORTS
 0   switch1      Atheros-8327     none                none               
 1   switch2      Atheros-8227     none                none               
```

根據交換晶片型別的不同，可用的配置能力也可能不同。

## 功能 {#features}

---

### 埠交換 {#port-switching}

要在非 CRS 系列裝置上設定埠交換，請檢視 [網橋硬體解除安裝](./index.md#bridge-hardware-offloading) 頁面。

:::warning
在 RouterOS v6.41 及更新版本中，埠交換透過網橋配置完成。在 RouterOS v6.41 之前，埠交換透過 master-port 屬性完成。
:::

#### 交換器全部埠功能 {#switch-all-ports-feature}

RB450G/RB435G/RB850Gx2 裝置上的 Ether1 埠具有一項功能，可將其從預設交換器組中移除或新增到預設交換器組。此設定位於 `/interface/ethernet/switch` 選單中。預設情況下，ether1 埠會包含在交換器組中。

![Switch 4](/img/913fb84cea71ea81.webp)

| 屬性 | 描述 |
| :-- | :-- |
| **switch-all-ports** (*no*\| yes*; 預設：**yes**) | 僅在 RB450G/RB435G/RB850Gx2 裝置上更改 ether1 交換器組。<code>yes</code> - ether1 是交換器的一部分，支援交換器組以及所有其他高階 Atheros8316/Atheros8327 功能，包括擴充套件統計資訊（<code>`/interface/ethernet/print` stats</code>）。<code>no</code> - ether1 不是交換器的一部分，實際上使其成為獨立的乙太網埠，從而在橋接和路由模式下提高其到其他埠的吞吐量，但會移除此埠上的交換可能性。 |

### 埠映象 {#port-mirroring}

埠映象讓交換器複製進出某個埠（`mirror-source`）的所有流量，並將這些複製的幀傳送到另一個埠（`mirror-target`）。此功能可用於輕鬆設定一個“分接”裝置，用來接收進出某個特定埠的所有流量。請注意，`mirror-source` 和 `mirror-target` 埠必須屬於同一交換器（在 `/interface/ethernet` 選單中檢視哪個埠屬於哪個交換器）。此外，mirror-target 可以具有特殊的 `cpu` 值，這意味著映象的封包應傳送到交換晶片的 CPU 埠。埠映象獨立於是否已設定交換器組而發生。

**子選單：** `/interface/ethernet/switch`

| 屬性 | 描述 |
| :-- | :-- |
| **mirror-source** (*name \| none*; 預設：**none**) | 選擇單個映象源埠。入站和出站流量將傳送到 `mirror-target` 埠。請注意，`mirror-target` 埠必須屬於同一交換器（在 `/interface/ethernet` 選單中檢視哪個埠屬於哪個交換器）。 |
| **mirror-target** (*name \| none \| cpu*; 預設：**none**) | 選擇單個映象目標埠。來自 `mirror-source` 和 `mirror`（請參閱規則表和主機表中的屬性）的映象封包將傳送到所選埠。 |
| **mirror-egress-target** (*name \| none*; 預設：**none**) | 選擇單個映象出站目標埠，僅在 **88E6393X**、**88E6191X** 和 **88E6190** 交換晶片上可用。來自 `mirror-egress`（請參閱埠選單中的屬性）的映象封包將傳送到所選埠。 |

**子選單：** `/interface/ethernet/switch/rule`

| 屬性 | 描述 |
| :-- | :-- |
| **mirror** (*no \| yes*; 預設：**no**) | 是否將封包副本傳送到 `mirror-target` 埠。 |
| **mirror-ports** (*name*; 預設：) | 選擇多個映象目標埠，僅在 **88E6393X** 交換晶片上可用。ACL 規則中匹配的封包將被複制併發送到所選埠。 |

**子選單：** `/interface/ethernet/switch/host`

| 屬性 | 描述 |
| :-- | :-- |
| **mirror** (*no \| yes*; 預設：**no**) | 是否將具有匹配 MAC 目的地址的幀的副本傳送到 `mirror-target` 埠（對於 CRS3xx 系列交換器，匹配目的地址或源地址） |

**子選單：** `/interface/ethernet/switch/port`

| 屬性 | 描述 |
| :-- | :-- |
| **mirror-egress** (*no \| yes*; 預設：**no**) | 是否將出站封包副本傳送到 `mirror-egress-target` 埠，僅在 **88E6393X**、**88E6191X** 和 **88E6190** 交換晶片上可用。 |
| **mirror-ingress** (*no \| yes*; 預設：**no**) | 是否將入站封包副本傳送到 `mirror-ingress-target` 埠，僅在 **88E6393X**、**88E6191X** 和 **88E6190** 交換晶片上可用。 |
| **mirror-ingress-target** (*name \| none*; 預設：**none**) | 選擇單個映象入站目標埠，僅在 **88E6393X**、**88E6191X** 和 **88E6190** 交換晶片上可用。來自 `mirror-ingress` 的映象封包將傳送到所選埠。 |

埠映象配置示例：

```ros
/interface/ethernet/switch
set switch1 mirror-source=ether2 mirror-target=ether3
```

:::danger
如果將某個乙太網埠設定為具有至少兩個交換晶片的裝置上的 mirror-source，並且這些 mirror-source 埠位於同一個網橋中，同時兩個交換晶片的 mirror-target 都設定為將封包傳送到 CPU，那麼這將導致環路，可能使裝置無法訪問。
:::

### 埠設定 {#port-settings}

此選單下的屬性用於為支援 VLAN 表的交換晶片配置 VLAN 交換和過濾選項。這些屬性僅適用於支援 VLAN 表的交換晶片。請檢視 [交換晶片功能](./switch-chip-features.md) 表，以確認您的裝置支援此功能。

:::danger
入站流量被視為傳送**進入**某個埠的流量；該埠有時稱為**入站埠**。出站流量被視為從某個埠傳送**出去**的流量；該埠有時稱為**出站埠**。區分它們對於正確設定 VLAN 過濾非常重要，因為某些屬性僅適用於入站或出站流量。
:::

| 屬性 | 描述 |
| :-- | :-- |
| **vlan-mode** (*check \| disabled \| fallback \| secure*; 預設：**disabled**) | 更改入站流量針對 [VLAN 表](./switch-chip-features.md#vlan-table) 的 VLAN 查詢機制。<code>disabled</code> - 完全停用針對入站流量的 VLAN 表檢查。在入站埠上設定時不會丟棄任何流量。<code>fallback</code> - 針對入站流量，將帶標籤流量與 VLAN 表進行對比檢查，並轉發所有未帶標籤流量。如果入站流量帶標籤，並且在 VLAN 表中找不到相應 VLAN ID 的出站埠，則丟棄流量。如果在 VLAN 表中找不到某個 VLAN ID，則轉發流量。用於僅在特定埠上允許已知 VLAN。<code>check</code> - 針對入站流量，將帶標籤流量與 VLAN 表進行對比檢查，並丟棄所有未帶標籤流量。如果入站流量帶標籤，並且在 VLAN 表中找不到相應 VLAN ID 的出站埠，則丟棄流量。<code>secure</code> - 針對入站流量，將帶標籤流量與 VLAN 表進行對比檢查，並丟棄所有未帶標籤流量。入站埠和出站埠都必須能在 VLAN 表中找到相應 VLAN ID，否則丟棄流量。 |
| **vlan-header** (*add-if-missing \| always-strip \| leave-as-is*; 預設：**leave-as-is**) | 設定對出站流量在埠上執行的操作。<code>add-if-missing</code> - 為出站流量新增 VLAN 標籤，並使用入站埠的 default-vlan-id。應用於 trunk 埠。<code>always-strip</code> - 移除出站流量上的 VLAN 標籤。應用於 access 埠。<code>leave-as-is</code> - 不新增或移除出站流量上的 VLAN 標籤。應用於 hybrid 埠。 |
| **default-vlan-id** (*auto \| integer: 0..4095*; 預設：**auto**) | 為埠上所有未帶標籤的入站流量新增具有指定 VLAN ID 的 VLAN 標籤。應在埠上將 vlan-header 設定為 `always-strip` 時使用，以將該埠配置為 access 埠。對於 hybrid 埠，default-vlan-id 用於為未帶標籤流量新增標籤。如果兩個埠具有相同的 default-vlan-id，則不會新增 VLAN 標籤，因為交換晶片假定流量正在 access 埠之間轉發。 |

:::warning
在 **QCA8337** 和 **Atheros8327** 交換晶片上，應使用預設的 `vlan-header=leave-as-is` 屬性。交換晶片將使用 `default-vlan-id` 屬性來確定哪些埠是 access 埠。`default-vlan-id` 僅應在 access/hybrid 埠上使用，以指定未帶標籤的入站流量分配到哪個 VLAN。
:::

### VLAN 表 {#vlan-table}

VLAN 表為具有特定 802.1Q 標籤的封包指定某些轉發規則。這些規則的優先順序高於使用 [網橋硬體解除安裝](./index.md#bridge-hardware-offloading) 功能配置的交換器組。基本上，表中包含將特定 VLAN 標籤 ID 對映到一個或多個埠組的條目。帶有 VLAN 標籤的封包透過相應表條目中設定的一個或多個埠離開交換晶片。控制帶 VLAN 標籤封包處理方式的確切邏輯由 `vlan-mode` 引數控制，該引數可按交換器埠更改。

基於 VLAN ID 的轉發會考慮主機表中動態學習或手動新增的 MAC 地址。QCA8337 和 Atheros8327 交換晶片還支援獨立 VLAN 學習（IVL），其學習基於 MAC 地址和 VLAN ID 兩者，從而允許同一個 MAC 用於多個 VLAN。

不帶 VLAN 標籤的封包會被視為具有埠 `default-vlan-id` 的 VLAN 標籤。如果配置了 `vlan-mode=check` 或 `vlan=mode=secure`，要轉發不帶 VLAN 標籤的封包，必須根據 `default-vlan-id` 將具有相同 VLAN ID 的條目新增到 VLAN 表中。

| 屬性 | 描述 |
| :-- | :-- |
| **disabled** (*no \| yes*; 預設：**no**) | 啟用或停用交換器 VLAN 條目。 |
| **independent-learning** (no*\| yes*; 預設：**yes**) | 使用共享 VLAN 學習（SVL）還是獨立 VLAN 學習（IVL）。 |
| **ports** (*name*; 預設：**none**) | 相應 VLAN 的介面成員列表。此設定接受逗號分隔的值，例如 `ports=ether1,ether2`。 |
| **switch** (*name*; 預設：**none**) | 相應 VLAN 條目所針對的交換器名稱。 |
| **vlan-id** (*integer: 0..4095*; 預設：) | 用於某些交換器埠配置的 VLAN ID。 |

:::warning
搭載 **MT7621**、**MT7531**、**EN7523, RTL8367**、**88E6393X**、**88E6191X**、**88E6190** 交換晶片的裝置在 RouterOS v7 中支援 [硬體解除安裝 VLAN 過濾](./index.md#bridge-vlan-filtering)。`/interface/ethernet/switch` 選單中與 VLAN 相關的配置不可用。
:::

#### VLAN 轉發 {#vlan-forwarding}

`vlan-mode` 和 `vlan-header` 以及 VLAN 表均可用於配置 VLAN 標記、取消標記和過濾。可以有多種組合，每種組合都會產生不同結果。下表列出了對於每種 VLAN 模式，當入站埠收到特定流量時，出站埠將傳送何種流量。

**注意：**

- **L** - `vlan-header` 設定為 `leave-as-is`
- **S** - `vlan-header` 設定為 `always-strip`
- **A** - `vlan-header` 設定為 `add-if-missing`
- **U** - 傳送未帶標籤流量
- **T** - 傳送帶標籤流量，入站埠上已存在標籤
- **TA** - 傳送帶標籤流量，在入站埠上添加了標籤
- **DI** - 由於 vlan-mode 中選擇的模式，流量在入站埠被丟棄
- **DE** - 由於在 VLAN 表中找不到出站埠，流量在出站埠被丟棄
- **VID 匹配** - 入站流量的 VLAN 標籤中的 VLAN ID 存在於 VLAN 表中
- **埠匹配** - 入站埠存在於 VLAN 表中相應 VLAN ID 下

|  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| *VLAN 模式 = disabled* | 出站埠不在 VLAN 表中 |  |  | 出站埠在 VLAN 表中 |  |  |
|  | L | S | A | L | S | A |
| 未帶標籤流量 | U | U | TA | U | U | TA |
| 帶標籤流量；無 VID 匹配 | T | U | T |  |  |  |
| 帶標籤流量；VID 匹配；無埠匹配 | T | U | T | T | U | T |
| 帶標籤流量；VID 匹配；埠匹配 | T | U | T | T | U | T |

|  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| *VLAN 模式 = fallback* | 出站埠不在 VLAN 表中 |  |  | 出站埠在 VLAN 表中 |  |  |
|  | L | S | A | L | S | A |
| 未帶標籤流量 | U | U | TA | U | U | TA |
| 帶標籤流量；無 VID 匹配 | T | U | T |  |  |  |
| 帶標籤流量；VID 匹配；無埠匹配 | DE | DE | DE | T | U | T |
| 帶標籤流量；VID 匹配；埠匹配 | DE | DE | DE | T | U | T |

|  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| *VLAN 模式 = check* | 出站埠不在 VLAN 表中 |  |  | 出站埠在 VLAN 表中 |  |  |
|  | L | S | A | L | S | A |
| 未帶標籤流量 |  |  |  |  |  |  |
| 帶標籤流量；無 VID 匹配 | DI | DI | DI |  |  |  |
| 帶標籤流量；VID 匹配；無埠匹配 | DE | DE | DE | T | U | T |
| 帶標籤流量；VID 匹配；埠匹配 | DE | DE | DE | T | U | T |

|  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| *VLAN 模式 = secure* | 出站埠不在 VLAN 表中 |  |  | 出站埠在 VLAN 表中 |  |  |
|  | L | S | A | L | S | A |
| 未帶標籤流量 |  |  |  |  |  |  |
| 帶標籤流量；無 VID 匹配 | DI | DI | DI |  |  |  |
| 帶標籤流量；VID 匹配；無埠匹配 | DI | DI | DI | DI | DI | DI |
| 帶標籤流量；VID 匹配；埠匹配 | DE | DE | DE | T | U | T |

:::warning
上表用於更高階的配置，並用於複核您對每個與 VLAN 相關屬性如何處理封包的理解。
:::

### 主機表 {#host-table}

主機表表示交換晶片內部的 MAC 地址到埠對映。它可以包含兩種條目：動態和靜態。動態條目會自動新增。這也稱為學習過程：當交換晶片從某個埠收到封包時，它會將該封包的源 MAC 地址以及收到該封包的埠新增到主機表，因此當具有相同目的 MAC 地址的封包進入時，它就知道應將封包轉發到哪個埠。如果目的 MAC 地址不在主機表中（所謂的未知單播流量），則會將封包轉發到組中的所有埠。動態條目大約需要 5 分鐘超時。學習僅在配置為交換器組一部分的埠上啟用，因此如果未設定埠交換，就不會看到動態條目。此外，您可以新增靜態條目；如果具有相同 MAC 地址的動態條目已存在，靜態條目會接管該動態條目。由於埠交換是使用帶硬體解除安裝的網橋配置的，因此在一張表（網橋主機表或交換器主機表）上建立的任何靜態條目都會作為動態條目出現在另一張表上。在交換器主機表上新增靜態條目將提供對更多功能的訪問，這些功能由以下引數控制：

| 屬性 | 描述 |
| :-- | :-- |
| **copy-to-cpu** (*no \| yes*; 預設：**no**) | 是否將具有匹配 MAC 目的地址的幀的副本傳送到交換器 CPU 埠（對於 CRS3xx 系列交換器，匹配目的地址或源地址） |
| **drop** (*no \| yes*; 預設：**no**) | 是否丟棄在某個埠收到的、具有匹配 MAC 源地址的幀（對於 CRS3xx 系列交換器，匹配目的地址或源地址） |
| **mac-address** (*MAC;* 預設：**00:00:00:00:00:00**) | 主機的 MAC 地址 |
| **mirror** (*no \| yes*; 預設：**no**) | 是否將具有匹配 MAC 目的地址的幀的副本傳送到 `mirror-target` 埠（對於 CRS3xx 系列交換器，匹配目的地址或源地址） |
| **ports** (*name*; 預設：**none**) | 介面名稱；靜態 MAC 地址可以對映到多個埠，包括交換器 CPU 埠 |
| **redirect-to-cpu** (*no \| yes*; 預設：**no**) | 是否將具有匹配 MAC 目的地址的幀重定向到交換器 CPU 埠（對於 CRS3xx 系列交換器，匹配目的地址或源地址） |
| **share-vlan-learned**(*no \| yes*; 預設：**no**) | 靜態主機 MAC 地址查詢是使用共享 VLAN 學習（SVL）還是獨立 VLAN 學習（IVL）。SVL 模式用於那些不支援 IVL 或 IVL 已停用（independent-learning=no）的 VLAN 條目 |
| **switch** (*name*; 預設：**none**) | 要將 MAC 地址分配到的交換器名稱 |
| **vlan-id** (*integer: 0..4095*; 預設：) | 靜態新增的 MAC 地址條目的 VLAN ID |

:::warning
每個交換晶片可儲存在晶片上的 MAC 地址數量有限，請參閱簡介表瞭解特定主機表大小。一旦主機表已滿，可以利用不同技術來應對該情況，例如，交換器可以移除較舊條目以為較新的 MAC 地址釋放空間（用於 QCA-8337 和 Atheros-8327 交換晶片）；另一種選擇是直接忽略新的 MAC 地址，並且僅在超時後移除條目（用於 Atheros8316、Atheros8227、Atheros-7240、ICPlus175D 和 Realtek-RTL8367 交換晶片）；最後一種選擇是前兩者的組合——僅允許一定數量的條目續期，並保持其他主機部分不變直到超時（用於 MediaTek-MT7621、MT7531、EN7523 交換晶片）。這些技術無法透過配置更改。
:::

:::warning
對於 Atheros8316、Atheros8227 和 Atheros-7240 交換晶片，當交換器組上至少有一個硬體解除安裝網橋埠處於活動狀態時，switch-cpu 埠將始終參與主機學習過程。這會導致 switch-cpu 埠從非硬體解除安裝介面學習 MAC 地址。當單個網橋包含硬體解除安裝和非硬體解除安裝介面時，這可能導致封包丟失。此外，當同一交換器組上使用重複 MAC 地址時，無論主機是否位於不同邏輯網路中，都可能出現數據包丟失。建議僅當所有網橋埠都能使用硬體解除安裝時才使用硬體解除安裝，或者當一個或多個網橋埠無法配置硬體解除安裝時，在所有交換器埠上保持停用。
:::

:::note
當建立具有 `forward-reserved-addresses=no` 和 `protocol-mode=stp/rstp` 的硬體解除安裝網橋時，交換晶片 **QCA-8337** 和 **Atheros-8327** 會自動將保留組播 MAC 地址（01:80:C2:00:00:0x）新增到主機表。這些 MAC 不應由相容 802.1Q 的網橋轉發，並且它們對於 R/STP 的正確執行至關重要。由於交換器的主機表條目數量有限，這些 MAC 地址僅分配給 VLAN 1。
:::

:::info
為確保具有這些目的 MAC 地址的封包被正確處理：

- 交換器埠應設定為預設 VLAN 1（`default-vlan-id=auto` 或 `default-vlan-id=1`）。
- 如果顯式配置了 VLAN 1，則必須使用獨立 VLAN 學習（`independent-learning=yes`）。

:::

### 規則表 {#rule-table}

規則表是一個非常強大的工具，可基於 L2、L3 和 L4 協定頭欄位條件實現線速封包過濾、轉發和 VLAN 標記。該選單包含一個有序規則列表，就像 `/ip/firewall/filter` 中一樣，因此會針對每個封包檢查 ACL 規則，直到找到匹配項。如果多條規則可以匹配，則只會觸發第一條規則。沒有任何動作引數的規則是接受封包的規則。

每條規則包含條件部分和動作部分。動作部分由以下引數控制：

| 屬性 | 描述 |
| :-- | :-- |
| **copy-to-cpu** (*no \| yes*; 預設：**no**) | 是否將封包副本傳送到交換器 CPU 埠 |
| **mirror** (*no \| yes*; 預設：**no**) | 是否將封包副本傳送到 `mirror-target` 埠 |
| **new-dst-ports** (*name*; 預設：**none**) | 按指定內容更改目的埠，允許多個埠，包括交換器 CPU 埠。設定為空將丟棄封包。未使用該引數時，封包將被接受 |
| **new-vlan-id** (*integer: 0..4095*) | 將 VLAN ID 更改為指定值，或在尚不存在 VLAN 標籤時新增新的 VLAN 標籤（該屬性僅適用於 **Atheros8316** 和 **88E6393X** 交換晶片（**注意**：對於 88E6393X 交換晶片，還需要 vlan-filtering=yes）） |
| **new-vlan-priority** (*integer: 0..7*) | 更改 VLAN 優先順序欄位（優先順序程式碼點；該屬性僅適用於 **Atheros8327**、**QCA8337** 和 **Atheros8316** 交換晶片） |
| **rate** (*integer: 0..4294967295*) | 為匹配流量設定入站流量限制（位元每秒），並且只能應用於前 32 個規則槽位（該屬性僅適用於 **Atheros8327/QCA8337** 交換晶片） |
| **redirect-to-cpu** (*no \| yes*; 預設：**no**) | 將匹配封包的目的埠更改為交換器 CPU |

條件部分由其餘引數控制：

| 屬性 | 描述 |
| :-- | :-- |
| **disabled** (*no \| yes*; 預設：**no**) | 啟用或停用交換器規則 |
| **dscp** (*integer: 0..63*) | 匹配封包的 DSCP 欄位 |
| **dst-address** (*IP address/Mask*) | 匹配目的 IP 地址和掩碼 |
| **dst-address6** (*IPv6 address/Mask*) | 匹配目的 IPv6 地址和掩碼 |
| **dst-mac-address** (*MAC address/Mask*) | 匹配目的 MAC 地址和掩碼 |
| **dst-port** (*integer:* *0..65535*) | 匹配目的協定埠號或範圍 |
| **flow-label** (*integer:* *0..1048575*) | 匹配 IPv6 流標籤 |
| **mac-protocol** (*802.2 \| arp \| capsman \| dot1x \| homeplug-av \| ip \| ipv6 \| ipx \| lacp \| lldp \| loop-protect \| macsec \| mpls-multicast \| mpls-unicast \| mvrp \| packing-compr \| packing-simple \| pppoe \| pppoe-discovery \| rarp \| romon \| service-vlan \| vlan \| or 0..65535 \| or 0x0000-0xffff*) | 匹配由協定名稱或編號指定的特定 MAC 協定（如果有 VLAN 標籤則跳過） |
| **ports** (*name*) | 規則將應用於接收流量的介面名稱，允許多個埠。如果 ports 屬性留空，則該規則將應用於所有交換器介面 |
| **protocol** (*dccp \| ddp \| egp \| encap \| etherip \| ggp \| gre \| hmp \| icmp \| icmpv6 \| idpr-cmtp \| igmp \| ipencap \| ipip \| ipsec-ah \| ipsec-esp \| ipv6 \| ipv6-frag \| ipv6-nonxt \| ipv6-opts \| ipv6-route \| iso-tp4 \| l2tp \| ospf \| pim \| pup \| rdp \| rspf \| rsvp \| sctp \| st \| tcp \| udp \| udp-lite \| vmtp \| vrrp \| xns-idp \| xtp \| or 0..255*) | 匹配由協定名稱或編號指定的特定 IP 協定 |
| **src-address** (*IP address/Mask*) | 匹配源 IP 地址和掩碼 |
| **src-address6** (*IPv6 address/Mask*) | 匹配源 IPv6 地址和掩碼 |
| **src-mac-address** (*MAC address/Mask*) | 匹配源 MAC 地址和掩碼 |
| **src-port** (*0..65535*) | 匹配源協定埠號或範圍 |
| **switch** (*switch group*) | 匹配規則將應用的交換器組 |
| **traffic-class** (*0..255*) | 匹配 IPv6 流量類別 |
| **vlan-id** (*0..4095*) | 匹配 VLAN ID（該屬性僅適用於 Atheros8316、Atheros8327、QCA8337、88E6393X 交換晶片） |
| **vlan-header** (*not-present \| present*) | 匹配 VLAN 頭，無論 VLAN 頭是否存在（該屬性僅適用於 Atheros8316、Atheros8327、QCA8337、88E6393X 交換晶片。對於 **88E6393X** 交換晶片，還需要 vlan-filtering=yes） |
| **vlan-priority** (*0..7*) | 匹配 VLAN 優先順序（優先順序程式碼點） |

:::warning
特定於 IPv4 和 IPv6 的條件不能出現在同一條規則中。
:::

:::warning
由於規則表完全在交換晶片硬體中處理，因此規則數量存在限制。根據規則中使用的條件數量（MAC 層、IP 層、IPv6、L4 層），活動規則數量可能不同：對於 Atheros8316 交換晶片為 8 到 32 條，對於 Atheros8327/QCA8337 交換晶片為 8 到 92 條，對於 88E6393X 交換晶片為 42 到 256 條。修改規則集後，您始終可以執行 `/interface/ethernet/switch/rule/print`，檢視列表末尾沒有規則顯示為 “invalid”，這意味著這些規則未能放入交換晶片。
:::

### 埠隔離 {#port-isolation}

埠隔離提供了劃分（隔離）網路某些部分的可能性。當您需要確保某些裝置無法訪問其他裝置時，這可能很有用。這可以透過隔離交換器埠來實現。埠隔離僅在同一交換器的成員埠之間生效。自 RouterOS v6.43 起，所有交換晶片都支援交換器埠隔離。

| 屬性 | 描述 |
| :-- | :-- |
| **forwarding-override** (*interface*; 預設：) | 強制將入站流量轉發到特定介面。可以透過用逗號分隔來指定多個介面。 |

:::info
(R/M)STP 僅在 PVLAN 設定中才能正常工作。在存在多個隔離交換器組的設定中，(R/M)STP 將無法正常工作，因為交換器組可能無法正確接收 BPDU，從而無法檢測網路環路。
:::

:::warning
`forwarding-override` 屬性僅影響入站流量。未指定 `forwarding-override` 的交換器埠可以透過所有交換器埠傳送封包。
:::

:::warning
支援 VLAN 表的交換晶片（**QCA8337**、**Atheros8327**、**Atheros8316**、**Atheros8227** 和 **Atheros7240**）在交換器埠上啟用 VLAN 查詢時（將 `vlan-mode` 設定為 `fallback`、`check` 或 `secure`），可以覆蓋埠隔離配置。如果同一 VLAN 上的埠之間需要額外的埠隔離，可以使用帶有 new-dst-ports 屬性的交換器規則。其他不支援交換器規則的裝置無法克服此限制。
:::

#### 專用 VLAN {#private-vlan}

在某些場景中，您可能需要將所有流量轉發到上行鏈路埠，同時所有其他埠彼此隔離。這種設定稱為 **專用 VLAN** 配置。**交換器**會將所有乙太網幀直接轉發到上行鏈路埠，使**路由器**能夠過濾不需要的封包，並限制交換器埠後方裝置之間的訪問。

![Port Isolation](/img/ae49133a966da305.webp)

要配置交換器埠隔離，您需要將所有所需埠加入交換：

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add interface=sfp1 bridge=bridge1 hw=yes
add interface=ether1 bridge=bridge1 hw=yes
add interface=ether2 bridge=bridge1 hw=yes
add interface=ether3 bridge=bridge1 hw=yes
```

:::warning
預設情況下，網橋介面的 `protocol-mode` 設定為 `rstp`。對於某些裝置，這可能會停用硬體解除安裝，因為特定交換晶片不支援此功能。請參閱 [網橋硬體解除安裝](./index.md#bridge-hardware-offloading) 部分了解支援的功能。
:::

為每個需要隔離的交換器埠（不包括上行鏈路埠）覆蓋出站埠：

```ros
/interface/ethernet/switch/port-isolation
set ether1 forwarding-override=sfp1
set ether2 forwarding-override=sfp1
set ether3 forwarding-override=sfp1
```

:::warning
可以為單個交換晶片設定多個上行鏈路埠，方法是指定多個介面並用逗號分隔。
:::

#### 隔離交換器組 {#isolated-switch-groups}

在某些場景中，您可能需要將一組裝置與其他組隔離。這可以使用交換器埠隔離功能來完成。當您有多個網路但希望使用單個交換器時，這很有用。透過埠隔離，您可以允許某些交換器埠僅透過一組交換器埠通訊。在此示例中，**ether1-3** 上的裝置只能與 **ether1-3** 上的裝置通訊，而 **ether4-5** 上的裝置只能與 **ether4-5** 上的裝置通訊（**ether1-3** 無法與 **ether4-5** 通訊）。

:::warning
埠隔離僅在屬於同一交換器的埠之間可用。
:::

![Port Isolation 2](/img/af23c24ae48bc2f6.webp)

要配置隔離交換器組，您必須先將所有埠加入交換：

```ros
/interface/bridge
add name=bridge
/interface/bridge/port
add bridge=bridge1 interface=ether1 hw=yes
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether3 hw=yes
add bridge=bridge1 interface=ether4 hw=yes
add bridge=bridge1 interface=ether5 hw=yes
```

:::warning
預設情況下，網橋介面的 `protocol-mode` 設定為 `rstp`。對於某些裝置，這可能會停用硬體解除安裝，因為特定交換晶片不支援此功能。請參閱 [網橋硬體解除安裝](./index.md#bridge-hardware-offloading) 部分了解支援的功能。
:::

然後，在 `forwarding-override` 屬性中指定您希望屬於同一隔離交換器組的所有埠（正在應用該屬性的埠除外），例如，為 **A** 裝置建立隔離交換器組：

```ros
/interface/ethernet/switch/port-isolation
set ether1 forwarding-override=ether2,ether3
set ether2 forwarding-override=ether1,ether3
set ether3 forwarding-override=ether1,ether2
```

要為 **B** 裝置建立隔離交換器組：

```ros
/interface/ethernet/switch/port-isolation
set ether4 forwarding-override=ether5
set ether5 forwarding-override=ether4
```

### CPU 流控 {#cpu-flow-control}

所有交換晶片都有一個稱為 **switchX-cpu** 的特殊埠。這是交換晶片的 CPU 埠。它用於將流量從交換晶片轉發到 CPU。管理流量和路由功能需要這樣的埠。預設情況下，交換晶片會確保此特殊 CPU 埠不發生擁塞，並在鏈路容量超出時傳送 Pause 幀，以確保埠不會過飽和。此功能稱為 **CPU 流控**。如果沒有此功能，對路由或管理目的可能至關重要的封包可能會被丟棄。

自 RouterOS v6.43 起，在使用以下交換晶片之一的某些裝置上可以停用 CPU 流控功能：QCA8337、Atheros8227、Atheros8327、Atheros7240、Atheros8316、88E6191X 和 88E6393X。其他交換晶片預設啟用此功能且無法更改。要停用 CPU 流控，請使用以下命令：

```ros
/interface/ethernet/switch/set switch1 cpu-flow-control=no
```

### 統計資訊 {#statistics}

某些交換晶片能夠報告統計資訊，這對於監控從內建交換晶片傳送到 CPU 的封包數量很有用。這些統計資訊還可用於監控 CPU 流控。您可以在下面找到交換晶片統計資訊的示例：

```ros
[admin@MikroTik] > /interface/ethernet/switch/print stats

                      name:      switch1
            driver-rx-byte:  221 369 701
          driver-rx-packet:    1 802 975
            driver-tx-byte:   42 621 969
          driver-tx-packet:      310 485
                  rx-bytes:  414 588 529
                 rx-packet:    2 851 236
              rx-too-short:            0
               rx-too-long:            0
              rx-broadcast:    1 040 309
                  rx-pause:            0
              rx-multicast:      486 321
              rx-fcs-error:            0
            rx-align-error:            0
               rx-fragment:            0
                rx-control:            0
             rx-unknown-op:            0
           rx-length-error:            0
             rx-code-error:            0
          rx-carrier-error:            0
                 rx-jabber:            0
                   rx-drop:            0
                  tx-bytes:   44 071 621
                 tx-packet:      312 597
              tx-too-short:            0
               tx-too-long:        8 397
              tx-broadcast:        2 518
                  tx-pause:        2 112
              tx-multicast:        7 142
    tx-excessive-collision:            0
     tx-multiple-collision:            0
       tx-single-collision:            0
     tx-excessive-deferred:            0
               tx-deferred:            0
         tx-late-collision:            0
        tx-total-collision:            0
                   tx-drop:            0
                 tx-jabber:            0
              tx-fcs-error:            0
                tx-control:        2 112
               tx-fragment:            0
                  tx-rx-64:        6 646
              tx-rx-65-127:    1 509 891
             tx-rx-128-255:    1 458 299
             tx-rx-256-511:      178 975
            tx-rx-512-1023:          953
           tx-rx-1024-1518:          672
            tx-rx-1519-max:            0
```

某些裝置具有多個 CPU 核心，這些核心使用獨立的資料通道直接連線到內建交換晶片。這些裝置可以報告從交換晶片向 CPU 埠轉發封包或從 CPU 埠轉發封包時使用了哪個資料通道。對於此類裝置，每一行都會增加一行額外內容，第一行表示使用第一個資料通道傳送的資料，第二行表示使用第二個資料通道傳送的資料，依此類推。您可以在下面找到具有連線 CPU 和內建交換晶片的多條資料通道的裝置的交換晶片統計資訊示例：

```ros
[admin@MikroTik] > /interface/ethernet/switch/print stats
                  name:      switch1
        driver-rx-byte:  226 411 248
                                   0
      driver-rx-packet:    1 854 971
                                   0
        driver-tx-byte:   45 988 067
                                   0
      driver-tx-packet:      345 282
                                   0
              rx-bytes:  233 636 763
                                   0
             rx-packet:    1 855 018
                                   0
          rx-too-short:            0
                                   0
           rx-too-long:            0
                                   0
              rx-pause:            0
                                   0
          rx-fcs-error:            0
                                   0
           rx-overflow:            0
                                   0
              tx-bytes:   47 433 203
                                   0
             tx-packet:      345 282
                                   0
    tx-total-collision:            0
                                   0
```

## 配置示例 {#setup-examples}

---

:::info
使用安全 `vlan-mode` 時，請確保已將所需的所有介面新增到 VLAN 表。要使路由功能在同一裝置上透過使用安全 `vlan-mode` 的埠正常工作，您需要允許這些埠訪問 CPU；可以透過將 switchX-cpu 介面本身新增到 VLAN 表來實現。示例可在 [管理埠](./switch-chip-features.md#management-access-configuration) 部分找到。
:::

:::note
可以同時使用內建交換晶片和 CPU 來建立交換器-路由器設定，其中裝置同時充當交換器和路由器。您可以在 [交換器-路由器](./switch-chip-features.md#inter-vlan-routing) 部分找到配置示例。
:::

:::warning
當允許訪問 CPU 時，您是在允許從某個埠訪問實際的路由器/交換器。這並不總是可取的。當允許從某個 VLAN ID 和埠訪問 CPU 時，請確保實施適當的防火牆過濾規則來保護您的裝置。使用防火牆過濾規則僅允許訪問特定服務。
:::

:::warning
搭載 **MT7621**、**MT7531**、**EN7523, RTL8367**、**88E6393X**、**88E6191X,** **88E6190** 交換晶片的裝置在 RouterOS v7 中支援 [硬體解除安裝 VLAN 過濾](./index.md#bridge-vlan-filtering)。`/interface/ethernet/switch` 選單中與 VLAN 相關的配置不可用。
:::

:::warning
要使與 VLAN 相關的匹配項或與 VLAN 相關的動作引數在 **88E6393X** 交換晶片上生效，您需要在網橋介面上啟用 vlan-filtering，並確保這些埠上啟用了硬體解除安裝，否則這些引數將不起作用。
:::

### VLAN 示例 1（Trunk 和 Access 埠） {#vlan-example-1-trunk-and-access-ports}

搭載 Atheros 交換晶片的 RouterBOARD 可用於 802.1Q Trunking。RouterOS v6 中的此功能受 **QCA8337, Atheros8316, Atheros8327, Atheros8227** 和 **Atheros7240** 交換晶片支援。在此示例中，**ether3**、**ether4** 和 **ether5** 介面是 access 埠，而 **ether2** 是 trunk 埠。每個 access 埠的 VLAN ID：ether3 - 200，ether4 - 300，ether5 - 400。

![Access Ports](/img/d235e6fd5caac3d6.webp)

將所需埠加入交換：

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether3 hw=yes
add bridge=bridge1 interface=ether4 hw=yes
add bridge=bridge1 interface=ether5 hw=yes
```

:::warning
預設情況下，網橋介面的 `protocol-mode` 設定為 `rstp`。對於某些裝置，這可能會停用硬體解除安裝，因為特定交換晶片不支援此功能。請參閱 [網橋硬體解除安裝](./index.md#bridge-hardware-offloading) 部分了解支援的功能。
:::

新增 VLAN 表條目，以允許埠之間具有特定 VLAN ID 的幀：

```ros
/interface/ethernet/switch/vlan
add ports=ether2,ether3 switch=switch1 vlan-id=200
add ports=ether2,ether4 switch=switch1 vlan-id=300
add ports=ether2,ether5 switch=switch1 vlan-id=400
```

為每個埠分配 `vlan-mode` 和 `vlan-header` 模式，併為每個 access 埠在入站方向分配 `default-vlan-id`：

```ros
/interface/ethernet/switch/port
set ether2 vlan-mode=secure vlan-header=add-if-missing
set ether3 vlan-mode=secure vlan-header=always-strip default-vlan-id=200
set ether4 vlan-mode=secure vlan-header=always-strip default-vlan-id=300
set ether5 vlan-mode=secure vlan-header=always-strip default-vlan-id=400
```

- 設定 `vlan-mode=secure` 可確保嚴格使用 VLAN 表。
- 為 access 埠設定 `vlan-header=always-strip` 會在幀離開交換晶片時移除幀上的 VLAN 頭。
- 為 trunk 埠設定 `vlan-header=add-if-missing` 會為未帶標籤的幀新增 VLAN 頭。
- `default-vlan-id` 指定為 access 埠的未帶標籤入站流量新增哪個 VLAN ID。

:::warning
在 **QCA8337** 和 **Atheros8327** 交換晶片上，應使用預設的 `vlan-header=leave-as-is` 屬性。交換晶片將使用 `default-vlan-id` 屬性來確定哪些埠是 access 埠。`default-vlan-id` 僅應在 access/hybrid 埠上使用，以指定未帶標籤的入站流量分配到哪個 VLAN。
:::

### VLAN 示例 2（Trunk 和 Hybrid 埠） {#vlan-example-2-trunk-and-hybrid-ports}

VLAN Hybrid 埠可以同時轉發帶標籤和未帶標籤流量。此配置僅受某些千兆交換晶片支援（**QCA8337, Atheros8327**）。

![Hybrid Ports](/img/238fa201dac1535f.webp)

將所需埠加入交換：

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether3 hw=yes
add bridge=bridge1 interface=ether4 hw=yes
add bridge=bridge1 interface=ether5 hw=yes
```

:::warning
預設情況下，網橋介面的 `protocol-mode` 設定為 `rstp`。對於某些裝置，這可能會停用硬體解除安裝，因為特定交換晶片不支援此功能。請參閱 [網橋硬體解除安裝](./index.md#bridge-hardware-offloading) 部分了解支援的功能。
:::

新增 VLAN 表條目，以允許埠之間具有特定 VLAN ID 的幀。

```ros
/interface/ethernet/switch/vlan
add ports=ether2,ether3,ether4,ether5 switch=switch1 vlan-id=200
add ports=ether2,ether3,ether4,ether5 switch=switch1 vlan-id=300
add ports=ether2,ether3,ether4,ether5 switch=switch1 vlan-id=400
```

在交換器埠選單中，為所有埠設定 `vlan-mode`，併為計劃作為 hybrid 的埠設定 `default-vlan-id`：

```ros
/interface/ethernet/switch/port
set ether2 vlan-mode=secure vlan-header=leave-as-is
set ether3 vlan-mode=secure vlan-header=leave-as-is default-vlan-id=200
set ether4 vlan-mode=secure vlan-header=leave-as-is default-vlan-id=300
set ether5 vlan-mode=secure vlan-header=leave-as-is default-vlan-id=400
```

- `vlan-mode=secure` 將確保嚴格使用 VLAN 表。
- `default-vlan-id` 將為埠上的未帶標籤入站流量定義 VLAN。
- 在 QCA8337 和 Atheros8327 晶片中，使用 `vlan-mode=secure` 時會忽略交換器埠的 `vlan-header` 選項。VLAN 表條目處理所有出站標記/取消標記，並在所有埠上按 `vlan-header=leave-as-is` 工作。這意味著帶標籤進入的流量也會帶標籤出去，只有 `default-vlan-id` 幀會在出站埠處未帶標籤。

### 管理訪問配置 {#management-access-configuration}

在這些示例中，將展示多個場景的示例，但每個場景都要求您已將埠加入交換。下面介紹如何將多個埠加入交換：

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add interface=ether1 bridge=bridge1 hw=yes
add interface=ether2 bridge=bridge1 hw=yes
```

:::warning
預設情況下，網橋介面的 `protocol-mode` 設定為 `rstp`。對於某些裝置，這可能會停用硬體解除安裝，因為特定交換晶片不支援此功能。請參閱 [網橋硬體解除安裝](./index.md#bridge-hardware-offloading) 部分了解支援的功能。
:::

在這些示例中，將假定 **ether1** 是 trunk 埠，**ether2** 是 access 埠，配置如下：

```ros
/interface/ethernet/switch/port
set ether1 vlan-header=add-if-missing
set ether2 default-vlan-id=100 vlan-header=always-strip
/interface/ethernet/switch/vlan
add ports=ether1,ether2,switch1-cpu switch=switch1 vlan-id=100
```

#### 帶標籤 {#tagged}

要使裝置僅可從某個 VLAN 訪問，您需要在網橋介面上建立新的 VLAN 介面，併為其分配 IP 地址：

```ros
/interface/vlan
add name=MGMT vlan-id=99 interface=bridge1
/ip/address
add address=192.168.99.1/24 interface=MGMT
```

指定允許從哪些介面訪問裝置：

```ros
/interface/ethernet/switch/vlan
add ports=ether1,switch1-cpu switch=switch1 vlan-id=99
```

:::warning
在此 VLAN 表條目中僅指定 trunk 埠。無法透過 access 埠允許帶標籤流量訪問 CPU，因為 access 埠會使用指定的 `default-vlan-id` 值為所有入站流量新增標籤。
:::

配置 VLAN 表後，您可以啟用 `vlan-mode=secure` 來限制對 CPU 的訪問：

```ros
/interface/ethernet/switch/port
set ether1 vlan-header=add-if-missing vlan-mode=secure
set ether2 default-vlan-id=100 vlan-header=always-strip vlan-mode=secure
set switch1-cpu vlan-header=leave-as-is vlan-mode=secure
```

#### 未帶標籤 {#untagged}

要使裝置可從 access 埠訪問，請建立一個 VLAN ID 與 `default-vlan-id` 中設定相同的 VLAN 介面（例如 VLAN 100），併為其新增 IP 地址：

```ros
/interface/vlan
add name=VLAN100 vlan-id=100 interface=bridge1
/ip/address
add address=192.168.100.1/24 interface=VLAN100
```

指定允許哪些 access（未帶標籤）埠訪問 CPU：

```ros
/interface/ethernet/switch/vlan
add ports=ether1,ether2,switch1-cpu switch=switch1 vlan-id=100
```

:::danger
最常見的情況是 access（未帶標籤）埠伴隨一個 trunk（帶標籤）埠。在未帶標籤訪問 CPU 的情況下，您被迫同時指定 access 埠和 trunk 埠。這也會使 trunk 埠能夠訪問 CPU。這並不總是所需的，可能需要在 VLAN 過濾之上使用防火牆。
:::

配置 VLAN 表後，您可以啟用 `vlan-mode=secure` 來限制對 CPU 的訪問：

```ros
/interface/ethernet/switch/port
set ether1 vlan-header=add-if-missing vlan-mode=secure
set ether2 default-vlan-id=100 vlan-header=always-strip vlan-mode=secure
set switch1-cpu vlan-header=leave-as-is vlan-mode=secure
```

:::warning
要在搭載 **Atheros7240** 交換晶片的裝置上使用未帶標籤流量設定管理埠，您需要為 CPU 埠設定 `vlan-header=add-if-missing`。
:::

#### 從帶標籤埠發出未帶標籤流量 {#untagged-from-tagged-port}

可以允許從 trunk（帶標籤）埠使用未帶標籤流量訪問裝置。為此，請為網橋介面分配 IP 地址：

```ros
/ip/address
add address=10.0.0.1/24 interface=bridge1
```

指定允許哪些埠訪問 CPU。使用 switch-cpu 和 trunk 埠在 `default-vlan-id` 中使用的 `vlan-id`，預設情況下設定為 0 或 1。

```ros
/interface/ethernet/switch/vlan
add ports=ether1,switch1-cpu switch=switch1 vlan-id=1
```

配置 VLAN 表後，您可以啟用 `vlan-mode=secure` 來限制對 CPU 的訪問：

```ros
/interface/ethernet/switch/port
set ether1 default-vlan-id=1 vlan-header=add-if-missing vlan-mode=secure
set switch1-cpu default-vlan-id=1 vlan-header=leave-as-is vlan-mode=secure
```

:::warning
此配置示例不適用於搭載 **Atheros8316** 和 **Atheros7240** 交換晶片的裝置。對於搭載 **QCA8337** 和 **Atheros8327** 交換晶片的裝置，可以使用任何其他 `default-vlan-id`，只要它在 switch-cpu 和 trunk 埠上保持一致即可。對於搭載 **Atheros8227** 交換晶片的裝置，只能使用 `default-vlan-id=0`，並且 trunk 埠必須使用 `vlan-header=leave-as-is`。
:::

### VLAN 間路由 {#inter-vlan-routing}

許多 MikroTik 裝置內建交換晶片，配置得當可大幅提高整體吞吐量。搭載交換晶片的裝置可以同時用作路由器和交換器。這使您可以為網路使用單臺裝置而不是多臺裝置。

![Switch Router](/img/b6d5d8808c9eda44.webp)

要使此類設定正常工作，您必須將所有所需埠加入交換：

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether3 hw=yes
```

為每個 VLAN ID 建立 VLAN 介面，併為其分配 IP 地址：

```ros
/interface/vlan
add interface=bridge1 name=VLAN10 vlan-id=10
add interface=bridge1 name=VLAN20 vlan-id=20
/ip/address
add address=192.168.10.1/24 interface=VLAN10
add address=192.168.20.1/24 interface=VLAN20
```

為每個 VLAN 設定 DHCP 伺服器：

```ros
/ip/pool
add name=POOL10 ranges=192.168.10.100-192.168.10.200
add name=POOL20 ranges=192.168.20.100-192.168.20.200
/ip/dhcp-server
add address-pool=POOL10 disabled=no interface=VLAN10 name=DHCP10
add address-pool=POOL20 disabled=no interface=VLAN20 name=DHCP20
/ip/dhcp-server/network
add address=192.168.10.0/24 dns-server=8.8.8.8 gateway=192.168.10.1
add address=192.168.20.0/24 dns-server=8.8.8.8 gateway=192.168.20.1
```

在裝置上啟用 NAT：

```ros
/ip/firewall/nat
add action=masquerade chain=srcnat out-interface=ether1
```

將每個埠新增到 VLAN 表，並允許這些埠訪問 CPU，以使 DHCP 和路由正常工作：

```ros
/interface/ethernet/switch/vlan
add independent-learning=yes ports=ether2,switch1-cpu switch=switch1 vlan-id=10
add independent-learning=yes ports=ether3,switch1-cpu switch=switch1 vlan-id=20
```

將每個埠指定為 access 埠，並在每個埠以及 switch1-cpu 埠上啟用安全 VLAN 模式：

```ros
/interface/ethernet/switch/port
set ether2 default-vlan-id=10 vlan-header=always-strip vlan-mode=secure
set ether3 default-vlan-id=20 vlan-header=always-strip vlan-mode=secure
set switch1-cpu vlan-mode=secure
```

:::warning
在 **QCA8337** 和 **Atheros8327** 交換晶片上，應使用預設的 `vlan-header=leave-as-is` 屬性。交換晶片將使用 `default-vlan-id` 屬性來確定哪些埠是 access 埠。`default-vlan-id` 僅應在 access/hybrid 埠上使用，以指定未帶標籤的入站流量分配到哪個 VLAN。
:::

如果您的裝置具有交換器規則表，則可以在硬體層面限制 VLAN 之間的訪問。一旦在 VLAN 介面上新增 IP 地址，就會啟用 VLAN 間路由，但可以在硬體層面加以限制，同時保留 DHCP 伺服器和其他路由器相關服務。為此，請使用以下 ACL 規則。透過此類配置，您可以使用 VLAN 實現隔離的埠組。

```ros
/interface/ethernet/switch/rule
add dst-address=192.168.20.0/24 new-dst-ports="" ports=ether2 switch=switch1
add dst-address=192.168.10.0/24 new-dst-ports="" ports=ether3 switch=switch1
```

## 另請參閱 {#see-also}

- [交換器-路由器](./switch-chip-features.md#inter-vlan-routing)
- [基本 VLAN 交換](./user-guides/basic-vlan-switching.md)
- [網橋硬體解除安裝](./index.md#bridge-hardware-offloading)
- [生成樹協定](./user-guides/spanning-tree-protocol.md)
- [DHCP 偵聽和 Option 82](./index.md#dhcp-snooping-and-dhcp-option-82)
- [RouterBOARD 上的 MTU](../hardware/mtu-in-routeros.md)
- [二層錯誤配置](./user-guides/layer2-misconfiguration.md)
