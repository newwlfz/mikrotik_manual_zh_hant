---
title: "Spanning Tree Protocol"
description: "本頁說明 MikroTik RouterOS 中的 Spanning Tree Protocol (STP)，詳細介紹如何透過選取根橋接器來避免網路迴圈，並使用 Bridge Protocol Data Units (BPDUs) 最佳化埠使用。本文強調在較大型網路中進行手動設定，並提供監控指令，以檢查橋接器與埠上的 STP 狀態。"
tags:
  - 'spanning-tree'
  - 'stp'
  - 'rstp'
source: https://manual.mikrotik.com/docs/7.24/bridging-and-switching/user-guides/spanning-tree-protocol
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

---

生成樹協定的目的，是在具有冗餘連結的情況下，仍能建立無迴圈的 Layer 2 拓撲。當連接多個橋接器，或只是交互連接橋接器埠時，可能會產生網路迴圈，並嚴重影響網路穩定性。生成樹協定透過引入根橋接器的概念來解決這個問題。同一 Layer 2 網域中的所有橋接器都會交換通往根橋接器最短路徑的資訊。之後，每個橋接器會協商要使用哪些埠來到達根橋接器。這項資訊交換是透過 Bridge Protocol Data Units（BPDU）完成。STP 會停用每個橋接器上的特定埠以避免迴圈，同時仍確保所有橋接器都能彼此通訊。如需協定的詳細說明，請參閱 IEEE 802.1D。

最佳做法是，一律建議手動設定每個橋接器的 priority、連接埠 priority 與連接埠 path cost，以確保 Layer2 隨時正常運作。對於由 1 至 2 個啟用 (R/M)STP 的橋接器所組成的網路，將 STP 相關值保持為預設值是可以接受的，但對於較大的網路，強烈建議手動設定這些值。由於 STP 會檢查網路中橋接器的 STP 相關值來選出根橋接器與根埠，若將 STP 設定保持為自動，可能會選出非預期的根橋接器與根埠，並在硬體故障時導致網路無法存取。

:::info
RouterOS bridge 不適用於 PVST 及其變體。PVST BPDU（MAC 目的地為 01:00:0C:CC:CC:CD）會被 RouterOS bridge 視為一般多播封包。簡單來說，它們會經過 RouterOS bridge/switch 轉送邏輯，並可能加上標籤或移除標籤。
:::

## 監控 {#monitoring}

---

你可以使用 `/interface/bridge/monitor` 指令檢查橋接器的 STP 狀態，例如：

```ros
/interface/bridge/monitor bridge1
                    state: enabled                         
      current-mac-address: 74:4D:28:6F:31:10               
                bridge-id: 0x8000.74:4D:28:6F:31:10        
              root-bridge: no                              
           root-bridge-id: 0.74:4D:28:11:70:6B             
  regional-root-bridge-id: 0.74:4D:28:11:70:6B             
           root-path-cost: 0                               
                root-port: combo1                          
               port-count: 2                               
    designated-port-count: 0                               
        mst-config-digest: 4e22fbb9ede77faa45ec995c4ffa8085
             fast-forward: no                              
         multicast-router: yes                             
             igmp-querier: none                            
              mld-querier: none                            
        declared-vlan-ids: 1                               
      registered-vlan-ids: 1      
```

請注意，根橋接器沒有任何根埠，只有指定埠。

你可以使用 `/interface/bridge/port/monitor` 指令檢查橋接器埠的 STP 狀態，例如：

```ros
/interface/bridge/port/monitor [find interface=combo1]
                  interface: combo1             
                     status: in-bridge          
                    port-id: 0x80.1             
                       role: root-port          
                  edge-port: no                 
        edge-port-discovery: yes                
        point-to-point-port: yes                
               external-fdb: no                 
               sending-rstp: yes                
                   learning: yes                
                 forwarding: yes                
           actual-path-cost: 2000               
    internal-root-path-cost: 2000               
       designated-bridge-id: 0.74:4D:28:11:70:6B
   designated-internal-cost: 0                  
         designated-port-id: 0x80.1             
  designated-remaining-hops: 20                 
                 bpdu-tx-rx: 3/7791             
        discard-transitions: 0                  
        forward-transitions: 1                  
                   tc-tx-rx: 2/2                
           topology-changes: 1                  
       last-topology-change: 4h19m43s           
           multicast-router: no                 
           hw-offload-group: switch1            
          declared-vlan-ids: 1                  
                             100                
        registered-vlan-ids: 1                  
                             100                
                             200-203     
```

請注意，`root-bridge-id` 由橋接器 priority 與橋接器的 MAC 位址組成；對於非根橋接器，根橋接器會顯示為 `designated-bridge`。

:::warning
當橋接器設定為使用 802.1Q 作為 EtherType 時，會將 BPDU 傳送至 01:80:C2:00:00:00，這些 BPDU 由 MSTP、RSTP 與 STP 使用。當使用 802.1ad 作為橋接器 VLAN 協定時，BPDU 與 802.1Q 橋接器不相容，且會傳送至 01:80:C2:00:00:08。若 Layer2 網路中的橋接器 VLAN 協定不同，(R/M)STP 將無法正常運作。
:::

## STP 與 RSTP {#stp-and-rstp}

---

