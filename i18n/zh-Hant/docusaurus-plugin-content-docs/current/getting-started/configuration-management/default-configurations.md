---
sidebar_key: "getting-started/configuration-management/default-configurations"
sidebar_position: 3
title: "預設配置"
sidebar_label: "預設配置"
description: "本頁介紹各種 MikroTik RouterOS 裝置的預設配置，包括 CPE 路由器、LTE CPE AP 路由器以及其他介面型別。它概述了每種配置型別的具體設定，例如 WAN/LAN 介面、防火牆規則和 DHCP 配置。"
tags:
  - 'cpe-router'
  - 'ap-router'
  - 'ltcpe'
source: https://manual.mikrotik.com/docs/getting-started/configuration-management/default-configurations
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

所有 MikroTik 裝置都帶有某種預設配置。根據板卡型別，有多種不同的配置：

- CPE 路由器
- LTE CPE AP 路由器
- AP 路由器（單頻或雙頻）
- PTP 網橋、W60G 網橋（AP 或 CPE）
- WISP 網橋（ap\_bridge 模式下的 AP）
- 交換器
- 僅 IP
- CAP

可以執行命令 `/system/default-configuration/print` 檢視實際應用的預設配置命令。

## CPE 路由器 {#cpe-router}
---

在此配置型別中，路由器被設定為無線用戶端裝置。WAN 介面是一個 **無線**介面。WAN 埠已配置 DHCP 用戶端，受 IP 防火牆保護，並且 MAC 發現和連線已停用。

使用此型別配置的路由器列表：

- RB 711,911,912,921,922 - 具有 level3 許可證
- SXT
- QRT
- SEXTANT
- LHG
- LDF
- DISC
- Groove
- Metal

**CPE 路由器模式**

- 無線介面連線到提供商的網路（WAN 埠）；
- WAN 埠受防火牆保護，並已啟用 DHCP 用戶端

**wlan1 配置**

|  |  |
| :-- | :-- |
| *mode* | station |
| *band* | 2ghz-b/g/n |
| *tx-chains* | 0;1 |
| *rx-chains* | 0;1 |
| *installation* | outdoor |
| *wpa2* | no |
| *ht-extension* | 20/40mhz-XX |

**LAN 配置：**

|  |  |
| :-- | :-- |
| *IP address* | 192.168.88.1/24 設定在 ether1（LAN 埠）上 |
| *DHCP Server* | enabled |
| *DNS* | enabled |

**WAN（閘道器）配置**

|  |  |
| :-- | :-- |
| *gateway* | wlan1 |
| *ip4 firewall* | enabled |
| *ip6 firewall* | enabled |
| *NAT* | enabled |
| *DHCP Client* | enabled |

**登入**

- admin 使用者受密碼保護

