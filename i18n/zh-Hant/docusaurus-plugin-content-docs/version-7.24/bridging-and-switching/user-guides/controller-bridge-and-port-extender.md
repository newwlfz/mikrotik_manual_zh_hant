---
sidebar_key: "bridging-and-switching/user-guides/controller-bridge-and-port-extender"
sidebar_position: 4
title: "控制器橋接與埠擴充套件器"
sidebar_label: "控制器橋接與埠擴充套件器"
description: "RouterOS 中的 Controller Bridge (CB) 和 Port Extender (PE) 可為 CRS3xx 交換器實現具有簡化管理的擴充套件網路拓撲，允許透過級聯/上游進行虛擬埠擴充套件和集中控制……"
tags:
  - 'controller-bridge'
  - 'port-extender'
  - 'vlan'
source: https://manual.mikrotik.com/docs/7.24/bridging-and-switching/user-guides/controller-bridge-and-port-extender
captured_at: '2026-11-07T17:11:03.548Z'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

:::danger
該功能自 v7.18 起已從 RouterOS 中移除。
:::

---

Controller Bridge (CB) 和 Port Extender (PE) 是 RouterOS 中針對 CRS3xx 系列交換器的 IEEE 802.1BR 標準實現。它允許透過 PE 裝置虛擬擴充套件 CB 埠，並從單個控制裝置管理這些擴充套件介面。此類配置提供了簡化的網路拓撲、靈活性、更高的埠密度以及更簡便的管理。Controller Bridge 和 Port Extender 拓撲示例如下。

![CB Summary](/img/2e226d34e405eb3e.webp)

Controller Bridge 透過**級聯埠**與 Port Extender 建立通訊。同樣，Port Extender 僅透過**上游埠**與 Controller Bridge 通訊。在 PE 裝置上，必須配置控制埠，並且只有一個埠（最靠近 CB 的埠）充當上游埠。其他控制埠可以作為上游埠的備份，甚至可以作為串聯連線交換器的級聯埠（例如上圖中的 Port Extender 2 和 3）。級聯埠和上游埠用於傳送和接收控制流量與網路流量。**擴充套件埠**是由 CB 裝置控制的介面，通常連線到終端主機。擴充套件埠僅傳送和接收網路流量。

請參見下表中各交換器型號支援的功能。

| **型號** | **Controller Bridge** | Port Extender |
| :-- | :-- | :-- |
| netPower 15FR (CRS318-1Fi-15Fr-2S) | **-** | **+** |
| netPower 16P (CRS318-16P-2S+) | **-** | **+** |
| CRS310-1G-5S-4S+ (netFiber 9/IN) | **-** | **+** |
| CRS326-24G-2S+ (RM/IN) | **-** | **+** |
| CRS328-24P-4S+ | **-** | **+** |
| CRS328-4C-20S-4S+ | **-** | **+** |
| CRS305-1G-4S+ | **-** | **+** |
| CRS309-1G-8S+ | **+** | **+** |
| CRS317-1G-16S+ | **+** | **+** |
| CRS312-4C+8XG | **+** | **+** |
| CRS326-24S+2Q+ | **+** | **+** |
| CRS354-48G-4S+2Q+ | **+** | **+** |
| CRS354-48P-4S+2Q+ | **+** | **+** |

### 限制 {#limitations}

儘管控制器允許配置 Port Extender 介面，但某些橋接和交換功能無法使用或無法正常工作。以下是 Controller Bridge 和 Port Extender 最常見的限制。該列表可能會隨著後續 RouterOS 版本而變化。

| 功能 | 支援 |
| :-- | :-- |
| 用於級聯和上游埠的 Bonding | + |
| 網橋 VLAN 過濾 | + |
| 用於擴充套件埠的 Bonding | - |
| Dot1x 認證器（伺服器） | - |
| 入方向和出方向速率 | - |
| 映象 | - |
| 埠入方向 VLAN 過濾 | - |
| 埠隔離 | - |
| 風暴控制 | - |
| 交換規則（ACL） | - |
| L3HW 解除安裝 | - |
| MLAG | - |

## 快速設定 {#quick-setup}

---

在本示例中，我們將建立一個 Controlling Bridge（例如 CRS317-1G-16S+ 交換器），它將透過 SFP+1 介面連線到單個 Port Extender（例如 CRS326-24G-2S+ 交換器）。

