---
title: "Bridge IGMP/MLD snooping"
description: "本頁說明 MikroTik RouterOS 橋接器針對 IGMP/MLD snooping 的功能，透過將串流篩選至已訂閱的埠，以有效率地轉送多播流量。內容涵蓋 IGMP/MLD 版本的設定選項、querier 偵測、多播路由器狀態，以及用於管理多播資料庫項目的監控工具。"
tags:
  - 'igmp'
  - 'mld'
  - 'sdvoe'
source: https://manual.mikrotik.com/docs/7.24/bridging-and-switching/user-guides/bridge-igmp-mld-snooping
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

---

IGMP (Internet Group Management Protocol) 與 MLD (Multicast Listener Discovery) snooping 是橋接器功能，可讓橋接器被動監聽 IGMP/MLD 網路通訊，並使用這些資訊為多點傳送流量做出智慧的轉送決策。橋接器預設會將所有多點傳送流量泛洪到每個橋接器埠，類似於廣播流量的處理方式。此預設行為對某些應用可能並不理想，例如多點傳送影片串流或 SDVoE (Software Defined Video over Ethernet) 部署。IGMP/MLD snooping 可解決此問題，方法是只將多點傳送流量轉送到已訂閱的感興趣用戶端所在的埠。請參閱下方的 IGMP/MLD 網路概念圖。

RouterOS 橋接器實作支援 IGMP 第 1、2、3 版，以及 MLD 第 1、2 版。此實作以 RFC4541 為基礎，各協定規格分別定義於 RFC1112 (IGMPv1)、RFC2236 (IGMPv2)、RFC3376 (IGMPv3)、RFC2710 (MLDv1) 與 RFC3810 (MLDv2)。

:::warning
IGMPv3 與 MLDv2 不支援指定來源多點傳送 (Source-specific multicast) 轉送。
:::

![IGMP Configuration Diagram](/img/bda205876bdd0bb4.webp)

橋接器只有在啟用 `igmp-snooping` 時才會處理 IGMP/MLD 訊息。此外，橋接器必須具有有效的 IPv6 位址，才能處理 MLD 封包。一開始，橋接器不會限制任何多點傳送流量，而是泛洪所有多點傳送封包。一旦偵測到 IGMP/MLD querier，也就是收到 IGMP/MLD 查詢訊息（來自外部多點傳送路由器，或來自本機啟用 `multicast-querier` 的橋接器介面），橋接器就會開始限制未知的 IP 多點傳送流量，並且只轉送來自 Multicast Database (MDB) 的已知多點傳送串流。IGMP 與 MLD querier 偵測各自獨立運作；偵測到 IGMP querier 不會影響 IPv6 多點傳送轉送，反之亦然。querier 偵測也不會限制非 IP 與連結區域多點傳送群組的轉送，例如 224.0.0.0/24 與 ff02::1。

:::danger
搭載 Marvell-98DX3236、Marvell-98DX224S 或 Marvell-98DX226S 交換器晶片的 CRS3xx 系列設備，在偵測到 IGMP 或 MLD querier 後，無法區分非 IP、IPv4 與 IPv6 多點傳送封包。這表示當偵測到 querier 時，交換器將停止轉送所有未知的多點傳送流量（不論協定為何）。此限制不適用於某些連結區域多點傳送位址範圍，例如 224.0.0.0/24 或 ff02::1。
:::

## 設定選項 {#configuration-options}

---

本節說明 IGMP 與 MLD snooping 的橋接器設定選項。

**子選單：** `/interface/bridge`

