---
sidebar_key: "hardware/peripherals"
sidebar_position: 6
title: "外圍裝置"
sidebar_label: "外圍裝置"
description: "本文介紹 RouterBOARD 硬體裝置所支援的附加外設。"
tags:
  - 'cellular-modems'
  - 'peripherals'
  - 'usb'
source: https://manual.mikrotik.com/docs/hardware/peripherals
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本文介紹 RouterBOARD 硬體裝置支援的附加外設。

## 蜂窩調變解調器 {#cellular-modems}

RouterOS v7 支援以下蜂窩調變解調器：

- MikroTik 調變解調器。
- 按裝置類/型別支援的第三方調變解調器：
  - MBIM 類 USB 介面
  - USB-CDC 類 USB 介面
  - RNDIS 型別 USB 介面
- 已新增支援的第三方調變解調器（見下方調變解調器表格）。

## 請注意 {#please-note}

- 並非所有調變解調器都列在支援的調變解調器表中。有些調變解調器即使未列出也可能可用，因為調變解調器製造商通常會重複使用相同的硬體 ID，反之亦然。
- 定製、本地化或鎖定的裝置可能存在相容性問題。
- 第三方調變解調器在用於 RouterOS 之前可能需要調整配置。
- 對於帶有 USB3.0 介面的 mini-PCIe 調變解調器，安裝在支援 PCIe/USB2.0 的 mini-PCIe 插槽中時，必須將 USB 速度限制為 USB2.0，或者必須隔離 mini-PCIe 共享的 PCIe/USB3.0 引腳。請參見表格下方的圖片。

## 蜂窩調變解調器 {#cellular-modems-1}

