---
sidebar_key: "bridging-and-switching/vxlan"
sidebar_position: 6
title: "VXLAN"
sidebar_label: "VXLAN"
description: "本頁介紹 MikroTik RouterOS 的 VXLAN 實現，涵蓋其在擴充套件 VLAN ID 方面的用途、VXLAN 介面和 VTEP 的配置選項，以及轉發表監控。它詳細說明了 MTU、VNI、ARP 處理以及用於 UDP 上二層 overlay 的組播組管理等設定。"
tags:
  - 'vxlan'
source: https://manual.mikrotik.com/docs/7.24/bridging-and-switching/vxlan
captured_at: '2026-11-04T11:27:34+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

---

Virtual eXtensible Local Area Network (VXLAN) 是一種隧道協定，旨在解決 IEEE 802.1Q 中 VLAN ID 數量有限（4096 個）的問題，並由 IETF RFC 7348 描述。使用 VXLAN 時，識別符號的大小擴充套件到 24 位（16777216）。它在三層網路上建立二層覆蓋方案，並且該協定執行在 UDP 之上。RouterOS VXLAN 介面支援 IPv4 或 IPv6（自 7.6 版本起），但不支援雙棧。

:::info
VXLAN 會為 IPv4 帶來 50 位元組開銷，為 IPv6 帶來 70 位元組開銷。配置 VXLAN 時，建議確保封裝後的乙太網幀大小不超過底層網路的 MTU，這可以透過相應配置 MTU 或限制乙太網幀大小來實現。
:::

只有同一 VXLAN 段內的裝置才能相互通訊。每個 VXLAN 段透過一個 24 位段 ID 來標識，稱為 VXLAN 網路識別符號（VNI）。與大多數隧道不同，VXLAN 是一對多網路，而不僅僅是點對點。終止 VXLAN 隧道的 VXLAN 端點稱為 VXLAN 隧道端點（VTEP）。RouterOS 僅支援靜態配置的遠端 VTEP。當需要透過 VXLAN 傳送單播流量時，裝置可以以類似於學習網橋的方式動態學習另一端的 IP 地址，並僅將流量轉發到必要的 VTEP。對於需要泛洪（廣播、未知單播和組播）到同一段內所有 VTEP 的流量，VXLAN 可以使用組播或帶首端複製的單播，為每個遠端 VTEP 傳送一個副本。

## 配置選項 {#configuration-options}

---

本節介紹 VXLAN 介面和 VTEP 配置選項。

**子選單：** `/interface/vxlan`

