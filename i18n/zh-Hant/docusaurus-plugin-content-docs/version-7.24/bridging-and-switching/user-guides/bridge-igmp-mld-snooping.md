---
sidebar_key: "bridging-and-switching/user-guides/bridge-igmp-mld-snooping"
sidebar_position: 2
title: "網橋 IGMP/MLD 偵聽"
sidebar_label: "網橋 IGMP/MLD 偵聽"
description: "本頁介紹 MikroTik RouterOS 網橋的 IGMP/MLD snooping 功能，透過僅將組播流轉發到已訂閱埠來實現高效的組播流量轉發。內容涵蓋 IGMP/MLD 版本、查詢器檢測、組播路由器狀態的配置選項，以及用於管理組播資料庫條目的監控工具。"
tags:
  - 'igmp'
  - 'mld'
  - 'sdvoe'
source: https://manual.mikrotik.com/docs/7.24/bridging-and-switching/user-guides/bridge-igmp-mld-snooping
captured_at: '2026-11-04T11:27:26+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

---

IGMP（Internet Group Management Protocol）和 MLD（Multicast Listener Discovery）snooping 是網橋功能，使網橋能夠被動偵聽 IGMP/MLD 網路通訊，並利用此資訊為組播流量做出智慧轉發決策。預設情況下，網橋會將所有組播流量泛洪到每個網橋埠，類似於廣播流量的處理方式。對於組播影片流或 SDVoE（Software Defined Video over Ethernet）部署等某些應用，這種預設行為可能並不理想。IGMP/MLD snooping 透過僅將組播流量轉發到有感興趣用戶端訂閱的埠來解決此問題。請參見下面的 IGMP/MLD 網路概念圖。

RouterOS 網橋實現支援 IGMP 版本 1、2 和 3，以及 MLD 版本 1 和 2。此實現基於 RFC4541，各協定規範分別在 RFC1112（IGMPv1）、RFC2236（IGMPv2）、RFC3376（IGMPv3）、RFC2710（MLDv1）和 RFC3810（MLDv2）中定義。

:::warning
源特定組播轉發在 IGMPv3 和 MLDv2 中不受支援。
:::

![IGMP Configuration Diagram](/img/bda205876bdd0bb4.webp)

網橋僅在啟用 `igmp-snooping` 時處理 IGMP/MLD 訊息。此外，網橋必須具有活動的 IPv6 地址才能處理 MLD 封包。最初，網橋不限制任何組播流量，並泛洪所有組播封包。一旦檢測到 IGMP/MLD 查詢器——透過接收 IGMP/MLD 查詢訊息（來自外部組播路由器，或在啟用 `multicast-querier` 時從網橋介面本地發出）——網橋開始限制未知 IP 組播流量，並僅轉發組播資料庫（MDB）中的已知組播流。IGMP 和 MLD 查詢器檢測獨立執行；檢測到 IGMP 查詢器不會影響 IPv6 組播轉發，反之亦然。查詢器檢測也不會限制非 IP 和鏈路本地組播組的轉發，例如 224.0.0.0/24 和 ff02::1。

:::danger
配備 Marvell-98DX3236、Marvell-98DX224S 或 Marvell-98DX226S 交換晶片的 CRS3xx 系列裝置，在檢測到 IGMP 或 MLD 查詢器後，無法區分非 IP、IPv4 和 IPv6 組播封包。這意味著當檢測到查詢器時，交換器會停止轉發所有未知組播流量（無論協定如何）。此限制不適用於某些鏈路本地組播地址範圍，例如 224.0.0.0/24 或 ff02::1。
:::

## 配置選項 {#configuration-options}

---

本節介紹 IGMP 和 MLD snooping 網橋配置選項。

**子選單：** `/interface/bridge`

