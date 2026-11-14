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
source: https://manual.mikrotik.com/docs/7.24/getting-started/configuration-management/default-configurations
captured_at: '2026-11-04T11:28:28+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

所有 MikroTik 裝置都帶有某種預設配置。根據板卡型別的不同，有多種不同的配置：

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

在此類配置中，路由器被配置為無線用戶端裝置。WAN 介面是 **Wireless** 介面。WAN 埠已配置 DHCP 用戶端，受 IP 防火牆保護，並且 MAC 發現/連線已停用。

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

:::info
CPE 路由器模式：

- \* 無線介面連線到提供商的網路（WAN 埠）；
- \* WAN 埠受防火牆保護，並啟用 DHCP 用戶端

wlan1 配置：

- mode: station;
- band: 2ghz-b/g/n;
- tx-chains: 0;1;
- rx-chains: 0;1;
- installation: outdoor;
- wpa2: no;
- ht-extension: 20/40mhz-XX;

LAN 配置：

- 在 ether1（LAN 埠）上設定 IP 地址 192.168.88.1/24
- DHCP Server: enabled;
- DNS: enabled;

WAN（閘道器）配置：

- gateway:wlan1 ;
- ip4 firewall: enabled;
- ip6 firewall: enabled;
- NAT: enabled;
- DHCP Client: enabled;

## 登入 {#login}

- admin 使用者受密碼保護

配置**預覽**：  
[CPE_Router.txt](pathname:///assets/167706794_CPE_Router.txt)。
:::

## LTE CPE AP 路由器 {#lte-cpe-ap-router}

此配置型別適用於同時具有 LTE 和無線介面的路由器。LTE 介面被視為受防火牆保護的 WAN 埠，並且 MAC 發現/連線已停用。WAN 埠上的 IP 地址會自動獲取。無線介面被配置為接入點，並與所有可用的乙太網埠橋接。

使用此型別配置的路由器列表：

- wAP LTE Kit
- SXT LTE
- LtAP 4G kit
- LtAP LTE kit
- Chateau

:::info

### CPE RouterMode {#cpe-routermode}

\* 無線介面連線到提供商的網路（WAN）

這裡指的是 LTE 介面，而不是無線介面。

\* WAN 埠受防火牆保護，並啟用了 DHCP 用戶端)

### LAN 配置： {#lan-configuration}

- 在網橋（LAN 埠）上設定 IP 地址 192.168.188.1/24
- DHCP Server: enabled;
- DNS: enabled;

### WAN（閘道器）配置： {#wan-gateway-configuration}

- gateway:lte1 ;
- ip4 firewall: enabled;
- ip6 firewall: enabled;
- NAT: enabled;

### 登入 {#login-1}

- admin 使用者受密碼保護

