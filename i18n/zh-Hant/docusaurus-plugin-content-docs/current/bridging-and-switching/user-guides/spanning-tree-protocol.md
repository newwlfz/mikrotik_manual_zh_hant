---
sidebar_key: "bridging-and-switching/user-guides/spanning-tree-protocol"
sidebar_position: 7
title: "生成樹協定"
sidebar_label: "生成樹協定"
description: "本頁介紹 MikroTik RouterOS 中的生成樹協定（STP），詳細說明其如何透過選舉根橋並利用橋協定資料單元（BPDU）最佳化埠使用來防止網路環路。文中強調了在較大型網路中應進行手動配置，並提供了用於檢查網橋和埠上 STP 狀態的監控命令。"
tags:
  - 'spanning-tree'
  - 'stp'
  - 'rstp'
source: https://manual.mikrotik.com/docs/bridging-and-switching/user-guides/spanning-tree-protocol
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

---

生成樹協定的目的是在具有冗餘鏈路的情況下，能夠建立無環的二層拓撲。連線多個網橋或僅交叉連線網橋埠時，可能會產生網路環路，從而嚴重影響網路的穩定性。生成樹協定旨在透過引入根橋的概念來解決此問題。同一二層域中的所有網橋都會交換有關到根橋的最短路徑的資訊。之後，每個網橋將協商使用哪些埠到達根橋。此資訊交換借助網橋協定資料單元 (BPDU) 完成。STP 會為每個網橋停用某些埠以避免環路，同時仍確保所有網橋能夠相互通訊。有關該協定的深入說明，請參閱 IEEE 802.1D。

作為最佳實踐，始終建議手動設定每個網橋的優先順序、埠優先順序和埠路徑開銷，以確保始終具備正常的二層功能。對於由 1 到 2 臺啟用 (R/M)STP 的網橋組成的網路，將 STP 相關值保留為預設值是可以接受的，但對於更大的網路，強烈建議手動設定這些值。由於 STP 會透過檢查網路中網橋的 STP 相關值來選舉根橋和根埠，將 STP 設定保留為自動可能會選舉出非預期的根橋和根埠，並且在發生硬體故障時可能導致網路無法訪問。

:::info
RouterOS 橋接不支援 PVST 及其變體。PVST BPDU（目標 MAC 為 01:00:0C:CC:CC:CD）會被 RouterOS 橋接視為典型的組播封包。簡單來說，它們會經過 RouterOS 橋接/交換轉發邏輯，並可能被標記或取消標記。
:::

## 監控 {#monitoring}

---

你可以使用 `/interface/bridge/monitor` 命令檢視網橋的 STP 狀態，例如：

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

請注意，根橋沒有任何根埠，只有指定埠。

你可以使用 `/interface/bridge/port/monitor` 命令檢視網橋埠的 STP 狀態，例如：

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

請注意，`root-bridge-id` 由網橋優先順序和網橋的 MAC 地址組成；對於非根網橋，根橋將顯示為 `designated-bridge`。

:::warning
當使用將 802.1Q 設定為 EtherType 的網橋時，它們會向 01:80:C2:00:00:00 傳送 BPDU，這些 BPDU 由 MSTP、RSTP 和 STP 使用。當使用 802.1ad 作為網橋 VLAN 協定時，BPDU 與 802.1Q 網橋不相容，並且會發送到 01:80:C2:00:00:08。如果二層網路中存在不同的網橋 VLAN 協定，則 (R/M)STP 將無法正常工作。
:::

## STP 和 RSTP {#stp-and-rstp}

---

STP 和 RSTP 在許多網路中被廣泛使用，但由於 RSTP 的優勢，幾乎所有網路都已切換到僅使用 RSTP。STP 是一種非常舊的協定，其收斂時間（完全學習網路拓撲變化並繼續正確轉發流量所需的時間）可長達 50 秒。RSTP 的收斂時間要短得多，只需幾秒甚至幾毫秒。建議使用 RSTP 而不是 STP，因為它快得多，並且還向後相容 STP。RSTP 更快的原因之一是可能出現的埠狀態減少了，以下是可能的 STP 埠狀態列表：

- **Forwarding** - 埠參與流量轉發並學習 MAC 地址，同時接收 BPDU。
- **Listening** - 埠不參與流量轉發，也不學習 MAC 地址，同時接收 BPDU。
- **Learning** - 埠不參與流量轉發，但會學習 MAC 地址。
- **Blocking** - 由於埠導致環路而被阻塞，但仍接收 BPDU。
- **Disabled** - 埠已停用或處於非活動狀態。

在 RSTP 中，disabled、listening 和 blocking 埠狀態被替換為僅一個稱為 **Discarding** 的狀態：

- **Forwarding** - 埠參與流量轉發、學習 MAC 地址並接收 BPDU（forwarding=yes）。
- **Learning** - 埠不參與流量轉發，但會學習 MAC 地址（learning=yes）。
- **Discarding** - 埠不參與流量轉發、不學習 MAC 地址，並接收 BPDU（forwarding=no）。

