---
sidebar_key: "getting-started/software-specifications/index"
sidebar_position: 2
title: "軟體規格"
sidebar_label: "軟體規格"
description: "本頁概述 RouterOS 軟體規格，涵蓋 MikroTik 裝置的硬體相容性、安裝方法、配置工具、備份/恢復能力、防火牆功能、路由協定以及 MPLS 支援。"
tags:
  - 'firewall'
  - 'vpn'
source: https://manual.mikrotik.com/docs/7.25/getting-started/software-specifications
captured_at: '2026-11-04T11:17:03+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 硬體支援 {#hardware-support}

**MikroTik 製造的裝置：** RouterOS 與預裝它的 MikroTik 硬體相容。即使是較舊的、已停產的 MikroTik 裝置也可以執行最新的 RouterOS，但效能可能有所不同。對於最古老的產品線，有一些例外。RouterOS v7 並非與所有 MIPS-LE 系列裝置相容（例如 RB100 系列、部分 RB700 系列裝置；請檢查相關裝置的架構）。軟體相容性或升級沒有固定限制。即使裝置已停產 20 年，只要具有足夠的 RAM 且不是基於 MIPS-LE CPU，仍可能收到軟體更新。

**第三方裝置：** RouterOS 也可以在滿足以下要求的第三方裝置上執行：

- x86 或基於 AMPERE 的 ARM CPU。
- 至少 64 MB RAM。
- IDE、SATA、USB 和快閃記憶體儲存介質，至少 64 MB 空間。
- Linux 核心支援的網路卡。

:::info
NVMe 儲存僅支援 CHR、x86、Tile 和 MMIPS 架構。請檢視各產品手冊或框圖以獲取具體資訊。
:::

:::info
採用預設配置的 RouterOS 7 至少需要 32 MB RAM，但對於更高階的配置，我們建議至少 64 MB。
:::

## 安裝 {#installation}

- [網路安裝](../installation-and-upgrade/netinstall/index.md)：透過支援 PXE 或 EtherBoot 的網路卡進行完整的基於網路的安裝。
- [CHR：安裝](../installation-and-upgrade/install/chr-installation/index.md)：旨在作為虛擬機器執行的 RouterOS 版本。
- 基於 CD 的安裝。

## 配置 {#configuration}

- 用於初始配置的基於 MAC 的訪問。
- [WinBox](../../management-tools/winbox.md) – 獨立的 Windows GUI 配置工具。
- [WebFig](../../management-tools/webfig.md) - 高階的基於 Web 的配置介面。
- MikroTik - [基於 Android 和 iOS 的配置工具](../../management-tools/mikrotik-mobile-app.md)。
- 強大的命令列配置介面，整合指令碼功能，可透過本地終端、序列控制檯、telnet 和 ssh 訪問。
- API - 建立自己的配置和監控應用程式的方式。

## 備份/恢復 {#backuprestore}