配置**預覽**：  
[LTE_CPE_AP_router.txt](pathname:///assets/167706791_LTE_CPE_AP_router.txt)。
:::

## AP 路由器 {#ap-router}

此配置型別適用於開箱即用、無需額外配置（路由器密碼和無線金鑰除外）的家庭接入點路由器。

第一個乙太網埠始終配置為 WAN 埠（受防火牆保護、啟用 DHCP 用戶端，並停用 MAC 連線/發現）。其他乙太網埠和無線介面會加入本地 LAN 網橋，並設定 192.168.88.1/24 地址和配置 DHCP 伺服器。對於雙頻路由器，一個無線介面配置為 5 GHz 接入點，另一個配置為 2.4 GHz 接入點。

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

:::info

### RouterMode {#routermode}

\* WAN 埠受防火牆保護，並啟用了 DHCP 用戶端

\* 無線和乙太網介面（WAN 埠除外）屬於 LAN 網橋

### LAN 配置： {#lan-configuration-1}

- 在網橋（LAN 埠）上設定 IP 地址 192.168.88.1/24
- DHCP Server: enabled;
- DNS: enabled;

### wlan1 配置： {#wlan1-configuration}

- mode: ap-bridge;
- band: 2ghz-b/g/n;
- tx-chains: 0;1;
- rx-chains: 0;1;
- installation: indoor;
- wpa2: no;
- ht-extension: 20/40mhz-XX;

### WAN（閘道器）配置： {#wan-gateway-configuration-1}

- ip4 firewall: enabled;
- ip6 firewall: enabled;
- NAT: enabled;
- DHCP Client: enabled;

### 登入 {#login-2}

- admin 使用者受密碼保護

### 配置**預覽** {#configuration-preview}

[RouterMode.txt](pathname:///assets/167706790_RouterMode.txt)
:::

## PTP 網橋、W60G 網橋 {#ptp-bridge-w60g-bridge}

將乙太網與無線介面橋接。在網橋介面上設定預設 IP 地址 192.168.88.1/24。有兩種可能的選項 - CPE 和 AP。對於 CPE，無線介面設定為 "station-bridge" 模式；對於 AP，使用 "bridge" 模式。W60G 網橋 - 此配置型別適用於具有 60 GHz 點對點鏈路的路由器。

:::info
PTP 網橋：

\* 無線和 LAN 介面已橋接；

### LAN 配置： {#lan-configuration-2}

#### 登入 {#login-3}

- admin 使用者受密碼保護

配置**預覽**：  
[PTP_Bridge.txt](pathname:///assets/167706792_PTP_Bridge.txt)

:::

使用此型別配置的路由器列表：

- DynaDish - 作為 CPE

:::info
W60G 網橋：

 \* W60G 和 LAN 介面已橋接；

### wlan60-1 配置： {#wlan60-1-configuration}

- SSID: MikroTik;
- mode:station-bridge;
- password: no;
- 在網橋上設定 IP 地址 192.168.88.1/24

#### 登入 {#login-4}

- admin 使用者受密碼保護

配置**預覽**：  
[W60G_Bridge.txt](pathname:///assets/167706793_W60G_Bridge.txt)

:::

## 使用此型別配置的路由器列表 {#list-of-routers-using-this-type-of-configuration}

- Cube, Cube Pro
- nRAY, Dish
- Wireless Wire kit
- wAP 60G - 具有 level3 許可證

## WISP 網橋 {#wisp-bridge}

該配置與 AP 模式下的 PTP 網橋相同，不同之處在於針對 PTMP 部署將無線模式設定為 ap\_bridge。可以使用 MAC 地址直接訪問路由器。如果裝置連線到啟用了 DHCP 伺服器的網路，則在網橋介面上配置的 DHCP 用戶端將獲取 IP 地址，該地址可用於訪問路由器。

使用此型別配置的路由器列表：

- RB 911,912,921,922 - 具有 Level4 許可證。
- Groove A, RB 711 A
- BaseBox, NetBox
- mANTBox, NetMetal
- wAP 60G AP - 具有 level4 許可證。
- LtAP
- CME

:::info
WISP 網橋：

 \* 無線和 LAN 介面已橋接；

### wlan1 配置： {#wlan1-configuration-1}

- mode: ap-bridge;
- band: 2ghz-b/g/n;
- tx-chains: 0;1;
- rx-chains: 0;1;
- installation:   outdoor;
- wpa2: no;
- ht-extension:   20/40mhz-XX;

### wlan2 配置： {#wlan2-configuration}

- mode: ap-bridge;
- band: 5ghz-a/n/ac;
- tx-chains: 0;1;
- rx-chains: 0;1;
- installation:   outdoor;
- wpa2: no;
- ht-extension:   20/40/80mhz-XXXX;

### LAN 配置： {#lan-configuration-3}

- DHCP 用戶端：在網橋（LAN 口）上啟用；

### 登入 {#login-5}

- admin 使用者受密碼保護

配置**預覽**：  
[WISP_Bridge.txt](pathname:///assets/167706789_WISP_Bridge.txt)
:::

## 交換器 {#switch}

此配置利用交換晶片功能來配置基礎交換器。所有乙太網埠都會加入交換器組，並且在網橋介面上設定預設 IP 地址 192.168.88.1/24。

使用此型別配置的路由器列表：

- FiberBox
- 不帶無線介面的 CRS

:::info
交換器模式：

- 所有介面均已啟用交換；

### 登入 {#login-6}

- admin 使用者受密碼保護

配置**預覽**：  
[switch.txt](pathname:///assets/234914118_switch.txt)

:::

## 僅 IP {#ip-only}

當未找到特定配置時，會在 ether1、combo1 或 sfp1 上設定 IP 地址 192.168.88.1/24。

使用此型別配置的路由器列表：

- RB 411,433,435,493,800,M11,M33,1100
- CCR, ROSE Data server

:::info

### LAN {#lan}

- IP on etherx: 192.168.88.1/24;

### 登入 {#login-7}

- admin 沒有密碼。

### 配置預覽 {#configuration-preview-1}

[ccr.txt](pathname:///assets/234914117_ccr.txt)
:::

## CAP {#cap}

當裝置需要作為由 [CAPsMAN](../../wireless/abgn/capsman/index.md) 控制的無線用戶端裝置使用時，會使用此配置型別。

載入 CAP 預設配置時，ether1 被視為管理埠，並配置了 DHCP 用戶端。所有其他乙太網介面都會橋接，wlan1 設定為由 CAPsMAN 管理。

要載入 CAP 配置，請參閱  [復位按鈕手冊](./routeros-configuration-reset.md)。