| 型號 | vendor-id | device-id | 測試的 RouterOS 版本 | 備註 | 格式 |
| :-- | :-- | :-- | :-- | :-- |  :-- |
| Alcatel IK40 |  |  | v6.41RC11 | LTE 介面，調變解調器只能透過調變解調器的配置 WEB 頁面進行配置。 | USB |
| Alcatel IK41 |  |  | v6.48 | 免配置 LTE 介面 | USB |
| Android usb tethering interface |  |  | v6.7 | 部分設定會被忽略。 | USB |
| AnyData ADU-E630WH |  |  | v6 | （又稱 "USB Wireless HSDPA/UMTS 2.1GHz GSM/GPRS/EGPRS 900/17000MHz/CDMA 1x EVDO Rev.A"） | USB |
| Anteniti 3372h-153 |  |  | 7.12 |  | USB |
| BandRich C501 |  |  | v5.25 和 v6.0 |  | USB |
| Cinterion LTE Modem | 0x1e2d | 0x0061 | v7.14 and higher | LTE 介面，部分設定會被忽略。SMS 功能不完整。 | MiniPCI-e |
| D-link DWM-157 | 0x2001 | 0x7d02 | v6.xx | 可用！資料通道：2，資訊通道：3，調變解調器初始化：AT+CFUN=1，vendor-id="0x2001" device-id="0x7d02" 來自調變解調器的一些資訊：> H/W Ver.: B1, F/W Ver.: 2.0.1eu, revision: +CGMR: MOLY.WR8.W1231.DC.WG.MP.V3, 2013/04/09 02:08 不同的硬體版本可能無法與 RouterOS 配合使用 | USB |
| D-link DWM-222 |  |  | 參見備註  | 存在多個具有相同市場名稱的調變解調器版本：H/W ver: A1 - 從 RoS v6.38 起作為免配置 LTE 介面受支援調變解調器韌體版本從 "2.1.4EU" 開始。H/W ver: A3 - 使用調變解調器韌體提供的 RNDIS 介面作為免配置 LTE 工作（僅 RouterOS v7） | USB |
| Dell DW5821e |  |  | v7.4beta4 and higher | MBIM 驅動程式。修訂版本：T77W968.F1.0.0.5.2.VZ.013 044 | M.2 |
| Dell DW5821e-eSIM | 0x413c | 0x81e0 | 7.11 and higher | MBIM 驅動程式。韌體：T77W968.F1.0.0.5.2.GC.013。已新增 "at-chat" 支援 | M.2 |
| DELL T99W175 | 0x05c6 | 0x90d5 | 7.16 and higher | MBIM 驅動程式。韌體：T99W175.F0.1.0.0.9.GC.004。已新增 "at-chat" 支援 | M.2 |
| Dell Wireless 5530 HSPA |  |  | v6.1 and higher | 資料通道 0，資訊通道 0，初始化：AT+CFUN=1（需要透過命令 AT\*ENAP=1,1 手動更改配置檔案） | MiniPCI-e |
| Ericsson F5521gw |  |  | v6.x 及更高版本 |  | MiniPCI-e |
| Fibocom FM150-AE/FM150-NA | 0x2cb7 | 0x0111 | v7.1beta5 | MBIM 驅動程式。修訂版本：89603.1000.00.01.01.03 | M.2 |
| Fibocom NL-952-EAU |  |  | v7.1beta5 | MBIM 驅動程式。修訂版本：19600.7000.00.04.01.05 | M.2 |
| 基於 Marvell PXA1802 的調變解調器 | 0x1286 | 0x4e31 | v7.2.2 |  | mini-PCIe |
| Huawei E153 |  |  | v6.31 及更高版本 |  | USB |
| Huawei E171 |  |  | v6.xx | 可用！ppp 介面，vendorid=0x12d1 deviceid=0x140c | USB |
| Huawei e3131 |  |  | v6.xx and higher | ppp 介面 | USB |
| Huawei E3372h, E5576h, E8372h | 0x12d1 | 0x14db | v6.8 | 適用於 vendor-id="0x12d1" device-id="0x14db" 的調變解調器的免配置 LTE 介面。帶字尾 -320 和 -608 的型號無法在 RouterOS v6 上工作，請改用 v7。帶字尾 -325 的型號僅適用於 arm cpu | USB |
| Huawei E3276-150 |  |  | v6.xx | ppp 介面 | USB |
| Huawei E3351 |  |  | v6.24 及更高版本 |  | USB |
| Huawei E3531 |  |  | v6.24 or 6.40RC25 | 此調變解調器存在不同版本，E3531-6 從版本 6.40RC25 起可作為 ppp 工作，mbim 僅從 RouterOS V7 起受支援 | USB |
| Huawei e398 |  |  | v6.xx and higher | ppp 介面 | USB |
| Huawei E5377 |  |  | v6.36.1 | MIFI 裝置。不支援序列埠，但可在 LTE 介面上透過 IP 工作 | USB |
| Huawei E5673s-609 |  |  | v6.xx | LTE 介面 | USB |
| Huawei K5160 |  |  | v6.37  v7.0beta6 | v6 和 v7 - 免配置 LTE 介面  v7 - 預設會嘗試以 MBIM 模式使用調變解調器 | USB |
| Huawei K5161 |  |  | v6.47 | 免配置 LTE 介面 | USB |
| Huawei ME909s-120 |  |  | v6.28 | 推薦的調變解調器韌體版本為 11.617.24.00.00。要將 LTE 介面 IP 子網掩碼縮減為 /32，請使用 at-chat 命令配置調變解調器：`/interface/lte/at-chat [find]` input="AT^CUSTFEATURE=3,1" | MiniPCI-e |
| Huawei ME909u-521 |  |  | v6.11 |  | MiniPCI-e |
| Huawei MU609 |  |  | v6.11 |  | MiniPCI-e |
| Huawei MU709s-2 |  |  | v6.28 |  | MiniPCI-e |
| Huawei MS2372h-517 |  |  | v7.12beta3 | ppp/序列介面 | USB |
| Jaton MT421e |  |  | v6.40RC32 | 具有乙太網模擬的 LTE 介面（無法配置），LTE 支援頻段 42/43 | MiniPCI-e |
| Netgear Unite Explore 815S |  |  | v6.41 | MIFI 裝置。不支援序列埠，但可在 LTE 介面上透過 IP 工作。 | USB |
| Novatel USB730L |  |  | v6.41RC6 | LTE 介面 | USB |
| Olivetti Olicard 500 |  |  | v6.41RC11 | ppp 介面 | USB |
| Quectel EC20/EC21 |  |  | v6.xx | ppp 介面 | MiniPCI-e |
| Quectel BG77 | 0x2c7c | 0x0700 | v6.47 | 序列/PPP 介面，單個 AT/調變解調器通道 | OEM 模組 |
| Quectel BG95-M3 |  |  | v6.47 | 序列/PPP 介面，單個 AT/調變解調器通道  無法在 wAP R ac 板上工作。 | mini-PCIe |
| Quectel BG96 |  |  | v6.45 | 序列/PPP 介面，2 個 AT/調變解調器通道 | mini-PCIe |
| Quectel EC25-EU | 0x2c7c | 0x0125 | v6.42 | ppp/LTE 介面。  RouterOS v6  CDC-ECM 模式 - LTE 介面接收地址位於調變解調器的內部網路中。  RouterOS v7 MBIM 模式 -  LTE 介面使用 APN IP 地址。 | MiniPCI-e |
| Quectel EG25-G | 0x2c7c | 0x0125 | 6.48.3 | RouterOS v6  CDC-ECM 模式 - LTE 介面接收地址位於調變解調器的內部網路中。  RouterOS v7 MBIM 模式 -  LTE 介面使用 APN IP 地址。  在某些板上可能需要停用 SIM 熱插拔檢測：```/interface/lte/set [find] modem-init="AT+QSIMDET=0,1"``` | MiniPCI-e |
| Quectel EM12-G | 0x2c7c | 0x0512 | v7.1beta5 | MBIM 驅動程式 | m.2 |
| Quectel EP06 |  |  | v6.42 | ppp/LTE 介面 | MiniPCI-e |
| Quectel RG255C-GL |  |  | v7.18 | 透過 at-chat 提供基本支援，最低韌體版本：RG255CGLABR01A04M4G\_A0.004.A0.004  調變解調器組合：`at+qcfg="usbnet",0` | mini-PCIe |
| Quectel RM500Q-GL | 0x2c7c | 0x0800 | v7.1beta6 | MBIM 驅動程式 | m.2 |
| Quectel RM500Q-AE | 0x2c7c | 0x0800 | v7.1beta6 | MBIM 驅動程式 | m.2 |
| Quectel RM502Q-AE | 0x2c7c | 0x0800 | v7.1beta5 | MBIM 驅動程式 | m.2 |
| Quectel RM510Q-GL | 0x2c7c | 0x0800 | 7.9 | MBIM 驅動程式 | m.2 |
| Quectel UC15 |  |  | v6.xx | 可用，ppp 介面 | MiniPCI-e |
| Quectel UC20 |  |  | v6.xx | 可用，ppp 介面 | MiniPCI-e |
| R11e-4G | 0x2cd2 | 0x0003 | v6.42 | LTE 介面。支援多個 APN 透傳。 | MiniPCI-e |
| R11e-LTE6 | 0x2cd2 | 0x0004 | v6.39.2 | LTE 介面。支援多個 APN 透傳。 | MiniPCI-e |
| R11e-LTE | 0x2cd2 | 0x0001 | v6.39.2 | LTE 介面。支援多個 APN 透傳。 | MiniPCI-e |
| Sierra Netgear AirCard 320U |  |  | 6.41 | 客戶已使用韌體 03.05.23 測試該調變解調器 | USB |
| Sierra wireless MC73xx |  |  | v6.xx(ppp) v7.xx (LTE) | 可用！PPP 介面。並且從 v7.xx 開始，在調變解調器切換為暴露 MBIM 介面後，將支援 LTE 介面。MC7304 已使用韌體 SWI9X15C\_05.05.67.00 測試 | MiniPCI-e |
| Sierra Wireless MC7430 |  |  | v6.xx and higher | 資料通道 2，資訊通道 2，調變解調器初始化：AT+CGATT=0，撥號命令：AT+CGATT=1;D\*99#，還需要隔離 3.0 引腳（PINS:23,25,27,31,33） | MiniPCI-e |
| Sierra Wireless MC74xx |  |  | v7.1 | 對具有 MBIM 介面/USB 組合的調變解調器提供基本功能支援 | mini-PCIe |
| Sierra Wireless MC7455 |  |  | v7.3beta37 | 支援 USB 組合擴充套件的 MBIM 模式：1009 - diag,modem,mbim100D - diag,nmea,modem,mbim | mini-PCIe |
| Sierra Wireless MC7710/MC7700/MC7750 |  |  | v5.25, v6.0 and 6.40RC43 | 如果調變解調器使用韌體 3.5，則應升級到 3.5.23.2 韌體版本，以便再次在 RouterOS 中正常工作。 | MiniPCI-e |
| SIMcom SIM5360 |  |  | v6.xx | 可用！使用 PPP 介面，vendor-id="0x05c6" device-id="0x9000" | MiniPCI-e / USB 帶轉換器 |
| SIMcom SIM7100 | 0x1e0e | 0x9001 | v6.xx(ppp) v7.xx (LTE) | 可用！PPP 介面。並且從 v7.xx 開始將支援 LTE 介面。 | MiniPCI-e / USB 帶轉換器 |
| SIMCom SIM8202G-M.2 |  |  | v7.11 | 支援 MBIM 驅動程式：AT+CUSBCFG=usbid,1e0e,901e | m.2 |
| SXT LTE |  |  | v6 | LTE 介面。舊版 SXT LTE | 內建 |
| Tele2.ru LTE-D402 |  |  | v6.47 | 免配置 LTE 介面 |  |
| Telecom NZ T-Stick ZTE MF-181 |  |  | v6.0rc13 | 資料通道=2，資訊通道=2，APN internet.telecom.co.nz，PHONE=\*99#。已在 CCR1016-12G 上測試資料與 SMS 均正常 | USB |
| Telit FN980m |  |  | v7.5 | AT#USBCFG=2 | m.2 |
| Telit LE910 | 0x1bc7 | 0x1201 | v6.xx | ppp 介面 | MiniPCI-e |
| Telit LE910C1 |  |  | v6.46 | 無法從 RouterOS 配置 | MiniPCI-e |
| Telit LM940 |  |  | v6.44 | 在某些情況下，LTE 介面需要隔離 3.0 引腳（PINS:23,25,27,29,31,33） | MiniPCI-e |
| Telit LM960 |  |  | v6.46 | 在某些情況下，LTE 介面需要隔離 3.0 引腳（PINS:23,25,27,29,31,33） | MiniPCI-e |
| TPS (Turning Point Solution) GCT450 |  |  | v6.48 | 免配置 LTE 介面 | MiniPCI-e |
| Vodafone (Huawei) K4203 |  |  | v7.xx | 在 ROS v6 中不受支援，但由於此調變解調器支援 MBIM 驅動程式，在 ROS v7 中將可以使用。 | USB |
| Vodafone K4201-Z |  |  | v6.8 | 部分設定會被忽略。LTE 介面。 | USB |
| Vodafone K4305 |  |  | v6.7 | 部分設定會被忽略。 | USB |
| Vodafone K5160 |  |  | v6.37 | 部分設定會被忽略。 | USB |
| Yota LU150 |  |  | v5.22 and v6.4 | 部分設定會被忽略。 | USB |
| Yota wifi modem |  |  | v6.7 | 部分設定會被忽略。 | USB |
| Yota WLTUBA-107 |  |  | v6.0 | 部分設定會被忽略。 | USB |
| ZTE 821D |  |  | v6.x | 設定資訊通道 = 1，資料通道 = 3，撥號命令=ATDT | USB |
| ZTE AC5730 |  |  | v6.x |  | USB |
| ZTE ME3630-E |  |  | v6.40RC26 | ppp 和 LTE 介面 | MiniPCI-e |
| ZTE MF110 |  |  | v6.28 and higher | 設定資訊通道 = 2，資料通道 = 2，撥號命令=ATM1L3DT | USB |
| ZTE MF823 |  |  | v6.8 | 部分設定會被忽略。對於某些裝置，需要進入 FACTORY 模式以更改執行狀態。 | USB |
| ZTE MF825A |  |  | v6.xx | 部分設定會被忽略。 | USB |
| ZTE MF827 |  |  | v6.8 | 部分設定會被忽略。 | USB |
| ZTE MF832S |  |  | v7.10 | 免配置支援，可能需要使用 at-chat 或調變解調器初始化字串設定某些設定 | USB |
| ZTE MF833U1 | 0x19d2 | 0x1405 | v7.20.6 | 免配置 LTE 介面 | USB |
| ZTE MF90 |  |  | v6.44beta32 and higher | LTE 介面 | USB |

