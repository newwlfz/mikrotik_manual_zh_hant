---
title: "控制器橋接器與埠擴充器"
description: "RouterOS 中的 Controller Bridge (CB) 與 Port Extender (PE) 可為 CRS3xx 交換器提供具簡化管理的延伸網路拓撲，透過 cascade/upstream 埠實現虛擬埠延伸與集中式控制，但不支援部分功能，例如 extended ports 的 bonding。"
tags:
  - 'controller-bridge'
  - 'port-extender'
  - 'vlan'
source: https://manual.mikrotik.com/docs/7.24/bridging-and-switching/user-guides/controller-bridge-and-port-extender
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

:::danger
此功能已自 RouterOS v7.18 起移除。
:::

---

Controller Bridge（CB）與 Port Extender（PE）是 RouterOS 中針對 CRS3xx 系列交換器實作的 IEEE 802.1BR 標準。它可透過 PE 設備虛擬延伸 CB 埠，並從單一控制設備管理這些延伸介面。此類設定可提供簡化的網路拓撲、彈性、更高的埠密度與易於管理的特性。Controller Bridge 與 Port Extender 拓撲範例如下所示。

![CB Summary](/img/2e226d34e405eb3e.webp)

Controller Bridge 透過 **cascade port** 與 Port Extender 建立通訊。同樣地，Port Extender 只會透過 **upstream port** 與 Controller Bridge 通訊。在 PE 設備上，必須設定控制埠，且只有一個埠（最接近 CB 的埠）會作為 upstream port。其他控制埠可作為 upstream port 的備援，甚至可作為串聯交換器的 cascade port（例如上圖中的 Port Extender 2 與 3）。Cascade 與 upstream 埠用於傳送與接收控制及網路流量。**Extended ports** 是由 CB 設備控制的介面，通常連接到終端主機。Extended ports 只會傳送與接收網路流量。

請參閱下方各交換器型號支援的功能。

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

### Limitations

雖然控制器允許設定 port extender 介面，但部分橋接與交換功能無法使用，或無法正常運作。以下是最常見的控制器與延伸器限制。這份清單可能會隨 RouterOS 後續版本而變更。

| 功能 | 支援 |
| :-- | :-- |
| Bonding for cascade and upstream ports | + |
| Bridge VLAN filtering | + |
| Bonding for extended ports | - |
| Dot1x authenticator (server) | - |
| Ingress and egress rates | - |
| Mirroring | - |
| Port ingress VLAN filtering | - |
| Port isolation | - |
| Storm control | - |
| Switch rules (ACL) | - |
| L3HW offloading | - |
| MLAG | - |

## 快速設定 {#quick-setup}

---

在此範例中，我們將建立一個 Controlling Bridge（例如 CRS317-1G-16S+ 交換器），透過 SFP+1 介面連接到單一 Port Extender（例如 CRS326-24G-2S+ 交換器）。

首先，在 CB 設備上設定已啟用 VLAN 過濾的 bridge：

```ros
/interface/bridge
add name=bridge1 vlan-filtering=yes
```

在同一台設備上，設定連接到 PE 設備且將作為級聯埠的埠：

```ros
/interface/bridge/port-controller
set bridge=bridge1 cascade-ports=sfp-sfpplus1 switch=switch1
```

最後，在 PE 設備上，只需設定控制埠，該埠將被選為上游埠：

```ros
/interface/bridge/port-extender
set control-ports=sfp-sfpplus1 switch=switch1
```

當 PE 與 CB 設備連線後，同一 switch group 中的所有介面（控制埠除外）都會被延伸，並可在 CB 設備上進一步設定。CB 設備會套用自動 bridge 埠設定，將所有延伸埠加入單一 bridge。之後可以修改此設定。

:::warning
若要將某個埠排除在延伸範圍外（例如用於帶外管理），請另外設定 `excluded-ports` 屬性。
:::