| 屬性 | 描述 |
| :-- | :-- |
| **igmp-snooping**（*yes \| no*；預設：**no**） | 啟用 IGMP 和 MLD snooping。 |
| **igmp-version**（*2 \| 3*；預設：**2**） | 選擇當網橋介面充當 IGMP 查詢器時將用於生成 IGMP 成員查詢的 IGMP 版本。僅當 `igmp-snooping` 和 `multicast-querier` 設定為 `yes` 時，此屬性才生效。 |
| **last-member-interval**（*time*；預設：**1s**） | 當網橋埠上的最後一個用戶端取消訂閱某個組播組，並且網橋充當活動查詢器時，網橋將傳送特定於該組的 IGMP/MLD 查詢，以確保沒有其他用戶端仍在訂閱。此設定會更改這些查詢的響應時間。如果在特定時間段（`last-member-interval` \* `last-member-query-count`）內未收到成員報告，則從組播資料庫（MDB）中移除該組播組。如果網橋埠配置了 fast-leave，則組播組會立即被移除，而不傳送任何查詢。僅當 `igmp-snooping` 和 `multicast-querier` 設定為 `yes` 時，此屬性才生效。 |
| **last-member-query-count**（*integer: 0..4294967295*；預設：**2**） | `last-member-interval` 應經過多少次後，IGMP/MLD snooping 網橋才停止轉發某個組播流。僅當 `igmp-snooping` 和 `multicast-querier` 設定為 `yes` 時，此屬性才生效。 |
| **membership-interval**（*time*；預設：**4m20s**） | 如果在網橋埠上未收到 IGMP/MLD 成員報告，則從組播資料庫（MDB）中移除條目之前的時間量。僅當 `igmp-snooping` 設定為 `yes` 時，此屬性才生效。 |
| **mld-version**（*1 \| 2*；預設：**1**） | 選擇當網橋介面充當 MLD 查詢器時將用於生成 MLD 成員查詢的 MLD 版本。僅當網橋具有活動的 IPv6 地址，且 `igmp-snooping` 和 `multicast-querier` 設定為 `yes` 時，此屬性才生效。 |
| **multicast-querier**（*yes \| no*；預設：**no**） | 組播查詢器會生成周期性 IGMP/MLD 通用成員查詢，所有支援 IGMP/MLD 的裝置都會以 IGMP/MLD 成員報告進行響應；通常由 PIM（組播）路由器或 IGMP 代理生成這些查詢。透過使用此屬性，可以使啟用了 IGMP/MLD snooping 的網橋生成 IGMP/MLD 通用成員查詢。當二層網路中沒有活動查詢器（PIM 路由器或 IGMP 代理）時，應使用此屬性。如果二層網路中沒有組播查詢器，則組播資料庫（MDB）不會更新，已學習的條目將超時，並且 IGMP/MLD snooping 將無法正常工作。僅生成未標記的 IGMP/MLD 通用成員查詢；IGMP 查詢使用網橋介面自身的 IPv4 地址作為源地址傳送（請參閱 `querier-uses-bridge-address`），MLD 查詢使用網橋介面的 IPv6 鏈路本地地址傳送。如果檢測到外部 IGMP/MLD 查詢器，則網橋不會發送查詢（請參閱監控值 `igmp-querier` 和 `mld-querier`）。僅當 `igmp-snooping` 設定為 `yes` 時，此屬性才生效。 |
| **multicast-router**（*disabled \| permanent \| temporary-query*；預設：**temporary-query**） | 組播路由器埠是連線組播路由器或查詢器的埠。在該埠上，將傳送未註冊的組播流和 IGMP/MLD 成員報告。此設定會更改網橋介面本身的組播路由器狀態。此屬性可用於將 IGMP/MLD 成員報告和組播流量傳送到網橋介面，以便進一步進行組播路由或代理。僅當 `igmp-snooping` 設定為 `yes` 時，此屬性才生效。<span className="ros-icon-success"><code>disabled</code></span> - 停用網橋介面上的組播路由器狀態。無論網橋介面上配置了什麼，未註冊的組播流和 IGMP/MLD 成員報告都不會發送到網橋介面。<span className="ros-icon-success"><code>permanent</code></span> - 啟用網橋介面上的組播路由器狀態。無論網橋介面上配置了什麼，未註冊的組播流和 IGMP/MLD 成員報告都會發送到網橋介面本身。<span className="ros-icon-success"><code>temporary-query</code></span> - 使用 IGMP/MLD 查詢自動檢測網橋介面上的組播路由器狀態。 |
| **querier-interval**（*time*；預設：**4m15s**） | 更改檢測到的查詢器和組播路由器埠的超時時間。僅當 `igmp-snooping` 設定為 `yes` 時，此屬性才生效。 |
| **querier-uses-bridge-address**（*yes \| no*；預設：**yes**） | 啟用後，網橋 IGMP 查詢器使用網橋介面自身的 IPv4 地址作為 IGMP 查詢封包的源地址，而不是預設的 0.0.0.0。某些組播用戶端認為來自 0.0.0.0 的查詢無效而不響應，這可能導致 snooping 表條目超時時組播流中斷。僅當 `igmp-snooping` 和 `multicast-querier` 設定為 `yes` 且網橋介面分配了 IPv4 地址時，此屬性才生效。此設定僅適用於 IPv4（IGMP）。MLD 查詢始終使用網橋介面的 IPv6 鏈路本地地址。 |
| **query-interval**（*time*；預設：**2m5s**） | 更改當網橋介面充當 IGMP/MLD 查詢器時傳送 IGMP/MLD 通用成員查詢的間隔。該間隔在傳送最後一個啟動查詢後生效。僅當 `igmp-snooping` 和 `multicast-querier` 設定為 `yes` 時，此屬性才生效。 |
| **query-response-interval**（*time*；預設：**10s**） | 當網橋充當 IGMP/MLD 查詢器時，此設定會更改通用 IGMP/MLD 查詢的響應時間。僅當 `igmp-snooping` 和 `multicast-querier` 設定為 `yes` 時，此屬性才生效。 |
| **startup-query-count**（*integer: 0..4294967295*；預設：**2**） | 指定當啟用網橋介面或活動查詢器超時時，必須傳送通用 IGMP/MLD 查詢的次數。僅當 `igmp-snooping` 和 `multicast-querier` 設定為 `yes` 時，此屬性才生效。 |
| **startup-query-interval**（*time*；預設：**31s250ms**） | 指定啟動通用 IGMP/MLD 查詢之間的間隔。僅當 `igmp-snooping` 和 `multicast-querier` 設定為 `yes` 時，此屬性才生效。 |

