---
title: "交換器晶片功能"
description: "本頁介紹 MikroTik RouterOS 交換器晶片功能，說明各種型號支援的 Port Switching 與 Mirroring 等功能，以及頻寬控制與 VLAN 設定方面的限制。"
tags:
  - 'switch-chip'
  - 'port-mirroring'
  - 'vlan'
source: https://manual.mikrotik.com/docs/7.24/bridging-and-switching/switch-chip-features
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

---

Routerboard 上有數種交換器晶片，且各自支援不同的功能組合。

:::info
Cloud Router Switch (CRS) 系列設備內建高度進階的交換器晶片，支援多種功能。若 MikroTik 設備搭載 Marvell Prestera 交換器（例如 CRS3xx），請參閱 [Marvell Prestera switch chip features](/docs/bridging-and-switching/marvell-prestera-switch-chip-features) 手冊。如需瞭解 CRS1xx/CRS2xx 系列設備上交換器晶片功能的更多詳情，請查閱 [CRS1xx/CRS2xx series switches](/docs/bridging-and-switching/crs1xx-and-2xx-series-switches) 手冊。
:::

| 交換器晶片 | 埠交換 | 埠鏡像 | TX 限制¹ | RX 限制¹ | 主機表 | Vlan 表² | 規則表 |
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