STP 與 Rapid STP 廣泛用於許多網路，但幾乎所有網路都已改用僅使用 RSTP，因為它具有優勢。STP 是非常舊的協定，收斂時間（完整學習網路拓撲變更並繼續正確轉送流量所需的時間）最長可達 50 秒。RSTP 的收斂時間短得多，只需幾秒甚至幾毫秒。建議使用 RSTP 而非 STP，因為它快得多，也向後相容 STP。RSTP 較快的原因之一是可能的埠狀態較少，以下是可能的 STP 埠狀態清單：

- **Forwarding** - 埠參與流量轉送並學習 MAC 位址，且正在接收 BPDU。
- **Listening** - 埠不參與流量轉送且不學習 MAC 位址，但正在接收 BPDU。
- **Learning** - 埠不參與流量轉送，但正在學習 MAC 位址。
- **Blocking** - 埠因為會造成迴路而被封鎖，但正在接收 BPDU。
- **Disabled** - 埠已停用或未作用。

在 RSTP 中，disabled、listening 與 blocking 埠狀態已由單一狀態取代，稱為 **Discarding** 狀態：

- **Forwarding** - 埠參與流量轉送並學習 MAC 位址且正在接收 BPDU（forwarding=yes）。
- **Learning** - 埠不參與流量轉送但正在學習 MAC 位址（learning=yes）。
- **Discarding** - 埠不參與流量轉送且不學習 MAC 位址且正在接收 BPDU（forwarding=no）。

在 STP 中，埠主要依狀態分類（例如 Forwarding、Listening、Learning、Blocking、Disabled）。埠行為會根據生成樹演算法動態決定，但不會明確指派角色。轉送或封鎖流量的邏輯衍生自 Root Bridge、Root Ports 與 Designated Ports 的計算，但這些被視為生成樹拓撲的一部分，而非正式化的埠角色。RSTP 明確定義埠角色，並引入備援路徑的概念，透過 Alternate Port 與 Backup Port 角色明確表示。這些角色在 STP 中並不存在，因為 STP 一律將封鎖的埠視為相同，不區分其作為潛在備援的功能。

以下是 RSTP 協定的埠角色說明：

- **Root Port** - 面向 root bridge 且通往 root bridge 路徑最佳（成本最低）的埠。每座 bridge 只會選出一個 root port（root bridge 本身除外）。
- **Designated Port** - 背向 root bridge 的埠，並將流量從 root bridge 轉送至下游設備。
- **Alternate Port** - 面向 root bridge 但不會轉送流量的埠。當目前的 root port 故障時，此埠提供通往 root bridge 的備援路徑。
- **Backup Port** - 背向 root bridge 但不會轉送流量的埠。此埠作為同一區段上 designated port 的備援。
- **Disabled Port** - 已停用或非作用中的埠。

在 STP 中，bridge 之間的連線狀態是透過相鄰 bridge 之間傳送與接收 BPDU 來決定。Designated port 會將 BPDU 傳送至 root port。若連續 3 次 **HelloTime** 都未收到 BPDU，則該連線會被視為不可用，並開始進行網路拓撲收斂。在某些情境下，可透過縮短 `forward-delay` 計時器來降低 STP 收斂時間，該計時器負責控制埠可停留在 learning/listening 狀態的時間。

在 RouterOS 中，可以指定哪些 bridge port 是 edge port。Edge port 是不應該接收任何 BPDU 的埠。這很有用，因為這可讓 STP 略過 learning 與 listening 狀態，直接進入 forwarding 狀態。這項功能有時稱為 **PortFast**。你可以將此參數保持為預設值 **auto**，也可以手動指定。對於後方不應該再有 bridge 的埠，可以手動將其設為 edge port。這些通常是 access port。

此外，bridge port 的 `point-to-point` 會指定 bridge port 是否透過點對點連結連接到 bridge，以便在故障時更快收斂。將此屬性設為 `yes` 會強制該連結為點對點連結，這會略過檢查機制，該機制會偵測並等待來自此單一連結上其他設備的 BPDU。將此屬性設為 `no` 表示該連結可能接收來自多台設備的 BPDU。將此屬性設為 `yes` 可大幅改善 (R/M)STP 收斂時間。一般而言，只有在連結之間可能連接其他設備時，才應將此屬性設為 `no`。這主要與無線媒介和 Ethernet hub 有關。若 Ethernet 連結為全雙工，`auto` 會啟用點對點功能。當 `protocol-mode` 設為 `none` 時，此屬性沒有作用。

### 預設值 {#default-values}

建立 bridge 或將埠加入 bridge 時，RouterOS 會指派下列預設值：

- 預設 bridge priority：**32768** / **0x8000**
- 預設 bridge port path cost：**based on interface speed**
- 預設 bridge port priority：**0x80**
- BPDU message age increment：**1**
- HelloTime：**2**
- 預設 max message age：**20**

bridge 介面設定 `port-cost-mode` 會變更 bridge port 的 `path-cost` 與 `internal-path-cost` 模式，並根據介面速度使用自動值。此設定不會影響已手動設定 `path-cost` 或 `internal-path-cost` 屬性的 bridge port。以下範例說明特定資料速率所對應的 path-cost（中間速率按比例計算）：

| 資料速率 | Long | Short |
| :-- | :-- | --: |
| 10 Mbps | 2,000,000 | 100 |
| 100 Mbps | 200,000 | 19 |
| 1 Gbps | 20,000 | 4 |
| 10 Gbps | 2,000 | 2 |
| 25 Gbps | 800 | 1 |
| 40 Gbps | 500 | 1 |
| 50 Gbps | 400 | 1 |
| 100 Gbps | 200 | 1 |