| 屬性 | 說明 |
| :-- | :-- |
| **igmp-snooping** (*yes \| no*；預設：**no**) | 啟用 IGMP 與 MLD snooping。 |
| **igmp-version** (*2 \| 3*；預設：**2**) | 選擇 bridge 介面作為 IGMP querier 時，產生 IGMP membership query 所使用的 IGMP 版本。此屬性只有在 `igmp-snooping` 與 `multicast-querier` 設為 `yes` 時才會生效。 |
| **last-member-interval** (*time*；預設：**1s**) | 當 bridge 連接埠上的最後一個用戶端取消訂閱 multicast 群組，且 bridge 作為主動 querier 時，bridge 會傳送群組特定的 IGMP/MLD query，以確認是否仍有其他用戶端訂閱。此設定會變更這些 query 的回應時間。若在特定期間內未收到 membership report（<code>last-member-interval</code> * <code>last-member-query-count</code>），該 multicast 群組會從 multicast database（MDB）中移除。<br/> 如果 bridge 連接埠設定了 fast-leave，multicast 群組會立即移除，而不會傳送任何 query。<br/> 此屬性只有在 <code>igmp-snooping</code> 與 <code>multicast-querier</code> 設為 <code>yes</code> 時才會生效。 |
| **last-member-query-count** (*integer: 0..4294967295*；預設：**2**) | `last-member-interval` 必須經過多少次，IGMP/MLD snooping bridge 才會停止轉送特定 multicast 串流。此屬性只有在 `igmp-snooping` 與 `multicast-querier` 設為 `yes` 時才會生效。 |
| **membership-interval** (*time*；預設：**4m20s**) | 當 bridge 連接埠未收到 IGMP/MLD membership report 時，Multicast Database（MDB）中的項目被移除前的時間。此屬性只有在 `igmp-snooping` 設為 `yes` 時才會生效。 |
| **mld-version** (*1 \| 2*；預設：**1**) | 選擇 bridge 介面作為 MLD querier 時，產生 MLD membership query 所使用的 MLD 版本。此屬性只有在 bridge 具有有效的 IPv6 位址，且 `igmp-snooping` 與 `multicast-querier` 設為 `yes` 時才會生效。 |
| **multicast-querier** (*yes \| no*；預設：**no**) | Multicast querier 會產生週期性的 IGMP/MLD general membership query，所有支援 IGMP/MLD 的設備都會以 IGMP/MLD membership report 回應，通常是由 PIM（multicast）路由器或 IGMP proxy 產生這些 query。<br/> 使用此屬性可讓啟用 IGMP/MLD snooping 的 bridge 產生 IGMP/MLD general membership query。每當 Layer2 網路中沒有主動 querier（PIM 路由器或 IGMP proxy）時，都應使用此屬性。若 Layer2 網路中沒有 multicast querier，Multicast Database（MDB）就不會更新，已學習的項目將會逾時，IGMP/MLD snooping 也無法正常運作。<br/> 只會產生未標記的 IGMP/MLD general membership query，IGMP query 會以 bridge 介面本身的 IPv4 位址作為來源位址傳送（請參閱 <code>querier-uses-bridge-address</code>），MLD query 則會以 bridge 介面的 IPv6 link-local 位址傳送。若偵測到外部 IGMP/MLD querier，bridge 就不會傳送 query（請參閱監控值 <code>igmp-querier</code> 與 <code>mld-querier</code>）。<br/> 此屬性只有在 <code>igmp-snooping</code> 設為 <code>yes</code> 時才會生效。 |
| **multicast-router** (*disabled \| permanent \| temporary-query*；預設：**temporary-query**) | Multicast router 連接埠是連接 multicast 路由器或 querier 的連接埠。未註冊的 multicast 串流與 IGMP/MLD membership report 會在該連接埠上傳送。此設定會變更 bridge 介面本身的 multicast router 狀態。此屬性可用於將 IGMP/MLD membership report 與 multicast 流量傳送至 bridge 介面，以進行進一步的 multicast 路由或 proxy。此屬性只有在 <code>igmp-snooping</code> 設為 <code>yes</code> 時才會生效。<ul><li><span className="ros-icon-success"><code>disabled</code></span> - 停用 bridge 介面上的 multicast router 狀態。不論 bridge 介面上設定為何，未註冊的 multicast 串流與 IGMP/MLD membership report 都不會傳送至 bridge 介面。</li><li><span className="ros-icon-success"><code>permanent</code></span> - 啟用 bridge 介面上的 multicast router 狀態。不論 bridge 介面上設定為何，未註冊的 multicast 串流與 IGMP/MLD membership report 都會傳送至 bridge 介面本身。</li><li><span className="ros-icon-success"><code>temporary-query</code></span> - 使用 IGMP/MLD query 自動偵測 bridge 介面上的 multicast router 狀態。</li></ul> |
| **querier-interval** (*time*；預設：**4m15s**) | 變更已偵測到的 querier 與 multicast-router 連接埠的逾時期間。此屬性只有在 `igmp-snooping` 設為 `yes` 時才會生效。 |
| **querier-uses-bridge-address** (*yes \| no*；預設：**yes**) | 啟用時，bridge IGMP querier 會使用 bridge 介面本身的 IPv4 位址作為 IGMP query 封包的來源位址，而不是預設的 0.0.0.0。某些 multicast 用戶端會將來自 0.0.0.0 的 query 視為無效而不回應，這可能導致 snooping 表項目逾時時發生 multicast 串流中斷。此屬性只有在 `igmp-snooping` 與 `multicast-querier` 設為 `yes`，且 bridge 介面已指派 IPv4 位址時才會生效。此設定僅適用於 IPv4（IGMP）。MLD query 一律使用 bridge 介面的 IPv6 link-local 位址。 |
| **query-interval** (*time*；預設：**2m5s**) | 變更 bridge 介面作為 IGMP/MLD querier 時，傳送 IGMP/MLD general membership query 的間隔。該間隔會在最後一個 startup query 送出後生效。此屬性只有在 `igmp-snooping` 與 `multicast-querier` 設為 `yes` 時才會生效。 |
| **query-response-interval** (*time*；預設：**10s**) | 當 bridge 作為 IGMP/MLD querier 時，此設定會變更 general IGMP/MLD query 的回應時間。此屬性只有在 `igmp-snooping` 與 `multicast-querier` 設為 `yes` 時才會生效。 |
| **startup-query-count** (*integer: 0..4294967295*；預設：**2**) | 指定啟用 bridge 介面或主動 querier 逾時時，必須傳送多少次 general IGMP/MLD query。此屬性只有在 `igmp-snooping` 與 `multicast-querier` 設為 `yes` 時才會生效。 |
| **startup-query-interval** (*time*；預設：**31s250ms**) | 指定 startup general IGMP/MLD query 之間的間隔。此屬性只有在 `igmp-snooping` 與 `multicast-querier` 設為 `yes` 時才會生效。 |