:::warning
並非所有調變解調器都列出。本地化和鎖定的裝置可能存在相容性問題。

:::

對於某些支援 USB3.0 的調變解調器，在某些情況下需要隔離 USB3.0 引腳以確保正確初始化：

![](/img/7181ffafef30e392.webp)

## SFP 模組 {#sfp-modules}

<WideTable>

| 品牌 | 型號 | 速率 | 聯結器/線纜型別 | 波長 | 測試裝置 | 可用 / 不可用 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| MikroTik | S-85DLC05D | 1,25G | 雙 LC，MM | 850nm | \*檢查：[SFP/SFP+ 相容性參考表](../wired-connections/mikrotik-wired-interface-compatibility.md) | 原生支援 |
| MikroTik | S-31DLC20D | 1,25G | 雙 LC，SM | 1310nm | \*檢查：[SFP/SFP+ 相容性參考表](../wired-connections/mikrotik-wired-interface-compatibility.md) | 原生支援 |
| MikroTik | S-35LC20D | 1,25G | BiDi LC，SM | Tx:1310nm/Rx:1550nm | \*檢查：[SFP/SFP+ 相容性參考表](../wired-connections/mikrotik-wired-interface-compatibility.md) | 原生支援 |
| MikroTik | S-53LC20D | 1,25G | BiDi LC，SM | Tx:1550nm/Rx:1310nm | \*檢查：[SFP/SFP+ 相容性參考表](../wired-connections/mikrotik-wired-interface-compatibility.md) | 原生支援 |
| MikroTik | S-RJ01 | 1000/100/10 | RJ45, Cat5/Cat6 | N/A | \*檢查：[SFP/SFP+ 相容性參考表](../wired-connections/mikrotik-wired-interface-compatibility.md) | 原生支援 |
| Axiom | AXG91632 | 1000BASE-LX | 雙 LC | 1310nm | CRS125-24G-1S-RM | 可用！ |
| Finisar | FCLF-8521-3 | 10/100/1000 | RJ45, Cat6 | N/A | RB2011LS-IN | 可用！ |
| Finisar | FCLF-8521-3-MD | 10/100/1000 | RJ45, Cat6 | N/A | RB2011LS-IN | 可用！ |
| Finisar | FTRJ8519P1BNL-B1 | 10/100/1000 1.25 Gb/s 1000Base-SX 乙太網 | 雙 LC，MM | 850nm | RB2011LS-IN | 可用！ |
| Finisar | FTLF8519P2BNL | 10/100/1000 1.25 Gb/s 1000Base-SX 乙太網 | 雙 LC，MM | 850nm | RB2011LS-IN | 可用！ |
| Finisar | FTRJ1319P1BTL | 1.25Gb/s 1000Base-LX 乙太網 | 雙 LC，SM | 1310nm | CCR1009-8G-1S-1S+ and CCR1009-7G-1C-1S+ | 可用！ |
| Unica | SFP-1.25G-T | 1000M | RJ45, Cat6 | N/A | RB2011LS-IN | 可用！ |
| Dell | FTLX8571D3BCL | 1,25G | 雙 LC，MM | 850nm | RB2011LS-IN | 可用！ |
| Unica | GP-3124-L2CD-C | 1,25G | 雙 LC，MM | 1310nm | RB2011LS-IN | 可用！ |
| Cisco | GLC-T | 1.25G | RJ45, Cat6 | N/A | RB2011LS-IN | 可用！ |
| Cisco | GLC-SX-MM | 用於 MMF 的 1000BASE-SX SFP 收發器模組，1.25G | 雙 LC，MM | 850nm | RB2011LS-IN | 可用！ |
| Cisco | SFP-GE-L | 用於 SMF 的 1000BASE-LX/LH SFP 收發器模組，1.25G | 雙 LC，SM | 1300nm | 各種 MT 硬體 | 可用！ |
| 6COM | 6C-SFP-T | 10/100/1000 | RJ45, Cat6 | N/A | RB2011LS-IN | 可用！ |
| 6COM | 6C-WDM-0210BSD | 1,25G | BiDi SC，SM | Tx:1550nm/Rx:1310nm | RB2011LS-IN | 可用！ |
| 6COM | 6C-WDM-0210ASD | 1,25G | BiDi SC，SM | Tx:1310nm/Rx:1550nm | RB2011LS-IN | 可用！ |
| 6COM | 6C-SFP-0310D | 1,25G | 雙 LC，MM | 1310nm | RB2011LS-IN | 可用！ |
| 6COM | 6C-SFP-0301D | 1,25G | 雙 LC，MM | 850nm | RB2011LS-IN | 可用！ |
| Ingellen | INSP-T(10/100/1000) | 10/100/1000 | RJ45, Cat6 | N/A | RB2011LS-IN | 可用！ |
| Ingellen | INSPL-53-BX | 1,25G | BiDi LC，MM | 1550/1310 | RB2011LS-IN | 可用！ |
| Ingellen | INSPL-35-BX | 1,25G | BiDi LC，MM | 1310/1550 | RB2011LS-IN | 可用！ |
| Ingellen | INSP-LX-SM | 1,25G | 雙 LC，SM | 1310nm | RB2011LS-IN | 可用！ |
| Ingellen | INSP-SX-MM | 1,25G | 雙 LC，MM | 850nm | RB2011LS-IN | 可用！ |
| AXCEN | AXGT-R1T4-05I1 | 10/100/1000 | RJ45, Cat6 | N/A | RB2011LS-IN | 可用！ |
| AXCEN | AXGD-37А4-0531 | 1,25G | BiDi LC，MM | Tx:1550nm/Rx:1310nm | RB2011LS-IN | 可用！ |
| AXCEN | AXGD-16А4-0531 | 1,25G | BiDi LC，MM | Tx:1310nm/Rx:1550nm | RB2011LS-IN | 可用！ |
| AXCEN | AXGD-1354-0531 | 1,25G | 雙 LC，MM | 1310nm | RB2011LS-IN | 可用！ |
| AXCEN | AXGD-5854-0511 | 1,25G | 雙 LC，MM | 850nm | RB2011LS-IN | 可用！ |
| TP-Link | TL-SM311LS | 1,25G | 雙 LC，SM | 1310nm | RB2011LS-IN | 可用！ |
| TP-Link | TL-SM311LM | 1,25G | 雙 LC，MM | 850nm | CCR1036 12G-4S | 可用！ |
| OPTIC | OPTIC-SFP-3524S-02-SC | 1,25G | BiDi SC，SM | Tx:1310nm/Rx:1550nm | RB2011UAS-RM, RB260GS | 可用！ |
| OPTIC | OPTIC-SFP-5324S-02-SC | 1,25G | BiDi SC，SM | Tx:1550nm/Rx:1310nm | RB2011UAS-RM, RB260GS | 可用！ |
| OPTIC | OPTIC-SFP-S1203-L3302-LC | 1,25G | BiDi LC，SM | Tx:1310nm/Rx:1550nm | RB2011UAS-RM, RB260GS | 可用！ |
| OPTIC | OPTIC-SFP-S1205-L3302-LC | 1,25G | BiDi LC，SM | Tx:1550nm/Rx:1310nm | RB2011UAS-RM, RB260GS | 可用！ |
| ROBOFiber | SFP-7120-55 | 1,25G | 雙 LC，SM | 1550nm | CCR1036-12G-4S, RB2011 | 可用！ |
| ROBOFiber | SFP-7120-WA | 1,25G | BiDi LC，MM | Tx:1490nm/Rx:1550nm | CCR, RB2011 | 可用！ |
| ROBOFiber | SFP-7120-WB | 1,25G | BiDi LC，MM | Tx:1550nm/Rx:1490nm | CCR, RB2011 | 可用！ |
| Enguity | SFP-3647603KM.b1310 XT | 1,25G | BiDi LC，SM | Tx:1310nm/Rx:1550nm | CCR, RB2011, RB260GS | 可用！ |
| Enguity | SFP-3647603KM.b1550 XT | 1,25G | BiDi LC，SM | Tx:1550nm/Rx:1310nm | CCR, RB2011, RB260GS | 可用！ |
| Enguity | SFP-3647610KM.b1490 XT | 1,25G | BiDi LC，SM | Tx:1490nm/Rx:1550nm | CCR, RB2011, RB260GS | 可用！ |
| Enguity | SFP-3647610KM.b1550 XT | 1,25G | BiDi LC，SM | Tx:1550nm/Rx:1490nm | CCR, RB2011, RB260GS | 可用！ |
| AdvOptics MSA | GLC-SX-MM | 1,25G | BiDi LC，MM | Tx:1310nm/Rx:1310nm | CCR, RB2011, RB260GS | 可用！ |
| AdvOptics MSA | GLC-ZX-SM | 1,25G | BiDi LC，SM | Tx:1310nm/Rx:1310nm | CCR, RB2011, RB260GS | 可用！ |
| Proline | GLC-BX-D20-PRO | 1,25G | BiDi LC，SM | Tx:1490nm/Rx:1310nm | CRS125 | 可用！ |
| Proline | GLC-BX-D40-PRO | 1,25G | BiDi LC，SM | Tx:1310nm/Rx:1490nm | CRS125 | 可用！ |
| Foundry Networks | E1MG-BXU-AC | 1,25G | BiDi LC，SM | Tx:1310nm/Rx:1490nm | RB3011UiAS, hAP ac | 可用！ |
| Avago | SFBR-5799APZ | 1,25G | 雙 LC，MM | 850nm | CRS326, CRS112 | 在 1Gbps 模式下可用！ |
| Eltex | NTU-SFP-100 | 1,25G | SC | N/A | RB4011iGS+ | 可用！ |