**配置預覽**：  
[CPE_Router.txt](pathname:///assets/167706794_CPE_Router.txt).

## LTE CPE AP 路由器 {#lte-cpe-ap-router}
---

此配置型別應用於同時具有 LTE 和無線介面的路由器。LTE 介面是 WAN 埠，受防火牆保護，並且 MAC 發現和連線已停用。WAN 埠上的 IP 地址會自動獲取。無線介面配置為接入點，並與所有可用的乙太網埠橋接。

使用此型別配置的路由器列表：

- wAP LTE Kit
- SXT LTE
- LtAP 4G kit
- LtAP LTE kit
- Chateau

**LTE CPE AP 路由器模式**

- 無線介面連線到提供商的網路（WAN）

這裡指的是 LTE 介面，而不是無線介面。

- WAN 埠受防火牆保護，並已啟用 DHCP 用戶端

**LAN 配置**

|  |  |
| :-- | :-- |
| *IP address* | 192.168.188.1/24 設定在 bridge（LAN 埠）上 |
| *DHCP Server* | enabled |
| *DNS* | enabled |

**WAN（閘道器）配置**

|  |  |
| :-- | :-- |
| *gateway* | lte1 |
| *ip4 firewall* | enabled |
| *ip6 firewall* | enabled |
| *NAT* | enabled |

**登入**

- admin 使用者受密碼保護

**配置預覽**：  
[LTE_CPE_AP_router.txt](pathname:///assets/167706791_LTE_CPE_AP_router.txt).

## AP 路由器 {#ap-router}
---

此配置型別應用於家庭接入點路由器，無需額外配置即可使用（路由器密碼和無線金鑰除外）。

第一個乙太網介面配置為 WAN 埠（受防火牆保護、已啟用 DHCP 用戶端，並且 MAC 連線和發現已停用）。其他乙太網埠和無線介面會加入 LAN bridge，並設定 IP 地址 192.168.88.1/24，同時配置 DHCP 伺服器。對於雙頻路由器，一個無線介面配置為 5 GHz 接入點，另一個配置為 2.4 GHz 接入點。

使用此型別配置的路由器列表：

- RB 450,751,850,951,953,2011,3011,4011
- hEX, PowerBox
- mAP
- wAP, wAP R（不帶 LTE 卡）
- hAP
- cAP
- OmniTIK
- 帶無線介面的 CRS 系列
- L009 系列
- Audience
- Knot
- PWR

**AP 路由器模式**

- WAN 埠受防火牆保護，並已啟用 DHCP 用戶端
- 無線和乙太網介面（WAN 埠除外）是 LAN bridge 的一部分

**LAN 配置：**

|  |  |
| :-- | :-- |
| *IP address* | 192.168.88.1/24 設定在 bridge（LAN 埠）上 |
| *DHCP Server* | enabled |
| *DNS* | enabled |

**wlan1 配置**

|  |  |
| :-- | :-- |
| *mode* | ap-bridge |
| *band* | 2ghz-b/g/n |
| *tx-chains* | 0;1 |
| *rx-chains* | 0;1 |
| *installation* | indoor |
| *wpa2* | no |
| *ht-extension* | 20/40mhz-XX |

**WAN（閘道器）配置**

|  |  |
| :-- | :-- |
| *ip4 firewall* | enabled |
| *ip6 firewall* | enabled |
| *NAT* | enabled |
| *DHCP Client* | enabled |

**登入**

- admin 使用者受密碼保護

**配置預覽**：  
[RouterMode.txt](pathname:///assets/167706790_RouterMode.txt)

## PTP 網橋 {#ptp-bridge}
---

乙太網與無線介面橋接。IP 地址 192.168.88.1/24 設定在 bridge 介面上。有兩種選項——CPE 和 AP。對於 CPE，無線介面使用 "station-bridge" 模式；對於 AP，則使用 "bridge" 模式。

使用此型別配置的路由器列表：

- DynaDish - 作為 CPE

**PTP 網橋模式**

- 無線和 LAN 介面已橋接；

**LAN 配置：**

**登入**

- admin 使用者受密碼保護

**配置預覽**：  
[PTP_Bridge.txt](pathname:///assets/167706792_PTP_Bridge.txt)

## W60G 網橋 {#w60g-bridge}
---

此配置型別應用於具有 60 GHz 點對點鏈路的路由器。

使用此型別配置的路由器列表：

- Cube, Cube Pro
- nRAY, Dish
- Wireless Wire kit
- wAP 60G - 具有 level3 許可證

**W60G 網橋模式**

- W60G 和 LAN 介面已橋接；

**wlan60-1 配置**

|  |  |
| :-- | :-- |
| *SSID* | MikroTik |
| *mode* | station-bridge |
| *password* | no |
| *IP address* | 192.168.88.1/24 設定在 bridge 上 |

**登入**

- admin 使用者受密碼保護

**配置預覽**：  
[W60G_Bridge.txt](pathname:///assets/167706793_W60G_Bridge.txt)

## WISP 網橋 {#wisp-bridge}
---

該配置與 AP 模式下的 PTP Bridge 相同，不同之處在於，對於 PTMP 設定，無線模式設定為 ap\_bridge。你可以使用 MAC 地址直接訪問路由器。如果裝置連線到啟用了 DHCP 伺服器的網路，則 bridge 介面上配置的 DHCP 用戶端會獲取一個 IP 地址，你可以使用該地址訪問路由器。

使用此型別配置的路由器列表：

- RB 911,912,921,922 - 具有 Level4 許可證。
- Groove A, RB 711 A
- BaseBox, NetBox
- mANTBox, NetMetal
- wAP 60G AP - 具有 level4 許可證。
- LtAP
- CME

**WISP 網橋模式**

- 無線和 LAN 介面已橋接；

**wlan1 配置**

|  |  |
| :-- | :-- |
| *mode* | ap-bridge |
| *band* | 2ghz-b/g/n |
| *tx-chains* | 0;1 |
| *rx-chains* | 0;1 |
| *installation* | outdoor |
| *wpa2* | no |
| *ht-extension* | 20/40mhz-XX |

**wlan2 配置**

|  |  |
| :-- | :-- |
| *mode* | ap-bridge |
| *band* | 5ghz-a/n/ac |
| *tx-chains* | 0;1 |
| *rx-chains* | 0;1 |
| *installation* | outdoor |
| *wpa2* | no |
| *ht-extension* | 20/40/80mhz-XXXX |

**LAN 配置：**

|  |  |
| :-- | :-- |
| *DHCP Client* | 在 bridge（LAN 埠）上為 enabled |

**登入**

- admin 使用者受密碼保護

**配置預覽**：  
[WISP_Bridge.txt](pathname:///assets/167706789_WISP_Bridge.txt)

## Switch {#switch}
---

此配置使用交換晶片功能來配置基本交換器。所有乙太網埠都會加入交換器組，並且 IP 地址 192.168.88.1/24 設定在 bridge 介面上。

使用此型別配置的路由器列表：

- FiberBox
- 不帶無線介面的 CRS

**Switch 模式**

- 所有介面均處於交換狀態；

**登入**

- admin 使用者受密碼保護

**配置預覽**：  
[switch.txt](pathname:///assets/234914118_switch.txt)

## 僅 IP {#ip-only}
---

當未找到特定配置時，會在 ether1、combo1 或 sfp1 上設定 IP 地址 192.168.88.1/24。

使用此型別配置的路由器列表：

- RB 411,433,435,493,800,M11,M33,1100
- CCR, ROSE Data server

**LAN**

|  |  |
| :-- | :-- |
| *etherx 上的 IP* | 192.168.88.1/24 |

**登入**

- admin 使用者沒有密碼。

**配置預覽**：  
[ccr.txt](pathname:///assets/234914117_ccr.txt)

## CAP {#cap}
---

當裝置需要作為由 [CAPsMAN](../../wireless/abgn/capsman/index.md) 控制的無線用戶端裝置執行時，使用此配置型別。

載入 CAP 預設配置後，ether1 是管理埠，並已配置 DHCP 用戶端。所有其他乙太網介面都會橋接，wlan1 由 CAPsMAN 管理。

要載入 CAP 配置，請參閱 [Reset Button 手冊](./routeros-configuration-reset.md)。
