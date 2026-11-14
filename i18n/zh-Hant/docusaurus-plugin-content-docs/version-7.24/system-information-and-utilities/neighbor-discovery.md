---
sidebar_key: "system-information-and-utilities/neighbor-discovery"
sidebar_position: 9
title: "鄰居發現"
sidebar_label: "鄰居發現"
description: "鄰居發現協定可在二層域中使用 MNDP、CDP 或 LLDP 檢測裝置，並顯示已連線鄰居的 IP/MAC 地址和介面。配置選項包括協定選擇、發現間隔調整，以及用於共享 QoS 和 VLAN 的 LLDP TLV。"
tags:
  - 'neighbor-discovery'
  - 'lldp'
source: https://manual.mikrotik.com/docs/7.24/system-information-and-utilities/neighbor-discovery
captured_at: '2026-11-04T11:33:38+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

鄰居發現協定允許我們在二層廣播域中查詢與 MNDP（MikroTik 鄰居發現協定）、CDP（Cisco 發現協定）或 LLDP（鏈路層發現協定）相容的裝置。它們可用於繪製網路拓撲。

## 鄰居列表 {#neighbor-list}

鄰居列表顯示二層廣播域中發現的所有鄰居。它顯示鄰居連線到哪個介面、其 IP/MAC 地址以及其他相關引數。該列表為只讀。下面提供了鄰居列表示例：

```ros
[admin@MikroTik] /ip/neighbor/print 
 # INTERFACE ADDRESS         MAC-ADDRESS       IDENTITY   VERSION    BOARD      
 0 ether13   192.168.33.2    00:0C:42:00:38:9F MikroTik   5.99       RB1100AHx2
 1 ether11   1.1.1.4         00:0C:42:40:94:25 test-host  5.8        RB1000   
 2 Local     10.0.11.203     00:02:B9:3E:AD:E0 c2611-r1   Cisco I...                    
 3 Local     10.0.11.47      00:0C:42:84:25:BA 11.47-750  5.7        RB750  
 4 Local     10.0.11.254     00:0C:42:70:04:83 tsys-sw1   5.8        RB750G    
 5 Local     10.0.11.202     00:17:5A:90:66:08 c7200      Cisco I...
```

**子選單：** `/ip/neighbor`

| 屬性 | 描述 |
| :-- | :-- |
| **address** (*IP*) | 發現的裝置上配置的最高 IP 地址 |
| **address6** (*IPv6*) | 發現的裝置上配置的 IPv6 地址 |
| **add-dns-entries** (*yes \| no*) | 指定是否為該特定鄰居建立動態 DNS 條目，並將 identity 用作域名 |
| **add-dns-entries-suffix** (*string*) | 為每個鄰居建立的動態 DNS 條目新增的字尾。 |
| **age** (*time*) | 自上一個發現數據包以來的時間間隔 |
| **discovered-by** (*cdp\|lldp\|mndp*) | 顯示發現該鄰居所使用的協定列表。該屬性自 RouterOS 7.7 版本起可用。 |
| **board** (*string*) | RouterBoard 型號。僅對已安裝 RouterOS 的裝置顯示 |
| **identity** (*string*) | 已配置的系統標識 |
| **interface** (*string*) | 發現的裝置所連線的介面名稱 |
| **interface-name** (*string*) | 鄰居裝置上連線到二層廣播域的介面名稱。適用於 CDP。 |
| **ipv6** (*yes \| no*) | 顯示裝置是否啟用了 IPv6。 |
| **mac-address** (*MAC*) | 遠端裝置的 MAC 地址。可用於透過 mac-telnet 連線。 |
| **platform** (*string*) | 平臺名稱。例如 “MikroTik”、“cisco” 等。 |
| **software-id** (*string*) | 遠端裝置上的 RouterOS 軟體 ID。僅適用於已安裝 RouterOS 的裝置。 |
| **system-caps** (*string*) | 鏈路層發現協定（LLDP）報告的系統能力。 |
| **system-caps-enabled** (*string*) | 鏈路層發現協定（LLDP）報告的已啟用系統能力。 |
| **unpack** (*none\|simple\|uncompressed-headers\|uncompressed-all*) | 顯示發現數據包的壓縮型別。 |
| **uptime** (*time*) | 遠端裝置的執行時間。僅對已安裝 RouterOS 的裝置顯示。 |
| **version** (*string*) | 遠端裝置上已安裝軟體的版本號 |
| **running** (string array) | 報告鄰居裝置上執行的“功能”列表。目前僅列出 “CAPsMAN” 功能。 |

