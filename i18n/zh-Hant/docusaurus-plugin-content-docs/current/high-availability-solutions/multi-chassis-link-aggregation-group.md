---
sidebar_key: "high-availability-solutions/multi-chassis-link-aggregation-group"
sidebar_position: 3
title: "多機箱鏈路聚合組"
sidebar_label: "多機箱鏈路聚合組"
description: "RouterOS 中的 MLAG 透過在兩個裝置上配置 LACP bond 來實現物理冗餘，讓用戶端感知到單一連線，同時確保故障切換。它使用 ICCP 進行對等通訊，支援 STP 協定，並且需要在專用埠上進行謹慎的 VLAN 配置。MLAG 在大型網路中會大量佔用 CPU，並且與 L3 hardware offloading 不相容。"
tags:
  - 'mlag'
  - 'bridge-configuration'
  - 'stp'
source: https://manual.mikrotik.com/docs/high-availability-solutions/multi-chassis-link-aggregation-group
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 簡介 {#introduction}

RouterOS 中的 MLAG（多機箱鏈路聚合組）實現允許在兩臺獨立裝置上配置 LACP bond，而用戶端裝置會認為自己連線的是同一臺機器。這在交換器故障時提供物理冗餘。

兩臺對等裝置都會建立 MLAG 介面，並透過 `mlag-peer-port` 使用 ICCP（Inter Chassis Control Protocol）更新網橋主機表。RouterOS ICCP 不需要 IP 配置；它會發送未標記的 Layer2 封包，這些封包標記為 EtherType 0x88B5，目的 MAC 地址為 01:80:C2:00:00:0E。ICCP 封包屬於鏈路本地流量，這意味著它們始終由 MLAG 裝置自身接收和處理，絕不會轉發到網路的其他部分。每臺 MLAG 裝置上的 peer-port 必須彼此直接連線。還建議將 peer 埠使用的未標記 VLAN 與網路其餘部分隔離：可以為 peer 埠分配專用的未標記 VLAN（使用 `pvid`），或將其設定為僅允許帶 VLAN 標籤的幀（使用 `frame-types=admit-only-vlan-tagged`）。peer 埠可以配置為單個乙太網介面或 bonding 介面。不過，建議使用 bonding 介面，因為它有助於防止單個介面故障影響連通性，尤其是在兩臺 MLAG 節點仍處於執行狀態時。

當 mlag-peer-port 正常執行且 ICCP 建立後，將進行主裝置選舉並選出 system-id。優先順序最低的對等裝置將充當主裝置。如果優先順序相同，則網橋 MAC 地址最低的對等裝置將成為主裝置。此 system-id 用於 STP BPDU 網橋標識和 LACP 系統 ID。MLAG 支援 STP、RSTP 或 MSTP 協定。在兩臺節點的雙連線網橋埠上使用相同的 STP 優先順序和相同的 STP 配置。當 MLAG 網橋被選舉為 STP 根橋時，兩臺裝置都會在網橋監控中顯示為根橋。

:::info
MLAG 按橋接介面進行配置。任何 RouterOS 裝置（包括虛擬 CHR 例項）都可以用作 MLAG 節點。

橋接硬體解除安裝 MLAG 僅在[配備 Marvell Prestera 交換器的 MikroTik 裝置](../bridging-and-switching/marvell-prestera-switch-chip-features.md)上可用。所有其他裝置僅支援軟體形式的 MLAG。
:::

:::info
MLAG 與 [L3 硬體解除安裝](../bridging-and-switching/l3-hardware-offloading.md) 不相容。使用 MLAG 時，必須在整個交換器上停用 L3 hardware offloading（`/interface/ethernet/switch/set 0 l3-hw-offloading=no`）。僅在單個交換器埠上設定 `l3-hw-offloading=no` 是不夠的。
:::

:::danger
在包含大量主機和 VLAN 的網路中，MLAG 主機同步可能會大量佔用 CPU 和記憶體。對於使用單核 **MIPSBE CPU** 的交換器（例如 CRS326-24S+2Q+RM、CRS354-48P-4S+2Q+RM、CRS518-16XS-2XQ-RM），建議僅在最多 1,000 臺主機的網路中使用 MLAG。

在主機數量更多的網路中，這些交換器上的 MLAG 可能導致意外行為。

:::

![](/img/5b5134db602c21b1.png)

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

![](/img/bd07685ca17e6836.png)為 **Peer1** 和 **Peer2** 裝置配置用於 MLAG 的 bonding 介面，在兩臺對等裝置上使用匹配的 `mlag-id` 設定，並將 LACPDU 傳送速率設定為 1 秒：

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

有多個與 MLAG 相關的設定和監控選項：來自 `interface/bridge` 選單的 [`mlag-heartbeat`](../cli-reference/interface/bridge/index.md#mlag-heartbeat)、[`mlag-init-delay`](../cli-reference/interface/bridge/index.md#mlag-init-delay)、[`mlag-lacp-fallback`](../cli-reference/interface/bridge/index.md#mlag-lacp-fallback)、[`mlag-peer-port`](../cli-reference/interface/bridge/index.md#mlag-peer-port)、[`mlag-priority`](../cli-reference/interface/bridge/index.md#mlag-priority)，以及來自 `interface/bonding` 選單的 [`mlag-id`](./bonding.md#mlag-id)。

預設情況下，MLAG 使用當選主節點的系統 ID 作為共享系統 ID，同時用於 RSTP 橋 ID 和雙連線聚合鏈路的 LACP 系統 ID。如果主節點重啟，剩餘的輔助節點會將其聚合鏈路恢復為自己的 LACP 系統 ID（請參閱 [`mlag-lacp-fallback`](../cli-reference/interface/bridge/index.md#mlag-lacp-fallback)）。然後 LACP 對端必須重新協商聚合鏈路，從而導致短暫的封包丟失。

考慮設定 `mlag-lacp-fallback=no`，以在對等鏈路丟失後保留共享的 MLAG 系統 ID，從而避免 LACP 重新協商。主節點必須重新加入叢集才能恢復共享系統 ID。

當節點加入或重新加入叢集時，其雙連線聚合從介面會保持不加入 802.3ad 聚合鏈路，直到 MLAG 系統 ID 與對等節點同步。[`mlag-init-delay`](../cli-reference/interface/bridge/index.md#mlag-init-delay) 控制重啟後從介面保持排除狀態的時長，防止聚合鏈路在短暫時間內使用本地系統 ID 啟用。

使用 `/interface/bridge/monitor` 命令檢視當前 MLAG 狀態和活動角色。`mlag-state` 欄位在 ICCP 建立後顯示 `connected`，在對等節點建立或重新建立連線期間顯示 `connecting`，或者當配置的對等埠不可用時顯示諸如 `peer port not running` 之類的錯誤。

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

可以使用 `monitor` 和 `monitor-slaves` 命令監控 LACP bonding 介面和 bonding 從埠。更多詳情請參閱 [Bonding 監控](./bonding.md#bonding-monitoring)。