首先，在 CB 裝置上配置一個啟用了 VLAN 過濾的網橋：

```ros
/interface/bridge
add name=bridge1 vlan-filtering=yes
```

在同一裝置上，配置一個連線到 PE 裝置並將充當級聯埠的埠：

```ros
/interface/bridge/port-controller
set bridge=bridge1 cascade-ports=sfp-sfpplus1 switch=switch1
```

最後，在 PE 裝置上，只需配置一個控制埠，該埠將被選為上游埠：

```ros
/interface/bridge/port-extender
set control-ports=sfp-sfpplus1 switch=switch1
```

一旦 PE 和 CB 裝置連線，處於同一交換器組中的所有介面（控制埠除外）都將被擴充套件，並可在 CB 裝置上進一步配置。CB 裝置上將自動應用網橋埠配置，將所有擴充套件埠新增到單個網橋中。此配置之後可以修改。

:::warning
為了將某個埠排除在擴充套件之外（例如用於帶外管理目的），還需配置 `excluded-ports` 屬性。
:::

:::warning
請確保不要將 `cascade-ports` 和 `control-ports` 包含在任何路由或橋接配置中。這些埠僅建議用於 CB 和 PE 用途。
:::

## 發現和控制協定 {#discovery-and-control-protocols}

---

在擴充套件埠上進行幀轉發之前，Controlling Bridge 和 Port Extender 必須相互發現並交換必要資訊。

啟用 CB 和 PE 的裝置使用帶有特定 Port Extension TLV 的鄰居發現協定 LLDP。這允許 CB 和 PE 裝置在級聯埠和控制埠上通告其支援。

:::warning
CB 和 PE 配置可以覆蓋鄰居發現設定，例如，如果某個級聯埠未包含在鄰居發現介面列表中，LLDP 訊息仍會被髮送。
:::

一旦 CB 和 PE 之間交換了 LLDP 訊息，就會啟動基於邊緣控制協定（ECP）的控制和狀態協定（CSP）。CSP 用於 CB 和 PE 之間，以施加控制並從關聯的 PE 接收狀態資訊——它為擴充套件埠分配唯一 ID，控制資料路徑設定（例如埠 VLAN 成員關係），併發送埠狀態資訊（例如介面統計資訊、PoE-out 監控）。ECP 提供可靠且按序的幀傳送（使用 EtherType 0x8940 編碼）。

:::danger
當前的 CB 實現不支援任何故障轉移技術。一旦 CB 裝置變得不可用，PE 裝置將丟失所有控制規則和資料轉發規則。
:::

## 封包流程 {#packet-flow}

---

為了更好地理解 Controlling Bridge 和 Port Extender 的基本原理，下面提供了封包遍歷過程：

1. 在擴充套件埠上接收到一個 L2 封包。
2. Port Extender 使用 E-TAG 頭（EtherType 0x893F）封裝該封包，並透過上游埠將其轉發給 Controller Bridge。E-TAG 封包包含有關 PE 源埠 ID 的資訊。PE 裝置不進行任何本地交換決策。
3. Controller Bridge 接收到 E-TAG 封包，並確切知道是哪個擴充套件介面接收了它。然後，CB 在內部解封裝該封包，並透過常規交換決策（主機學習、目的地址查詢、VLAN 過濾等）進行處理。
4. 一旦做出交換決策，CB 將再次使用 E-TAG 封裝原始封包，並透過級聯埠傳送給 Port Extender。
   1. 對於單目的地封包（單播），CB 將在 E-TAG 中包含 PE 目的埠 ID，並透過正確的級聯埠傳送。
   2. 對於多目的地封包（廣播、組播或未知單播），CB 將在 E-TAG 中包含目標組標記和源埠 ID，併為每個級聯埠傳送單個數據包副本。
5. 一旦 PE 裝置在上游埠上收到 E-TAG 封包，PE 會將其解封裝，並透過擴充套件埠傳送原始 L2 封包。
   1. 對於單目的地封包（單播），PE 將僅把封包傳送到正確的擴充套件埠。
   2. 對於多目的地封包（廣播、組播或未知單播），PE 將為每個擴充套件埠傳送單個數據包副本（接收該封包的源埠除外）。

|  |  |
| :-- | :-- |
| ![CB 單播 3](/img/0b036b8c3624374c.webp)<br/> |  |