:::warning
鄰居條目數量限制為每個介面（總 RAM 兆位元組數）\*16，以避免記憶體耗盡。
:::

### LLDP 鄰居 {#lldp-neighbors}

透過 LLDP 發現的鄰居顯示在 `/ip/neighbor/lldp` 下的單獨只讀選單中。此選單顯示從鄰居裝置接收的詳細 LLDP 型別-長度-值（TLV）。

與彙總來自所有發現協定（MNDP、CDP 和 LLDP）的鄰居的常規 `/ip/neighbor` 選單不同，`/ip/neighbor/lldp` 僅顯示透過 LLDP 發現的條目。

示例輸出：

```ros
[admin@Switch] > /ip/neighbor/lldp/print
Columns: INTERFACE, ADDRESS4, ADDRESS6, MAC-ADDRESS, LLDP-CHASSIS-ID, LLDP-PORT-ID, LLDP-PORT-DESCRIPTION, LLDP-SYSTEM-NAME, LLDP-SYSTEM-DESCRIPTION
#  INTERFACE  ADDRESS4        ADDRESS6                   MAC-ADDRESS        LLDP-CHASSIS-ID    LLDP-PORT-ID  LLDP-PORT-DESCRIPTION  LLDP-SYSTEM-NAME  LLDP-SYSTEM-DESCRIPTION                                                     
0  ether2     192.168.88.128  fe80::f61e:57ff:fe13:d794  F4:1E:57:13:D7:94  F4:1E:57:13:D7:94  ether1        ether1                 Tested_CRS812     MikroTik RouterOS 7.24rc1 (testing) 2026-07-01 13:53:30 CRS812-8DS-2DQ-2DDQ 
   bridge1                                                                                                                                                                                                                        
1  ether3     192.168.88.127  fe80::f61e:57ff:fe47:9255  F4:1E:57:47:92:55  F4:1E:57:47:92:55  ether1        ether1                 Tested_CRS520     MikroTik RouterOS 7.24rc1 (testing) 2026-07-01 13:53:30 CRS520-4XS-16XQ     
   bridge1                                                                                                                                                                                                                        
2  ether4     192.168.88.9    fe80::1afd:74ff:fe81:9a    18:FD:74:81:00:9A  18:FD:74:81:00:86  ether1        ether1                 Tester6           MikroTik RouterOS 7.24rc1 (testing) 2026-07-01 13:53:30 CCR2216-1G-12XS-2XQ 
   bridge1                                                                                                                                                                                                                        
3  ether5     192.168.88.132  fe80::d601:c3ff:fe43:c035  D4:01:C3:43:C0:35  D4:01:C3:43:C0:35  ether1        ether1                 Tested_L009       MikroTik RouterOS 7.24rc1 (testing) 2026-07-01 13:53:30 L009UiGS            
   bridge1                                                                                                                                                                                                                        
4  ether8     192.168.88.129  fe80::f61e:57ff:fec2:8a3d  F4:1E:57:C2:8A:3D  F4:1E:57:C2:8A:2B  ether17       ether17                Tested_CRS418     MikroTik RouterOS 7.24rc1 (testing) 2026-07-01 13:53:30 CRS418-8P-8G-2S+    
   bridge1   
```

:::note
`lldpRemTable` SNMP 表僅報告透過 LLDP 發現的鄰居。僅由 CDP 或 MNDP 發現的條目會從 SNMP LLDP-MIB 中排除。
:::

## 發現配置 {#discovery-configuration}

可以使用介面列表更改介面是否參與鄰居發現。如果介面包含在發現介面列表中，它將傳送有關係統的基本資訊，並處理在二層網路中廣播的已接收發現封包。從介面列表中移除介面將同時停用此介面上的鄰居發現以及在該介面上發現此裝置本身的可能性。

**子選單：** `/ip/neighbor/discovery-settings`