對於 bonded 介面，會套用所有 bonded 成員埠中最高的 `path-cost`，此值不會受到 bonding 總連結速度的影響。對於虛擬介面（例如 VLAN、EoIP、VXLAN），以及 wifi、wireless 和 60GHz 介面，long 模式會指派 `path-cost` 20,000，short 模式則指派 10。對於動態橋接的介面（例如 wifi、wireless、PPP、VPLS），`path-cost` 在 long 模式下預設為 20,000，在 short 模式下預設為 10。不過，將介面動態新增至 bridge 的服務可以手動覆寫此值，例如使用 CAPsMAN `datapath.bridge-cost` 設定。7.13 之前的 RouterOS 版本不會根據連結速度變更埠的路徑成本，對於 10M、100M、1000M 和 10000M 連結速度，埠新增至 bridge 時的預設路徑成本值一律為 **10**。

BPDU 的年齡取決於 BPDU 經過的 bridge 數量乘以訊息年齡，因為 RouterOS 使用 **1** 作為訊息年齡增量，所以 BPDU 封包可通過的 bridge 數量上限由 `max-message-age` 參數指定。預設值為 **20**。這表示在第 20 個 bridge 之後，BPDU 封包將被捨棄，而下一個 bridge 會成為 root bridge。請注意，若設定 `max-message-age=20`，則很難預測第 21 個 bridge 上哪些埠會成為 designated port，並可能導致流量無法正確轉送。

:::warning
若使用 bridge filter 規則，請務必允許具有 DST-MAC 位址 **01:80:C2:00:00:00** 的封包，因為這些封包攜帶 BPDU，對 STP 正常運作至關重要。
:::

### 選舉程序 {#election-process}

若要正確設定網路中的 STP，您需要瞭解選舉程序，以及各參數參與的順序。在 RouterOS 中，root bridge 會依下列特定順序，根據最小的 priority 與最小的 MAC 位址選出：

1. Bridge priority（最低）。
2. Bridge MAC 位址（最低）。

在 RouterOS 中，root port 會依下列特定順序，根據最低的 Root port 路徑成本、最低的 bridge identifier 與最低的 bridge port ID 選出：

1. Root port path cost（最低）
2. Bridge identifier（最低）
3. Bridge port ID（最低）

首先，當設備考慮要將哪個連接埠選為 root port 時，會檢查其連接埠所見的 **root path cost**。如果兩個或多個連接埠的 root path cost 相同，則會檢查 **上游**設備的 **Bridge identifier**，連接到最低 bridge identifier 的連接埠將成為 root port。如果在兩個或多個連接埠上看到相同的 bridge identifier，則會檢查 **上游**設備的 **Bridge port ID**。

## 屬性說明 {#explanation-of-attributes}

Root path cost：所有 bridge 都有 Root Path Cost。root bridge 的 root path cost 為 0。對於其他所有 Bridge，它是通往 Root Bridge 的最低成本路徑上所有 Port Path Costs 的總和。你可以在 `/interface/bridge/port` 下修改本機連接埠的路徑成本。
bridge identifier 是「bridge priority」與「bridge MAC」的組合，可在 `/interface/bridge` 下設定。

Bridge port ID 是「unique ID」與「bridge port priority」的組合。unique ID 會在將 bridge port 加入 bridge 時自動指派。它無法編輯。你可以在 WinBox 的「Bridge Port」的「Port Number」欄位中查看，或使用 `/interface/bridge/port/monitor` 並以 `port-number` 查看。

:::tip 瞭解 STP 連接埠選舉
請務必將路徑成本與優先順序套用到正確的連接埠：

- **Path Cost** 會影響朝向 root bridge 的連接埠。（在 root bridge 連接埠上設定路徑成本沒有作用）。
- **Port Priority** 會影響遠離 root bridge 的連接埠。
- **Bridge Identifier** 不會影響設備自身的 root port 選舉；它會影響 **下游**設備的 root port 選舉。
:::

:::warning Bridge Priority 相容性
RouterOS 允許設定 0 到 65535 之間的任何 bridge priority 值。不過，IEEE 802.1W 標準嚴格要求 bridge priority 必須以 4096 為間隔。為避免與其他廠商設備不相容，請**只**使用下列優先順序值：
`0, 4096, 8192, 12288, 16384, 20480, 24576, 28672, 32768, 36864, 40960, 45056, 49152, 53248, 57344, 61440`
:::

### 範例 {#examples}

#### 根路徑成本範例 {#root-path-cost-example}

![Root Path](/img/3683697e750a8f2f.webp)

此範例說明根路徑成本的運作方式。SW1 將成為根橋接器，因為其優先順序最低，為 0x1000。每個橋接器都會計算通往根橋接器的路徑成本。計算根路徑成本時，橋接器會將其埠上設定的路徑成本，加上相鄰橋接器通告的根路徑成本。

**SW1**：由於其為根橋接器，即使其設定的路徑成本為 10，仍會向相鄰裝置通告根路徑成本 0。

**SW2:****ether1** 的根路徑成本為 0 + 25=**25**。在 **ether2** 路徑上，成本為 10+10+10+0=**30**

**SW3:** **ether2** 的根路徑成本為 0 + 10=**10**。在 **ether4** 路徑上，路徑成本為 10+5+25+0=**40**

**SW4:** **ether1** 的根路徑成本為 0+25+5=**30**。在 **ether4** 上，路徑成本為 10+10+0=**20**。

