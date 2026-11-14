---
sidebar_key: "high-availability-solutions/multi-chassis-link-aggregation-group"
sidebar_position: 3
title: "多機箱鏈路聚合組"
sidebar_label: "多機箱鏈路聚合組"
description: "RouterOS 中的 MLAG 透過在兩臺裝置上配置 LACP bond 來實現物理冗餘，使用戶端感知為單一連線，同時確保故障切換。它使用 ICCP 進行對等通訊，支援 STP 協定，並且需要在專用埠上進行仔細的 VLAN 配置。對於大型網路，MLAG 是 CPU 密集型的，並且與 L3 offloading 或 MVRP 的相容性有限。"
tags:
  - 'mlag'
  - 'bridge-configuration'
  - 'stp'
source: https://manual.mikrotik.com/docs/7.24/high-availability-solutions/multi-chassis-link-aggregation-group
captured_at: '2026-11-04T11:29:58+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 簡介 {#introduction}

RouterOS 中的 MLAG（多機箱鏈路聚合組）實現允許在兩臺獨立裝置上配置 LACP bond，而用戶端裝置會認為自己連線的是同一臺機器。這在交換器故障時提供物理冗餘。

兩臺對等裝置都會建立 MLAG 介面，並透過 `mlag-peer-port` 使用 ICCP（Inter Chassis Control Protocol）更新網橋主機表。RouterOS ICCP 不需要 IP 配置；它會發送未標記的 Layer2 封包，這些封包標記為 EtherType 0x88B5，目的 MAC 地址為 01:80:C2:00:00:0E。ICCP 封包屬於鏈路本地流量，這意味著它們始終由 MLAG 裝置自身接收和處理，絕不會轉發到網路的其他部分。每臺 MLAG 裝置上的 peer-port 必須彼此直接連線。還建議將 peer 埠使用的未標記 VLAN 與網路其餘部分隔離：可以為 peer 埠分配專用的未標記 VLAN（使用 `pvid`），或將其設定為僅允許帶 VLAN 標籤的幀（使用 `frame-types=admit-only-vlan-tagged`）。peer 埠可以配置為單個乙太網介面或 bonding 介面。不過，建議使用 bonding 介面，因為它有助於防止單個介面故障影響連通性，尤其是在兩臺 MLAG 節點仍處於執行狀態時。

當 mlag-peer-port 正常執行且 ICCP 建立後，將進行主裝置選舉並選出 system-id。優先順序最低的對等裝置將充當主裝置。如果優先順序相同，則網橋 MAC 地址最低的對等裝置將成為主裝置。此 system-id 用於 STP BPDU 網橋標識和 LACP 系統 ID。MLAG 支援 STP、RSTP 或 MSTP 協定。在兩臺節點的雙連線網橋埠上使用相同的 STP 優先順序和相同的 STP 配置。當 MLAG 網橋被選舉為 STP 根橋時，兩臺裝置都會在網橋監控中顯示為根橋。

:::info
從 **RouterOS 版本 7.22** 開始，MLAG 按網橋介面配置，而不是透過專用的 MLAG 子選單配置。由於這一變化，任何 RouterOS 裝置（包括虛擬 CHR 例項）都可用作 MLAG 節點。

硬體解除安裝的 MLAG 僅在[配備 Marvell Prestera 交換器的 MikroTik 裝置](../bridging-and-switching/marvell-prestera-switch-chip-features.md)上可用。所有其他裝置僅支援軟體實現的 MLAG。

配置語法和監控屬性有哪些變化？

| RouterOS 7.22+（新）                    | RouterOS 7.21-（舊）                         |
|:--|:--|
| 配置選單：`/interface/bridge` | 配置選單：`/interface/bridge/mlag` |
| `mlag-heartbeat`                        | `heartbeat`                                  |
| `mlag-peer-port`                        | `peer-port`                                  |
| `mlag-priority`                         | `priority`                                   |
| `mlag-state`                            | `status`                                     |
| `mlag-active-role`                      | `active-role`                                |
| `bridge-id`                             | `system-id`                                  |

換句話說，增加了 mlag- 字首，整個 MLAG 配置和監控現在都在普通 bridge 樹下完成。

升級到 RouterOS 7.22（或任何更新版本）會自動將舊 MLAG 配置轉換為新格式。無需手動更改。  
降級到早於 7.22 的版本將清除 MLAG 配置，因為舊韌體無法識別新語法。建議：在降級前備份當前配置或匯出 MLAG 設定，以便降級後重新應用。

:::

:::info
MLAG 與 [L3 硬體解除安裝](../bridging-and-switching/l3-hardware-offloading.md) 不相容。使用 MLAG 時，必須停用 L3 硬體解除安裝。

