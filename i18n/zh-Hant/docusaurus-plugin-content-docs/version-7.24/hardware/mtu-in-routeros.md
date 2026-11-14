---
sidebar_key: "hardware/mtu-in-routeros"
sidebar_position: 5
title: "RouterOS 中的 MTU"
sidebar_label: "RouterOS 中的 MTU"
description: "本頁介紹 MikroTik RouterOS 中的最大傳輸單元 (MTU) 配置，說明其對網路效率和相容性的重要性。內容涵蓋不同的 MTU 型別，包括 Layer-2/L3 MTU 和完整幀 MTU，並詳細說明各種 RouterBoard 型號所支援的取值。"
tags:
  - 'mtu'
  - 'l2mtu'
source: https://manual.mikrotik.com/docs/7.24/hardware/mtu-in-routeros
captured_at: '2026-11-04T11:29:52+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 簡介 {#introduction}

管理員必須配置最大傳輸單元（MTU），以確保預期的服務和應用能夠在網路中成功部署。換言之，管理員負責配置 MTU 值，使封包大小不超過網路裝置的能力。

最初，MTU 的引入是由於高誤位元速率和低通訊速度。對資料流進行分片，可以只重傳損壞的分片而不是整個資料流，從而糾正損壞錯誤。此外，在調變解調器等低速連線上，傳輸大分片會耗費過多時間，因此只有使用較小的分片才能進行通訊。

如今，誤位元速率已大大降低，通訊速度也顯著提高。這為增大 MTU 值提供了機會。增大 MTU 可減少協定開銷並降低 CPU 利用率，這主要得益於中斷次數的減少。因此，出現了一些非標準幀大小：

- **Giant** 或 **Jumbo** 幀 —— 超過標準（IEEE）乙太網 MTU 的幀。
- **Baby Giant** 或 **Baby Jumbo** 幀 —— 略微大於標準（IEEE）乙太網 MTU 的幀。

如今，乙太網介面支援高於標準的物理 MTU 值已很常見，但這不能想當然。還必須考慮其他網路裝置的能力。例如，如果兩塊帶乙太網介面、支援物理 MTU 1526 的路由器板透過一臺乙太網交換器連線，那麼該交換器也必須支援轉發這些大型乙太網幀，應用才能正常工作。

## 最大傳輸單元 {#maximum-transmission-unit}

|  |  |
| :-- | :-- |
| ![](/img/9536d9b1ecab1e58.webp)  |  Mikrotik RouterOS 可識別幾種型別的 MTU：IP/Layer-3/L3 MTU、MPLS/Layer-2.5/L2.5 MTU、MAC/Layer-2/L2 MTU、完整幀 MTU |

### 完整幀 MTU {#full-frame-mtu}

完整幀 MTU 表示特定介面所傳送幀的實際大小。幀校驗和（FCS）不包含在此數值中，因為當幀到達目的地時，乙太網驅動會立即將其移除。

### MAC/Layer-2/L2 MTU {#maclayer-2l2-mtu}

L2MTU 表示該介面可以傳送的、不含 MAC 頭的幀的最大大小。

在 RouterOS 中，可以在 "/interface" 選單中檢視 L2MTU 值。所有與 Routerboard 相關的乙太網介面、VLAN、Bridge、VPLS 和無線介面均已新增 L2MTU 支援。其中部分介面支援配置 L2MTU 值。所有其他乙太網介面僅在其晶片組與 Routerboard 乙太網相同時才會顯示 L2MTU。

這樣使用者就能檢查所需的配置是否可行。使用者可以利用額外的位元組來承載 VLAN 和 MPLS 標籤，或者簡單地增大介面 MTU 以消除一些不必要的分片。

下表列出了 Mikrotik RouterBoard 支援的 *max-l2mtu*（可在 `/interface/print` 選單中以只讀選項 "max-l2mtu" 的值檢視）：