**子選單：** `/interface/bridge/port`

| 屬性 | 說明 |
| :-- | :-- |
| **fast-leave** (*yes \| no*；預設：**no**) | 在 bridge 連接埠上啟用 IGMP/MLD fast leave 功能。當收到 IGMP/MLD leave 訊息時，bridge 會停止將 multicast 流量轉送至 bridge 連接埠。此屬性只有在 `igmp-snooping` 設為 `yes` 時才會生效。 |
| **multicast-router** (*disabled \| permanent \| temporary-query*；預設：**temporary-query**) | Multicast router 連接埠是連接 multicast 路由器或 querier 的連接埠。未註冊的 multicast 串流與 IGMP/MLD membership report 會在該連接埠上傳送。此設定會變更 bridge 連接埠的 multicast router 狀態。此屬性可用於將 IGMP/MLD membership report 與 multicast 串流傳送至特定 bridge 連接埠，以進行進一步的 multicast 路由或 proxy。此屬性只有在 <code>igmp-snooping</code> 設為 <code>yes</code> 時才會生效。<ul><li><span className="ros-icon-success"><code>disabled</code></span> - 停用 bridge 連接埠上的 multicast router 狀態。不論連接埠上連接了什麼，未註冊的 multicast 串流與 IGMP/MLD membership report 都不會傳送至 bridge 連接埠。</li><li><span className="ros-icon-success"><code>permanent</code></span> - 啟用 bridge 連接埠上的 multicast router 狀態。不論連接埠上連接了什麼，未註冊的 multicast 與 IGMP/MLD membership report 都會傳送至 bridge 連接埠。</li><li><span className="ros-icon-success"><code>temporary-query</code></span> - 使用 IGMP/MLD query 自動偵測 bridge 連接埠上的 multicast router 狀態。</li></ul> |
| **unknown-multicast-flood** (*yes \| no*；預設：**yes**) | 變更 bridge 連接埠上的 multicast flood 選項。它只控制 egress 流量。啟用時，bridge 允許將 multicast 封包泛洪至指定的 bridge 連接埠；停用時，bridge 會限制 multicast 流量泛洪至指定的 bridge 連接埠。此設定會影響所有 multicast 流量，包括非 IP、IPv4、IPv6，以及 link-local multicast 範圍（例如 224.0.0.0/24 與 ff02::1）。<br/> 請注意，當 <code>igmp-snooping</code> 已啟用且偵測到 IGMP/MLD querier 時，bridge 會自動限制未知 IP multicast 泛洪，因此此設定對 IGMP/MLD snooping 組態並非必要。<br/> 當此設定與 <code>igmp-snooping</code> 一起使用時，bridge 連接埠上唯一允許的 multicast 流量是來自 MDB 表的已知 multicast。 |

