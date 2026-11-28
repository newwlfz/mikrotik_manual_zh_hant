---
title: "L3 硬體卸載"
description: "L3 Hardware Offloading 透過將 CPU 密集型工作卸載到交換器晶片，讓路由能以線速運作。本頁詳細說明如何為整個交換器、個別埠，以及 IPv6 支援與 FastTrack offloading 等全域設定設定 L3HW，並提醒可能對現有連線造成的影響。"
tags:
  - 'l3hw'
  - 'switching'
source: https://manual.mikrotik.com/docs/7.24/bridging-and-switching/l3-hardware-offloading
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

**Layer 3 Hardware Offloading** (**L3HW**，亦稱為 IP switching 或 HW routing) 可將部分路由器功能卸載到交換器晶片。這讓封包路由能達到線速，而這僅靠 CPU 是無法達成的。

## 交換器設定 {#switch-configuration}

若要啟用 Layer 3 Hardware Offloading，請為交換器設定 `l3-hw-offloading=yes`：

```ros
/interface/ethernet/switch/set 0 l3-hw-offloading=yes
```

### 交換器埠設定 {#switch-port-configuration}

Layer 3 Hardware Offloading 可針對每個實體交換器埠進行設定。例如：

```ros
/interface/ethernet/switch/port/set sfp-sfpplus1 l3-hw-offloading=yes
```

請注意，交換器與埠的 l3hw 設定不同：

- 為交換器設定 `l3-hw-offloading``=no` 會完全停用 offloading，所有封包都將由 CPU 路由。
- 不過，為交換器埠設定 `l3-hw-offloading``=no` 只會停用該特定埠的硬體路由。此外，該埠仍可參與 Fasttrack 連線 offloading。

若要啟用完整硬體路由，請在所有交換器埠上啟用 l3hw：

```ros
/interface/ethernet/switch/set 0 l3-hw-offloading=yes
/interface/ethernet/switch/port/set [find] l3-hw-offloading=yes
```

若要讓所有封包先經過 CPU，並且僅卸載 Fasttrack 連線，請在所有埠上停用 l3hw，但保持交換器晶片本身啟用：

```ros
/interface/ethernet/switch/set 0 l3-hw-offloading=yes
/interface/ethernet/switch/port/set [find] l3-hw-offloading=no
```

:::info
**當 ingress 與 egress 埠都設定 `l3-hw-offloading=yes` 時，封包會由硬體路由。**

若 ingress 與 egress 埠都設定 `l3-hw-offloading=no`，封包會經過 CPU／Firewall，且僅卸載 Fasttrack 連線。

只要設定 egress 埠的 `l3-hw-offloading=no`，即可讓封包經過 CPU／Firewall。不過，僅設定 ingress 埠的 `l3-hw-offloading=no` 可能導致無法預期的行為，例如封包仍可能由硬體路由，並完全略過 CPU／firewall。
:::

下一個範例會在所有埠上啟用硬體路由，但上游埠（sfp-sfpplus16）除外。進出 sfp-sfpplus16 的封包會進入 CPU，因此會經過 Firewall／NAT 處理。

```ros
/interface/ethernet/switch/set 0 l3-hw-offloading=yes
/interface/ethernet/switch/port/set [find] l3-hw-offloading=yes
/interface/ethernet/switch/port/set sfp-sfpplus16 l3-hw-offloading=no
```

:::warning
現有連線可能不會受到 `l3-hw-offloading` 設定變更的影響。
:::

### L3HW 設定 {#l3hw-settings}

#### 基本設定 {#basic-settings}

L3HW Settings 選單可設定 Layer 3 Hardware Offloading 驅動程式的全域參數。

**子選單：** `/interface/ethernet/switch/l3hw-settings`