</WideTable>

## SFP+ 模組 {#sfp-modules-1}

<WideTable>

| 品牌 | 型號 | 距離 | 速率 | 聯結器/線纜型別 | 波長 | 測試裝置 | 可用 / 不可用 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| MikroTik | S+85DLC03D | 300m | 10G | 雙 LC，MM | 850nm | 所有帶 SFP/SFP+ 介面的 MikroTik 產品 | 原生支援 |
| MikroTik | S+31DLC10D | 10km | 10G | 雙 LC，SM | 1310nm | 所有帶 SFP/SFP+ 介面的 MikroTik 產品 | 原生支援 |
| MikroTik | S+23LC10D | 10km | 10G | BiDi LC，SM | Tx:1270nm/Rx:1330nm | 所有帶 SFP/SFP+ 介面的 MikroTik 產品 | 原生支援 |
| MikroTik | S+32LC10D | 10km | 10G | BiDi LC，SM | Tx:1330nm/Rx:1270nm | 所有帶 SFP/SFP+ 介面的 MikroTik 產品 | 原生支援 |
| MikroTik | S+DA0001 | 1m | 10G | Twinax 銅纜 | N/A | 所有帶 SFP/SFP+ 介面的 MikroTik 產品 | 原生支援 |
| MikroTik | S+DA0003 | 3m | 10G | Twinax 銅纜 | N/A | 所有帶 SFP/SFP+ 介面的 MikroTik 產品 | 原生支援 |
| MikroTik | S+RJ10 | 多種，取決於鏈路速率。更多詳情請檢視手冊 | 10G/5G/2.5G/1G/100M/10M | RJ45 - Cat5E/Cat6/Cat7 | N/A | 所有帶 SFP+ 介面的 MikroTik 產品 | 原生支援 |
| Atop | APSP55B30CDL40 | 40km | 10G | 雙 LC，SM | 1550nm | 帶 SFP+ 介面的 CRS 系列、CCR 系列裝置 | 不可用！ |
| Cisco | SFP-10G-LR | 10km | 10G | 雙 LC，SM | 1310nm | RB2011LS-IN | 可用！ |
| Dell (Finisar) | FTLX8571D3BCL | 300m | 10G | 雙 LC，MM | 850nm | 大多數 SFP/SFP+ MikroTik 產品 | 可用！ |
| Juniper (Finisar) | FTLX8571D3BCL-J1 | 300m | 10G | 雙 LC，MM | 850nm | 大多數 SFP/SFP+ MikroTik 產品 | 可用！ |
| Intel (Finisar) | FTLX8571D3BCV-IT | 300m | 10G | 雙 LC，MM | 850nm | 大多數 SFP/SFP+ MikroTik 產品 | 可用！ |
| OEM (Juniper?) | EX-SFP-10GE-SR-OEM | 300m | 10G | 雙 LC，MM | 850nm | 大多數 SFP/SFP+ MikroTik 產品 | 可用！ |
| Fiberstore | SFP-10G31-40 | 40km | 10G | 雙 LC，SM | 1310nm | 帶 SFP+ 介面的 CRS 系列、CCR 系列裝置 | 可用！ |
| Fiberstore | SFP-10G55-40 | 40km | 10G | 雙 LC，SM | 1310nm | 帶 SFP+ 介面的 CRS 系列、CCR 系列裝置 | 可用！ |
| Fiberstore | SFP-10G32-40 | 40km | 10G | BiDi LC，SM | Tx:1330nm/Rx:1270nm | 帶 SFP+ 介面的 CRS 系列、CCR 系列裝置 | 可用！ |
| Fiberstore | SFP-10G23-40 | 40km | 10G | BiDi LC，SM | Tx:1270nm/Rx:1330nm | 帶 SFP+ 介面的 CRS 系列、CCR 系列裝置 | 可用！ |
| Optech | OPAK-TX1-00-C | 30m | 10G | RJ45 - Cat 6a/7 線纜 | N/A | 帶 SFP+ 介面的 CCR、CCR、CSS 系列裝置 | 可用，從 v6.40rc20 RouterOS 構建開始。 |
| ProLabs | SFP-10G-T-C | 30m | 10G | RJ45 - Cat 6a/7 線纜 | N/A | 帶 SFP+ 介面的 CCR、CCR、CSS 系列裝置 | 可用，從 v6.40rc20 RouterOS 構建開始。 |

</WideTable>

## 用於 RDS 的 U.2 磁碟 {#u2-disks-for-rds}

RDS2216-2XG-4S+4XS-2XQ 支援任意容量的 U.2 SSD 硬碟，但物理高度限制為 7mm。雖然任何滿足此物理要求的硬碟都應受支援，但以下型號已經過驗證：

- Samsung PM9A3
- Samsung PM983
- Micron 7300 系列
- Micron 7400 系列
- WD DC SN640
- Transcend UTE210T
- Innodisk 4TG2-P
