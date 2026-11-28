---
title: "VXLAN"
description: "本頁說明 MikroTik RouterOS 的 VXLAN 實作，涵蓋其用於擴充 VLAN ID 的目的、VXLAN 介面與 VTEP 的設定選項，以及轉送表監控。文中詳細說明 MTU、VNI、ARP 處理，以及透過 UDP 建立 Layer 2 覆蓋網路時的群播群組管理等設定。"
tags:
  - 'vxlan'
source: https://manual.mikrotik.com/docs/7.24/bridging-and-switching/vxlan
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

---

Virtual eXtensible Local Area Network（VXLAN）是一種隧道協定，用於解決 IEEE 802.1Q 中 VLAN ID 數量有限（4096）的問題，並由 IETF RFC 7348 描述。使用 VXLAN 時，識別碼大小會擴充為 24 位元（16777216）。它會在 Layer 3 網路上建立 Layer 2 覆疊架構，且協定會透過 UDP 執行。RouterOS VXLAN 介面支援 IPv4 或 IPv6（自 7.6 版起），但不支援雙堆疊。

:::info
VXLAN 對 IPv4 會產生 50 位元組的額外負擔，對 IPv6 則會產生 70 位元組的額外負擔。設定 VXLAN 時，建議確認封裝後的 Ethernet 訊框大小不會超過底層網路的 MTU，方法是據此設定 MTU，或限制 Ethernet 訊框的大小。
:::

只有位於同一 VXLAN 區段內的設備才能彼此通訊。每個 VXLAN 區段都是透過 24 位元的區段 ID 識別，稱為 VXLAN Network Identifier（VNI）。與大多數隧道不同，VXLAN 是 1 對 N 的網路，而不只是點對點。終止 VXLAN 隧道的 VXLAN 端點稱為 VXLAN tunnel endpoints（VTEPs）。RouterOS 僅支援靜態設定的遠端 VTEPs。當需要透過 VXLAN 傳送單播流量時，設備可以類似學習橋接器的方式，動態學習另一端點的 IP 位址，並只將流量轉送至必要的 VTEP。對於需要泛洪（廣播、未知單播與多播）至同一區段中所有 VTEPs 的流量，VXLAN 可以使用多播，或使用具前端複製的單播，為每個遠端 VTEP 傳送一份複本。

## 設定選項 {#configuration-options}

---

本節說明 VXLAN 介面與 VTEP 設定選項。

**子選單：** `/interface/vxlan`