- 二進位制配置 [backup](../configuration-management/backup.md) 的儲存和載入。
- 以人類可讀的文字格式進行[配置匯出和匯入](../configuration-management/index.md#configuration-export-and-import)。

## 防火牆 {#firewall}

- 有狀態過濾。
- 源 NAT 和目標 NAT。
- NAT 助手（h323、pptp、quake3、sip、ftp、irc、tftp）。
- 內部連線標記、路由標記和封包標記。
- 按 IP 地址和地址範圍、埠和埠範圍、IP 協定、DSCP 等進行過濾。
- 地址列表。
- 自定義 Layer7 匹配器。
- 支援 IPv6。
- PCC - 每連線分類器，用於負載均衡配置。
- 用於繞過連線跟蹤的 RAW 過濾。

## 路由 {#routing}

- 靜態路由。
- 虛擬路由和轉發（VRF）。
- 基於策略的路由。
- 介面路由。
- ECMP 路由。
- IPv4 動態路由協定：RIP v1/v2、OSPFv2、BGP v4。
- IPv6 動態路由協定：RIPng、OSPFv3、BGP。
- 雙向轉發檢測（BFD）。

## MPLS {#mpls}

- 用於 IPv4 的靜態標籤繫結。
- 用於 IPv4 的標籤分發協定。
- RSVP 流量工程隧道。
- 基於 VPLS MP-BGP 的自動發現和信令。
- 基於 MP-BGP 的 MPLS IP VPN。

## VPN {#vpn}

- [IPSec](../../virtual-private-networks/ipsec/index.md) – 隧道和傳輸模式、證書或 PSK、AH 和 ESP 安全協定。
- 支援 IKEv2。
- IPSec 的 AES-NI 硬體加速支援。
- 點對點隧道（[OpenVPN](../../virtual-private-networks/openvpn.md)、[PPTP](../../virtual-private-networks/pptp.md)、[PPPoE](../../virtual-private-networks/pppoe/index.md)、[L2TP](../../virtual-private-networks/l2tp/index.md)、[SSTP](../../virtual-private-networks/sstp.md)）。
- 高階 PPP 功能（MLPPP、BCP）。
- BCP 在 sstp、ppp、pptp、l2tp 和 pppoe 上受支援。
- 簡單隧道（[IPIP](../../virtual-private-networks/ipip.md)、[EoIP](../../virtual-private-networks/eoip.md)）支援 IPv4 和 IPv6。
- [6to4](../../virtual-private-networks/6to4.md) 隧道支援（IPv4 網路上的 IPv6）。
- VLAN – IEEE802.1q 虛擬 LAN 支援、Q-in-Q 支援。
- 基於 MPLS 的 VPN。
- [WireGuard](../../virtual-private-networks/wireguard.md)。
- [ZeroTier](../../virtual-private-networks/zerotier.md)。

## 無線 {#wireless}

- IEEE802.11a/b/g 無線用戶端和接入點。
- 全面支援 IEEE802.11n。
- Nstreme 和 Nstreme2 專有協定。
- NV2 協定。
- 無線分散式系統（WDS）。
- 虛擬 AP。
- WEP、WPA、WPA2。
- 訪問控制列表。
- 無線用戶端漫遊。
- WMM。
- HWMP+ 無線 MESH 協定。
- MME 無線路由協定。

## DHCP {#dhcp}

- 每個介面的 DHCP 伺服器。
- DHCP 用戶端和中繼。
- 靜態和動態 DHCP 租約。
- 支援 RADIUS。
- 自定義 DHCP 選項。
- DHCPv6 字首委派（DHCPv6-PD）。
- DHCPv6 用戶端。

## 熱點 {#hotspot}

- 對網路的 Plug-n-Play 訪問。
- 本地網路用戶端的認證。
- 使用者計費。
- 用於認證和計費的 RADIUS 支援。

## QoS {#qos}

- 具有 CIR、MIR、突發和優先順序支援的層級令牌桶（HTB）QoS 系統。
- 用於基本 QoS 實現的簡單快速解決方案 - Simple queues。
- 動態用戶端速率均衡（PCQ）。

## 代理 {#proxy}

- HTTP 快取代理伺服器。
- 透明 HTTP 代理。
- 支援 SOCKS 協定。
- DNS 靜態條目。
- 支援在獨立驅動器上進行快取。
- 支援父代理。
- 訪問控制列表。
- 快取列表。

## 工具 {#tools}

- Ping、traceroute
- 頻寬測試、ping flood
- 封包嗅探器、torch
- Telnet、ssh
- 電子郵件和 SMS 傳送工具
- 自動化指令碼執行工具
- CALEA
- 檔案獲取工具
- 高階流量生成器
- WoL（區域網路喚醒）傳送

## 其他功能 {#other-features}

- 支援 Samba。
- 支援 OpenFlow。
- 橋接 – 生成樹協定（STP、RSTP）、橋接防火牆和 MAC natting。
- 動態 DNS 更新工具。
- NTP 用戶端/伺服器以及與 GPS 系統同步。
- 支援 VRRP v2 和 v3。
- SNMP。
- M3P - 用於無線鏈路和乙太網的 MikroTik Packet Packer Protocol。
- MNDP - MikroTik Neighbor Discovery Protocol，支援 CDP（Cisco Discovery Protocol）。
- RADIUS 認證和計費。
- TFTP 伺服器。
- 同步介面支援（僅 Farsync 卡）（在 v5.x 中已移除）。
- 非同步 – 序列 PPP 撥入/撥出，按需撥號。
- ISDN – 撥入/撥出，128K 捆綁支援，Cisco HDLC、x75i、x75ui、x75bui 線路協定，按需撥號。

## 核心版本 {#kernel-version}

- RouterOS 版本 6.x 使用 3.3.5
- RouterOS 版本 7.x 使用 5.6.3

## 支援的加密 {#supported-encryptions}

RouterOS 7 用於網路（電信）裝置的管理。

- RouterOS 7 包含加密功能（元件），旨在保障透過電信通道和裝置控制通道傳輸的資料（資訊）安全。
- 所有加密功能（元件）都是 RouterOS 7 的組成部分，終端使用者無法更改。
- RouterOS 7 旨在由終端使用者安裝，無需供應商提供大量支援。
- RouterOS 7 使用以下安全協定。

| 支援的安全協定 | 加密演算法 | 最大金鑰長度 |
| :-- | :-- | :-- |
| <br/> IPSec | DES | 56 bit |
|  | 3DES | 168 bit |
|  | AES | 128、192、256 位 |
|  | Blowfish | 448 bit |
|  | Twofish | 256 bit |
|  | Camellia | 128, 192, 256 bit |
| PPTP（使用 MPPE） | RC4 | 128 bit |
| L2TP（使用 MPPE） | RC4 | 128 bit |
| SNMP | DES | 56 bit |
|  | AES | 128 bit |
| SSH | Blowfish | 128 bit |
|  | 3DES | 168 bit |
|  | AES | 128、192、256 位 |
| SSTP | AES | 256 bit |
|  | RC4 | 128 位 |
| 用於 WinBox 連線（無名稱） | AES | 128 bit |
| WEP | RC4 | 104 bit |
| WPA-TKIP | RC4 | 128 bit |
| WPA2-TKIP | RC4 | 128 bit |
| WPA-AES | AES | 128 bit |
| WPA2-AES | AES | 128、256 位 |
| WPA3 | AES | 128、256 位 |
| HTTPS | NULL、RC4、DES、DES40、3DES、AES | 128、192、256 位 |

## 相關主題 {#related-topics}

<DocCardList />