:::warning
請勿將 `cascade-ports` 與 `control-ports` 包含在任何路由或 bridge 設定中。這些埠建議僅供 CB 與 PE 使用。
:::

## 探索與控制協定 {#discovery-and-control-protocols}

---

在擴充埠上進行訊框轉送之前，Controlling Bridge 與 Port Extender 必須先互相探索並交換必要資訊。

啟用 CB 與 PE 的設備會使用鄰居探索協定 LLDP，並搭配特定的 Port Extension TLV。這可讓 CB 與 PE 設備通告其在串接埠與控制埠上的支援能力。

:::warning
CB 與 PE 設定可以覆蓋鄰居探索設定，例如，即使串接埠未包含在鄰居探索介面清單中，LLDP 訊息仍會傳送。
:::

一旦 CB 與 PE 之間交換 LLDP 訊息，就會啟動透過 Edge Control Protocol（ECP）執行的 Control and Status Protocol（CSP）。CSP 用於 CB 與 PE 之間，以確認控制權並接收來自相關 PE 的狀態資訊。它會為擴充埠指派唯一 ID、控制資料路徑設定（例如埠 VLAN 成員資格），並傳送埠狀態資訊（例如介面統計、PoE-out 監控）。ECP 提供可靠且具順序的訊框傳遞（以 EtherType 0x8940 編碼）。

:::danger
目前的 CB 實作不支援任何容錯移轉技術。一旦 CB 設備無法使用，PE 設備將失去所有控制與資料轉送規則。
:::

## 封包流程 {#packet-flow}

---

為了更瞭解 Controlling Bridge 與 Port Extender 的底層原理，以下提供封包流程說明：

1. L2 封包在擴充埠上接收。
2. Port Extender 會使用 E-TAG 標頭（EtherType 0x893F）封裝封包，並透過上游埠往 Controller Bridge 轉送。E-TAG 封包包含與 PE 來源埠 ID 有關的資訊。PE 設備不會進行任何本機交換決策。
3. Controller Bridge 接收 E-TAG 封包，並確切知道是哪個擴充介面接收到該封包。接著 CB 會在內部解封裝封包，並依一般交換決策處理（主機學習、目的位址查詢、VLAN 過濾等）。
4. 做出交換決策後，CB 會再次使用 E-TAG 封裝原始封包，並透過串接埠傳送至 Port Extender。
   1. 對於單一目的封包（unicast），CB 會在 E-TAG 中加入 PE 目的埠 ID，並透過正確的串接埠傳送。
   2. 對於多重目的封包（broadcast、multicast 或 unknown-unicast），CB 會在 E-TAG 中加入目標群組標記與來源埠 ID，並為每個串接埠傳送一份封包副本。
5. 一旦 PE 設備在上游埠接收到 E-TAG 封包，PE 會將其解封裝，並透過擴充埠傳送原始 L2 封包。
   1. 對於單一目的封包（unicast），PE 只會將封包傳送至正確的擴充埠。
   2. 對於多重目的封包（broadcast、multicast 或 unknown-unicast），PE 會為每個擴充埠傳送一份封包副本（接收封包的來源埠除外）。

|  |  |
| :-- | :-- |
| <img decoding="async" loading="lazy" alt="CB Unicast 3" src="/assets/images/controller-bridge-and-port-extender-02-c9b2dd45ed582b2c8780f52805fd11bc.webp" width="822" height="613"/><br/> |  |

![CB Broadcast 2](/img/c463f4757394bb7b.webp) 

## Controller Bridge 設定與監控 {#controller-bridge-settings-and-monitoring}

---

本節說明 Controller Bridge 的設定與監控選項。

**子選單：** `/interface/bridge/port-controller`