路徑成本最低的埠將被選為根埠。STP 拓撲中的每個橋接器都需要一條通往根橋接器的路徑。找到最佳路徑後，多餘的路徑將被封鎖，在此範例中，即 SW2 與 SW4 之間的路徑。

:::warning
您可以在根橋接器上設定路徑成本，但只有在該橋接器失去根狀態時才會納入考量。
:::

#### STP 範例 {#stp-example}

![STP Example 1](/img/4c8bc04b481c916d.webp)

在此範例中，我們要確保 ServerA 與 ServerB 連線的 Layer2 備援。如果某個埠連接到不是橋接器且未執行 (R)STP 的設備，則該埠會被視為邊緣埠。在此情況下，ServerA 與 ServerB 連接到邊緣埠。這可透過在網路中使用 STP 來達成。以下是每部交換器的設定範例：

- SW1 的設定：

```ros
/interface/bridge
add name=bridge priority=0x1000
/interface/bridge/port
add bridge=bridge interface=ether1 priority=0x60
add bridge=bridge interface=ether2 priority=0x50
add bridge=bridge interface=ether3 priority=0x40
add bridge=bridge interface=ether4 priority=0x30
add bridge=bridge interface=ether5
```

- SW2 的設定：

```ros
/interface/bridge
add name=bridge priority=0x2000
/interface/bridge/port
add bridge=bridge interface=ether1
add bridge=bridge interface=ether2
add bridge=bridge interface=ether3
```

- SW3 的設定

```ros
/interface/bridge
add name=bridge priority=0x3000
/interface/bridge/port
add bridge=bridge interface=ether1
add bridge=bridge interface=ether2
add bridge=bridge interface=ether3
```

- SW4 的設定：

```ros
/interface/bridge
add name=bridge priority=0x4000
/interface/bridge/port
add bridge=bridge interface=ether1
add bridge=bridge interface=ether2 path-cost=20
add bridge=bridge interface=ether3
```

在此範例中，**SW1** 是根橋接器，因為它具有最低的橋接器優先權。**SW2** 與 **SW3** 的 ether1、ether2 連接到根橋接器，而 ether3 連接到 **SW4**。當所有交換器都正常運作時，流量會從 ServerA 經過 SW1\_ether2、SW2 與 SW4 流向 ServerB。若 **SW1** 發生故障，**SW2** 會因為次低優先權而成為根橋接器，如圖中的虛線所示。以下是每部交換器的埠及其角色清單：

- **root-port** - SW2\_ether2、SW3\_ether2、SW4\_ether1
- **alternate-port** - SW2\_ether1、SW3\_ether1、SW4\_ether2
- **designated-port** - SW1\_ether1、SW1\_ether2、SW1\_ether3、SW1\_ether4、SW1\_ether5、SW2\_ether3、SW3\_ether3、SW4\_ether3

:::note
**注意：** 根據 802.1Q 建議，bridge priority 應以 4096 為間隔。若要設定建議的優先順序，使用十六進位表示法會更方便，例如 0 為 0x0000，4096 為 0x1000，8192 為 0x2000，依此類推（0..F）。
:::

## 多重生成樹通訊協定 {#multiple-spanning-tree-protocol}

---

Multiple Spanning Tree Protocol（MSTP）用於 bridge 介面，以確保跨多個 VLAN 的拓撲不會產生迴圈。MSTP 也可提供 Layer2 備援，並可作為 VLAN 的負載平衡技術，因為它能夠讓不同 VLAN 使用不同路徑。MSTP 的運作方式與 (R)STP 非常相似，許多 (R)STP 的概念都可套用於 MSTP，強烈建議在使用 MSTP 前先了解 (R)STP 背後的原理，但在設計啟用 MSTP 的網路時，仍有一些差異必須納入考量。

若使用 (R)STP，BPDU 會透過 bridge 中的所有實體介面傳送，以判斷迴圈，並在連接埠造成迴圈時停止轉送流量。若某個 VLAN 內部發生迴圈，(R)STP 可能無法偵測到。部分 STP 變體會在每個 VLAN 上執行一個 STP 實例來解決此問題（PVST），但這已被證實效率不佳；另一些 STP 變體則是在所有 VLAN 上執行單一 STP 實例（CST），但無法針對每個 VLAN 或 VLAN 群組進行負載平衡。MSTP 透過 MST 實例來解決這兩個問題，MST 實例可定義一組 VLAN（VLAN mapping），用於負載平衡與備援，這表示每個 VLAN 群組都可以有不同的 root bridge 與不同的路徑。請注意，將多個 VLAN 分組到單一實例中是有益的，可減少每次網路拓撲變更所需的 CPU 週期。

:::danger
在啟用 MSTP 的 RouterOS 中，bridge priority 是 CIST 的 root bridge priority，如 IEEE 802.1Q 標準所述，bridge priority 必須以 4096 為間隔，最低 12 位元會被忽略。以下是有效的 bridge priority：0、4096、8192、12288、16384、20480、24576、28672、32768、36864、40960、45056、49152、53248、57344、61440。設定無效的 bridge priority 時，RouterOS 會發出警告，並將值截斷為有效值，但會在設定中儲存原始值，因為無效的 bridge priority 值仍可用於執行 RouterOS 的設備之間的 (R)STP，不過建議改用有效的 bridge priority。
:::

### MSTP 區域 {#mstp-regions}