在 STP 中，埠主要按狀態分類（例如 Forwarding、Listening、Learning、Blocking、Disabled）。埠行為根據生成樹演算法動態確定，但不會顯式分配角色。轉發或阻塞流量的邏輯源自對根橋、根埠和指定埠的計算，但這些被視為生成樹拓撲的一部分，而不是正式化的埠角色。RSTP 明確定義了埠角色，並引入了備份路徑的概念，這些路徑透過 Alternate Port 和 Backup Port 角色顯式表示。這些角色在 STP 中不存在，因為 STP 對阻塞埠進行通用處理，沒有區分它們作為潛在備份的功能。

以下是 RSTP 協定的埠角色細分：

- **Root Port** - 朝向根橋並具有到根橋的最佳（最低開銷）路徑的埠。每個網橋只選舉一個根埠（根橋本身除外）。
- **Designated Port** - 背向根橋並將流量從根橋轉發到下游裝置的埠。
- **Alternate Port** - 朝向根橋但不會轉發流量的埠。如果當前根埠發生故障，該埠提供通往根橋的備份路徑。
- **Backup Port** - 背向根橋但不會轉發流量的埠。該埠充當同一網段上指定埠的備份。
- **Disabled Port** - 已停用或非活動的埠。

在 STP 中，網橋之間的連通性透過鄰居網橋之間傳送和接收 BPDU 來確定。指定埠會向根埠傳送 BPDU。如果連續 3 個 **HelloTime** 週期未收到 BPDU，則認為連線不可用，並將開始網路拓撲收斂。在某些場景中，可以透過減少 `forward-delay` 計時器來縮短 STP 收斂時間，該計時器決定埠可處於 learning/listening 狀態的時間。

在 RouterOS 中，可以指定哪些網橋埠是邊緣埠。邊緣埠是不應接收任何 BPDU 的埠。這很有益，因為它允許 STP 跳過 learning 和 listening 狀態，直接進入 forwarding 狀態。此功能有時稱為 **PortFast**。你可以將此引數保留為預設值 **auto**，也可以手動指定。對於其後不應再有網橋的埠，可以手動將埠設定為邊緣埠。通常，這些是接入埠。

此外，網橋埠 `point-to-point` 指定網橋埠是否透過點對點鏈路連線到網橋，以便在發生故障時更快收斂。將此屬性設定為 `yes`，即強制該鏈路為點對點鏈路，這會跳過檢查機制，該機制會檢測並等待來自此單條鏈路上其他裝置的 BPDU。將此屬性設定為 `no`，表示該鏈路可以接收來自多個裝置的 BPDU。將此屬性設定為 `yes`，可顯著改善 (R/M)STP 收斂時間。通常，只有在鏈路之間可能連線另一臺裝置時，才應將此屬性設定為 `no`。這主要與無線介質和乙太網集線器相關。如果乙太網鏈路是全雙工，`auto` 會啟用點對點功能。當 `protocol-mode` 設定為 `none` 時，此屬性無效。

### 預設值 {#default-values}

建立網橋或向網橋新增埠時，RouterOS 分配的預設值如下：

- 預設網橋優先順序：**32768** / **0x8000**
- 預設網橋埠路徑開銷：**基於介面速率**
- 預設網橋埠優先順序：**0x80**
- BPDU 訊息年齡增量：**1**
- HelloTime：**2**
- 預設最大訊息年齡：**20**

網橋介面設定 `port-cost-mode` 會更改橋接埠的埠 `path-cost` 和 `internal-path-cost` 模式，使用基於介面速率的自動值。此設定不會影響已手動配置 `path-cost` 或 `internal-path-cost` 屬性的橋接埠。以下示例說明了特定資料速率對應的 path-cost（中間速率按比例計算）：

| 資料速率 | 長 | 短 |
| :-- | :-- | --: |
| 10 Mbps | 2,000,000 | 100 |
| 100 Mbps | 200,000 | 19 |
| 1 Gbps | 20,000 | 4 |
| 10 Gbps | 2,000 | 2 |
| 25 Gbps | 800 | 1 |
| 40 Gbps | 500 | 1 |
| 50 Gbps | 400 | 1 |
| 100 Gbps | 200 | 1 |

對於繫結介面，會應用所有繫結成員埠中最大的 `path-cost`，該值不受繫結總鏈路速率的影響。對於虛擬介面（例如 VLAN、EoIP、VXLAN）以及 wifi、wireless 和 60GHz 介面，長模式下會分配 `path-cost` 為 20,000，短模式下為 10。對於動態橋接的介面（例如 wifi、wireless、PPP、VPLS），`path-cost` 在長模式下預設為 20,000，在短模式下預設為 10。但是，這可以由動態向網橋新增介面的服務手動覆蓋，例如使用 CAPsMAN 的 `datapath.bridge-cost` 設定。7.13 之前的 RouterOS 版本不會根據鏈路速率更改埠路徑開銷；對於 10M、100M、1000M 和 10000M 鏈路速率，向網橋新增埠時的預設路徑開銷值始終為 **10**。