|  |  |
| :-- | :-- |
| **型號名稱** | **MTU 說明** |
| **RB SXT 系列, RB LHG, RB LDF, PL6411-2nD, PL7411-2nD, RB711 系列, wAP R-2nD, RB912R-2nD-LTm (LtAP mini), RB Metal 系列, RB SXT Lite 系列, RB Groove 系列, Cube Lite60, LHG Lite60** | ether1:2028 |
| **RB SXT G 系列, RB DynaDish, wAP ac, RB QRT 系列, RB711G 系列, RB911G, RB912UAG** | ether1:4076 |
| **RB OmniTik 系列, RB750, RB750UP, RB751U-2HnD, RB951-2n** | ether1:4076; ether2-ether5:2028 |
| **RB OmniTik ac 系列, RB750GL, RB750Gr2** | ether1-ether5:4074 |
| **RB mAP, RB mAP lite, RB cAP, RB wAP** | ether1-ether2:2028 |
| **RB750r2, RB750P-PBr2, RB750UPr2, RB941-2nD, RB951Ui/RB952Ui 系列** | ether1-ether5:2028 |
| **RB750Gr3** | ether1-ether5:2026 |
| **RB751G-2HnD, RB951G-2HnD** | ether1-ether5:4074 |
| **RB962UiGS, RB960PGS** | ether1-ether5:4074; sfp1:4076 |
| **RB LHGG 系列** | ether1:9214 |
| **LHG XL 52 ac** | ether1:9214; sfp1:9214 |
| **RB1100Hx2, RB1100AHx2** | ether1-ether10:9498; ether11:9500; ether12-ether13:9116 |
| **RB4011iGS+ series** | ether1-ether10:9578; sfp-sfpplus1:9982 |
| **CCR1009 系列** | ether1-ether4:10224; ether5-ether8:10226; sfp1:10226; sfp-sfpplus1:10226 |
| **CCR1016 系列** | ether1-ether12:10226; sfp1-sfp12:10226; sfp-sfpplus1:10226 |
| **CCR1036 系列** | ether1-ether12:10226; sfp1-sfp4:10226; sfp-sfpplus1-sfp-sfpplus2:10226 |
| **CCR1072 系列** | ether1:9116; sfp-sfpplus1-sfp-sfpplus8:10226 |
| **CCR2004-1G-12S+2XS** | ether1:9586; sfp-sfpplus1-sfp-sfpplus12:9578; sfp28-1 - sfp28-2:9578 |
| **CCR2004-16G-2S+** | ether1-ether16:9582; sfp-sfpplus1-sfp-sfpplus2:9586 |
| **CCR2116-12G-4S+** | ether1-ether12:9570; ether13:9586; sfp-sfpplus1-sfp-sfpplus4:9570 |
| **CCR2216-1G-12XS-2XQ** | ether1:9586; sfp28-1 - sfp28-12:9570; qsfp28-1-1 - qsfp28-2-4:9570 |
| **CRS109-8G-1S** | ether1-ether8:4064; sfp1:4064 |
| **CRS125-24G-1S** | ether1-ether24:4064; sfp1:4064 |
| **CRS112-8G-4S, CRS112-8P-4S** | ether1-ether8:9204; sfp9-sfp12:9204 |
| **CRS106-1C-5S** | sfp1-sfp5:9204; combo1:9204 |
| **CRS210-8G-2S+** | ether1-ether8:9204; sfp-sfpplus1:9204; sfpplus2:9204 |
| **CRS212-1G-10S-1S+** | ether1:9204; sfp1-sfp10:9204; sfpplus1:9204 |
| **CRS226-24G-2S+** | ether1-ether24:9204; sfp-sfpplus1:9204; sfpplus2:9204 |
| **CRS326-24G-2S+, CSS326-24G-2S+** | ether1-ether24:10218; sfp-sfpplus1:10218; sfpplus2:10218 |
| **CRS317-1G-16S+** | ether1:10218; sfp-sfpplus1-sfp-sfpplus16:10218 |
| **CRS328-24P-4S+** | ether1-ether24:10218; sfp-sfpplus1-sfp-sfpplus4:10218 |
| **CRS328-4C-20S-4S+** | combo1-combo4:10218; sfp1-sfp20:10218; sfp-sfpplus1-sfp-sfpplus4:10218 |
| **CRS305-1G-4S+** | ether1:10218; sfp-sfpplus1-sfp-sfpplus4:10218 |
| **CRS304-4XG** | ether1-ether4:10218; ether5:9676 |
| **CRS309-1G-8S+** | ether1:10218; sfp-sfpplus1-sfp-sfpplus8:10218 |
| **netFiber 9/IN (CRS310-1G-5S-4S+)** | sfp1-sfp5:10218; sfp-sfpplus1-sfp-sfpplus4:10218 |
| **CRS310-8G+2S+IN** | ether1-ether8:10218; sfp-sfpplus1-sfp-sfpplus2:10218 |
| **CRS312-4C+8XG** | combo1-combo4:10218; ether1-ether8:10218; ether9:2028 |
| **netPower 15FR (CRS318-1Fi-15Fr-2S)** | ether1-ether16:10218; sfp1-sfp2:10218 |
| **netPower 16P (CRS318-16P-2S+)** | ether1-ether16:10218; sfp-sfpplus1-sfp-sfpplus2:10218 |
| **CRS326-4C+20G+2Q+** | combo1-combo4:10218; ether1-ether20:10218; qsfpplus1-1-qsfpplus2-4:10218; ether21:2028 |
| **CRS326-24S+2Q+** | sfp-sfpplus1-sfp-sfpplus24:10218; qsfpplus1-1-qsfpplus2-4:10218; ether1:2028 |
| **CRS354-48G-4S+2Q+, CRS354-48P-4S+2Q+** | sfp-sfpplus1-sfp-sfpplus4:10218; qsfpplus1-1-qsfpplus2-4:10218; ether1-ether48:10218; ether49:2028 |
| **CRS418-8P-8G-2S+RM** | ether1-ether16:10218; ether17:9018; sfp-sfpplus1-sfp-sfpplus2: 10218 |
| **CRS504-4XQ-IN** | ether1:2028; qsfp28-1-1 - qsfp28-4-4:10218 |
| **CRS510-8XS-2XQ-IN** | ether1:2028; sfp28-1 - sfp28-8:10218; qsfp28-1-1 - qsfp28-2-4:10218 |
| **CRS518-16XS-2XQ** | ether1:2028; sfp28-1 - sfp28-16:10218; qsfp28-1-1 - qsfp28-2-4:10218 |
| **CRS812-8DS-2DQ-2DDQ-RM** | ether1-ether2:9586; qsfp56-1-1 - qsfp56-2-4:9570; qsfp56-dd-1-1 - qsfp56-dd-2-8:9570; sfp56-1 - sfp56-8:9570 |
| **CSS610-8G-2S+, CSS610-8P-2S+** | ether1-ether8:10218; sfp-sfpplus1-sfp-sfpplus2:10218 |
| **D52G-5HacD2HnD (hAP ac²)** | ether1-ether5:9124 |
| **C52iG-5HaxD2HaxD (hAP ax[^2])** | ether1-ether5:9214 |
| **C53UiG+5HPaxD2HPaxD (hAP ax[^3])** | ether1-ether5:9214 |
| **L41G-2axD (hAP ax lite)** | ether1-ether4:2026 |
| **cAP ac** | ether1-ether2:9124 |
| **GPEN21** | ether1-ether2:10222; sfp1: 10222 |
| **wAP60G, LHG60G** | ether1:9124 |
| **RB260GS 系列, CSS106-5G-1S, CSS106-1G-4P-1S** | ether1-ether5:9198; sfp1:9198 |
| **RBFTC11** | ether1:4046; sfp1:4046 |
| **RBM33G** | ether1-ether3:2026 |
| **RBM11G** | ether1:2026 |
| **RB760iGS** | ether1-ether5:2026; sfp1:2026 |
| **E50UG** | ether1:2048; ether2-ether5:2026 |
| **RB411 系列** | ether1:1526 |
| **RB433 系列, RB450, RB493 系列** | ether1:1526; ether2-ether3:1522 |
| **RB450Gx4** | ether1-ether5:9214 |
| **RB411GL** | ether1:1520 |
| **RB433GL, RB435G, RB450G, RB493G** | ether1-ether3:1520 |
| **RB800** | ether1-ether2:9500; ether3:9116 |
| **RB850Gx2** | ether1-ether5:1580 |
| **RB921UAGS, RB922UAGS** | ether1:4076; sfp1:4076 |
| **D23UGS-5HPacD2HnD (NetMetal ac²)** | ether1:9214; sfp1:9214 |
| **L23UGSR-5HaxD2HaxD (NetMetal ax)** | ether1:8158; sfp1:8158 |
| **RB953GS** | ether1-ether2:4074; sfp1:4074; sfp2:4076 |
| **RB2011 系列** | ether1-ether5:4074; ether6-ether10:2028; sfp1:4074 |
| **RB3011 系列** | ether1-ether5:8156; ether6-ether10:8156; sfp1:8158 |
| **RB5009 系列** | ether1-ether8: 9796; sfp-sfpplus1: 9796 |
| **L009 系列** | ether1: 8158; ether2-ether8: 8154; sfp1: 8154 |
| **RB44Ge** | ether1-ether4:9116 |