| 屬性 | 說明 |
| :-- | :-- |
| **bridge** (*name;*Default: **none**) | 將延伸埠的 bridge 介面。只有在指定 `bridge` 與 `switch` 屬性時，CB 才會啟用，否則會處於停用狀態。 |
| **cascade-ports** (*interfaces;* Default: **none**) | 作為級聯埠的介面。也支援具有 802.3ad 或 balance-xor `mode` 的 bonding 介面。 |
| **switch** (*name;*Default: **none**) | 作為 CB 並確保控制與網路流量的交換器。只有在指定 `bridge` 與 `switch` 屬性時，CB 才會啟用，否則會處於停用狀態。 |

設定並連線 CB 與 PE 設備後，每個 PE 設備都會自動顯示在 device 選單中。使用 `print` 與 `monitor` 指令檢視更多詳細資料。

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

| 屬性 | 說明 |
| :-- | :-- |
| **connected-via-devs** (*name*) | 顯示從 PE 到 CB 路徑上已連線的設備。 |
| **connected-via-ports** (*name*) | 顯示從 PE 到 CB 的連線路徑。 |
| **control-ports** (*interfaces*) | PE 設備控制埠。 |
| **descr** (*name*) | PE 設備的簡短描述。 |
| **name** (*name*) | 自動指派的 PE 設備名稱。 |
| **pe-mac** (*MAC address*) | PE 設備的 MAC 位址。 |
| **status** (*active \| inactive*) | PE 設備狀態。 |

此外，可以在 port 選單監控每個 PE 設備介面。使用 `print` 與 `monitor` 指令檢視更多詳細資訊。

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

| 屬性 | 說明 |
| :-- | :-- |
| **device** (*name*) | 自動指派的 PE 設備名稱。 |
| **name** (*name*) | 自動指派的 PE 埠名稱。 |
| **pcid** (*integer*) | 自動指派的埠識別碼。 |
| **port-status** (*dev-inactive \| not-added \| ok*) | PE 埠狀態。 |
| **rate** (*bps*) | 連線的資料速率。 |
| **status** (*link-ok \| no-link \| unknown*) | PE 埠連結狀態。 |

Controller Bridge 可以在 port PoE 選單監控來自 Port Extender 的 PoE-out 相關資訊。使用 `print` 與 `monitor` 指令檢視更多詳細資訊。如需更多關於 PoE-out 的資訊，請參閱 [PoE-out 手冊](/docs/hardware/poe-out)。

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

本節說明 Port Extender 設定。

**子選單：** `/interface/bridge/port-extender`

| 屬性 | 說明 |
| :-- | :-- |
| **control-ports** (*interfaces;* Default: **none**) | 將用來連接到 CB（上游埠）或以串聯方式連接其他 PE 設備（級聯埠）的介面。也支援具有 802.3ad 或 balance-xor `mode` 的 bonding 介面。 |
| **excluded-ports** (*interfaces;* Default: **none**) | 不會被延伸的介面。 |
| **switch** (*name;*Default: **none**) | 將作為延伸器並確保控制與網路流量的交換器。只有指定此屬性時才會啟用 PE，否則 PE 會處於停用狀態。 |

## 設定範例 {#configuration-examples}

---