BPDU 的年齡由 BPDU 經過的網橋數量乘以訊息年齡決定，因為 RouterOS 使用 **1** 作為訊息年齡增量，所以 BPDU 封包可以經過 `max-message-age` 引數指定的那麼多網橋。預設情況下，此值設定為 **20**。這意味著經過第 20 個網橋後，BPDU 封包將被丟棄，下一個網橋將成為根橋。請注意，如果設定了 `max-message-age=20`，則很難預測第 21 個網橋上的哪些埠將成為指定埠，並可能導致流量無法正確轉發。

:::warning
如果使用網橋過濾規則，請確保允許目的 MAC 地址為 **01:80:C2:00:00:00** 的封包，因為這些封包攜帶對 STP 正常工作至關重要的 BPDU。
:::

### 選舉過程 {#election-process}

要在網路中正確配置 STP，你需要了解選舉過程以及哪些引數以何種順序參與。在 RouterOS 中，根橋將按以下特定順序基於最小優先順序和最小 MAC 地址選舉：

1. 網橋優先順序（最低）。
2. 網橋 MAC 地址（最低）。

在 RouterOS 中，根埠按以下特定順序基於最低根埠路徑開銷、最低網橋識別符號和最低網橋埠 ID 選舉：

1. 根埠路徑開銷（最低）
2. 網橋識別符號（最低）
3. 網橋埠 ID（最低）

首先，當裝置考慮將其哪個埠選舉為根埠時，它會檢查其埠所見的**根路徑開銷**。如果兩個或多個埠的根路徑開銷相同，則將檢查**上游**裝置的**網橋識別符號**，連線到最低網橋識別符號的埠將成為根埠。如果在兩個或多個埠上看到相同的網橋識別符號，則將檢查**上游**裝置的**網橋埠 ID**。

## 屬性說明 {#explanation-of-attributes}

根路徑開銷：所有網橋都有一個根路徑開銷。根橋的根路徑開銷為 0。對於所有其他網橋，它是最低開銷路徑上到根橋的各埠路徑開銷之和。你可以在 `/interface/bridge/port` 下修改本地埠路徑開銷。
網橋識別符號是“網橋優先順序”和“網橋 MAC”的組合，可在 `/interface/bridge` 下配置。

網橋埠 ID 是“唯一 ID”和“網橋埠優先順序”的組合。唯一 ID 在將網橋埠新增到網橋時自動分配。它無法編輯。可在 WinBox 的“Bridge Port”的“Port Number”列中檢視，或使用 `/interface/bridge/port/monitor` 以 `port-number` 檢視。

:::tip 理解 STP 埠選舉
確保將路徑開銷和優先順序應用到正確的埠：

- **Path Cost** 影響*朝向*根橋的埠。（在根橋埠上設定路徑開銷沒有效果）。
- **Port Priority** 影響*背向*根橋的埠。
- **Bridge Identifier** 不影響裝置自身根埠的選舉；它會影響*下游*裝置的根埠選舉。
:::

:::warning 網橋優先順序相容性
RouterOS 允許將網橋優先順序設定為 0 到 65535 之間的任意值。但是，IEEE 802.1W 標準嚴格要求網橋優先順序以 4096 為步長。為避免與其他廠商裝置不相容，請**僅**使用以下優先順序值：
`0, 4096, 8192, 12288, 16384, 20480, 24576, 28672, 32768, 36864, 40960, 45056, 49152, 53248, 57344, 61440`
:::

### 示例 {#examples}

#### 根路徑開銷示例 {#root-path-cost-example}

![Root Path](/img/3683697e750a8f2f.webp)

此示例概述了根路徑開銷的工作方式。SW1 將成為根橋，因為它具有最低的優先順序 0x1000。每個網橋都會計算到根橋的路徑開銷。計算根路徑開銷時，網橋會考慮其埠上配置的路徑開銷 + 鄰居網橋通告的根路徑開銷。

**SW1**：由於它是根橋，即使配置的路徑開銷為 10，它也會向鄰居通告根路徑開銷為 0。

**SW2:****ether1** 的根路徑開銷為 0 + 25=**25**。在 **ether2** 路徑上，開銷將為 10+10+10+0=**30**

**SW3:** **ether2** 的根路徑開銷為 0 + 10=**10**。在 **ether4** 路徑上，路徑開銷將為 10+5+25+0=**40**

**SW4:** **ether1** 的根路徑開銷為 0+25+5=**30**。在 **ether4** 上，路徑開銷將為 10+10+0=**20**。

具有最低路徑開銷的埠將被選舉為根埠。STP 拓撲中的每個網橋都需要一條通往根橋的路徑。找到最佳路徑後，冗餘路徑將被阻塞，在本例中，即 SW2 和 SW4 之間的路徑。

