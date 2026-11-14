---
sidebar_key: "virtual-private-networks/zerotier"
sidebar_position: 12
title: "ZeroTier"
sidebar_label: "ZeroTier"
description: "ZeroTier 是適用於 MikroTik RouterOS 的網路虛擬化引擎，它透過乙太網虛擬化和加密的點對點網路實現安全的跨網路裝置連線。它支援遊戲、LAN 訪問、NAT 穿透和遠端 Pi-Hole 管理，同時需要正確配置 UDP 埠、選擇 NAT 型別並儘量減少 NAT 層數以獲得可靠的連線。"
tags:
  - 'zerotier'
  - 'ipv6'
source: https://manual.mikrotik.com/docs/7.24/virtual-private-networks/zerotier
captured_at: '2026-11-04T11:35:20+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

[ZeroTier](https://docs.zerotier.com/) 網路虛擬機器監控器是一個自包含的網路虛擬化引擎，它實現了類似於 VXLAN 的乙太網虛擬化層，構建在加密安全的全球點對點網路之上。它提供與企業級 SDN 交換器相當的高階網路虛擬化和管理能力，但可跨區域網路和廣域網路，並連線幾乎任何型別的應用或裝置。

MikroTik 已將 ZeroTier 新增到 RouterOS v7.1rc2，作為面向 **ARM/ARM64** 架構的獨立軟體包。

### 等等，那我能用它做什麼？ {#wait-so-what-can-i-use-it-for}

- 在家中託管遊戲伺服器（適用於僅限 LAN 的遊戲），或者只是與朋友建立 LAN 聚會。
- 直接訪問 NAT 後的 LAN 裝置。
- 無需向網際網路開放埠即可透過 SSH 訪問 LAN 裝置。
- 透過網際網路從任何地方使用你本地的 Pi-Hole 設定。

:::info
重要

ZeroTier 功能可能會被 device-mode 阻止。配置 ZeroTier 之前，請確保已在 system/device-mode 中啟用它。（[更多資訊](../system-information-and-utilities/device-mode.md)
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

這些 ZeroTier 推薦指南與絕大多數使用商用閘道器和接入點的典型部署一致：

- 不要限制出站 UDP 流量。
- 在網路上支援 UPnP 或 NAT-PMP 可以大幅提升效能，因為它允許 ZeroTier 端點對映外部埠並完全避免 NAT 穿透。
- 建議使用 IPv6；如果直連鏈路兩端都支援 IPv6，它可以大幅提高直連可靠性。若使用 IPv6，則應在沒有 NAT 的情況下實施（IPv6 完全不需要 NAT，NAT 只會增加複雜性），並使用允許雙向 UDP 會話的狀態化防火牆。
- 不要使用“對稱”NAT。請使用“全錐形”或“埠受限錐形”NAT。對稱 NAT 對點對點流量極其不利，會降低 VoIP、影片聊天、遊戲、WebRTC 以及許多其他協定和 ZeroTier 的效能。
- ZeroTier 端點與網際網路之間不應存在超過一層 NAT。多層 NAT 會因不同層級的狀態和行為之間混亂的互動而引入連線不穩定性。**禁止雙重 NAT。**
- NAT 的埠對映或連線超時時間不應短於 60 秒。
- 每個由 NAT 管理的外部 IP 地址後最多放置約 16,000 臺裝置，以確保每臺裝置都能對映足夠數量的埠。
- 交換器和無線接入點應允許本地裝置之間的直接本地流量。關閉任何“本地隔離”功能。某些交換器可能允許更細粒度的控制；在這些裝置上，允許與 9993 相關的本地 UDP 流量（或一般情況下的本地 UDP 流量）即可。

## 配置示例 {#configuration-example}

![](/img/973091414929cb14.webp)

預設情況下，ZeroTier 被設計為零配置。使用者無需編寫配置檔案或提供其他節點的 IP 地址，即可啟動新的 ZeroTier 節點。它還被設計為快速。世界上任意兩臺裝置都應能夠幾乎瞬間找到彼此並通訊，因此以下示例將在 RouterOS 裝置上啟用 ZeroTier，並使用 ZeroTier 應用連線一部手機。

1. 在 [my.zerotier.com](https://my.zerotier.com/) 上註冊並**建立網路**，獲取 *網路 ID*，在此示例中為：*1d71939404912b40*。  
   ![](/img/8a1dad2da1ff845b.webp)
2. [下載](https://mikrotik.com/download)並在 RouterOS 中安裝 ZeroTier NPK 軟體包，你可以在“額外軟體包”下找到它；將軟體包上傳到裝置並重啟裝置。
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

6. 現在你可能需要允許從 ZeroTier 介面到路由器的連線，並且**可選地**允許到其他 LAN 介面的連線：

   ```ros
   /ip/firewall/filter/add action=accept chain=forward in-interface=zerotier1 place-before=0
   /ip/firewall/filter/add action=accept chain=input in-interface=zerotier1 place-before=0
   ```

7. 在你的智慧手機或計算機上安裝 ZeroTier 用戶端，並按照 ZeroTier 手冊瞭解如何從那裡連線到同一網路。
8. 如果 **"****訪問控制"** 設定為 **"Private"**，則必須先授權節點，節點才能成為成員：  
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

### 对等节点 {#peer}

**子菜单：** `/zerotier/peer`

ZeroTier 的对等节点是一个信息性部分，列出你的节点已知的节点。除非节点加入同一网络并获得授权，否则它们无法相互通信。

```ros
[admin@Home] > `/zerotier/peer/print` 
Columns: INSTANCE, ZT-ADDRESS, LATENCY, ROLE, PATH
# INSTANCE  ZT-ADDRESS  LATENCY  ROLE    PATH
0 zt1       61d294b9cb  186ms    PLANET  active,preferred,50.7.73.34/9993,recvd:4s526ms                  
1 zt1       62f865ae71  270ms    PLANET  active,preferred,50.7.252.138/9993,recvd:4s440ms,sent:9s766ms   
2 zt1       778cde7190  132ms    PLANET  active,preferred,103.195.103.66/9993,recvd:4s579ms,sent:9s766ms 
3 zt1       992fcf1db7  34ms     PLANET  active,preferred,195.181.173.159/9993,recvd:4s675ms,sent:4s712ms
4 zt1       159924d630  130ms    LEAF    active,preferred,34.121.192.xx/21002,recvd:3s990ms,sent:3s990ms
```

# 引數 {#parameters}

**子選單：** `/zerotier`

| 屬性                                                                                                                                          | 說明                                                                                                 |
|:--|:--|
| **name**(*string*; default: **zt1**)                                                                                                              | 例項名稱。                                                                                              |
| **port** (*number;*default: **9993**)                                                                                                             | 例項監聽的埠號。                                                                         |
| **identity** (*string*; default) *[敏感](https://help.MikroTik.com/docs/spaces/ROS/pages/380076066/List+of+menus+with+sensitive+parameters)* | 例項的 40 位唯一地址。                                                                             |
| **interface** (string; default: **all)**                                                                                                          | 用於發現 ZeroTier 對等節點的介面列表，透過使用 ARP 和 IP 型別連線來發現。 |
| **route-distance** (number; default: **1** )                                                                                                      | 從 planet/moon 伺服器獲取的路由的路由距離。                                                |

```ros
[admin@MikroTik] > zerotier/interface/
```

| 屬性 | 描述 |
|:--|:--|
| **allow-default** (*string; yes | no)*         | 網路可以覆蓋系統的預設路由（強制 VPN 模式）。 |
| **allow-global**(*string; yes | no)*           | ZeroTier IP 地址和路由可以與公共 IP 空間重疊。      |
| **allow-managed**(*string; yes | no)*          | 分配 ZeroTier 管理的 IP 地址和路由。             |
| **arp-timeout** ( *number*; default: **auto**) | ARP 超時值。                                                |
| **comment** (*string*; Default: )              | 介面的描述性註釋。                            |
| **copy-from**                                  | 允許複製現有介面配置。                  |
| **disable-running-check**(*string; yes | no)*  | 強制介面處於“running”狀態。                                |
| **instance**(*string*; Default:**zt1**)        | ZeroTier 例項名稱。                                            |
| **name**(*string*; default: **zerotier1**)     | 短名稱。                                                      |
| **network**(*string*; Default)                 | 16 位網路 ID。                                               |

# 控制器 {#controller}

RouterOS 以節點角色實現 ZeroTier 功能，其中大部分網路配置必須在 ZeroTier 網頁儀表板上完成。但是，在你希望在自己的裝置上完成所有配置的情況下，RouterOS 提供託管自己的控制器的功能。

一個常見的誤解是將網路控制器與根伺服器（planet 和 moons）混為一談。根伺服器是在 **[VL1 層](https://docs.zerotier.com/zerotier/manual/#2networkhypervisoroverviewaname2a)** 執行的連線促進器。網路控制器是配置管理器和證書頒發機構，屬於 **[VL2 層](https://docs.zerotier.com/zerotier/manual/#22vl2theethernetvirtualizationlayeraname2_2a)。** 通常，根伺服器不加入或控制虛擬網路，網路控制器也不是根伺服器，不過一個節點可以同時承擔兩者。

**子選單：** `/zerotier/controller`

每個 ZeroTier 例項都有一個可用於託管虛擬網路的自託管網路控制器。控制器負責允許成員加入網路，並頒發包括證書在內的預設配置資訊。理論上，控制器最多可託管 2^24 個網路並服務數百萬臺（或更多）裝置，但出於負載均衡和容錯原因，我們建議將大量網路分散到多個控制器上。

## 引數 {#parameters-1}

| 屬性 | 描述 |
|:--|:--|
| **broadcast** *( yes | no; Default: **yes**)*    | 允許接收廣播（*FF:FF:FF:FF:FF:FF*）封包。                                                                                                                                                                                                                                                             |
| **comment** (*string*; Default: )                | 控制器的描述性註釋。                                                                                                                                                                                                                                                                              |
| **copy-from** (*string*; Default: )         | 複製現有專案。它從另一個專案獲取新專案屬性的預設值。如果你不想製作完全相同的副本，可以為某些屬性指定新值。複製具有名稱的專案時，通常需要為副本指定新名稱。                                     |
| **instance** (*string*; Default: **zt1**)        | ZeroTier 例項名稱。                                                                                                                                                                                                                                                                                              |
| **ip-range** (*IP*; Default: )                   | IP 範圍，*例如 172.16.16.1-172.16.16.254。*                                                                                                                                                                                                                                                                  |
| **ip6-6plane** *( yes | no; Default: **no**)*    | 此選項為每個成員在 /40 網路中分配一個 /80，但使用 NDP 模擬將 *所有* 位於該 /80 下的 IP 路由到其所有者。`6plane` 模式非常適合 Docker 等用例，因為它允許每個成員在其 /80 內分配 IPv6 地址，這些地址可以立即在整個網路中全域性正常工作。 |
| **ip6-rfc4193** *( yes | no; Default: **no**)*   | *rfc4193* 模式為每個成員在 /88 網路上分配一個 /128。                                                                                                                                                                                                                                                       |
| **ip6-range** (*IPv6*; Default: )                | IPv6 範圍，*例如 fd00:feed:feed:beef::-fd00:feed:feed:beef:ffff:ffff:ffff:ffff。*                                                                                                                                                                                                                             |
| **mtu** *(integer;* Default: **2800**)           | 網路 MTU。                                                                                                                                                                                                                                                                                                         |
| **multicast-limit** (*integer*: Default: **32**) | 多播封包的最大接收者數量。                                                                                                                                                                                                                                                                           |
| **name** (*string*; Default: )                   | 此控制器的短名稱。                                                                                                                                                                                                                                                                                    |
| **network** (*string*; Default)                  | 16 位網路 ID。                                                                                                                                                                                                                                                                                                 |
| **private** *( yes | no; Default: **yes**)*      | 啟用訪問控制。                                                                                                                                                                                                                                                                                              |
| **routes** (*IP@GW*; Default: )                  | 按以下格式推送路由：*Routes ::= Route[,Routes]* *Route ::= Dst[@Gw]*                                                                                                                                                                                                                                |

## 配置示例 {#configuration-example-1}

在以下示例中，我們將使用 RouterOS 內建的 ZeroTier 控制器向新的網路主機發送適當的證書、憑據和配置資訊。控制器將從“RouterOS 家庭裝置”執行，我們將把 3 臺裝置加入網路：手機、筆記型電腦、RouterOS 辦公室裝置；但理論上，一個網路中最多可以加入 100 臺裝置。

![](/img/a615ed03be4e8fb8.webp)

### RouterOS 家庭 {#routeros-home}

首先，我們啟用執行在 **VL1** 層的預設例項：

```ros
[admin@Home] /zerotier> print
Columns: NAME, PORT, IDENTITY.PUBLIC
# NAME  PORT  IDENTITY.PUBLIC
;;; ZeroTier Central controller - https://my.zerotier.com/
0 zt1   9993  879c0b5265:0:d5fd2d17805e011d9b93ce8779385e427c8f405e520eea9284809d8444de0335a817xxb21aa4ba153bfbc229ca34d94e08de96d925a4aaa19b252da546693a28
```

現在我們透過控制器部分建立一個新網路，它將執行在 **VL2** 層。每個網路都有自己的控制器，每個網路 ID 都由控制器地址和控制器 ID 組合生成。

請注意，我們使用 ***private=yes*** 選項來獲得更安全的網路：

```ros
[admin@Home] /zerotier> controller/add name=ZT-private instance=zt1 ip-range=172.27.27.10-172.27.27.20 private=yes routes=172.27.27.0/24
[admin@Home] /zerotier> controller/print
Columns: INSTANCE, NAME, NETWORK, PRIVATE
# INSTANCE  NAME        NETWORK           PRIVATE
0 zt1       ZT-private  879c0b5265a99e4b  yes
```

在介面部分下新增我們的新網路：

```ros
[admin@Home] /zerotier> interface/add network=879c0b5265a99e4b name=myZeroTier instance=zt1 
[admin@Home] /zerotier> interface/print interval=1
Columns: NAME, MAC-ADDRESS, NETWORK, STATUS
# NAME        MAC-ADDRESS        NETWORK           STATUS
0 myZeroTier  4A:19:35:6E:00:6E  879c0b5265a99e4b  ACCESS_DENIED
```

每個新對等節點都會請求控制器加入網路；在這種情況下，我們會看到 *ACCESS\_DENIED* 狀態，並且必須授權新對等節點，這是因為我們使用了 **private=yes** 選項。

授權後，網路中的每個成員都會從控制器接收有關新對等節點的資訊以及可以與其交換封包的批准：

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

在辦公室裝置上進行配置。我們將啟用預設例項，並請求控制器加入 *879c0b5265a99e4b* 網路：

```ros
[admin@office] /zerotier> interface/add network=879c0b5265a99e4b instance=zt1 name=ZT-interface 
[admin@office] /zerotier> interface/print interval=1
Columns: NAME, MAC-ADDRESS, NETWORK, STATUS
# NAME          MAC-ADDRESS        NETWORK           STATUS
0 ZT-interface  4A:40:1C:38:97:BA  879c0b5265a99e4b  ACCESS_DENIED
```

如前所述，由於我們的網路是私有網路，我們必須透過“RouterOS 家庭裝置”授權新對等節點。之後驗證從控制器接收到的 IP 地址和路由：

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

1) 透過我們筆記型電腦上的 ZeroTier 應用程式，我們加入 *879c0b5265a99e4b* 網路；

2) 使用 ZeroTier 移動應用加入 *879c0b5265a99e4b* 網路；

:::warning
此外，所有其他新主機都必須在 */zerotier/controller/member/* 部分下進行授權。
:::

![](/img/3028aaa4ec6e1981.webp)

![](/img/9c8d77f1a4790aaf.png)