| 屬性 | 描述 |
| :-- | :-- |
| **discover-interface-list** (*string*; 預設值：**static**) | 發現協定將在其成員上執行的介面列表。 |
| **discover-interval** (*time: 5s..9h6m8s*; 預設值：**30s**) | 調整鄰居發現數據包的傳輸頻率。它還使用以下公式調整 CDP 和 LLDP 封包的生存時間（TTL）TLV 值：(`discover-interval` \* 4) + 1。該設定自 RouterOS 7.16 版本起可用。 |
| **lldp-dcbx** (*yes \| no*; 預設值：**no**) | 是否傳送資料中心橋接能力交換協定（DCBX）TLV，這允許使用 LLDP 與其他鄰居裝置通訊交換器的 [QoS 設定](../bridging-and-switching/quality-of-service.md)和能力。僅適用於採用 Marvell Prestera 交換器的 MikroTik 裝置（例如 CRS3xx）。  啟用 DCBX 包括以下 TLV：ETS（增強傳輸選擇）配置 TLV。此 TLV 用於共享交換器的 ETS 配置。它包括：willingness 位，用於指示裝置是否願意接受來自鄰居裝置的 QoS 配置。在 RouterOS 中，willingness 位設定為 disabled，表示交換器不會接受遠端配置，而是使用自己的設定。優先順序分配表，將優先順序對映到特定流量類別。頻寬分配表，其中 RouterOS 根據 <span className="ros-background-accent-green-bolder"><code>weight</code></span> 屬性計算分配給每個佇列的頻寬百分比。這適用於在 <code>`/interface/ethernet/switch/qos/tx-manager/queue`</code> 設定中使用 <span className="ros-background-accent-green-bolder"><code>high-priority-group</code></span> 的佇列。傳輸選擇演算法（TSA）表，其中 <span className="ros-background-accent-green-bolder"><code>high-priority-group</code></span> 佇列分配給 ETS，<span className="ros-background-accent-green-bolder"><code>strict-priority</code></span> 佇列分配給 Strict Priority，而 <span className="ros-background-accent-green-bolder"><code>low-priority-group</code></span> 或非硬體解除安裝佇列分配給廠商特定演算法。ETS 建議 TLV。這提供了關於鄰居裝置應如何配置 ETS 的建議。RouterOS 使用與 ETS 配置 TLV 相同的資料來給出建議。基於優先順序的流控配置 TLV。此 TLV 用於共享 PFC 配置。與 ETS TLV 類似，willingness 位設定為 disabled，表示交換器不接受遠端 PFC 配置。PFC 會根據在 <code>`/interface/ethernet/switch/qos/priority-flow-control`</code> 和 <code>`/interface/ethernet/switch/qos/port`</code> 下配置的設定，為特定優先順序啟用。應用優先順序 TLV。此 TLV 用於傳達網路中不同應用如何設定優先順序。應用 VLAN TLV。此 TLV 用於共享應用的 VLAN 配置。RouterOS 目前不支援在此 TLV 中傳送值，而是傳送空 VLAN 表。 |
| **lldp-mac-phy-config**(*yes \| no*; 預設值：**no**) | 是否在 LLDP 中傳送 MAC/PHY 配置/狀態 TLV，該 TLV 指示介面能力、雙工狀態的當前設定、位元率和自動協商。僅適用於乙太網介面。雖然該 TLV 在 LLDP 中是可選的，但在傳送 LLDP-MED 時是必需的，這意味著即使該屬性配置為 disabled，在必要時也會包含此 TLV。 |
| **lldp-max-frame-size** (*yes \| no*; 預設值：**no**) | 是否在 LLDP 中傳送最大幀大小 TLV，該 TLV 以位元組為單位指示介面的最大幀大小能力（`l2mtu` + 18）。僅適用於乙太網介面。 |
| **lldp-med** (*yes \| no*; 預設值：**yes**) | 指定是否通告 LLDP-MED 媒體能力 TLV。使用 `lldp-med-net-policy-vlan` 時必須啟用此選項。該設定自 RouterOS 7.23 版本起可用。 |
| **lldp-poe-power** (*yes \| no*; 預設值：**yes**) | 有兩個特定 TLV 用於促進供電裝置（PSE）與受電裝置（PD）之間的乙太網供電（PoE）管理：IEEE 802.3 組織特定 Power Via MDI TLV；TIA-1057（LLDP-MED）組織特定擴充套件 Power via MDI TLV。`lldp-poe-power` 屬性決定是否在 LLDP 訊息中傳輸 IEEE 802.3 組織特定 Power Via MDI TLV。  LLDP-MED 組織特定擴充套件 Power via MDI TLV 的傳輸不可配置。當遠端裝置已傳輸接收功率的 LLDP-MED 能力時，它會自動包含在發出的 LLDP-MED 封包中。  這些 TLV 僅與支援 [PoE-Out](../hardware/poe-out.md) 的乙太網介面相關。該設定自 RouterOS 7.15 版本起可用，並取代 PoE-out 埠 `poe-lldp-enabled` 設定。 |
| **lldp-med-net-policy-vlan** (*integer 0..4094*; 預設值：**disabled**) | 用於 LLDP-MED 網路策略 TLV 的通告 VLAN ID。這允許為支援 LLDP-MED 的裝置（例如 VoIP 電話）分配 VLAN ID。僅當在介面上發現支援 LLDP-MED 的裝置且啟用了 `lldp-med` 時，才會將該 TLV 新增到這些介面。其他 TLV 值是預定義的，無法更改：應用型別 - Voice；VLAN 型別 - Tagged；二層優先順序 - 0；DSCP 優先順序 - 0。與橋接介面一起使用時，應透過 `protocol-mode` 設定啟用 (R/M)STP 協定。  此外，應使用 `protocol` 設定排除其他鄰居發現協定（例如 CDP），以避免 LLDP-MED 配置錯誤。 |
| **lldp-vlan-info** (*yes \| no;* 預設值：**no**) | 是否在 LLDP 中傳送與 VLAN 相關的 IEEE 802.1 組織特定 TLV。  啟用此設定後，會通告三個 TLV：埠 VLAN ID。這適用於橋接埠的 <span className="ros-background-accent-green-bolder"><code>pvid</code></span> 屬性。埠和協定 VLAN ID。此 TLV 未使用，始終指示 “not supported” 和 “not enabled”。VLAN 名稱。這包括來自 “<code>`/interface/bridge/vlan`</code>” 表中的最多 10 個活動 VLAN。這些 TLV 與新增到 [vlan-filtering](../bridging-and-switching/index.md#bridge-vlan-filtering) 橋接的介面相關，該設定自 RouterOS 7.16 版本起可用。 |
| **mode** (*rx-only \| tx-only \| tx-and-rx*; 預設值：**tx-and-rx**) | 選擇鄰居發現數據包的傳送和接收模式。該設定自 RouterOS 7.7 版本起可用。 |
| **protocol** (*cdp \| lldp \| mndp*; 預設值：**cdp,lldp,mndp**) | 使用的發現協定列表。 |

自 RouterOS v6.44 起，鄰居發現在各個從介面上工作。每當主介面（例如 bonding 或 bridge）包含在發現介面列表中時，其所有從介面都會自動參與鄰居發現。可以僅允許某些從介面進行鄰居發現。為此，請將特定的從介面包含在列表中，並確保不包含主介面。

```ros
/interface/bonding
add name=bond1 slaves=ether5,ether6
/interface/list
add name=only-ether5
/interface/list/member
add interface=ether5 list=only-ether5
/ip/neighbor/discovery-settings
set discover-interface-list=only-ether5
```

現在，鄰居列表會顯示主介面以及接收到發現訊息的實際從介面。

```ros
[admin@R2] > ip neighbor print
 # INTERFACE ADDRESS                                           MAC-ADDRESS       IDENTITY   VERSION    BOARD         
 0 ether5    192.168.88.1                                      CC:2D:E0:11:22:33 R1         6.45.4 ... CCR1036-8G-2S+
   bond1    
```

## LLDP {#lldp}

根據 RouterOS 配置，可以在 LLDP 訊息中傳送不同的型別-長度-值（TLV）。這包括：

- 機箱 ID（MAC 地址）。
- 埠 ID（介面名稱）。
- 生存時間。
- 系統名稱（系統標識）。
- 系統描述（平臺 - MikroTik，軟體版本 - RouterOS 版本，硬體名稱 - RouterBoard 名稱）。
- 管理地址（埠上配置的所有 IP 地址）。
- 系統能力（已啟用的系統能力，例如 bridge 或 router）。
- 埠描述（如果傳送介面是 bridge 或 bond 的一部分，則為類似 “bridge/ether1” 的組合介面名稱；否則為與埠 ID 相同的介面名稱）。
- IEEE 802.1 埠 VLAN ID。
- IEEE 802.1 埠和協定 VLAN ID。
- IEEE 802.1 VLAN 名稱。
- IEEE 802.3 MAC/PHY 配置/狀態。
- IEEE 802.3 Power Via MDI。
- IEEE 802.3 最大幀大小。
- LLDP-MED 媒體能力（MED 能力列表）。
- LLDP-MED 網路策略（為語音流量分配的 VLAN ID）。
- LLDP-MED 擴充套件 Power via MDI。
- 埠擴充套件（埠擴充套件器和控制器橋通告）。
- LLDPDU 結束。
