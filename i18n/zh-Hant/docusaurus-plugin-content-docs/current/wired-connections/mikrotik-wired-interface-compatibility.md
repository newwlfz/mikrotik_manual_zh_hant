---
sidebar_key: "wired-connections/mikrotik-wired-interface-compatibility"
sidebar_position: 2
title: "MikroTik 有線介面相容性"
sidebar_label: "MikroTik 有線介面相容性"
description: "MikroTik SFP/SFP+/SFP28/QSFP+/QSFP28/QSFP56-DD 相容性"
tags:
  - 'sfp'
  - 'ethernet'
source: https://manual.mikrotik.com/docs/wired-connections/mikrotik-wired-interface-compatibility
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## MikroTik SFP/SFP+/SFP28/QSFP+/QSFP28/QSFP56-DD 相容性 {#mikrotik-sfpsfpsfp28qsfpqsfp28qsfp56-dd-compatibility}

本文介紹 MikroTik 裝置與 SFP、SFP+、SFP28、QSFP+、QSFP28 和 QSFP56-DD 收發器的相容性。文中提供了詳細的相容性表格，可幫助深入瞭解哪些收發器適合與 MikroTik 裝置配合使用。此外，還提供了一些使用 RouterOS CLI 設定不同資料傳輸速率的實用配置示例。有關屬性的更詳細說明，請參閱 [乙太網](./ethernet.md) 使用者手冊。

:::info
MikroTik 裝置與 SFP、SFP+、SFP28、QSFP+、QSFP28 和 QSFP56-DD 模組對其他廠商的裝置沒有任何限制。

雖然 MikroTik 無法保證與所有制造商的模組完全相容，但只要其他廠商的模組和裝置符合收發器多源協定（MSA），它們就應當能與 MikroTik 相容。

**警告：** RouterOS 將停用的 **FEC** 模式作為 SFP28 和 QSFP28 介面的預設設定。為確保與其他廠商裝置成功建立鏈路，您可能需要透過將 FEC 模式配置為 `fec74` 或 `fec91` 來啟用它。更多資訊請參閱 [乙太網](./ethernet.md) 使用者手冊。
:::

### 1G SFP {#1g-sfp}

<WideTable>