MLAG 與 [多 VLAN 註冊協定（MVRP）](../bridging-and-switching/index.md#mvrp) 不相容。雙連線 bond 上已註冊的 VLAN 不會同步到另一臺 MLAG 節點。

:::

:::danger
在包含大量主機和 VLAN 的網路中，MLAG 主機同步可能會大量佔用 CPU 和記憶體。對於使用單核 **MIPSBE CPU** 的交換器（例如 CRS326-24S+2Q+RM、CRS354-48P-4S+2Q+RM、CRS518-16XS-2XQ-RM），建議僅在最多 1,000 臺主機的網路中使用 MLAG。

在主機數量更多的網路中，這些交換器上的 MLAG 可能導致意外行為。

:::

![](/img/7dac383ebfcf0a67.webp)

### 封包轉發與負載均衡 {#packet-forwarding-and-load-balancing}

BUM（廣播、未知單播、組播）封包轉發分兩個階段進行。

#### 階段 1 - 本地轉發 {#stage-1---local-forwarding}

當節點收到 BUM 流量時，會像傳統（非 MLAG）設定中一樣，將封包本地泛洪到同一 VLAN 的所有成員埠。此外，它還會透過 peer-port 將流量轉發到另一臺 MLAG 節點。

:::info
僅當 peer-port 也是該 VLAN 的成員時，才會透過 peer-port 轉發。因此文件強調應將 peer-port 包含在跨越兩臺 MLAG 節點的所有 VLAN 中。

:::

#### 階段 2 - 對等裝置遠端轉發 {#stage-2---remote-forwarding-by-peer}

當對等節點透過 peer-port 收到 BUM 流量時，會將該流量泛洪到同一 VLAN 的所有常規網橋埠。這些是未指定 `mlag-id` 的埠（即獨立的乙太網或 bond 介面）。對於帶 `mlag-id` 的 bond 介面，對等節點會根據鏈路狀態做出決定：

- 如果兩條鏈路（本地和遠端）均處於活動狀態，則不會將流量泛洪到自己的 MLAG bond 埠——這樣可以避免傳送重複封包，因為第一個節點已經處理過該流量。
- 如果遠端對等裝置的鏈路不活動，而本地鏈路活動，則對等節點會將流量泛洪到 MLAG bond，以確保送達。

單播流量的行為類似，但在比較常規 LAG 與 MLAG 時有一個關鍵區別。在常規 LAG 設定中，出站封包會根據傳送雜湊策略在所有活動鏈路上進行負載均衡。在兩條鏈路均處於活動狀態的 MLAG 設定中，流量不會透過兩臺交換器之間的 peer-port 進行負載均衡。相反，流量僅透過 MLAG 的本地成員鏈路轉發——始終走最短路徑。僅當本地 MLAG 鏈路故障時才使用 peer-port。在這種情況下，流量會透過 peer-port 轉發到另一臺節點以到達目的地。發生這種情況時，主機表還會更新在 MLAG bond 上學習到的 MAC 地址條目，以表明目的地現在可透過 peer-port 到達。在 MLAG bond 由 2 + 2 條活動鏈路（每節點 2 條鏈路）組成的設定中，傳送雜湊僅在兩條本地鏈路之間執行——而不是在所有四條鏈路上執行。當 MLAG 對用於多個雙連線 bond，且傳入流量已經分佈在兩個對上時，才能實現負載均衡。

## 快速設定 {#quick-setup}

在此示例中，CRS317 和 CRS309 裝置用作 MLAG 對等裝置，任何具有兩個 SFP+ 介面的裝置都可以用作 LACP 用戶端。兩臺對等節點上都使用 SFP+1 介面來建立 `mlag-peer-port`，並將其用於 ICCP，網路示意圖見下文。

![](/img/19c0854c81bd23fd.webp)為 **Peer1** 和 **Peer2** 裝置配置用於 MLAG 的 bonding 介面，在兩臺對等裝置上使用匹配的 `mlag-id` 設定，並將 LACPDU 傳送速率設定為 1 秒：

```ros
# Peer1
/interface/bonding
add mlag-id=10 mode=802.3ad name=client-bond slaves=sfp-sfpplus2 lacp-rate=1sec

# Peer2
/interface/bonding
add mlag-id=10 mode=802.3ad name=client-bond slaves=sfp-sfpplus2 lacp-rate=1sec
```

設定啟用 `vlan-filtering` 的網橋介面。指定 `mlag-peer-port` 以啟用 MLAG。要控制哪臺裝置成為主 MLAG 節點，請在首選裝置上設定較低的 `mlag-priority` 值。在此示例中，我們希望 Peer1 成為主節點，因此設定其 `priority=50`。Peer2 保留預設優先順序 128，從而成為輔助節點。

在此示例中，我們希望兩臺 MLAG 節點都充當根橋，因此使用 `priority=0x1000` 分配更優（更低）的網橋優先順序。請確保兩臺 MLAG 節點使用相同的優先順序值。

可選：可以在網橋介面上設定 `frame-types=admit-only-vlan-tagged`，以停用預設的未標記 VLAN 1（`pvid=1`）。

```routeros
# Peer1
/interface/bridge
add name=bridge1 vlan-filtering=yes mlag-peer-port=sfp-sfpplus1 mlag-priority=50 priority=0x1000 frame-types=admit-only-vlan-tagged

# Peer2
/interface/bridge
add name=bridge1 vlan-filtering=yes mlag-peer-port=sfp-sfpplus1 priority=0x1000 frame-types=admit-only-vlan-tagged
```

接下來，將必要的介面新增到網橋。在此示例中，只需新增 peer 埠（sfp-sfpplus1）和 client-bond 介面。

對於 peer 埠，我們透過將其配置為僅接受帶 VLAN 標籤的流量（`frame-types=admit-only-vlan-tagged`）來停用預設的未標記 VLAN 1（`pvid=1`）。

對於 client-bond 介面，我們希望未標記流量屬於 VLAN 10，因此在該介面上設定 `pvid=10`。

```ros
# Peer1
/interface/bridge/port
add bridge=bridge1 interface=sfp-sfpplus1 frame-types=admit-only-vlan-tagged
add bridge=bridge1 interface=client-bond pvid=10

# Peer2
/interface/bridge/port
add bridge=bridge1 interface=sfp-sfpplus1 frame-types=admit-only-vlan-tagged
add bridge=bridge1 interface=client-bond pvid=10
```

:::danger
MLAG 支援 STP、RSTP 或 MSTP 協定。在兩臺節點的雙連線網橋埠上使用相同的 STP 優先順序和相同的 STP 配置（例如 path-cost、priority、edge）。

:::

:::info
如果雙連線 bond 介面未連線到任何其他 RSTP/MSTP 網橋或交換器，可以在兩臺 MLAG 節點的該介面上設定 `edge=yes`。

此設定允許 bond 埠快速進入轉發狀態，有助於在 MLAG 一側再次可用時減少封包丟失。

:::

在此示例中，client-bond 介面使用 VLAN 10 承載未標記流量（透過 `pvid=10` 設定），並且我們還希望允許帶標籤的 VLAN 20。為確保兩個 VLAN 的流量都能在 MLAG 裝置之間透過，我們需要在兩臺 MLAG 節點上將 peer 埠新增為 VLAN 10 和 20 的帶標籤成員。重要的是，要將 peer 埠包含在其他網橋埠使用的所有 VLAN 中。這包括未標記和帶標籤的 VLAN。以下是兩臺對等裝置的配置命令：

```ros
# Peer1
/interface/bridge/vlan
add bridge=bridge1 tagged=sfp-sfpplus1 vlan-ids=10
add bridge=bridge1 tagged=sfp-sfpplus1,client-bond vlan-ids=20

# Peer2
/interface/bridge/vlan
add bridge=bridge1 tagged=sfp-sfpplus1 vlan-ids=10
add bridge=bridge1 tagged=sfp-sfpplus1,client-bond vlan-ids=20
```

:::danger
網橋從埠使用的所有 VLAN 也必須為 peer-port 配置為帶標籤 VLAN，以便 peer-port 成為這些 VLAN 的成員並能夠轉發資料。

:::

最後，檢查對等裝置上的 MLAG 狀態，並確保用戶端 LACP 的兩個介面均處於活動狀態。

```ros
# Peer1
[admin@Peer1] > /interface/bridge/monitor [find name=bridge1]
                  state: enabled                 
    current-mac-address: B8:69:F4:1B:B0:7C       
              bridge-id: 0x1000.B8:69:F4:1B:B0:7C
            root-bridge: yes                     
         root-bridge-id: 0x1000.B8:69:F4:1B:B0:7C
         root-path-cost: 0                       
              root-port: none                    
             port-count: 2                       
  designated-port-count: 2                       
           fast-forward: no                      
             mlag-state: connected               
       mlag-active-role: primary  

# Peer2
[admin@Peer2] > /interface/bridge/monitor [find name=bridge1]
                  state: enabled                 
    current-mac-address: B8:69:F4:1B:B0:7C       
              bridge-id: 0x1000.B8:69:F4:1B:B0:7C
            root-bridge: yes                     
         root-bridge-id: 0x1000.B8:69:F4:1B:B0:7C
         root-path-cost: 0                       
              root-port: none                    
             port-count: 2                       
  designated-port-count: 1                       
           fast-forward: no                      
             mlag-state: connected               
       mlag-active-role: secondary    

# Client
[admin@Client] > /interface/bonding/monitor bond1 
                    mode: 802.3ad
            active-ports: sfp-sfpplus1,sfp-sfpplus2
          inactive-ports: 
          lacp-system-id: 74:4D:28:7B:7F:96
    lacp-system-priority: 65535
  lacp-partner-system-id: B8:69:F4:1B:B0:7C

```

如果 **Client** 裝置是 RouterOS，以下是建立常規 [繫結](./bonding.md#8023ad) 的配置命令。為加快 LACP 鏈路建立，請使用 1 秒的 LACPDU 傳送速率：

```ros
/interface/bonding
add mode=802.3ad name=bond1 slaves=sfp-sfpplus1,sfp-sfpplus2 lacp-rate=1sec 
```

## MLAG 設定與監控 {#mlag-settings-and-monitoring}

本節介紹可用的 MLAG 設定和監控選項。

**子選單：** `/interface/bridge`

| 屬性 | 描述 |
| :-- | :-- |
| **mlag-heartbeat** (*time: 1s..10s \| none*; 預設：**00:00:05**) | 此設定控制向對等裝置傳送心跳訊息以檢查對等裝置之間連線的頻率。如果連續三個間隔未收到心跳訊息，對等裝置將記錄一條有關潛在通訊問題的警告。如果設定為 `none`，則完全不傳送心跳訊息。 |
| **mlag-peer-port**  (*interface \| bond;* 預設：**none**) | 將用作 peer 埠的介面。兩臺對等裝置透過這些 peer 埠進行跨機箱通訊，以建立 MLAG 並更新主機表。  peer 埠可以配置為單個乙太網介面或 bonding 介面。不過，建議使用 bonding 介面，因為它有助於防止單個介面故障影響連通性，尤其是在兩臺 MLAG 節點仍處於執行狀態時。  建議將 peer 埠使用的未標記 VLAN 與網路其餘部分隔離：可以為 peer 埠分配專用的未標記 VLAN（使用 `pvid`），或將其設定為僅允許帶 VLAN 標籤的幀（使用 `frame-types=admit-only-vlan-tagged`）。  網橋從埠使用的所有 VLAN 也必須在 `/interface/bridge/vlan` 表中為 peer-port 配置為帶標籤 VLAN，以便 peer-port 成為這些 VLAN 的成員並能夠轉發資料。 |
| **mlag-priority** (*integer: 0..128;* 預設：**128**) | 此設定更改選擇主 MLAG 節點的優先順序。數值越低表示優先順序越高。如果兩臺 MLAG 節點優先順序相同，則網橋 MAC 地址最低的一臺將成為主裝置。 |

使用 `/interface/bridge/monitor` 命令檢視當前 MLAG 狀態和活動角色。

```ros
 [admin@Peer1] > /interface/bridge/monitor [find name=bridge1]
                  state: enabled                 
    current-mac-address: B8:69:F4:1B:B0:7C       
              bridge-id: 0x1000.B8:69:F4:1B:B0:7C
            root-bridge: yes                     
         root-bridge-id: 0x1000.B8:69:F4:1B:B0:7C
         root-path-cost: 0                       
              root-port: none                    
             port-count: 2                       
  designated-port-count: 2                       
           fast-forward: no                      
             mlag-state: connected               
       mlag-active-role: primary   
```

| 屬性 | 描述 |
| :-- | :-- |
| **mlag-state** (*connected \| connecting \| disabled*) | MLAG 狀態。 |
| **mlag-active-role** (*primary \| secondary*) | 具有最低 `priority` 的對等裝置將充當主裝置。如果優先順序相同，則網橋 MAC 地址最低的對等裝置將成為主裝置。主裝置的 `system-id` 用於傳送 (R/M)STP BPDU 網橋標識和 LACP 系統 ID。 |

**子選單：** `/interface/bonding`

| 屬性 | 描述 |
| :-- | :-- |
| **mlag-id** (*integer: 0..4294967295*; 預設：) | 更改 bonding 介面的 MLAG ID。兩臺對等裝置應使用相同的 MLAG ID，以便為用戶端裝置成功建立單個 LAG。不應為 `mlag-peer-port` 配置 MLAG ID。 |

可以使用 `monitor` 和 `monitor-slaves` 命令監控 LACP bonding 介面和 bonding 從埠。更多詳情請參閱 [Bonding 監控](./bonding.md#bonding-monitoring)。
