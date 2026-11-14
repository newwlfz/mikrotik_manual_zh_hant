---
sidebar_key: "hardware/product-naming"
sidebar_position: 9
title: "產品命名"
sidebar_label: "產品命名"
description: "MikroTik 產品命名遵循 RouterBOARD 型號的結構化約定，詳細說明板卡系列、有線/無線介面、CPU 核心以及頻段和功率等級等無線特性，幫助使用者快速識別硬體規格。"
tags:
  - 'routerboard'
  - 'product-naming'
  - 'board-features'
source: https://manual.mikrotik.com/docs/hardware/product-naming
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 簡介 {#introduction}

MikroTik 產品命名乍看可能令人困惑，但所有產品程式碼都遵循邏輯命名約定。理解這種命名結構有助於使用者一眼識別關鍵產品特性和規格。本文件解釋 MikroTik 產品程式碼每一段的含義，並提供示例幫助你解讀任何型號。

### RouterBOARD（短版本 RB） {#routerboard-short-version-rb}

`<board name> <board features>-<built-in wireless> <wireless card features>-<connector type>-<enclosure type>`

### 板卡名稱 {#board-name}

目前，板卡名稱可以有三類：

- **3 個符號的名稱**：
  - 第 1 個符號表示系列（可以是數字或字母）；新增：D - Dakota；C - Cypress；S - Chateau；L - Maple；E - Econet；MA - Miami。
  - 第 2 位數字表示潛在有線介面（Ethernet、SFP、SFP+）的數量。
  - 第 3 位數字表示潛在無線介面（內建以及 mPCI 和 mPCIe 插槽）的數量。

- **單詞** - 當前使用的名稱有：**OmniTIK, Groove, SXT, SEXTANT, Metal, LHG, DynaDish, cAP, wAP, LDF, DISC, mANTBox, QRT, hAP, hEX**。如果板卡硬體發生根本性變化（例如完全不同的 CPU），則會在末尾新增修訂版本。

- **特殊情況命名** - 600、800、1000、1100、1200、2011、3011、4011 板卡是系列的獨立代表，或者具有超過 9 個有線介面，因此名稱簡化為整百或開發年份。

### 板卡特性 {#board-features}

板卡特性緊跟在板卡名稱之後，之間沒有空格或破折號分隔。例外情況是板卡名稱為單詞；此時，板卡特性用空格分隔。

使用以下特性，按出現順序列出：

- **U** – USB 埠。
- **P** – 帶控制器的電源注入。
- **i** – 不帶控制器的單埠電源注入器。
- **A** – 額外記憶體和/或更高許可證級別。
- **H** – 更強大的 CPU。
- **G** – 千兆乙太網（可與 U、A 或 H 組合；不與 L 一起使用）。
- **L** – Lite 版。
- **D** – 額外儲存磁碟（SSD 或 M.2）。
- **S** – SFP 埠（SwitchOS 裝置的舊式用法）。
- **e** – PCIe 介面擴充套件卡。
- **xN** – CPU 核心數（例如 x2、x16、x36）。
- **R** – 同時具有 USB 和 PCIe 線路的 MiniPCIe 插槽。
- **M** – 同時具有 USB 和 PCIe 線路的 M.2 插槽。

### 內建無線詳細資訊 {#built-in-wireless-details}

如果板卡具有內建無線，則其所有特性按以下格式表示：

`<band><power_per_chain><protocol><number_of_chains>`

- **band**：
  - **6** - 6GHz。
  - **5** - 5GHz。
  - **2** - 2.4GHz。
  - **52** - 雙頻 5GHz 和 2.4GHz。

- **每條鏈的功率**：
  - （未使用）- “Normal” - 在 6Mbps 802.11a 時 &lt;23dBm。在 6Mbps 802.11g 時 &lt;24dBm。
  - **H** - “High” - 在 6Mbps 802.11a 時為 23-24dBm。在 6Mbps 802.11g 時為 24-27dBm。
  - **HP** - “High Power” - 在 6Mbps 802.11a 時為 25-26dBm。在 6Mbps 802.11g 時為 28-29dBm。
  - **SHP** - “Super High Power” - 在 6Mbps 802.11a 時為 27+dBm。在 6Mbps 802.11g 時為 30+dBm。

- **protocol**：
  - （未使用）- 適用於僅支援 802.11a/b/g 的卡。
  - **n** - 適用於支援 802.11n 的卡。
  - **ac** - 適用於支援 802.11ac 的卡。
  - **ax** - 適用於支援 802.11ax 的卡。
  - **be** - 適用於支援 802.11be 的卡。
  - **bn** - 適用於支援 802.11bn 的介面。

- **number\_of\_chains**：
  - （未使用）- 單鏈。
  - **D** - 雙（2）鏈。
  - **T** - 三（3）鏈。
  - **Q** - 四（4）鏈。
  - **P** - 五（5）鏈。
  - **H** - 六（6）鏈。
  - **S** - 七（7）鏈。
  - **O** - 八（8）鏈。
  - **N** - 九（9）鏈。
  - **E** - “Ene”（10）鏈（因為 “deca” 的 D 已被佔用）。

- **聯結器型別**：
  - （未使用）- 該型號只有一個聯結器選項。
  - **MMCX** - MMCX 聯結器型別。
  - **u.FL** - u.FL 聯結器型別。

### 外殼型別 {#enclosure-type}

- （未使用）- 產品的主要外殼型別。
- **BU** - 板卡單元（無外殼）- 適用於需要僅板卡選項，但主產品已帶外殼的情況。
- **RM** - 機架安裝外殼。
- **IN** - 室內外殼。
- **EM** - 擴充套件記憶體。
- **LM** - 精簡記憶體。
- **BE** - 黑色版外殼。
- **TC** - 塔式（垂直）機箱外殼（用於 hEX、hAP 和其他家用路由器）。
- **OUT** - 室外外殼。

## 更具體的 OUT 外殼型別包括 {#more-specific-types-out-enclosures-are}

- **SA** - 扇區天線外殼（用於 SXT）。
- **HG** - 高增益天線外殼（用於 SXT）。
- **BB** - Basebox 外殼（用於 RB911）。
- **NB** - NetBox 外殼（用於 RB911）。
- **NM** - NetMetal 外殼（用於 RB911）。
- **QRT** - QRT 外殼（用於 RB911）。
- **SX** - Sextant 外殼（用於 RB911、RB711）。
- **SXTsq -**SXTsq 外殼。
- **PB** - PowerBOX 外殼（用於 RB750P、RB950P）。
- **XL** - 特大外殼（例如更大尺寸的 LHG）。
- **LTm** - LtAP mini 機箱。
- **LT** - LtAP 機箱。
- **KN**- KNOT 機箱。

### 示例 {#example}

- RB（RouterBOARD）。
- 912 - 第 9 系列板卡，具有 1 個有線（乙太網）介面和兩個無線介面（內建和 mini PCIe）。
- UAG - 具有 USB 埠、更多記憶體和千兆乙太網埠。
- 5HPnD - 具有內建 5GHz 高功率雙鏈無線卡，支援 802.11n。

## 2 解碼 [RBD52G-5HacD2HnD-TC](https://mikrotik.com/product/hap_ac2) 命名 {#2-decode-rbd52g-5hacd2hnd-tc-naming}

- RouterBOARD（在新產品中已棄用）
- D - Dakota 系列 CPU
- 5 - 有線介面
- 2 - 無線介面
- G - 千兆
- 5HacD - 具有內建 5GHz 高功率雙鏈無線卡，支援 802.11ac。
- 2HnD  - 具有內建 2.4GHz 高功率雙鏈無線卡，支援 802.11n。
- TC - 塔式機箱

## 示例 {#example-1}

# 3 解碼 [C52iG-5HaxD2HaxD-TC](https://mikrotik.com/product/hap_ax2) 命名 {#3-decode-c52ig-5haxd2haxd-tc-naming}

- C - Cypress 系列 CPU。
- 5 - 有線介面。
- 2 - 無線介面。
- i - 不帶控制器的單埠電源注入器。
- G - 千兆。
- 5HaxD - 具有內建 5GHz 高功率雙鏈無線卡，支援 802.11ax。
- 2HaxD - 具有內建 2.4GHz 高功率雙鏈無線卡，支援 802.11ax。
- TC - 塔式機箱。

## CloudCoreRouter 命名詳情 {#cloudcorerouter-naming-details}

CloudCoreRouter（短版本：CCR）的命名由以下部分組成：

`<4 digit number>-<list of ports>-<enclosure type>`

- **4 位數字**：
  - 第 1 位數字表示系列。
  - 第 2 位（保留）。
  - 第 3-4 位數字表示裝置上的 CPU 核心總數。

- **埠列表**：
  - -n**G** 1G 乙太網埠數量。
  - -n**P** 帶 PoE-out 的 1G 乙太網埠數量。
  - -n**C** 組合 1G 乙太網/SFP 埠數量。
  - -n**S** 1G SFP 埠數量。
  - -n**G+** 2.5G 乙太網埠數量。
  - -n**P+** 帶 PoE-out 的 2.5G 乙太網埠數量。
  - -n**C+** 組合 10G 乙太網/SFP+ 埠數量。
  - -n**S+** 10G SFP+ 埠數量。
  - -n**XG** 5G/10G 乙太網埠數量。
  - -n**XP** 帶 PoE-out 的 5G/10G 乙太網埠數量。
  - -n**XC** 組合 10G/25G SFP+ 埠數量。
  - -n**XS** 25G SFP+ 埠數量。
  - -n**Q+** 40G QSFP+ 埠數量。
  - -n**XQ** 100G QSFP+ 埠數量。
  - -n**DQ**  200G QSFP56 埠數量。
  - -n**DDQ** 400G QSFP-DD 埠數量。

- **外殼型別**  - 與 RouterBOARD 產品相同。

## CloudRouterSwitch 和 CloudSmartSwitch 命名詳情 {#cloudrouterswitch-and-cloudsmartswitch-naming-details}

CloudRouterSwitch（短版本 CRS，RouterOS 裝置）和 CloudSmartSwitch（短版本 CSS，SwOS 裝置）的命名由以下部分組成：

`<3 digit number>-<list of ports>-<built-in wireless card>-<enclosure type>`

- **3 位數字**：
  - 第 1 位數字表示系列。
  - 第 2-3 位數字 - 有線介面（Ethernet、SFP、SFP+）總數。

- **埠列表**：
  - -n**F** 100M 乙太網埠數量。
  - -n**Fi** 帶 PoE-out 注入器的 100M 乙太網埠數量。
  - -n**Fp** 帶受控 PoE-out 的 100M 乙太網埠數量。
  - -n**Fr** 帶反向 PoE（PoE-in）的 100M 乙太網埠數量。
  - -n**G** 1G 乙太網埠數量。
  - -n**P** 帶 PoE-out 的 1G 乙太網埠數量。
  - -n**C** 組合 1G 乙太網/SFP 埠數量。
  - -n**S** 1G SFP 埠數量。
  - -n**G+** 2.5G 乙太網埠數量。
  - -n**P+** 帶 PoE-out 的 2.5G 乙太網埠數量。
  - -n**C+** 組合 10G 乙太網/SFP 埠數量。
  - -n**S+** 10G SFP+ 埠數量。
  - -n**XG** 5G/10G 乙太網埠數量。
  - -n**XP** 帶 PoE-out 的 5G/10G 乙太網埠數量。
  - -n**XC** 組合 10G/25G SFP+ 埠數量。
  - -n**XS** 25G SFP+ 埠數量。
  - -n**Q+** 40G QSFP+ 埠數量。
  - -n**XQ** 100G QSFP+ 埠數量。
  - n**DQ**  200G QSFP56 埠數量。
  - -n**DDQ** 400G QSFP-DD 埠數量。
  - `-nP` 表示支援 IEEE 802.3af/at（PoE / PoE+）的 PoE-out 埠。
  - -`<n>B` 表示支援 IEEE 802.3af/at/bt 的 PoE-out 埠（包括 PoE++ / 802.3bt 高功率 PoE）。

- **內建無線卡** - 與 RouterBOARD 產品相同。

- **外殼型別** - 與 RouterBOARD 產品相同。