1. 對於 RTL8367、88E6393X、88E6191X、88E6190、MT7621、MT7531 與 EN7523，可透過 `/interface/ethernet/switch/port` 選單上的 `egress-rate` 與 `ingress-rate` 屬性變更 Tx/Rx 速率限制。對於 QCA8337、Atheros8327、Atheros8316、Atheros8227 與 Atheros7240，可透過 `/interface/ethernet` 選單上的 `bandwidth` 屬性變更 Tx/Rx 速率限制，詳情請參閱 [Ethernet manual](/docs/wired-connections/ethernet)。
2. 對於 88E6393X、88E6191X、88E6190、MT7621、MT7531、EN7523、RTL8367 交換器晶片，VLAN 表是透過 `/interface/bridge` 選單使用 [bridge HW vlan-filtering](/docs/bridging-and-switching/switch-chip-features#bridge-vlan-filtering) 設定。對於其他支援 VLAN 表的交換器，請參閱 [VLAN Table](/docs/bridging-and-switching/switch-chip-features#vlan-table)，並使用 `/interface/ethernet/switch/vlan` 選單設定 VLAN 表。

| RouterBoard | 交換器晶片說明 |
| :-- | :-- |
| **MA53UG+HbeH (hAP be³ Media)** | QCA8386 (ether2-ether5) |
| **C52iG-5HaxD2HaxD-TC (hAP ax²), C53UiG+5HPaxD2HPaxD (hAP ax³), Chateau ax series** | IPQ-PPE (ether1-ether5) |
| **cAPGi-5HaxD2HaxD (cAP ax)** | IPQ-PPE (ether1-ether2) |
| **L009 series** | 88E6190 (ether2-ether8, sfp1) |
| **RB5009 series** | 88E6393X (ether1-ether8, sfp-sfpplus1) |
| **CCR2004-16G-2S+** | 88E6191X (ether1-ether8); 88E6191X (ether9-ether16); |
| **RB4011iGS+** | RTL8367 (ether1-ether5); RTL8367 (ether6-ether10); |
| **RB1100AHx4** | RTL8367 (ether1-ether5); RTL8367 (ether6-ether10); RTL8367 (ether11-ether13) |
| **L41G-2axD (hAP ax lite)** | MT7531 (ether1-ether4) |
| **RB750Gr3 (hEX), RB760iGS (hEX S)** | MT7621 (ether1-ether5) |
| **E50UG (hEX Refresh)** | EN7523 (ether2-ether5) |
| **RBM33G** | MT7621 (ether1-ether3) |
| **RB3011 series** | QCA8337 (ether1-ether5); QCA8337 (ether6-ether10) |
| **RB OmniTik ac series** | QCA8337 (ether1-ether5) |
| **RBwsAP-5Hac2nD (wsAP ac lite)** | Atheros8227 (ether1-ether3) |
| **RB941-2nD (hAP lite)** | Atheros8227 (ether1-ether4) |
| **RB951Ui-2nD (hAP); RB952Ui-5ac2nD (hAP ac lite); RB750r2 (hEX lite); RB750UPr2 (hEX PoE lite); RB750P-PBr2 (PowerBox); RB750P r2; RBOmniTikU-5HnDr2 (OmniTIK 5); RBOmniTikUPA-5HnDr2 (OmniTIK 5 PoE)** | Atheros8227 (ether1-ether5) |
| **RB750Gr2 (hEX); RB962UiGS-5HacT2HnT (hAP ac); RB960PGS (hEX PoE); RB960PGS-PB (PowerBox Pro)** | QCA8337 (ether1-ether5) |
| **RB953GS** | Atheros8327 (ether1-ether3+sfp1) |
| **RB850Gx2** | Atheros8327 (ether1-ether5)，ether1 為選用 |
| **RB2011 series** | Atheros8327 (ether1-ether5+sfp1); Atheros8227 (ether6-ether10) |
| **RB750GL; RB751G-2HnD; RB951G-2HnD; RBD52G-5HacD2HnD (hAP ac²), RBD53iG-5HacD2HnD (hAP ac³), RBD53GR-5HacD2HnD&R11e-LTE6 (hAP ac³ LTE6 kit), RBD53G-5HacD2HnD-TC&EG12-EA (Chateau LTE12)** | Atheros8327 (ether1-ether5) |
| **RBcAPGi-5acD2nD (cAP ac), RBwAPGR-5HacD2HnD (wAP R ac and wAP ac LTE series), RBwAPG-5HacD2HnD (wAP ac), RBD25G-5HPacQD2HPnD (Audience), RBD25GR-5HPacQD2HPnD&R11e-LTE6 (Audience LTE6 kit),** | Atheros8327 (ether1-ether2) |
| **RBD22UGS-5HPacD2HnD (mANTBox 52 15s)** | Atheros8327 (ether1-sfp1) |
| **RB1100AH** | Atheros8327 (ether1-ether5); Atheros8327 (ether6-ether10) |
| **RB1100AHx2** | Atheros8327 (ether1-ether5); Atheros8327 (ether6-ether10) |
| **CCR1009-8G-1S-1S+; CCR1009-8G-1S** | Atheros8327 (ether1-ether4) |
| **RB493G** | Atheros8316 (ether1+ether6-ether9); Atheros8316 (ether2-ether5) |
| **RB435G** | Atheros8316 (ether1-ether3)，ether1 為選用 |
| **RB450G** | Atheros8316 (ether1-ether5)，ether1 為選用 |
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
| **RB433 series** | ICPlus175D (ether2-ether3)；舊機型使用 ICPlus175C |
| **RB450** | ICPlus175D (ether2-ether5)；舊機型使用 ICPlus175C |
| **RB493 series** | ICPlus178C (ether2-ether9) |
| **RB816** | ICPlus178C (ether1-ether16) |

指令列設定位於 switch 選單下。此選單包含系統中所有交換器晶片的清單，以及一些子選單。

```ros
[admin@MikroTik] > /interface/ethernet/switch/print 
Flags: I - invalid 
 #   NAME         TYPE             MIRROR-SOURCE       MIRROR-TARGET       SWITCH-ALL-PORTS
 0   switch1      Atheros-8327     none                none               
 1   switch2      Atheros-8227     none                none               
```

依交換器類型不同，可用的設定功能也會有所不同。

## 功能 {#features}

---

### 埠切換 {#port-switching}

若要在非 CRS 系列設備上設定埠切換，請查看 [Bridge Hardware Offloading](/docs/bridging-and-switching/switch-chip-features#bridge-hardware-offloading) 頁面。

:::warning
RouterOS v6.41 及更新版本的埠切換是透過 bridge 設定完成。在 RouterOS v6.41 之前，埠切換是透過 master-port 屬性完成。
:::

#### 切換所有埠功能 {#switch-all-ports-feature}

RB450G/RB435G/RB850Gx2 設備上的 Ether1 埠具有一項功能，可將其從預設交換器群組中移除或加入。此設定可在 `/interface/ethernet/switch` 選單中使用。預設情況下，ether1 埠會包含在交換器群組中。

![Switch 4](/img/913fb84cea71ea81.webp)

| 屬性 | 說明 |
| :-- | :-- |
| **switch-all-ports** (no*\| yes*; Default: **yes**) | 僅在 RB450G/RB435G/RB850Gx2 設備上變更 ether1 交換器群組。 <br/><ul><li><code>yes</code> - ether1 屬於交換器的一部分，並支援交換器群組以及所有其他進階 Atheros8316/Atheros8327 功能，包括延伸統計資料（<code><code>/interface/ethernet/print</code> stats</code>）。</li><li><code>no</code> - ether1 不屬於交換器的一部分，實際上會使其成為獨立的乙太網路埠，藉此提高其在 bridged 與 routed 模式下對其他埠的吞吐量，但會移除該埠的交換功能。</li></ul> |

### 埠鏡像 {#port-mirroring}

埠鏡像可讓交換器複製進出某個埠的所有流量（`mirror-source`），並將這些複製的訊框傳送至其他埠（`mirror-target`）。此功能可用於輕鬆設定接收特定埠所有進出流量的「tap」設備。請注意，`mirror-source` 與 `mirror-target` 埠必須屬於同一個交換器（可在 `/interface/ethernet` 選單中查看哪個埠屬於哪個交換器）。此外，mirror-target 可以有特殊的 `cpu` 值，表示鏡像封包應傳送至交換器晶片的 CPU 埠。埠鏡像會獨立於已設定或未設定的交換群組運作。

**子選單：** `/interface/ethernet/switch`

| 屬性 | 說明 |
| :-- | :-- |
| **mirror-source** (*name \| none*；預設：**none**) | 選取單一鏡像來源埠。傳入與傳出流量將會傳送至 `mirror-target` 埠。請注意，`mirror-target` 埠必須屬於同一個交換器（請在 `/interface/ethernet` 選單中查看哪個埠屬於哪個交換器）。 |
| **mirror-target** (*name \| none \| cpu*；預設：**none**) | 選取單一鏡像目標埠。來自 `mirror-source` 與 `mirror` 的鏡像封包（請參閱規則與主機表中的屬性）將會傳送至所選埠。 |
| **mirror-egress-target** (*name \| none*；預設：**none**) | 選取單一鏡像傳出目標埠，僅適用於 **88E6393X**、**88E6191X** 與 **88E6190** 交換器晶片。來自 `mirror-egress` 的鏡像封包（請參閱埠選單中的屬性）將會傳送至所選埠。 |

**子選單：** `/interface/ethernet/switch/rule`

| 屬性 | 說明 |
| :-- | :-- |
| **mirror** (*no \| yes*；預設：**no**) | 是否將封包副本傳送至 `mirror-target` 埠。 |
| **mirror-ports** (*name*；預設：) | 選取多個鏡像目標埠，僅適用於 **88E6393X** 交換器晶片。ACL 規則中符合的封包將會被複製並傳送至所選埠。 |

**子選單：** `/interface/ethernet/switch/host`

| 屬性 | 說明 |
| :-- | :-- |
| **mirror** (*no \| yes*；預設：**no**) | 是否將具有相符 MAC 目的地位址的訊框副本傳送至 `mirror-target` 埠（CRS3xx 系列交換器為相符目的地位址或來源位址） |

**子選單：** `/interface/ethernet/switch/port`

| 屬性 | 說明 |
| :-- | :-- |
| **mirror-egress** (*no \| yes*；預設：**no**) | 是否將傳出封包副本傳送至 `mirror-egress-target` 埠，僅適用於 **88E6393X**、**88E6191X** 與 **88E6190** 交換器晶片。 |
| **mirror-ingress** (*no \| yes*；預設：**no**) | 是否將傳入封包副本傳送至 `mirror-ingress-target` 埠，僅適用於 **88E6393X**、**88E6191X** 與 **88E6190** 交換器晶片。 |
| **mirror-ingress-target** (*name \| none*；預設：**none**) | 選取單一鏡像傳入目標埠，僅適用於 **88E6393X**、**88E6191X** 與 **88E6190** 交換器晶片。來自 `mirror-ingress` 的鏡像封包將會傳送至所選埠。 |

連接埠鏡像設定範例：

```ros
/interface/ethernet/switch
set switch1 mirror-source=ether2 mirror-target=ether3
```

:::danger
如果將 mirror-source 設為具備至少兩個交換器晶片的設備的 Ethernet 連接埠，且這些 mirror-source 連接埠位於單一 bridge 中，同時兩個交換器晶片的 mirror-target 都設為將封包傳送至 CPU，則會造成迴圈，可能使您的設備無法存取。
:::

### 連接埠設定 {#port-settings}

此選單下的屬性用於設定支援 VLAN Table 的交換器晶片的 VLAN 切換與篩選選項。這些屬性僅適用於支援 VLAN Table 的交換器晶片。請查看 [Switch Chip Features](/docs/bridging-and-switching/switch-chip-features) 表格，以確認您的設備支援此功能。

:::danger
Ingress 流量是指傳送**進入**特定連接埠的流量；此連接埠有時稱為 **ingress port**。Egress 流量是指從特定連接埠傳送**出去**的流量；此連接埠有時稱為 **egress port**。正確設定 VLAN 篩選時，區分兩者非常重要，因為某些屬性僅適用於 ingress 或 egress 流量。
:::

| 屬性 | 說明 |
| :-- | :-- |
| **vlan-mode** (*check \| disabled \| fallback \| secure*；預設：**disabled**) | 針對 ingress 流量，變更依據 <a href="/docs/bridging-and-switching/switch-chip-features#vlan-table">VLAN Table</a> 進行的 VLAN 查閱機制。<ul><li><code>disabled</code> - 完全停用 ingress 流量對 VLAN Table 的檢查。設定於 ingress 連接埠時，不會捨棄任何流量。</li><li><code>fallback</code> - 針對 ingress 流量，依據 VLAN Table 檢查具標籤的流量，並轉送所有未具標籤的流量。如果 ingress 流量具標籤，且在 VLAN Table 中找不到對應 VLAN ID 的 egress 連接埠，則會捨棄流量。如果在 VLAN Table 中找不到 VLAN ID，則會轉送流量。用於只允許特定連接埠上使用已知的 VLAN。</li><li><code>check</code> - 針對 ingress 流量，依據 VLAN Table 檢查具標籤的流量，並捨棄所有未具標籤的流量。如果 ingress 流量具標籤，且在 VLAN table 中找不到對應 VLAN ID 的 egress 連接埠，則會捨棄流量。</li><li><code>secure</code> - 針對 ingress 流量，依據 VLAN Table 檢查具標籤的流量，並捨棄所有未具標籤的流量。ingress 與 egress 連接埠都必須能在 VLAN Table 中找到對應的 VLAN ID，否則會捨棄流量。</li></ul> |
| **vlan-header** (*add-if-missing \| always-strip \| leave-as-is*；預設：**leave-as-is**) | 設定對連接埠 egress 流量執行的動作。<ul><li><code>add-if-missing</code> - 在 egress 流量上新增 VLAN 標籤，並使用 ingress 連接埠的 default-vlan-id。應用於 trunk 連接埠。</li><li><code>always-strip</code> - 移除 egress 流量上的 VLAN 標籤。應用於 access 連接埠。</li><li><code>leave-as-is</code> - 不在 egress 流量上新增或移除 VLAN 標籤。應用於 hybrid 連接埠。</li></ul> |
| **default-vlan-id** (*auto \| integer: 0..4095*；預設：**auto**) | 在連接埠上所有未具標籤的 ingress 流量中新增具有指定 VLAN ID 的 VLAN 標籤。應與連接埠上設為 `always-strip` 的 vlan-header 搭配使用，以將該連接埠設定為 access 連接埠。對於 hybrid 連接埠，default-vlan-id 用於標記未具標籤的流量。如果兩個連接埠具有相同的 default-vlan-id，則不會新增 VLAN 標籤，因為交換器晶片會假設流量是在 access 連接埠之間轉送。 |

:::warning
在 **QCA8337** 與 **Atheros8327** 交換器晶片上，應使用預設的 `vlan-header=leave-as-is` 屬性。交換器晶片會使用 `default-vlan-id` 屬性判斷哪些連接埠是 access 連接埠。`default-vlan-id` 只應在 access/hybrid 連接埠上使用，以指定未具標籤的 ingress 流量被指派到哪個 VLAN。
:::

### VLAN 表格 {#vlan-table}

VLAN 表會針對具有特定 802.1Q 標籤的封包指定若干轉送規則。這些規則的優先順序高於使用 [Bridge Hardware Offloading](/docs/bridging-and-switching/switch-chip-features#bridge-hardware-offloading) 功能設定的交換器群組。基本上，此表包含的項目會將特定 VLAN 標籤 ID 對應至一或多個埠的群組。具有 VLAN 標籤的封包會透過對應表項目中設定的一或多個埠離開交換器晶片。控制具有 VLAN 標籤封包如何處理的確切邏輯，是由可依各交換器埠變更的 `vlan-mode` 參數控制。

以 VLAN ID 為基礎的轉送會考量在主機表中動態學習或手動新增的 MAC 位址。QCA8337 與 Atheros8327 交換器晶片也支援 Independent VLAN Learning（IVL），會同時根據 MAC 位址與 VLAN ID 進行學習，因此同一個 MAC 可用於多個 VLAN。

沒有 VLAN 標籤的封包會被視為具有埠 `default-vlan-id` 的 VLAN 標籤。若設定 `vlan-mode=check` 或 `vlan=mode=secure`，若要轉送沒有 VLAN 標籤的封包，必須依據 `default-vlan-id` 在 VLAN 表中新增具有相同 VLAN ID 的項目。

| Property | Description |
| :-- | :-- |
| **disabled** (*no \| yes*; Default: **no**) | 啟用或停用交換器 VLAN 項目。 |
| **independent-learning** (no*\| yes*; Default: **yes**) | 是否使用 shared-VLAN-learning（SVL）或 independent-VLAN-learning（IVL）。 |
| **ports** (*name*; Default: **none**) | 對應 VLAN 的介面成員清單。此設定接受以逗號分隔的值，例如 `ports=ether1,ether2`。 |
| **switch** (*name*; Default: **none**) | 此 VLAN 項目所屬的交換器名稱。 |
| **vlan-id** (*integer: 0..4095*; Default:) | 特定交換器埠設定的 VLAN ID。 |

:::warning
具有 **MT7621**、**MT7531**、**EN7523, RTL8367**、**88E6393X**、**88E6191X**、**88E6190** 交換器晶片的設備，在 RouterOS v7 中支援 [HW offloaded vlan-filtering](/docs/bridging-and-switching/switch-chip-features#bridge-vlan-filtering)。`/interface/ethernet/switch` 選單中的 VLAN 相關設定無法使用。
:::

#### VLAN 轉送 {#vlan-forwarding}

`vlan-mode` 與 `vlan-header` 搭配 VLAN 表可用於設定 VLAN 標記、移除標記與篩選。多種組合皆有可能，每種組合都會產生不同的結果。下表列出在各種 VLAN Mode 下，當 ingress 埠收到特定流量時，何種流量會透過 egress 埠送出。

**NOTES:**

- **L** - `vlan-header` 設為 `leave-as-is`
- **S** - `vlan-header` 設為 `always-strip`
- **A** - `vlan-header` 設為 `add-if-missing`
- **U** - 送出未標記流量
- **T** - 送出已標記流量，標籤已存在於 ingress 埠
- **TA** - 送出已標記流量，標籤是在 ingress 埠新增
- **DI** - 流量因 vlan-mode 中選取的模式而在 ingress 埠被丟棄
- **DE** - 流量因在 VLAN 表中找不到 egress 埠而在 egress 埠被丟棄
- **VID match** - ingress 流量的 VLAN 標籤中的 VLAN ID 存在於 VLAN 表中
- **Port match** - ingress 埠存在於 VLAN 表中對應的 VLAN ID 項目內

|  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| *VLAN Mode = disabled* | Egress 埠未出現在 VLAN Table 中 |  |  | Egress 埠出現在 VLAN Table 中 |  |  |
|  | L | S | A | L | S | A |
| 未標記流量 | U | U | TA | U | U | TA |
| 已標記流量；沒有 VID 相符項目 | T | U | T |  |  |  |
| 已標記流量；VID 相符；沒有 Port 相符項目 | T | U | T | T | U | T |
| 已標記流量；VID 相符；Port 相符 | T | U | T | T | U | T |

|  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| *VLAN Mode = fallback* | Egress 埠未出現在 VLAN Table 中 |  |  | Egress 埠出現在 VLAN Table 中 |  |  |
|  | L | S | A | L | S | A |
| 未標記流量 | U | U | TA | U | U | TA |
| 已標記流量；沒有 VID 相符項目 | T | U | T |  |  |  |
| 已標記流量；VID 相符；沒有 Port 相符項目 | DE | DE | DE | T | U | T |
| 已標記流量；VID 相符；Port 相符 | DE | DE | DE | T | U | T |

|  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| *VLAN Mode = check* | Egress 埠未出現在 VLAN Table 中 |  |  | Egress 埠出現在 VLAN Table 中 |  |  |
|  | L | S | A | L | S | A |
| 未標記流量 |  |  |  |  |  |  |
| 已標記流量；沒有 VID 相符項目 | DI | DI | DI |  |  |  |
| 已標記流量；VID 相符；沒有 Port 相符項目 | DE | DE | DE | T | U | T |
| 已標記流量；VID 相符；Port 相符 | DE | DE | DE | T | U | T |

|  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| *VLAN Mode = secure* | Egress 埠未出現在 VLAN Table 中 |  |  | Egress 埠出現在 VLAN Table 中 |  |  |
|  | L | S | A | L | S | A |
| 未標記流量 |  |  |  |  |  |  |
| 已標記流量；沒有 VID 相符項目 | DI | DI | DI |  |  |  |
| 已標記流量；VID 相符；沒有 Port 相符項目 | DI | DI | DI | DI | DI | DI |
| 已標記流量；VID 相符；Port 相符 | DE | DE | DE | T | U | T |

:::warning
上表適用於進階設定，並可用來再次確認你對各項 VLAN 相關屬性如何處理封包的理解。
:::

### 主機表 {#host-table}

Host Table 代表交換器晶片內部的 MAC 位址與埠對應關係。它可以包含兩種類型的項目：動態與靜態。動態項目會自動新增。這也稱為學習程序：當交換器晶片從某個埠收到封包時，它會將封包的來源 MAC 位址與接收封包的埠新增到 Host Table，因此當具有相同目的 MAC 位址的封包進入時，它就知道應將封包轉送至哪個埠。如果目的 MAC 位址未出現在 Host Table 中（即所謂的 unknown-unicast 流量），則會將封包轉送至群組中的所有埠。動態項目約需 5 分鐘才會逾時。學習只會在設定為交換器群組一部分的埠上啟用，因此若你尚未設定埠交換，就不會看到動態項目。此外，你可以新增靜態項目；如果已有相同 MAC 位址的動態項目，靜態項目會取代動態項目。由於埠交換是透過啟用硬體卸載的 bridge 設定，因此在任一表格（bridge host 或 switch host）上建立的靜態項目，都會以動態項目的形式出現在另一個表格中。在 switch host table 上新增靜態項目，可提供對若干功能的存取，這些功能由下列參數控制：

| Property | Description |
| :-- | :-- |
| **copy-to-cpu** (*no \| yes*; Default: **no**) | 是否從具有相符 MAC 目的位址的封包，傳送一份訊框副本至交換器 CPU 埠（CRS3xx 系列交換器為相符目的或來源位址） |
| **drop** (*no \| yes*; Default: **no**) | 是否丟棄在特定埠上收到且具有相符 MAC 來源位址的訊框（CRS3xx 系列交換器為相符目的或來源位址） |
| **mac-address** (*MAC;* Default: **00:00:00:00:00:00**) | 主機的 MAC 位址 |
| **mirror** (*no \| yes*; Default: **no**) | 是否從具有相符 MAC 目的位址的封包，傳送一份訊框副本至 `mirror-target` 埠（CRS3xx 系列交換器為相符目的或來源位址） |
| **ports** (*name*; Default: **none**) | 介面名稱，靜態 MAC 位址可以對應至一個以上的埠，包括交換器 CPU 埠 |
| **redirect-to-cpu** (*no \| yes*; Default: **no**) | 是否將具有相符 MAC 目的位址的封包重新導向至交換器 CPU 埠（CRS3xx 系列交換器為相符目的或來源位址） |
| **share-vlan-learned**(*no \| yes*; Default: **no**) | 靜態主機 MAC 位址查閱是否搭配 shared-VLAN-learning（SVL）或 independent-VLAN-learning（IVL）使用。SVL 模式用於不支援 IVL 或 IVL 已停用（independent-learning=no）的 VLAN 項目 |
| **switch** (*name*; Default: **none**) | 要指派 MAC 位址的交換器名稱 |
| **vlan-id** (*integer: 0..4095*; Default:) | 靜態新增 MAC 位址項目的 VLAN ID |

:::warning
每個交換器晶片可儲存的 MAC 位址數量有限，請參閱 Introduction 表格以瞭解特定主機表大小。一旦主機表已滿，可使用不同技術來處理這種情況，例如，交換器可以移除較舊的項目，以騰出空間給較新的 MAC 位址（用於 QCA-8337 和 Atheros-8327 交換器晶片）；另一種做法是直接忽略新的 MAC 位址，並只在逾時後移除項目（用於 Atheros8316、Atheros8227、Atheros-7240、ICPlus175D 和 Realtek-RTL8367 交換器晶片）；最後一種做法是前兩種的組合，只允許特定數量的項目更新，並保留其他主機部分直到逾時（用於 MediaTek-MT7621、MT7531、EN7523 交換器晶片）。這些技術無法透過設定變更。
:::

:::warning
對於 Atheros8316、Atheros8227 和 Atheros-7240 交換器晶片，當交換群組中至少有一個硬體卸載橋接埠為作用中時，switch-cpu 埠一律會參與主機學習程序。這會讓 switch-cpu 埠從非 HW 卸載介面學習 MAC 位址。當單一橋接同時包含 HW 與非 HW 卸載介面時，這可能導致封包遺失。此外，即使主機位於不同邏輯網路，只要相同交換群組上使用重複的 MAC 位址，也可能出現封包遺失。建議只有在所有橋接埠都能使用 HW 卸載時才使用 HW 卸載；當一或多個橋接埠無法設定 HW 卸載時，請在所有交換器埠上保持停用。
:::

:::note
交換器晶片 **QCA-8337** 和 **Atheros-8327** 會在以 `forward-reserved-addresses=no` 和 `protocol-mode=stp/rstp` 建立硬體卸載橋接時，自動將保留的群播 MAC 位址（01:80:C2:00:00:0x）加入主機表。這些 MAC 不應由 802.1Q 相容橋接轉送，且對 R/STP 的正確運作至關重要。由於交換器可容納的主機表項目數量有限，這些 MAC 位址只會指派給 VLAN 1。
:::

:::info
若要確保具有這些目的 MAC 位址的封包能正確處理：

- 交換器埠應設為預設 VLAN 1（`default-vlan-id=auto` 或 `default-vlan-id=1`）。
- 若明確設定 VLAN 1，則必須使用獨立 VLAN 學習（`independent-learning=yes`）。
:::

### 規則表 {#rule-table}

Rule table 是非常強大的工具，可根據 L2、L3 和 L4 協定標頭欄位條件，以線速進行封包過濾、轉送和 VLAN 標記。此選單包含已排序的規則清單，就像 `/ip/firewall/filter` 中一樣，因此每個封包都會檢查 ACL 規則，直到找到相符項目為止。如果多條規則都相符，則只會觸發第一條規則。沒有任何動作參數的規則即為接受封包的規則。

每條規則都包含條件部分與動作部分。動作部分由下列參數控制：

| Property | Description |
| :-- | :-- |
| **copy-to-cpu** (*no \| yes*; Default: **no**) | 是否將封包副本傳送至交換器 CPU 埠 |
| **mirror** (*no \| yes*; Default: **no**) | 是否將封包副本傳送至 `mirror-target` 埠 |
| **new-dst-ports** (*name*; Default: **none**) | 依指定變更目的埠，允許多個埠，包括交換器 CPU 埠。空白設定會捨棄封包。未使用此參數時，封包會被接受 |
| **new-vlan-id** (*integer: 0..4095*) | 將 VLAN ID 變更為指定值，若原本沒有 VLAN 標記則新增一個（此屬性僅適用於 **Atheros8316** 和 **88E6393X** 交換器晶片（**注意**：若是 88E6393X 交換器晶片，也需要 vlan-filtering=yes）） |
| **new-vlan-priority** (*integer: 0..7*) | 變更 VLAN 優先順序欄位（priority code point；此屬性僅適用於 **Atheros8327**、**QCA8337** 和 **Atheros8316** 交換器晶片） |
| **rate** (*integer: 0..4294967295*) | 為相符流量設定 ingress 流量限制（每秒位元數），且只能套用於前 32 個規則槽位（此屬性僅適用於 **Atheros8327/QCA8337** 交換器晶片） |
| **redirect-to-cpu** (*no \| yes*; Default: **no**) | 將相符封包的目的埠變更為交換器 CPU |

條件部分由其餘參數控制：

| Property | Description |
| :-- | :-- |
| **disabled** (*no \| yes*；預設：**no**) | 啟用或停用交換器規則 |
| **dscp** (*integer: 0..63*) | 比對封包的 DSCP 欄位 |
| **dst-address** (*IP address/Mask*) | 比對目的 IP 位址與遮罩 |
| **dst-address6** (*IPv6 address/Mask*) | 比對目的 IPv6 位址與遮罩 |
| **dst-mac-address** (*MAC address/Mask*) | 比對目的 MAC 位址與遮罩 |
| **dst-port** (*integer:* *0..65535*) | 比對目的通訊協定埠號或範圍 |
| **flow-label** (*integer:* *0..1048575*) | 比對 IPv6 flow label |
| **mac-protocol** (*802.2 \| arp \| capsman \| dot1x \| homeplug-av \| ip \| ipv6 \| ipx \| lacp \| lldp \| loop-protect \| macsec \| mpls-multicast \| mpls-unicast \| mvrp \| packing-compr \| packing-simple \| pppoe \| pppoe-discovery \| rarp \| romon \| service-vlan \| vlan \| or 0..65535 \| or 0x0000-0xffff*) | 比對由協定名稱或號碼指定的特定 MAC 協定（若有 VLAN 標籤，則會略過） |
| **ports** (*name*) | 規則將套用於接收流量的介面名稱，允許多個埠。若 ports 屬性留空，規則將套用於所有交換器介面 |
| **protocol** (*dccp \| ddp \| egp \| encap \| etherip \| ggp \| gre \| hmp \| icmp \| icmpv6 \| idpr-cmtp \| igmp \| ipencap \| ipip \| ipsec-ah \| ipsec-esp \| ipv6 \| ipv6-frag \| ipv6-nonxt \| ipv6-opts \| ipv6-route \| iso-tp4 \| l2tp \| ospf \| pim \| pup \| rdp \| rspf \| rsvp \| sctp \| st \| tcp \| udp \| udp-lite \| vmtp \| vrrp \| xns-idp \| xtp \| or 0..255*) | 比對由協定名稱或號碼指定的特定 IP 協定 |
| **src-address** (*IP address/Mask*) | 比對來源 IP 位址與遮罩 |
| **src-address6** (*IPv6 address/Mask*) | 比對來源 IPv6 位址與遮罩 |
| **src-mac-address** (*MAC address/Mask*) | 比對來源 MAC 位址與遮罩 |
| **src-port** (*0..65535*) | 比對來源通訊協定埠號或範圍 |
| **switch** (*switch group*) | 比對規則將套用的交換器群組 |
| **traffic-class** (*0..255*) | 比對 IPv6 traffic class |
| **vlan-id** (*0..4095*) | 比對 VLAN ID（此屬性僅適用於 Atheros8316、Atheros8327、QCA8337、88E6393X 交換器晶片） |
| **vlan-header** (*not-present \| present*) | 比對 VLAN 標頭，也就是 VLAN 標頭是否存在（此屬性僅適用於 Atheros8316、Atheros8327、QCA8337、88E6393X 交換器晶片。若是 **88E6393X** 交換器晶片，也需要 vlan-filtering=yes） |
| **vlan-priority** (*0..7*) | 比對 VLAN 優先順序（priority code point） |

:::warning
同一條規則中不能同時存在 IPv4 與 IPv6 特定條件。
:::

:::warning
由於規則表完全在交換器晶片硬體中處理，因此可擁有的規則數量有限。視您在規則中使用的條件數量（MAC 層、IP 層、IPv6、L4 層）而定，作用中規則的數量可能有所不同：Atheros8316 交換器晶片為 8 至 32 條，Atheros8327/QCA8337 交換器晶片為 8 至 92 條，88E6393X 交換器晶片為 42 至 256 條。修改規則集後，您隨時可以執行 `/interface/ethernet/switch/rule/print`，查看清單尾端的規則是否為 'invalid'，這表示那些規則無法放入交換器晶片。
:::

### 埠隔離 {#port-isolation}

Port isolation 可讓您劃分（隔離）網路的特定部分。當您需要確保特定設備無法存取其他設備時，這很有用。您可以透過隔離交換器埠來達成。Port isolation 僅在屬於同一交換器的埠之間生效。自 RouterOS v6.43 起，所有交換器晶片皆可使用交換器埠隔離。

| Property | Description |
| :-- | :-- |
| **forwarding-override** (*interface*；預設： ) | 強制將 ingress 流量轉送至特定介面。可以逗號分隔指定多個介面。 |

:::info
(R/M)STP 僅在 PVLAN 設定中才會正常運作。若設定中有多個隔離交換器群組，(R/M)STP 將無法正常運作，因為交換器群組可能無法正確接收 BPDU，因此無法偵測網路迴圈。
:::

:::warning
`forwarding-override` 屬性只會影響 ingress 流量。未指定 `forwarding-override` 的交換器埠可以透過所有交換器埠傳送封包。
:::

:::warning
支援 VLAN 表的交換器晶片（**QCA8337**、**Atheros8327**、**Atheros8316**、**Atheros8227** 與 **Atheros7240**）在交換器埠啟用 VLAN 查詢時（將 `vlan-mode` 設為 `fallback`、`check` 或 `secure`），可以覆寫埠隔離設定。如果同一 VLAN 中的埠之間需要額外的埠隔離，可以實作具有 new-dst-ports 屬性的交換器規則。其他不支援交換器規則的設備無法克服此限制。
:::

#### Private VLAN

在某些情境中，你可能需要將所有流量轉送至 uplink 埠，同時讓其他所有埠彼此隔離。這種設定稱為 **Private VLAN** 設定。**Switch** 會將所有 Ethernet 訊框直接轉送至 uplink 埠，讓 **Router** 可以篩選不需要的封包，並限制交換器埠後方設備之間的存取。

![Port Isolation](/img/ae49133a966da305.webp)

若要設定交換器埠隔離，你需要切換所有必要的埠：

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
預設情況下，bridge 介面的 `protocol-mode` 設為 `rstp`。對某些設備而言，這可能會停用硬體卸載，因為特定交換器晶片不支援此功能。請參閱 [Bridge Hardware Offloading](/docs/bridging-and-switching/switch-chip-features#bridge-hardware-offloading) 一節，以取得支援的功能。
:::

針對每個需要隔離的交換器埠（不包括 uplink 埠）覆寫 egress 埠：

```ros
/interface/ethernet/switch/port-isolation
set ether1 forwarding-override=sfp1
set ether2 forwarding-override=sfp1
set ether3 forwarding-override=sfp1
```

:::warning
可以為單一交換器晶片設定多個 uplink 埠，只要指定多個介面並以逗號分隔即可。
:::

#### 隔離交換器群組 {#isolated-switch-groups}

在某些情境中，你可能需要將一組設備與其他群組隔離。這可透過交換器埠隔離功能完成。當你有多個網路，但想使用單一交換器時，這很有用。透過埠隔離，你可以讓特定交換器埠只能與一組交換器埠通訊。在此範例中，**ether1-3** 上的設備只能與 **ether1-3** 上的設備通訊，而 **ether4-5** 上的設備只能與 **ether4-5** 上的設備通訊（**ether1-3** 無法與 **ether4-5** 通訊）。

:::warning
埠隔離僅適用於屬於同一交換器的成員埠之間。
:::

![Port Isolation 2](/img/af23c24ae48bc2f6.webp)

若要設定隔離交換器群組，必須先切換所有埠：

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
預設情況下，bridge 介面的 `protocol-mode` 設為 `rstp`。對某些設備而言，這可能會停用硬體卸載，因為特定交換器晶片不支援此功能。請參閱 [Bridge Hardware Offloading](/docs/bridging-and-switching/switch-chip-features#bridge-hardware-offloading) 一節，以取得支援的功能。
:::

然後在 `forwarding-override` 屬性中指定你想要加入同一隔離交換器群組的所有埠（不包括你要套用該屬性的埠），例如，若要為 **A** 設備建立隔離交換器群組：

```ros
/interface/ethernet/switch/port-isolation
set ether1 forwarding-override=ether2,ether3
set ether2 forwarding-override=ether1,ether3
set ether3 forwarding-override=ether1,ether2
```

若要為 **B** 設備建立隔離交換器群組：

```ros
/interface/ethernet/switch/port-isolation
set ether4 forwarding-override=ether5
set ether5 forwarding-override=ether4
```

### CPU 流量控制 {#cpu-flow-control}

所有交換器晶片都有一個特殊埠，稱為 **switchX-cpu**。這是交換器晶片的 CPU 埠，用於將流量從交換器晶片轉送至 CPU。此類埠是管理流量與路由功能所需的。預設情況下，交換器晶片會確保這個特殊 CPU 埠不會壅塞，並在超過鏈路容量時傳送 Pause Frames，以確保該埠不會過載。此功能稱為 **CPU Flow Control**。若沒有此功能，對路由或管理用途可能很重要的封包可能會被丟棄。

自 RouterOS v6.43 起，部分使用下列交換器晶片的設備可以停用 CPU Flow Control 功能：QCA8337、Atheros8227、Atheros8327、Atheros7240、Atheros8316、88E6191X 與 88E6393X。其他交換器晶片預設啟用此功能，且無法變更。若要停用 CPU Flow Control，請使用下列指令：

```ros
/interface/ethernet/switch/set switch1 cpu-flow-control=no
```

### 統計資訊 {#statistics}

部分交換器晶片可回報統計資訊，這有助於監控有多少封包從內建交換器晶片傳送至 CPU。這些統計資訊也可用於監控 CPU Flow Control。你可以在下方找到交換器晶片統計資訊的範例：

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

部分設備有多個 CPU 核心，透過獨立的資料通道直接連接到內建交換器晶片。這些設備可以回報是使用哪一條資料通道將封包從交換器晶片轉送至 CPU 埠，或從 CPU 埠轉送至交換器晶片。對於這類設備，每一列會新增一行，第一行代表使用第一條資料通道傳送的資料，第二行代表使用第二條資料線傳送的資料，依此類推。你可以找到具有多條資料通道連接 CPU 與內建交換器晶片的設備之交換器晶片統計資訊範例：

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

## 設定範例 {#setup-examples}

---

:::info
使用安全的 `vlan-mode` 時，請確認你已將所有需要的介面加入 VLAN 表。若要讓路由功能在同一台設備上透過使用安全 `vlan-mode` 的埠正常運作，你需要允許這些埠存取 CPU；這可透過將 switchX-cpu 介面本身加入 VLAN 表來完成。範例請參閱 [Management port](/docs/bridging-and-switching/switch-chip-features#management-access-configuration) 章節。
:::

:::note
可以同時使用內建交換器晶片與 CPU 建立 Switch-Router 設定，讓設備同時作為交換器與路由器。設定範例請參閱 [Switch-Router](/docs/bridging-and-switching/switch-chip-features#inter-vlan-routing) 章節。
:::

:::warning
當允許存取 CPU 時，即表示允許從特定埠存取實際的路由器／交換器。這不一定是你想要的行為。當特定 VLAN ID 與埠被允許存取 CPU 時，請務必實作適當的防火牆篩選規則，以保護你的設備。使用防火牆篩選規則，只允許存取特定服務。
:::

:::warning
具備 **MT7621**、**MT7531**、**EN7523, RTL8367**、**88E6393X**、**88E6191X,** **88E6190** 交換器晶片的設備，在 RouterOS v7 中支援 [HW offloaded vlan-filtering](/docs/bridging-and-switching/switch-chip-features#bridge-vlan-filtering)。`/interface/ethernet/switch` 選單中無法使用 VLAN 相關設定。
:::

:::warning
若要讓 VLAN 相關比對條件或 VLAN 相關動作參數在 **88E6393X** 交換器晶片上生效，你必須在 bridge 介面上啟用 vlan-filtering，並確認這些埠已啟用硬體卸載，否則這些參數不會有任何作用。
:::

### VLAN 範例 1（Trunk 與 Access 埠） {#vlan-example-1-trunk-and-access-ports}

具備 Atheros 交換器晶片的 RouterBOARD 可用於 802.1Q Trunking。RouterOS v6 中，此功能由 **QCA8337, Atheros8316, Atheros8327, Atheros8227** 與 **Atheros7240** 交換器晶片支援。在此範例中，**ether3**、**ether4,** 與 **ether5** 介面為 access 埠，而 **ether2** 為 trunk 埠。各 access 埠的 VLAN ID：ether3 - 200、ether4 - 300、ether5 - 400。

![Access Ports](/img/d235e6fd5caac3d6.webp)

將所需埠橋接在一起：

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
預設情況下，bridge 介面的 `protocol-mode` 設為 `rstp`。對某些設備而言，這可能會停用硬體卸載，因為特定交換器晶片不支援此功能。請參閱 [Bridge Hardware Offloading](/docs/bridging-and-switching/switch-chip-features#bridge-hardware-offloading) 一節，以取得支援的功能。
:::

新增 VLAN 表項目，以允許具有特定 VLAN ID 的訊框在埠之間通過：

```ros
/interface/ethernet/switch/vlan
add ports=ether2,ether3 switch=switch1 vlan-id=200
add ports=ether2,ether4 switch=switch1 vlan-id=300
add ports=ether2,ether5 switch=switch1 vlan-id=400
```

為每個埠指派 `vlan-mode` 與 `vlan-header` 模式，並為每個 access 埠的 ingress 指派 `default-vlan-id`：

```ros
/interface/ethernet/switch/port
set ether2 vlan-mode=secure vlan-header=add-if-missing
set ether3 vlan-mode=secure vlan-header=always-strip default-vlan-id=200
set ether4 vlan-mode=secure vlan-header=always-strip default-vlan-id=300
set ether5 vlan-mode=secure vlan-header=always-strip default-vlan-id=400
```

- 設定 `vlan-mode=secure` 可確保嚴格使用 VLAN 表。
- 為 access 埠設定 `vlan-header=always-strip`，會在訊框離開交換器晶片時移除 VLAN 標頭。
- 為 trunk 埠設定 `vlan-header=add-if-missing`，會為未標記的訊框加入 VLAN 標頭。
- `default-vlan-id` 指定要為 access 埠的未標記 ingress 流量加入哪個 VLAN ID。

:::warning
在 **QCA8337** 與 **Atheros8327** 交換器晶片上，應使用預設的 `vlan-header=leave-as-is` 屬性。交換器晶片會使用 `default-vlan-id` 屬性判斷哪些埠是 access 埠。`default-vlan-id` 只應在 access/hybrid 埠上使用，以指定未標記 ingress 流量要指派到哪個 VLAN。
:::

### VLAN 範例 2（Trunk 與 Hybrid 埠） {#vlan-example-2-trunk-and-hybrid-ports}

VLAN Hybrid 埠可以轉送已標記與未標記的流量。此設定僅受部分 Gigabit 交換器晶片支援（**QCA8337, Atheros8327**）。

![Hybrid Ports](/img/238fa201dac1535f.webp)

將所需的埠交換在一起：

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
預設情況下，bridge 介面的 `protocol-mode` 設為 `rstp`。對某些設備而言，這可能會停用硬體卸載，因為特定交換器晶片不支援此功能。請參閱 [Bridge Hardware Offloading](/docs/bridging-and-switching/switch-chip-features#bridge-hardware-offloading) 一節，以取得支援的功能。
:::

加入 VLAN 表項目，以允許具有特定 VLAN ID 的訊框在埠之間傳遞。

```ros
/interface/ethernet/switch/vlan
add ports=ether2,ether3,ether4,ether5 switch=switch1 vlan-id=200
add ports=ether2,ether3,ether4,ether5 switch=switch1 vlan-id=300
add ports=ether2,ether3,ether4,ether5 switch=switch1 vlan-id=400
```

在交換器埠功能表中，於所有埠設定 `vlan-mode`，並在預計作為 hybrid 的埠上設定 `default-vlan-id`：

```ros
/interface/ethernet/switch/port
set ether2 vlan-mode=secure vlan-header=leave-as-is
set ether3 vlan-mode=secure vlan-header=leave-as-is default-vlan-id=200
set ether4 vlan-mode=secure vlan-header=leave-as-is default-vlan-id=300
set ether5 vlan-mode=secure vlan-header=leave-as-is default-vlan-id=400
```

- `vlan-mode=secure` 可確保嚴格使用 VLAN 表。
- `default-vlan-id` 會定義埠上未標記 ingress 流量的 VLAN。
- 在 QCA8337 與 Atheros8327 晶片中，使用 `vlan-mode=secure` 時，會忽略交換器埠的 `vlan-header` 選項。VLAN 表項目會處理所有 egress 標記／取消標記，並在所有埠上以 `vlan-header=leave-as-is` 的方式運作。這表示進入時有標記的訊框，離開時也會保留標記，只有 `default-vlan-id` 訊框會在 egress 埠取消標記。

### 管理存取設定 {#management-access-configuration}

在這些範例中，會展示多種情境的範例，但每個情境都需要你先切換埠。以下說明如何切換多個埠：

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add interface=ether1 bridge=bridge1 hw=yes
add interface=ether2 bridge=bridge1 hw=yes
```

:::warning
橋接器介面預設會將 `protocol-mode` 設為 `rstp`。對某些設備而言，這可能會停用硬體卸載，因為特定交換器晶片不支援此功能。請參閱 [Bridge Hardware Offloading](/docs/bridging-and-switching/switch-chip-features#bridge-hardware-offloading) 一節，以瞭解支援的功能。
:::

在這些範例中，會假設 **ether1** 是 trunk 埠，而 **ether2** 是 access 埠，設定如下：

```ros
/interface/ethernet/switch/port
set ether1 vlan-header=add-if-missing
set ether2 default-vlan-id=100 vlan-header=always-strip
/interface/ethernet/switch/vlan
add ports=ether1,ether2,switch1-cpu switch=switch1 vlan-id=100
```

#### Tagged

若要讓設備只能從特定 VLAN 存取，你需要在橋接器介面上建立新的 VLAN 介面，並為其指派 IP 位址：

```ros
/interface/vlan
add name=MGMT vlan-id=99 interface=bridge1
/ip/address
add address=192.168.99.1/24 interface=MGMT
```

指定允許從哪些介面存取設備：

```ros
/interface/ethernet/switch/vlan
add ports=ether1,switch1-cpu switch=switch1 vlan-id=99
```

:::warning
在此 VLAN 表項目中僅指定 trunk 埠。無法透過 access 埠允許具標籤流量存取 CPU，因為 access 埠會以指定的 `default-vlan-id` 值標記所有 ingress 流量。
:::

設定 VLAN 表後，可以啟用 `vlan-mode=secure` 來限制對 CPU 的存取：

```ros
/interface/ethernet/switch/port
set ether1 vlan-header=add-if-missing vlan-mode=secure
set ether2 default-vlan-id=100 vlan-header=always-strip vlan-mode=secure
set switch1-cpu vlan-header=leave-as-is vlan-mode=secure
```

#### Untagged

若要讓設備可從 access 埠存取，請建立 VLAN ID 與 `default-vlan-id` 中設定相同的 VLAN 介面，例如 VLAN 100，並為其新增 IP 位址：

```ros
/interface/vlan
add name=VLAN100 vlan-id=100 interface=bridge1
/ip/address
add address=192.168.100.1/24 interface=VLAN100
```

指定允許存取 CPU 的 access（untagged）埠：

```ros
/interface/ethernet/switch/vlan
add ports=ether1,ether2,switch1-cpu switch=switch1 vlan-id=100
```

:::danger
最常見的情況是 access（untagged）埠會搭配 trunk（tagged）埠。若是對 CPU 採 untagged 存取，必須同時指定 access 埠與 trunk 埠。這也會讓 trunk 埠得以存取 CPU。這不一定是所需的結果，因此可能需要在 VLAN  filtering 之上額外設定 Firewall。
:::

設定 VLAN 表後，可以啟用 `vlan-mode=secure` 來限制對 CPU 的存取：

```ros
/interface/ethernet/switch/port
set ether1 vlan-header=add-if-missing vlan-mode=secure
set ether2 default-vlan-id=100 vlan-header=always-strip vlan-mode=secure
set switch1-cpu vlan-header=leave-as-is vlan-mode=secure
```

:::warning
若要在具備 **Atheros7240** 交換器晶片的設備上，使用 untagged 流量設定管理埠，必須為 CPU 埠設定 `vlan-header=add-if-missing`。
:::

#### 從 tagged 埠轉換為 untagged {#untagged-from-tagged-port}

可以允許從 trunk（tagged）埠以 untagged 流量存取設備。若要這麼做，請為 bridge 介面指派 IP 位址：

```ros
/ip/address
add address=10.0.0.1/24 interface=bridge1
```

指定允許存取 CPU 的埠。針對 switch-cpu 與 trunk 埠，請使用 `default-vlan-id` 中所使用的 `vlan-id`，預設為 0 或 1。

```ros
/interface/ethernet/switch/vlan
add ports=ether1,switch1-cpu switch=switch1 vlan-id=1
```

設定 VLAN 表後，可以啟用 `vlan-mode=secure` 以限制對 CPU 的存取：

```ros
/interface/ethernet/switch/port
set ether1 default-vlan-id=1 vlan-header=add-if-missing vlan-mode=secure
set switch1-cpu default-vlan-id=1 vlan-header=leave-as-is vlan-mode=secure
```

:::warning
此設定範例不適用於搭載 **Atheros8316** 與 **Atheros7240** 交換器晶片的設備。對於搭載 **QCA8337** 與 **Atheros8327** 交換器晶片的設備，可以使用任何其他 `default-vlan-id`，只要 switch-cpu 與 trunk 埠上的值相同即可。對於搭載 **Atheros8227** 交換器晶片的設備，只能使用 `default-vlan-id=0`，且 trunk 埠必須使用 `vlan-header=leave-as-is`。
:::

### VLAN 間路由 {#inter-vlan-routing}

許多 MikroTik 設備內建交換器晶片，正確設定後可大幅提升整體吞吐量。搭載交換器晶片的設備可同時做為路由器與交換器使用。這讓你能夠在網路中使用單一設備，而非多部設備。

![Switch Router](/img/b6d5d8808c9eda44.webp)

若要讓此類設定運作，必須將所有需要的埠交換在一起

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether3 hw=yes
```

為每個 VLAN ID 建立 VLAN 介面，並為其指派 IP 位址：

```ros
/interface/vlan
add interface=bridge1 name=VLAN10 vlan-id=10
add interface=bridge1 name=VLAN20 vlan-id=20
/ip/address
add address=192.168.10.1/24 interface=VLAN10
add address=192.168.20.1/24 interface=VLAN20
```

為每個 VLAN 設定 DHCP Server：

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

在設備上啟用 NAT：

```ros
/ip/firewall/nat
add action=masquerade chain=srcnat out-interface=ether1
```

將每個埠加入 VLAN 表，並允許這些埠存取 CPU，讓 DHCP 與路由正常運作：

```ros
/interface/ethernet/switch/vlan
add independent-learning=yes ports=ether2,switch1-cpu switch=switch1 vlan-id=10
add independent-learning=yes ports=ether3,switch1-cpu switch=switch1 vlan-id=20
```

指定每個埠為 access 埠，並在每個埠及 `switch1-cpu` 埠上啟用安全 VLAN 模式：

```ros
/interface/ethernet/switch/port
set ether2 default-vlan-id=10 vlan-header=always-strip vlan-mode=secure
set ether3 default-vlan-id=20 vlan-header=always-strip vlan-mode=secure
set switch1-cpu vlan-mode=secure
```

:::warning
在 **QCA8337** 與 **Atheros8327** 交換器晶片上，應使用預設的 `vlan-header=leave-as-is` 屬性。交換器晶片會使用 `default-vlan-id` 屬性判斷哪些埠是 access 埠。`default-vlan-id` 只應在 access/hybrid 埠上使用，以指定未標記的 ingress 流量要指派給哪個 VLAN。
:::

如果設備具有交換器規則表，則可以在硬體層級限制 VLAN 之間的存取。只要在 VLAN 介面上新增 IP 位址，就會啟用 VLAN 間路由，但可以在硬體層級加以限制，同時保留 DHCP Server 與其他路由器相關服務。若要這麼做，請使用這些 ACL 規則。透過這種組態，可以使用 VLAN 建立隔離的埠群組。

```ros
/interface/ethernet/switch/rule
add dst-address=192.168.20.0/24 new-dst-ports="" ports=ether2 switch=switch1
add dst-address=192.168.10.0/24 new-dst-ports="" ports=ether3 switch=switch1
```

## 另請參閱 {#see-also}

- [Switch Router](/docs/bridging-and-switching/switch-chip-features#inter-vlan-routing)
- [Basic VLAN Switching](/docs/bridging-and-switching/user-guides/basic-vlan-switching)
- [Bridge Hardware Offloading](/docs/bridging-and-switching/switch-chip-features#bridge-hardware-offloading)
- [Spanning Tree Protocol](/docs/bridging-and-switching/user-guides/spanning-tree-protocol)
- [DHCP Snooping and Option 82](/docs/bridging-and-switching/switch-chip-features#dhcp-snooping-and-dhcp-option-82)
- [MTU on RouterBOARD](/docs/hardware/mtu-in-routeros)
- [Layer2 misconfiguration](/docs/bridging-and-switching/user-guides/layer2-misconfiguration)