:::warning
你可以在根橋上配置路徑開銷，但只有當該網橋失去根狀態時才會考慮它。
:::

#### STP 示例 {#stp-example}

![STP Example 1](/img/4c8bc04b481c916d.webp)

在此示例中，我們希望確保從 ServerA 到 ServerB 的連線具備二層冗餘。如果某個埠連線到不是網橋且未執行 (R)STP 的裝置，則該埠被視為邊緣埠。在本例中，ServerA 和 ServerB 連線到邊緣埠。透過在網路中使用 STP 可以實現這一點。以下是每個交換器的配置示例：

- SW1 的配置：

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

- SW2 的配置：

```ros
/interface/bridge
add name=bridge priority=0x2000
/interface/bridge/port
add bridge=bridge interface=ether1
add bridge=bridge interface=ether2
add bridge=bridge interface=ether3
```

- SW3 的配置

```ros
/interface/bridge
add name=bridge priority=0x3000
/interface/bridge/port
add bridge=bridge interface=ether1
add bridge=bridge interface=ether2
add bridge=bridge interface=ether3
```

- SW4 的配置：

```ros
/interface/bridge
add name=bridge priority=0x4000
/interface/bridge/port
add bridge=bridge interface=ether1
add bridge=bridge interface=ether2 path-cost=20
add bridge=bridge interface=ether3
```

在此示例中，**SW1** 是根橋，因為它具有最低的網橋優先順序。**SW2** 和 **SW3** 的 ether1、ether2 連線到根橋，ether3 連線到 **SW4**。當所有交換器正常工作時，流量將從 ServerA 經過 SW1\_ether2、SW2 和 SW4 流向 ServerB。如果 **SW1** 發生故障，**SW2** 將因次低優先順序而成為根橋，如圖中虛線所示。以下是每個交換器的埠及其角色列表：

- **root-port** - SW2\_ether2、SW3\_ether2、SW4\_ether1
- **alternate-port** - SW2\_ether1、SW3\_ether1、SW4\_ether2
- **designated-port** - SW1\_ether1、SW1\_ether2、SW1\_ether3、SW1\_ether4、SW1\_ether5、SW2\_ether3、SW3\_ether3、SW4\_ether3

:::note
**注意：** 根據 802.1Q 建議，應使用以 4096 為步長的網橋優先順序。要設定建議的優先順序，使用十六進位制表示法更方便，例如，0 為 0x0000，4096 為 0x1000，8192 為 0x2000，依此類推（0..F）。
:::

## 多生成樹協定 {#multiple-spanning-tree-protocol}

---

多生成樹協定 (MSTP) 用於網橋介面，以確保跨多個 VLAN 的無環拓撲。MSTP 還可以提供二層冗餘，並可用作 VLAN 的負載均衡技術，因為它能夠為不同 VLAN 使用不同路徑。MSTP 的執行方式與 (R)STP 非常相似，並且 (R)STP 的許多概念都可以應用於 MSTP；強烈建議在使用 MSTP 之前理解 (R)STP 的原理，但在設計啟用 MSTP 的網路時，必須考慮一些差異。

在使用 (R)STP 的情況下，BPDU 會在網橋中的所有物理介面上傳送，以確定環路，並在埠導致環路時阻止其轉發流量。如果某個 VLAN 記憶體在環路，(R)STP 可能無法檢測到。某些 STP 變體透過在每個 VLAN 上執行一個 STP 例項 (PVST) 來解決此問題，但這已被證明效率低下；還有一些 STP 變體透過在所有 VLAN 上執行單個 STP 例項 (CST) 來解決此問題，但它無法為每個 VLAN 或 VLAN 組進行負載均衡。MSTP 傾向於透過使用 MST 例項來解決這兩個問題，這些例項可以定義一組 VLAN（VLAN 對映），用於負載均衡和冗餘，這意味著每個 VLAN 組可以有不同的根橋和不同的路徑。請注意，將多個 VLAN 分組到單個例項中有利於減少每次網路拓撲變化時的 CPU 週期數。

:::danger
在啟用 MSTP 的 RouterOS 中，網橋優先順序是 CIST 的根橋優先順序。如 IEEE 802.1Q 標準所述，網橋優先順序必須以 4096 為步長，最低的 12 位會被忽略。以下是有效的網橋優先順序：0、4096、8192、12288、16384、20480、24576、28672、32768、36864、40960、45056、49152、53248、57344、61440。設定無效的網橋優先順序時，RouterOS 會發出警告並將該值截斷為有效值，但會在配置中儲存原始值，因為無效的網橋優先順序值仍可在執行 RouterOS 的裝置之間的 (R)STP 中使用，不過建議改用有效的網橋優先順序。
:::

### MSTP 區域 {#mstp-regions}