| 屬性 | 說明 |
| :-- | :-- |
| **allow-fast-path**（*yes \| no*；預設：**yes**） | 是否允許 [Fast Path](/docs/firewall-and-quality-of-service/packet-flow-in-routeros#fast-path) 處理。透過 VXLAN 的片段化與泛洪封包會經由慢速路徑重新導向。對於使用 VRF 的 VXLAN 介面，Fast Path 會停用。此設定自 RouterOS 7.8 版起可用。 |
| **arp**（*disabled \| enabled \| local-proxy-arp \| proxy-arp \| reply-only*；預設：**enabled**） | Address Resolution Protocol 設定<ul><li><span className="ros-icon-success"><code>disabled</code></span> - 介面不會使用 ARP</li><li><span className="ros-icon-success"><code>enabled</code></span> - 介面會使用 ARP</li><li><span className="ros-icon-success"><code>local-proxy-arp</code></span> - 路由器會在介面上執行 proxy ARP，並將回覆傳送至同一介面</li><li><span className="ros-icon-success"><code>proxy-arp</code></span> - 路由器會在介面上執行 proxy ARP，並將回覆傳送至其他介面</li><li><span className="ros-icon-success"><code>reply-only</code></span> - 介面只會回覆來自符合 IP 位址／MAC 位址組合的要求，這些組合必須在 IP/ARP 表中輸入為靜態項目。IP/ARP 表中不會自動儲存動態項目。因此，若要成功通訊，必須已存在有效的靜態項目。</li></ul> |
| **arp-timeout**（*auto \| integer*；預設：**auto**） | 在沒有從 IP 收到封包後，ARP 記錄會在 ARP 表中保留多久。值 `auto` 等於 IP/Settings 中的 `arp-timeout` 值，預設為 30 秒。 |
| **bridge**（*name*；預設： ） | 要將 VXLAN 介面新增為從屬埠的 [bridge](/docs/user-guides/routing-and-networking-protocols/unicast/bgp) 介面名稱。 |
| **bridge-pvid**（*integer 1..4094;*；預設：**1**） | 用於指派動態橋接埠的 PVID 參數。只有在 bridge vlan-filtering 設為 yes 時，此屬性才會生效。 |
| **checksum**（*yes \| no*；預設：**no**） | 此設定控制是否在傳送的外部 VXLAN 封包中計算 UDP 檢查碼：<br/><ul><li><span className="ros-background-accent-green-bolder"><code>no</code></span> – 傳送的外部封包中，UDP 檢查碼會設為零。這也允許透過 IPv6 接收 UDP 檢查碼為零的 VXLAN 封包。</li><li><span className="ros-background-accent-green-bolder"><code>yes</code></span> - 會在傳送的外部封包中計算 UDP 檢查碼。</li></ul> 如果使用硬體卸載進行封包傳送，則會忽略此設定，且行為預設為傳送 UDP 檢查碼為零的封包。 |
| **comment**（*string*；預設： ） | 介面的簡短描述。 |
| **disabled**（*yes \| no*；預設：**no**） | 變更介面是否停用。 |
| **dont-fragment**（*auto \| disabled \| enabled \| inherit*；預設：**auto**） | Don't Fragment（DF）旗標控制封包在透過網路傳送前，是否可以分割成較小的封包（稱為片段）。設定 VXLAN 時，此設定會決定外部 IPv4 標頭中 DF 旗標的有無，並可在封裝封包超過傳出介面 MTU 時控制封包片段化。此設定有三個選項：<br/><ul><li><span className="ros-icon-success"><code>auto</code></span> - 如果設備支援 VXLAN 卸載，dont-fragment 模式會以 <span className="ros-icon-success"><code>enabled</code></span> 運作。如果不支援 VXLAN 卸載，則會使用 <span className="ros-background-accent-green-bolder"><code>inherit</code></span> 模式。</li><li><span className="ros-icon-success"><code>disabled</code></span> - 外部 IPv4 標頭中不會設定 DF 旗標，這表示若封包太大而無法透過傳出介面傳送，就可以進行片段化。這也允許 VXLAN 使用 IPv6 underlay 時進行封包片段化。在相容設備上會停用硬體卸載。</li><li><span className="ros-icon-success"><code>enabled</code></span> - 外部 IPv4 標頭中一律設定 DF 旗標，這表示封包不會被片段化，且若超過傳出介面的 MTU，就會被捨棄。這也可避免 VXLAN 使用 IPv6 underlay 時發生封包片段化。</li><li><span className="ros-background-accent-green-bolder"><code>inherit</code></span> - 外部 IPv4 標頭上的 DF 旗標會依據內部 IPv4 DF 旗標。如果內部 IPv4 標頭已設定 DF 旗標，外部 IPv4 標頭也會設定該旗標。如果封包超過傳出介面的 MTU 且已設定 DF，封包就會被捨棄。如果內部封包不是 IP，外部 IPv4 標頭就不會設定 DF 旗標，且封包可以片段化。如果內部封包是 IPv6，外部 IPv4 標頭一律會設定 DF 旗標，且封包無法片段化。請注意，當 VXLAN 使用 IPv6 underlay 時，此設定沒有任何作用，並會被視為與 <span className="ros-icon-success"><code>disabled</code></span> 相同。</li></ul> 此設定自 RouterOS 7.8 版起可用。 |
| **group**（*IPv4 \| IPv6*；預設： ） | 指定時，可以使用多播群組位址在 VTEPs 之間轉送廣播、未知單播與多播流量。此屬性需要指定 `interface` 設定。介面會使用 IGMP 或 MLD 加入指定的多播群組，請務必新增必要的 PIM 與 IGMP/MLD 設定。設定此屬性時，`vteps-ip-version` 會自動更新為所使用的多播 IP 版本。在相容設備上會停用硬體卸載。 |
| **hw**（*yes \| no*；預設：**yes**） | 允許停用硬體卸載，僅適用於支援 VXLAN 卸載的設備。 |
| **interface**（*name*；預設： ） | 用於多播轉送的介面名稱。此屬性需要指定 `group` 設定。在相容設備上會停用硬體卸載。 |
| **learning**（*yes \| no*；預設：**yes**） | 此設定控制是否從接收到的封包動態學習內部來源 MAC 位址與遠端 VTEP IP/IPv6 位址。 |
| **local-address**（*IPv4 \| IPv6*；預設： ） | 指定 VXLAN 介面的本機來源位址。若未設定，則會選取傳出介面的其中一個 IP 位址作為 VXLAN 封包的來源位址。設定此屬性時，`vteps-ip-version` 會自動更新為所使用的本機 IP 版本。此設定自 RouterOS 7.7 版起可用。 |
| **mac-address**（*MAC*；預設： ） | 介面的靜態 MAC 位址。若未指定，則會指派隨機產生的 MAC 位址。 |
| **max-fdb-size**（*integer: 1*..65535**；預設：**4096**） | 限制 VXLAN 可在轉送資料庫（FDB）中儲存的 MAC 位址數量上限。 |
| **mtu**（*integer*；預設：**1500**） | 對於最大傳輸單元，VXLAN 介面預設會將 MTU 設為 1500。`l2mtu` 會根據關聯的 `interface` 自動設定（扣除 VXLAN 標頭對應的 50 位元組）。若未指定介面，則會使用 `l2mtu` 值 65535。無法變更 `l2mtu`。 |
| **name**（*text*；預設：**vxlan1**） | 介面名稱。 |
| **port**（*integer: 1*..65535**；預設：**4789**） | 用於監聽及傳送封包至遠端 VTEPs 的 UDP 埠號。 |
| **rem-csum**（*both \| none \| rx \| tx*；預設：**none**） | 變更 VXLAN 介面的 Remote Checksum Offload（RCO）設定。RCO 是一種省略封裝資料報內部檢查碼的技術，讓外部檢查碼可由網路驅動程式卸載。不過，這確實會涉及封裝協定的變更，接收端也必須支援。因此，此功能預設停用，並提供此設定以確保與依賴此功能的系統相容。<br/> RCO 的詳細資料請參閱下列 Internet-Drafts：<br/> Remote checksum offload for VXLAN, draft-herbert-vxlan-rco-00. Remote checksum offload for encapsulation, draft-herbert-remotecsumoffload-00. <br/> 如果使用<a href="/docs/bridging-and-switching/vxlan#hardware-offloaded-vxlan">硬體卸載</a>，則會忽略此設定，且行為預設為 none。 |
| **ttl**（*auto \| integer: 0*..255**；預設：**auto**） | 指定傳出封包要使用的 TTL 值。依預設，使用 `auto` 選項時，TTL 會設為 64。不過，如果 VXLAN 使用多播 underlay 網路，預設 TTL 會設為 1。如果多播網路涉及路由，您需要將 TTL 提高為較大的值。 |
| **vni**（*integer: 1..16777215*；預設： ） | VXLAN Network Identifier（VNI）。 |
| **vtep-vrf**（*name*；預設：**main**） | 設定 VTEPs 監聽及建立連線所在 VXLAN 介面的 VRF。使用 `interface` 與多播 `group` 設定時，不支援 VRF。相同的 UDP `port` 無法同時用於多個路由表。使用未設為「main」的 VRF 時，相容設備上的硬體卸載會停用。此設定自 RouterOS 7.7 版起可用。 |
| **vteps-ip-version**（*ipv4 \| ipv6*；預設：**ipv4**） | 用於靜態設定 VTEPs 的 IP 協定版本。RouterOS VXLAN 介面不支援雙堆疊，任何使用相反 IP 版本的遠端 VTEPs 都會被忽略。設定多播 `group` 或 `local-address` 屬性時，`vteps-ip-version` 會自動更新為所使用的 IP 版本。使用 IPv6 會在相容設備上停用硬體卸載。此設定自 RouterOS 7.6 版起可用。 |

**子選單：** `/interface/vxlan/vteps`

| 屬性 | 說明 |
| :-- | :-- |
| **comment** (*string*; Default: ) | 已設定 VTEP 的簡短說明。 |
| **interface** (*name*; Default: ) | VXLAN 介面的名稱。 |
| **remote-ip** (*IPv4 \| IPv6*; Default: ) | 定義 VTEP 端點的 IPv4 或 IPv6 位址，當 VXLAN 介面需要傳送 BUM（broadcast、unknown-unicast、multicast）流量時會使用。此項目不用於存取控制。 |

## 轉送表 {#forwarding-table}

---

自 RouterOS 7.9 版起，可以監控從遠端 VTEP 學習到的 MAC 位址。

**子選單：** `/interface/vxlan/fdb`

| 屬性 | 說明 |
| :-- | :-- |
| **interface** (*read-only: *name**) | VXLAN 介面的名稱。 |
| **mac-address** (*read-only: MAC address*) | MAC 位址。 |
| **remote-ip** (*read-only: IPv4 \| IPv6 address*) | 遠端 VTEP 的 IPv4 或 IPv6 目的地位址。 |

```ros
[admin@MikroTik] > /interface/vxlan/fdb/print          
 0 remote-ip=2001::2 mac-address=56:FF:AA:1A:72:33 interface=vxlan1 

 1 remote-ip=2002::2 mac-address=AE:EC:C4:12:8B:B9 interface=vxlan1 

 2 remote-ip=192.168.10.20 mac-address=FE:AF:58:31:A7:B6 interface=vxlan2
```

## 設定範例 {#configuration-example}

---

此設定範例會在兩個靜態設定的 VTEP 端點之間建立單一 VXLAN 隧道。

首先，在兩台路由器上建立 VXLAN 介面。

```ros
/interface/vxlan
add name=vxlan1 port=4789 vni=10
```

接著在兩台路由器上設定 VTEP，並使用各自的 IPv4 目的地位址。兩台設備都應有通往目的地位址的有效路由。

```ros
# Router1
/interface/vxlan/vteps
add interface=vxlan1 remote-ip=192.168.10.10

# Router2
/interface/vxlan/vteps
add interface=vxlan1 remote-ip=192.168.20.20
```

設定已完成。可以將 VXLAN 介面加入包含其他 Ethernet 介面的 bridge。

## 硬體卸載 VXLAN {#hardware-offloaded-vxlan}

---

從 RouterOS 7.18 版開始，引進了硬體卸載 VXLAN 的初始支援。這使得卸載的 VXLAN 資料平面成為可能，支援封裝與解封裝，並允許在啟用 vlan-filtering 的 bridge 中進行靜態一對一 VLAN 對 VXLAN 對應。相容設備清單請參閱 [L3HW Device Support](/docs/bridging-and-switching/l3-hardware-offloading#l3hw-device-support) 文件。

目前仍有部分已知功能尚未實作。

### Underlay（路由封裝的 VXLAN 封包） {#underlay-routing-encapsulated-vxlan-packets}

1. 不支援透過 ECMP 使用 VTEP。

2. 不支援透過 bond、bridge、VLAN 介面使用 VTEP（僅支援獨立路由的 Ethernet 介面）。

3. 不支援透過 multicast 的 VTEP。

4. VTEP 無法在 VRF 內運作。

5. 不支援搭配 IPv6 的 VTEP。

### Overlay（Ethernet 與 VXLAN 之間的轉送） {#overlay-forwarding-between-ethernet-and-vxlan}

1. 不支援透過 VXLAN 的 VLAN 標記。

2. 不支援不同 VXLAN VNI 之間的路由。

3. VTEP 彼此隔離，且沒有機制可控制它們之間的「horizon」。

4. 橋接的 VXLAN 介面不支援 IGMP snooping。啟用 snooping 時，VXLAN 上的 MDB 項目不會被卸載，且 multicast 流量會在 Ethernet 與 VXLAN 之間受到限制。

5. MLAG 不支援橋接的 VXLAN 介面。

### 基本設定範例 {#basic-configuration-example}

在此範例中，使用靜態路由連線至遠端 VTEP，但也可以使用 OSPF 或 BGP 等動態路由協定。上游介面使用較高的 MTU，以支援大型封包與 VXLAN 封裝。以下是網路拓撲概觀：

**sfp-sfpplus1** - 上游（underlay）介面  
**sfp-sfpplus3** - 未標記 VLAN 10 的橋接埠  
**sfp-sfpplus4** - 未標記 VLAN 20 的橋接埠  
**vxlan-10010** - 未標記 VLAN 10 的 overlay 埠  
**vxlan-10020** - 未標記 VLAN 20 的 overlay 埠

```routeros
/interface/bridge
add name=bridge1 vlan-filtering=yes
/interface/ethernet
set [ find default-name=sfp-sfpplus1 ] l2mtu=9500 mtu=9500
/interface/vxlan
add bridge=bridge1 bridge-pvid=10 local-address=192.168.1.1 name=vxlan-10010 vni=10010
add bridge=bridge1 bridge-pvid=20 local-address=192.168.1.1 name=vxlan-10020 vni=10020
/interface/bridge/port
add bridge=bridge1 interface=sfp-sfpplus3 pvid=10
add bridge=bridge1 interface=sfp-sfpplus4 pvid=20
/interface/vxlan/vteps
add interface=vxlan-10010 remote-ip=192.168.1.2
add interface=vxlan-10020 remote-ip=192.168.1.2
/ip/address
add address=192.168.1.1 interface=lo network=192.168.1.1
add address=192.168.10.10/24 interface=sfp-sfpplus1 network=192.168.10.0
/ip/route
add dst-address=192.168.1.2 gateway=192.168.10.20
/interface/ethernet/switch
set 0 l3-hw-offloading=yes
```
