---
title: "服務品質"
description: "本文件介紹 MikroTik RouterOS 中適用於搭載 Marvell Prestera 交換器晶片設備的 Quality of Service (QoS) 功能，說明 QoS 優先順序、流量整形與壅塞管理。內容涵蓋 RouterOS v7.23 的增強功能，例如無損流量支援、動態緩衝區，以及適用於各種交換器型號的 QoS 裝置相容性表。"
tags:
  - 'qos'
  - 'marvell-prestera'
  - 'active-queue-management'
source: https://manual.mikrotik.com/docs/7.24/bridging-and-switching/quality-of-service
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

本文件說明在配備 **[Marvell Prestera 交換器晶片](/docs/bridging-and-switching/marvell-prestera-switch-chip-features)** 的設備上，RouterOS 中 **服務品質（Quality of Service，QoS）** 的實作方式。

QoS 是網路交換器中的一組功能，可讓網路管理員排定流量優先順序並配置網路資源，以確保關鍵資料能順暢傳輸並維持低延遲。

網路交換器中 QoS 的主要功能，是以符合不同類型網路應用程式特定需求的方式管理流量。例如，語音與影片資料需要低延遲與極低的封包遺失率，以確保高品質通訊；而檔案傳輸與其他資料應用程式則可容忍較高的延遲與封包遺失率。

QoS 的運作方式是識別流經交換器的流量類型，並依其需求指派優先順序。交換器接著使用此資訊修改封包標頭並排定流量優先順序，確保較高優先順序的流量能獲得比較低優先順序流量更優先的處理。

需要 RouterOS v7.15 或更新版本才能支援所有 QoS 功能：

1. **QoS 標記。** 依傳入封包標頭比對 QoS 設定檔，再依指派的 QoS 設定檔修改傳出標頭。
2. **QoS 強制執行。** 依指派的 QoS 設定檔與流量整形避免或解決壅塞。
3. **QoS 原則。** 透過 ACL 規則指派 QoS 設定檔。
4. 主動佇列管理：**WRED**（加權隨機早期偵測）、**ECN** 通知與處理、**PFC**（優先順序流量控制）。
5. 流量整形。

### RouterOS v7.23 中的 QoS 變更 {#qos-changes-in-routeros-v723}

RouterOS v7.23 對服務品質（Quality of Service，QoS）卸載功能引進重大變更。這些變更簡化了設定流程，並新增對「無遺失」流量類別的支援。雖然硬體資源有限，但當所有連線設備都支援並正確設定這些功能時，使用 ECN 及／或 PFC 的主動佇列管理可避免封包遺失。先前的 RouterOS 版本已支援 ECN 與 PFC，但 v7.23 簡化了設定方式。

:::info
並非所有設備都支援無損流量。請檢查 QoS Device Support 表格。
:::

#### 設定變更摘要 {#configuration-change-summary}

- QoS Settings：多數變更預設設為「auto」，讓 RouterOS 為設定挑選已知的最佳設定。
- QoS Settings：新增 `lossless-traffic-class` 與 `lossless-buffers`，可明確指定無損流量並為其保留佇列資源。使用者也可以將這些欄位保持為「auto」。
- QoS Monitor：分別顯示有損與無損流量的共用集區使用情況。
- Tx Queue：移除共用集區索引。RouterOS 會根據流量類型（有損或無損）自動選取共用集區。
- QoS Profile：新增自動對應至指定的 PCP 與 DSCP 值（預設啟用）。例如，新增 DSCP=46 的 QoS profile 時，會自動將該 profile 套用至從信任埠接收的流量。

## QoS 術語 {#qos-terminology}

本節定義本文件中使用的關鍵術語與縮寫：