![CB Broadcast 2](/img/c463f4757394bb7b.webp) 

## Controller Bridge 設定和監控 {#controller-bridge-settings-and-monitoring}

---

本節介紹 Controller Bridge 的設定和監控選項。

**子選單：** `/interface/bridge/port-controller`

| 屬性 | 描述 |
| :-- | :-- |
| **bridge** (*name;*Default: **none**) | 將在其中擴充套件埠的網橋介面。僅當指定了 `bridge` 和 `switch` 屬性時，CB 才會啟用；否則將處於停用狀態。 |
| **cascade-ports** (*interfaces;* Default: **none**) | 將充當級聯埠的介面。也支援使用 802.3ad 或 balance-xor `mode` 的 bonding 介面。 |
| **switch** (*name;*Default: **none**) | 將充當 CB 並確保控制流量和網路流量的交換器。僅當指定了 `bridge` 和 `switch` 屬性時，CB 才會啟用；否則將處於停用狀態。 |

在配置並連線 CB 和 PE 裝置後，每個 PE 裝置將自動顯示在裝置選單中。使用 `print` 和 `monitor` 命令檢視更多詳細資訊。

```ros
[admin@Controller] > /interface/bridge/port-controller/device/print
Flags: I - inactive 
 0   name="pe1" pe-mac=64:D1:54:EB:AE:BC descr="MikroTik RouterOS 6.48beta35 (testing) CRS328-24P-4S+" control-ports=pe1-sfpplus1,pe1-sfpplus2 

 1   name="pe2" pe-mac=64:D1:54:C7:3A:58 descr="MikroTik RouterOS 6.48beta35 (testing) CRS326-24G-2S+" control-ports=pe2-sfpplus1
[admin@Controller] > /interface/bridge/port-controller/device/monitor pe2
                 name: pe2
               status: active
  connected-via-ports: sfp-sfpplus1==pe1-sfpplus1,pe1-sfpplus2==pe2-sfpplus1
   connected-via-devs: controller,pe1
```

**子選單：** `/interface/bridge/port-controller/device`

| 屬性 | 描述 |
| :-- | :-- |
| **connected-via-devs** (*name*) | 顯示從 PE 到 CB 路徑上已連線的裝置。 |
| **connected-via-ports** (*name*) | 顯示從 PE 到 CB 的連線路徑。 |
| **control-ports** (*interfaces*) | PE 裝置控制埠。 |
| **descr** (*name*) | 簡短的 PE 裝置描述。 |
| **name** (*name*) | 自動分配的 PE 裝置名稱。 |
| **pe-mac** (*MAC address*) | PE 裝置 MAC 地址。 |
| **status** (*active \| inactive*) | PE 裝置狀態。 |

此外，每個 PE 裝置介面都可以在埠選單中監控。使用 `print` 和 `monitor` 命令檢視更多詳細資訊。

```ros
[admin@Controller] > /interface/bridge/port-controller/port/print where !disabled
Flags: I - inactive, X - disabled, R - running, U - upstream-port, C - cascade-port 
 #    NAME                                   DEVICE
 0 I  pe1-ether1                             pe1
 1 R  pe1-ether2                             pe1
 2 R  pe1-ether3                             pe1
 3 R  pe1-ether4                             pe1
 4  U pe1-sfpplus1                           pe1
 5 RC pe1-sfpplus2                           pe1
 6 I  pe2-ether1                             pe2
 7 R  pe2-ether2                             pe2
 8 R  pe2-ether3                             pe2
 9 R  pe2-ether4                             pe2
10  U pe2-sfpplus1                           pe2
[admin@Controller] > /interface/bridge/port-controller/port/monitor [find where !disabled]
           name: pe1-ether1 pe1-ether2 pe1-ether3 pe1-ether4 pe1-sfpplus1 pe1-sfpplus2 pe2-ether1 pe2-ether2 pe2-ether3 pe2-ether4 pe2-sfpplus1
         status: unknown    link-ok    link-ok    link-ok    no-link      link-ok      unknown    link-ok    link-ok    link-ok    no-link
           rate:            1Gbps      1Gbps      1Gbps      10Gbps       10Gbps                  1Gbps      1Gbps      1Gbps      10Gbps
    port-status: not-added  ok         ok         ok         ok           ok           not-added  ok         ok         ok         ok
           pcid:            457        458        459        480          481                     509        510        511        532
```