以下說明最常見的設定範例。為了讓 CB 與 PE 設定正常運作，必須啟用 bridge VLAN filtering，因此請先了解篩選原則：[bridge VLAN filtering](/docs/bridging-and-switching#bridge-vlan-filtering)、[bridge VLAN table](/docs/bridging-and-switching/user-guides/bridge-vlan-table)。

### 基本 CB 與 PE 設定 {#basic-cb-and-pe-configuration}

在此範例中，CRS317-1G-16S+ 設備作為 Controller Bridge，CRS328-24P-4S+ 作為 Port Extender；請參閱下方的連線架構。

![Basic CB PE Configuration](/img/0b58575d7d9204a3.webp)

首先，設定 CB 設備。您可以新增一個已啟用 VLAN filtering 的 bridge 介面來完成。此外，將任何本機介面加入同一個 bridge，這可讓流量在本機介面與延伸介面之間轉送。在此範例中，加入了 sfp-sfpplus2 介面。

```ros
/interface/bridge
add name=bridge1 vlan-filtering=yes
/interface/bridge/port
add bridge=bridge1 interface=sfp-sfpplus2
```

若要啟用 CB，請指定 bridge、switch 與至少一個 cascade 埠。請確認 cascade 埠未包含在 bridge 或路由設定中。建議這些埠僅用於 CB 與 PE。

```ros
/interface/bridge/port-controller
set bridge=bridge1 cascade-ports=sfp-sfpplus1 switch=switch1
```

若要啟用 PE，請設定 control 埠與 switch。此外，請使用 `excluded-ports` 屬性設定一或多個不應被延伸的介面（例如用於帶外管理）。在此範例中，所有 switch 埠都會被延伸。

```ros
/interface/bridge/port-extender
set control-ports=sfp-sfpplus4 switch=switch1
```

當 PE 與 CB 設備完成探索並啟動 Control and Status Protocol（CSP）後，RouterOS 會永久建立新介面，並將其加入 CB 設備上的 bridge。介面名稱由自動指派的 PE 設備名稱加上預設介面名稱組成。之後可以修改這些介面名稱。請注意，control 與 excluded 埠也會顯示在介面清單中，但它們不會包含在 bridge 中。

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

現在，CRS317-1G-16S+ 設備已使用 CRS328-24P-4S+ 設備擴充其埠，並且可以在所有已橋接的埠之間進行封包轉送。

### Trunk 與 Access 埠 {#trunk-and-access-ports}

在此範例中，將在 Controller Bridge 設備上建立未標記（access）與標記（trunk）埠設定。請參閱下方的網路圖。

![CB PE VLANs](/img/6a112aa3a790d572.webp)First, configure the CB and PE devices. The configuration is identical to the previous example. Use this configuration for the CB device.

```ros
/interface/bridge
add name=bridge1 vlan-filtering=yes
/interface/bridge/port
add bridge=bridge1 interface=sfp-sfpplus2
/interface/bridge/port-controller
set bridge=bridge1 cascade-ports=sfp-sfpplus1 switch=switch1
```

在 PE 設備上使用此設定。

```ros
/interface/bridge/port-extender
set control-ports=sfp-sfpplus4 switch=switch1
```

在 extended ports 成功建立並新增至 CB 設備的 bridge 後，即可開始設定 VLAN 相關屬性。首先，使用 `pvid` 屬性將 access 埠設定至各自的 VLAN ID。在 `/interface/bridge/port` 選單中使用 `print` 指令，以找出確切的介面名稱。

```ros
/interface/bridge/port
set [find interface=pe1-ether1] pvid=10
set [find interface=pe1-ether2] pvid=20
set [find interface=pe1-ether3] pvid=30
```

然後新增 bridge VLAN 項目，並指定 tagged、untagged 埠。請注意，有兩個 tagged 埠：名為 sfp-sfpplus2 的本地埠，以及名為 pe1-sfpplus1 的 extended port。

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=pe1-sfpplus1,sfp-sfpplus2 untagged=pe1-ether1 vlan-ids=10
add bridge=bridge1 tagged=pe1-sfpplus1,sfp-sfpplus2 untagged=pe1-ether2 vlan-ids=20
add bridge=bridge1 tagged=pe1-sfpplus1,sfp-sfpplus2 untagged=pe1-ether3 vlan-ids=30
```

此時 VLAN 已設定完成，設備應能透過這些埠進行通訊。不過，建議再進一步套用一些額外的篩選選項。在本機 bridge 埠上啟用 `ingress-filtering`，並使用 `frame-types` 設定依封包類型進行訊框篩選。

```ros
/interface/bridge/port
set [find interface=pe1-ether1] frame-types=admit-only-untagged-and-priority-tagged
set [find interface=pe1-ether2] frame-types=admit-only-untagged-and-priority-tagged
set [find interface=pe1-ether3] frame-types=admit-only-untagged-and-priority-tagged
set [find interface=pe1-sfpplus1] frame-types=admit-only-vlan-tagged
set [find interface=sfp-sfpplus2] frame-types=admit-only-vlan-tagged ingress-filtering=yes
```

:::warning
extended ports 不支援埠 ingress VLAN 篩選。
:::

### 串接多個 Port Extender 並使用 bonding 介面 {#cascading-multiple-port-extenders-and-using-bonding-interface}

在此範例中，兩個 PE 設備（CRS328-24P-4S+ 與 CRS326-24G-2S+）將新增至 CB（CRS317-1G-16S+）。為了提高上游與串接埠的吞吐量，將建立 [bonding 介面](/docs/high-availability-solutions/bonding)。請參閱下方的網路架構圖。

![Bonding Cascade](/img/79872d18d20c4e0b.webp)

CB 與 PE 的設定與第一個範例相似，主要差異在於 bonding 介面的使用。首先，設定 CB 設備：為串接埠建立 bonding 介面，建立 bridge 並新增任何所需的本機 bridge 埠，最後啟用 CB。使用下列指令：

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

接著設定 Port Extender 1 設備。此設備需要兩個 bonding 介面：第一個將作為上游埠，第二個將作為 Port Extender 2 設備的串接埠。此外，請使用 `excluded-ports` 屬性設定一或多個不應被延伸的介面（例如用於頻外管理）。在此範例中，所有交換器埠都會被延伸。

```ros
/interface/bonding
add mode=802.3ad name=bond1 slaves=sfp-sfpplus1,sfp-sfpplus2
add mode=802.3ad name=bond2 slaves=sfp-sfpplus3,sfp-sfpplus4
/interface/bridge/port-extender
set control-ports=bond1,bond2 switch=switch1
```

最後，設定 Port Extender 2 設備：建立 bonding 介面並啟用 PE。此外，必要時設定一或多個 `excluded-ports`。在此範例中，所有交換器埠都會被延伸。

```ros
/interface/bonding
add mode=802.3ad name=bond1 slaves=sfp-sfpplus1,sfp-sfpplus2
/interface/bridge/port-extender
set control-ports=bond1 switch=switch1
```

現在，CRS317-1G-16S+ 設備已將其埠延伸出額外的 48 個 Gigabit Ethernet 埠，並可在所有 bridged 埠之間進行封包轉送。

使用 device 選單中的 `monitor` 指令查看 PE 設備的連線路徑。另外，使用 port 選單中的 `print` 指令查看哪些 PE 介面作為上游與串接埠。

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

### 設定修改與移除 {#configuration-modification-and-removal}

在某些情況下，需要調整 CB 與 PE 設備設定（例如 PE 設備需要新的控制埠），或將其完全移除。若要修改 PE 設備設定，應先從 CB 設備移除所有相關的 PE 設備設定。之後才能套用新設定。

首先，若要從 CB 移除 PE 設定，請使用下列指令停用 PE：

```ros
/interface/bridge/port-extender/set switch=none control-ports="" excluded-ports=""
```

然後，在 CB 設備上，移除使用 PE 介面的相關 bridge 與其他 RouterOS 設定（例如，請參閱 `/interface/bridge/port` 與 `/interface/bridge/vlan` 選單的 `export`）。例如，若要移除特定 PE 設備的所有 bridge 埠，請使用下列指令：

```ros
/interface/bridge/port/remove [find interface~"pe1"]
```

設定移除後，即可從 CB 設備清單移除 PE。此指令也會自動從 CB 介面清單移除所有 PE 設備介面。若 CB 上仍有部分 PE 介面設定，這些設定將不再有效。請使用 `print` 指令找出 PE 設備名稱。

```ros
/interface/bridge/port-controller/device/remove [find name=pe1]
```