MSTP 以稱為區域的組來工作。每個區域都會有一個區域根橋，並且在區域之間會選舉一個根橋。MSTP 將使用內部生成樹 (IST) 構建區域內的網路拓撲，並使用公共生成樹 (CST) 在區域外構建多個區域之間的網路拓撲。MSTP 將這兩種協定合併為公共和內部生成樹 (CIST)，它儲存有關區域內和區域間拓撲的資訊。從 CST 的角度來看，一個區域似乎是一個單一的虛擬網橋，因此 MSTP 被認為對大型網路非常具有可擴充套件性。要使網橋處於同一區域，它們的配置必須匹配。BPDU 不會包含 VLAN 對映，因為對映可能很大，而是會傳輸計算出的雜湊值。如果網橋透過某個埠收到 BPDU 且配置不匹配，則 MSTP 會將該埠視為邊界埠，並認為它可用於到達其他區域。以下是 MSTP 認為 BPDU 來自同一區域所需匹配的引數列表：

- 區域名稱
- 區域修訂版本
- 到 MST 例項 ID 的 VLAN 對映（計算出的雜湊）

可以建立不帶區域的啟用 MSTP 網路，但要能夠按 VLAN 組進行負載均衡，網橋需要從與其連線且具有上述相同引數的網橋接收 BPDU。在 RouterOS 中，預設區域名稱為空，區域修訂版本為 0，這些都是有效值，但你必須確保它們匹配，才能讓多個網橋處於同一個 MSTP 區域。如果區域中的網橋分散在網路中，則該區域無法存在；這些網橋必須至少以一種方式連線，使它們能夠在不離開區域的情況下發送和接收 BPDU。例如，如果一臺具有不同區域相關引數的網橋位於兩臺具有相同區域相關引數的網橋之間，那麼將至少存在 3 個不同的 MSTP 區域。

![MSTP Topology](/img/77a9b366354f5ae5.webp)

將每個網橋都執行在單個 MSTP 區域中的缺點是 CPU 週期過多。相比之下，PVST(+) 會為網路中存在的每個 VLAN ID 建立一個生成樹例項；由於網路中可能存在的路徑非常有限，這種方法會產生大量開銷和不必要的 CPU 週期。這也意味著這種方法可擴充套件性不佳，並且可能使 CPU 效能不是很強的交換器過載。MSTP 透過將網路劃分為 MSTP 區域來解決此問題：此區域內的每個網橋將交換並處理同一區域記憶體在的 VLAN 資訊，但會在後臺執行單個生成樹協定例項，以維護區域之間的網路拓撲。此方法已被證明更加有效且更具可擴充套件性。這意味著對於較大的網路，應使用區域來減少 CPU 週期。

在區域中，你可以定義 MST 例項，用於配置按 VLAN 組的負載均衡並選舉區域根橋。值得注意的是，每個區域中都存在一個預定義的 MST 例項，在大多數文件中稱為 **MSTI0**· 此 MST 例項被視為預設 MST 例項。有一些引數適用於此特殊 MST 例項。當流量經過啟用 MSTP 的網橋時，MSTP 會查詢具有匹配 VLAN 對映的 MST 例項；但如果某個 VLAN ID 不存在 VLAN 對映，則流量將歸入 **MSTI0**。

:::warning
由於 MSTP 要求啟用網橋介面上的 VLAN 過濾，因此請確保你已在 `/interface/bridge/vlan` 中允許所有必需的 VLAN ID；否則，流量將不會被轉發，並且可能看起來像是 MSTP 配置錯誤，儘管這實際上是 VLAN 過濾配置錯誤。
:::

### 選舉過程 {#election-process-1}

MSTP 中的選舉過程可以分為兩部分：區域內和區域間。要使 MSTP 正常工作，始終需要有一個區域根，即區域內的根橋，以及一個 CIST 根，即區域之間的根橋。區域根是區域內的根橋，需要區域根橋來正確設定區域內 VLAN 組的負載均衡。CIST 根將用於配置哪些埠將成為替代/備份埠（非活動），以及哪些埠將成為根埠（活動）。

:::warning
在區域之間，沒有按 VLAN 組的負載均衡，也沒有根埠選舉過程，並且 MSTP 區域之間的埠阻塞方式與 (R)STP 中相同。如果 CIST 已阻塞 MSTP 區域內的某個埠以防止 MSTP 區域之間的流量環路，則該埠仍可對 IST 保持活動，以便在 MSTP 區域內按 VLAN 組進行負載均衡。
:::

- 以下引數參與在 MSTP 區域內選舉區域根橋或根埠：