**子選單：** `/interface/bridge/mdb`

| 屬性 | 說明 |
| :-- | :-- |
| **bridge** (*name*；預設： ) | 要指派 MDB 項目的 bridge 介面。 |
| **disabled** (*yes \| no*；預設：**no**) | 停用或啟用靜態 MDB 項目。 |
| **group** (*ipv4 \| ipv6 address*；預設： ) | IPv4 或 IPv6 multicast 位址。無法建立 link-local multicast 群組 224.0.0.0/24 與 ff02::1 的靜態項目，因為這些封包一律會在所有連接埠與 VLAN 上泛洪。 |
| **ports** (*name*；預設： ) | 要轉送 multicast 群組的 bridge 連接埠清單。 |
| **vid** (*integer: 1..4094*；預設： ) | 要建立 MDB 項目的 VLAN ID，只有在啟用 `vlan-filtering` 時適用。未指定 VLAN ID 時，該項目會以 shared-VLAN 模式運作，並動態套用至特定連接埠上所有已定義的 VLAN ID。 |

## 監控與疑難排解 {#monitoring-and-troubleshooting}

---

本節說明 IGMP/MLD snooping bridge 的監控與疑難排解選項。

若要監控已學習的 multicast database（MDB）項目，請使用 `print` 指令。

**子選單：** `/interface/bridge/mdb`

| 屬性 | 說明 |
| :-- | :-- |
| **bridge** (*read-only: *name**) | 顯示該項目所屬的 bridge 介面。 |
| **group** (*read-only:* *ipv4 \| ipv6 address*) | 顯示群播群組位址。 |
| **on-ports** (*read-only: name*) | 顯示已訂閱特定群播群組的 bridge 埠。 |
| **vid** (*read-only: integer*) | 顯示群播群組的 VLAN ID，僅在啟用 `vlan-filtering` 時適用。 |

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

若要監控 bridge 介面的目前狀態，請使用 `monitor` 指令。

**子選單：** `/interface/bridge`