RouterOS 中的所有無線介面（包括 Nstreme2）都支援 2290 位元組的 L2MTU。

:::danger
L2MTU 配置變更會因必要的內部處理過程而觸發所有介面過載（link down/link up）。  
建議謹慎配置 L2MTU，並牢記這可能會對所連線的裝置造成短暫中斷。

:::

### MPLS/Layer-2.5/L2.5 MTU {#mplslayer-25l25-mtu}

MPLS MTU 在 `/mpls/interface` 選單中配置，用於指定可透過特定介面傳送的、包含 MPLS 標籤的最大封包大小。

請確保 MPLS MTU 值小於或等於 L2MTU。根據 MPLS 路由器所執行的操作不同，MPLS MTU 對封包的影響也不同。由於 MPLS MTU 對 MPLS 交換封包的影響，強烈建議在組成 MPLS 雲的所有路由器上配置相同的 MPLS MTU 值。這一要求意味著，加入 MPLS 雲的所有介面都必須配置為參與介面中最小的 MPLS MTU 值；因此，在選擇要使用的硬體時必須仔細斟酌。

### MPLS 交換 {#mpls-switching}

當包含 MPLS 標籤的封包超過配置的 MPLS MTU 時，路由器會嘗試判斷 MPLS 幀內承載的協定型別：