| 屬性 | 描述 |
| :-- | :-- |
| **priority** (*integer：0..65535 十進位制格式或 0x0000-0xffff 十六進位制格式*；預設值：**32768 / 0x8000**) | `/interface/bridge/msti`，MST 例項優先順序，用於在 MSTP 區域內選舉區域根。必須以 4096 (0x1000) 為步長設定；最低 12 位會被忽略。有效值：0x0000、0x1000、0x2000、...、0xf000（或十進位制等價值：0、4096、8192、...、61440）。 |
| **internal-path-cost** (*integer：1..200000000*；預設值： ) | `/interface/bridge/port`，未知 VLAN ID (MSTI0) 到區域根的路徑開銷，用於 MSTP 區域內的根埠。 |
| **priority** (*0x00 \| 0x10 \| 0x20 \| 0x30 \| 0x40 \| 0x50 \| 0x60 \| 0x70 \| 0x80 \| 0x90 \| 0xa0 \| 0xb0 \| 0xc0 \| 0xd0 \| 0xe0 \| 0xf0*；預設值：**0x80**) | `/interface/bridge/port/mst-override`，為定義的 MST 例項設定 MST 埠優先順序，用於區域根橋上的網橋埠。必須以 16 (0x10) 為步長設定。 |
| **internal-path-cost** (*integer：1..200000000*；預設值： ) | `/interface/bridge/port/mst-override`，為定義的 MST 例項設定 MST 埠路徑開銷，用於 MSTP 區域內的非根網橋埠。 |

- 以下引數參與選舉 CIST 根橋或 CIST 根埠：

| 屬性 | 描述 |
| :-- | :-- |
| **priority** (*integer：0..65535 十進位制格式或 0x0000-0xffff 十六進位制格式*；預設值：**32768 / 0x8000**) | `/interface/bridge`，CIST 網橋優先順序，用於選舉 CIST 根橋。必須以 4096 (0x1000) 為步長設定；最低 12 位會被忽略。 |
| **priority** (*0x00 \| 0x10 \| 0x20 \| 0x30 \| 0x40 \| 0x50 \| 0x60 \| 0x70 \| 0x80 \| 0x90 \| 0xa0 \| 0xb0 \| 0xc0 \| 0xd0 \| 0xe0 \| 0xf0*；預設值：**0x80**) | `/interface/bridge/port`，CIST 埠優先順序，用於在 CIST 根橋上選舉 CIST 根埠。必須以 16 (0x10) 為步長設定。 |
| **path-cost** (*integer：1..200000000*；預設值： ) | `/interface/bridge/port`，CIST 埠路徑開銷，用於在 CIST 非根網橋埠上選舉 CIST 根埠。 |

:::warning
MSTP 檢查選舉根橋/根埠所依據的引數順序與 (R)STP 中相同，你可以閱讀 (R)STP 選舉過程一節瞭解更多資訊。
:::

### MST 例項 {#mst-instance}

**子選單：** `/interface/bridge/msti`

此部分用於將多個 VLAN ID 分組到單個例項中，以便為 MSTP 區域內的每個 VLAN 組建立不同的根橋。

| 屬性 | 描述 |
| :-- | :-- |
| **bridge** (*text*；預設值： ) | MST 例項分配到的網橋。 |
| **identifier** (*integer：1..31*；預設值： ) | MST 例項識別符號。 |
| **priority** (*integer：0..65535 十進位制格式或 0x0000-0xffff 十六進位制格式*；預設值：**32768 / 0x8000**) | MST 例項優先順序用於確定 MSTP 區域中一組 VLAN 的根橋。 |
| **vlan-mapping** (*integer：1..4094*；預設值： ) | 要分配給 MST 例項的 VLAN ID 列表。此設定接受 VLAN ID 範圍以及逗號分隔的值。例如 `vlan-mapping=100-115,120,122,128-130` |

### MST 覆蓋 {#mst-override}

**子選單：** `/interface/bridge/port/mst-override`

此部分用於為 MSTP 區域內的每個 VLAN 對映選擇所需路徑。

| 屬性 | 描述 |
| :-- | :-- |
| **disabled** (*yes \| no*；預設值：**no**) | 條目是否已停用。 |
| **internal-path-cost** (*integer：1..200000000*；預設值： ) | MST 例項 VLAN 對映的路徑開銷，用於面向根橋的 VLAN 以操縱路徑選擇；路徑開銷越低越優先。 |
| **identifier** (*integer：1..31*；預設值： ) | MST 例項識別符號。 |
| **priority** (*integer：0..240*；預設值：**128**) | MST 例項 VLAN 的優先順序，用於背向根橋的 VLAN 以操縱路徑選擇；優先順序越低越優先。 |
| **interface** (*name*；預設值： ) | 要使用已配置的 MST 例項 VLAN 對映以及定義的路徑開銷和優先順序的埠名稱。 |

### 監控 {#monitoring-1}

與 (R)STP 類似，也可以監控 MSTP 狀態。透過監控網橋介面本身，可以檢視當前的 CIST 根橋以及 MSTI0 的當前區域根橋。還可以檢視 MST 例項識別符號和 VLAN 對映的計算雜湊值。這在確保某些網橋處於同一 MSTP 區域時很有用。以下是監控 MSTP 網橋的示例：

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

在 MSTP 中，可以監控 MST 例項。這對於確定某個 MST 例項和 VLAN 組的當前區域根橋很有用。以下是監控 MST 例項的示例：

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