| 屬性 | 說明 |
| :-- | :-- |
| **igmp-querier** (*none*\| *interface & IPv4 address*) | 顯示從偵測到的 IGMP querier 取得的 bridge 埠與來源 IP 位址。僅顯示偵測到的外部 IGMP querier，不會顯示本機 bridge IGMP querier（包括 IGMP proxy 與 PIM）。只有在啟用 `igmp-snooping` 時才會出現監控值。 |
| **mld-querier** (*none*\| *interface & IPv6 address*) | 顯示從偵測到的 MLD querier 取得的 bridge 埠與來源 IPv6 位址。僅顯示偵測到的外部 MLD querier，不會顯示本機 bridge MLD querier。只有在啟用 `igmp-snooping` 且 bridge 具有有效的 IPv6 位址時才會出現監控值。 |
| **multicast-router** (*yes \| no*) | 顯示是否在 bridge 介面上偵測到群播路由器。只有在啟用 `igmp-snooping` 時才會出現監控值。 |

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

若要監控 bridge 埠的目前狀態，請使用 `monitor` 指令。

**子選單：** `/interface/bridge/port`

| 屬性 | 說明 |
| :-- | :-- |
| **multicast-router** (*yes \| no*) | 顯示是否在該埠上偵測到群播路由器。只有在啟用 `igmp-snooping` 時才會出現監控值。 |

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

## 設定範例 {#configuration-examples}

---