**子選單：** `/interface/bridge/port`

| 屬性 | 描述 |
| :-- | :-- |
| **fast-leave**（*yes \| no*；預設：**no**） | 在網橋埠上啟用 IGMP/MLD fast leave 功能。當收到 IGMP/MLD 離開訊息時，網橋將停止向該網橋埠轉發組播流量。僅當 `igmp-snooping` 設定為 `yes` 時，此屬性才生效。 |
| **multicast-router**（*disabled \| permanent \| temporary-query*；預設：**temporary-query**） | 組播路由器埠是連線組播路由器或查詢器的埠。在該埠上，將傳送未註冊的組播流和 IGMP/MLD 成員報告。此設定會更改網橋埠的組播路由器狀態。此屬性可用於將 IGMP/MLD 成員報告和組播流傳送到某些網橋埠，以便進一步進行組播路由或代理。僅當 `igmp-snooping` 設定為 `yes` 時，此屬性才生效。<span className="ros-icon-success"><code>disabled</code></span> - 停用網橋埠上的組播路由器狀態。無論連線到該埠的是什麼，未註冊的組播流和 IGMP/MLD 成員報告都不會發送到該網橋埠。<span className="ros-icon-success"><code>permanent</code></span> - 啟用網橋埠上的組播路由器狀態。無論連線到該埠的是什麼，未註冊的組播和 IGMP/MLD 成員報告都會發送到該網橋埠。<span className="ros-icon-success"><code>temporary-query</code></span> - 使用 IGMP/MLD 查詢自動檢測網橋埠上的組播路由器狀態。 |
| **unknown-multicast-flood**（*yes \| no*；預設：**yes**） | 更改網橋埠上的組播泛洪選項。它僅控制出方向流量。啟用時，網橋允許將組播封包泛洪到指定的網橋埠；停用時，網橋限制組播流量泛洪到指定的網橋埠。此設定影響所有組播流量。這包括非 IP、IPv4、IPv6 以及鏈路本地組播範圍（例如 224.0.0.0/24 和 ff02::1）。請注意，當啟用 `igmp-snooping` 並檢測到 IGMP/MLD 查詢器時，網橋會自動限制未知 IP 組播泛洪，因此對於 IGMP/MLD snooping 設定來說，此設定不是必需的。當將此設定與 `igmp-snooping` 一起使用時，網橋埠上唯一允許的組播流量是來自 MDB 表的已知組播。 |

**子選單：** `/interface/bridge/mdb`