還可以監控某個 MST 覆蓋條目。這在 MSTP 區域中配置根埠和替代/備份埠時，對於確定某個 MST 例項的埠角色很有用。以下是監控 MST 覆蓋條目的示例：

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

### MSTP 示例 {#mstp-example}

假設我們需要設計一個拓撲並配置 MSTP，使 VLAN 10、20 沿一條路徑轉發，而 VLAN 30、40 沿另一條路徑轉發，同時所有其他 VLAN ID 將沿其中一條路徑轉發。透過設定 MST 例項並分配埠路徑開銷，可以輕鬆完成此操作。以下是一個需要按 VLAN 組進行負載均衡且包含 3 個獨立區域的網路拓撲示例：

![MSTP Example](/img/27652a7629c4268f.webp)

按 VLAN 組進行負載均衡的啟用 MSTP 網路拓撲

首先將每個介面新增到網橋。最初，應建立一個未啟用 VLAN 過濾的 (R)STP 網橋。這是為了防止失去對 CPU 的訪問。此示例中的每個裝置都按其所在區域 (Rx) 和裝置編號 (\_x) 命名。對於較大的網路，由於鏈路和裝置數量眾多，配置 MSTP 可能會令人困惑。我們建議使用 The Dude 來監控和設計網路拓撲。

- 在 **R1\_1**、**R1\_3**、**R2\_1**、**R2\_3**、**R3\_1**、**R3\_3** 上使用以下命令：

```ros
/interface/bridge
add name=bridge protocol-mode=rstp vlan-filtering=no
/interface/bridge/port
add bridge=bridge interface=ether1
add bridge=bridge interface=ether2
add bridge=bridge interface=ether3
add bridge=bridge interface=ether4
```

- 在 **R1\_2**、**R2\_2**、**R3\_2** 上使用以下命令。

```ros
/interface/bridge
add name=bridge protocol-mode=rstp vlan-filtering=no
/interface/bridge/port
add bridge=bridge interface=ether1
add bridge=bridge interface=ether2
```

- 確保在這些裝置上允許所需的 VLAN ID。這裡我們假設每個裝置都會收到需要按 VLAN 組進行負載均衡的帶標籤流量。在 **R1\_1**、**R1\_3**、**R2\_1**、**R2\_3**、**R3\_1**、**R3\_3** 上使用以下命令：

```ros
/interface/bridge/vlan
add bridge=bridge tagged=ether1,ether2,ether3,ether4 vlan-ids=10,20,30,40
```

- 在 **R1\_2**、**R2\_2**、**R3\_2** 上使用以下命令：

```ros
/interface/bridge/vlan
add bridge=bridge tagged=ether1,ether2 vlan-ids=10,20,30,40
```

:::warning
請確保將所有需要的 VLAN ID 和埠新增到網橋 VLAN 表中，否則你的裝置將不會轉發所有必需的 VLAN，和/或你將失去對裝置的訪問。
:::

我們需要為希望處於同一 MSTP 區域的每個網橋分配區域名稱。你也可以指定區域修訂版本，但它是可選的，不過它們需要匹配。在此示例中，如果所有網橋具有相同的區域名稱，那麼它們都將處於單個 MSTP 網橋中。在本例中，我們希望將一組 3 個網橋分到不同的 MSTP 區域，以便按 VLAN 組進行負載均衡並實現多樣性和可擴充套件性：

- 為每個網橋設定適當的區域名稱（和區域修訂版本），並在每臺裝置上使用以下命令（**更改區域名稱！**）：

```ros
/interface/bridge
set bridge region-name=Rx region-revision=1
```

建立 3 個不同的 MSTP 區域後，我們需要決定哪臺裝置將作為每個 VLAN 組的區域根。為了一致性，我們將把每個區域中的第一臺裝置 (\_1) 設定為 VLAN 10、20 的區域根，並把每個區域中的第三臺裝置 (\_3) 設定為 VLAN 30、40 的區域根。這可以透過為每個 VLAN 組建立 MST 例項併為其分配網橋優先順序來完成。MST 例項識別符號僅在 MSTP 區域內部相關；在 MSTP 區域外部，這些識別符號可以不同，並對映到不同的 VLAN 組。

- 在 **R1\_1**、**R2\_1**、**R3\_1** 上使用以下命令：

```ros
/interface/bridge/msti
add bridge=bridge identifier=1 priority=0x1000 vlan-mapping=10,20
add bridge=bridge identifier=2 priority=0x3000 vlan-mapping=30,40
```

- 在 **R1\_3**、**R2\_3**、**R3\_3** 上使用以下命令：

```ros
/interface/bridge/msti
add bridge=bridge identifier=1 priority=0x3000 vlan-mapping=10,20
add bridge=bridge identifier=2 priority=0x1000 vlan-mapping=30,40
```

- 在 **R1\_2**、**R2\_2**、**R3\_2** 上使用以下命令。