**子選單：** `/interface/bridge/port-controller/port`

| 屬性 | 描述 |
| :-- | :-- |
| **device** (*name*) | 自動分配的 PE 裝置名稱。 |
| **name** (*name*) | 自動分配的 PE 埠名稱。 |
| **pcid** (*integer*) | 自動分配的埠識別符號。 |
| **port-status** (*dev-inactive \| not-added \| ok*) | PE 埠狀態。 |
| **rate** (*bps*) | 連線的資料速率。 |
| **status** (*link-ok \| no-link \| unknown*) | PE 埠鏈路狀態。 |

Controller Bridge 可以在埠 PoE 選單中監控來自 Port Extender 的 PoE-out 相關資訊。使用 `print` 和 `monitor` 命令檢視更多詳細資訊。有關 PoE-out 的更多資訊，請訪問 [PoE-out 手冊](../../hardware/poe-out.md)。

```ros
[admin@Controller] > /interface/bridge/port-controller/port/poe/print
 # NAME                                    DEVICE
 0 pe1-ether1                              pe1
 1 pe1-ether2                              pe1
 2 pe1-ether3                              pe1
 3 pe1-ether4                              pe1
 4 pe1-ether5                              pe1
 5 pe1-ether6                              pe1
 6 pe1-ether7                              pe1
...
[admin@Controller] > /interface/bridge/port-controller/port/poe/monitor pe1-ether2,pe1-ether3
               name: pe1-ether2 pe1-ether3
     poe-out-status: powered-on powered-on
    poe-out-voltage: 52.8V      52.9V
    poe-out-current: 123mA      95mA
      poe-out-power: 6.4W       5W
```

## Port Extender 設定 {#port-extender-settings}

---

本節介紹 Port Extender 設定。

**子選單：** `/interface/bridge/port-extender`

| 屬性 | 描述 |
| :-- | :-- |
| **control-ports** (*interfaces;* Default: **none**) | 將連線到 CB（上游埠）或以串聯方式連線其他 PE 裝置（級聯埠）的介面。也支援使用 802.3ad 或 balance-xor `mode` 的 bonding 介面。 |
| **excluded-ports** (*interfaces;* Default: **none**) | 將不被擴充套件的介面。 |
| **switch** (*name;*Default: **none**) | 將充當擴充套件器並確保控制流量和網路流量的交換器。僅當指定此屬性時，PE 才會啟用；否則將處於停用狀態。 |

## 配置示例 {#configuration-examples}

---