| 屬性 | 描述 |
| :-- | :-- |
| **bridge**（*name*；預設：） | MDB 條目將分配到的網橋介面。 |
| **disabled**（*yes \| no*；預設：**no**） | 停用或啟用靜態 MDB 條目。 |
| **group**（*ipv4 \| ipv6 address*；預設：） | IPv4 或 IPv6 組播地址。無法為鏈路本地組播組 224.0.0.0/24 和 ff02::1 建立靜態條目，因為這些封包始終會在所有埠和 VLAN 上泛洪。 |
| **ports**（*name*；預設：） | 組播組將轉發到的網橋埠列表。 |
| **vid**（*integer: 1..4094*；預設：） | 將在其上建立 MDB 條目的 VLAN ID，僅在啟用 `vlan-filtering` 時適用。未指定 VLAN ID 時，該條目將在共享 VLAN 模式下工作，並動態應用於特定埠的所有已定義 VLAN ID。 |

## 監控和故障排除 {#monitoring-and-troubleshooting}

---

本節介紹 IGMP/MLD snooping 網橋監控和故障排除選項。

要監控已學習的組播資料庫（MDB）條目，請使用 `print` 命令。

**子選單：** `/interface/bridge/mdb`

| 屬性 | 描述 |
| :-- | :-- |
| **bridge**（*只讀：* *name*） | 顯示該條目所屬的網橋介面。 |
| **group**（*只讀：* *ipv4 \| ipv6 address*） | 顯示組播組地址。 |
| **on-ports**（*只讀：* *name*） | 顯示訂閱了某個組播組的網橋埠。 |
| **vid**（*只讀：* *integer*） | 顯示該組播組的 VLAN ID，僅在啟用 `vlan-filtering` 時適用。 |

```ros
[admin@MikroTik] /interface/bridge/mdb/print 
Flags: D - DYNAMIC
Columns: GROUP, VID, ON-PORTS, BRIDGE
 #   GROUP              VID  ON-PORTS  BRIDGE 
 0 D ff02::2              1  bridge1   bridge1
 1 D ff02::6a             1  bridge1   bridge1
 2 D ff02::1:ff00:0       1  bridge1   bridge1
 3 D ff02::1:ff01:6a43    1  bridge1   bridge1
 4 D 229.1.1.1           10  ether2    bridge1
 5 D 229.2.2.2           10  ether3    bridge1
                             ether2           
 6 D ff02::2             10  ether5    bridge1
                             ether3           
                             ether2           
                             ether4            
```

要監控橋接介面的當前狀態，請使用 `monitor` 命令。

**子選單：** `/interface/bridge`

| 屬性 | 描述 |
| :-- | :-- |
| **igmp-querier**（*none*\| *介面和 IPv4 地址*） | 顯示檢測到的 IGMP 查詢器的網橋埠和源 IP 地址。僅顯示檢測到的外部 IGMP 查詢器，不會顯示本地網橋 IGMP 查詢器（包括 IGMP 代理和 PIM）。僅當啟用 `igmp-snooping` 時，才會顯示該監控值。 |
| **mld-querier**（*none*\| *介面和 IPv6 地址*） | 顯示檢測到的 MLD 查詢器的網橋埠和源 IPv6 地址。僅顯示檢測到的外部 MLD 查詢器，不會顯示本地網橋 MLD 查詢器。僅當啟用 `igmp-snooping` 且網橋具有活動的 IPv6 地址時，才會顯示該監控值。 |
| **multicast-router**（*yes \| no*） | 顯示是否在網橋介面上檢測到組播路由器。僅當啟用 `igmp-snooping` 時，才會顯示該監控值。 |

```ros
[admin@MikroTik] /interface/bridge/monitor bridge1
                  state: enabled
    current-mac-address: 64:D1:54:C7:3A:59
            root-bridge: yes
         root-bridge-id: 0x8000.64:D1:54:C7:3A:59
         root-path-cost: 0
              root-port: none
             port-count: 3
  designated-port-count: 3
           fast-forward: no
       multicast-router: no
           igmp-querier: ether2 192.168.10.10
            mld-querier: ether2 fe80::e68d:8cff:fe39:3824
```

要監控橋接埠的當前狀態，請使用 `monitor` 命令。

**子選單：** `/interface/bridge/port`

| 屬性 | 描述 |
| :-- | :-- |
| **multicast-router**（*yes \| no*） | 顯示是否在埠上檢測到組播路由器。僅當啟用 `igmp-snooping` 時，才會顯示該監控值。 |