- **QoS** - Quality of Service，一組讓網路管理員排序流量優先順序並分配網路資源的功能。
- **ACL** - Access Control List，一組交換器規則，用於依指定條件篩選網路流量。
- **AQM** - Active Queue Management，一種壅塞控制機制，透過在佇列溢位前丟棄或標記封包來管理流量。
- **DSCP** - Differentiated Services Code Point，IP 標頭中的 6 位元欄位，用於排序網路流量優先順序。
- **ECN** - Explicit Congestion Notification，一種機制，可讓路由器在不丟棄封包的情況下，向端點設備通知壅塞。
- **ETS** - Enhanced Transmission Selection，一種流量排程方法，使用加權循環配置在多個佇列群組之間分配頻寬。
- **PCP** - Priority Code Point，VLAN 標頭中的 3 位元欄位，用於排序 VLAN 內的流量優先順序。
- **PFC** - Priority-based Flow Control（IEEE 802.1Qbb），一種流量控制機制，會暫停特定優先順序佇列上的流量，以避免封包遺失。
- **RoCE** - RDMA over Converged Ethernet，一種通訊協定，可透過乙太網路實現遠端直接記憶體存取。
- **WRED** - Weighted Random Early Detection，一種壅塞避免機制，會在佇列接近容量時隨機丟棄封包。
- **/in/eth/sw/** - `/interface/ethernet/switch/` 的 CLI 捷徑。

## 新一代 Marvell Prestera 交換器晶片的 QoS 增強 {#qos-enhancements-in-new-generation-marvell-prestera-switch-chips}

搭載新一代 Marvell Prestera 交換器晶片的 MikroTik 設備（例如執行 [switch-marvell package](/docs/getting-started/installation-and-upgrade/packages#extra-packages) 的 CRS8xx 系列）提供新的 QoS 強制執行方式。先前的型號需要在保證緩衝區與共用 Tx 佇列緩衝區之間取捨。提高共用緩衝區比例可讓設備吸收較大的流量突發，但同時，單一壅塞埠可能佔用所有共用緩衝區，限制其他埠的 QoS 能力。使用新一代交換器晶片可透過 **Dynamic Buffers** 同時兼顧兩者。交換器晶片會根據目前的壅塞程度動態調整埠與佇列緩衝區限制。若設備內沒有壅塞，單一埠可吸收大量流量突發，避免封包遺失。當多個埠的 Tx 佇列大小增加時，設備會降低每埠與每佇列限制，在確保未壅塞佇列有足夠緩衝區可繼續轉送流量的同時，強制公平使用共用資源。整個程序全自動化，使用者無需任何設定。

新一代 Marvell Prestera 交換器晶片的另一項改良，是消除了用於儲存控制資料的已入佇列封包描述元不足問題。前一代設備具有 Packet Cap 與 Use 統計。當設備收到大量小型封包的突發流量時，即使有足夠的佇列緩衝區可儲存酬載，仍可能因達到 Packet Cap 而開始尾部丟棄封包。新一代設備可確保始終有足夠的記憶體儲存控制資料，讓 Dynamic Buffer 大小成為唯一的限制因素。這就是新一代設備中沒有 Packet Cap/Use 統計的原因。

新一代設備要求一律啟用 QoS HW Offloading（**qos-hw-offloading=yes**）。RouterOS 會忽略使用者停用它的要求，但為了向後相容仍保留該欄位。

## QoS 設備支援 {#qos-device-support}

<WideTable>

| 交換器晶片 | 型號 | QoS 設定檔 | QoS 對應 | Tx Managers | WRED | ECN | PFC | Lossless Buffers | Dynamic Buffers | 埠／佇列使用量統計 |
| :-- | :-- | --: | --: | --: | :-- | :-- | :-- | :-- | :-- | :-- |
| **98DX3236** | CRS305-1G-4S+IN <br/> CRS326-24G-2S+ (RM/IN) <br/> CRS328-24P-4S+RM <br/> CRS328-4C-20S-4S+RM | 128 | 1 | 8 |  |  |  |  |  | 目前值 |
| **98DX226S** | CRS305-1G-4S+OUT (FiberBox Plus) <br/> CRS310-1G-5S-4S+ (netFiber 9/IN) <br/> CRS310-8G+2S+IN <br/> CRS318-16P-2S+OUT (netPower 16P) <br/> CRS320-8P-8B-4S+RM <br/> CRS418-8P-8G-2S+RM <br/> CRS418-8P-8G-2S+5axQ2axQ-RM | 128 | 1 | 8 |  |  |  |  |  | 目前值 |
| **98DX224S** | CRS318-1Fi-15Fr-2S-OUT (netPower 15FR) | 128 | 1 | 8 |  |  |  |  |  | 目前值 |
| **98DX2528** | CRS304-4XG-IN | 128 | 1 | 8 |  |  |  |  |  | 目前值 |
| **98DX8525** | CCR2216-1G-12XS-2XQ <br/> CRS518-16XS-2XQ-RM | 1024 | 12 | 15 | ✔ | ✔ | ✔ | ✔ |  | 最大填入量 <sup>1</sup> |
| **98DX4310** | CRS504-4XQ (IN/OUT) <br/> CRS510-8XS-2XQ-IN <br/> RDS2216-2XG-4S+4XS-2XQ | 1024 | 12 | 15 | ✔ | ✔ | ✔ | ✔ |  | 最大填入量 <sup>1</sup> |
| **98DX8208** | CRS309-1G-8S+IN | 1024 | 12 | 15 | ✔ | ✔ | ✔ | ✔ |  | 目前值 <sup>2</sup> |
| **98DX8212** | CRS312-4C+8XG-RM | 1024 | 12 | 15 | ✔ | ✔ | ✔ | ✔ |  | 目前值 <sup>2</sup> |
| **98DX8216** | CRS317-1G-16S+RM | 1024 | 12 | 15 | ✔ | ✔ | ✔ | ✔ |  | 目前值 <sup>2</sup> |
| **98DX8332** | CRS326-24S+2Q+RM <br/> CRS326-4C+20G+2Q+RM | 1024 | 12 | 15 | ✔ | ✔ | ✔ | ✔ |  | 目前值 <sup>2</sup> |
| **98DX3257** | CRS354-48G-4S+2Q+RM <br/> CRS354-48P-4S+2Q+RM | 1024 | 12 | 15 | ✔ | ✔ | ✔ | ✔ |  | 目前值 <sup>2</sup> |
| **98DX3255** | CCR2116-12G-4S+ | 1024 | 12 | 15 | ✔ | ✔ | ✔ | ✔ |  | 目前值 <sup>2</sup> |
| **98CX8410** | CRS520-4XS-16XQ-RM | 1024 | 12 | 15 | ✔ | ✔ | ✔ | ✔ |  | 無法使用 <sup>3</sup> |
| **98DX7335** | CRS812-8DS-2DQ-2DDQ-RM <br/> CRS804-4DDQ-hRM | 1024 | 12 | 15 | ✔ | ✔ | ✔ | ✔ | ✔ | 目前值 + 最大填入量 |

</WideTable>

<sup>**1**</sup> The device gathers max queue fill statistics instead of displaying the current usage values. Use the `reset-counters` command to clear those stats.  
<sup>**2**</sup> Due to hardware limitations, some switch chip models may experience temporary traffic flow disruption while reading or polling QoS port/queue usage data.  
<sup>**3**</sup> Usage data for individual queues on a port is unavailable; only the aggregate total usage for the entire physical port can be accessed.

## 應用與使用範例 {#applications-and-usage-examples}

---

### 基本設定範例 {#basic-configuration-example}

此範例示範如何在標準 Best Effort 類別之上，為 VoIP（IP Telephony）設定單一 QoS 層級。此設定使用 CRS326-24G-2S+ 設備，並採用下列配置：

- 所有埠都已橋接並使用 **[vlan-filtering](/docs/bridging-and-switching/quality-of-service#bridge-vlan-filtering)**；
- sfp-sfpplus1 作為連接到另一台交換器的 VLAN trunk；
- ether1 至 ether9 是 IP 話機的專用埠；
- ether10 至 ether24 是用於連接主機的標準埠。

首先，定義 QoS profile。此 profile 指定將套用至 egress 轉送封包的 DSCP 與 PCP 值：

```ros
/interface/ethernet/switch/qos/profile
add dscp=46 name=voip pcp=5 traffic-class=5
```

接著，將 VoIP QoS profile 指派給 IP 電話專用的埠。這會將 profile 套用至這些埠上的 ingress 流量。其他所有 Ethernet 埠都會使用預設 profile（其中 dscp=0 且 pcp=0）：

```ros
/interface/ethernet/switch/qos/port
set ether1 profile=voip
set ether2 profile=voip
set ether3 profile=voip
set ether4 profile=voip
set ether5 profile=voip
set ether6 profile=voip
set ether7 profile=voip
set ether8 profile=voip
set ether9 profile=voip
```

trunk 埠會接收兩種類型的 QoS 流量。為了區分它們，請啟用 trust-l3 與 trust-l2：

```ros
/interface/ethernet/switch/qos/port
set sfp-sfpplus1 trust-l3=trust trust-l2=trust
```

> **Note:** 如果你執行的是 RouterOS 7.23 或更新版本，VLAN priority 與 IP DSCP 對應會自動建立，因此不需要此步驟。如果你使用較早的 RouterOS 版本，必須使用 QoS profile 手動建立 VLAN priority 與 IP DSCP 對應：

```routeros
/interface/ethernet/switch/qos/map/ip
add dscp=46 profile=voip

/interface/ethernet/switch/qos/map/vlan
add pcp=5 profile=voip
```

最後，啟用 QoS 硬體卸載，讓上述設定生效：

```ros
/interface/ethernet/switch
set switch1 qos-hw-offloading=yes
```

你可以使用 `print` 指令驗證埠的 QoS 設定：

```ros
[admin@MikroTik] /interface/ethernet/switch/qos/port/print
Column: NAME, SWITCH, PROFILE, MAP, TRUST-L2, TRUST-L3
 # NAME          SWITCH   PROFILE  MAP      TRUST-L2  TRUST-L3  TX-MANAGER
 0 ether1        switch1  voip     default  ignore    ignore    default
 1 ether2        switch1  voip     default  ignore    ignore    default
 2 ether3        switch1  voip     default  ignore    ignore    default
 3 ether4        switch1  voip     default  ignore    ignore    default
 4 ether5        switch1  voip     default  ignore    ignore    default
 5 ether6        switch1  voip     default  ignore    ignore    default
 6 ether7        switch1  voip     default  ignore    ignore    default
 7 ether8        switch1  voip     default  ignore    ignore    default
 8 ether9        switch1  voip     default  ignore    ignore    default
 9 ether10       switch1  default  default  ignore    ignore    default
10 ether11       switch1  default  default  ignore    ignore    default
11 ether12       switch1  default  default  ignore    ignore    default
12 ether13       switch1  default  default  ignore    ignore    default
13 ether14       switch1  default  default  ignore    ignore    default
14 ether15       switch1  default  default  ignore    ignore    default
15 ether16       switch1  default  default  ignore    ignore    default
16 ether17       switch1  default  default  ignore    ignore    default
17 ether18       switch1  default  default  ignore    ignore    default
18 ether19       switch1  default  default  ignore    ignore    default
19 ether20       switch1  default  default  ignore    ignore    default
20 ether21       switch1  default  default  ignore    ignore    default
21 ether22       switch1  default  default  ignore    ignore    default
22 ether23       switch1  default  default  ignore    ignore    default
23 ether24       switch1  default  default  ignore    ignore    default
24 sfp-sfpplus1  switch1  default  default  trust     ignore    default
25 sfp-sfpplus2  switch1  default  default  ignore    ignore    default
26 switch1-cpu   switch1   
```

透過此設定，port ether1 至 ether9 上的傳入封包會標記為 Priority Code Point（PCP）值 5 與 Differentiated Services Code Point（DSCP）值 46。port ether10 至 ether24 上的傳入封包會標記為 PCP 與 DSCP 值 0。當封包在 sfp-sfpplus1 埠上接收時，任何 PCP 值為 5 的封包都會保留其 PCP 值 5 與 DSCP 值 46，而其他所有封包都會標記為 PCP 與 DSCP 值 0。

## Dante

從 RouterOS v7.15 開始，所有支援 QoS 的 MikroTik 設備都與 Dante audio networking 相容。

Dante 硬體使用下列 DSCP/Diffserv 優先順序值進行流量優先排序：

| Dante Priority | 用途 | DSCP Label | DSCP Value |
| :-- | :-- | :-- | --: |
| High | 時間關鍵的 PTP 事件 | CS7 | 56 |
| Medium | 音訊、PTP | EF | 46 |
| None | 其他流量 | BE | 0 |

此範例假設交換器使用預設設定，其中包含一個預設 bridge 介面，且所有 Ethernet 介面都已新增為 bridge 埠。任何這些介面都可用於 Dante。

首先，建立 QoS profile 以比對 Dante 流量類別。已存在一個預先建立的「default」profile，對應 Dante 的 None 優先順序。

```ros
/interface/ethernet/switch/qos/profile
add name=dante-ptp dscp=56 pcp=7 traffic-class=7
add name=dante-audio dscp=46 pcp=5 traffic-class=5
```

如果你執行的是 RouterOS 7.23 或更新版本，IP DSCP 對應會自動建立，因此不需要此步驟。如果你使用較早的 RouterOS 版本，請建立 QoS 對應，以根據 DSCP 值比對 QoS profile：

```ros
/interface/ethernet/switch/qos/map/ip
add dscp=56 profile=dante-ptp
add dscp=46 profile=dante-audio
```

設定硬體佇列，以對 Dante 流量強制執行 QoS：

```ros
/interface/ethernet/switch/qos/tx-manager/queue
set [find where traffic-class=7] schedule=strict-priority
set [find where traffic-class=5] schedule=strict-priority
```

Dante 的 High 與 Medium 優先順序流量會以嚴格優先順序進行排程。設備會傳送時間關鍵的 PTP 封包，直到 queue7 清空，然後繼續處理音訊（queue5）。其他流量只有在 PTP 與音訊佇列都清空時才會傳送。

下一步是為傳入的 Layer 3 封包啟用 trust mode（IP DSCP 欄位）：

```ros
/interface/ethernet/switch/qos/port
set [find] trust-l3=keep
```

最後，啟用 QoS 硬體卸載，讓上述設定生效：

```ros
/interface/ethernet/switch
set switch1 qos-hw-offloading=yes
```

在 multicast 模式下使用 Dante 時，建議在交換器上啟用 IGMP snooping。此功能只會將流量導向具有訂閱設備的埠，避免不必要的泛洪。此外，啟用 IGMP querier（若同一 LAN 中的其他設備尚未啟用）、調整查詢間隔，以及啟用 fast-leave，可進一步最佳化 multicast 效能。

```ros
/interface/bridge
set [find name=bridge] igmp-snooping=yes multicast-querier=yes query-interval=60s

/interface/bridge/port
set [find] fast-leave=yes
```

## 融合式乙太網路上的 RDMA（RoCE） {#rdma-over-converged-ethernet-roce}

RoCE 可透過乙太網路直接存取遠端儲存系統的記憶體，而無需主機 CPU 參與。這可大幅降低延遲與 CPU 負擔，使 RoCE 非常適合高效能運算與資料中心環境。RoCE 也可建立匯聚網路，讓各種服務（例如資料儲存、網路與多媒體）在單一乙太網路基礎架構上執行，簡化網路管理，並降低維護獨立網路的成本與複雜度。

RoCE 透過使用 **ECN** 與 **PFC** 機制來達成這點。這些功能有助於避免網路壅塞與封包遺失，確保可靠、不遺失資料的通訊。請參閱[設備功能表](/docs/bridging-and-switching/quality-of-service#qos-device-support)以取得相容的交換器。雖然交換器可支援 RoCE 環境，但終端主機也必須相容於 RoCE 通訊協定，並配備支援 RDMA 的網路介面卡（NIC）。

RoCE 主要有兩個版本。RoCEv1 作為乙太網路鏈路層通訊協定運作，並使用 Ethertype 0x8915。RoCEv2 可在標準 IP 網路上運作，使用 UDP 目的埠號 4791。IP 標頭中的 ECN 位元會被標記，以通知網路壅塞，並使用 Congestion Notification Packet（CNP）向傳送端確認壅塞。為了進行流量優先順序處理，RoCEv2 流量使用 DSCP 26，而 CNP 使用 DSCP 48。

以下範例可用於搭配 PFC 與 ECN 的不遺失資料 RoCEv2，並假設交換器使用預設設定，其中包含預設 bridge 介面，且所有乙太網路介面都已新增為 bridge 埠。建議的最低 RouterOS 版本為 7.17。

首先，設定其他設定檔。非 RoCE 流量會指派給現有的 "default" 設定檔，traffic-class 為 1；RoCEv2 指派給 traffic-class 3；CNP 指派給 traffic-class 6。

```routeros
/interface/ethernet/switch/qos/profile
add dscp=26 name=roce traffic-class=3
add dscp=48 name=cnp traffic-class=6
```

如果您執行的是 RouterOS 7.23 或更新版本，IP DSCP 對應會自動建立，因此不需要執行此步驟。如果您使用較早的 RouterOS 版本，請建立 QoS 對應，以根據 DSCP 值比對 QoS 設定檔。

```routeros
/interface/ethernet/switch/qos/map/ip
add dscp=26 profile=roce
add dscp=48 profile=cnp
```

設定硬體佇列與排程器。針對 traffic-class 1 與 traffic-class 3 使用 ETS（`schedule=high-priority-group`），各自分配 50% 頻寬（`weight=1`），並針對 traffic-class 6 使用嚴格優先權排程。此外，請為 traffic-class 3 啟用 ECN（`ecn=yes`），以在交換器中標記遭遇壅塞的 IP 封包。

```routeros
/interface/ethernet/switch/qos/tx-manager/queue
set 1 schedule=high-priority-group weight=1
set 3 schedule=high-priority-group weight=1 ecn=yes
set 6 schedule=strict-priority
```

:::tip
雖然使用 `schedule=low-priority-group` 可讓您為另一組 traffic-classes 建立獨立的 ETS 排程與頻寬配置，但不建議將此設定與 `lldp-dcbx=yes` 一起使用。原因是 ETS Configuration/Recommendation TLV 的設計是用於處理跨流量類別的單一頻寬配置，因此應改用 `schedule=high-priority-group`。
:::

請為 traffic-class 3 設定 PFC 設定檔，以確保 RoCEv2 流量具備不丟失封包的環境。

```routeros
/interface/ethernet/switch/qos/priority-flow-control
add name=pfc-tc3 rx=yes traffic-class=3 tx=yes
```

在預期會有 RoCEv2 流量的交換器埠上設定 Layer3 信任模式（`trust-l3=keep`）。設定 PFC（`pfc=pfc-tc3`）與 queue3 的出口速率，以符合 PFC 需求（`egress-rate-queue3=10.0Gbps`）。在此範例中，使用的是 10Gbps SFP+ 介面，出口速率可設定為與介面的實體速度相符。請依您的介面速度變更此屬性。

```routeros
/interface/ethernet/switch/qos/port
set sfp-sfpplus1 egress-rate-queue3=10.0Gbps pfc=pfc-tc3 trust-l3=keep
set sfp-sfpplus2 egress-rate-queue3=10.0Gbps pfc=pfc-tc3 trust-l3=keep
set sfp-sfpplus3 egress-rate-queue3=10.0Gbps pfc=pfc-tc3 trust-l3=keep
set sfp-sfpplus4 egress-rate-queue3=10.0Gbps pfc=pfc-tc3 trust-l3=keep
```

啟用 QoS 硬體卸載，讓上述設定開始生效。

```routeros
/interface/ethernet/switch
set switch1 qos-hw-offloading=yes
```

啟用 LLDP Data Center Bridging Capability Exchange Protocol（DCBX），與其他相鄰設備分享 QoS 設定與能力。

```routeros
/ip/neighbor/discovery-settings
set lldp-dcbx=yes
```

作為選擇性步驟，可提高 L2MTU 以容納較大的資料封包。

```routeros
/interface/ethernet
set [find switch=switch1] l2mtu=9500
```

## QoS 標記 {#qos-marking}

---

### 瞭解對應範圍 {#understanding-map-ranges}

為了避免逐一定義所有可能的 PCP 與 DSCP 對應，RouterOS 可讓你在建立 QoS profile 對應時，指定多個值或範圍。

在此範例中，PCP 值 0 與 2 使用預設 QoS profile，值 1 與 3-4 使用 streaming profile，值 5 使用 voip profile，值 6-7 使用 control profile：

```ros
/interface/ethernet/switch/qos/map/vlan
add pcp=1,3-4 profile=streaming
add pcp=5 profile=voip
add pcp=6-7 profile=control
```

這種做法會將相關的優先順序值分組，而不是為每個個別值建立不同的對應規則，可簡化設定。

### 瞭解埠、Profile 與對應的關係 {#understanding-port-profile-and-map-relation}

每個交換器埠都有 Layer2 與 Layer3 trust 設定，會改變 ingress 封包分類至 QoS profile 的方式，以及將使用哪些 PCP 與 DSCP 值。以下表格說明所有可能的選項：

| **qos-trust-l2** | **qos-trust-l3** | 行為 |
| :-- | :-- | :-- |
| **ignore** | **ignore** | 此埠被視為不受信任。系統會忽略兩個標頭，並對所有 ingress 封包強制使用該埠的 **profile**。這是預設設定。 |
| **ignore** | **trust** | 信任 Layer 3 標頭。使用 ingress 封包 IP 標頭中的 DSCP 欄位進行 QoS profile 查閱（請參閱 `/in/eth/sw/qos/map/ip`）。若查閱失敗（沒有任何 QoS profile 對應至指定的 DSCP 值），則使用 **default** QoS profile（不是交換器埠的 QoS profile）。交換器埠的 **profile** 欄位僅用於非 IP 流量。 |
| **ignore** | **keep** | 信任 Layer 3 標頭。使用 ingress 封包 IP 標頭中的 DSCP 欄位進行 QoS profile 查閱（請參閱 `/in/eth/sw/qos/map/ip`）。若查閱失敗，則使用 **default** QoS profile。交換器埠的 **profile** 欄位僅用於非 IP 流量。若轉送／路由的封包具有 VLAN 標記，其 PCP 值會從所選 QoS profile 設定。不過，封包原始的 DSCP 值會保持不變。 |
| **trust** | **ignore** | 信任 Layer 2 標頭，但忽略 L3。若 ingress 封包具有 VLAN 標記，請使用 VLAN 標頭中的 PCP 欄位進行 QoS profile 查閱（請參閱 `/in/eth/sw/qos/map/vlan`）。若查閱失敗（沒有任何 QoS profile 對應至指定的 PCP 值），則使用 **default** QoS profile。交換器埠的 **profile** 欄位僅用於未標記的流量。 |
| **trust** | **trust** | 信任兩個標頭，但 Layer 3 具有較高優先順序。若為 IP 封包，請使用 DSCP 欄位進行 QoS profile 查閱（請參閱 `/in/eth/sw/qos/map/ip`）。若 DSCP 對 QoS 的查閱失敗，請使用 **default** profile。若封包不是 IP 封包但具有 VLAN 標記，請使用 VLAN 標頭中的 PCP 欄位進行 QoS profile 查閱（請參閱 `/in/eth/sw/qos/map/vlan`）。若 VLAN 對 QoS 的查閱失敗，請使用 **default** QoS profile。非 IP 未標記封包會使用交換器埠的 **profile**。 |
| **trust** | **keep** | 與 **trust+trust** 相同，但在轉送／路由的封包中保留原始 DSCP 值。 |
| **keep** | **ignore** | 信任 Layer 2 標頭，但忽略 L3。若 ingress 封包具有 VLAN 標記，請使用 VLAN 標頭中的 PCP 欄位進行 QoS profile 查閱（請參閱 `/in/eth/sw/qos/map/vlan`）。若查閱失敗（沒有任何 QoS profile 對應至指定的 PCP 值），則使用 **default** QoS profile。交換器埠的 **profile** 欄位僅用於未標記的流量。若封包在 ingress 與 egress 都具有 VLAN 標記，則保留原始 PCP 值。 |
| **keep** | **trust** | 信任兩個標頭，但 Layer 3 具有較高優先順序。若為 IP 封包，請使用 DSCP 欄位進行 QoS profile 查閱（請參閱 `/in/eth/sw/qos/map/ip`）。若 DSCP 對 QoS 的查閱失敗，請使用 **default** profile。若封包不是 IP 封包但具有 VLAN 標記，請使用 VLAN 標頭中的 PCP 欄位進行 QoS profile 查閱（請參閱 `/in/eth/sw/qos/map/vlan`）。若 VLAN 對 QoS 的查閱失敗，請使用 **default** QoS profile。非 IP 未標記封包會使用交換器埠的 **profile**。若封包在 ingress 與 egress 都具有 VLAN 標記，則保留原始 PCP 值。轉送／路由封包中的 DSCP 值會從所選 QoS profile 設定。 |
| **keep** | **keep** | 信任兩個標頭，但 Layer 3 具有較高優先順序。若為 IP 封包，請使用 DSCP 欄位進行 QoS profile 查閱（請參閱 `/in/eth/sw/qos/map/ip`）。若 DSCP 對 QoS 的查閱失敗，請使用 **default** profile。若封包不是 IP 封包但具有 VLAN 標記，請使用 VLAN 標頭中的 PCP 欄位進行 QoS profile 查閱（請參閱 `/in/eth/sw/qos/map/vlan`）。若 VLAN 對 QoS 的查閱失敗，請使用 **default** QoS profile。非 IP 未標記封包會使用交換器埠的 **profile**。在具有 VLAN 標記及／或 IP 封包的情況下，分別保持原始 PCP 及／或 DSCP 值不變。 |

<WideTable>

| **埠設定** |  | 轉送／路由封包中所選取的 QoS 設定檔，以及 PCP / DSCP 欄位值的來源 |  |  |  |  |  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| **qos-trust-l2** | **qos-trust-l3** | VLAN-Tagged IP |  |  | Untagged IP |  |  | VLAN-Tagged Non-IP |  |  | Untagged Non-IP |  |  |
|  |  | QoS Profile | PCP | DSCP | QoS Profile | PCP <sup>1</sup> | DSCP | QoS Profile | PCP | DSCP | QoS Profile | PCP <sup>1</sup> | DSCP |
| ignore | ignore | profile | profile | profile | profile | profile | profile | profile | profile | - | profile | profile | - |
| ignore | trust | map/ip | map/ip | map/ip | map/ip | map/ip | map/ip | profile | profile | - | profile | profile | - |
| ignore | keep | `/map/ip` | `/map/ip` | original | `/map/ip` | `/map/ip` | original | profile | profile | - | profile | profile | - |
| trust | ignore | map/vlan | map/vlan | map/vlan | profile | profile | profile | map/vlan | map/vlan | - | profile | profile | - |
| trust | trust | `/map/ip` | `/map/ip` | `/map/ip` | `/map/ip` | `/map/ip` | `/map/ip` | `/map/vlan` | `/map/vlan` | - | profile | profile | - |
| trust | keep | `/map/ip` | `/map/ip` | original | `/map/ip` | `/map/ip` | original | `/map/vlan` | `/map/vlan` | - | profile | profile | - |
| keep | ignore | map/vlan | original | map/vlan | profile | profile | profile | map/vlan | original | - | profile | profile | - |
| keep | trust | map/ip | original | map/ip | map/ip | profile | map/ip | map/vlan | original | - | profile | profile | - |
| keep | keep | map/ip | original | original | map/ip | profile | original | map/vlan | original | - | profile | profile | - |

</WideTable>

<sup>**1**</sup> Applies only when ingress traffic is untagged, but the egress interface requires the frames to be VLAN-tagged.

### 透過交換器規則（ACL）進行 QoS 標記 {#qos-marking-via-switch-rules-acl}

從 **RouterOS v7.15** 開始，你可以使用交換器規則（ACL）為網路流量指派 QoS 設定檔。此方法可根據各種封包屬性進行彈性的流量分類。

**子選單：** `/interface/ethernet/switch/rule`

| 新增／變更的屬性 | 說明 |
| :-- | :-- |
| **new-qos-profile** (*name*) | 要指派給符合封包的 [QoS 設定檔](#qos-profile)名稱。 |
| **keep-qos-fields** (*yes \| no*；預設：**no**) | 是否保留 QoS 欄位（PCP、DSCP）的原始值（*yes*），或將其取代為所指派 QoS 設定檔中的值（*no*）？僅在設定 **new-qos-profile** 時相關。 |
| **new-vlan-priority** (*0..7*) | 已淘汰，應改用對應的 **new-qos-profile**。保留是為了向後相容。僅在 qos-hw-offloading=no 時相關。 |

下列範例會根據來源 MAC 位址指派 QoS 設定檔：

```ros
/interface/ethernet/switch/rule
add new-qos-profile=stream port=ether1,ether2 src-mac-address=00:01:02:00:00:00/FF:FF:FF:00:00:00 switch=switch1
add new-qos-profile=voip port=ether1,ether2 src-mac-address=04:05:06:00:00:00/FF:FF:FF:00:00:00 switch=switch1
```

## QoS 強制執行 {#qos-enforcement}

### 硬體佇列 {#hardware-queues}

每個交換器埠都有八個硬體傳輸（Tx）佇列（queue0 至 queue7）。每個佇列對應一個由 [QoS profile](#qos-profile) 定義的流量類別（tc0 至 tc7）。當封包進入交換器時，它會獲得 QoS profile 指派，這會決定流量類別，並據此選擇適當的出口佇列進行傳輸。

硬體佇列具有可變大小，由 [Transmission Manager](#transmission-manager) 設定。此外，多個埠與佇列可以透過稱為 *Shared Buffers* 的機制彼此共用資源。例如，具有 25 個埠的設備，其緩衝記憶體足以總共佇列 1200 個封包。若資源平均分配，每個埠會獲得 48 個專用緩衝區，每個佇列最多 6 個封包（48 除以 8），這通常不足以吸收即使是短暫的流量突發。不過，若配置 50% 的緩衝區供共用，每個埠會保留 24 個專用緩衝區（每個佇列 3 個），同時允許單一佇列成長至最多 603 個緩衝區（3 個專用加上 600 個共用）。

RouterOS 可針對每個佇列個別啟用或停用共用集區。這項功能有助於避免低優先順序流量耗盡所有可用的硬體記憶體。此外，埠緩衝區限制可以限制單一低速埠佔用整個共用集區。如需更多詳細資訊，請參閱 [QoS Settings](#qos-settings) 與 [Transmission Manager](#transmission-manager)。

:::info
預設的 best-effort 流量類別（PCP=0、DSCP=0）是流量類別 1，而最低優先順序流量（PCP=1）使用流量類別 0。
:::

## 硬體資源 {#hardware-resources}

交換器晶片具有有限的硬體資源（記憶體）。有兩個主要硬體資源與 QoS 作業相關：

- **Packet descriptor** - 包含封包控制資訊，例如目標埠、標頭修改及其他中繼資料。
- **Data buffer** - 儲存實際封包酬載的記憶體區塊。緩衝區大小會依交換器晶片型號而異；通常為 256 位元組。

一個封包 descriptor 可能会使用多個緩衝區（取決於酬載大小），而在多點傳送或廣播流量的情況下，緩衝區也可能由多個 descriptor 共用。如果硬體沒有足夠的可用 descriptor 或緩衝區，封包就會被丟棄（tail-drop）。

硬體資源可依目的地類型（multicast/unicast）、埠或 TX 佇列進行限制。當達到其中任何一項限制時，就無法再將額外封包排入傳輸佇列，後續封包會被丟棄。

RouterOS 會抽象化底層硬體細節，讓資源限制能以封包數或總量百分比來設定。RouterOS 會根據使用者指定的封包限制與埠的 MTU，自動計算所需的硬體描述項與緩衝區數量。此外，RouterOS 內含預先設定好的硬體資源，因此在常見 QoS 情境中不需要手動設定。

:::danger
在執行階段修改任何硬體資源配置參數，都會造成設備短暫停止運作，期間無法將封包排入佇列或傳送。設備轉送流量時，預期會發生短暫封包遺失。
:::

## 資源節省（前一代設備） {#resource-saving-previous-generation-devices}

:::info
本節僅適用於**不**支援 **Dynamic Buffers** 的設備。
:::

由於硬體資源無法在執行階段重新配置，RouterOS 無法自動釋放為非作用中埠保留的佇列緩衝區。這些緩衝區會持續閒置。不過，若你知道某個特定埠永遠不會使用（例如，它始終保持實體連線中斷），可以透過指派內建的 "offline" tx-manager 並使用最低資源，手動釋放對應的佇列資源：

```ros
/interface/ethernet/switch/qos/port
set sfp-sfpplus1 tx-manager=offline
set sfp-sfpplus2 tx-manager=offline
```

:::danger
請勿在 **switch-cpu** 埠上設定 "offline" tx-manager。
:::
:::warning
設定 QSFP+ 或 QSFP28 介面的 `tx-manager` 設定時，必須對該埠的全部四個子介面套用相同設定。例如，若介面 qsfp28-1-1 為作用中並以 100Gbps 連線，而子介面（qsfp28-1-2、qsfp28-1-3、qsfp28-1-4）顯示 non-running 旗標，**請勿將 "offline" tx-manager 指派給這些 non-running 子介面**。這樣做也會影響 100Gbps 連線。不過，若四個子介面皆未運行，則可安全地指派 "offline" tx-manager 設定。
:::

## 流量優先順序 {#traffic-prioritization}

硬體支援兩種類型的流量傳輸優先順序：

- **Strict Priority**：來自較高佇列的流量一律先傳送。
- **Enhanced Transmission Selection (ETS)**：多個佇列透過加權循環方式，同時參與封包傳輸排程。

**Strict Priority** 佇列相當單純。如果最高優先順序佇列（Q7）有封包，就會先傳送這些封包。當 Q7 清空時，才會傳送 Q6 的封包，依此類推。來自最低優先順序佇列（Q0）的封包，只有在其他所有佇列都清空時才會傳送。

嚴格優先順序的缺點是，在過度優先處理較高佇列時，會增加較低佇列的延遲。假設 TC5 可接受的延遲為 20ms，TC3 為 50ms。出現在 Q5 的流量會因為佇列的嚴格優先順序而立即傳送，並對較低佇列（Q4..Q0）中的每個封包增加額外延遲。Q5 中的封包爆量（例如語音通話開始）可能暫時讓 Q3「癱瘓」，使 TC3 延遲超過可接受的 50ms（甚至因佇列已滿而導致封包丟棄），而 TC5 封包則以 &lt;1ms 傳送（遠低於 20ms 限制）。若在中間穿插傳送 TC3 封包，稍微犧牲 TC5 延遲，就能讓各方都滿意。這正是 **ETS** 的用途。

**Enhanced Transmission Selection (ETS)** 會以加權循環方式，排程來自多個佇列（群組成員）的流量進行傳送。佇列的權重會設定每一輪從該佇列傳送的封包數量。例如，如果 Q2、Q1 與 Q0 是群組成員，且權重分別為 3、2 與 1，則排程器會從 Q2 傳送 3 個封包、從 Q1 傳送 2 個、從 Q0 傳送 1 個。上述範例中每一輪的實際傳送順序為「Q2、Q1、Q0、Q2、Q1、Q2」，以達到更公平的排程。

硬體有兩個群組：`low-priority-group` 與 `high-priority-group`。兩個群組之間有嚴格的優先順序：只有當 *high-priority-group* 中的*所有*佇列都清空時，*low-priority-group* 才會傳送。不過，也可以只使用一個群組處理所有佇列。

以下列出預設（內建）RouterOS 佇列設定。Q3-Q5 在 high-priority group 內共用頻寬，並在 Q6 與 Q7 清空時傳送封包。Q0-Q2 是 low-priority-group 的成員，並在 Q3-Q7 清空時傳送封包。

```ros
[admin@MikroTik] /interface/ethernet/switch/qos/tx-manager/queue> print 
Columns: TX-MANAGER, TRAFFIC-CLASS, SCHEDULE, WEIGHT, QUEUE-BUFFERS, USE-SHARED-BUFFERS
#  TX-MANAGER  TRAFFIC-CLASS  SCHEDULE             WEIGHT  QUEUE-BUFFERS  USE-SHARED-BUFFERS
0  default     0              low-priority-group   1       auto           no                
1  default     1              low-priority-group   2       auto           yes                
2  default     2              low-priority-group   3       auto           yes                
3  default     3              high-priority-group  3       auto           yes               
4  default     4              high-priority-group  4       auto           yes               
5  default     5              high-priority-group  5       auto           yes               
6  default     6              strict-priority              auto           yes               
7  default     7              strict-priority              auto           yes 
```

:::tip
建議所有群組成員彼此相鄰。
:::

## 主動佇列管理 (AQM) {#active-queue-management-aqm}

### 加權隨機早期偵測 (WRED) {#weighted-random-early-detection-wred}

WRED 是一種以個別佇列為基礎運作的壅塞控制機制。它會在佇列溢位發生前丟棄封包，向端點設備通知壅塞事件。WRED 依賴端點中會對封包遺失作出反應的速率節流機制，例如 TCP/IP。

WRED 使用隨機封包丟棄演算法來預期壅塞事件，並在壅塞實際發生前節流流量速率以作出回應。WRED 的隨機特性可避免 TCP 流量全域同步所造成的吞吐量崩潰。

WRED 可在每個 Tx Manager 中依佇列啟用或停用。請針對不允許遺失的流量類別停用 WRED。對於原本就不應發生壅塞的高速埠，也沒有理由啟用 WRED。

其行為由 WRED 臨界值控制。WRED 臨界值定義可超過佇列共用緩衝區限制 (cap) 的封包或位元組數量上限。當佇列使用量超過其對應容量時，即開始隨機丟棄封包：

- `queueX-packet-use > queueX-shared-packet-cap`，或
- `queueX-byte-use > queueX-shared-byte-cap`。

使用量超過容量的程度越高，封包丟棄的機率就越高，並在 `queueX-shared-packet-cap + wred-packet-threshold`（或對應的位元組值）時達到 100%。

RouterOS 會根據佇列或共用集區容量自動選擇實際的 WRED 臨界值。使用者可以透過 QoS 設定調整臨界值。

:::danger
WRED 需要對應的 Tx 佇列使用共用緩衝區（**use-shared-buffers=yes**）。
:::

選擇 WRED 臨界值時，需要在預期壅塞與吸收突發流量之間取捨。設定較高的 WRED 臨界值可能導致更早限制流量速率，因此可解決壅塞。不過，過高的臨界值會在有限的流量突發期間造成封包丟棄，而這些封包原本可由佇列緩衝區吸收，並在 WRED 未啟動時以無遺失方式傳送。

例如，建立遠端資料庫連線時，通常會在初始化階段產生較大的流量（「封包突發」），之後流量速率會降至「合理」水準。初始化階段期間的任何封包丟棄，都會因需要重新傳送而導致資料庫連線變慢。因此，建議對這類流量降低 WRED 臨界值，或完全停用 WRED。相反的情況是影片串流，及早偵測壅塞有助於選擇舒適的串流速率，而不會因重新傳送浪費過多頻寬，或犧牲品質等級。

:::info
使用 Switch Rules (ACL) 或其他 QoS Marking 技術來區分流量，並將封包放入具有所需 WRED 設定的佇列。
:::

下列指令碼只將 WRED 套用至 TCP/IP 流量，方法是將其重新導向至 queue2。UDP 與其他封包仍保留在 queue1，因為其端點通常無法回應早期丟棄。Queue1 與 queue2 會以相同方式排程，不會優先處理其中一個佇列：

```ros
/interface/ethernet/switch/qos/profile
add name=tcp-wred traffic-class=2 pcp=0 dscp=0

# move TCP traffic to queue2
/interface/ethernet/switch/rule
add new-qos-profile=tcp-wred ports=ether1,ether2,ether3,ether4 protocol=tcp switch=switch1

# set the same scheduling priority (weight) between queue1 and queue2
# apply WRED only to queue2 - TCP traffic
/interface/ethernet/switch/qos/tx-manager/queue/
set [find where traffic-class=1] weight=2 schedule=low-priority-group use-shared-buffers=yes wred=no
set [find where traffic-class=2] weight=2 schedule=low-priority-group use-shared-buffers=yes wred=yes
```

## 明確壅塞通知（ECN） {#explicit-congestion-notification-ecn}

部分交換器晶片型號支援 IP 封包的硬體層級 ECN 標記，符合 RFC 3168。此機制的運作方式與 WRED 類似，但在壅塞期間不會丟棄封包，而是會在 ECN 欄位中標記 CE（Congestion Experienced，二進位 11）旗標。只有支援 ECN 的 IP 封包才會收到此標記，也就是 ECN 欄位值為 ECT(1) 或 ECT(0)（二進位 01 或 10）的封包。不支援 ECN 的傳輸封包（ECN=00）永遠不會被標記。如果封包已帶有 CE 標記（ECN=11），則無論設備是否發生壅塞，都會保留此標示。

在所需的 [Tx Manager Queue](/docs/bridging-and-switching/quality-of-service#transmission-manager) 上設定 **ecn=yes**，即可啟用 ECN 標記。

:::danger
ECN 標記機制需要對應的 Tx 佇列使用共用緩衝區（**use-shared-buffers=yes**）。
:::

當下列**所有**條件都符合時，封包會收到 CE 標記：

1. 封包為 IPv4 或 IPv6。
2. IP 標頭中的 ECN 欄位值為 ECT(1) 或 ECT(0)。
3. egress 埠的 Tx Queue 已啟用 **ecn=yes**，並使用共用緩衝區（**use-shared-buffers=yes**）。
4. 佇列使用量超過共用緩衝區容量：`queueX-packet-use > queueX-shared-packet-cap` 或 `queueX-byte-use > queueX-shared-byte-cap`。

:::danger
由於啟用 ECN（ecn=yes）會避免丟棄支援 ECN 的封包，如果流量傳送端未及時回應壅塞通知，佇列使用量可能會超過 WRED 臨界值。
:::

## 以優先順序為基礎的流量控制（PFC） {#priority-based-flow-control-pfc}

Priority-based Flow Control (PFC) 可讓最多八種流量類別以不丟失封包的方式運作，確保某一流量類別發生壅塞時，不會暫停其他類別的流量。這讓對丟失敏感的流量類型與可容忍丟失的流量類型可以在同一網路上共存。

支援 PFC 的交換器晶片符合 IEEE 802.1Qbb PFC 標準，也就是說，它們可以產生並回應 PFC 訊框。當出口埠發生壅塞時，來源埠會針對受影響的流量類別傳送 PFC 訊框。產生的 PFC 訊框會使用計時器值 0xFFFF 表示暫停（XOFF），使用 0x0 表示恢復（XON），並在優先權啟用向量中設定對應位元。在接收端，PFC 訊框會依訊框中指定的期間，暫停目的地埠上的特定優先權佇列。

在 RouterOS 中，PFC 設定以設定檔組織。每個埠都可以指派至特定的 PFC 設定檔，該設定檔定義要啟用 PFC 的流量類別、用於傳送 XOFF 與 XON 訊框的暫停與恢復臨界值，以及所指派的埠是否應傳送及（或）接收 PFC 訊框。

當出口埠發生壅塞時，會在入口埠觸發 PFC。必須使用共用緩衝區，將入口流量與等待在 Tx 佇列中的封包建立關聯。針對每個啟用 PFC 的流量類別，在對應的 Tx 佇列上設定 **use-shared-buffers=yes**。

:::info
RouterOS 在流量類別與 Tx 佇列之間實作 1:1 對應。流量類別 0 的封包會進入 queue0，TC1 進入 queue1，依此類推，直到 TC7 進入 queue7。因此，本文件中「traffic class」與「Tx queue」這兩個詞可互換使用。
:::

選擇暫停與恢復臨界值時，請考量傳送與處理 PFC 訊框的延遲。例如，設備 A 在時間 T 發生壅塞，傳送 PFC 暫停訊框給設備 B，而 B 在時間 T+D 處理該訊框並停止傳送。在 D 這段時間差內，設備 B 會繼續傳送流量。如果設備 A 將暫停臨界值設定為 100%，表示沒有可用的空閒緩衝區，封包可能會丟棄，這對無遺失流量類別而言是不可接受的。設定較低的暫停臨界值（例如 80%），會在仍保留空閒記憶體以吸收 D 這段時間差內的流量時，傳送 PFC 暫停訊框。相同的原則也適用於恢復臨界值。將其設定為 0% 會讓設備在這段時間差內保持閒置，降低整體吞吐量。

PFC 接收需要為所有相關佇列設定出口速率，以計算暫停時間，即使該速率與線路速度相同也一樣。例如，如果 PFC 在流量類別 3 上執行，所指派的埠需要 `egress-rate-queue3` 設定。

```routeros
/interface/ethernet/switch/qos/priority-flow-control/add name=pfctc3 traffic-class=3 rx=yes
/interface/ethernet/switch/qos/port/set sfp-sfpplus1,sfp-sfpplus2 pfc=pfctc3 egress-rate-queue3=10G
```

## 屬性參考 {#property-reference}

### 交換器設定 {#switch-settings}

**子選單：** `/interface/ethernet/switch`

交換器 QoS 設定（除了現有設定之外）。

| 屬性 | 說明 |
| :-- | :-- |
| **qos-hw-offloading** (*yes \| no*；預設：**no**) | 允許為指定交換器晶片啟用 QoS（若其支援 QoS）。<br/> 新一代設備會強制始終使用 <strong>qos-hw-offloading=yes</strong>。 |

:::tip
啟用 QoS 後，關閉 **qos-hw-offloading** 設定並不會完全還原至先前的功能。建議在停用後重新啟動設備。
:::

### 埠設定 {#port-settings}

**子選單：** `/interface/ethernet/switch/qos/port`

此子選單用於設定個別交換器埠的 QoS 設定。它可讓你將 QoS 設定檔指派給抵達特定埠的入口封包。若該埠設定為信任，指派的設定檔可由根據封包標頭值進行比對的規則覆蓋。

預設情況下，所有埠皆為不受信任，並接收預設 QoS 設定檔（Best-Effort、PCP=0、DSCP=0）。在此預設狀態下，優先權欄位會從出口封包中清除。

#### 埠統計資訊 {#port-stats}

**Example**

```ros
[admin@Mikrotik] /interface/ethernet/switch/qos/port> print stats where name=ether2
                  name:     ether2
             tx-packet:      2 887
               tx-byte:  3 938 897
           drop-packet:      1 799
             drop-byte:  2 526 144
      tx-queue0-packet:         50
      tx-queue1-packet:      1 871
      tx-queue3-packet:        774
      tx-queue5-packet:        192
        tx-queue0-byte:      3 924
        tx-queue1-byte:  2 468 585
        tx-queue3-byte:  1 174 932
        tx-queue5-byte:    291 456
    drop-queue1-packet:      1 799
      drop-queue1-byte:  2 526 144
```

| Property | Description |
| :-- | :-- |
| **name** | 埠名稱。 |
| **tx-packet** | 透過此埠傳送的封包總數。 |
| **tx-byte** | 透過此埠傳送的位元組總數。 |
| **drop-packet** | 應透過此埠傳送，但因為資源不足（例如佇列緩衝區）或 QoS Enforcement 而遭丟棄的封包總數。 |
| **drop-byte** | 應透過此埠傳送，但遭丟棄的位元組總數。 |
| **tx-queue0-packet** .. **tx-queue7-packet** | 從對應佇列透過此埠傳送的封包數。 |
| **tx-queue0-byte** .. **tx-queue7-byte** | 從對應佇列透過此埠傳送的位元組數。 |
| **drop-queue0-packet** .. **drop-queue7-packet** | 從對應佇列遭丟棄的封包數（或因資源不足而完全未加入佇列）。 |
| **drop-queue0-byte** .. **drop-queue7-byte** | 從對應佇列遭丟棄的位元組數。 |

#### 埠資源／使用情況 {#port-resourcesusage}

:::danger
由於硬體限制，部分交換器晶片型號在存取 QoS 埠 `usage` 資料時，可能會中斷流量。請僅將埠 `usage` 用於診斷／疑難排解。若要進行監控，請改用 QoS `monitor` 或 Port `stats`。
:::

**Example**

```ros
[admin@crs326] /interface/ethernet/switch/qos/port> print usage where name=ether2
                 name:  ether2
           packet-cap:     136
           packet-use:       5
             byte-cap:  35 840
             byte-use:   9 472
    queue0-packet-cap:     130
    queue0-packet-use:       1
    queue1-packet-cap:       5
    queue1-packet-use:       4
    queue3-packet-cap:      65
    queue3-packet-use:       2
      queue0-byte-cap:  24 576
      queue0-byte-use:     256
      queue1-byte-cap:   7 680
      queue1-byte-use:   6 144
      queue3-byte-cap:  14 080
      queue3-byte-use:   3 072
```

| Property | Description |
| :-- | :-- |
| **name** | 埠名稱。 |
| **packet-cap** | 埠的封包容量。可加入佇列以透過該埠傳送的封包數上限。 |
| **packet-use** <sup>1</sup> | 埠的封包使用量。目前在所有埠佇列中加入佇列的封包數。 |
| **byte-cap** | 埠的位元組容量（緩衝區大小）。可加入佇列以透過該埠傳送的位元組數上限。 |
| **byte-use** <sup>1</sup> | 埠的位元組使用量。目前為已加入佇列的封包所配置的硬體緩衝區大小（以位元組為單位）。由於緩衝區是以區塊配置（通常每塊 256B），因此配置的緩衝區大小可能大於實際酬載。 |
| **queue0-packet-cap** .. **queue7-packet-cap** <sup>2</sup> | 個別佇列容量。可在對應佇列中加入佇列的封包數上限（除非啟用 **Shared Buffers**）。 |
| **queue0-shared-packet-cap** .. **queue7-shared-packet-cap** <sup>2</sup> | 共用佇列容量（個別佇列容量 + 共用緩衝區）。可在對應佇列中加入佇列的封包數上限。 |
| **queue0-packet-use** .. **queue7-packet-use** <sup>2</sup> | 佇列封包使用量。對應佇列中已加入佇列的封包數。 |
| **queue0-byte-cap** .. **queue7-byte-cap** <sup>2</sup> | 個別佇列容量。可在對應佇列中加入佇列的位元組數上限（除非啟用 **Shared Buffers**）。 |
| **queue0-shared-byte-cap** .. **queue7-shared-byte-cap** <sup>2</sup> | 共用佇列容量（個別佇列容量 + 共用緩衝區）。可在對應佇列中加入佇列的位元組數上限。 |
| **queue0-byte-use** .. **queue7-byte-use** <sup>2</sup> | 佇列緩衝區使用量（以位元組為單位）。目前為對應佇列中的封包所配置的硬體緩衝區大小（以位元組為單位）。 |
| **queue0-byte-max** .. **queue7-byte-max** <sup>2</sup> | 佇列緩衝區最高填充水準（以位元組為單位）。僅在提供佇列統計服務的裝置上可用。使用 `reset-counters` 指令重設數值。 |

<sup>**1**</sup> Port's packet/byte usage can exceed the capacity if Shared Buffers are enabled.  
<sup>**2**</sup> Only the queues in use are printed.

#### 連接埠 PFC 統計資料（舊世代） {#port-pfc-stats-previous-generations}

**Example**

```ros
[admin@crs317] /interface/ethernet/switch/qos/port> print pfc interval=1 where running
                 name:  sfp-sfpplus1 sfp-sfpplus2   ether1
                  pfc:          roce     disabled disabled
               pfc-tx:            46            
        pfc-paused-tc:             3            
 pfc3-pause-threshold:     1 048 576            
pfc3-resume-threshold:        10 240            
             pfc3-use:     1 075 200
```

| Property | Description |
| :-- | :-- |
| **name** | 埠名稱。 |
| **pfc** | PFC 設定檔名稱。 |
| **pfc-rx** | 接收的 PFC 訊框數。 |
| **pfc-tx** | 傳送的 PFC 訊框數。 |
| **pfc-paused-tc** | 應暫停的流量類別清單（從傳送端的角度）。系統會定期傳送 PFC 暫停訊框（XOFF），並從此埠設定列出的計時器。 |
| **pfc0-pause-threshold .. pfc7-pause-threshold** | 對應流量類別的暫停閾值。僅顯示已啟用 PFC 的流量類別。 |
| **pfc0-resume-threshold .. pfc7-resume-threshold** | 對應流量類別的恢復閾值。僅顯示已啟用 PFC 的流量類別。 |
| **pfc0-use .. pfc7-use** | 對應流量類別目前的緩衝區使用量（以位元組為單位）。換句話說，這是從此埠接收、且在所有埠上排入佇列的所有封包總大小。僅顯示已啟用 PFC 的流量類別。 |

#### 新一代連接埠 PFC 統計資料 {#port-pfc-stats-new-generations}

**Example**

```routeros
[admin@crs812] /interface/ethernet/switch/qos/port> print pfc interval=1 where pfc=roce
                 name:       sfp56-5 
                  pfc:          roce
             rx-pause:           287              
             tx-pause:            46             
             pfc3-use:     2 184 200 
```

| 屬性 | 說明 |
| :-- | :-- |
| **name** | 埠名稱。 |
| **pfc** | PFC 設定檔名稱。 |
| **pfc0-use .. pfc7-use** | 各流量類別目前的緩衝區使用量（以位元組為單位）。換句話說，這是從此埠接收、並在所有埠上排隊的所有封包的總大小。只會顯示已啟用 PFC 的流量類別。 |
| **rx-pause** | 接收的暫停訊框計數。 |
| **tx-pause** | 傳送的暫停訊框計數。 |

### QoS 選單 {#qos-menu}

**子選單：** `/interface/ethernet/switch/qos`

整個 QoS 硬體設定位於 `/in/eth/sw/qos` 下。這種集中式方式可讓你將所有 QoS 相關設定項目儲存在同一處，方便使用 `/in/eth/sw/qos/export` 監控與匯出設定。

QoS 項目有兩個主要的旗標指示：

- **H** - 硬體卸載項目。
- **I** - 非作用中項目。

### QoS 設定 {#qos-settings}

**子選單：** `/interface/ethernet/switch/qos/settings`

| 屬性 | 說明 |
| :-- | :-- |
| **mirror-buffers** (*percent**: 1..90*; Default: **auto**) | [鏡像](/docs/bridging-and-switching/marvell-prestera-switch-chip-features#mirroring)流量的最大封包緩衝區數量（佔緩衝區總記憶體的百分比）。 |
| **mirror-profile** (*name*; Default: **default**) | 要指派給[鏡像](/docs/bridging-and-switching/marvell-prestera-switch-chip-features#mirroring)封包的 [QoS profile](#qos-profile) 名稱（請參閱 **`/in/eth/sw/qos/profile`**）。 |
| **multicast-buffers** (*percent**: 1..90*; Default: **auto**) | 多播／廣播流量的最大封包緩衝區數量（佔緩衝區總記憶體的百分比）。 |
| **shared-buffers** (*percent**: 0..90*; Default: **auto**) | 可在埠之間共用的最大封包緩衝區數量（佔緩衝區總記憶體的百分比）。設定為 0 會停用緩衝區共用。其餘緩衝區記憶體會分配給各埠。 <br/> 在使用 <strong>Dynamic Buffers</strong> 的新一代交換器晶片上，所有緩衝區都會被視為共用。交換器晶片會根據目前的壅塞程度自動調整埠與佇列的緩衝區限制。使用 auto 值可讓設備利用 100% 的可用緩衝區記憶體，這是大多數情境的建議設定。在特定使用情境中，若延遲比避免封包丟棄更重要，可以手動降低緩衝區限制。 |
| **lossless-buffers**(*percent**: 0..100*; Default: **auto**) | 如果設備支援多個共用緩衝區集區，此設定可調整無損集區的大小（佔 *shared* 緩衝區記憶體的百分比，其中 100% 表示由 **shared-buffers** 設定配置的所有共用緩衝區）。例如，若 shared-buffers=50 且 lossless-buffers=80，無損集區會取得緩衝區總記憶體的 40%（50% 的 80%，即 "0.8 \* 0.5 = 0.4"），而有損集區會取得其餘 10% 的共用緩衝區。 |
| **lossless-traffic-class**(*integer array: 0..7*; Default: **auto**) | 無損流量類別清單。 |
| **wred-threshold**(*low \| medium \| high;*Default: **medium**) | 在共用佇列上限（`queueX-shared-packet-cap` 或 `queueX-shared-byte-cap`）之上，開始發生隨機丟棄的相對封包數量。此臨界值僅套用於已啟用 [Weighted Random Early Detection](/docs/bridging-and-switching/quality-of-service#weighted-random-early-detection-wred)（**wred=yes**）且使用共用緩衝區（****use-shared-buffers=yes)****）的佇列。佇列緩衝區填充程度越高，封包丟棄機率越高。*low* 臨界值表示隨機尾部丟棄較晚開始；*high* 則較早開始。 |

### QoS 監控 {#qos-monitor}

**指令：**`/interface/ethernet/switch/qos/monitor`

#### 範例 {#example}

```ros
[admin@crs312] /interface/ethernet/switch/qos> monitor once
           total-packet-cap: 11 480   
           total-packet-use: 0        
             total-byte-cap: 2648.0KiB
             total-byte-use: 0        
       multicast-packet-cap: 1 148    
       multicast-packet-use: 0        
         multicast-byte-cap: 264.8KiB 
         multicast-byte-use: 0        
  mirror-ingress-packet-cap: 1 148    
  mirror-ingress-packet-use: 0        
    mirror-ingress-byte-cap: 264.8KiB 
    mirror-ingress-byte-use: 0        
   mirror-egress-packet-cap: 1 148    
   mirror-egress-packet-use: 0        
     mirror-egress-byte-cap: 264.8KiB 
     mirror-egress-byte-use: 0        
      lossy-pool-packet-cap: 2 301    
      lossy-pool-packet-use: 0        
   lossless-pool-packet-cap: 2 301    
   lossless-pool-packet-use: 0        
        lossy-pool-byte-cap: 530.0KiB 
        lossy-pool-byte-use: 0        
     lossless-pool-byte-cap: 530.0KiB 
     lossless-pool-byte-use: 0 
```

監控硬體 QoS 資源。

| 屬性 | 說明 |
| :-- | :-- |
| **total-packet-cap** *(integer)* | 封包總容量。設備可在所有佇列中儲存的硬體封包描述元最大數量。 |
| **total-packet-use** *(integer)* | 封包總使用量。目前位於硬體記憶體中的封包描述元數量。 |
| **total-byte-cap** *(byte)* | Tx 記憶體總容量。 |
| **total-byte-use** *(byte)* | Tx 記憶體總使用量。所有 tx 佇列中封包所佔用的目前位元組數。 |
| **multicast-packet-cap***(integer)* | 多播封包容量。可供多播／廣播流量使用的硬體封包描述元最大數量。取決於 **multicast-buffers** 設定。 |
| **multicast-packet-use** *(integer)* | 多播封包使用量。硬體會為每個多播目的地複製一份封包描述元。 |
| **mirror-ingress-packet-cap** *(integer)* | 入口鏡像封包容量。可供入口鏡像流量使用的硬體封包描述元最大數量。取決於 **mirror-buffers** 設定。 |
| **mirror-ingress-packet-use** *(integer)* | 入口鏡像封包使用量。 |
| **mirror-ingress-byte-cap** *(byte)* | 入口鏡像位元組容量。取決於 **mirror-buffers** 設定。 |
| **mirror-ingress-byte-use** *(byte)* | 入口鏡像位元組使用量。 |
| **mirror-egress-packet-cap** *(integer)* | 出口鏡像封包容量。可供出口鏡像流量使用的硬體封包描述元最大數量。取決於 **mirror-buffers** 設定。 |
| **mirror-egress-packet-use** *(integer)* | 出口鏡像封包使用量。 |
| **mirror-egress-byte-cap** *(byte)* | 出口鏡像位元組容量。取決於 **mirror-buffers** 設定。 |
| **mirror-egress-byte-use** *(byte)* | 出口鏡像位元組使用量。 |
| **shared-packet-cap** *(integer)* | 共用封包容量。可在埠與 tx 佇列之間共用的硬體封包描述元最大數量。取決於 **shared-buffers** 設定。 |
| **shared-packet-use** *(integer)* | 共用封包使用量。所有 tx 佇列目前使用的共用封包描述元數量。 |
| **shared-byte-cap** *(byte)* | 共用 Tx 記憶體容量。取決於 **shared-buffers** 設定。 |
| **shared-byte-use** *(byte)* | 共用 Tx 記憶體使用量。所有 tx 佇列中封包所佔用的共用緩衝區數量。 |
| **lossy-pool-packet-cap**(integer) | 有損集區的共用封包容量。如果設備不支援多個共用集區，則會省略此欄位。 |
| **lossy-pool-packet-use (integer)** | 有損集區的共用封包使用量。如果設備不支援多個共用集區，則會省略此欄位。 |
| **lossless-pool-packet-cap (integer)** | 無損集區的共用封包容量。如果設備不支援多個共用集區，則會省略此欄位。 |
| **lossless-pool-packet-use (integer)** | 無損集區的共用封包使用量。如果設備不支援多個共用集區，則會省略此欄位。 |
| **wred-packet-cap** *(integer)* | 佇列可在共用上限（`queueX-shared-packet-cap`，位於 `/in/eth/sw/qos/port/print usage`）之上使用，以觸發隨機尾部丟棄的最大封包數。例如，若 `queue1-shared-packet-cap=3072` 且 `wred-packet-cap=512`，當 `queue1-packet-use` 超過 3072 時，WRED 會觸發，並在 3072+512=3584 個封包時達到 100% 丟棄率。 |
| **wred-byte-cap** *(integer)* | 佇列可在共用上限（`queueX-shared-byte-cap`）之上使用，以觸發隨機尾部丟棄的最大位元組數。例如，若 `queue1-shared-byte-cap=768KiB` 且 `wred-byte-cap=128KiB`，當 `queue1-packet-use` 超過 768KiB 時，WRED 會觸發，並在 768+128=896KiB 時達到 100% 丟棄率。 |

### QoS 設定檔 {#qos-profile}

**子選單：**`/interface/ethernet/switch/qos/profile`

QoS 設定檔會決定轉送／路由封包的優先順序欄位值（PCP、DSCP）。壅塞避免／解決是根據 QoS 設定檔。每個封包都會根據 ingress 交換器埠的 QoS 設定指派一個 QoS 設定檔（請參閱 `/in/eth/sw/port`）。

| 屬性 | 說明 |
| :-- | :-- |
| ****color**** (*green \| yellow \| red*; Default: **green**) | 用於支援色彩感知（color-aware）的丟棄優先順序管理之流量色彩。若使用不支援色彩感知（color-blind）的丟棄優先順序管理，請保留預設值（green）。 |
| ****dscp**** (*integer: 0..63*; Default: **0**) | 指派給 QoS 設定檔的 egress 封包之 IPv4/IPv6 DSCP 欄位值。 |
| **name** (*string*; Default: ) | 使用者定義的 QoS 設定檔名稱。 |
| **pcp** (*integer: 0..7*; Default: **0**) | VLAN 優先順序值（IEEE 802.1q PCP - Priority Code Point）。僅當指派給 QoS 設定檔的 egress 封包具有 VLAN 標籤（具備 802.1q 標頭）時使用。此值可透過 QoS Egress Map 進一步變更。 |
| **traffic-class** (*integer: 0..7*; Default: **0**) | 流量類別會決定封包優先順序與 egress 佇列（請參閱 **tx-manager**）。佇列編號通常與流量類別相同（tc0 的封包會進入 queue0，tc1 - queue1，... tc7 - queue7）。與 pcp 不同，pcp 中 0 表示預設優先順序，而 1 表示最低優先順序（且可進一步自訂），流量類別則是嚴格排序。TC0 一律選擇最低優先順序，依此類推。 |
| ******automap******(yes*\| no*; Default: **yes**) | 自動將具有相符 PCP 或 DSCP 值的封包對應至此 QoS 設定檔。僅適用於 **trusted** 埠。 |

### QoS 對應 {#qos-mapping}

**子選單：** `/interface/ethernet/switch/qos/map`

信任封包的優先順序對設定檔對應表。所有交換器晶片都有一個內建對應表：**default**。此外，部分型號可讓使用者定義自訂對應表，並透過 **qos-map** 屬性將不同對應表指派給各種交換器埠：

- 以 **Marvell Prestera **98DX224S, 98DX226S**** 或 ****98DX3236**** 交換器晶片型號為基礎的設備僅支援一個對應表：default。
- 以 **Marvell Prestera 98DX8xxx**、**98DX4xxx** 交換器晶片或 **98DX325x** 型號為基礎的設備最多支援 12 個對應表（預設值 + 11 個使用者定義）。

| 屬性 | 說明 |
| :-- | :-- |
| **name** (*string*; Default: ) | 使用者定義的對應表名稱。 |

#### `VLAN Map`

**子選單：** `/interface/ethernet/switch/qos/map/vlan`

將 VLAN 優先順序（802.1p PCP/DEI 欄位）比對至 QoS 設定檔。預設會將所有值比對至預設 QoS 設定檔。

| 屬性 | 說明 |
| :-- | :-- |
| ****dei-only**** (yes *\| no*；預設：**no**) | 僅比對 VLAN 標頭中已設定 DEI（舊稱 CFI）位元的封包。 |
| **map** (*name*；預設：**default**) | 比對表的名稱。 |
| **profile** (*name*；預設： ) | 要指派給符合封包的 QoS 設定檔名稱。 |
| **pcp** (*range: 0..7*；預設：**0**) | 用於查閱的 VLAN 優先順序（PCP）值。 |

#### DSCP 對應表 {#dscp-map}

**子選單：** `/interface/ethernet/switch/qos/map/ip`

將 DSCP 值比對至 QoS 設定檔。

| 屬性 | 說明 |
| :-- | :-- |
| **dscp** (*range: 0..63*；預設：**0**) | 用於查閱的 DSCP 值。 |
| **map** (*name*；預設：**default**) | 比對表的名稱。若未設定，則會變更標準（內建）比對表。 |
| **profile** (*name*；預設： ) | 要指派給符合封包的 QoS 設定檔名稱。 |

### 傳輸管理員 {#transmission-manager}

**子選單：** `/interface/ethernet/switch/qos/tx-manager`

Transmission (Tx) Manager 控制封包傳送時的入佇列與封包傳送順序。不同的交換器埠可以指派給不同的 Tx Manager。硬體 Tx Manager 的最大數量取決於交換器晶片型號。

| 屬性 | 說明 |
| :-- | :-- |
| **name** (*string*; Default: ) | 使用者定義的 Tx Manager 名稱 |
| **queue-buffers***(percent: 0%..100% \| bytes \| auto;*Default:**auto**) | 配置給所有連結至此 Tx Manager 的埠的硬體 Tx 緩衝區總數。除 **auto** 外的任何值都不會依埠數縮放。例如，若 queue-buffers=30%，且有 3 個埠使用此 Tx Manager，則每個埠會取得總可用資源的 10%。再新增兩個埠至 Tx Manager 後，每個埠的緩衝區會降至 6%（30/5）。 |

:::info
埠狀態不影響已配置的資源。若所有埠都指派給同一個 Tx Manager，則運作中的埠會與未連線或已停用的埠取得相同數量的佇列緩衝區。
:::

#### 傳送佇列排程器 {#transmission-queue-scheduler}

**子選單：** `/interface/ethernet/switch/qos/tx-manager/queue`

每個埠都有八個 Tx 佇列。指派的 Tx Manager 會控制封包入佇列，並排程傳送順序。每個佇列可以使用嚴格優先權（具有最高流量類別的封包永遠會先傳送），或分組在一起進行加權循環傳送排程。

建立 Tx Manager 時，會自動建立對應的八個佇列排程器。

:::danger
變更 Tx manager 或佇列的任何屬性，會在卸載程序中完全停止封包的入佇與傳輸。設備轉發流量時，預期會發生短暫封包遺失。
:::

| 屬性 | 說明 |
| :-- | :-- |
| **tx-manager** (*name*; *read-only*) | 連結的 Tx Manager |
| **traffic-class** (*integer: 0..7*;  *read-only*) | 排程器控制的流量類別（tc0..tc7）及對應的埠佇列（queue0..queue7）。 |
| **schedule**(*strict-priority \| high-priority-group \| low-priority-group* ) | <ul><li><strong>strict-priority</strong> - 對應佇列中的封包一律先於移至較低流量類別前進行排程。目前佇列清空前，不會傳輸流量類別較低的封包。</li><li><strong>high-priority-group</strong> - 群組中的所有佇列會使用加權循環原則一起排程。例如，若 TC5 的權重為 4、TC4 為 3、TC3 為 2，則排程器在單一輪次中會從 queue5 傳輸 4 個封包、從 Q4 傳輸 3 個封包，並從 Q3 傳輸 2 個封包。為了降低延遲，每一輪會在群組內所有佇列之間「切片」。換句話說，上述範例中每一輪的封包順序為「Q5, Q4, Q3, Q5, Q4, Q3, Q5, Q4, Q5」。</li><li><strong>low-priority-group</strong> - 邏輯與 high-priority-group 相似，但只有當 high-priority-group 中的所有佇列皆清空時，才會排程 low-priority-group。</li></ul> |
| **weight** *(integer: 0..255;* 預設: **1**) | 流量類別屬於排程群組時的權重值。使用 strict priority 排程時，不會使用此欄位。 |
| ****queue-buffers*****(percent: 0%..100% \| bytes \| auto;*預設:**auto**) | 配置給此佇列的硬體 Tx 緩衝區數量。除 **auto** 外的任何值都不會依埠數縮放，也就是說，該值會在連結至 Tx Manager 的埠之間拆分。以百分比表示時，代表 tx-manager 的 queue-buffers 值的百分比。 |
| ****use-shared-buffers**** *(yes \| no)* | 允許佇列在 **queue-buffers** 已滿時使用共用緩衝區集區。若佇列已滿且停用共用緩衝區，封包會被丟棄。若啟用共用緩衝區，佇列最多可使用共用集區中的 **shared-packet-cap** 或 **shared-poolX-packet-cap** 個封包（詳情請參閱 [QoS Settings](#qos-settings)）。 |
| ****wred****(*yes \| no*; 預設: **no)** | 啟用或停用指定佇列的 [Weighted Random Early Detection](/docs/bridging-and-switching/quality-of-service#weighted-random-early-detection-wred)。 |
| *****ecn (******yes \| no; 預設: **no**)* | 啟用或停用已傳輸封包的 [ECN marking](http://help.mikrotik.com#ecn)。 |
| ****wred-actual****(*yes \| no*;  read-only) | 實際的 WRED 值。 |
| ****ecn-actual**** (*yes \| no*;  read-only) | 實際的 ECN 值。 |

:::danger
在某些設備型號上，受限於硬體限制，在一個佇列上啟用 ECN 會在所有佇列上開啟支援 ECN 封包的 CE 標記。在此情況下，即使 `ecn=no`，仍會顯示 `ecn-actual=yes`。
:::

### 以優先順序為基礎的流量控制（PFC） {#priority-based-flow-control-pfc-1}

**子選單：** `/interface/ethernet/switch/qos/priority-flow-control`

[PFC](/docs/bridging-and-switching/quality-of-service#priority-based-flow-control-pfc) 設定以設定檔組織。不同的交換器埠可以指派到不同的 PFC 設定檔。硬體 Tx manager 的數量上限取決於交換器晶片型號。內建名為「**disabled**」的設定檔無法變更。

| 屬性 | 說明 |
| :-- | :-- |
| **name** (*string*; 預設: ) | 使用者定義的 PFC 設定檔名稱 |
| **pause-threshold** (*percent: 0%..100% \| bytes \| auto;* 預設: **auto)** | 當入佇封包的總大小達到這個臨界值時，傳輸暫停訊框（XOFF）。入佇封包會依 ingress 埠分別計算。僅在 **tx=yes** 時適用。此值可以明確指定為位元組，或指定為對應共用集區大小的百分比（**shared-poolX-byte-cap**）。 |
| **resume-threshold** (*percent: 0%..100% \| bytes \| auto;* 預設: **auto)** | 當入佇封包的總大小降至這個臨界值時，傳輸恢復訊框（XON）。入佇封包會依 ingress 埠分別計算。僅在 **tx=yes** 時適用。此值可以明確指定為位元組，或指定為對應共用集區大小的百分比（**shared-poolX-byte-cap**）。 |
| ****rx**** (*yes \| no*; 預設: **no)** | 啟用接收 PFC 訊框。接收到的 PFC 訊框會在 PFC 訊框指定的期間內，暫停接收到該 PFC 訊框之埠上的特定優先順序佇列。停用 rx 會停用佇列暫停。 |
| **traffic-class** (*integer array: 0..7*) | 啟用 PFC 的流量類別清單。 |
| **tx** (*yes \| no*; 預設: **no)** | 啟用傳輸 PFC 訊框。 |
