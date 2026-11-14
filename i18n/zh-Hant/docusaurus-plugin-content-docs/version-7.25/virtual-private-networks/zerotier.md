---
sidebar_key: "virtual-private-networks/zerotier"
sidebar_position: 12
title: "ZeroTier"
sidebar_label: "ZeroTier"
description: "ZeroTier 是適用於 MikroTik RouterOS 的網路虛擬化引擎，它透過乙太網虛擬化和加密的點對點網路實現安全的跨網路裝置連線。它支援遊戲、LAN 訪問、NAT 穿透和遠端 Pi-Hole 管理，同時需要正確配置 UDP 埠、選擇 NAT 型別並儘量減少 NAT 層數以獲得可靠的連線。"
tags:
  - 'zerotier'
  - 'ipv6'
source: https://manual.mikrotik.com/docs/7.25/virtual-private-networks/zerotier
captured_at: '2026-11-04T11:23:40+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

[ZeroTier](https://docs.zerotier.com/) 網路虛擬機器監控器是一個自包含的網路虛擬化引擎，它實現了類似於 VXLAN 的乙太網虛擬化層，構建在加密安全的全球點對點網路之上。它提供與企業級 SDN 交換器相當的高階網路虛擬化和管理能力，但可跨區域網路和廣域網路，並連線幾乎任何型別的應用或裝置。

MikroTik 已將 ZeroTier 新增到 RouterOS v7.1rc2，作為面向 **ARM/ARM64** 架構的獨立軟體包。

### 使用場景 {#use-cases}

- 在家中託管遊戲伺服器（適合僅限 LAN 的遊戲），或與朋友舉辦 LAN 聚會。
- 直接訪問 NAT 後面的 LAN 裝置。
- 無需向網際網路開放埠，即可透過 SSH 訪問 LAN 裝置。
- 透過網際網路從任何地方使用你本地的 Pi-Hole 設定。

:::info
ZeroTier 功能可能會被 `device-mode` 阻止。配置 ZeroTier 之前，請確保已在 `system/device-mode` 中啟用該功能。（[更多資訊](../system-information-and-utilities/device-mode.md)）
:::

### 影片教程 {#video-tutorial}

- [ZeroTier](https://youtu.be/60uIlyF8Z5s)

## 所需網路配置 {#required-network-configuration}

### ZeroTier 使用哪些埠？ {#what-ports-does-zerotier-use}

它監聽 3 個 UDP 埠：

- 9993 - 預設
- 一個由你的 ZeroTier 地址派生出的隨機高位埠
- 一個用於 UPnP/NAT-PMP 對映的隨機高位埠

這意味著你的 *對等節點* 可能監聽任意埠。要直接與它們通訊，你需要能夠向它們的任意埠傳送資料。

### 推薦的本地網路和網際網路閘道器配置 {#recommended-local-network-and-internet-gateway-configuration}

這些 ZeroTier 推薦準則與絕大多數使用通用閘道器和接入點的典型部署一致：

- 不要限制出站 UDP 流量。
- 在網路中支援 UPnP 或 NAT-PMP 可以顯著提升效能，因為它允許 ZeroTier 端點對映外部埠並完全避免 NAT 穿透。
- 建議使用 IPv6；如果直連鏈路兩端都支援 IPv6，它可以顯著提高直接連線的可靠性。若存在 IPv6，請在不使用 NAT 的情況下實施（IPv6 無需 NAT，且 NAT 會增加複雜性），並使用允許雙向 UDP 會話的狀態化防火牆。
- 不要使用“對稱”NAT。請使用“完全錐形”或“埠受限錐形”NAT。對稱 NAT 對點對點流量極其不友好，並且會降低 VoIP、影片聊天、遊戲、WebRTC 以及 ZeroTier 等許多其他協定的表現。
- ZeroTier 端點與網際網路之間不應存在超過一層 NAT。多層 NAT 會因不同層級的狀態和行為之間混亂的互動而引入連線不穩定性。不要使用雙重 NAT。
- NAT 裝置的埠對映或連線超時時間不應短於 60 秒。
- 每個由 NAT 管理的外部 IP 地址後放置的裝置不應超過 16,000 臺，以確保每臺裝置都能對映足夠數量的埠。
- 交換器和無線接入點應允許本地裝置之間的直接本地流量。關閉任何“本地隔離”功能。如果交換器允許更細粒度的控制，請允許進出埠 9993 的本地 UDP 流量。

## 配置示例 {#configuration-example}

![](/img/973091414929cb14.webp)

ZeroTier 被設計為零配置——你無需編寫配置檔案或提供其他節點的 IP 地址即可啟動新節點。世界上任意兩臺裝置都能幾乎即時地相互定位並通訊。以下示例在 RouterOS 裝置上啟用 ZeroTier，並使用 ZeroTier 應用程式連線一部手機。

1. 在 [my.zerotier.com](https://my.zerotier.com/) 上註冊並**建立網路**，獲取*網路 ID*，本示例中為：*1d71939404912b40*。  
   ![](/img/8a1dad2da1ff845b.webp)
2. [下載](https://mikrotik.com/download)並安裝 ZeroTier NPK 包。你可以在“Extra packages”下找到它。將包上傳到裝置並重啟。
3. 啟用預設（官方）ZeroTier 例項：

   ```ros
   [admin@MikroTik] > /zerotier/enable zt1
   ```

4. 新增一個新網路，指定你在 ZeroTier 雲控制檯中建立的網路 ID：

   ```ros
   [admin@mikrotik] /zerotier/interface/add network=1d71939404912b40 instance=zt1
   ```

5. 驗證 ZeroTier 配置：

   ```ros
   [admin@MikroTik] > /zerotier/interface/print
   Flags: R - RUNNING
   Columns: NAME, MAC-ADDRESS, NETWORK, NETWORK-NAME, STATUS
   #   NAME       MAC-ADDRESS        NETWORK           NETWORK-NAME     STATUS
   0 R zerotier1  42:AC:0D:0F:C6:F6  1d71939404912b40  modest_metcalfe  OK   
   ```

6. 你可能需要允許從 ZeroTier 介面到路由器的連線，以及可選的到其他 LAN 介面的連線：

   ```ros
   /ip/firewall/filter/add action=accept chain=forward in-interface=zerotier1 place-before=0
   /ip/firewall/filter/add action=accept chain=input in-interface=zerotier1 place-before=0
   ```

7. 在你的智慧手機或計算機上安裝 ZeroTier 用戶端。按照 ZeroTier 手冊連線到同一網路。
8. 如果 **"Access Control"** 設定為 **"Private"**，則必須先授權節點，節點才能成為成員：  
   ![](/img/b58464df52d7e227.webp)

9. ```ros
   [admin@MikroTik] > `/ip/address/print` where interface~"zero"
   Flags: D - DYNAMIC
   Columns: ADDRESS, NETWORK, INTERFACE
   #   ADDRESS             NETWORK        INTERFACE
   3 D 192.168.192.105/24  192.168.192.0  zerotier1

   [admin@MikroTik] > ping 192.168.192.252 count=3
   SEQ HOST                                     SIZE TTL TIME       STATUS                                                                                                                                           
   0 192.168.192.252                            56  64 407us     
   1 192.168.192.252                            56  64 452us     
   2 192.168.192.252                            56  64 451us     
   sent=3 received=3 packet-loss=0% min-rtt=407us avg-rtt=436us max-rtt=452us 
   ```

:::tip
你应在 [ZeroTier 云控制台](https://my.zerotier.com/) 中为特定内部子网指定路由，以确保从其他设备连接时能够访问这些网络。
:::

# 控制器 {#controller}

RouterOS 以节点角色实现 ZeroTier 功能，其中大部分网络配置必须在 ZeroTier 网页仪表板上完成。但是，在你希望在自己的设备上完成所有配置的情况下，RouterOS 提供托管自己的控制器的功能。

一个常见的误解是将网络控制器与根服务器（planet 和 moons）混为一谈。根服务器是在 **[VL1 层](https://docs.zerotier.com/zerotier/manual/#2networkhypervisoroverviewaname2a)** 运行的连接促进器。网络控制器是配置管理器和证书颁发机构，属于 **[VL2 层](https://docs.zerotier.com/zerotier/manual/#22vl2theethernetvirtualizationlayeraname2_2a)。** 通常，根服务器不加入或控制虚拟网络，网络控制器也不是根服务器，不过一个节点可以同时承担两者。

每个 ZeroTier 实例都有一个可用于托管虚拟网络的自托管网络控制器。控制器负责允许成员加入网络，并颁发包括证书在内的默认配置信息。理论上，控制器最多可托管 2^24 个网络并服务数百万台设备，但你应将大量网络分散到多个控制器上，以实现负载均衡和容错。

控制器在 [`/zerotier/controller`](../cli-reference/zerotier/controller/index.md) 菜单中配置。

## 配置示例 {#configuration-example-1}

本示例使用 RouterOS 内置的 ZeroTier 控制器向新网络主机发送适当的证书、凭据和配置信息。控制器运行在“RouterOS Home”设备上，并将 3 台设备加入网络：一部手机、一台笔记本电脑和一台 RouterOS Office 设备。一个网络最多可加入 100 台设备。

![](/img/a615ed03be4e8fb8.webp)

### RouterOS 家庭 {#routeros-home}

首先，启用运行在 **VL1** 层级的默认实例：

```ros
[admin@Home] /zerotier> print
Columns: NAME, PORT, IDENTITY.PUBLIC
# NAME  PORT  IDENTITY.PUBLIC
;;; ZeroTier Central controller - https://my.zerotier.com/
0 zt1   9993  879c0b5265:0:d5fd2d17805e011d9b93ce8779385e427c8f405e520eea9284809d8444de0335a817xxb21aa4ba153bfbc229ca34d94e08de96d925a4aaa19b252da546693a28
```

現在，透過控制器部分建立一個新網路，該部分執行在 **VL2** 層級。每個網路都有自己的控制器，每個網路 ID 都由控制器地址和控制器 ID 組合生成。

使用 ***private=yes*** 選項以獲得更安全的網路：

```ros
[admin@Home] /zerotier> controller/add name=ZT-private instance=zt1 ip-range=172.27.27.10-172.27.27.20 private=yes routes=172.27.27.0/24
[admin@Home] /zerotier> controller/print
Columns: INSTANCE, NAME, NETWORK, PRIVATE
# INSTANCE  NAME        NETWORK           PRIVATE
0 zt1       ZT-private  879c0b5265a99e4b  yes
```

在介面部分下新增新網路：

```ros
[admin@Home] /zerotier> interface/add network=879c0b5265a99e4b name=myZeroTier instance=zt1 
[admin@Home] /zerotier> interface/print interval=1
Columns: NAME, MAC-ADDRESS, NETWORK, STATUS
# NAME        MAC-ADDRESS        NETWORK           STATUS
0 myZeroTier  4A:19:35:6E:00:6E  879c0b5265a99e4b  ACCESS_DENIED
```

每個新對等節點都會向控制器請求加入網路。在這種情況下，狀態為 *ACCESS\_DENIED*，並且必須授權該對等節點，因為使用了 **private=yes** 選項。

授權後，網路中的每個成員都會從控制器收到有關新對等節點的資訊，以及與其交換封包的批准：

```ros
[admin@Home] /zerotier> controller/member/print
Columns: NETWORK, ZT-ADDRESS
# NETWORK     ZT-ADDRESS
0  ZT-private  879a0b5265
[admin@Home] /zerotier> controller/member/set 0 authorized=yes
```

## 驗證新配置的 IP 地址和路由 {#verify-newly-configured-ip-address-and-route}

```ros
[admin@Home] /zerotier> `/ip/address/print` where interface~"Zero"
Flags: D - DYNAMIC
Columns: ADDRESS, NETWORK, INTERFACE
# ADDRESS          NETWORK      INTERFACE
4 D 172.27.27.15/24  172.27.27.0  myZeroTier

[admin@Home] /zerotier> `/ip/route/pr` where gateway~"Zero"
Flags: D - DYNAMIC; A - ACTIVE; c, y - COPY
Columns: DST-ADDRESS, GATEWAY, DISTANCE
    DST-ADDRESS     GATEWAY     DISTANCE
DAc 172.27.27.0/24  myZeroTier         0
```

### RouterOS 辦公 {#routeros-office}

在 Office 裝置上進行配置。啟用預設例項，並請求控制器加入 *879c0b5265a99e4b* 網路：

```ros
[admin@office] /zerotier> interface/add network=879c0b5265a99e4b instance=zt1 name=ZT-interface 
[admin@office] /zerotier> interface/print interval=1
Columns: NAME, MAC-ADDRESS, NETWORK, STATUS
# NAME          MAC-ADDRESS        NETWORK           STATUS
0 ZT-interface  4A:40:1C:38:97:BA  879c0b5265a99e4b  ACCESS_DENIED
```

如前所述，由於網路是私有的，新對等節點必須在“RouterOS Home”裝置上獲得授權。之後，驗證從控制器收到的 IP 地址和路由：

```ros
[admin@Home] /zerotier> controller/member/print
Flags: A - AUTHORIZED
Columns: NETWORK, ZT-ADDRESS, IP-ADDRESS, LAST-SEEN
# NETWORK     ZT-ADDRESS  IP-ADDRESS    LAST-SEEN
0 A  ZT-private  879a0b5265  172.27.27.15           
1 A  ZT-private  554a914c7f  172.27.27.17           
2 A  ZT-private  a83ac6032a  172.27.27.10           
3    ZT-private  deba5dc5b1  172.27.27.13  3s348ms  
[admin@Home] /zerotier> controller/member/set 3 authorized=yes
[admin@Home] /zerotier> controller/member/print               
Flags: A - AUTHORIZED
Columns: NETWORK, ZT-ADDRESS, IP-ADDRESS, LAST-SEEN
# NETWORK     ZT-ADDRESS  IP-ADDRESS    LAST-SEEN
0 A  ZT-private  879a0b5265  172.27.27.15           
1 A  ZT-private  554a914c7f  172.27.27.17           
2 A  ZT-private  a83ac6032a  172.27.27.10           
3 A  ZT-private  deba5dc5b1  172.27.27.13  4s55ms 
```

驗證透過 ZeroTier 獲取的 IP 地址和路由：

```ros
[admin@office] /zerotier> `/ip/address/print` where interface~"ZT"
Flags: D - DYNAMIC
Columns: ADDRESS, NETWORK, INTERFACE
# ADDRESS          NETWORK      INTERFACE
0 D 172.27.27.13/24  172.27.27.0  ZT-interface

[admin@office] /zerotier> `/ip/route/print` where gateway~"ZT"
Flags: D - DYNAMIC; A - ACTIVE; c, y - COPY
Columns: DST-ADDRESS, GATEWAY, DISTANCE
    DST-ADDRESS     GATEWAY       DISTANCE
DAc 172.27.27.0/24  ZT-interface         0
```

### 其他裝置 {#other-devices}

[下載 ZeroTier 應用](https://www.zerotier.com/download/)到你的手機或計算機，並加入你新建立的網路：

1. 在筆記型電腦上的 ZeroTier 應用中，加入 *879c0b5265a99e4b* 網路。
2. 使用 ZeroTier 移動應用加入 *879c0b5265a99e4b* 網路。

:::warning
所有其他新主機也必須在 `/zerotier/controller/member/` 部分中獲得授權。
:::

![](/img/3028aaa4ec6e1981.webp)

![](/img/9c8d77f1a4790aaf.png)