下面描述了最常見的配置示例。要使 CB 和 PE 配置正常工作，需要啟用網橋 VLAN 過濾，因此請務必先理解過濾原理——[網橋 VLAN 過濾](../index.md#bridge-vlan-filtering)、[網橋 VLAN 表](./bridge-vlan-table.md)。

### 基本 CB 和 PE 配置 {#basic-cb-and-pe-configuration}

在本示例中，CRS317-1G-16S+ 裝置用作 Controller Bridge，CRS328-24P-4S+ 用作 Port Extender；請參見下面的連線示意圖。

![Basic CB PE Configuration](/img/0b58575d7d9204a3.webp)

首先，配置 CB 裝置。這可以透過新增一個啟用了 VLAN 過濾的網橋介面來完成。此外，將任意本地介面新增到同一網橋中，這樣可以在此類本地介面和擴充套件介面之間轉發流量。在本示例中，添加了 sfp-sfpplus2 介面。

```ros
/interface/bridge
add name=bridge1 vlan-filtering=yes
/interface/bridge/port
add bridge=bridge1 interface=sfp-sfpplus2
```

要啟用 CB，請指定 bridge、switch 以及至少一個級聯埠。確保級聯埠未包含在網橋或路由配置中。建議這些埠僅用於 CB 和 PE。

```ros
/interface/bridge/port-controller
set bridge=bridge1 cascade-ports=sfp-sfpplus1 switch=switch1
```

要啟用 PE，請配置控制埠和 switch。此外，使用 `excluded-ports` 屬性配置一個或多個不應被擴充套件的介面（例如用於帶外管理目的）。在本示例中，所有交換器埠都將被擴充套件。

```ros
/interface/bridge/port-extender
set control-ports=sfp-sfpplus4 switch=switch1
```

一旦 PE 和 CB 裝置完成發現並啟動控制和狀態協定（CSP），RouterOS 將永久建立新介面並將其新增到 CB 裝置上的網橋中。介面以自動分配的 PE 裝置名稱加上預設介面名稱命名。這些介面名稱之後可以修改。請注意，控制埠和排除埠也會顯示在介面列表中，但它們不包含在網橋中。

```ros
[admin@Controller_Bridge] > /interface/print where name~"pe"
Flags: D - dynamic, X - disabled, R - running, S - slave 
 #     NAME                                TYPE       ACTUAL-MTU L2MTU  MAX-L2MTU
 0  RS pe1-ether1                          extport          1500  1584
 1  RS pe1-ether2                          extport          1500  1584
 2  RS pe1-ether3                          extport          1500  1584
 3   S pe1-ether4                          extport          1500  1584
 4   S pe1-ether5                          extport          1500  1584
 5   S pe1-ether6                          extport          1500  1584
 6   S pe1-ether7                          extport          1500  1584
 7   S pe1-ether8                          extport          1500  1584
 8   S pe1-ether9                          extport          1500  1584
 9   S pe1-ether10                         extport          1500  1584
10   S pe1-ether11                         extport          1500  1584
11   S pe1-ether12                         extport          1500  1584
12   S pe1-ether13                         extport          1500  1584
13   S pe1-ether14                         extport          1500  1584
14   S pe1-ether15                         extport          1500  1584
15   S pe1-ether16                         extport          1500  1584
16   S pe1-ether17                         extport          1500  1584
17   S pe1-ether18                         extport          1500  1584
18   S pe1-ether19                         extport          1500  1584
19   S pe1-ether20                         extport          1500  1584
20   S pe1-ether21                         extport          1500  1584
21   S pe1-ether22                         extport          1500  1584
22   S pe1-ether23                         extport          1500  1584
23   S pe1-ether24                         extport          1500  1584
24  RS pe1-sfpplus1                        extport          1500  1584
25  RS pe1-sfpplus2                        extport          1500  1584
26  RS pe1-sfpplus3                        extport          1500  1584
27     pe1-sfpplus4                        extport          1500  1584
[admin@Controller_Bridge] > interface bridge port print 
Flags: X - disabled, I - inactive, D - dynamic, H - hw-offload 
 #     INTERFACE              BRIDGE             HW  PVID PRIORITY  PATH-COST INTERNAL-PATH-COST    HORIZON
 0   H sfp-sfpplus2           bridge1            yes    1     0x80         10                 10       none
 1   H pe1-ether1             bridge1            yes    1     0x80         10                 10       none
 2   H pe1-ether2             bridge1            yes    1     0x80         10                 10       none
 3   H pe1-ether3             bridge1            yes    1     0x80         10                 10       none
 4 I H pe1-ether4             bridge1            yes    1     0x80         10                 10       none
 5 I H pe1-ether5             bridge1            yes    1     0x80         10                 10       none
 6 I H pe1-ether6             bridge1            yes    1     0x80         10                 10       none
 7 I H pe1-ether7             bridge1            yes    1     0x80         10                 10       none
 8 I H pe1-ether8             bridge1            yes    1     0x80         10                 10       none
 9 I H pe1-ether9             bridge1            yes    1     0x80         10                 10       none
10 I H pe1-ether10            bridge1            yes    1     0x80         10                 10       none
11 I H pe1-ether11            bridge1            yes    1     0x80         10                 10       none
12 I H pe1-ether12            bridge1            yes    1     0x80         10                 10       none
13 I H pe1-ether13            bridge1            yes    1     0x80         10                 10       none
14 I H pe1-ether14            bridge1            yes    1     0x80         10                 10       none
15 I H pe1-ether15            bridge1            yes    1     0x80         10                 10       none
16 I H pe1-ether16            bridge1            yes    1     0x80         10                 10       none
17 I H pe1-ether17            bridge1            yes    1     0x80         10                 10       none
18 I H pe1-ether18            bridge1            yes    1     0x80         10                 10       none
19 I H pe1-ether19            bridge1            yes    1     0x80         10                 10       none
20 I H pe1-ether20            bridge1            yes    1     0x80         10                 10       none
21 I H pe1-ether21            bridge1            yes    1     0x80         10                 10       none
22 I H pe1-ether22            bridge1            yes    1     0x80         10                 10       none
23 I H pe1-ether23            bridge1            yes    1     0x80         10                 10       none
24 I H pe1-ether24            bridge1            yes    1     0x80         10                 10       none
25   H pe1-sfpplus1           bridge1            yes    1     0x80         10                 10       none
26   H pe1-sfpplus2           bridge1            yes    1     0x80         10                 10       none
27   H pe1-sfpplus3           bridge1            yes    1     0x80         10                 10       none
```

現在，CRS317-1G-16S+ 裝置已使用 CRS328-24P-4S+ 裝置擴充套件了其埠，並且可以在所有橋接埠之間進行封包轉發。

### Trunk 和 Access 埠 {#trunk-and-access-ports}

在本示例中，將在 Controller Bridge 裝置上建立 untagged（access）和 tagged（trunk）埠配置。請參見下面的網路圖。

![CB PE VLANs](/img/6a112aa3a790d572.webp)First, configure the CB and PE devices. The configuration is identical to the previous example. Use this configuration for the CB device.

```ros
/interface/bridge
add name=bridge1 vlan-filtering=yes
/interface/bridge/port
add bridge=bridge1 interface=sfp-sfpplus2
/interface/bridge/port-controller
set bridge=bridge1 cascade-ports=sfp-sfpplus1 switch=switch1
```

將此配置用於 PE 裝置。

```ros
/interface/bridge/port-extender
set control-ports=sfp-sfpplus4 switch=switch1
```

在擴充套件埠成功建立並新增到 CB 裝置上的網橋後，我們可以開始配置與 VLAN 相關的屬性。首先，使用 `pvid` 屬性將 access 埠配置到各自的 VLAN ID。在 `/interface/bridge/port` 選單中使用 `print` 命令找出確切的介面名稱。

```ros
/interface/bridge/port
set [find interface=pe1-ether1] pvid=10
set [find interface=pe1-ether2] pvid=20
set [find interface=pe1-ether3] pvid=30
```

然後新增網橋 VLAN 條目，並指定 tagged、untagged 埠。請注意，有兩個 tagged 埠——名為 sfp-sfpplus2 的本地埠和名為 pe1-sfpplus1 的擴充套件埠。

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=pe1-sfpplus1,sfp-sfpplus2 untagged=pe1-ether1 vlan-ids=10
add bridge=bridge1 tagged=pe1-sfpplus1,sfp-sfpplus2 untagged=pe1-ether2 vlan-ids=20
add bridge=bridge1 tagged=pe1-sfpplus1,sfp-sfpplus2 untagged=pe1-ether3 vlan-ids=30
```

此時 VLAN 已配置，裝置應能夠透過這些埠通訊。但是，建議更進一步，應用一些額外的過濾選項。在本地網橋埠上啟用埠 `ingress-filtering`，並使用 `frame-types` 設定基於封包型別進行幀過濾。

```ros
/interface/bridge/port
set [find interface=pe1-ether1] frame-types=admit-only-untagged-and-priority-tagged
set [find interface=pe1-ether2] frame-types=admit-only-untagged-and-priority-tagged
set [find interface=pe1-ether3] frame-types=admit-only-untagged-and-priority-tagged
set [find interface=pe1-sfpplus1] frame-types=admit-only-vlan-tagged
set [find interface=sfp-sfpplus2] frame-types=admit-only-vlan-tagged ingress-filtering=yes
```

:::warning
擴充套件埠不支援埠入口 VLAN 過濾。
:::

### 級聯多個 Port Extender 並使用 bonding 介面 {#cascading-multiple-port-extenders-and-using-bonding-interface}

在本示例中，兩個 PE 裝置（CRS328-24P-4S+ 和 CRS326-24G-2S+）將新增到 CB（CRS317-1G-16S+）。為了提高上游埠和級聯埠的吞吐量，將建立 [bonding 介面](../../high-availability-solutions/bonding.md)。請參見下面的網路圖。

![Bonding Cascade](/img/79872d18d20c4e0b.webp)

CB 和 PE 配置與第一個示例類似，主要區別是 bonding 介面的使用。首先，配置 CB 裝置——為級聯埠建立 bonding 介面，建立網橋並新增任何所需的本地網橋埠，最後啟用 CB。使用以下命令：

```ros
/interface/bonding
add mode=802.3ad name=bond1 slaves=sfp-sfpplus1,sfp-sfpplus2
/interface/bridge
add name=bridge1 vlan-filtering=yes
/interface/bridge/port
add bridge=bridge1 interface=sfp-sfpplus3
/interface/bridge/port-controller
set bridge=bridge1 cascade-ports=bond1 switch=switch1
```

然後配置 Port Extender 1 裝置。此裝置需要兩個 bonding 介面——第一個將用作上游埠，第二個將用作 Port Extender 2 裝置的級聯埠。此外，使用 `excluded-ports` 屬性配置一個或多個不應被擴充套件的介面（例如用於帶外管理目的）。在本示例中，所有交換器埠都將被擴充套件。

```ros
/interface/bonding
add mode=802.3ad name=bond1 slaves=sfp-sfpplus1,sfp-sfpplus2
add mode=802.3ad name=bond2 slaves=sfp-sfpplus3,sfp-sfpplus4
/interface/bridge/port-extender
set control-ports=bond1,bond2 switch=switch1
```

最後，配置 Port Extender 2 裝置——建立 bonding 介面並啟用 PE。如有必要，另外配置一個或多個 `excluded-ports`。在本示例中，所有交換器埠都將被擴充套件。

```ros
/interface/bonding
add mode=802.3ad name=bond1 slaves=sfp-sfpplus1,sfp-sfpplus2
/interface/bridge/port-extender
set control-ports=bond1 switch=switch1
```

現在，CRS317-1G-16S+ 裝置已擴展出其埠，增加了 48 個千兆乙太網埠，並且可以在所有橋接埠之間實現封包轉發。

在裝置選單中使用 `monitor` 命令檢視 PE 裝置連線路徑。另外，在埠選單中使用 `print` 命令檢視哪些 PE 介面用作上游埠和級聯埠。

```ros
[admin@Controller_Bridge] > /interface/bridge/port-controller/device/monitor [find]
                   name: pe1                    pe2
                 status: active                 active
    connected-via-ports: bond1==pe1-cntrl-bond1 bond1==pe1-cntrl-bond1
                                                pe1-cntrl-bond2==pe2-cntrl-bond1
     connected-via-devs: controller             controller
                                                pe1
[admin@Controller_Bridge] > /interface/bridge/port-controller/port/print where running or upstream-port 
Flags: I - inactive, X - disabled, R - running, U - upstream-port, C - cascade-port 
 #    NAME                                                  DEVICE                                                 
 0 R  pe1-ether2                                            pe1                                                    
 1 R  pe1-ether3                                            pe1                                                    
 2 R  pe1-ether4                                            pe1                                                    
 3  U pe1-sfpplus1                                          pe1                                                    
 4  U pe1-sfpplus2                                          pe1                                                    
 5 RC pe1-sfpplus3                                          pe1                                                    
 6 RC pe1-sfpplus4                                          pe1                                                    
 7 R  pe2-ether1                                            pe2                                                    
 8 R  pe2-ether2                                            pe2                                                    
 9 R  pe2-ether3                                            pe2                                                    
10 R  pe2-ether4                                            pe2                                                    
11  U pe2-sfpplus1                                          pe2                                                    
12  U pe2-sfpplus2                                          pe2                                                    
```

### 配置修改和移除 {#configuration-modification-and-removal}

在某些情況下，需要調整（例如 PE 裝置需要新的控制埠）或完全移除 CB 和 PE 裝置配置。要修改 PE 裝置配置，應首先從 CB 裝置移除所有相關的 PE 裝置配置。只有這樣才能應用新配置。

首先，要從 CB 移除 PE 配置，請使用以下命令停用 PE：

```ros
/interface/bridge/port-extender/set switch=none control-ports="" excluded-ports=""
```

然後，在 CB 裝置上移除相關的網橋以及其他使用過 PE 介面的 RouterOS 配置（例如，檢視 `/interface/bridge/port` 和 `/interface/bridge/vlan` 選單中的 export）。例如，要移除特定 PE 裝置的所有網橋埠，請使用以下命令：

```ros
/interface/bridge/port/remove [find interface~"pe1"]
```

配置移除後，可以從 CB 裝置列表中移除 PE。此命令還會自動從 CB 介面列表中移除所有 PE 裝置介面。如果 CB 上仍應用了某些 PE 介面配置，則該配置將不再有效。使用 `print` 命令找出 PE 裝置名稱。

```ros
/interface/bridge/port-controller/device/remove [find name=pe1]
```