| 屬性 | 說明 |
| :-- | :-- |
| **autorestart** (*yes \| no*; 預設: **no**) | 發生錯誤時自動重新啟動 l3hw 驅動程式。否則，若發生錯誤，`l3-hw-offloading` 會被停用，且錯誤碼會顯示在交換器設定與 [#monitor](/docs/bridging-and-switching/l3-hardware-offloading#monitor) 中。自動重新啟動不適用於系統故障，例如 OOM (Out Of Memory)。 |
| **fasttrack-hw** (*yes \| no*; 預設: **yes**(if supported)) | 啟用或停用 FastTrack HW Offloading。除非需要保留 HW TCAM 記憶體，例如用於建立動態交換器 ACL 規則，否則請保持啟用。並非所有交換器晶片都支援 FastTrack HW Offloading（請參閱 **hw-supports-fasttrack**）。 |
| **ipv6-hw** (*yes \| no*; 預設: **no**) | 啟用或停用 IPv6 Hardware Offloading。由於 IPv6 路由會佔用大量硬體記憶體，請僅在 IPv6 流量速度足以從硬體路由獲益時啟用。 |
| **icmp-reply-on-error** (*yes \| no*; 預設: **yes**) | 由於硬體無法傳送 ICMP 訊息，發生錯誤時（例如「Time Exceeded」、「Fragmentation required」等），封包必須重新導向至 CPU 以傳送 ICMP 回覆。啟用 icmp-reply-on-error 有助於網路診斷，但可能開啟 DDoS 攻擊的潛在弱點。停用 icmp-reply-on-error 時，發生錯誤會直接在硬體層靜默丟棄封包。 |

**唯讀屬性**

| 屬性 | 說明 |
| :-- | :-- |
| **hw-supports-fasttrack** (**yes \| no**) | 指出硬體（交換器晶片）是否支援 FastTrack HW Offloading。 |

#### 進階設定 {#advanced-settings}

此選單可針對特定使用情境調整 l3hw 設定。

:::danger
除非 MikroTik Support 或 MikroTik Certified Routing Engineer 指示，否則不建議變更進階 L3HW 設定。套用不正確的設定可能會破壞 L3HW 運作。
:::

**子選單：** `/interface/ethernet/switch/l3hw-settings`

| 屬性 | 說明 |
| :-- | :-- |
| **route-queue-limit-high** (*number*; 預設: **256**) | 當 <strong>route-queue-size</strong>（請參閱 <a href="/docs/bridging-and-switching/l3-hardware-offloading#monitor">#monitor</a>）超過此值時，交換器驅動程式會停止路由索引。降低此值可加快路由處理，但會增加路由出現在 RouterOS 與進入硬體記憶體之間的延遲。<br/> 設定 <strong>route-queue-limit-high=0</strong> 時，只要處理佇列中有任何路由，就會停用路由索引；這是最有效率的 CPU 使用方式，但硬體解除卸載前的延遲最長。適用於只有靜態路由的情況。不建議與路由協定（例如 BGP 或 OSPF）一起使用，因為路由表會頻繁變更。 |
| **route-queue-limit-low** (*number*; 預設: **0**) | 當 <strong>route-queue-size</strong> 降至該值時，重新啟用路由索引。不得超過高限制。<br/> 設定 <strong>route-queue-limit-low=0</strong> 會讓交換器驅動程式在下次 hw-offloading 嘗試前處理所有待處理路由。雖然這是預期行為，但在持續 BGP feed 下，可能會完全阻斷 hw-offloading。 |
| **shwp-reset-counter** (*number*; 預設: **128**) | 在路由表變更達到此次數後，重設 Shortest HW Prefix（請參閱 <a href="/docs/bridging-and-switching/l3-hardware-offloading#monitor">#monitor</a> 中的 <strong>ipv4-shortest-hw-prefix</strong> / <strong>ipv6-shortest-hw-prefix</strong>），並嘗試完整路由表解除卸載。在部分解除卸載時，若整個路由表無法放入硬體記憶體，且較短的前綴會被重新導向至 CPU，則理論上沒有必要嘗試解除卸載比 SHWP 更短的路由前綴，因為無論如何都會被重新導向至 CPU。不過，路由表大幅變更可能導致不同的索引配置，進而改變可 hw-offloaded 的路由數量。因此建議偶爾執行完整資料表重新索引。<br/> 降低此值可能讓更多路由被 hw-offloaded，但會增加 CPU 使用率，反之亦然。設定 <strong>shwp-reset-counter=0</strong> 會在每次路由表變更後一律執行完整重新索引。<br/> 此設定僅在 Partial Offloading 期間使用，當 <strong>ipv4-shortest-hw-prefix=0</strong>（IPv6 亦同）時沒有作用。 |
| **partial-offload-chunk** (*number*; 預設: **1024**, min: 16) | Partial Offloading 中增量新增路由的最小數量。視交換器晶片型號而定，路由會以原樣解除卸載（RouterOS 中每個路由項目對應硬體記憶體中的一個項目），或建立索引，再由索引項目寫入硬體記憶體。此設定僅用於後者在 Partial Offloading 期間。<br/> 視索引分散程度而定，新增單一 IPv4 路由可能佔用 -3 到 +6 個 LPM 硬體記憶體區塊（某些路由新增可能因索引重組而降低所需硬體記憶體量）。因此，無法預測可放入硬體記憶體的確切路由數量。交換器驅動程式會使用二進位分割演算法找出可放入硬體的最大路由數量。<br/> 假設有 128k 條路由，全部都無法放入硬體記憶體。演算法會將數量減半，嘗試解除卸載 64k 條路由。假設解除卸載成功。下一次迭代中，演算法選擇 96k，假設失敗；接著 80k 再次失敗，72k 成功，76k 等，直到成功與失敗數量之間的差異低於 <strong>partial-offload-chunk</strong> 值。<br/> 降低 <strong>partial-offload-chunk</strong> 值會增加 hw-offloaded 路由數量，但也會提高 CPU 使用率，反之亦然。 |
| **route-index-delay-min** (*time*; 預設: **1s**) | 路由處理與其解除卸載之間的最小延遲。此延遲可讓更多路由一起處理並一次解除卸載，節省 CPU 使用率。它也可透過減少每條路由的處理工作，加快整個路由表的解除卸載。另一方面，會減慢單一路由的解除卸載。<br/> 若在此延遲期間收到額外路由，計時器會重設為 <strong>route-index-delay-min</strong> 值。在延遲期間持續新增更多路由，會不斷重設計時器，直到達到 <strong>route-index-delay-max</strong>。 |
| **route-index-delay-max** (*time*; 預設: **10s**) | 路由處理與其解除卸載之間的最大延遲。達到最大延遲時，即使仍有更多路由待處理，已處理的路由仍會被解除卸載。不過，**route-queue-limit-high** 的優先順序高於此設定，表示達到特定佇列大小時，索引／解除卸載仍會暫停。 |
| **neigh-keepalive-interval** (*time*; 預設: **15s**, min: 5s) | 鄰居（主機）keepalive 間隔。當主機（IP 鄰居）被 hw-offloaded 時，所有往返它的流量都由交換器晶片路由，RouterOS 可能認為該鄰居處於非作用中並將其刪除。為避免這種情況，交換器驅動程式必須定期向 RouterOS 傳送重新整理，以維持已解除卸載鄰居的活動狀態。 |
| **neigh-discovery-interval** (*time*; 預設: **1m37s**, min: 30s) | 可惜的是，交換器晶片不提供個別鄰居統計資料。因此，檢查已解除卸載主機是否仍處於活動狀態的唯一方法，是偶爾向連線網路傳送 ARP (IPv4) / Neighbor Discovery (IPv6) 要求。提高此值可降低廣播流量，但可能讓非作用中在主機硬體記憶體中停留更久。<br/> 鄰居探索會在鄰居 keepalive 工作中觸發。因此，探索時間會進位至下一次 keepalive 工作階段。請選擇無法被 <strong>neigh-keepalive-interval</strong> 整除的 <strong>neigh-discovery-interval</strong> 值，以在不同工作階段傳送 ARP/ND 要求，避免廣播暴增。 |
| **neigh-discovery-burst-limit**(*number*; 預設: **64**) | 一次可傳送的 ARP/ND 要求數量上限。 |
| **neigh-discovery-burst-delay** (*time*; 預設: **300ms**, min: 10ms) | 當要求數量超過 **neigh-discovery-burst-limit** 時，ARP/ND 後續突發之間的延遲。 |

:::info
部分設定僅適用於特定交換器型號。
:::

#### Monitor

L3HW Monitor 功能已於 RouterOS 7.10 版引入。它可監控與 L3HW 相關的交換器晶片與驅動程式統計資料。

```ros
/interface/ethernet/switch/l3hw-settings/monitor
        ipv4-routes-total: 99363
           ipv4-routes-hw: 61250
          ipv4-routes-cpu: 38112
  ipv4-shortest-hw-prefix: 24
               ipv4-hosts: 87
        ipv6-routes-total: 15
           ipv6-routes-hw: 11
          ipv6-routes-cpu: 4
  ipv6-shortest-hw-prefix: 0
               ipv6-hosts: 7
         route-queue-size: 118
     fasttrack-ipv4-conns: 2031
   fasttrack-hw-min-speed: 0
              nexthop-cap: 8192
            nexthop-usage: 93
    vxlan-mtu-packet-drop: 0
```

**Stats**

| 屬性 | 說明 |
| :-- | :-- |
| **ipv4-routes-total** | 由交換器驅動程式處理的 IPv4 路由總數。 |
| **ipv4-routes-hw** | 已由硬體卸載的 IPv4 路由數（亦稱硬體路由） |
| **ipv4-routes-cpu** | 已重新導向至 CPU 的 IPv4 路由數（亦稱軟體路由） |
| **ipv4-shortest-hw-prefix** | IPv4 的 *Shortest Hardware Prefix (SHWP)*。若整個 IPv4 路由表無法放入硬體記憶體，則會套用 *partial offloading*，較長的前綴會由硬體卸載，而較短的前綴會重新導向至 CPU。此欄位顯示已卸載至硬體記憶體的最短路由前綴（/x）。所有比此值更短的前綴都會由 CPU 處理。`ipv4-shortest-hw-prefix=0` 表示整個 IPv4 路由表已卸載至硬體記憶體。 |
| **ipv4-hosts** | 已由硬體卸載的 IPv4 主機數（/32 路由） |
| **ipv6-routes-total** <sup>1</sup> | 由交換器驅動程式處理的 IPv6 路由總數。 |
| **ipv6-routes-hw** <sup>1</sup> | 已由硬體卸載的 IPv6 路由數（亦稱硬體路由） |
| **ipv6-routes-cpu** <sup>1</sup> | 已重新導向至 CPU 的 IPv6 路由數（亦稱軟體路由） |
| **ipv6-shortest-hw-prefix** <sup>1</sup> | IPv6 的 *Shortest Hardware Prefix (SHWP)*。若整個 IPv6 路由表無法放入硬體記憶體，則會套用 *partial offloading*，較長的前綴會由硬體卸載，而較短的前綴會重新導向至 CPU。此欄位顯示已卸載至硬體記憶體的最短路由前綴（/x）。所有比此值更短的前綴都會由 CPU 處理。`ipv6-shortest-hw-prefix=0` 表示整個 IPv6 路由表已卸載至硬體記憶體。 |
| **ipv6-hosts** <sup>1</sup> | 已由硬體卸載的 IPv6 主機數（/128 路由） |
| **route-queue-size** | 在佇列中等待交換器晶片驅動程式處理的路由數。在正常運作情況下，此欄位為 0，表示所有路由都已由驅動程式處理。 |
| **nexthop-cap** | nexthop 容量。 |
| **nexthop-usage** | 目前使用的 nexthop 數量。 |
| **vxlan-mtu-packet-drop** | 因超過介面 MTU 設定而遭捨棄的 VXLAN 封包數。 |
| **fasttrack-ipv4-conns** <sup>2</sup> | 已由硬體卸載的 FastTrack 連線數。 |
| **fasttrack-hw-min-speed** <sup>2</sup> | 當用於儲存 FastTrack 的硬體記憶體已滿時，此欄位會顯示已由硬體卸載的 FastTrack 連線的最低速度（每秒位元組數）。較慢的連線會由 CPU 路由。 |

---

<sup>1</sup> IPv6 stats appear only when IPv6 hardware routing is enabled (`ipv6-hw=yes`)  
<sup>2</sup> FastTrack stats appear only when hardware offloading of FastTrack connections is enabled (`fasttrack-hw=yes`)

#### 進階監控 {#advanced-monitor}

Monitor 的增強版本，為進階使用者提供額外的遙測資料。Advanced Monitor 包含基本 monitor 的所有資料，以及下列欄位。

```ros
/interface/ethernet/switch/l3hw-settings/advanced> monitor once
        ipv4-routes-total: 29968
           ipv4-routes-hw: 29957
          ipv4-routes-cpu: 11
  ipv4-shortest-hw-prefix: 0
               ipv4-hosts: 3
        ipv6-routes-total: 4
           ipv6-routes-hw: 0
          ipv6-routes-cpu: 4
  ipv6-shortest-hw-prefix: 0
               ipv6-hosts: 0
         route-queue-size: 0
         route-queue-rate: 0
       route-process-rate: 0
     fasttrack-ipv4-conns: 0
     fasttrack-queue-size: 0
     fasttrack-queue-rate: 0
   fasttrack-process-rate: 0
   fasttrack-hw-min-speed: 0
   fasttrack-hw-offloaded: 0
    fasttrack-hw-unloaded: 0
                  lpm-cap: 54560
                lpm-usage: 31931
             lpm-bank-cap: 2728
           lpm-bank-usage: 46,0,0,0,2589,2591,1983,0,2728,2728,2728,2728,2728,2728,2728,2728,2728,170,0,0
                  pbr-cap: 8192
                pbr-usage: 0
             pbr-lpm-bank: 3
                nat-usage: 0
              nexthop-cap: 8192
            nexthop-usage: 85
```

**Stats**

| 屬性 | 說明 |
| :-- | :-- |
| **route-queue-rate** | 路由新增至佇列等待交換器驅動程式處理的速率。換句話說，即 **route-queue-size** 的成長速率（每秒路由數） |
| **route-process-rate** | 先前佇列中的路由由交換器驅動程式處理的速率。換句話說，即 **route-queue-size** 的縮減速率（每秒路由數） |
| **fasttrack-queue-size** | 在佇列中等待交換器晶片驅動程式處理的 FastTrack 連線數。 |
| **fasttrack-queue-rate** | FastTrack 連線新增至佇列等待交換器驅動程式處理的速率。換句話說，即 **fasttrack-queue-size** 的成長速率（每秒連線數） |
| **fasttrack-process-rate** | 先前佇列中的 FastTrack 連線由交換器驅動程式處理的速率。換句話說，即 **fasttrack-queue-size** 的縮減速率（每秒連線數） |
| **fasttrack-hw-offloaded** | 已卸載至硬體的 FastTrack 連線數。計數器每秒（或每個 monitor interval）重設一次。 |
| **fasttrack-hw-unloaded** | 已從硬體卸載的 FastTrack 連線數（重新導向至軟體路由）。計數器每秒（或每個 monitor interval）重設一次。 |
| **lpm-cap** | LPM 硬體表的大小（LPM = Longest Prefix Match）。LPM 會儲存硬體路由的路由索引。並非所有交換器晶片型號都使用 LPM，其他型號會使用 TCAM。 |
| **lpm-usage** | 已使用的 LPM 區塊數。**lpm-usage**/ **lpm-cap** = 使用率百分比。 |
| **lpm-bank-cap** | LPM 記憶體以 bank 組織，bank 是特殊的記憶體單位。bank 大小取決於交換器晶片型號。此值顯示單一 bank 的大小（以 LPM 區塊為單位）。**lpm-cap** / **lpm-bank-cap** = bank 數量（通常為 20）。 |
| **lpm-bank-usage** | 各 bank 的 LPM 使用量（以 LPM 區塊為單位） |
| **pbr-cap** | Policy-Based Routing（PBR）硬體表的大小。PBR 用於 FastTrack 連線的 NAT 卸載。 |
| **pbr-usage** | 已使用的 PBR 項目數。**pbr-usage**/ **pbr-cap** = 使用率百分比。 |
| **pbr-lpm-bank** | PBR 與路由表共用 LPM 記憶體 bank。此值顯示與 PBR 共用的 LPM bank 索引（0 = 第一個 bank）。 |
| **nat-usage** | 已使用的 NAT 硬體項目數（適用於 FastTrack 連線）。 |

### 介面清單 {#interface-lists}

無法直接使用介面清單控制 `l3-hw-offloading`，因為介面清單可能包含虛擬介面（例如 VLAN），而 `l3-hw-offloading` 設定必須僅套用於實體交換器埠。例如，若有兩個 VLAN 介面（vlan20 與 vlan30）執行在同一個交換器埠（trunk 埠）上，就無法在 vlan20 上啟用硬體路由，同時在 vlan30 上保持停用。

不過，介面清單也可作為埠選擇器。下列範例示範如何在 LAN 埠（屬於「LAN」介面清單的埠）上啟用硬體路由，並在 WAN 埠上停用硬體路由：

```ros
:foreach i in=[/interface/list/member/find where list=LAN] do={
    /interface/ethernet/switch/port/set [/interface/list/member/get $i interface] l3-hw-offloading=yes
}

:foreach i in=[/interface/list/member/find where list=WAN] do={
    /interface/ethernet/switch/port/set [/interface/list/member/get $i interface] l3-hw-offloading=no
}
```

請注意，由於介面清單不會直接用於硬體路由控制，**修改介面清單也不會自動反映在 l3hw 變更中**。例如，將交換器埠加入「LAN」介面清單，並不會自動在該埠上啟用 `l3-hw-offloading`。使用者必須重新執行上述指令碼，才能套用變更。

### MTU

硬體支援最多 8 個 MTU 設定檔，這表示使用者可以為介面設定最多 8 種不同的 MTU 值：預設 1500 加上 7 個自訂值。

:::tip
建議在變更介面上的 MTU/L2MTU 值時停用 `l3-hw-offloading`。
:::

**MTU 變更範例**

```ros
/interface/ethernet/switch/set 0 l3-hw-offloading=no
/interface/set sfp-sfpplus1 mtu=9000 l2mtu=9022
/interface/set sfp-sfpplus2 mtu=9000 l2mtu=9022
/interface/set sfp-sfpplus3 mtu=10000 l2mtu=10022
/interface/ethernet/switch/set 0 l3-hw-offloading=yes
```

### 第 2 層相依性 {#layer-2-dependency}

第 3 層硬體處理位於第 2 層硬體處理之上。因此，L3HW offloading 需要在底層介面上啟用 L2HW offloading。後者預設啟用，但有一些例外。例如，搭載 Marvell Prestera 交換器的 MikroTik 設備僅支援一個硬體橋接器。如果有多個橋接器，其他橋接器會由 CPU 處理，且不適用 L3HW。

另一個範例是 ACL 規則。如果規則將流量重新導向至 CPU 進行軟體處理，則不會觸發硬體路由（L3HW）：

#### 在特定埠上停用硬體處理的 ACL 規則 {#acl-rule-to-disable-hardware-processing-on-a-specific-port}

```ros
/interface/ethernet/switch/rule/add switch=switch1 ports=ether1 redirect-to-cpu=yes
```

:::tip
建議在設定 L2 時關閉 L3HW offloading。
:::

為確保軟體與硬體兩側的 Layer 3 與 Layer 2 保持同步，建議在設定 Layer 2 功能時停用 L3HW。此建議適用於下列設定：

- 新增／移除／啟用／停用 bridge。
- 在 bridge 中新增／移除交換器埠。
- 綁定交換器埠／移除綁定。
- 變更 VLAN 設定。
- 變更交換器埠的 MTU／L2MTU。
- 變更 ethernet（MAC）位址。

簡言之，在 `/interface/bridge/` 與 `/interface/vlan/` 下進行變更時，請停用 `l3-hw-offloading`：

#### Layer 2 設定範本 {#layer-2-configuration-template}

```ros
/interface/ethernet/switch/set 0 l3-hw-offloading=no

/interface/bridge
# put bridge configuration changes here

/interface/vlan
# define/change VLAN interfaces
/interface/ethernet/switch/set 0 l3-hw-offloading=yes
```

### MAC telnet

當 **98DX8xxx**、**98DX4xxx,** 或 **98DX325x** 交換器晶片啟用 L3HW offloading 時，MAC telnet 有一項限制。來自 MAC Telnet 的封包會被丟棄，且不會送達 CPU，因此將無法存取設備。

若希望搭配 L3HW 使用 MAC telnet，可以建立特定 ACL 規則，強制將這些封包導向 CPU。

例如，若需要在 sfp-sfpplus1 與 sfp-sfpplus2 上啟用 MAC telnet 存取，請新增此 ACL 規則。也可以使用 `ports` 設定選取更多介面。

```ros
/interface/ethernet/switch/rule
add dst-port=20561 ports=sfp-sfpplus1,sfp-sfpplus2 protocol=udp redirect-to-cpu=yes switch=switch1
```

### VLAN 間路由 {#inter-vlan-routing}

由於 L3HW 依賴 L2HW，而 L2HW 負責處理 VLAN，因此 Inter-VLAN *硬體* 路由需要底層具備硬體橋接器。即使特定 VLAN 只有一個 tagged 埠成員，該埠也必須是橋接器成員。請勿將 VLAN 介面直接指派到交換器埠！否則 L3HW offloading 會失敗，流量將由 CPU 處理：

`/interface/vlan/add interface=ether2 name=vlan20 vlan-id=20`

請改為將 VLAN 介面指派到橋接器。如此一來，VLAN 設定會卸載到硬體，並在啟用 L3HW 時，讓流量進行 Inter-VLAN 硬體路由。

#### VLAN 設定範例 {#vlan-configuration-example}

```ros
/interface/ethernet/switch/set 0 l3-hw-offloading=no
/interface/bridge/port/add bridge=bridge interface=ether2
/interface/bridge/vlan/add bridge=bridge tagged=bridge,ether2 vlan-ids=20
/interface/vlan/add interface=bridge name=vlan20 vlan-id=20
/ip/address/add address=192.0.2.1/24 interface=vlan20
/interface/bridge/set bridge vlan-filtering=yes
/interface/ethernet/switch/set 0 l3-hw-offloading=yes
```

:::info
對於 Inter-VLAN 路由，橋接器介面必須是每個可路由 `/interface/bridge/vlan/` 項目的 tagged 成員。
:::

### 個別 VLAN offloading {#per-vlan-offloading}

自 RouterOS 7.21 起，可在 `/interface/vlan` 選單中使用 `l3-hw-offloading=yes|no` 設定，為個別 VLAN 介面設定 L3HW 卸載。這可更精細地控制哪些 VLAN（與其相關路由）會卸載至交換器晶片，以及哪些由 CPU 處理。若要停用特定 VLAN 的 L3HW 路由，不再需要停用交換器埠上的 L3HW。

只有在符合下列所有條件時，VLAN 介面才會被卸載（取得 H 旗標）：

- VLAN 介面具有 `l3-hw-offloading=yes`。
- VLAN 介面建立於已啟用硬體卸載且啟用 vlan-filtering 的橋接器上。
- 屬於該 VLAN 的所有交換器埠都具有 l3-hw-offloading=yes。

對於 VLAN 間路由，ingress 與 egress VLAN 都必須啟用硬體卸載，否則封包會傳送至 CPU。

:::info
如果交換器埠承載多個具有不同 L3HW 設定的 VLAN，請保持該埠的 `l3-hw-enabled=yes`。
:::

### L3HW MAC 位址範圍限制（僅限 DX2000/DX3000 系列） {#l3hw-mac-address-range-limitation-dx2000dx3000-series-only}

Marvell Prestera DX2000 與 DX3000 交換器晶片有一項硬體限制，只允許為每個介面設定 MAC 位址的最後一個（最低有效）位元組。其他五個（最高有效）位元組是全域設定，因此所有介面（交換器埠、橋接器、VLAN）都必須相同。換句話說，MAC 位址必須採用「**XX:XX:XX:XX:XX:??**」格式，其中：

- 「**XX:XX:XX:XX:XX**」部分是所有介面共用的。
- 「**??**」是可變部分。

**此需求僅適用於 Layer 3（路由）。** Layer 2（橋接）不會使用交換器的 ethernet 位址。此外，此需求不適用於 bridge 埠，因為它們使用 bridge 的 MAC 位址。

共同五個 octet 的需求適用於：

- 已啟用硬體路由的獨立交換器埠（非 bridge 成員）（`l3-hw-offloading=yes`）。
- bridge 本身。
- VLAN 介面（預設使用 bridge MAC 位址的介面）。

## 路由設定 {#route-configuration}

---

### 抑制 HW Offload {#suppressing-hw-offload}

預設所有路由都是硬體候選路由。若要進一步微調要 offload 的流量，每條路由都有一個選項可停用／啟用 **`suppress-hw-offload`**。

例如，如果我們知道大部分流量都流向伺服器所在的網路，可以只對該特定目的地啟用 offloading：

```ros
/ip/route/set [find where static && dst-address!="192.168.3.0/24"] suppress-hw-offload=yes
```

現在只有通往 192.168.3.0/24 的路由具有 H 旗標，表示它將是唯一符合資格被選進行 HW offloading 的路由：

```ros
[admin@MikroTik] > /ip/route/print where static
Flags: A - ACTIVE; s - STATIC, y - COPY; H - HW-OFFLOADED
Columns: DST-ADDRESS, GATEWAY, DISTANCE
#     DST-ADDRESS       GATEWAY         D
0 As  0.0.0.0/0         172.16.2.1      1
1 As  10.0.0.0/8        10.155.121.254  1
2 AsH 192.168.3.0/24    172.16.2.1      1
```

:::danger
H-flag 並不表示該路由實際上已由硬體卸載；它只表示該路由可被選取進行硬體卸載。
:::

### 路由篩選器 {#routing-filters}

對於 OSPF 與 BGP 等動態路由協定，可以使用[路由篩選器](/docs/user-guides/routing-and-networking-protocols/route-selection-and-filtering)抑制硬體卸載。例如，若要抑制所有 OSPF instance 路由的硬體卸載，請使用 "**`suppress-hw-offload yes`**" 屬性：

```ros
/routing/ospf/instance
set [find name=instance1] in-filter-chain=ospf-input
/routing/filter/rule
add chain="ospf-input" rule="set suppress-hw-offload yes; accept"
```

### 卸載 Fasttrack 連線 {#offloading-fasttrack-connections}

防火牆篩選規則具有 Fasttrack 的 **`hw-offload`** 選項，可讓連線卸載進行細部調整。由於 Fasttrack 連線可用的硬體記憶體非常有限，因此我們可以選擇要卸載的連線類型，進而享有接近線速的流量表現。下列範例只卸載 TCP 連線，而 UDP 封包則由 CPU 路由，且不佔用硬體記憶體：

```ros
/ip/firewall/filter
add action=fasttrack-connection chain=forward connection-state=established,related hw-offload=yes protocol=tcp
add action=fasttrack-connection chain=forward connection-state=established,related hw-offload=no
add action=accept chain=forward connection-state=established,related
```

### 無狀態硬體防火牆 {#stateless-hardware-firewall}

連線追蹤與狀態式防火牆只能由 CPU 執行，而硬體可以透過[交換器規則（ACL）](/docs/bridging-and-switching/marvell-prestera-switch-chip-features#switch-rules-acl)執行無狀態防火牆。下列範例會在硬體層級阻止從 ether1 存取 MySQL 伺服器，並將來自 ether2 與 ether3 的封包重新導向至 CPU／Firewall：

```ros
/interface/ethernet/switch/rule
add switch=switch1 dst-address=10.0.1.2/32 dst-port=3306 ports=ether1 new-dst-ports=""
add switch=switch1 dst-address=10.0.1.2/32 dst-port=3306 ports=ether2,ether3 redirect-to-cpu=yes
```

### 交換器規則（ACL）與 Fasttrack 硬體卸載的比較 {#switch-rules-acl-vs-fasttrack-hw-offloading}

部分防火牆規則可以同時透過[交換器規則（ACL）](/docs/bridging-and-switching/marvell-prestera-switch-chip-features#switch-rules-acl)與 CPU [Firewall Filter](/docs/firewall-and-quality-of-service/firewall/filter) + Fasttrack HW Offloading 實作。兩種選項都能提供接近線速的效能。那麼應該使用哪一種？

首先，[並非所有設備都支援 Fasttrack HW Offloading](/docs/bridging-and-switching/l3-hardware-offloading#l3hw-device-support)，若沒有 HW offloading，Firewall Filter 只會使用軟體路由，速度會遠慢於硬體對應方案。其次，即使可以使用 Fasttrack HW Offloading，也有個簡單原則：

:::tip
可能的話，請一律使用 Switch Rules（ACL）。
:::

交換器規則與 Fasttrack 連線共用硬體記憶體。不過，硬體資源會配置給每個 Fasttrack 連線，而單一 ACL 規則可以比對多個連線。例如，若你有一個訪客 WiFi 網路連接到 sfp-sfpplus1 VLAN 10，而且不希望它存取內部網路，只要建立一條 ACL 規則：

```ros
/interface/ethernet/switch/rule
add switch=switch1 ports=sfp-sfpplus1 vlan-id=10 dst-address=10.0.0.0/8 new-dst-ports=""
```

比對到的封包會在硬體層級被丟棄。這比讓*所有*訪客封包都送到 CPU 進行防火牆篩選要好得多。

當然，ACL 規則無法比對所有項目。例如，ACL 規則無法篩選連線狀態：接受 established，丟棄其他連線。這時就輪到 Fasttrack HW Offloading 發揮作用：預設將封包重新導向到 CPU 進行防火牆篩選，然後卸載已建立的 Fasttrack 連線。不過，針對整個交換器或埠停用 `l3-hw-offloading` 並不是唯一的選項。

:::info
請定義具有 `redirect-to-cpu=yes` 的 ACL 規則，而不要在交換器埠上設定 `l3-hw-offloading=no`，以縮小送往 CPU 的流量範圍。
:::

### 硬體卸載 VRF {#hardware-offloaded-vrf}

硬體卸載 VRF 支援於 [98DX8xxx、98DX4xxx、98DX325x、98CX8410](#ccr2xxx-crs3xx-crs5xx-switch-98dx8xxx-and-98dx4xxx-series) 與 [98DX7xxx](#crs8xx-switch-98dx7xxx-series) 交換器晶片。不支援 [98DX3xxx 與 98DX2xxx](#crs3xx-switch-98dx3xxx-and-98dx2xxx-series) 系列。

如果路由位於 VRF 中，且出口介面具備 L3HW 能力，交換器晶片將路由該封包。您可以將任何具備 L3HW 能力的介面（Ethernet、bonding、bridge、VLAN）與 VRF 建立關聯。請務必將主介面與 VRF 建立關聯，而不是標記為 `S`（slave）旗標的介面，例如 bridge 或 bonding 埠。Fasttrack、NAT 與 VXLAN 卸載僅限於 `main` 路由表。

VRF 在 `/ip/vrf` 下設定。如需詳細資訊，請參閱 [VRF](/docs/user-guides/routing-and-networking-protocols/vrf) 手冊。

98DX8208、98DX8212、98DX8332、98DX3257、98DX3255 支援最多 512 個 VRF 表。其他所有支援的交換器晶片支援最多 1024 個。

#### 透過 ACL 指派 VRF {#vrf-assignment-via-acl}

L3HW 支援使用 ACL 交換器規則將 VRF 指派給入口流量。`/interface/ethernet/switch/rule` 中的 `new-vrf` 選項可將符合條件的封包導向特定 VRF 表。

在不支援 VRF 的交換器（98DX3xxx 與 98DX2xxx 系列）上，將 `new-vrf` 設為 `main` 以外的值會導致 `redirect-to-cpu=yes`。

如需 ACL 規則的詳細資訊，請參閱 [Switch Rules (ACL)](/docs/bridging-and-switching/marvell-prestera-switch-chip-features#switch-rules-acl)。

## 設定範例 {#configuration-examples}

---

### 上游埠位於 Firewall/NAT 後方的 VLAN 間路由 {#inter-vlan-routing-with-upstream-port-behind-firewallnat}

此範例示範如何在上游埠上維持 Firewall 與 NAT 運作的同時，享受接近線速的 VLAN 間路由效益。此外，通往上游埠的 Fasttrack 連線也會卸載到硬體，使流量速度提升至接近線速。VLAN 間流量完全由硬體路由，不會進入 CPU/Firewall，因此也不會佔用 Fasttrack 連線的硬體記憶體。

我們使用 **CRS317-1G-16S+** 機型，並採用以下設定：

- sfp1-sfp4 - 橋接埠，VLAN ID 20，未標記。
- sfp5-sfp8 - 橋接埠，VLAN ID 30，未標記。
- sfp16 - 上游埠。
- ether1 - 管理埠。

設定介面清單，以便存取：

### 介面清單 {#interface-lists-1}

```ros
/interface/list
add name=LAN
add name=WAN
add name=MGMT 

/interface/list/member
add interface=sfp-sfpplus1 list=LAN
add interface=sfp-sfpplus2 list=LAN
add interface=sfp-sfpplus3 list=LAN
add interface=sfp-sfpplus4 list=LAN
add interface=sfp-sfpplus5 list=LAN
add interface=sfp-sfpplus6 list=LAN
add interface=sfp-sfpplus7 list=LAN
add interface=sfp-sfpplus8 list=LAN
add interface=sfp-sfpplus16 list=WAN
add interface=ether1 list=MGMT 
```

### Bridge 設定 {#bridge-setup}

```ros
/interface/bridge
add name=bridge vlan-filtering=yes

/interface/bridge/port
add bridge=bridge interface=sfp-sfpplus1 pvid=20
add bridge=bridge interface=sfp-sfpplus2 pvid=20
add bridge=bridge interface=sfp-sfpplus3 pvid=20
add bridge=bridge interface=sfp-sfpplus4 pvid=20
add bridge=bridge interface=sfp-sfpplus5 pvid=30
add bridge=bridge interface=sfp-sfpplus6 pvid=30
add bridge=bridge interface=sfp-sfpplus7 pvid=30
add bridge=bridge interface=sfp-sfpplus8 pvid=30

/interface/bridge/vlan
add bridge=bridge tagged=bridge untagged=sfp-sfpplus1,sfp-sfpplus2,sfp-sfpplus3,sfp-sfpplus4 vlan-ids=20
add bridge=bridge tagged=bridge untagged=sfp-sfpplus5,sfp-sfpplus6,sfp-sfpplus7,sfp-sfpplus8 vlan-ids=30
```

路由需要專用的 VLAN 介面。對於標準 L2 VLAN 橋接（不含 VLAN 間路由），可以略過下一步。

#### 用於路由的 VLAN 介面設定 {#vlan-interface-setup-for-routing}

```ros
/interface/vlan
add interface=bridge name=vlan20 vlan-id=20
add interface=bridge name=vlan30 vlan-id=30

/ip/address
add address=192.168.20.17/24 interface=vlan20 network=192.168.20.0
add address=192.168.30.17/24 interface=vlan30 network=192.168.30.0
```

設定管理埠與上游埠、基本防火牆、NAT，並啟用 Fasttrack 連線的硬體卸載：

#### 防火牆設定 {#firewall-setup}

```ros
/ip/address
add address=192.168.88.1/24 interface=ether1
add address=10.0.0.17/24 interface=sfp-sfpplus16

/ip/route
add gateway=10.0.0.1

/ip/firewall/filter
add action=fasttrack-connection chain=forward connection-state=established,related hw-offload=yes
add action=accept chain=forward connection-state=established,related

/ip/firewall/nat
add action=masquerade chain=srcnat out-interface-list=WAN
```

此時，所有路由仍由 CPU 執行。在交換器晶片上啟用硬體路由：

#### 啟用 Layer 3 硬體卸載 {#enable-layer-3-hardware-offloading}

```ros
# Enable full hardware routing on LAN ports
:foreach i in=[/interface/list/member/find where list=LAN] do={ 
    /interface/ethernet/switch/port/set [/interface/list/member/get $i interface] l3-hw-offloading=yes 
} 

# Disable full hardware routing on WAN or Management ports
:foreach i in=[/interface/list/member/find where list=WAN or list=MGMT] do={ 
    /interface/ethernet/switch/port/set [/interface/list/member/get $i interface] l3-hw-offloading=no 
}

# Activate Layer 3 Hardware Offloading on the switch chip
/interface/ethernet/switch/set 0 l3-hw-offloading=yes
```

Results:

- 在同一 VLAN 內（例如 sfp1-sfp4），流量由硬體在 Layer 2 轉送 *(L2HW)*。
- VLAN 間流量（例如 sfp1-sfp5）由硬體在 Layer 3 路由 *(L3HW)。*
- 往返 WAN 埠的流量會先由 CPU／防火牆處理。接著 Fasttrack 連線會卸載至硬體 *(Hardware-Accelerated L4 Stateful Firewall)。* NAT 會套用於由 CPU 與硬體處理的封包。
- 前往管理埠的流量受到防火牆保護。

## 常見錯誤設定 {#typical-misconfiguration}

---
以下是設定 Layer 3 Hardware Offloading 時常見的使用者錯誤。

### 交換器埠或 bond 上的 VLAN 介面 {#vlan-interface-on-a-switch-port-or-bond}

```ros
/interface/vlan
add name=vlan10 vlan-id=10 interface=sfp-sfpplus1
add name=vlan20 vlan-id=20 interface=bond1
```

由於 Layer 2 相依性，只有在啟用硬體卸載且啟用 vlan-filtering 的 bridge 上建立的 VLAN 介面，才支援 L3HW 卸載。正確設定如下：

```ros
/interface/bridge/port
add bridge=bridge1 interface=sfp-sfpplus1 frame-types=admit-only-vlan-tagged
add bridge=bridge1 interface=bond1 frame-types=admit-only-vlan-tagged
 
/interface/bridge/vlan
add bridge=bridge1 tagged=bridge1,sfp-sfpplus1 vlan-ids=10
add bridge=bridge1 tagged=bridge1,bond1 vlan-ids=20
 
/interface/vlan
add name=vlan10 vlan-id=10 interface=bridge1
add name=vlan20 vlan-id=20 interface=bridge1
```

:::warning
若直接在 Ethernet 或 bonding 介面上建立 VLAN 介面，封包可能會被錯誤地卸載，略過 CPU 處理（例如防火牆與 NAT），並造成未定義行為。

若需要這類設定，必須在 `/interface/ethernet/switch/port` 選單中，將相關交換器埠的 `l3-hw-offloading=no`，以停用 L3HW 卸載。
:::

### 未將 bridge 介面加入 /interface/bridge/vlan/ {#not-adding-the-bridge-interface-to-interfacebridgevlan}

若要進行 Inter-VLAN 路由，bridge 介面本身必須加入指定 VLAN 的 tagged 成員。在下列範例中，Inter-VLAN 路由可在 VLAN 10 與 11 之間運作，但封包不會被路由至 VLAN 20。

```ros
/interface/bridge/vlan
add bridge=bridge1 vlan-ids=10 tagged=bridge1,sfp-sfpplus1
add bridge=bridge1 vlan-ids=11 tagged=bridge1 untagged=sfp-sfpplus2,sfp-sfpplus3 
add bridge=bridge1 vlan-ids=20 tagged=sfp-sfpplus1 untagged=sfp-sfpplus4,sfp-sfpplus5
```

上述範例不一定代表錯誤。有時，您可能希望設備在部分或所有 VLAN 中作為簡單的 L2 交換器。請確認這類行為是刻意設定的，而非設定錯誤所致。

### 建立多個 bridge {#creating-multiple-bridges}

這些設備僅支援一個硬體橋接器。如果建立了多個橋接器，只有其中一個會取得硬體卸載。對於 L2 而言，這表示其他橋接器會使用軟體轉送；而在 L3HW 的情況下，多個橋接器可能導致未定義的行為。

:::tip
請不要建立多個橋接器，而是建立一個橋接器，並使用 VLAN 篩選隔離 L2 網路。
:::

### 使用不屬於交換器的埠 {#using-ports-that-do-not-belong-to-the-switch}

有些設備具有兩顆交換器晶片，或管理埠直接連接到 CPU。例如，**CRS312-4C+8XG** 的 **ether9** 埠連接到獨立的交換器晶片。嘗試將此埠加入橋接器，或讓它參與 L3HW 設定，會導致非預期的結果。請保留管理埠用於管理！

```ros
[admin@crs312] /interface/ethernet/switch> print
Columns: NAME, TYPE, L3-HW-OFFLOADING
# NAME     TYPE              L3-HW-OFFLOADING
0 switch1  Marvell-98DX8212  yes            
1 switch2  Atheros-8227      no   
           
[admin@crs312] /interface/ethernet/switch> port print
Columns: NAME, SWITCH, L3-HW-OFFLOADING, STORM-RATE
 # NAME         SWITCH   L3-HW-OFFLOADING  STORM-RATE
 0 ether9       switch2                             
 1 ether1       switch1  yes                      100
 2 ether2       switch1  yes                      100
 3 ether3       switch1  yes                      100
 4 ether4       switch1  yes                      100
 5 ether5       switch1  yes                      100
 6 ether6       switch1  yes                      100
 7 ether7       switch1  yes                      100
 8 ether8       switch1  yes                      100
 9 combo1       switch1  yes                      100
10 combo2       switch1  yes                      100
11 combo3       switch1  yes                      100
12 combo4       switch1  yes                      100
13 switch1-cpu  switch1                           100
14 switch2-cpu  switch2
```

### 過度依賴 Fasttrack HW Offloading {#relying-on-fasttrack-hw-offloading-too-much}

由於 Fasttrack HW Offloading 提供接近線速的效能，且幾乎不需要額外設定，使用者往往會將其當作預設解決方案。不過，HW Fasttrack 連線的數量非常有限，其他流量仍會留給 CPU 處理。請盡可能使用硬體路由，透過交換器 ACL 規則將 CPU 流量降至最低，然後再透過防火牆篩選規則微調要卸載哪些 Fasttrack 連線。

### 嘗試卸載 slow-path 連線 {#trying-to-offload-slow-path-connections}

使用特定設定（例如啟用橋接器「**use-ip-firewall**」設定、建立橋接器 nat/filter 規則），或執行 sniffer、torch 等特定功能，可能會停用 RouterOS [FastPath](/docs/firewall-and-quality-of-service/packet-flow-in-routeros#fast-path)，進而影響連線是否能夠正確 FastTrack 與硬體卸載。如果需要 HW offloaded Fasttrack，請確認沒有會停用 FastPath 的設定，並驗證連線是否取得「H」旗標，或使用 L3HW [monitor](/docs/bridging-and-switching/l3-hardware-offloading#monitor) 指令查看已硬體卸載的連線數量。

## L3HW 功能支援 {#l3hw-feature-support}

- **HW** - 此功能受支援，並會卸載到硬體。
- **CPU** - 此功能受支援，但由軟體（CPU）執行。
- **N/A** - 此功能無法與 L3HW 一起使用。必須完全停用第 3 層硬體卸載（**switch** `l3-hw-offloading=no`），此功能才會運作。
- **FW** - 此功能需要給定的 **switch port** 設定 `l3-hw-offloading=no`。在 **switch** 層級，`l3-hw-offloading=yes`。

| 功能 | 支援 | 備註 | 版本 |
| :-- | :-- | :-- | :-- |
| IPv4 Unicast Routing | **HW** |  | 7.1 |
| IPv6 Unicast Routing | **HW** | <br/><code>/interface/ethernet/switch/l3hw-settings/set ipv6-hw=yes</code><br/> | 7.6 |
| IPv4 Multicast Routing | **CPU** |  |  |
| IPv6 Multicast Routing | **CPU** |  |  |
| ECMP | **HW** | 多路徑路由。L3HW 使用交換器晶片本身的 ECMP 雜湊遮罩，其中包含 TCP/UDP 的 L4 埠；對於硬體轉送的 ECMP，所設定的雜湊原則會被忽略。FastTrack 卸載的連線會遵循核心 FIB 查詢，並可能選取不同的下一跳。[FastPath](/docs/firewall-and-quality-of-service/packet-flow-in-routeros#fast-path) 會依 L3 快取路由。 | 7.1 |
| Blackholes | **HW** | <br/><code>/ip/route/add dst-address=10.0.99.0/24 blackhole</code><br/> | 7.1 |
| `gateway=<interface_name>` | **CPU/HW** | <br/><code>/ip/route/add dst-address=10.0.0.0/24 gateway=ether1</code><br/><br/> 這僅適用於直接連線的網路。由於 HW 不知道如何傳送 ARP 要求，CPU 會在符合 DST IP 位址的連線第一個封包上傳送 ARP 要求並等待回覆，以找出 DST MAC 位址。決定 DST MAC 後，會新增 HW 項目，後續所有封包都會由交換器晶片處理。 | 7.1 |
| Bridge | **HW** | 從硬體卸載的 [bridge](/docs/bridging-and-switching#bridge-hardware-offloading) 介面進行路由，或路由至該介面。 | 7.1 |
| VLAN | **HW** | 在具有 <a href="/docs/bridging-and-switching#bridge-vlan-filtering">vlan-filtering</a> 的硬體卸載 bridge 介面上建立的 VLAN 介面之間進行路由。 <br/><br/><code>/interface/vlan</code><br/> | 7.1 |
| Bonding | **HW** | bonding 介面之間的路由。 <br/><br/><code>/interface/bonding</code><br/><br/> 只有 <code>802.3ad</code> 與 <code>balance-xor</code> bonding 模式會進行硬體卸載。 | 7.1 |
| IPv4 Firewall | **FW** | 使用者必須選擇 HW 加速路由或防火牆。防火牆規則會由 CPU 處理。***Fasttrack*** 連線會卸載到 HW。 | 7.1 |
| IPv4 NAT | **FW** | 套用到已卸載 ***Fasttrack*** 連線的 NAT 規則也會由 HW 處理。 | 7.1 |
| MLAG | **N/A** |  |  |
| VRF | **HW** | [硬體卸載的 VRF](#hardware-offloaded-vrf)。 |  |
| VRRP | **N/A** |  |  |
| Controller Bridge and Port Extender | **N/A** |  |  |
| Traffic-Flow | **N/A** | L3HW 卸載的流量不會透過 [Traffic Flow](/docs/diagnostics-monitoring-and-troubleshooting/traffic-flow) 回報。 |  |
| VXLAN | **HW** | 支援硬體卸載的 <a href="/docs/bridging-and-switching/vxlan">VXLAN</a> 資料平面、VXLAN 封裝與解封裝。這允許在 vlan-filtering bridge 內進行靜態的一對一 VLAN 對 VXLAN 對應。目前仍有部分已知功能尚未實作。<br/><strong>Underlay（路由已封裝的 VXLAN 封包）：</strong><br/> 1. 不支援透過 ECMP 的 VTEP <br/> 2. 不支援透過 bond、bridge、VLAN 介面的 VTEP（僅支援獨立路由的 Ethernet 介面） <br/> 3. 不支援透過 multicast 的 VTEP <br/> 4. VXLAN 硬體卸載僅限於 <code>main</code> 路由表。VTEP 無法在 VRF 內運作。 <br/> 5. 不支援搭配 IPv6 的 VTEP <br/><strong>Overlay（在 Ethernet 與 VXLAN 之間轉送）：</strong><br/> 1. 不支援透過 VXLAN 的 VLAN 標記 <br/> 2. 不支援不同 VXLAN VNI 之間的路由 <br/> 3. VTEP 彼此隔離，且沒有機制可控制它們之間的「horizon」。 <br/> 4. 已 bridge 的 VXLAN 介面不支援 IGMP snooping。啟用 snooping 時，VXLAN 上的 MDB 項目不會卸載，且 multicast 流量會在 Ethernet 與 VXLAN 之間受到限制。 <br/> 5. MLAG 不支援已 bridge 的 VXLAN 介面。 <br/><br/><code>/interface/vxlan</code><br/> | 7.18 |
| MTU | **HW** | 硬體支援最多 8 個 MTU 設定檔。 | 7.1 |
| QinQ Routing | **CPU** | 堆疊的可路由 VLAN 介面會失去 L3HW 卸載，而直接在 bridge 介面上建立的可路由 VLAN 介面仍可使用 HW 卸載。 |  |

:::warning
混合同一流量的硬體轉送封包與 FastTrack/CPU 轉送封包，可能會選取不同的 ECMP 下一跳，造成非對稱路由與連線重設。
:::

只有下表所列的設備支援 L3 HW Offloading。

## L3HW 設備支援 {#l3hw-device-support}

只有下表所列的設備支援 L3 HW Offloading。

### CRS3xx：Switch 98DX3xxx 與 98DX2xxx 系列 {#crs3xx-switch-98dx3xxx-and-98dx2xxx-series}

下列設備以 **Marvell **98DX224S、98DX226S****、**98DX2528,** 或 **98DX3236** 交換器晶片型號為基礎。

:::info
**98DX3255** 與 **98DX3257** 型號為例外，其功能集屬於 98DX8xxx，而非 98DX3xxx 系列。

**注意：** 與其他交換器型號相比，下列是這些設備缺少的一些重要功能：

- Fasttrack 與 NAT 連線卸載
- 每 VLAN 封包與位元組計數器
- VXLAN 卸載
- 硬體卸載 VRF。
:::

| 交換器晶片 | 型號 | IPv4 路由前綴 <sup>1</sup> | IPv6 路由前綴 <sup>2</sup> | 下一跳 | 每個前綴的 ECMP 路徑 <sup>3</sup> |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **98DX3236** | CRS305-1G-4S+IN <br/> CRS326-24G-2S+ (RM/IN) <br/> CRS328-24P-4S+RM <br/> CRS328-4C-20S-4S+RM | 13312 | 3328 | 4K | 8 |
| **98DX226S** | CRS305-1G-4S+OUT (FiberBox Plus) <br/> CRS310-1G-5S-4S+ (netFiber 9/IN) <br/> CRS310-8G+2S+IN <br/> CRS318-16P-2S+OUT (netPower 16P) <br/> CRS320-8P-8B-4S+RM <br/> CRS418-8P-8G-2S+RM <br/> CRS418-8P-8G-2S+5axQ2axQ-RM | 13312 | 3328 | 4K | 8 |
| **98DX224S** | CRS318-1Fi-15Fr-2S-OUT (netPower 15FR) | 13312 | 3328 | 4K | 8 |
| **98DX2528** | CRS304-4XG-IN | 13312 | 3328 | 4K | 8 |

---

<sup>1</sup> Since the total number of routes that can be offloaded is limited, prefixes with higher netmask are preferred to be forwarded by hardware (e.g., /32, /30, /29, etc.). Any other prefixes that do not fit in the HW table will be processed by the CPU. Directly connected hosts are offloaded as /32 (IPv4) or /128 (IPv6) route prefixes. The number of hosts is also limited by max-neighbor-entries in [IP Settings](/docs/cli-reference/ip/settings) / [IPv6 Settings](/docs/cli-reference/ipv6/settings).  
<sup>2</sup> IPv4 and IPv6 routing tables share the same hardware memory.  
<sup>3</sup> If a route has more paths than the hardware ECMP limit (X), only the first X paths get offloaded.

#### 部分卸載 {#partial-offloading}

對於 **98DX3xxx**、**98DX2xxx** 交換器晶片系列，情況相當簡單：一筆 RouterOS 路由項目 (/ip/route/) 會對應一筆 HW IPv4 路由前綴項目。已連線的主機 (/32 路由) 也會佔用同一個表。只要路由總數 ("/ip/route/print count-only") 加上已連線主機數 ("/ip/arp/print count-only where status=reachable or status=stale") 不超過 **13312 (13k)**，所有項目都會被卸載。超過這個數量時，具有*較短*前綴的路由會留在 CPU 上。

### CCR2xxx、CRS3xx、CRS5xx：Switch 98DX8xxx 與 98DX4xxx 系列 {#ccr2xxx-crs3xx-crs5xx-switch-98dx8xxx-and-98dx4xxx-series}

下列設備以 **Marvell 98DX8xxx**、**98DX4xxx** 交換器晶片，或 **98DX325x** 型號為基礎。

<WideTable>

| 交換器晶片 | 型號 | IPv4 路由 <sup>1</sup> | IPv4 主機 <sup>5</sup> | IPv6 路由 <sup>1</sup> | IPv6 主機 <sup>5</sup> | 下一跳 | IPv4 Fasttrack 連線 <sup>2, 3, 4</sup> | IPv4 NAT 項目 <sup>2, 4</sup> | IPv4 Fasttrack/NAT、VXLAN 卸載 每 VLAN 封包/位元組計數器 |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **98DX8208** | CRS309-1G-8S+IN | 最高 36K | 最高 16K | 最高 6K | 最高 12K | 8K | 4.5K | 3.9K | + |
| **98DX8212** | CRS312-4C+8XG-RM | 最高 36K | 最高 16K | 最高 6K | 最高 12K | 8K | 2.25K | 2.25K | + |
| **98DX8216** | CRS317-1G-16S+RM | 最高 240K | 最高 64K | 最高 40K | 最高 48K | 8K | 4.5K | 4K | + |
| **98DX8332** | CRS326-24S+2Q+RM <br/> CRS326-4C+20G+2Q+RM | 最高 36K | 最高 16K | 最高 6K | 最高 12K | 8K | 2.25K | 2.25K | + |
| **98DX3257** <sup>6</sup> | CRS354-48G-4S+2Q+RM <br/> CRS354-48P-4S+2Q+RM | 最高 36K | 最高 16K | 最高 6K | 最高 12K | 8K | 2.25K | 2.25K | + |
| **98DX4310** | CRS504-4XQ (IN/OUT) <br/> CRS510-8XS-2XQ-IN <br/> RDS2216-2XG-4S+4XS-2XQ | 最高 120K | 最高 64K | 最高 20K | 最高 48K | 8K | 4.5K | 4K | + |
| **98CX8410** | CRS520-4XS-16XQ-RM | 最高 240K | 最高 64K | 最高 40K | 最高 48K | 8K | 4.5K | 4K | + |
| **98DX3255** <sup>6</sup> | CCR2116-12G-4S+ | 最高 36K | 最高 16K | 最高 6K | 最高 12K | 8K | 2.25K | 2.25K | + |
| **98DX8525** | CCR2216-1G-12XS-2XQ <br/> CRS518-16XS-2XQ-RM | 最高 120K | 最高 64K | 最高 20K | 最高 48K | 8K | 4.5K | 4K | + |

</WideTable>

<sup>1</sup> Depends on the complexity of the routing table. Whole-byte IP prefixes (/8, /16, /24, etc.) occupy less HW space than others (e.g., /22). When the Routing HW table gets full, only routes with longer subnet prefixes are offloaded (/30, /29, /28, etc.) while the CPU processes the shorter prefixes. Users can fine-tune what routes to offload via routing filters (for dynamic routes) or suppressing hardware offload per switch port, static route or VLAN. IPv4 and IPv6 routing tables share the same hardware memory.  
<sup>2</sup> When the HW limit of Fasttrack or NAT entries is reached, other connections will fall back to the CPU. MikroTik's smart connection offload algorithm ensures that the connections with the most traffic are offloaded to the hardware.  
<sup>3</sup> Fasttrack connections share the same HW memory with ACL rules. Depending on the complexity, one ACL rule may occupy the memory of 3-6 Fasttrack connections.  
<sup>4</sup> If a Fasttrack connection requires Network Address Translation, a hardware NAT entry is created. The hardware supports both SRCNAT and DSTNAT.  
<sup>5</sup> DX4000/DX8000 switch chips store directly connected hosts, IPv4 /32, and IPv6 /128 route entries in the FDB table rather than the routing table. The HW memory is shared between regular FDB L2 entries (MAC), IPv4, and IPv6 addresses. The number of hosts is also limited by max-neighbor-entries in [IP Settings](/docs/cli-reference/ip/settings) / [IPv6 Settings](/docs/cli-reference/ipv6/settings).  
<sup>6</sup> The switch chip has a feature set of the DX8000 series.

#### 部分卸載 {#partial-offloading-1}

**98DX8xxx**、**98DX4xxx** 具有完全不同的路由表。我們不是卸載前綴，而是必須卸載路由索引。整個 IPv4 位址範圍（IPv6 也是如此）都必須建立索引，也就是 0.0.0.0 - 255.255.255.255。新增路由項目會造成索引重建，並依路由表的複雜度增加 0-5 個項目的硬體記憶體用量。這就是為什麼沒有提供確切數字。舉例來說，某些包含 240K 個項目的路由表可以完整卸載到 CRS317 HW，而另一些只有 160K 個項目的路由表卻幾乎放不下。而且在你實際嘗試之前，永遠不會知道結果。

當為整個 IP 位址範圍（0.0.0.0 - 255.255.255.255）建立索引時，只要也有一條使用相同 next-hop 的預設路由（0.0.0.0/0），就可以卸載任意數量的路由。

例如，在一台 CCR2216 路由器上建立了約 950k 條具有 /30 前綴的路由，全部使用相同的 next-hop，並搭配一條預設路由。結果，所有路由都已卸載，而 lpm-usage 仍維持在很低的水準。

```routeros
[admin@MikroTik] > /interface/ethernet/switch/l3hw-settings/advanced/monitor 
        ipv4-routes-total: 942338
           ipv4-routes-hw: 942326
          ipv4-routes-cpu:     11
  ipv4-shortest-hw-prefix:      0
               ipv4-hosts:      1
         route-queue-size:      0
         route-queue-rate:      0
       route-process-rate:      0
              nexthop-cap:   8192
            nexthop-usage:     85
    vxlan-mtu-packet-drop:      0
     fasttrack-ipv4-conns:      0
     fasttrack-queue-size:      0
     fasttrack-queue-rate:      0
   fasttrack-process-rate:      0
   fasttrack-hw-min-speed:      0
   fasttrack-hw-offloaded:      0
    fasttrack-hw-unloaded:      0
                  lpm-cap:  27200
                lpm-usage:     11
             lpm-bank-cap:   1360
           lpm-bank-usage:      1
                                0
                                0
                                0
                                1
                                0
                                0
                                0
                                4
                                0
                                0
                                0
                                5
                                0
                                0
                                0
                                0
                                0
                                0
                                0
                  pbr-cap:   8192
                pbr-usage:      0
             pbr-lpm-bank:      2
                nat-usage:      0
```

不過，如果位址範圍中有「間隙」，例如沒有使用預設路由，或有多個 next-hop，就會消耗 HW 表。當路由 HW 表滿了，只會卸載具有較長子網路前綴的路由（/30、/29、/28 等），而較短前綴則由 CPU 處理。以下是停用預設路由或使用不同 next-hop 時會發生的情況：HW 表中只能放下 37k 條具有 /30 前綴的路由。這是 CCR2216 最糟的情況。

```routeros
[admin@MikroTik] > /interface/ethernet/switch/l3hw-settings/advanced/monitor 
        ipv4-routes-total: 942337
           ipv4-routes-hw:  37729
          ipv4-routes-cpu: 904608
  ipv4-shortest-hw-prefix:     30
               ipv4-hosts:      1
         route-queue-size:      0
         route-queue-rate:      0
       route-process-rate:      0
              nexthop-cap:   8192
            nexthop-usage:     85
    vxlan-mtu-packet-drop:      0
     fasttrack-ipv4-conns:      0
     fasttrack-queue-size:      0
     fasttrack-queue-rate:      0
   fasttrack-process-rate:      0
   fasttrack-hw-min-speed:      0
   fasttrack-hw-offloaded:      0
    fasttrack-hw-unloaded:      0
                  lpm-cap:  27200
                lpm-usage:  22392
             lpm-bank-cap:   1360
           lpm-bank-usage:   1022
                             1033
                             1027
                             1028
                             1221
                             1033
                             1040
                              678
                             1358
                             1245
                             1254
                             1242
                             1246
                             1249
                             1273
                             1260
                             1101
                             1024
                             1031
                             1027
                  pbr-cap:   8192
                pbr-usage:      0
             pbr-lpm-bank:      2
                nat-usage:      0
```

在許多情況下，預設行為「只卸載具有較長子網路前綴的路由」並不是最佳做法，尤其是當 CPU 處理的路由與 HW 卸載的路由比例過高時。發生這種情況時，封包由硬體轉發的機率會大幅下降。

如果 HW 記憶體不足而發生部分卸載，對你身為網路管理員來說，較好的做法是只卸載承載最多流量的路由，並將需求較低的路由留在 CPU 上，而不是讓部分卸載自行發生。

幸運的是，有幾種方式可以管理這件事。可以使用 per-switch-port 與 static route suppression，以及[使用多種屬性篩選動態路由](/docs/user-guides/routing-and-networking-protocols/route-selection-and-filtering)。其中一個範例是使用 as-path 篩選需求最高的前綴（Google、Meta），而其餘路由則設定 L3HW suppressed。

### CRS8xx：98DX7xxx 系列交換器 {#crs8xx-switch-98dx7xxx-series}

下列設備基於 **Marvell 98DX7xxx** 交換器晶片型號。

:::danger
下列功能的軟體支援仍在開發中，目前尚不可用：

- FastTrack 與 NAT 連線卸載
- VXLAN 卸載
:::

<WideTable>

| 交換器晶片 | 型號 | IPv4 Routes <sup>1</sup> | IPv4 Hosts <sup>2</sup> | IPv6 Routes <sup>1</sup> | IPv6 Hosts <sup>2</sup> | Nexthops | IPv4 Fasttrack connections | IPv4 NAT entries | VXLAN offloading | Per-VLAN packet/byte counters |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **98DX7335** | CRS812-8DS-2DQ-2DDQ-RM | 最高 240K | 最高 64K | 最高 40K | 最高 48K | 16K | 待公布 | 待公布 | 待公布 | + |
| **98DX7335** | CRS804-4DDQ-hRM | 最高 240K | 最高 64K | 最高 40K | 最高 48K | 16K | 待公布 | 待公布 | 待公布 | + |

</WideTable>

---

<sup>1</sup> Depends on the complexity of the routing table. Whole-byte IP prefixes (/8, /16, /24, etc.) occupy less HW space than others (e.g., /22). When the Routing HW table gets full, only routes with longer subnet prefixes are offloaded (/30, /29, /28, etc.) while the CPU processes the shorter prefixes. Users can fine-tune what routes to offload via routing filters (for dynamic routes) or suppressing hardware offload of static routes. IPv4 and IPv6 routing tables share the same hardware memory.  
<sup>2</sup> 98DX7xxx switch chips store directly connected hosts, IPv4 /32 route entries, and IPv6 /128 route entries in the FDB table rather than the routing table. The HW memory is shared between regular FDB L2 entries (MAC), IPv4 addresses, and IPv6 addresses. The number of hosts is also limited by max-neighbor-entries in [IP Settings](/docs/cli-reference/ip/settings) / [IPv6 Settings](/docs/cli-reference/ipv6/settings).