MSTP 以稱為 region 的群組運作。每個 region 都會有一個 regional root bridge，而 region 之間則會選出一個 root bridge。MSTP 會使用 Internal Spanning Tree（IST）在 region 內建立網路拓撲，並使用 Common Spanning Tree（CST）在 region 外建立多個 region 之間的網路拓撲。MSTP 將這兩個協定結合為 Common and Internal Spanning Tree（CIST），其中保存 region 內與 region 之間的拓撲資訊。從 CST 的角度來看，region 看起來會像單一虛擬 bridge，因此 MSTP 被認為非常適合大規模網路擴充。若要讓 bridge 位於同一 region，其設定必須相符。BPDU 不會包含 VLAN mapping，因為其可能很大，而是傳送計算出的雜湊值。若 bridge 透過某個連接埠收到 BPDU，但設定不相符，則 MSTP 會將該連接埠視為 boundary port，並可用於連接到其他 region。以下是 MSTP 判斷 BPDU 來自同一 region 時必須相符的參數清單：

- Region name
- Region revision
- VLAN mappings to MST Instance IDs（計算出的雜湊值）

可以建立未劃分區域的 MSTP 網路，不過若要依 VLAN 群組進行負載平衡，橋接器必須從與其相連且具有相同參數的橋接器接收 BPDU。在 RouterOS 中，預設區域名稱為空，區域修訂版本為 0，這些都是有效值，但必須確保相符，才能讓多個橋接器位於同一個 MSTP 區域。若區域內的橋接器分散在網路中，則該區域無法存在；這些橋接器必須至少以一種方式相連，讓它們能在不離開區域的情況下傳送與接收 BPDU。例如，若兩台具有相同區域相關參數的橋接器之間有一台區域相關參數不同的橋接器，則會存在至少 3 個不同的 MSTP 區域。

![MSTP Topology](/img/77a9b366354f5ae5.webp)

讓每台橋接器都位於單一 MSTP 區域的缺點是會耗費過多 CPU 週期。相較之下，PVST(+) 會為網路中存在的每個 VLAN ID 建立一個 Spanning Tree Instance，由於網路中可存在的路徑非常有限，這種做法會產生大量額外負擔與不必要的 CPU 週期。這也代表這種做法的擴充性不佳，並可能讓 CPU 效能不強的交換器過載。MSTP 透過將網路劃分為 MSTP 區域來解決這個問題，在每個區域內，橋接器會交換並處理存在於同一區域內 VLAN 的資訊，但在背景執行單一 Spanning Tree Protocol 執行個體，以維護區域之間的網路拓撲。這種做法已被證實更有效率，也更具擴充性。這代表較大的網路應使用區域，以減少 CPU 週期。

在區域中，您可以定義 MST Instances，用於設定依 VLAN 群組進行的負載平衡，以及選出區域根橋接器。值得一提的是，每個區域中都存在一個預定義的 MST Instance，在大多數文件中，這被稱為 **MSTI0**。這個 MST Instance 被視為預設 MST Instance。有特定參數會套用至這個特殊的 MST Instance。當流量通過啟用 MSTP 的橋接器時，MSTP 會尋找具有相符 VLAN 對應的 MST Instance，但若某個 VLAN ID 沒有 VLAN 對應，則流量會歸屬於 **MSTI0**。

:::warning
由於 MSTP 要求橋接器介面上的 VLAN 篩選必須啟用，請確認您已在 `/interface/bridge/vlan` 中允許所有必要的 VLAN ID，否則流量將不會被轉送，且看起來可能像是 MSTP 設定錯誤，但實際上是 VLAN 篩選設定錯誤。
:::

### 選舉程序 {#election-process-1}

MSTP 中的選舉程序可分為兩個部分：區域內與區域間。為了讓 MSTP 正常運作，必須始終存在區域根，也就是區域內的根橋接器，以及 CIST 根，也就是區域之間的根橋接器。區域根是區域內的根橋接器，而區域根橋接器是正確設定區域內 VLAN 群組負載平衡所需的。CIST 根將用於設定哪些埠是 alternate/backup 埠（非作用中），以及哪些埠是 root 埠（作用中）。

:::warning
區域之間沒有依 VLAN 群組進行的負載平衡，也沒有 root 埠選舉程序，而 MSTP 區域之間的埠區塊處理方式與 (R)STP 相同。若 CIST 已封鎖 MSTP 區域內的某個埠，以防止 MSTP 區域之間發生流量迴圈，則該埠仍可對 IST 保持作用中，以在 MSTP 區域內進行依 VLAN 群組的負載平衡。
:::

- 下列參數會參與選出 MSTP 區域內的區域根橋接器或 root 埠：

| 屬性 | 說明 |
| :-- | :-- |
| **priority** (*integer: 0..65535 decimal format or 0x0000-0xffff hex format*; Default: **32768 / 0x8000**) | `/interface/bridge/msti`，MST Instance 優先順序，用於在 MSTP 區域內選出區域根橋。必須以 4096（0x1000）為步長設定；最低 12 位元會被忽略。有效值：0x0000、0x1000、0x2000、...、0xf000（或十進位對應值：0、4096、8192、...、61440）。 |
| **internal-path-cost** (*integer: 1..200000000*; Default: ) | `/interface/bridge/port`，未知 VLAN ID（MSTI0）通往區域根橋的路徑成本，用於 MSTP 區域內的根埠。 |
| **priority** (*0x00 \| 0x10 \| 0x20 \| 0x30 \| 0x40 \| 0x50 \| 0x60 \| 0x70 \| 0x80 \| 0x90 \| 0xa0 \| 0xb0 \| 0xc0 \| 0xd0 \| 0xe0 \| 0xf0*; Default: **0x80**) | `/interface/bridge/port/mst-override`，已定義 MST Instance 的 MST 埠優先順序，用於區域根橋上的橋接埠。必須以 16（0x10）為步長設定。 |
| **internal-path-cost** (*integer: 1..200000000*; Default: ) | `/interface/bridge/port/mst-override`，已定義 MST Instance 的 MST 埠路徑成本，用於 MSTP 區域內的非根橋接埠。 |