| 屬性 | 描述 |
| :-- | :-- |
| **allow-fast-path** (*yes \| no*; 預設值: **yes**) | 是否允許 [Fast Path](../firewall-and-quality-of-service/packet-flow-in-routeros.md#fast-path) 處理。透過 VXLAN 傳輸的分片和泛洪封包將被重定向到慢速路徑。使用 VRF 的 VXLAN 介面會停用 Fast Path。該設定自 RouterOS 7.8 版本起可用。 |
| **arp** (*disabled \| enabled \| local-proxy-arp \| proxy-arp \| reply-only*; 預設值: **enabled**) | 地址解析協定（ARP）設定<ul><li><span className="ros-icon-success"><code>disabled</code></span> - 介面將不使用 ARP</li><li><span className="ros-icon-success"><code>enabled</code></span> - 介面將使用 ARP</li><li><span className="ros-icon-success"><code>local-proxy-arp</code></span> - 路由器在介面上執行代理 ARP，並將應答傳送回同一介面</li><li><span className="ros-icon-success"><code>proxy-arp</code></span> - 路由器在介面上執行代理 ARP，並將應答傳送到其他介面</li><li><span className="ros-icon-success"><code>reply-only</code></span> - 介面僅應答源自與 IP/ARP 表中靜態條目匹配的 IP 地址/MAC 地址組合的請求。動態條目不會自動儲存到 IP/ARP 表中。因此，要使通訊成功，必須已存在有效的靜態條目。</li></ul> |
| **arp-timeout** (*auto \| integer*; 預設值: **auto**) | 在未從某 IP 收到封包後，ARP 記錄在 ARP 表中保留的時長。值 `auto` 等於 IP/Settings 中 `arp-timeout` 的值，預設為 30 秒。 |
| **bridge** (*name*; 預設值: ) | 將 VXLAN 介面作為從屬埠新增到的[網橋](../user-guides/routing-and-networking-protocols/unicast/bgp/index.md)介面名稱。 |
| **bridge-pvid** (*integer 1..4094;* 預設值: **1**) | 用於為動態網橋埠分配 PVID 引數。僅當網橋的 vlan-filtering 設定為 yes 時，此屬性才會生效。 |
| **checksum**(*yes \| no*; 預設值：**no**) | 設定控制是否在傳送的外部 VXLAN 封包中計算 UDP 校驗和：<span className="ros-background-accent-green-bolder"><code>no</code></span> – 在傳送的外部封包中，UDP 校驗和設定為零。這還允許接收透過 IPv6 傳輸且 UDP 校驗和為零的 VXLAN 封包。<span className="ros-background-accent-green-bolder"><code>yes</code></span> - 在傳送的外部封包中計算 UDP 校驗和。如果封包傳輸使用硬體解除安裝，則忽略此設定，行為預設為傳送 UDP 校驗和為零的封包。 |
| **comment** (*string*; 預設值: ) | 介面的簡短描述。 |
| **disabled** (*yes \| no*; 預設值: **no**) | 更改介面是否被停用。 |
| **dont-fragment**(*auto \| disabled \| enabled \| inherit*; 預設值: **auto**) | “不分片”（DF）標誌控制封包在網路中傳送前是否可被拆分為更小的封包（即分片）。在配置 VXLAN 時，此設定決定外層 IPv4 報頭中是否設定 DF 標誌，並且當封裝的封包超過出介面 MTU 時可以控制封包分片。此設定有三個選項： <br/><ul><li><span className="ros-icon-success"><code>auto</code></span> - 如果裝置支援 VXLAN 解除安裝，則 dont-fragment 模式將按 <span className="ros-icon-success"><code>enabled</code></span> 執行。如果不支援 VXLAN 解除安裝，則將使用 <span className="ros-background-accent-green-bolder"><code>inherit</code></span> 模式。</li><li><span className="ros-icon-success"><code>disabled</code></span> - 不在外層 IPv4 報頭中設定 DF 標誌，這意味著如果封包過大而無法通過出介面傳送，則可以被分片。這也允許在 VXLAN 使用 IPv6 底層網路時進行封包分片。會在相容裝置上停用硬體解除安裝。</li><li><span className="ros-icon-success"><code>enabled</code></span> - 始終在外層 IPv4 報頭中設定 DF 標誌，這意味著封包不會被分片，若超過出介面的 MTU 則會被丟棄。這也避免了在 VXLAN 使用 IPv6 底層網路時的封包分片。</li><li><span className="ros-background-accent-green-bolder"><code>inherit</code></span> - 外層 IPv4 報頭中的 DF 標誌取決於內層 IPv4 的 DF 標誌。如果內層 IPv4 報頭設定了 DF 標誌，則外層 IPv4 報頭也會設定。如果封包超過出介面的 MTU 且已設定 DF，則會被丟棄。如果內層封包不是 IP，則外層 IPv4 報頭不會設定 DF 標誌，封包可以被分片。如果內層封包是 IPv6，則外層 IPv4 報頭將始終設定 DF 標誌，封包不能被分片。請注意，當 VXLAN 使用 IPv6 底層網路時，此設定不起任何作用，其處理方式與 <span className="ros-icon-success"><code>disabled</code></span> 相同。</li></ul> 該設定自 RouterOS 7.8 版本起可用。 |
| **group** (*IPv4 \| IPv6*; 預設值: ) | 指定後，可使用組播組地址在 VTEP 之間轉發廣播、未知單播和組播流量。此屬性需要同時指定 `interface` 設定。介面將使用 IGMP 或 MLD 加入指定的組播組，請確保新增必要的 PIM 和 IGMP/MLD 配置。設定此屬性後，`vteps-ip-version` 會自動更新為所使用的組播 IP 版本。會在相容裝置上停用硬體解除安裝。 |
| **hw** (*yes \| no*; 預設值: **yes**) | 允許停用硬體解除安裝，僅適用於支援 VXLAN 解除安裝的裝置。 |
| **interface** (*name*; 預設值: ) | 用於組播轉發的介面名稱。此屬性需要同時指定 `group` 設定。會在相容裝置上停用硬體解除安裝。 |
| **learning**(*yes \| no*; 預設值: **yes**) | 該設定控制是否從接收到的封包中動態學習內層源 MAC 地址和遠端 VTEP IP/IPv6 地址。 |
| **local-address** (*IPv4 \| IPv6*; 預設值: ) | 指定 VXLAN 介面的本地源地址。如果未設定，則會選擇一個出介面的 IP 地址作為 VXLAN 封包的源地址。設定該屬性後，`vteps-ip-version` 會自動更新為所使用的本地 IP 版本。該設定自 RouterOS 7.7 版本起可用。 |
| **mac-address** (*MAC*; 預設值: ) | 介面的靜態 MAC 地址。未指定時將分配一個隨機生成的 MAC 地址。 |
| **max-fdb-size** (*integer: 1*..65535**; 預設值: **4096**) | 限制 VXLAN 可在轉發資料庫（FDB）中儲存的 MAC 地址最大數量。 |
| **mtu** (*integer*; 預設值: **1500**) | 對於最大傳輸單元，VXLAN 介面預設將 MTU 設定為 1500。`l2mtu` 將根據關聯的 `interface` 自動設定（減去與 VXLAN 報頭對應的 50 位元組）。如果未指定介面，則使用 `l2mtu` 值 65535。`l2mtu` 無法更改。 |
| **name** (*text*; 預設值: **vxlan1**) | 介面名稱。 |
| **port** (*integer: 1*..65535**; 預設值: **4789**) | 用於監聽並向遠端 VTEP 傳送封包的 UDP 埠號。 |
| **rem-csum** (*both \| none \| rx \| tx*; 預設值: **none**) | 更改 VXLAN 介面的遠端校驗和解除安裝（RCO）設定。RCO 是一種省略封裝封包內層校驗和的技術，允許由網路驅動解除安裝外層校驗和。然而，它涉及對封裝協定的改動，接收方也必須支援。因此，預設情況下它是停用的，提供該設定是為了確保與依賴此功能的系統相容。 <br/> RCO 在以下 Internet-Draft 中有詳細說明： <br/> Remote checksum offload for VXLAN, draft-herbert-vxlan-rco-00. Remote checksum offload for encapsulation, draft-herbert-remotecsumoffload-00. <br/> 如果使用了[硬體解除安裝](./vxlan.md#hardware-offloaded-vxlan)，則忽略此設定，行為預設為 none。 |
| **ttl** (*auto \| integer: 0*..255**; 預設值: **auto**) | 指定在傳送的封包中使用的 TTL 值。使用 `auto` 選項時，TTL 預設設定為 64。但是，如果 VXLAN 使用組播底層網路，則預設 TTL 設定為 1。如果組播網路涉及路由，則需要將 TTL 增大到更高的值。 |
| **vni** (*integer: 1..16777215*; 預設值: ) | VXLAN 網路識別符號（VNI）。 |
| **vtep-vrf** (*name*; 預設值: **main**) | 為 VXLAN 介面設定 VRF，VTEP 將在該 VRF 上監聽並建立連線。使用 `interface` 和組播 `group` 設定時不支援 VRF。同一個 UDP `port` 不能同時用於多個路由表。當使用未設定為 "main" 的 VRF 時，會在相容裝置上停用硬體解除安裝。該設定自 RouterOS 7.7 版本起可用。 |
| **vteps-ip-version** (*ipv4 \| ipv6*; 預設值: **ipv4**) | 用於靜態配置的 VTEP 的 IP 協定版本。RouterOS VXLAN 介面不支援雙棧，任何配置為相反 IP 版本的遠端 VTEP 都將被忽略。當設定了組播 `group` 或 `local-address` 屬性時，`vteps-ip-version` 會自動更新為所使用的 IP 版本。使用 IPv6 會在相容裝置上停用硬體解除安裝。該設定自 RouterOS 7.6 版本起可用。 |

**子選單：** `/interface/vxlan/vteps`

| 屬性 | 描述 |
| :-- | :-- |
| **comment** (*string*; 預設值：) | 已配置 VTEP 的簡短描述。 |
| **interface** (*name*; 預設值：) | VXLAN 介面的名稱。 |
| **remote-ip** (*IPv4 \| IPv6*; 預設值：) | 定義當 VXLAN 介面需要傳送 BUM（廣播、未知單播、組播）流量時使用的 VTEP 端點 IPv4 或 IPv6 地址。它不用作訪問控制。 |

## 轉發表 {#forwarding-table}

---

自 RouterOS 7.9 版本起，可以監控從遠端 VTEP 學習到的 MAC 地址。

**子選單：** `/interface/vxlan/fdb`

| 屬性 | 描述 |
| :-- | :-- |
| **interface** (*只讀：*name**) | VXLAN 介面的名稱。 |
| **mac-address** (*只讀：MAC 地址*) | MAC 地址。 |
| **remote-ip** (*只讀：IPv4 \| IPv6 地址*) | 遠端 VTEP 的 IPv4 或 IPv6 目標地址。 |

```ros
[admin@MikroTik] > /interface/vxlan/fdb/print          
 0 remote-ip=2001::2 mac-address=56:FF:AA:1A:72:33 interface=vxlan1 

 1 remote-ip=2002::2 mac-address=AE:EC:C4:12:8B:B9 interface=vxlan1 

 2 remote-ip=192.168.10.20 mac-address=FE:AF:58:31:A7:B6 interface=vxlan2
```

## 配置示例 {#configuration-example}

---

此配置示例在兩個靜態配置的 VTEP 端點之間建立單個 VXLAN 隧道。

首先，在兩臺路由器上建立 VXLAN 介面。

```ros
/interface/vxlan
add name=vxlan1 port=4789 vni=10
```

然後，在兩臺路由器上使用各自的 IPv4 目標地址配置 VTEP。兩臺裝置都應具有通往目標地址的活動路由。

```ros
# Router1
/interface/vxlan/vteps
add interface=vxlan1 remote-ip=192.168.10.10

# Router2
/interface/vxlan/vteps
add interface=vxlan1 remote-ip=192.168.20.20
```

配置完成。可以將 VXLAN 介面與其他乙太網介面一起加入網橋。

## 硬體解除安裝 VXLAN {#hardware-offloaded-vxlan}

---

從 RouterOS 7.18 版本開始，引入了對硬體解除安裝 VXLAN 的初步支援。這使得解除安裝的 VXLAN 資料平面成為可能，支援封裝和解封裝，並允許在啟用 vlan-filtering 的網橋內進行靜態的一對一 VLAN 到 VXLAN 對映。有關相容裝置列表，請參閱 [L3HW 裝置支援](./l3-hardware-offloading.md#l3hw-device-support) 文件。

目前，一些已知功能尚未實現。

### 底層網路（路由封裝後的 VXLAN 封包） {#underlay-routing-encapsulated-vxlan-packets}

1. VTEP 不支援透過 ECMP。

2. VTEP 不支援透過 bond、bridge、VLAN 介面（僅支援獨立的路由乙太網介面）。

3. VTEP 不支援透過組播。

4. VTEP 無法在 VRF 內執行。

5. VTEP 不支援 IPv6。

### 覆蓋網路（在乙太網和 VXLAN 之間轉發） {#overlay-forwarding-between-ethernet-and-vxlan}

1. 不支援在 VXLAN 上打 VLAN 標籤。

2. 不支援不同 VXLAN VNI 之間的路由。

3. VTEP 是隔離的，並且沒有機制控制它們之間的“horizon”。

4. 橋接的 VXLAN 介面不支援 IGMP 偵聽。啟用偵聽後，VXLAN 上的 MDB 條目不會被解除安裝，並且乙太網和 VXLAN 之間的組播流量會受到限制。

5. 橋接的 VXLAN 介面不支援 MLAG。

### 基本配置示例 {#basic-configuration-example}

在此示例中，使用靜態路由到達遠端 VTEP，但也可以使用 OSPF 或 BGP 等動態路由協定。上游介面具有更高的 MTU，以支援大型封包和 VXLAN 封裝。以下是網路拓撲概覽：

**sfp-sfpplus1** - 上游（底層）介面  
**sfp-sfpplus3** - 用於未標記 VLAN 10 的橋接埠  
**sfp-sfpplus4** - 用於未標記 VLAN 20 的橋接埠  
**vxlan-10010** - 用於未標記 VLAN 10 的覆蓋埠  
**vxlan-10020** - 用於未標記 VLAN 20 的覆蓋埠

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