```ros
/interface/bridge/msti
add bridge=bridge identifier=1 priority=0x2000 vlan-mapping=10,20
add bridge=bridge identifier=2 priority=0x2000 vlan-mapping=30,40
```

現在我們需要為每個 MST 例項覆蓋埠 `path-cost` 和/或埠優先順序。這可以透過為每個埠和每個 MST 例項新增 MST 覆蓋條目來完成。要使某個 MST 例項的流量流路徑不同，我們只需確保埠路徑開銷和/或優先順序更大。我們可以增加埠路徑開銷，或減少面向區域根橋的埠的埠路徑開銷。增加還是減少所有值並不重要；重要的是最終一個埠的路徑開銷要大於另一個埠。

- 在 **R1\_1**、**R2\_1**、**R3\_1** 上使用以下命令：

```ros
/interface/bridge/port/mst-override
add identifier=2 interface=ether1 internal-path-cost=5
add identifier=2 interface=ether2 internal-path-cost=15
```

- 在 **R1\_2**、**R2\_2**、**R3\_2** 上使用以下命令：

```ros
/interface/bridge/port/mst-override
add identifier=1 interface=ether1 internal-path-cost=5
add identifier=2 interface=ether2 internal-path-cost=9
```

- 在 **R1\_3**、**R2\_3**、**R3\_3** 上使用以下命令：

```ros
/interface/bridge/port/mst-override
add identifier=1 interface=ether2 internal-path-cost=5
add identifier=1 interface=ether3 internal-path-cost=9
```

在這種情況下，對於 VLAN 10、20 從第一臺裝置到達第三臺裝置，它會在 ether1 和 ether2 之間選擇，其中一個埠將被阻塞並設定為替代埠；ether1 的路徑開銷為 `5+9=14`，ether2 的路徑開銷為 `10`，ether2 將被選舉為第三臺裝置上 MSTI1 的根埠。對於 VLAN 30、40 從第三臺裝置到達第一臺裝置的情況，ether1 的路徑開銷為 `5+9=14`，ether2 的路徑開銷為 `15`，ether1 將被選舉為第三臺裝置上 MSTI2 的根埠。

現在我們可以為 **MSTI0** 配置根埠，它將涵蓋所有未分配給特定 MST 例項的 VLAN，例如我們示例中的 VLAN 10、20 和 VLAN 30、40。要配置此特殊 MST 例項，你需要為網橋埠指定 `internal-path-cost`。此值僅與 MSTP 區域相關，在 MSTP 區域外沒有任何效果。在此示例中，我們將選擇讓所有未知 VLAN 沿與 VLAN 30、40 相同的路徑轉發，只需增加其中一個埠的路徑開銷即可。

- 在 **R1\_3**、**R2\_3**、**R3\_3** 上使用以下命令：

```ros
/interface/bridge/port
set [find where interface=ether3] internal-path-cost=25
```

至此，可以認為單區域 MSTP 已配置完成；一般來說，MSTP 已完全可用。強烈建議配置 CIST 部分，但出於測試目的，可以保留預設值。在進行任何測試之前，你需要在所有網橋上啟用 MSTP。

- 在**所有**裝置上使用以下命令：

```ros
/interface/bridge
set bridge protocol-mode=mstp vlan-filtering=yes
```

配置 MSTP 區域後，你可以透過轉發流量來檢查它們是否配置正確，例如，從第一臺裝置向第三臺裝置傳送帶標籤流量，並更改帶標籤流量的 VLAN ID，以觀察基於 VLAN ID 的不同路徑。當此功能按預期工作時，你可以繼續配置 CIST 相關引數，以選舉 CIST 根橋和 CIST 根埠。為了一致性，我們將選擇第一個區域中的第一臺裝置作為 CIST 根橋；並且為了確保故障時的一致性，我們可以為所有其他網橋設定更高的優先順序。

- 在 **R1\_1** 上使用以下命令：

```ros
/interface/bridge
set bridge priority=0x1000
```

- 在 **R1\_2** 上使用以下命令：

```ros
/interface/bridge
set bridge priority=0x2000
```

- ...

- 在 **R3\_3** 上使用以下命令：

```ros
/interface/bridge
set bridge priority=0x9000
```

我們還需要在每個網橋上選舉一個根埠；為簡單起見，我們將選擇最接近 **R1\_1** 且跳數最少的埠作為根埠。此時，選舉根埠的過程與 (R)STP 中的過程相同。

- 在 **R3\_3** 上使用以下命令：

```ros
/interface/bridge/port
set [find where interface=ether2] path-cost=30
set [find where interface=ether3] path-cost=40
set [find where interface=ether4] path-cost=20
```

- 在 **R1\_3** 和 **R2\_3** 上使用以下命令：

```ros
/interface/bridge/port
set [find where interface=ether2] path-cost=20
set [find where interface=ether3] path-cost=30
```

- 在 **R1\_2** 上使用以下命令：

```ros
/interface/bridge/port
set [find where interface=ether1] path-cost=30
```