- **IP 封包**：如果被封裝的​封包是 IP 封包，MPLS 會生成 ICMP "Need Fragmentation" 錯誤訊息。此行為與標準 IP 協定的處理方式一致。請注意，該 ICMP 錯誤不會直接路由回封包發起者；而是沿標籤交換路徑（LSP）向末端交換，由出口路由器將其路由回源端。

- **非 IP 封包**：如果被封裝的​封包不是 IP 封包，MPLS 會直接將其丟棄，因為路由器無法解析封包內容。此行為對 VPLS 等 MPLS 應用尤為重要，因為穿越 MPLS 網路的幀並非 IP 封包，而是被封裝的乙太網幀。如果 LSP 沿途任一介面上配置的 MPLS MTU 小於入口路由器準備的​封包大小，這些幀將被靜默丟棄。

#### IP 入口 {#ip-ingress}

當路由器首次為 IP 封包壓入標籤，且包含 MPLS 標籤後得到的​封包大小超過 MPLS MTU 時，路由器的行為就如同超出了介面 MTU。它要麼在附加標籤後將封包分片為不超過 MPLS MTU 的分片（如果 IP 的 Don't Fragment 位未置位），要麼生成 ICMP Need Fragmentation 錯誤併發送回發起者。

#### VPLS 入口 {#vpls-ingress}

當路由器封裝乙太網幀以便透過 VPLS 偽線轉發時，它會檢查封包大小（包括 VPLS 控制字（4 位元組）以及任何必要的標籤（通常為 2 個標籤，即增加 8 位元組））是否超過出介面的 MPLS MTU。如果超過，VPLS 會對封包進行分片，使其符合出介面的 MPLS MTU。封包將在 VPLS 偽線的出口點重新組裝。

## 配置示例 {#setup-examples}

在這些示例中，我們將檢視透過乙太網介面進入和離開路由器的幀。

### 簡單路由 {#simple-routing}

該圖顯示了簡單路由情況下的封包 MTU 大小，封包大小不會被修改。

![](/img/ef8a175a467f76f2.webp)

### 帶 VLAN 封裝的路由 {#routing-with-vlan-encap}

每個 VLAN 標籤長度為 4 位元組。VLAN 標籤由路由器新增。L2-MTU 增加 4 位元組。

![](/img/28a6b9c3bc3236ce.webp)

### 帶標籤的簡單 MPLS {#simple-mpls-with-tags}

當 MPLS 用作 IP 路由的簡單替代方案時，每個封包只附加一個標籤，因此封包大小增加 4 位元組。而我們面對的是有兩個 MPLS 標籤的情況。為了能夠在不分片的情況下轉發標準大小（1500 位元組）的 IP 封包，對於兩個 MPLS 標籤，MPLS MTU 必須至少設定為 1508。

![](/img/5e9c949dd091d2e4.webp)

### VPLS 隧道 {#vpls-tunnel}

當對端未直接連線時，會存在兩個 MPLS 標籤。一個 MPLS 標籤用於到達對端；第二個標籤用於標識 VPLS 隧道。

![](/img/89d4d59759cf7056.webp)

## 高階配置示例 {#advanced-setup-examples}

在本示例中，我們將進一步瞭解所有類乙太網介面（包括 Bridge、VLAN 和 VPLS 介面）所需的 L2MTU。

在此配置中，我們將使用 3 臺路由器：

- Q-in-Q 路由器 - 該路由器將接收標準的 1500 位元組乙太網幀，併為封包新增兩個 VLAN 標籤。然後，封包將透過乙太網網路傳送到第二臺路由器。

- VPLS 路由器 - 該路由器將移除外層 VLAN 標籤，並將帶有剩餘 VLAN 標籤的封包與 VPLS 隧道進行橋接。VPLS 隧道將攜帶封包穿過 MPLS 網路到達第三臺路由器。

- MPLS 邊緣路由器 - 將移除 VPLS 和 VLAN 標籤，並將封包橋接到用戶端乙太網網路。

![](/img/84458d44b3e328e4.webp)