- 下列參數會參與選出 CIST 根橋或 CIST 根埠：

| 屬性 | 說明 |
| :-- | :-- |
| **priority** (*integer: 0..65535 decimal format or 0x0000-0xffff hex format*; Default: **32768 / 0x8000**) | `/interface/bridge`，CIST 橋接優先順序，用於選出 CIST 根橋。必須以 4096（0x1000）為步長設定；最低 12 位元會被忽略。 |
| **priority** (*0x00 \| 0x10 \| 0x20 \| 0x30 \| 0x40 \| 0x50 \| 0x60 \| 0x70 \| 0x80 \| 0x90 \| 0xa0 \| 0xb0 \| 0xc0 \| 0xd0 \| 0xe0 \| 0xf0*; Default: **0x80**) | `/interface/bridge/port`，CIST 埠優先順序，用於 CIST 根橋上選出 CIST 根埠。必須以 16（0x10）為步長設定。 |
| **path-cost** (*integer: 1..200000000*; Default: ) | `/interface/bridge/port`，CIST 埠路徑成本，用於 CIST 非根橋接埠選出 CIST 根埠。 |

:::warning
MSTP 檢查參數以選出根橋／埠的順序與 (R)STP 相同，你可以在 (R)STP Election Process 一節中閱讀更多相關資訊。
:::

### MST 執行個體 {#mst-instance}

**子選單：** `/interface/bridge/msti`

本節用於將多個 VLAN ID 分組為單一 instance，以便在 MSTP 區域內為每個 VLAN 群組建立不同的根橋。

| 屬性 | 說明 |
| :-- | :-- |
| **bridge** (*text*; Default: ) | 指派 MST instance 的橋接器。 |
| **identifier** (*integer: 1..31*; Default: ) | MST instance 識別碼。 |
| **priority** (*integer: 0..65535 decimal format or 0x0000-0xffff hex format*; Default: **32768 / 0x8000**) | MST instance 優先順序，用於判斷 MSTP 區域中一組 VLAN 的根橋。 |
| **vlan-mapping** (*integer: 1..4094*; Default: ) | 要指派給 MST instance 的 VLAN ID 清單。此設定接受 VLAN ID 範圍，以及以逗號分隔的值。例如：`vlan-mapping=100-115,120,122,128-130` |

### MST 覆寫 {#mst-override}

**子選單：** `/interface/bridge/port/mst-override`

本節用於為 MSTP 區域內的每個 VLAN 對應選擇所需的路徑。

| 屬性 | 說明 |
| :-- | :-- |
| **disabled** (*yes \| no*；預設：**no**) | 此項目是否停用。 |
| **internal-path-cost** (*integer: 1..200000000*；預設： ) | MST instance 的 VLAN 對應路徑成本，用於朝向 root bridge 的 VLAN，以操控路徑選擇；路徑成本越低越優先。 |
| **identifier** (*integer: 1..31*；預設： ) | MST instance 識別碼。 |
| **priority** (*integer: 0..240*；預設：**128**) | MST instance 的 VLAN 優先順序，用於遠離 root bridge 的 VLAN，以操控路徑選擇；優先順序越低越優先。 |
| **interface** (*name*；預設： ) | 要使用所設定 MST instance 的 VLAN 對應，以及已定義路徑成本與優先順序的埠名稱。 |

### 監控 {#monitoring-1}

與 (R)STP 類似，也可以監控 MSTP 狀態。透過監控 bridge 介面本身，可以查看目前的 CIST root bridge 與 MSTI0 目前的區域 root bridge。也可以查看 MST Instance 識別碼與 VLAN 對應的計算雜湊值。這在確認特定 bridge 是否位於同一個 MSTP 區域時很有用。以下為監控 MSTP bridge 的範例：

```ros
/interface/bridge/monitor bridge
                    state: enabled
      current-mac-address: 6C:3B:6B:7B:F0:AA
                bridge-id: 0x8000.6C:3B:6B:7B:F0:AA 
              root-bridge: no
           root-bridge-id: 0x1000.64:D1:54:24:23:72
  regional-root-bridge-id: 0x4000.6C:3B:6B:7B:F0:AA
           root-path-cost: 10
                root-port: ether4
               port-count: 5
    designated-port-count: 3
        mst-config-digest: 74edbeefdbf82cf63a70cf60e43a56f3
             fast-forward: no                              
         multicast-router: yes                             
             igmp-querier: none                            
              mld-querier: none                            
        declared-vlan-ids: 1                               
      registered-vlan-ids: 1
```

在 MSTP 中，可以監控 MST Instance。這有助於判斷特定 MST Instance 與 VLAN 群組目前的區域 root bridge。以下為監控 MST Instance 的範例：