```ros
[admin@MikroTik] > /interface/bridge/port/monitor [find]
              interface: ether2          ether3          ether4
                 status: in-bridge       in-bridge       in-bridge
            port-number: 1               2               3
                   role: designated-port designated-port designated-port
              edge-port: no              yes             yes
    edge-port-discovery: yes             yes             yes
    point-to-point-port: yes             yes             yes
           external-fdb: no              no              no
           sending-rstp: yes             yes             yes
               learning: yes             yes             yes
             forwarding: yes             yes             yes
       multicast-router: yes             no              no
       hw-offload-group: switch1         switch1         switch1
```

## 配置示例 {#configuration-examples}

---

下面介紹最常見的配置示例。部分示例使用帶有 VLAN 過濾的網橋，因此請務必先了解過濾原理 - [網橋 VLAN 過濾](../index.md#bridge-vlan-filtering)、[網橋 VLAN 表](./bridge-vlan-table.md)。

### 基本 IGMP snooping 配置 {#basic-igmp-snooping-configuration}

第一個示例僅包含一個 IGMP snooping 網橋、一個組播源裝置和幾個組播用戶端裝置。請參見下面的網路方案。

![IGMP Basic Setup Diagram](/img/33992ed3c8365049.webp)

首先，建立一個啟用了 IGMP snooping 的網橋介面。在此示例中，沒有活動的 IGMP 查詢器（沒有組播路由器或代理），因此必須在同一網橋上啟用本地 IGMP 查詢器。這可以透過 `multicast-querier` 設定來完成。如果 LAN 中沒有活動的 IGMP 查詢器，未註冊的 IP 組播將被泛洪，並且組播條目將始終從組播資料庫中超時。

```ros
/interface/bridge
add igmp-snooping=yes multicast-querier=yes name=bridge1
```

然後新增必要的介面作為網橋埠。

```ros
/interface/bridge/port
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=ether3
add bridge=bridge1 interface=ether4
add bridge=bridge1 interface=ether5
```

基本 IGMP snooping 配置已完成。使用 "`/interface/bridge/mdb/print"` 命令監控活動的組播組。如有必要，可以在同一網橋介面上配置 IP 地址和 [DHCP 伺服器](../../network-management/dhcp.md#configuration-examples)。

### 帶 VLAN 的 IGMP snooping 配置 {#igmp-snooping-configuration-with-vlans}

第二個示例增加了一些複雜性。有兩個 IGMP snooping 網橋，我們需要在不同的 VLAN 上隔離組播流量。請參見下面的網路方案。

![IGMP VLAN Setup Diagram](/img/106ab87a1a96eb99.webp)

首先，在兩臺裝置上建立網橋，並將需要的介面新增為網橋埠。要更改網橋埠的未標記 VLAN，請使用 `pvid` 設定。Bridge1 將充當 IGMP 查詢器。以下是 Bridge1 的配置命令：

```ros
/interface/bridge
add igmp-snooping=yes multicast-querier=yes name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether2 pvid=10
add bridge=bridge1 interface=ether3 pvid=10
add bridge=bridge1 interface=ether4 pvid=10
add bridge=bridge1 interface=ether5 pvid=20
add bridge=bridge1 interface=sfp-sfpplus1 pvid=10
```

Bridge2 的配置如下：

```ros
/interface/bridge
add igmp-snooping=yes name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether3 pvid=10
add bridge=bridge1 interface=ether4 pvid=10
add bridge=bridge1 interface=ether5 pvid=20
add bridge=bridge1 interface=sfp-sfpplus1 pvid=10
```

:::warning
網橋 IGMP 查詢器實現只能傳送未標記的 IGMP 查詢。如果需要傳送標記的 IGMP 查詢，或需要在多個 VLAN 中生成 IGMP 查詢，可以結合 [IGMP 代理](../../user-guides/routing-and-networking-protocols/multicast/igmp-proxy.md) 或 [PIM-SM](../../user-guides/routing-and-networking-protocols/multicast/pim-sm.md) 配置 VLAN 介面。IGMP Proxy 的下游介面以及 PIM-SM 介面可以充當 IGMP 查詢器。
:::

請確保為裝置配置[管理訪問](../index.md#management-access-configuration)。在配置帶有 VLAN 過濾的網橋時，這一點至關重要。在此示例中，將一個帶有 IP 地址的 VLAN 99 介面新增到網橋。該 VLAN 將在標記的 sfp-sfpplus1 埠上允許。以下是 Bridge1 的配置命令：

```ros
/interface/vlan
add interface=bridge1 name=MGMT vlan-id=99
/ip/address
add address=192.168.99.1/24 interface=MGMT network=192.168.99.0
/interface/bridge/vlan
add bridge=bridge1 tagged=bridge1,sfp-sfpplus1 vlan-ids=99
```

Bridge2 的配置如下：

```ros
/interface/vlan
add interface=bridge1 name=MGMT vlan-id=99
/ip/address
add address=192.168.99.2/24 interface=MGMT network=192.168.99.0
/interface/bridge/vlan
add bridge=bridge1 tagged=bridge1,sfp-sfpplus1 vlan-ids=99
```

新增網橋 VLAN 條目並指定標記和未標記埠。VLAN 99 條目已在配置管理訪問時建立；現在只應新增 VLAN 10 和 VLAN 20。以下是 Bridge1 的配置命令：

```ros
/interface/bridge/vlan
add bridge=bridge1 untagged=ether2,ether3,ether4,sfp-sfpplus1 vlan-ids=10
add bridge=bridge1 tagged=sfp-sfpplus1 untagged=ether5 vlan-ids=20
```

Bridge2 的配置如下：

```ros
/interface/bridge/vlan
add bridge=bridge1 untagged=ether3,ether4,sfp-sfpplus1 vlan-ids=10
add bridge=bridge1 tagged=sfp-sfpplus1 untagged=ether5 vlan-ids=20
```

最後，啟用 VLAN 過濾。以下是 Bridge1 和 Bridge2 的配置命令：

```ros
/interface/bridge/set [find name=bridge1] vlan-filtering=yes
```

此時，VLAN 和 IGMP snooping 已配置完成，裝置應能夠透過埠通訊。但是，建議更進一步並應用一些額外的過濾選項。在網橋埠上啟用 `ingress-filtering` 和 `frame-types`。以下是 Bridge1 的配置命令：

```ros
/interface/bridge/port
set [find interface=ether2] ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged
set [find interface=ether3] ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged
set [find interface=ether4] ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged
set [find interface=ether5] ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged
set [find interface=sfp-sfpplus1] ingress-filtering=yes
```

Bridge2 的配置如下：

```ros
/interface/bridge/port
set [find interface=ether3] ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged
set [find interface=ether4] ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged
set [find interface=ether5] ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged
set [find interface=sfp-sfpplus1] ingress-filtering=yes
```

### 靜態 MDB 條目 {#static-mdb-entries}

從 RouterOS 7.7 版本開始，可以為 IPv4 和 IPv6 組播組建立靜態 MDB 條目。例如，要在 VLAN 10 上的埠 ether2 和 ether3 上為組播組 229.10.10.10 建立靜態 MDB 條目，請使用以下命令：

```ros
/interface/bridge/mdb
add bridge=bridge1 group=229.10.10.10 ports=ether2,ether3 vid=10
```

使用 `print` 命令驗證結果：

```ros
[admin@MikroTik] > /interface/bridge/mdb/print where group=229.10.10.10
Columns: GROUP, VID, ON-PORTS, BRIDGE
 # GROUP         VID  ON-PORTS  BRIDGE 
12 229.10.10.10   10  ether2    bridge1
                      ether3   
```

如果某個 IPv6 組播組不需要被 snooping，並且希望在所有埠和 VLAN 上泛洪，則可以在所有 VLAN 和埠（包括網橋介面本身）上建立靜態 MDB 條目。使用以下命令為所有 VLAN 和埠上的組播組 ff02::2 建立靜態 MDB 條目（根據你的具體設定修改 `ports` 設定）：

```ros
/interface/bridge/mdb
add bridge=bridge1 group=ff02::2 ports=bridge1,ether2,ether3,ether4,ether5

[admin@MikroTik] > /interface/bridge/mdb/print where group=ff02::2
Flags: D - DYNAMIC
Columns: GROUP, VID, ON-PORTS, BRIDGE
 #   GROUP    VID  ON-PORTS  BRIDGE 
 0   ff02::2                 bridge1
15 D ff02::2    1  bridge1   bridge1
16 D ff02::2   10  bridge1   bridge1
                   ether2           
                   ether3           
                   ether4           
                   ether5           
17 D ff02::2   20  bridge1   bridge1
                   ether2           
                   ether3           
18 D ff02::2   30  bridge1   bridge1
                   ether2           
                   ether3     
```