以下說明最常見的設定範例。部分範例使用啟用 VLAN 過濾的 bridge，因此請先瞭解過濾原則：[bridge VLAN filtering](/docs/bridging-and-switching#bridge-vlan-filtering)、[bridge VLAN table](/docs/bridging-and-switching/user-guides/bridge-vlan-table)。

### 基本 IGMP snooping 設定 {#basic-igmp-snooping-configuration}

第一個範例只包含單一 IGMP snooping bridge、單一多播來源設備，以及幾個多播用戶端設備。請參閱下方的網路架構圖。

![IGMP Basic Setup Diagram](/img/33992ed3c8365049.webp)

首先，建立已啟用 IGMP snooping 的 bridge 介面。在此範例中，沒有作用中的 IGMP querier（沒有多播路由器或代理），因此必須在同一個 bridge 上啟用本機 IGMP querier。這可透過 `multicast-querier` 設定完成。如果 LAN 中沒有作用中的 IGMP querier，未註冊的 IP 多播將會被泛洪，且多播項目會持續從多播資料庫逾時。

```ros
/interface/bridge
add igmp-snooping=yes multicast-querier=yes name=bridge1
```

然後將必要的介面新增為 bridge 埠。

```ros
/interface/bridge/port
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=ether3
add bridge=bridge1 interface=ether4
add bridge=bridge1 interface=ether5
```

基本 IGMP snooping 設定已完成。使用「`/interface/bridge/mdb/print`」指令監控作用中的多播群組。如有需要，可以在同一個 bridge 介面上設定 IP 位址與 [DHCP server](/docs/network-management/dhcp#configuration-examples)。

### 含 VLAN 的 IGMP snooping 設定 {#igmp-snooping-configuration-with-vlans}

第二個範例增加了一些複雜度。其中有兩個 IGMP snooping 橋接器，我們需要將多播流量隔離在不同的 VLAN 上。請參閱下方的網路架構。

![IGMP VLAN Setup Diagram](/img/106ab87a1a96eb99.webp)

首先，在兩台設備上建立橋接器，並將所需的介面新增為橋接埠。若要變更橋接埠的未標記 VLAN，請使用 `pvid` 設定。Bridge1 將作為 IGMP querier。以下是 Bridge1 的設定指令：

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

以下是 Bridge2 的設定指令：

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
橋接器 IGMP querier 實作只能傳送未標記的 IGMP 查詢。若需要傳送已標記的 IGMP 查詢，或需要在多個 VLAN 中產生 IGMP 查詢，可以設定 VLAN 介面，並搭配 [IGMP Proxy](/docs/user-guides/routing-and-networking-protocols/multicast/igmp-proxy) 或 [PIM-SM](/docs/user-guides/routing-and-networking-protocols/multicast/pim-sm)。IGMP Proxy 的下游介面，以及 PIM-SM 介面，都可以作為 IGMP querier 運作。
:::

請務必為設備設定[管理存取](/docs/bridging-and-switching#management-access-configuration)。這在設定啟用 VLAN 過濾的橋接器時非常重要。在此範例中，已將具有 IP 位址的 VLAN 99 介面新增至橋接器。此 VLAN 將允許在已標記的 sfp-sfpplus1 埠上通過。以下是 Bridge1 的設定指令：

```ros
/interface/vlan
add interface=bridge1 name=MGMT vlan-id=99
/ip/address
add address=192.168.99.1/24 interface=MGMT network=192.168.99.0
/interface/bridge/vlan
add bridge=bridge1 tagged=bridge1,sfp-sfpplus1 vlan-ids=99
```

以下是 Bridge2 的設定指令：

```ros
/interface/vlan
add interface=bridge1 name=MGMT vlan-id=99
/ip/address
add address=192.168.99.2/24 interface=MGMT network=192.168.99.0
/interface/bridge/vlan
add bridge=bridge1 tagged=bridge1,sfp-sfpplus1 vlan-ids=99
```

新增橋接器 VLAN 項目，並指定已標記與未標記的埠。VLAN 99 項目已在設定管理存取時建立；現在只需新增 VLAN 10 與 VLAN 20。以下是 Bridge1 的設定指令：

```ros
/interface/bridge/vlan
add bridge=bridge1 untagged=ether2,ether3,ether4,sfp-sfpplus1 vlan-ids=10
add bridge=bridge1 tagged=sfp-sfpplus1 untagged=ether5 vlan-ids=20
```

以下是 Bridge2 的設定指令：

```ros
/interface/bridge/vlan
add bridge=bridge1 untagged=ether3,ether4,sfp-sfpplus1 vlan-ids=10
add bridge=bridge1 tagged=sfp-sfpplus1 untagged=ether5 vlan-ids=20
```

最後，啟用 VLAN filtering。以下是 Bridge1 與 Bridge2 的設定指令：

```ros
/interface/bridge/set [find name=bridge1] vlan-filtering=yes
```

此時，VLAN 與 IGMP snooping 已設定完成，設備應該可以透過埠進行通訊。不過，建議再進一步套用一些額外的篩選選項。在 bridge 埠上啟用 `ingress-filtering` 與 `frame-types`。以下是 Bridge1 的設定指令：

```ros
/interface/bridge/port
set [find interface=ether2] ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged
set [find interface=ether3] ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged
set [find interface=ether4] ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged
set [find interface=ether5] ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged
set [find interface=sfp-sfpplus1] ingress-filtering=yes
```

以下是 Bridge2 的設定指令：

```ros
/interface/bridge/port
set [find interface=ether3] ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged
set [find interface=ether4] ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged
set [find interface=ether5] ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged
set [find interface=sfp-sfpplus1] ingress-filtering=yes
```

### 靜態 MDB 項目 {#static-mdb-entries}

自 RouterOS 7.7 版起，可以為 IPv4 與 IPv6 群播群組建立靜態 MDB 項目。例如，若要在 VLAN 10 的 ether2 與 ether3 埠上，為群播群組 229.10.10.10 建立靜態 MDB 項目，請使用以下指令：

```ros
/interface/bridge/mdb
add bridge=bridge1 group=229.10.10.10 ports=ether2,ether3 vid=10
```

使用 `print` 指令驗證結果：

```ros
[admin@MikroTik] > /interface/bridge/mdb/print where group=229.10.10.10
Columns: GROUP, VID, ON-PORTS, BRIDGE
 # GROUP         VID  ON-PORTS  BRIDGE 
12 229.10.10.10   10  ether2    bridge1
                      ether3   
```

若某個 IPv6 群播群組不需要進行 snooping，且希望在所有埠與 VLAN 上泛洪，可以在所有 VLAN 與埠上建立靜態 MDB 項目，包括 bridge 介面本身。使用以下指令，為所有 VLAN 與埠建立群播群組 ff02::2 的靜態 MDB 項目（請依你的特定環境修改 `ports` 設定）：

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