```ros
/interface/bridge/msti/monitor 1
                    state: enabled
               identifier: 2
      current-mac-address: 6C:3B:6B:7B:F0:AA
                bridge-id: 0x8000.6C:3B:6B:7B:F0:AA
              root-bridge: no
           root-bridge-id: 0.00:00:00:00:00:00
  regional-root-bridge-id: 0x1002.6C:3B:6B:7B:F9:08
           root-path-cost: 0
                root-port: ether2
               port-count: 5
    designated-port-count: 1
```

也可以監控特定 MST Override 項目。這有助於在 MSTP 區域中設定 root port 與 alternate/backup port 時，判斷特定 MST Instance 的埠角色。以下為監控 MST Override 項目的範例：

```ros
/interface/bridge/port/mst-override/monitor 1
                      port: ether3
                    status: active
                identifier: 2
                   port-id: 0x80.1     
                      role: alternate-port
                  learning: no
                forwarding: no
   internal-root-path-cost: 15
         designated-bridge: 0x1002.6C:3B:6B:7B:F9:08
  designated-internal-cost: 0
        designated-port-id: 0x80.1  
 designated-remaining-hops: 20                      
                tx-rx-bpdu: 3/7991                  
       discard-transitions: 0                       
       forward-transitions: 1                       
                  tx-rx-tc: 2/2                     
          topology-changes: 1                       
```

### MSTP 範例 {#mstp-example}

假設我們需要設計一個拓撲，並以這樣的方式設定 MSTP：VLAN 10,20 會經由一條路徑轉送，而 VLAN 30,40 會經由另一條路徑轉送，其他所有 VLAN ID 則會經由其中一條路徑轉送。這可以透過設定 MST Instances 並指派埠路徑成本來輕鬆完成。以下是一個網路拓撲範例，需要針對 VLAN 群組進行負載平衡，並分為 3 個獨立區域：

![MSTP Example](/img/27652a7629c4268f.webp)

啟用 MSTP 的網路拓撲，針對 VLAN 群組進行負載平衡

首先將每個介面加入 bridge。一開始，請建立一個未啟用 VLAN 過濾的 (R)STP bridge，以避免失去對 CPU 的存取。此範例中的每台設備都以其所在區域 (Rx) 和設備編號 (\_x) 命名。對於較大的網路，由於連結與設備數量眾多，設定 MSTP 可能會令人混淆。我們建議使用 The Dude 監控及設計網路拓撲。

- 在 **R1\_1**、**R1\_3**、**R2\_1**、**R2\_3**、**R3\_1**、**R3\_3** 上使用下列指令：

```ros
/interface/bridge
add name=bridge protocol-mode=rstp vlan-filtering=no
/interface/bridge/port
add bridge=bridge interface=ether1
add bridge=bridge interface=ether2
add bridge=bridge interface=ether3
add bridge=bridge interface=ether4
```

- 在 **R1\_2**、**R2\_2**、**R3\_2** 上使用下列指令。

```ros
/interface/bridge
add name=bridge protocol-mode=rstp vlan-filtering=no
/interface/bridge/port
add bridge=bridge interface=ether1
add bridge=bridge interface=ether2
```

- 請確認這些設備上允許所需的 VLAN ID。在這裡，我們假設每台設備都會接收需要依 VLAN 群組進行負載平衡的標記流量。在 **R1\_1**、**R1\_3**、**R2\_1**、**R2\_3**、**R3\_1**、**R3\_3** 上使用下列指令：

```ros
/interface/bridge/vlan
add bridge=bridge tagged=ether1,ether2,ether3,ether4 vlan-ids=10,20,30,40
```

- 在 **R1\_2**、**R2\_2**、**R3\_2** 上使用下列指令：

```ros
/interface/bridge/vlan
add bridge=bridge tagged=ether1,ether2 vlan-ids=10,20,30,40
```

:::warning
請務必將所有需要的 VLAN ID 與埠加入 bridge VLAN 表，否則設備將不會轉送所有必要的 VLAN，及/或您將失去對設備的存取。
:::

我們需要為每個要位於同一個 MSTP region 的 bridge 指派 region 名稱。您也可以指定 region revision，但這是選用的，不過它們需要相符。在此範例中，如果所有 bridge 都有相同的 region 名稱，則它們都會位於同一個 MSTP bridge。在此情況下，我們要將一組 3 台 bridge 分隔到不同的 MSTP region，以針對每個 VLAN 群組進行負載平衡，並建立多樣性與擴充性：

- 為每台 bridge 設定適當的 region 名稱（與 region revision），並在每台設備上使用下列指令（**請變更 region 名稱！**）：

```ros
/interface/bridge
set bridge region-name=Rx region-revision=1
```

在建立 3 個不同的 MSTP region 後，我們需要決定哪台設備要作為每個 VLAN 群組的 regional root。為了維持一致性，我們會將每個 region 中的第一台設備（\_1）設為 VLAN 10,20 的 regional root，並將每個 region 中的第三台設備（\_3）設為 VLAN 30,40 的 regional root。這可透過為每個 VLAN 群組建立 MST Instance，並為其指派 bridge priority 來完成。MST Instance 識別碼僅在 MSTP region 內有意義；在 MSTP region 外，這些識別碼可以不同，並對應到不同的 VLAN 群組。

- 在 **R1\_1**、**R2\_1**、**R3\_1** 上使用下列指令：

```ros
/interface/bridge/msti
add bridge=bridge identifier=1 priority=0x1000 vlan-mapping=10,20
add bridge=bridge identifier=2 priority=0x3000 vlan-mapping=30,40
```