|  |  |  |  |  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| **型號** | **[S-RJ01](https://mikrotik.com/product/S-RJ01)** | **[S-85DLC05D](https://mikrotik.com/product/S-85DLC05D-180)** | **[S-31DLC20D](https://mikrotik.com/product/S-31DLC20D-181)** | **[S-3553LC20D](https://mikrotik.com/product/S-3553LC20D)** | **[S-55DLC80D](https://mikrotik.com/product/s_55dlc80d)** | **[S-4554LC80D](https://mikrotik.com/product/s_4554lc80d)** | **[SFP CWDM](https://i.mt.lv/cdn/product_files/splitter_modules_180841.pdf)** | **SFP [1m](https://mikrotik.com/product/SplusDA0001)/[3m](https://mikrotik.com/product/SplusDA0003) DAC** | **[S+AO0005](https://mikrotik.com/product/s_ao0005) AOC** | **SFP28 [1m](https://mikrotik.com/product/xs_da0001)/[3m](https://mikrotik.com/product/xs_da0003) DAC** |
| CCR1072-1G-8S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CCR1036-12G-4S | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CCR1036-8G-2S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CCR1016-12S-1S+ | **+ 1** | **+ 1** | **+ 1** | **+ 1** | **+ 1** | **+ 1** | **+** | **+** | **+** | **+** |
| CCR1009-7G-1C | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CCR1009-8G-1S-1S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CCR1009-7G-1C-1S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CCR2004-1G-2XS-PCIe | **-** | **-** | **-** | **-** | **-** | **-** | **-** | **-** | **-** | **-** |
| CCR2004-1G-12S+2XS | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CCR2004-16G-2S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CCR2116-12G-4S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CCR2216-1G-12XS-2XQ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| RDS2216-2XG-4S+4XS-2XQ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS125-24G-1S | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS305-1G-4S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS309-1G-8S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS312-4C+8XG | **-** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS318-1Fi-15Fr-2S | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS318-16P-2S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CSS318-16G-2S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS320-8P-8B-4S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS326-4C+20G+2Q+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS326-24S+2Q+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS354-48G/P-4S+2Q+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS418-8P-8G-2S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS520-4XS-16XQ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS518-16XS-2XQ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS510-8XS-2XQ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CSS/CRS326-24G-2S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS317-1G-16S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS328-4C-20S-4S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS328-24P-4S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS226-24G-2S+ | **-** | **+ 2** | **+ 2** | **+ 2** | **+ 2** | **+ 2** | **+** | **+** | **+** | **+** |
| CRS212-1G-10S-1S+ | **+ 1** | **+ 1** | **+ 1** | **+ 1** | **+ 1** | **+ 1** | **+** | **+** | **+** | **+** |
| CRS210-8G-2S+ | **-** | **+ 2** | **+ 2** | **+ 2** | **+ 2** | **+ 2** | **+** | **+** | **+** | **+** |
| CRS112-8G/P-4S | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS109-8G-1S | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS106-1C-5S/FiberBox | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| RB5009 | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| RB4011 | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| RB3011 | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| RB2011 | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| L009 | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 14** | **+ 14** | **+ 14** |
| RB260/CSS106 | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| RB922/921 | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| RB953GS | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| hAP AC | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| hAP ax S | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 14** | **+ 14** | **+ 14** |
| hEX PoE/PowerBox Pro | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| hEX S | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| hEX S (2025) | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 14** | **+ 14** | **+ 14** |
| RBFTC11 | **+** | **+ 8** | **+ 8** | **+ 8** | **+ 8** | **+ 8** | **+ 8** | **+ 8** | **+ 8** | **+ 8** |
| FTC11XG | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| FTC21 | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 14** | **+ 14** | **+ 14** |
| LHG XL 52 ac | **-** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| RBD22/D23 mANTBox 52 15s/NetMetal ac² | **-** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| L22/mANTBox ax 15s L23/NetMetal ax | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 14** | **+ 14** | **+ 14** |
| GPEN21 | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CSS610 | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS310-1G-5S-4S+/netFiber 9 | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS310-8G+2S+IN | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS812-8DS-2DQ-2DDQ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS804-4DDQ | **-** | **-** | **-** | **-** | **-** | **-** | **-** | **-** | **-** | **-** |

</WideTable>

### 10G SFP+/25G SFP28 {#10g-sfp25g-sfp28}

<WideTable>

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| **型號** | **[S+RJ10](https://mikrotik.com/product/s_rj10)** | **[S+85DLC03D](https://mikrotik.com/product/Splus85DLC03D)** | **[S+31DLC10D](https://mikrotik.com/product/s_31dlc10d)** | **[S+2332LC10D](https://mikrotik.com/product/Splus2332LC10D)** | **[SFP+ CWDM](https://i.mt.lv/cdn/product_files/splitter_modules_180841.pdf)** | **SFP+ [1m](https://mikrotik.com/product/SplusDA0001)/[3m](https://mikrotik.com/product/SplusDA0003) DAC** | **[S+AO0005](https://mikrotik.com/product/s_ao0005) AOC** | **[Q+BC0003-S+](https://mikrotik.com/product/q_bc0003_s)** | **[XQ+BC0003-XS+](https://mikrotik.com/product/xq_bc0003_xs_)** | **SFP28 [1m](https://mikrotik.com/product/xs_da0001)/[3m](https://mikrotik.com/product/xs_da0003) DAC** | **SFP28 [XS+31LC10D](https://mikrotik.com/product/xs_31lc10d)** | **SFP28 [XS+2733LC15D](https://mikrotik.com/product/xs_2733lc15d)** | **SFP28 [XS+85LC01D](https://mikrotik.com/product/xs_85lc01d)** |
| CCR1072-1G-8S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CCR1036-12G-4S | **-** | **+** | **+** | **+** | **+** | **+** | **+** | **-** | **-** | **+** | **+** | **+** | **+** |
| CCR1036-8G-2S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CCR1016-12S-1S+ | **+ 10** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 1,5** | **+ 1,5** | **+** | **+** | **+** | **+** |
| CCR1009-7G-1C | **-** | **+** | **+** | **+** | **+** | **+** | **+** | **-** | **-** | **+** | **+** | **+** | **+** |
| CCR1009-8G-1S-1S+ | **+ 10** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CCR1009-7G-1C-1S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CCR2004-1G-2XS-PCIe | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CCR2004-1G-12S+2XS | **+ 11** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CCR2004-16G-2S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CCR2116-12G-4S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CCR2216-1G-12XS-2XQ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| RDS2216-2XG-4S+4XS-2XQ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS125-24G-1S | **-** | **+** | **+** | **+** | **+** | **+** | **+** | **-** | **-** | **+** | **+** | **+** | **+** |
| CRS305-1G-4S+ | **+ 7** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CRS309-1G-8S+ | **+ 4** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CRS312-4C+8XG | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CRS318-1Fi-15Fr-2S | **-** | **+** | **+** | **+** | **+** | **+** | **+** | **-** | **-** | **+** | **+** | **+** | **+** |
| CRS318-16P-2S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CSS318-16G-2S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CRS320-8P-8B-4S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS326-4C+20G+2Q+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS326-24S+2Q+ | **+ 6** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS354-48G/P-4S+2Q+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS418-8P-8G-2S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS520-4XS-16XQ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS518-16XS-2XQ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS510-8XS-2XQ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CSS/CRS326-24G-2S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+ 9** | **+ 9** | **+** |
| CRS317-1G-16S+ | **+ 3** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CRS328-4C-20S-4S+ | **+ 10** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CRS328-24P-4S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+ 9** | **+ 9** | **+** |
| CRS226-24G-2S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CRS212-1G-10S-1S+ | **+ 10** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CRS210-8G-2S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CRS112-8G/P-4S | **-** | **+** | **+** | **+** | **+** | **+** | **+** | **-** | **-** | **+** | **+** | **+** | **+** |
| CRS109-8G-1S | **-** | **+** | **+** | **+** | **+** | **+** | **+** | **-** | **-** | **+** | **+** | **+** | **+** |
| CRS106-1C-5S/FiberBox | **-** | **+** | **+** | **+** | **+** | **+** | **+** | **-** | **-** | **+** | **+** | **+** | **+** |
| RB5009 | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| RB4011 | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| RB3011 | **-** | **+** | **+** | **+** | **+** | **+** | **+** | **-** | **-** | **+** | **+** | **+** | **+** |
| RB2011 | **-** | **+** | **+** | **+** | **+** | **+** | **+** | **-** | **-** | **+** | **+** | **+** | **+** |
| L009 | **-** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** |
| RB260/CSS106 | **-** | **+** | **+** | **+** | **+** | **+** | **+** | **-** | **-** | **+** | **+** | **+** | **+** |
| RB922/921 | **-** | **+** | **+** | **+** | **+** | **+** | **+** | **-** | **-** | **+** | **+** | **+** | **+** |
| RB953GS | **-** | **+** | **+** | **+** | **+** | **+** | **+** | **-** | **-** | **+** | **+** | **+** | **+** |
| hAP AC | **-** | **+** | **+** | **+** | **+** | **+** | **+** | **-** | **-** | **+** | **+** | **+** | **+** |
| hAP ax S | **-** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** |
| hEX PoE/PowerBox Pro | **-** | **+** | **+** | **+** | **+** | **+** | **+** | **-** | **-** | **+** | **+** | **+** | **+** |
| hEX S | **-** | **+** | **+** | **+** | **+** | **+** | **+** | **-** | **-** | **+** | **+** | **+** | **+** |
| hEX S (2025) | **-** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** |
| RBFTC11 | **-** | **+ 8** | **+ 8** | **+ 8** | **+ 8** | **+ 8** | **+ 8** | **-** | **-** | **+ 8** | **+ 8** | **+ 8** | **+ 8** |
| FTC11XG | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| FTC21 | **-** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** |
| LHG XL 52 ac | **-** | **+** | **+** | **+** | **+** | **+** | **+** | **-** | **-** | **+** | **+** | **+** | **+** |
| RBD22/D23 mANTBox 52 15s/NetMetal ac² | **-** | **+** | **+** | **+** | **+** | **+** | **+** | **-** | **-** | **+** | **+** | **+** | **+** |
| L22/mANTBox ax 15s L23/NetMetal ax | **-** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** |
| CSS610 | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CRS310-1G-5S-4S+/netFiber 9 | **+ 10** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CRS310-8G+2S+IN | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CRS812-8DS-2DQ-2DDQ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS804-4DDQ | **-** | **-** | **-** | **-** | **-** | **-** | **-** | **-** | **-** | **-** | **-** | **-** | **-** |

</WideTable>

### 40G QSFP+ {#40g-qsfp}

|  |  |  |  |
| :-- | :-- | :-- | :-- |
| **型號** | **QSFP+ [Q+DA0001](https://mikrotik.com/product/q_da0001)** | **[Q+85MP01D](https://mikrotik.com/product/q_85mp01d)** | **[Q+BC0003-S+](https://mikrotik.com/product/q_bc0003_s)** |
| CRS326-4C+20G+2Q+ | **+** | **+** | **+** |
| CRS326-24S+2Q+ | **+** | **+** | **+** |
| CRS354-48G/P-4S+2Q+ | **+** | **+** | **+** |
| CRS504-4XQ-IN | **+** | **+** | **+** |
| CRS504-4XQ-OUT | **+13** | **+** | **+13** |
| CRS510-8XS-2XQ | **+** | **+** | **+** |
| CRS518-16XS-2XQ | **+** | **+** | **+** |
| CRS520-4XS-16XQ | **+** | **+** | **+** |
| CCR2216-1G-12XS-2XQ | **+** | **+** | **+** |
| RDS2216-2XG-4S+4XS-2XQ | **+** | **+** | **+** |
| CRS812-8DS-2DQ-2DDQ | **+** | **+** | **+** |
| CRS804-4DDQ | **+** | **+** | **+** |

### 100G QSFP28 {#100g-qsfp28}

<WideTable>

|  |  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| **型號** | **[XQ+31LC10D](https://mikrotik.com/product/xq_31lc10d)** | **[XQ+31LC02D](https://mikrotik.com/product/xq_31lc02d)** | **[XQ+85MP01D](https://mikrotik.com/product/xq_85mp01d)** | **[XQ+DA0001](https://mikrotik.com/product/xq_da0001)** | **[XQ+DA0003](https://mikrotik.com/product/xq_da0003)** | **[XQ+BC0003-XS+](https://mikrotik.com/product/xq_bc0003_xs_)** | **[XQ+CM0000-XS+](https://mikrotik.com/product/xq_cm0000_xs_)** |
| CRS326-4C+20G+2Q+ | **-** | **-** | **+** | **+** | **+** | **+** | **+** |
| CRS326-24S+2Q+ | **-** | **-** | **+** | **+** | **+** | **+** | **+** |
| CRS354-48G/P-4S+2Q+ | **-** | **-** | **+** | **+** | **+** | **+** | **+** |
| CRS504-4XQ-IN | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS504-4XQ-OUT | **+** | **+** | **+** | **+13** | **+13** | **+13** | **+** |
| CRS510-8XS-2XQ | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS518-16XS-2XQ | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS520-4XS-16XQ | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CCR2216-1G-12XS-2XQ | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| RDS2216-2XG-4S+4XS-2XQ | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS812-8DS-2DQ-2DDQ | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS804-4DDQ | **+** | **+** | **+** | **+** | **+** | **+** | **+** |

</WideTable>

### 400G QSFP56-DD {#400g-qsfp56-dd}

|  |  |  |  |
| :-- | :-- | :-- | :-- |
| **型號** | **[DDQ+DA0001](https://mikrotik.com/product/ddq_da0001)** | **[DDQ+DA0003](https://mikrotik.com/product/ddq_da0003)** | **[DDQ+85MP01D](https://mikrotik.com/product/ddq_85mp01d)** |
| CRS812-8DS-2DQ-2DDQ | **+** | **+** | **+** |
| CRS804-4DDQ | **+** | **+** | **+** |

|  |  |  |
| :-- | :-- | :-- |
| **圖例** |  |  |
| 顏色程式碼： | 不支援 | 請檢視下方註釋 |

:::note
註釋：

1. **CCR1016-12S-1S+**、**CRS212-1G-10S-1S+** - SFP+1 介面在除 10G 以外的任何鏈路速度下都無法工作（不支援 1.25G 光纖收發器）
2. **CRS226-24G-2S+**、**CRS210-8G-2S+**- SFP+1 介面還支援 SFP 1.25G 光纖收發器，SFP+2 僅適用於 10G 收發器/鏈路。
3. **CSS/CRS317-1G-16S+**- 電源控制器最多支援 10 個同時使用的 S+RJ10 模組。
4. **CSS/CRS309-1G-8S+**- 最多支援 4 個同時使用的 S+RJ10 模組。我們不建議在沒有額外散熱的情況下將 S+RJ10 用於被動散熱裝置，因為它們的功耗相對較高，工作溫度也相應較高。
5. **Q+BC0003-S+**、**XQ+BC0003-XS+**- 在 SFP+/SFP28 埠籠中支援 SFP+ 聯結器
6. **CSS/CRS326-24S+2Q+**- 最多支援 12 個同時使用的 S+RJ10 模組
7. **CSS/CRS305-1G-4S+**- 最多支援 2 個同時使用的 S+RJ10 模組。
8. **RBFTC11**- 連線到另一臺裝置的 1G SFP 埠時可正常工作。
9. **XS+31LC10D**、**XS+2733LC15D** - 自 2021 年 10 月起生產的 CSS/CRS326-24G-2S+ 和 CRS328-24P-4S+ 交換器已新增完整支援。
10. **S+RJ10** - 在 SFP+ 埠籠中提供支援。
11. **CCR2004-1G-12S+2XS**- 最多支援 6 個同時使用的 S+RJ10 模組。
12. **CCR2004-1G-2XS-PCIe**- 兩個 SFP28 埠僅支援相同速度（2 x 25G 或 2 x 10G 模式）。
13. **CRS504-4XQ-OUT**- [IP 防護等級從 IP66 降低至 IP54。](https://help.mikrotik.com/docs/display/UM/CRS504-4XQ-OUT#heading-Quickstart)
14. **10G SFP+/25G SFP28 模組** - 裝置 SFP 最高支援 2.5G 速率，需要手動設定速度才能工作。
15. **CRS312-4C+8XG、CRS326-4C+20G+2Q+** - Combo SFP+ 介面支援 1G 和 10G 速度（不支援 2.5G 和 5G）

:::

## S-RJ01 {#s-rj01}

該表說明 S-RJ01 模組安裝在特定 MikroTik 裝置中時可工作的鏈路速率。請僅在啟用自動協商的情況下使用這些模組。不支援強制鏈路速度。它們會協商到正確的雙工模式和最高可能的速率。

|  |  |  |  |
| :-- | :-- | :-- | :-- |
| **型號** | **1000** | **100** | **10** |
| RB5009 | **+** | **+** | **+** |
| RB4011 | **+** | **+** | **+** |
| RB3011 | **+** | **+** | **+** |
| RB922 | **+** | **+** | **+** |
| RB921 | **+** | **+** | **+** |
| hAP ac | **+** | **+** | **+** |
| hEX PoE | **+** | **+** | **+** |
| hEX S | **+** | **-** | **-** |
| RB953 | **+/+** | **-/+** | **-/+** |
| RB2011 | **+** | **-** | **-** |
| RB260/CSS106 | **+** | **-** | **-** |
| RBFTC11 | **+** | **-** | **-** |
| LHG XL 52 ac | **-** | **-** | **-** |
| RBD22/D23 mANTBox 52 15s/NetMetal ac² | **-** | **-** | **-** |
| CRS106 | **+** | **+** | **+** |
| CRS112 | **+** | **+** | **+** |
| CRS125/CRS109 | **+** | **+** | **+** |
| CRS212 | **+** | **+** | **+** |
| CRS226/CRS210 | **-** | **-** | **-** |
| CSS/CRS305-1G-4S+ | **+** | **+** | **+** |
| CSS/CRS309-1G-8S+ | **+** | **+** | **+** |
| CRS318-1Fi-15Fr-2S | **+** | **+** | **+** |
| CRS318-16P-2S+ | **+** | **+** | **+** |
| CSS/CRS326-24G-2S+ | **+** | **+** | **+** |
| CRS354 | **+** | **+** | **+** |
| CSS/CRS328-4C-20S-4S+ | **+** | **+** | **+** |
| CSS/CRS328-24P-4S+ | **+** | **+** | **+** |
| CSS/CRS317-1G-16S+ | **+** | **+** | **+** |
| CRS326-4C+20G+2Q+ | **+** | **+** | **+** |
| CRS326-24S+2Q+ | **+** | **+** | **+** |
| CSS610 | **+** | **+** | **+** |
| FTC11XG | **+** | **+** | **+** |
| CRS310-1G-5S-4S+/netFiber 9 | **+** | **+** | **+** |
| CRS310-8G+2S+IN | **+** | **+** | **+** |
| CCR1009 | **+/+** | **+/+** | **+/+** |
| CCR1016-12S-1S+ | **+** | **+** | **+** |
| CCR1036-12G-4S | **+** | **+** | **+** |
| CCR1036-8G-2S+ | **+** | **+** | **+** |
| CCR1072-1G-8S+ | **+** | **+** | **+** |

:::note
註釋

- 該速率可正常工作：**+**
- 該速率無法工作：**-**
- RB953：SFP1/SFP2
- CCR1009：SFP+/SFP

:::

## 10 千兆乙太網 {#10-gigabit-ethernet}

### S+RJ10 {#srj10}

請**僅在啟用自動協商的 10G SFP+ 埠**中使用這些模組。不支援強制鏈路速度和可配置的鏈路速度通告。它們會協商到正確的雙工模式和最高可能的速率。有關 S+RJ10 模組的正確安裝方法和推薦使用場景，請參閱 [S+RJ10 通用指南](../hardware/s-plus-rj10-general-guidance.md)。

| 速度 | 線纜型別 | S+RJ10 到乙太網埠 |
| :-- | :-- | :-- |
| 10BASE-T | Cat5e/6 | 100m |
| 100BASE-T | Cat5e/6 | 100m |
| 1000BASE-T | Cat5e/6 | 100m |
| 2.5GBASE-T | Cat5e/6 UTP | 100m |
| 2.5GBASE-T | Cat5e/6 STP | 100m |
| 5GBASE-T | Cat5e/6 | 100m |
| 10GBASE-T | Cat6/7 | 30m |

:::info
協商速度在很大程度上取決於所用線纜的質量和長度。

**重要：** S+RJ10 到 S+RJ10 始終會協商到最高可能的速率。
:::

S+RJ10 的最新版本在序列號末尾包含 "/r2"。它帶來以下改進：

- 在 2.5G、5G 和 10G 速度下支援高達 10218 位元組的巨型幀。
- 實際鏈路速度報告。
- DDM 監控（供電電壓、模組溫度）。

| 鏈路速度 | 最大 MTU |
| :-- | --: |
| 10Gbps | 10218 |
| 5Gbps | 10218 |
| 2.5Gbps | 10218 |
| 1000Mbps | 1504 |
| 100Mbps | 1504 |
| 10Mbps | 1504 |

### CRS312-4C+8XG {#crs312-4c8xg}

10GE 埠支援的最大線纜長度。

| 速度 | 線纜型別 | 10 千兆乙太網埠 |
| :-- | :-- | :-- |
| 10BASE-T | Cat5e/6 | 100m |
| 100BASE-T | Cat5e/6 | 100m |
| 1000BASE-T | Cat5e/6 | 100m |
| 2.5GBASE-T | Cat5e/6 | 100m |
| 5GBASE-T | Cat5e/6 | 100m |
| 10GBASE-T | Cat6/7 | 30m |

:::warning
協商速度在很大程度上取決於所用線纜的質量和長度。

**注意：** 10GE 埠在使用強制鏈路速度時不支援半雙工模式。
:::

## SFP 介面與 100M 光收發器的相容性 {#sfp-interface-compatibility-with-100m-optical-transceivers}

所列裝置上的 SFP 介面與[快速乙太網光纖](https://en.wikipedia.org/wiki/Fast_Ethernet#Fiber_optics)鏈路相容。

### 相容裝置（介面） {#compatible-devices-interface}

- CCR1009-7G-1C (combo1)
- CCR1009-7G-1C-1S+ (combo1)
- CRS106-1C-5S (combo1)
- CRS328-4C-20S-4S+ (combo1 - combo4 和 SFP1 - SFP20)
- LHG XL 52 ac
- RBD22/D23/mANTBox 52 15s/NetMetal ac²

## SFP+ 介面與 1G 光收發器的相容性 {#sfp-interface-compatibility-with-1g-optical-transceivers}

對於帶有同時支援 10G 和 1G 鏈路速率的 SFP+ 介面的 MikroTik 裝置，必須在鏈路兩端裝置的相關介面上設定以下引數。這些設定僅在使用光 SFP 收發器時適用。為使它們以 1G 鏈路速率工作，請使用以下配置：

```ros
# 自 RouterOS v7.12 起
/interface/ethernet/set sfp-sfpplus1 auto-negotiation=no speed=1G-baseX

# 较早版本的 RouterOS
/interface/ethernet/set sfp-sfpplus1 auto-negotiation=no speed=1Gbps full-duplex=yes 
```

- 停用自動協商。
- 埠速度為 1G。
- 全雙工。

### SFP+ 埠支援 1G 鏈路的裝置 {#devices-which-sfp-ports-support-1g-links}

- CCR2004-1G-12S+2XS - 如有需要，所有 SFP+ 介面均可用於 1G 模式。
- CCR2004-16G-2S+ - 如有需要，所有 SFP+ 介面均可用於 1G 模式。
- CCR1072-1G-8S+ - 如有需要，所有 SFP+ 介面均可用於 1G 模式。
- CCR1036-8G-2S+ - 如有需要，所有 SFP+ 介面均可用於 1G 模式。
- CCR1009-8G-1S-1S+ - 如有需要，所有 SFP+ 介面均可用於 1G 模式。
- CCR1009-7G-1C-1S+ - 如有需要，所有 SFP+ 介面均可用於 1G 模式。
- CSS3xx 系列交換器 - 如有需要，所有 SFP+ 介面均可用於 1G 模式。
- CRS3xx 系列交換器 - 如有需要，所有 SFP+ 介面均可用於 1G 模式。
- RB5009 系列 - 如有需要，SFP+1 介面可用於 1G 模式。
- RB4011 系列 - 如有需要，SFP+1 介面可用於 1G 模式。
- CRS226-24G-2S+ - 僅 SFP+1 支援 1G 鏈路速度，SFP+2 僅用於 10G 鏈路。
- CRS210-8G-2S+ - 僅 SFP+1 支援 1G 鏈路速度，SFP+2 僅用於 10G 鏈路。
- CSS610 系列交換器 - 如有需要，所有 SFP+ 介面均可用於 1G 模式。
- FTC11XG - 如有需要，SFP+1 介面可用於 1G 模式。

### SFP+ 介面僅可用於 10G 鏈路的裝置 {#devices-which-sfp-interfaces-can-be-used-only-for-10g-links}

- CCR1016-12S-1S+
- CRS212-1G-10S-1S+

## SFP+ 介面與 10G/25G 光收發器的相容性 {#sfp-interface-compatibility-with-10g25g-optical-transceivers}

帶有 SFP+ 埠的 MikroTik 裝置可使用 10G/25G 光纖收發器建立 10G 鏈路；但是，必須配置額外的 SFP Rate Select 設定，以避免傳輸過程中發生資料損壞。SFP+ 介面上需要以下設定：

```ros
# 自 RouterOS v7.12 起
/interface/ethernet/set sfp-sfpplus1 auto-negotiation=no speed=10G-baseSR-LR sfp-rate-select=low

# 较早版本的 RouterOS
/interface/ethernet/set sfp-sfpplus1 auto-negotiation=no speed=10Gbps full-duplex=yes sfp-rate-select=low
```

此要求適用於以下 MikroTik 10G/25G 模組：

- XS+31LC10D
- XS+2733LC15D

## SFP+/SFP28 介面與 2.5G 收發器的相容性 {#sfpsfp28-interface-compatibility-with-25g-transceivers}

自 RouterOS v7.3 起已支援 2.5G 鏈路速率。支援 2.5G 鏈路速率的、帶有 SFP+ 和 SFP28 介面的 MikroTik 裝置需要在鏈路兩端的裝置介面上設定以下配置。

```ros
# 自 RouterOS v7.12 起
/interface/ethernet/set sfp-sfpplus1 auto-negotiation=no speed=2.5G-baseX

# 较早版本的 RouterOS
/interface/ethernet/set sfp-sfpplus1 auto-negotiation=no speed=2.5Gbps full-duplex=yes
```

- 停用自動協商。
- 埠速度為 2.5G。
- 全雙工。

### 在 SFP/SFP+/SFP28 埠上支援 2.5G 鏈路的裝置 {#devices-which-support-25g-links-in-sfpsfpsfp28-ports}

- CRS3xx 系列交換器 - 如有需要，所有 SFP+ 介面均可用於 2.5G 模式。
- CCR2004-1G-12S+2XS - 如有需要，所有 SFP+ 和 SFP28 介面均可用於 2.5G 模式。
- CCR2116-12G-4S+ - 如有需要，所有 SFP+ 介面均可用於 2.5G 模式。
- CRS5xx 系列 - 如有需要，所有 SFP28 介面均可用於 2.5G 模式。
- CCR2216-1G-12XS-2XQ - 如有需要，所有 SFP28 介面均可用於 2.5G 模式。
- RB5009 系列 - 如有需要，SFP+ 介面可用於 2.5G 模式。
- L009 系列 - 如有需要，SFP 介面可用於 2.5G 模式。
- L23 系列 - 如有需要，SFP 介面可用於 2.5G 模式。
- CSS610 系列交換器 - 如有需要，所有 SFP+ 介面均可用於 2.5G 模式。
- FTC11XG - 如有需要，SFP+1 介面可用於 2.5G 模式。
- E60/E62 - 如有需要，SFP 介面可用於 2.5G 模式。

## QSFP+/QSFP28/QSFP56/QSFP56-DD 介面支援的鏈路速率 {#qsfpqsfp28qsfp56qsfp56-dd-interface-supported-link-rates}

在 RouterOS 中，QSFP+、QSFP28、QSFP56 和 QSFP56-DD 介面旨在透過利用多個通道來處理高速資料傳輸。每個 QSFP+、QSFP28 或 QSFP56 介面分為四個子介面，QSFP56-DD 分為八個子介面，每個子介面對應正常執行所需的一個傳輸通道。

:::info
QSFP+、QSFP28、QSFP56 和 QSFP56-DD 子介面的命名約定包括兩部分：

- “qsfpplus”、“qsfp28-”、“qsfp56-”或“qsfp56-dd-”後面的第一位數字表示 QSFP+、QSFP28、QSFP56 或 QSFP56-DD 物理埠。
- 第二位數字表示各個獨立通道：對於 QSFP+、QSFP28、QSFP56，範圍為 1 到 4；對於 QSFP56-DD，範圍為 1 到 8。

:::

以下示例展示了 QSFP+、QSFP28、QSFP56 和 QSFP56-DD 介面在 RouterOS 中的顯示方式：

```ros
# QSFP+
/interface/ethernet/print
Flags: R - RUNNING
Columns: NAME, MTU, MAC-ADDRESS, ARP, SWITCH
 #   NAME            MTU  MAC-ADDRESS        ARP      SWITCH 
 1   qsfpplus1-1    1500  48:8F:5A:B6:09:8C  enabled  switch1
 2   qsfpplus1-2    1500  48:8F:5A:B6:09:8D  enabled  switch1
 3   qsfpplus1-3    1500  48:8F:5A:B6:09:8E  enabled  switch1
 4   qsfpplus1-4    1500  48:8F:5A:B6:09:8F  enabled  switch1

# QSFP28
/interface/ethernet/print
Flags: R - RUNNING
Columns: NAME, MTU, MAC-ADDRESS, ARP, SWITCH
 #   NAME         MTU  MAC-ADDRESS        ARP      SWITCH 
 1   qsfp28-1-1  1500  DC:2C:6E:9E:11:14  enabled  switch1
 2   qsfp28-1-2  1500  DC:2C:6E:9E:11:15  enabled  switch1
 3   qsfp28-1-3  1500  DC:2C:6E:9E:11:16  enabled  switch1
 4   qsfp28-1-4  1500  DC:2C:6E:9E:11:17  enabled  switch1

# QSFP56
/interface/ethernet/print
Flags: R - RUNNING; S - SLAVE
Columns: NAME, MTU, MAC-ADDRESS, ARP, SWITCH
 #   NAME            MTU  MAC-ADDRESS        ARP      SWITCH 
 2   qsfp56-1-1     1500  04:F4:1C:1A:82:A1  enabled  switch1
 3   qsfp56-1-2     1500  04:F4:1C:1A:82:A2  enabled  switch1
 4   qsfp56-1-3     1500  04:F4:1C:1A:82:A3  enabled  switch1
 5   qsfp56-1-4     1500  04:F4:1C:1A:82:A4  enabled  switch1

# QSFP56-DD
/interface/ethernet/print
Flags: R - RUNNING; S - SLAVE
Columns: NAME, MTU, MAC-ADDRESS, ARP, SWITCH
 #    NAME            MTU  MAC-ADDRESS        ARP      SWITCH
 10   qsfp56-dd-1-1  1500  04:F4:1C:1A:82:91  enabled  switch1
 11   qsfp56-dd-1-2  1500  04:F4:1C:1A:82:92  enabled  switch1
 12   qsfp56-dd-1-3  1500  04:F4:1C:1A:82:93  enabled  switch1
 13   qsfp56-dd-1-4  1500  04:F4:1C:1A:82:94  enabled  switch1
 14   qsfp56-dd-1-5  1500  04:F4:1C:1A:82:95  enabled  switch1
 15   qsfp56-dd-1-6  1500  04:F4:1C:1A:82:96  enabled  switch1
 16   qsfp56-dd-1-7  1500  04:F4:1C:1A:82:97  enabled  switch1
 17   qsfp56-dd-1-8  1500  04:F4:1C:1A:82:98  enabled  switch1
```

這些子介面的配置和監控可能因自動協商、通告速度以及收發器型別（例如分支線纜或單纖）等因素而異。以下各節將針對每種使用場景提供所需配置的指導。

:::warning
停用或啟用任一物理埠子介面都會觸發整個埠組重新配置，並重啟所有通道。
:::

### QSFP+ {#qsfp}

對於 MikroTik CRS3xx 系列裝置，QSFP+ 介面支援以下鏈路速度：

- 1x 40G
- 4x 10G
- 4x 1G

#### 鏈路配置 {#link-configuration}

- **40G**：可使用自動協商或強制 40G 速度進行配置。
- **4x10G 和 4x1G**：必須設定為強制速度模式並停用自動協商。

從 RouterOS 7.12 版本開始，除了選擇正確的傳輸速率外，還必須指定正確的鏈路模式。例如，DAC（Direct Attach Copper，直連銅纜）可使用 **CR4**，光纖可使用 **SR4-LR4**。

#### 配置示例 {#configuration-examples}

*適用於 RouterOS v7.12 及更高版本：*

```ros
# 1x40G - DAC
/interface/ethernet/set qsfpplus1-1 auto-negotiation=no speed=40G-baseCR4

# 1x40G - Optical
/interface/ethernet/set qsfpplus1-1 auto-negotiation=no speed=40G-baseSR4-LR4

# 4x10G - DAC
/interface/ethernet/set qsfpplus1-1 auto-negotiation=no speed=10G-baseCR
/interface/ethernet/set qsfpplus1-2 auto-negotiation=no speed=10G-baseCR
/interface/ethernet/set qsfpplus1-3 auto-negotiation=no speed=10G-baseCR
/interface/ethernet/set qsfpplus1-4 auto-negotiation=no speed=10G-baseCR  

# 4x10G - Optical
/interface/ethernet/set qsfpplus1-1 auto-negotiation=no speed=10G-baseSR-LR
/interface/ethernet/set qsfpplus1-2 auto-negotiation=no speed=10G-baseSR-LR
/interface/ethernet/set qsfpplus1-3 auto-negotiation=no speed=10G-baseSR-LR
/interface/ethernet/set qsfpplus1-4 auto-negotiation=no speed=10G-baseSR-LR  
```

:::warning
在單鏈路模式下，只需配置第一個 QSFP+ 子介面，其餘子介面應保持啟用。
:::

*適用於低於 v7.12 的 RouterOS 版本：*

```routeros
# 1x40G - DAC/Optical
/interface/ethernet/set qsfpplus1-1 auto-negotiation=no speed=40Gbps full-duplex=yes

# 4x10G - DAC/Optical
/interface/ethernet/set qsfpplus1-1 auto-negotiation=no speed=10Gbps full-duplex=yes
/interface/ethernet/set qsfpplus1-2 auto-negotiation=no speed=10Gbps full-duplex=yes
/interface/ethernet/set qsfpplus1-3 auto-negotiation=no speed=10Gbps full-duplex=yes
/interface/ethernet/set qsfpplus1-4 auto-negotiation=no speed=10Gbps full-duplex=yes 
```

### QSFP28 {#qsfp28}

對於 MikroTik CRS5xx 系列和 CCR2216 裝置，QSFP28 介面支援以下鏈路速度：

- 1x 100G。
- 2x 50G（自 RouterOS v7.12 起可用）。
- 1x 40G。
- 4x 25G。
- 4x 10G。
- 4x 1G。

:::warning
不支援：單通道 50G、2x 40G
:::

#### 鏈路配置 {#link-configuration-1}

- **100G**：可使用自動協商或強制 100G 速度進行配置。
- **2x50G、1x40G、4x25G、4x10G 和 4x1G**：必須設定為強制速度模式並停用自動協商。

從 RouterOS 7.12 版本開始，除了選擇正確的傳輸速率外，還必須指定正確的鏈路模式。例如，DAC（Direct Attach Copper，直連銅纜）可使用 **CR4**，光纖可使用 **SR4-LR4**。

#### 配置示例 {#configuration-examples-1}

*適用於 RouterOS v7.12 及更高版本：*

```ros
# 1x100G - DAC
/interface/ethernet/set qsfp28-1-1 auto-negotiation=no speed=100G-baseCR4

# 1x100G - Optical
/interface/ethernet/set qsfp28-2-1 auto-negotiation=no speed=100G-baseSR4-LR4

# 2x50G - DAC
/interface/ethernet/set qsfp28-1-1 auto-negotiation=no speed=50G-baseCR2
/interface/ethernet/set qsfp28-1-3 auto-negotiation=no speed=50G-baseCR2

# 2x50G - Optical
/interface/ethernet/set qsfp28-1-1 auto-negotiation=no speed=50G-baseSR2-LR2
/interface/ethernet/set qsfp28-1-3 auto-negotiation=no speed=50G-baseSR2-LR2

# 4x25G - DAC
/interface/ethernet/set qsfp28-1-1 auto-negotiation=no speed=25G-baseCR
/interface/ethernet/set qsfp28-1-2 auto-negotiation=no speed=25G-baseCR
/interface/ethernet/set qsfp28-1-3 auto-negotiation=no speed=25G-baseCR
/interface/ethernet/set qsfp28-1-4 auto-negotiation=no speed=25G-baseCR

# 4x25G - Optical
/interface/ethernet/set qsfp28-1-1 auto-negotiation=no speed=25G-baseSR-LR
/interface/ethernet/set qsfp28-1-2 auto-negotiation=no speed=25G-baseSR-LR
/interface/ethernet/set qsfp28-1-3 auto-negotiation=no speed=25G-baseSR-LR
/interface/ethernet/set qsfp28-1-4 auto-negotiation=no speed=25G-baseSR-LR
```

:::warning
在單鏈路模式下，只需配置第一個 QSFP28 子介面，其餘子介面應保持啟用。同樣，對於 2x50G 鏈路模式，只需配置主介面（例如 qsfp28-1-1 和 qsfp28-1-3），但其他子介面必須保持啟用。
:::

*適用於低於 v7.12 的 RouterOS 版本：*

```ros
# 1x100G - DAC/Optical
/interface/ethernet/set qsfp28-1-1 auto-negotiation=no speed=100Gbps full-duplex=yes

# 4x25G - DAC/Optical
/interface/ethernet/set qsfp28-1-1 auto-negotiation=no speed=25Gbps full-duplex=yes
/interface/ethernet/set qsfp28-1-2 auto-negotiation=no speed=25Gbps full-duplex=yes
/interface/ethernet/set qsfp28-1-3 auto-negotiation=no speed=25Gbps full-duplex=yes
/interface/ethernet/set qsfp28-1-4 auto-negotiation=no speed=25Gbps full-duplex=yes
```

### QSFP56 {#qsfp56}

對於 MikroTik CRS812 裝置，QSFP56 介面支援以下鏈路速度：

- 1x 200G
- 2x 100G
- 4x 50G
- 2x 50G
- 1x 40G
- 4x 25G
- 4x 10G
- 4x 1G

#### 鏈路配置 {#link-configuration-2}

- **2x100G、4x50G、1x100G、2x50G、1x40G、4x25G、4x10G 和 4x1G**：必須設定為強制速度模式並停用自動協商。

必須指定正確的鏈路模式。例如，DAC（Direct Attach Copper，直連銅纜）可使用 **CR4**，光纖可使用 **SR4-LR4**。

#### 配置示例 {#configuration-examples-2}

```ros
# 1x200G - DAC
/interface/ethernet/set qsfp56-1-1 auto-negotiation=no speed=200G-baseCR4

# 1x200G - Optical
/interface/ethernet/set qsfp56-1-1 auto-negotiation=no speed=200G-baseSR4-LR4

# 2x100G - DAC
/interface/ethernet/set qsfp56-1-1 auto-negotiation=no speed=100G-baseCR2
/interface/ethernet/set qsfp56-1-3 auto-negotiation=no speed=100G-baseCR2

# 2x100G - Optical
/interface/ethernet/set qsfp56-1-1 auto-negotiation=no speed=100G-baseSR2-LR2
/interface/ethernet/set qsfp56-1-3 auto-negotiation=no speed=100G-baseSR2-LR2

# 4x50G - DAC
/interface/ethernet/set qsfp56-1-1 auto-negotiation=no speed=50G-baseCR
/interface/ethernet/set qsfp56-1-2 auto-negotiation=no speed=50G-baseCR
/interface/ethernet/set qsfp56-1-3 auto-negotiation=no speed=50G-baseCR
/interface/ethernet/set qsfp56-1-4 auto-negotiation=no speed=50G-baseCR

# 4x50G - Optical
/interface/ethernet/set qsfp56-1-1 auto-negotiation=no speed=50G-baseSR-LR
/interface/ethernet/set qsfp56-1-2 auto-negotiation=no speed=50G-baseSR-LR
/interface/ethernet/set qsfp56-1-3 auto-negotiation=no speed=50G-baseSR-LR
/interface/ethernet/set qsfp56-1-4 auto-negotiation=no speed=50G-baseSR-LR

# 1x100G - DAC
/interface/ethernet/set qsfp56-1-1 auto-negotiation=no speed=100G-baseCR4

# 1x100G - Optical
/interface/ethernet/set qsfp56-1-1 auto-negotiation=no speed=100G-baseSR4-LR4

# 2x50G - DAC
/interface/ethernet/set qsfp56-1-1 auto-negotiation=no speed=50G-baseCR2
/interface/ethernet/set qsfp56-1-3 auto-negotiation=no speed=50G-baseCR2

# 2x50G - Optical
/interface/ethernet/set qsfp56-1-1 auto-negotiation=no speed=50G-baseSR2-LR2
/interface/ethernet/set qsfp56-1-3 auto-negotiation=no speed=50G-baseSR2-LR2

# 4x25G - DAC
/interface/ethernet/set qsfp56-1-1 auto-negotiation=no speed=25G-baseCR
/interface/ethernet/set qsfp56-1-2 auto-negotiation=no speed=25G-baseCR
/interface/ethernet/set qsfp56-1-3 auto-negotiation=no speed=25G-baseCR
/interface/ethernet/set qsfp56-1-4 auto-negotiation=no speed=25G-baseCR

# 4x25G - Optical
/interface/ethernet/set qsfp56-1-1 auto-negotiation=no speed=25G-baseSR-LR
/interface/ethernet/set qsfp56-1-2 auto-negotiation=no speed=25G-baseSR-LR
/interface/ethernet/set qsfp56-1-3 auto-negotiation=no speed=25G-baseSR-LR
/interface/ethernet/set qsfp56-1-4 auto-negotiation=no speed=25G-baseSR-LR
```

### QSFP56-DD {#qsfp56-dd}

對於 MikroTik CRS812 和 CRS804 裝置，QSFP56-DD 介面支援以下鏈路速度：

- 1x 400G
- 2x 200G
- 4x 100G
- 8x 50G
- 8x 25G
- 2x 40G
- 8x 10G
- 8x 1G

#### 鏈路配置 {#link-configuration-3}

- **400G**：可使用自動協商或強制 400G 速度進行配置。
- **2x200G、4x100G、8x50G、8x25G、2x40G、8x10G 和 8x1G**：必須設定為強制速度模式並停用自動協商。

必須指定正確的鏈路模式。例如，DAC（Direct Attach Copper，直連銅纜）可使用 **CR8**，光纖可使用 **SR8-LR8**。

#### 配置示例 {#configuration-examples-3}

```ros
# 1x400G - DAC
/interface/ethernet/set qsfp56-dd-1-1 auto-negotiation=no speed=400G-baseCR8

# 1x400G - Optical
/interface/ethernet/set qsfp56-dd-1-1 auto-negotiation=no speed=400G-baseSR8-LR8

# 2x200G - DAC
/interface/ethernet/set qsfp56-dd-1-1 auto-negotiation=no speed=200G-baseCR4
/interface/ethernet/set qsfp56-dd-1-5 auto-negotiation=no speed=200G-baseCR4

# 2x200G - Optical
/interface/ethernet/set qsfp56-dd-1-1 auto-negotiation=no speed=200G-baseSR4-LR4
/interface/ethernet/set qsfp56-dd-1-5 auto-negotiation=no speed=200G-baseSR4-LR4

# 4x100G - DAC
/interface/ethernet/set qsfp56-dd-1-1 auto-negotiation=no speed=100G-baseCR2
/interface/ethernet/set qsfp56-dd-1-3 auto-negotiation=no speed=100G-baseCR2
/interface/ethernet/set qsfp56-dd-1-5 auto-negotiation=no speed=100G-baseCR2
/interface/ethernet/set qsfp56-dd-1-7 auto-negotiation=no speed=100G-baseCR2

# 4x100G - Optical
/interface/ethernet/set qsfp56-dd-1-1 auto-negotiation=no speed=100G-baseSR2-LR2
/interface/ethernet/set qsfp56-dd-1-3 auto-negotiation=no speed=100G-baseSR2-LR2
/interface/ethernet/set qsfp56-dd-1-5 auto-negotiation=no speed=100G-baseSR2-LR2
/interface/ethernet/set qsfp56-dd-1-7 auto-negotiation=no speed=100G-baseSR2-LR2

# 8x50G - DAC
/interface/ethernet/set qsfp56-dd-1-1 auto-negotiation=no speed=50G-baseCR
/interface/ethernet/set qsfp56-dd-1-2 auto-negotiation=no speed=50G-baseCR
/interface/ethernet/set qsfp56-dd-1-3 auto-negotiation=no speed=50G-baseCR
/interface/ethernet/set qsfp56-dd-1-4 auto-negotiation=no speed=50G-baseCR
/interface/ethernet/set qsfp56-dd-1-5 auto-negotiation=no speed=50G-baseCR
/interface/ethernet/set qsfp56-dd-1-6 auto-negotiation=no speed=50G-baseCR
/interface/ethernet/set qsfp56-dd-1-7 auto-negotiation=no speed=50G-baseCR
/interface/ethernet/set qsfp56-dd-1-8 auto-negotiation=no speed=50G-baseCR

# 8x50G - Optical
/interface/ethernet/set qsfp56-dd-1-1 auto-negotiation=no speed=50G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-2 auto-negotiation=no speed=50G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-3 auto-negotiation=no speed=50G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-4 auto-negotiation=no speed=50G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-5 auto-negotiation=no speed=50G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-6 auto-negotiation=no speed=50G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-7 auto-negotiation=no speed=50G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-8 auto-negotiation=no speed=50G-baseSR-LR

# 8x25G - DAC
/interface/ethernet/set qsfp56-dd-1-1 auto-negotiation=no speed=25G-baseCR
/interface/ethernet/set qsfp56-dd-1-2 auto-negotiation=no speed=25G-baseCR
/interface/ethernet/set qsfp56-dd-1-3 auto-negotiation=no speed=25G-baseCR
/interface/ethernet/set qsfp56-dd-1-4 auto-negotiation=no speed=25G-baseCR
/interface/ethernet/set qsfp56-dd-1-5 auto-negotiation=no speed=25G-baseCR
/interface/ethernet/set qsfp56-dd-1-6 auto-negotiation=no speed=25G-baseCR
/interface/ethernet/set qsfp56-dd-1-7 auto-negotiation=no speed=25G-baseCR
/interface/ethernet/set qsfp56-dd-1-8 auto-negotiation=no speed=25G-baseCR

# 8x25G - Optical
/interface/ethernet/set qsfp56-dd-1-1 auto-negotiation=no speed=25G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-2 auto-negotiation=no speed=25G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-3 auto-negotiation=no speed=25G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-4 auto-negotiation=no speed=25G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-5 auto-negotiation=no speed=25G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-6 auto-negotiation=no speed=25G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-7 auto-negotiation=no speed=25G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-8 auto-negotiation=no speed=25G-baseSR-LR

# 2x40G - DAC
/interface/ethernet/set qsfp56-dd-1-1 auto-negotiation=no speed=40G-baseCR4
/interface/ethernet/set qsfp56-dd-1-5 auto-negotiation=no speed=40G-baseCR4

# 2x40G  - Optical
/interface/ethernet/set qsfp56-dd-1-1 auto-negotiation=no speed=40G-baseSR4-LR4
/interface/ethernet/set qsfp56-dd-1-5 auto-negotiation=no speed=40G-baseSR4-LR4

# 8x10G - DAC
/interface/ethernet/set qsfp56-dd-1-1 auto-negotiation=no speed=10G-baseCR
/interface/ethernet/set qsfp56-dd-1-2 auto-negotiation=no speed=10G-baseCR
/interface/ethernet/set qsfp56-dd-1-3 auto-negotiation=no speed=10G-baseCR
/interface/ethernet/set qsfp56-dd-1-4 auto-negotiation=no speed=10G-baseCR
/interface/ethernet/set qsfp56-dd-1-5 auto-negotiation=no speed=10G-baseCR
/interface/ethernet/set qsfp56-dd-1-6 auto-negotiation=no speed=10G-baseCR
/interface/ethernet/set qsfp56-dd-1-7 auto-negotiation=no speed=10G-baseCR
/interface/ethernet/set qsfp56-dd-1-8 auto-negotiation=no speed=10G-baseCR

# 8x10G - Optical
/interface/ethernet/set qsfp56-dd-1-1 auto-negotiation=no speed=10G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-2 auto-negotiation=no speed=10G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-3 auto-negotiation=no speed=10G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-4 auto-negotiation=no speed=10G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-5 auto-negotiation=no speed=10G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-6 auto-negotiation=no speed=10G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-7 auto-negotiation=no speed=10G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-8 auto-negotiation=no speed=10G-baseSR-LR
```

## QSFP+/QSFP28 介面與 breakout 線纜的相容性 {#qsfpqsfp28-interface-compatibility-with-breakout-cables}

MikroTik 裝置可以使用 breakout 線纜在 QSFP+/QSFP28 與 SFP+/SFP28 埠之間建立鏈路。

### 配置示例 {#configuration-examples-4}

*適用於 RouterOS v7.12 及更高版本：*

```ros
# QSFP+ - DAC
/interface/ethernet/set qsfpplus1-1 auto-negotiation=no speed=10G-baseCR
/interface/ethernet/set qsfpplus1-2 auto-negotiation=no speed=10G-baseCR
/interface/ethernet/set qsfpplus1-3 auto-negotiation=no speed=10G-baseCR
/interface/ethernet/set qsfpplus1-4 auto-negotiation=no speed=10G-baseCR

# QSFP+ - Optical
/interface/ethernet/set qsfpplus1-1 auto-negotiation=no speed=10G-baseSR-LR
/interface/ethernet/set qsfpplus1-2 auto-negotiation=no speed=10G-baseSR-LR
/interface/ethernet/set qsfpplus1-3 auto-negotiation=no speed=10G-baseSR-LR
/interface/ethernet/set qsfpplus1-4 auto-negotiation=no speed=10G-baseSR-LR

# QSFP28 - DAC
/interface/ethernet/set qsfp28-1-1 auto-negotiation=no speed=25G-baseCR
/interface/ethernet/set qsfp28-1-2 auto-negotiation=no speed=25G-baseCR
/interface/ethernet/set qsfp28-1-3 auto-negotiation=no speed=25G-baseCR
/interface/ethernet/set qsfp28-1-4 auto-negotiation=no speed=25G-baseCR

# QSFP28 - Optical
/interface/ethernet/set qsfp28-1-1 auto-negotiation=no speed=25G-baseSR-LR
/interface/ethernet/set qsfp28-1-2 auto-negotiation=no speed=25G-baseSR-LR
/interface/ethernet/set qsfp28-1-3 auto-negotiation=no speed=25G-baseSR-LR
/interface/ethernet/set qsfp28-1-4 auto-negotiation=no speed=25G-baseSR-LR

```

也可以使用 QSFP28 轉 2x50G QSFP28 Breakout 線纜：

```routeros
# 2x50G - DAC
/interface/ethernet/set qsfp28-1-1 auto-negotiation=no speed=50G-baseCR2
/interface/ethernet/set qsfp28-1-3 auto-negotiation=no speed=50G-baseCR2

# 2x50G - Optical
/interface/ethernet/set qsfp28-1-1 auto-negotiation=no speed=50G-baseSR2-LR2
/interface/ethernet/set qsfp28-1-3 auto-negotiation=no speed=50G-baseSR2-LR2
```

或者為每個 QSFP+/QSFP28 子介面配置不同的速率：

```routeros
# QSFP28 - DAC
/interface/ethernet/set qsfp28-1-1 auto-negotiation=no speed=25G-baseCR
/interface/ethernet/set qsfp28-1-2 auto-negotiation=no speed=25G-baseCR
/interface/ethernet/set qsfp28-1-3 auto-negotiation=no speed=10G-baseCR
/interface/ethernet/set qsfp28-1-4 auto-negotiation=no speed=10G-baseCR

# QSFP28 - Optical
/interface/ethernet/set qsfp28-1-1 auto-negotiation=no speed=25G-baseSR-LR
/interface/ethernet/set qsfp28-1-2 auto-negotiation=no speed=25G-baseSR-LR
/interface/ethernet/set qsfp28-1-3 auto-negotiation=no speed=10G-baseSR-LR
/interface/ethernet/set qsfp28-1-4 auto-negotiation=no speed=10G-baseSR-LR
```

*適用於低於 v7.12 的 RouterOS 版本：*

```routeros
# QSFP+ - DAC/Optical
/interface/ethernet/set qsfpplus1-1 auto-negotiation=no speed=10Gbps full-duplex=yes
/interface/ethernet/set qsfpplus1-2 auto-negotiation=no speed=10Gbps full-duplex=yes
/interface/ethernet/set qsfpplus1-3 auto-negotiation=no speed=10Gbps full-duplex=yes
/interface/ethernet/set qsfpplus1-4 auto-negotiation=no speed=10Gbps full-duplex=yes

# QSFP28 - DAC/Optical
/interface/ethernet/set qsfp28-1-1 auto-negotiation=no speed=25Gbps full-duplex=yes
/interface/ethernet/set qsfp28-1-2 auto-negotiation=no speed=25Gbps full-duplex=yes
/interface/ethernet/set qsfp28-1-3 auto-negotiation=no speed=25Gbps full-duplex=yes
/interface/ethernet/set qsfp28-1-4 auto-negotiation=no speed=25Gbps full-duplex=yes
```