- 在 **R1\_3**、**R2\_3**、**R3\_3** 上使用下列指令：

```ros
/interface/bridge/msti
add bridge=bridge identifier=1 priority=0x3000 vlan-mapping=10,20
add bridge=bridge identifier=2 priority=0x1000 vlan-mapping=30,40
```

- 在 **R1\_2**、**R2\_2**、**R3\_2** 上使用下列指令：

```ros
/interface/bridge/msti
add bridge=bridge identifier=1 priority=0x2000 vlan-mapping=10,20
add bridge=bridge identifier=2 priority=0x2000 vlan-mapping=30,40
```

現在我們需要覆寫每個 MST Instance 的埠 `path-cost` 及/或埠優先權。這可透過為每個埠與每個 MST Instance 新增 MST-Override 項目來完成。若要讓特定 MST Instance 的流量路徑不同，我們只需確保埠的路徑成本及/或優先權較大。我們可以增加埠路徑成本，或降低朝向 regional root bridge 的埠路徑成本。增加或減少所有值並不重要；重要的是最後某個埠的路徑成本會大於另一個埠。

- 在 **R1\_1**、**R2\_1**、**R3\_1** 上使用下列指令：

```ros
/interface/bridge/port/mst-override
add identifier=2 interface=ether1 internal-path-cost=5
add identifier=2 interface=ether2 internal-path-cost=15
```

- 在 **R1\_2**、**R2\_2**、**R3\_2** 上使用下列指令：

```ros
/interface/bridge/port/mst-override
add identifier=1 interface=ether1 internal-path-cost=5
add identifier=2 interface=ether2 internal-path-cost=9
```

- 在 **R1\_3**、**R2\_3**、**R3\_3** 上使用下列指令：

```ros
/interface/bridge/port/mst-override
add identifier=1 interface=ether2 internal-path-cost=5
add identifier=1 interface=ether3 internal-path-cost=9
```

在此例中，VLAN 10、20 從第一台設備抵達第三台設備時，會在 ether1 與 ether2 之間進行選擇，其中一個埠會被封鎖並設為 alternate 埠，ether1 的路徑成本為 `5+9=14`，ether2 的路徑成本為 `10`，因此 ether2 會被選為第三台設備上 MSTI1 的 root 埠。VLAN 30、40 從第三台設備抵達第一台設備時，ether1 的路徑成本為 `5+9=14`，ether2 的路徑成本為 `15`，因此 ether1 會被選為第三台設備上 MSTI2 的 root 埠。

現在我們可以設定 **MSTI0** 的 root 埠，它會適用於所有未指派給特定 MST Instance 的 VLAN，例如此例中的 VLAN 10、20 與 VLAN 30、40。若要設定這個特殊的 MST Instance，你需要為 bridge 埠指定 `internal-path-cost`。此值僅與 MSTP 區域相關，在 MSTP 區域外不會有任何作用。在此例中，我們會選擇讓所有未知 VLAN 都透過與 VLAN 30、40 相同的路徑轉送，只需增加其中一個埠的路徑成本即可。

- 在 **R1\_3**、**R2\_3**、**R3\_3** 上使用下列指令：

```ros
/interface/bridge/port
set [find where interface=ether3] internal-path-cost=25
```

此時，單一區域的 MSTP 可視為已完成設定，一般而言，MSTP 已可完整運作。強烈建議設定 CIST 部分，但為了測試目的，可以保留預設值。在進行任何測試之前，你需要在所有 bridge 上啟用 MSTP。

- 在**所有**設備上使用下列指令：

```ros
/interface/bridge
set bridge protocol-mode=mstp vlan-filtering=yes
```

設定 MSTP 區域後，你可以透過轉送流量檢查設定是否正確，例如從第一部設備向第三部設備傳送具標記的流量，並變更具標記流量的 VLAN ID，以觀察依 VLAN ID 而定的不同路徑。當運作結果符合預期時，即可繼續設定 CIST 相關參數，以選出 CIST 根橋接器與 CIST 根埠。為保持一致，我們會選擇第一個區域中的第一部設備作為 CIST 根橋接器；為確保故障時的一致性，可以將所有其他橋接器設定為較高的優先順序。

- 在 **R1\_1:** 上使用下列指令：

```ros
/interface/bridge
set bridge priority=0x1000
```

- 在 **R1\_2:** 上使用下列指令：

```ros
/interface/bridge
set bridge priority=0x2000
```

- ...

- 在 **R3\_3:** 上使用下列指令：

```ros
/interface/bridge
set bridge priority=0x9000
```

我們還需要在每部橋接器上選出根埠；為簡化起見，我們會選擇最接近 **R1\_1** 且跳數最少的埠作為根埠。此時，選出根埠的程序與 (R)STP 中的程序相同。

- 在 **R3\_3:** 上使用下列指令：

```ros
/interface/bridge/port
set [find where interface=ether2] path-cost=30
set [find where interface=ether3] path-cost=40
set [find where interface=ether4] path-cost=20
```

- 在 **R1\_3** 與 **R2\_3:** 上使用下列指令：

```ros
/interface/bridge/port
set [find where interface=ether2] path-cost=20
set [find where interface=ether3] path-cost=30
```

- 在 **R1\_2:** 上使用下列指令：

```ros
/interface/bridge/port
set [find where interface=ether1] path-cost=30
```
