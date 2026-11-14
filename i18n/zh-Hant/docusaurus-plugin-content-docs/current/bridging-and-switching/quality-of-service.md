---
sidebar_key: "bridging-and-switching/quality-of-service"
sidebar_position: 3
title: "服務質量"
sidebar_label: "服務質量"
description: "本文件介紹 MikroTik RouterOS 中適用於搭載 Marvell Prestera 交換晶片裝置的服務質量（QoS）功能，詳細說明 QoS 優先順序、流量整形和擁塞管理。內容涵蓋 RouterOS v7.23 的增強功能，如無損流量支援、動態緩衝區，以及針對各種交換器型號的 QoS 裝置相容性表。"
tags:
  - 'qos'
  - 'marvell-prestera'
  - 'active-queue-management'
source: https://manual.mikrotik.com/docs/bridging-and-switching/quality-of-service
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本文件介紹在配備 **[Marvell Prestera 交換晶片](./marvell-prestera-switch-chip-features.md)** 的裝置上，RouterOS 中 **服務質量（QoS）** 的實現。

QoS 是網路交換器中的一組功能，允許網路管理員對流量劃分優先順序並分配網路資源，以確保關鍵資料流能夠以低延遲順暢傳輸。

網路交換器中 QoS 的主要功能是以滿足不同型別網路應用特定需求的方式來管理流量。例如，語音和影片資料需要低延遲和最小丟包，以確保高質量通訊；而檔案傳輸和其他資料應用則可以承受更高的延遲和丟包。

QoS 透過識別流經交換器的流量型別，並根據其需求分配優先順序來工作。然後，交換器會使用這些資訊修改封包報頭並確定流量傳輸的優先順序，從而確保高優先順序流量比低優先順序流量獲得優先處理。

需要 RouterOS v7.15 或更高版本才能支援所有 QoS 功能：

1. **QoS 標記。** 根據入站封包報頭匹配 QoS 配置檔案，然後按照分配的 QoS 配置檔案修改出站報頭。
2. **QoS 強制執行。** 根據分配的 QoS 配置檔案和流量整形來避免或解決擁塞。
3. **QoS 策略。** 透過 ACL 規則分配 QoS 配置檔案。
4. 主動佇列管理：**WRED**（加權隨機早期檢測）、**ECN** 通知與處理、**PFC**（基於優先順序的流量控制）。
5. 流量整形。

### RouterOS v7.23 中的 QoS 變更 {#qos-changes-in-routeros-v723}

RouterOS v7.23 對服務質量（QoS）解除安裝進行了重大更改。這些更改簡化了配置過程，並新增了對“無損”流量類別的支援。儘管硬體資源是有限的，但當所有連線的裝置都支援這些功能並正確配置時，使用 ECN 和/或 PFC 的主動佇列管理可以防止丟包。此前的 RouterOS 版本已經支援 ECN 和 PFC，但 v7.23 簡化了它們的設定方式。

:::info
並非所有裝置都支援無損流量。請檢視 QoS 裝置支援表。
:::

#### 配置變更摘要 {#configuration-change-summary}

- QoS 設定：大多數更改預設設為“auto”，允許 RouterOS 為當前設定選擇最合適的已知設定。
- QoS 設定：新增 `lossless-traffic-class` 和 `lossless-buffers`，允許顯式指定無損流量併為其預留佇列資源。使用者也可以將這些欄位保留為“auto”。
- QoS 監控：分別顯示有損和無損共享池的使用情況。
- Tx 佇列：移除了共享池索引。RouterOS 會根據流量型別（有損或無損）自動選擇共享池。
- QoS 配置檔案：新增到指定 PCP 和 DSCP 值的自動對映（預設啟用）。例如，新增一個 DSCP=46 的 QoS 配置檔案會自動將該配置檔案應用於從受信任埠接收的流量。

## QoS 術語 {#qos-terminology}

本節定義本文件中使用的關鍵術語和縮寫：

- **QoS** - 服務質量，一組允許網路管理員對流量劃分優先順序並分配網路資源的功能。
- **ACL** - 訪問控制列表，一組用於根據指定條件過濾網路流量的交換器規則。
- **AQM** - 主動佇列管理，一種擁塞控制機制，透過在佇列溢位前丟棄或標記封包來管理流量。
- **DSCP** - 差分服務程式碼點，IP 報頭中的 6 位欄位，用於對網路流量劃分優先順序。
- **ECN** - 顯式擁塞通知，一種允許路由器向端點裝置發出擁塞訊號而不丟棄封包的機制。
- **ETS** - 增強傳輸選擇，一種流量排程方法，使用加權輪詢在多個佇列組之間分配頻寬。
- **PCP** - 優先順序程式碼點，VLAN 報頭中的 3 位欄位，用於在 VLAN 內對流量劃分優先順序。
- **PFC** - 基於優先順序的流量控制（IEEE 802.1Qbb），一種流控制機制，會暫停特定優先順序佇列上的流量以防止丟包。
- **RoCE** - 融合乙太網上的 RDMA，一種支援在乙太網上進行遠端直接記憶體訪問的協定。
- **WRED** - 加權隨機早期檢測，一種擁塞避免機制，在佇列接近容量時隨機丟棄封包。
- **/in/eth/sw/** - `/interface/ethernet/switch/` 的 CLI 快捷方式。

## 新一代 Marvell Prestera 交換晶片中的 QoS 增強 {#qos-enhancements-in-new-generation-marvell-prestera-switch-chips}

配備新一代 Marvell Prestera 交換晶片的 MikroTik 裝置（例如執行 [switch-marvell 軟體包](../getting-started/installation-and-upgrade/packages.md#extra-packages) 的 CRS8xx 系列）提供了新的 QoS 強制執行方式。此前的型號需要在保證 Tx 佇列緩衝區和共享 Tx 佇列緩衝區之間做出權衡。透過提高共享緩衝區百分比，裝置可以吸收更大的流量突發，但與此同時，一個擁塞埠可能會佔用所有共享緩衝區，從而限制其他埠的 QoS 能力。使用新一代交換晶片可以兼顧兩者優勢，因為它引入了**動態緩衝區**。交換晶片會根據當前擁塞程度動態調整埠和佇列緩衝區限制。如果裝置內部沒有擁塞，單個埠可以吸收大量突發流量，從而防止丟包。當多個埠的 Tx 佇列大小增加時，裝置會降低每埠和每佇列限制，強制公平使用共享資源，同時確保非擁塞佇列有足夠緩衝區繼續轉發流量。整個過程完全自動化，無需使用者配置。

新一代 Marvell Prestera 交換晶片的另一項改進是消除了用於儲存控制資料的入隊封包描述符短缺問題。上一代裝置有 Packet Cap 和 Use 統計。當裝置收到小封包突發時，即使有足夠的佇列緩衝區儲存有效載荷，也可能因為達到 Packet Cap 而開始尾部丟棄封包。新一代裝置確保始終有足夠記憶體儲存控制資料，只受動態緩衝區大小的限制。這就是新一代裝置沒有 Packet Cap/Use 統計的原因。

新一代裝置要求始終啟用 QoS 硬體解除安裝（**qos-hw-offloading=yes**）。RouterOS 會忽略使用者停用它請求，同時保留該欄位以保持向後相容。

## QoS 裝置支援 {#qos-device-support}

<WideTable>

| 交換晶片 | 型號 | QoS 配置檔案 | QoS 對映 | Tx 管理器 | WRED | ECN | PFC | 無損緩衝區 | 動態緩衝區 | 埠/佇列使用統計 |
| :-- | :-- | --: | --: | --: | :-- | :-- | :-- | :-- | :-- | :-- |
| **98DX3236** | CRS305-1G-4S+IN  CRS326-24G-2S+ (RM/IN)  CRS328-24P-4S+RM  CRS328-4C-20S-4S+RM | 128 | 1 | 8 |  |  |  |  |  | 當前值 |
| **98DX226S** | CRS305-1G-4S+OUT (FiberBox Plus)  CRS310-1G-5S-4S+ (netFiber 9/IN)  CRS310-8G+2S+IN  CRS318-16P-2S+OUT (netPower 16P)  CRS320-8P-8B-4S+RM  CRS418-8P-8G-2S+RM  CRS418-8P-8G-2S+5axQ2axQ-RM | 128 | 1 | 8 |  |  |  |  |  | 當前值 |
| **98DX224S** | CRS318-1Fi-15Fr-2S-OUT (netPower 15FR) | 128 | 1 | 8 |  |  |  |  |  | 當前值 |
| **98DX2528** | CRS304-4XG-IN | 128 | 1 | 8 |  |  |  |  |  | 當前值 |
| **98DX8525** | CCR2216-1G-12XS-2XQ  CRS518-16XS-2XQ-RM | 1024 | 12 | 15 | ✔ | ✔ | ✔ | ✔ |  | 最大佔用 <sup>1</sup> |
| **98DX4310** | CRS504-4XQ (IN/OUT)  CRS510-8XS-2XQ-IN  RDS2216-2XG-4S+4XS-2XQ | 1024 | 12 | 15 | ✔ | ✔ | ✔ | ✔ |  | 最大佔用 <sup>1</sup> |
| **98DX8208** | CRS309-1G-8S+IN | 1024 | 12 | 15 | ✔ | ✔ | ✔ | ✔ |  | 當前值 <sup>2</sup> |
| **98DX8212** | CRS312-4C+8XG-RM | 1024 | 12 | 15 | ✔ | ✔ | ✔ | ✔ |  | 當前值 <sup>2</sup> |
| **98DX8216** | CRS317-1G-16S+RM | 1024 | 12 | 15 | ✔ | ✔ | ✔ | ✔ |  | 當前值 <sup>2</sup> |
| **98DX8332** | CRS326-24S+2Q+RM  CRS326-4C+20G+2Q+RM | 1024 | 12 | 15 | ✔ | ✔ | ✔ | ✔ |  | 當前值 <sup>2</sup> |
| **98DX3257** | CRS354-48G-4S+2Q+RM  CRS354-48P-4S+2Q+RM | 1024 | 12 | 15 | ✔ | ✔ | ✔ | ✔ |  | 當前值 <sup>2</sup> |
| **98DX3255** | CCR2116-12G-4S+ | 1024 | 12 | 15 | ✔ | ✔ | ✔ | ✔ |  | 當前值 <sup>2</sup> |
| **98CX8410** | CRS520-4XS-16XQ-RM | 1024 | 12 | 15 | ✔ | ✔ | ✔ | ✔ |  | 不可用 <sup>3</sup> |
| **98DX7335** | CRS812-8DS-2DQ-2DDQ-RM  CRS804-4DDQ-hRM | 1024 | 12 | 15 | ✔ | ✔ | ✔ | ✔ | ✔ | 當前值 + 最大佔用 |

</WideTable>

<sup>**1**</sup> 裝置會收集最大佇列佔用統計資訊，而不是顯示當前使用值。使用 `reset-counters` 命令清除這些統計資訊。  
<sup>**2**</sup> 由於硬體限制，某些交換晶片型號在讀取或輪詢 QoS 埠/佇列使用資料時，可能會出現臨時流量中斷。  
<sup>**3**</sup> 無法獲取埠上各個佇列的使用資料；只能訪問整個物理埠的彙總總使用量。

## 應用與使用示例 {#applications-and-usage-examples}

---

### 基礎配置示例 {#basic-configuration-example}

本示例演示如何在標準 Best Effort 類之上為 VoIP（IP 電話）配置單一 QoS 級別。該配置使用 CRS326-24G-2S+ 裝置，設定如下：

- 所有埠均已橋接並使用 **[vlan-filtering](./index.md#bridge-vlan-filtering)**；
- sfp-sfpplus1 作為 VLAN 中繼連線到另一臺交換器；
- ether1 到 ether9 是 IP 電話專用埠；
- ether10 到 ether24 是用於連線主機的標準埠。

首先，定義 QoS 配置檔案。該配置檔案指定將應用於出站轉發封包的 DSCP 和 PCP 值：

```ros
/interface/ethernet/switch/qos/profile
add dscp=46 name=voip pcp=5 traffic-class=5
```

接下來，將 VoIP QoS 配置檔案分配給 IP 電話專用埠。這會將配置檔案應用於這些埠的入站流量。所有其他乙太網埠將使用預設配置檔案（其中 dscp=0 且 pcp=0）：

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

中繼埠會接收兩種 QoS 流量。為了區分它們，請啟用 trust-l3 和 trust-l2：

```ros
/interface/ethernet/switch/qos/port
set sfp-sfpplus1 trust-l3=trust trust-l2=trust
```

> **注意：** 如果執行的是 RouterOS 7.23 或更高版本，VLAN 優先順序和 IP DSCP 對映會自動建立，因此此步驟不是必需的。如果使用的是較早的 RouterOS 版本，則必須透過 QoS 配置檔案手動建立 VLAN 優先順序和 IP DSCP 對映：

```routeros
/interface/ethernet/switch/qos/map/ip
add dscp=46 profile=voip

/interface/ethernet/switch/qos/map/vlan
add pcp=5 profile=voip
```

最後，啟用 QoS 硬體解除安裝，使上述設定生效：

```ros
/interface/ethernet/switch
set switch1 qos-hw-offloading=yes
```

可以使用 `print` 命令驗證埠 QoS 設定：

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

使用此配置時，埠 ether1 到 ether9 上的入站封包會標記為優先順序程式碼點（PCP）值 5 和差分服務程式碼點（DSCP）值 46。埠 ether10 到 ether24 上的入站封包會標記為 PCP 和 DSCP 值 0。當在 sfp-sfpplus1 埠上收到封包時，任何 PCP 值為 5 的封包會保留其 PCP 值 5 和 DSCP 值 46，而所有其他封包會標記為 PCP 和 DSCP 值 0。

## Dante {#dante}

從 RouterOS v7.15 開始，所有支援 QoS 的 MikroTik 裝置都與 Dante 音訊網路相容。

Dante 硬體使用以下 DSCP/Diffserv 優先順序值進行流量優先順序劃分：

| Dante 優先順序 | 用途 | DSCP 標籤 | DSCP 值 |
| :-- | :-- | :-- | --: |
| High | 時間關鍵的 PTP 事件 | CS7 | 56 |
| Medium | 音訊、PTP | EF | 46 |
| None | 其他流量 | BE | 0 |

本示例假設交換器使用其預設配置，其中包括一個預設橋接介面，所有乙太網介面都已作為橋接埠加入。這些介面中的任何一個都可以用於 Dante。

首先，建立 QoS 配置檔案以匹配 Dante 流量類別。已經存在一個預先存在的“default”配置檔案，它對應 Dante 的 None 優先順序。

```ros
/interface/ethernet/switch/qos/profile
add name=dante-ptp dscp=56 pcp=7 traffic-class=7
add name=dante-audio dscp=46 pcp=5 traffic-class=5
```

如果執行的是 RouterOS 7.23 或更高版本，IP DSCP 對映會自動建立，因此此步驟不是必需的。如果使用的是較早的 RouterOS 版本，請建立基於 DSCP 值匹配 QoS 配置檔案的 QoS 對映：

```ros
/interface/ethernet/switch/qos/map/ip
add dscp=56 profile=dante-ptp
add dscp=46 profile=dante-audio
```

配置硬體佇列以對 Dante 流量強制執行 QoS：

```ros
/interface/ethernet/switch/qos/tx-manager/queue
set [find where traffic-class=7] schedule=strict-priority
set [find where traffic-class=5] schedule=strict-priority
```

Dante 的 High 和 Medium 優先順序流量按嚴格優先順序順序排程。裝置會持續傳送時間關鍵的 PTP 封包，直到 queue7 為空，然後繼續傳送音訊（queue5）。只有在 PTP 和音訊佇列為空時，才會傳送其他流量。

下一步是為入站三層封包啟用信任模式（IP DSCP 欄位）：

```ros
/interface/ethernet/switch/qos/port
set [find] trust-l3=keep
```

最後，啟用 QoS 硬體解除安裝，使上述設定生效：

```ros
/interface/ethernet/switch
set switch1 qos-hw-offloading=yes
```

在以組播模式使用 Dante 時，建議在交換器上啟用 IGMP snooping。此功能只會將流量定向到已訂閱裝置的埠，從而防止不必要的泛洪。此外，啟用 IGMP querier（如果同一 LAN 中的另一臺裝置尚未啟用）、調整查詢間隔並激活 fast-leave，可以進一步最佳化組播效能。

```ros
/interface/bridge
set [find name=bridge] igmp-snooping=yes multicast-querier=yes query-interval=60s

/interface/bridge/port
set [find] fast-leave=yes
```

## 融合乙太網上的 RDMA（RoCE） {#rdma-over-converged-ethernet-roce}

RoCE 支援透過乙太網網路直接記憶體訪問遠端儲存系統，而無需主機 CPU 參與。這顯著降低了延遲和 CPU 開銷，使 RoCE 非常適合高效能計算和資料中心環境。RoCE 還支援融合網路，其中各種服務（如資料儲存、網路和多媒體）在單一乙太網基礎設施上執行，從而簡化網路管理，並降低維護獨立網路的成本和複雜性。

RoCE 透過使用 **ECN** 和 **PFC** 機制來實現這一點。這些功能有助於防止網路擁塞和丟包，確保可靠、無損的通訊。有關相容交換器，請參閱[裝置功能表](./quality-of-service.md#qos-device-support)。雖然交換器可以支援 RoCE 環境，但終端主機也必須相容 RoCE 協定，並配備支援 RDMA 的網路介面卡（NIC）。

RoCE 有兩個主要版本。RoCEv1 作為乙太網鏈路層協定執行，並使用 Ethertype 0x8915。RoCEv2 在標準 IP 網路上執行，使用 UDP 目標埠號 4791。IP 報頭中的 ECN 位會被標記以表示網路擁塞，並使用擁塞通知封包（CNP）向傳送方確認擁塞。對於流量優先順序劃分，RoCEv2 流量使用 DSCP 26，而 CNP 使用 DSCP 48。

以下示例可用於帶有 PFC 和 ECN 的無損 RoCEv2，並假設交換器使用其預設配置，其中包括一個預設橋接介面，所有乙太網介面都已作為橋接埠加入。建議的最低 RouterOS 版本為 7.17。

首先，配置附加配置檔案。非 RoCE 流量將分配到已存在的“default”配置檔案，其 traffic-class 為 1；RoCEv2 分配到 traffic-class 3；CNP 分配到 traffic-class 6。

```routeros
/interface/ethernet/switch/qos/profile
add dscp=26 name=roce traffic-class=3
add dscp=48 name=cnp traffic-class=6
```

如果執行的是 RouterOS 7.23 或更高版本，IP DSCP 對映會自動建立，因此此步驟不是必需的。如果使用的是較早的 RouterOS 版本，請建立基於 DSCP 值匹配 QoS 配置檔案的 QoS 對映。

```routeros
/interface/ethernet/switch/qos/map/ip
add dscp=26 profile=roce
add dscp=48 profile=cnp
```

配置硬體佇列和排程器。對 traffic-class 1 和 traffic-class 3 使用 ETS（`schedule=high-priority-group`），各分配 50% 頻寬（`weight=1`），並對 traffic-class 6 使用嚴格優先順序排程。此外，為 traffic-class 3 啟用 ECN（`ecn=yes`），以在交換器中標記經歷擁塞的 IP 封包。

```routeros
/interface/ethernet/switch/qos/tx-manager/queue
set 1 schedule=high-priority-group weight=1
set 3 schedule=high-priority-group weight=1 ecn=yes
set 6 schedule=strict-priority
```

:::tip
儘管使用 `schedule=low-priority-group` 可以為另一組流量類別建立單獨的 ETS 排程和頻寬分配，但不建議將此設定與 `lldp-dcbx=yes` 一起使用。原因是 ETS Configuration/Recommendation TLV 設計為跨流量類別處理單一頻寬分配，因此應改用 `schedule=high-priority-group`。
:::

為 traffic-class 3 配置 PFC 配置檔案，以確保 RoCEv2 流量處於無損環境。

```routeros
/interface/ethernet/switch/qos/priority-flow-control
add name=pfc-tc3 rx=yes traffic-class=3 tx=yes
```

在預期會有 RoCEv2 流量的交換器埠上設定三層信任模式（`trust-l3=keep`）。設定 PFC（`pfc=pfc-tc3`）以及 queue3 的出站速率，以滿足 PFC 要求（`egress-rate-queue3=10.0Gbps`）。在本示例中，使用的是 10Gbps SFP+ 介面，出站速率可以設定為與介面物理速率匹配。請根據介面速率更改此屬性。

```routeros
/interface/ethernet/switch/qos/port
set sfp-sfpplus1 egress-rate-queue3=10.0Gbps pfc=pfc-tc3 trust-l3=keep
set sfp-sfpplus2 egress-rate-queue3=10.0Gbps pfc=pfc-tc3 trust-l3=keep
set sfp-sfpplus3 egress-rate-queue3=10.0Gbps pfc=pfc-tc3 trust-l3=keep
set sfp-sfpplus4 egress-rate-queue3=10.0Gbps pfc=pfc-tc3 trust-l3=keep
```

啟用 QoS 硬體解除安裝，使上述設定開始生效。

```routeros
/interface/ethernet/switch
set switch1 qos-hw-offloading=yes
```

啟用 LLDP 資料中心橋接能力交換協定（DCBX），以與其他相鄰裝置共享 QoS 設定和能力。

```routeros
/ip/neighbor/discovery-settings
set lldp-dcbx=yes
```

作為可選步驟，增加 L2MTU 以容納更大的封包。

```routeros
/interface/ethernet
set [find switch=switch1] l2mtu=9500
```

## QoS 標記 {#qos-marking}

---

### 理解對映範圍 {#understanding-map-ranges}

為了避免逐個定義所有可能的 PCP 和 DSCP 對映，RouterOS 允許在建立 QoS 配置檔案對映時為 PCP 和 DSCP 指定多個值或範圍。

在此示例中，PCP 值 0 和 2 使用預設 QoS 配置檔案，值 1 和 3-4 使用 streaming 配置檔案，值 5 使用 voip 配置檔案，值 6-7 使用 control 配置檔案：

```ros
/interface/ethernet/switch/qos/map/vlan
add pcp=1,3-4 profile=streaming
add pcp=5 profile=voip
add pcp=6-7 profile=control
```

這種方法透過將相關優先順序值分組在一起，而不是為每個單獨值建立單獨的對映規則，從而簡化了配置。

### 理解埠、配置檔案與對映的關係 {#understanding-port-profile-and-map-relation}

每個交換器埠都有二層和三層信任設定，這些設定會改變入站封包如何分類到 QoS 配置檔案，以及將使用哪些 PCP 和 DSCP 值。下表描述了所有可能的選項：

| **qos-trust-l2** | **qos-trust-l3** | 行為 |
| :-- | :-- | :-- |
| **ignore** | **ignore** | 該埠被視為不受信任。兩個報頭都會被忽略，並且埠的 **profile** 會強制應用於所有入站封包。這是預設設定。 |
| **ignore** | **trust** | 信任三層報頭。使用入站封包 IP 報頭中的 DSCP 欄位進行 QoS 配置檔案查詢（參見 `/in/eth/sw/qos/map/ip`）。如果查詢失敗（沒有 QoS 配置檔案對映到給定 DSCP 值），則使用 **default** QoS 配置檔案（不是交換器埠的 QoS 配置檔案）。交換器埠的 **profile** 欄位僅用於非 IP 流量。 |
| **ignore** | **keep** | 信任三層報頭。使用入站封包 IP 報頭中的 DSCP 欄位進行 QoS 配置檔案查詢（參見 `/in/eth/sw/qos/map/ip`）。如果查詢失敗，則使用 **default** QoS 配置檔案。交換器埠的 **profile** 欄位僅用於非 IP 流量。如果轉發/路由的封包帶有 VLAN 標籤，其 PCP 值會根據所選 QoS 配置檔案設定。但是，封包的原始 DSCP 值保持不變。 |
| **trust** | **ignore** | 信任二層報頭，但忽略三層。如果入站封包帶有 VLAN 標籤，則使用 VLAN 報頭中的 PCP 欄位進行 QoS 配置檔案查詢（參見 `/in/eth/sw/qos/map/vlan`）。如果查詢失敗（沒有 QoS 配置檔案對映到給定 PCP 值），則使用 **default** QoS 配置檔案。交換器埠的 **profile** 欄位僅用於未打標籤的流量。 |
| **trust** | **trust** | 信任兩個報頭，但三層具有更高優先順序。對於 IP 封包，使用 DSCP 欄位進行 QoS 配置檔案查詢（參見 `/in/eth/sw/qos/map/ip`）。如果 DSCP 到 QoS 的查詢失敗，則使用 **default** 配置檔案。如果封包不是 IP 封包但帶有 VLAN 標籤，則使用 VLAN 報頭中的 PCP 欄位進行 QoS 配置檔案查詢（參見 `/in/eth/sw/qos/map/vlan`）。如果 VLAN 到 QoS 的查詢失敗，則使用 **default** QoS 配置檔案。非 IP 且未打標籤的封包使用交換器埠的 **profile**。 |
| **trust** | **keep** | 與 **trust+trust** 相同，但在轉發/路由的封包中保留原始 DSCP 值。 |
| **keep** | **ignore** | 信任二層報頭，但忽略三層。如果入站封包帶有 VLAN 標籤，則使用 VLAN 報頭中的 PCP 欄位進行 QoS 配置檔案查詢（參見 `/in/eth/sw/qos/map/vlan`）。如果查詢失敗（沒有 QoS 配置檔案對映到給定 PCP 值），則使用 **default** QoS 配置檔案。交換器埠的 **profile** 欄位僅用於未打標籤的流量。如果封包在入站和出站時都帶有 VLAN 標籤，則保留原始 PCP 值。 |
| **keep** | **trust** | 信任兩個報頭，但三層具有更高優先順序。對於 IP 封包，使用 DSCP 欄位進行 QoS 配置檔案查詢（參見 `/in/eth/sw/qos/map/ip`）。如果 DSCP 到 QoS 的查詢失敗，則使用 **default** 配置檔案。如果封包不是 IP 封包但帶有 VLAN 標籤，則使用 VLAN 報頭中的 PCP 欄位進行 QoS 配置檔案查詢（參見 `/in/eth/sw/qos/map/vlan`）。如果 VLAN 到 QoS 的查詢失敗，則使用 **default** QoS 配置檔案。非 IP 且未打標籤的封包使用交換器埠的 **profile**。如果封包在入站和出站時都帶有 VLAN 標籤，則保留原始 PCP 值。轉發/路由的封包中的 DSCP 值會根據所選 QoS 配置檔案設定。 |
| **keep** | **keep** | 信任兩個報頭，但三層具有更高優先順序。對於 IP 封包，使用 DSCP 欄位進行 QoS 配置檔案查詢（參見 `/in/eth/sw/qos/map/ip`）。如果 DSCP 到 QoS 的查詢失敗，則使用 **default** 配置檔案。如果封包不是 IP 封包但帶有 VLAN 標籤，則使用 VLAN 報頭中的 PCP 欄位進行 QoS 配置檔案查詢（參見 `/in/eth/sw/qos/map/vlan`）。如果 VLAN 到 QoS 的查詢失敗，則使用 **default** QoS 配置檔案。非 IP 且未打標籤的封包使用交換器埠的 **profile**。對於帶 VLAN 標籤和/或 IP 封包，分別保留原始 PCP 和/或 DSCP 值。 |

<WideTable>

| **埠設定** |  | 所選 QoS 配置檔案以及轉發/路由封包中 PCP / DSCP 欄位值的來源 |  |  |  |  |  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| **qos-trust-l2** | **qos-trust-l3** | 帶 VLAN 標籤的 IP |  |  | 未打標籤的 IP |  |  | 帶 VLAN 標籤的非 IP |  |  | 未打標籤的非 IP |  |  |
|  |  | QoS 配置檔案 | PCP | DSCP | QoS 配置檔案 | PCP <sup>1</sup> | DSCP | QoS 配置檔案 | PCP | DSCP | QoS 配置檔案 | PCP <sup>1</sup> | DSCP |
| ignore | ignore | profile | profile | profile | profile | profile | profile | profile | profile | - | profile | profile | - |
| ignore | trust | map/ip | map/ip | map/ip | map/ip | map/ip | map/ip | profile | profile | - | profile | profile | - |
| ignore | keep | `/map/ip` | `/map/ip` | 原始值 | `/map/ip` | `/map/ip` | 原始值 | profile | profile | - | profile | profile | - |
| trust | ignore | map/vlan | map/vlan | map/vlan | profile | profile | profile | map/vlan | map/vlan | - | profile | profile | - |
| trust | trust | `/map/ip` | `/map/ip` | `/map/ip` | `/map/ip` | `/map/ip` | `/map/ip` | `/map/vlan` | `/map/vlan` | - | profile | profile | - |
| trust | keep | `/map/ip` | `/map/ip` | 原始值 | `/map/ip` | `/map/ip` | 原始值 | `/map/vlan` | `/map/vlan` | - | profile | profile | - |
| keep | ignore | map/vlan | 原始值 | map/vlan | profile | profile | profile | map/vlan | 原始值 | - | profile | profile | - |
| keep | trust | map/ip | 原始值 | map/ip | map/ip | profile | map/ip | map/vlan | 原始值 | - | profile | profile | - |
| keep | keep | map/ip | 原始值 | 原始值 | map/ip | profile | 原始值 | map/vlan | 原始值 | - | profile | profile | - |

</WideTable>

<sup>**1**</sup> 僅在入站流量未打標籤，但出站介面要求幀帶 VLAN 標籤時適用。

### 透過交換器規則（ACL）進行 QoS 標記 {#qos-marking-via-switch-rules-acl}

從 **RouterOS v7.15** 開始，可以使用交換器規則（ACL）為網路流量分配 QoS 配置檔案。此方法允許根據各種封包屬性靈活地對流量進行分類。

以下示例根據源 MAC 地址分配 QoS 配置檔案：

```ros
/interface/ethernet/switch/rule
add new-qos-profile=stream port=ether1,ether2 src-mac-address=00:01:02:00:00:00/FF:FF:FF:00:00:00 switch=switch1
add new-qos-profile=voip port=ether1,ether2 src-mac-address=04:05:06:00:00:00/FF:FF:FF:00:00:00 switch=switch1
```

## QoS 強制執行 {#qos-enforcement}

### 硬體佇列 {#hardware-queues}

每個交換器埠都有八個硬體傳輸（Tx）佇列（queue0 到 queue7）。每個佇列對應一個由 [QoS 配置檔案](../cli-reference/interface/ethernet/switch/qos/profile.md) 定義的流量類別（tc0 到 tc7）。當封包進入交換器時，會獲得一個 QoS 配置檔案分配，這決定了流量類別，並因此選擇適當的出站佇列進行傳輸。

硬體佇列具有由 [傳輸管理器](../cli-reference/interface/ethernet/switch/qos/tx-manager/index.md) 配置的可變大小。此外，多個埠和佇列可以透過稱為*共享緩衝區*的機制相互共享資源。例如，一臺有 25 個埠的裝置，其緩衝區記憶體足以排隊 1200 個數據包。如果資源平均分配，每個埠獲得 48 個獨佔緩衝區，每佇列最多 6 個數據包（48 除以 8），這通常不足以吸收甚至很短的流量突發。但是，如果分配 50% 的緩衝區用於共享，則每個埠保留 24 個獨佔緩衝區（每佇列 3 個），同時允許單個佇列增長到 603 個緩衝區（3 個獨佔加 600 個共享）。

RouterOS 允許為每個佇列單獨啟用或停用共享池。此功能有助於防止低優先順序流量消耗所有可用硬體記憶體。此外，埠緩衝區限制可以限制單個低速埠占用整個共享池。更多詳細資訊，請參閱 [QoS 設定](../cli-reference/interface/ethernet/switch/qos/settings.md) 和 [傳輸管理器](../cli-reference/interface/ethernet/switch/qos/tx-manager/index.md)。

:::info
預設的 best-effort 流量類別（PCP=0，DSCP=0）是流量類別 1，而最低優先順序流量（PCP=1）使用流量類別 0。
:::

## 硬體資源 {#hardware-resources}

交換晶片的硬體資源（記憶體）有限。與 QoS 操作相關的兩個主要硬體資源是：

- **封包描述符** - 包含封包控制資訊，例如目標埠、報頭修改和其他元資料。
- **資料緩衝區** - 儲存實際封包有效載荷的記憶體塊。緩衝區大小因交換晶片型號而異；通常為 256 位元組。

一個數據包描述符可能使用多個緩衝區（取決於有效載荷大小），並且在組播或廣播流量情況下，緩衝區可能由多個描述符共享。如果硬體沒有足夠的空閒描述符或緩衝區，封包會被丟棄（尾部丟棄）。

硬體資源可以按目的地型別（組播/單播）、按埠和按 TX 佇列進行限制。當達到任何這些限制時，無法再將要傳輸的封包入隊，後續封包會被丟棄。

RouterOS 抽象了底層硬體細節，允許以封包數量或總量百分比的形式配置資源限制。RouterOS 會根據使用者指定的封包限制和埠 MTU 自動計算所需的硬體描述符和緩衝區數量。此外，RouterOS 包含預配置的硬體資源，在常見 QoS 場景中無需手動配置。

:::danger
在執行時修改任何硬體資源分配引數會導致裝置臨時停止，在此期間無法將封包入隊或傳輸。裝置轉發流量時預計會出現臨時丟包。
:::

## 節省資源（上一代裝置） {#resource-saving-previous-generation-devices}

:::info
本節僅適用於**不**支援**動態緩衝區**的裝置。
:::

由於硬體資源無法在執行時重新分配，RouterOS 無法自動釋放為未活動埠預留的佇列緩衝區。這些緩衝區會保持未使用狀態。但是，如果您知道某個特定埠永遠不會使用（例如，它始終保持物理斷開），則可以透過分配具有最小資源的內建“offline”tx-manager 來手動釋放相應佇列資源：

```ros
/interface/ethernet/switch/qos/port
set sfp-sfpplus1 tx-manager=offline
set sfp-sfpplus2 tx-manager=offline
```

:::danger
不要在 **switch-cpu** 埠上配置“offline”tx-manager。
:::
:::warning
為 QSFP+ 或 QSFP28 介面配置 `tx-manager` 設定時，必須對該埠的所有四個子介面應用相同的配置。例如，如果介面 qsfp28-1-1 處於活動狀態並以 100Gbps 連線，而子介面（qsfp28-1-2、qsfp28-1-3、qsfp28-1-4）顯示非執行標誌，**不要將“offline”tx-manager 分配給這些非執行的子介面**。這樣做也會影響 100Gbps 鏈路。但是，如果四個子介面都未執行，則可以安全地分配“offline”tx-manager 設定。
:::

## 流量優先順序劃分 {#traffic-prioritization}

硬體支援兩種流量傳輸優先順序劃分方式：

- **嚴格優先順序** - 來自較高佇列的流量始終優先傳輸。
- **增強傳輸選擇（ETS）** - 多個佇列同時使用加權輪詢參與封包傳輸排程。

**嚴格優先順序**排隊很簡單。如果最高優先順序佇列（Q7）有封包，則這些封包會優先傳輸。當 Q7 為空時，來自 Q6 的封包會被傳輸，依此類推。只有當所有其他佇列都為空時，才會傳輸最低優先順序佇列（Q0）中的封包。

嚴格優先順序劃分的缺點是，在“過度優先”高優先順序佇列的同時，會增加低優先順序佇列的延遲。假設 TC5 的可接受延遲為 20ms，TC3 為 50ms。由於佇列的嚴格優先順序，出現在 Q5 中的流量會立即傳輸，從而給低優先順序佇列（Q4..Q0）中的每個封包增加額外延遲。Q5 中的封包突發（例如語音通話開始）可能會暫時“癱瘓”Q3，使 TC3 延遲增加到超過可接受的 50ms（甚至由於佇列滿而導致丟包），而 TC5 封包則以 &lt;1ms 傳輸（遠低於 20ms 限制）。如果透過在中間傳輸 TC3 封包來稍微犧牲 TC5 的延遲，就能讓所有流量都滿意。這正是 **ETS** 的用途。

**增強傳輸選擇（ETS）** 以加權輪詢方式排程來自多個佇列（組成員）的流量進行傳輸。佇列的權重設定每輪從該佇列傳輸的封包數量。例如，如果 Q2、Q1 和 Q0 是組成員，其權重分別為 3、2 和 1，則排程器會從 Q2 傳輸 3 個數據包，從 Q1 傳輸 2 個，從 Q0 傳輸 1 個。上述示例每輪的實際傳輸順序是“Q2、Q1、Q0、Q2、Q1、Q2”——以實現更公平的排程。

有兩個硬體組：`low-priority-group` 和 `high-priority-group`。兩個組之間存在嚴格優先順序順序：只有當高優先順序組中的*所有*佇列都為空時，低優先順序組才會傳輸。但是，也可以所有佇列只使用一個組。

下面列出了預設（內建）RouterOS 佇列設定。Q3-Q5 在高優先順序組內共享頻寬，當 Q6 和 Q7 為空時傳輸封包。Q0-Q2 是低優先順序組的成員，當 Q3-Q7 為空時傳輸封包。

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
建議所有組成員彼此相鄰。
:::

## 主動佇列管理（AQM） {#active-queue-management-aqm}

### 加權隨機早期檢測（WRED） {#weighted-random-early-detection-wred}

WRED 是一種基於每佇列執行的擁塞控制機制。它透過在佇列溢位前丟棄封包，向端點裝置發出擁塞事件訊號。WRED 依賴於端點中對丟包做出響應的速率限制機制，例如 TCP/IP。

WRED 使用隨機丟包演算法來預測擁塞事件，並在擁塞實際發生前透過限制流量速率來響應。WRED 的隨機性可防止 TCP 流全域性同步導致吞吐量崩潰。

可以在每個 Tx 管理器中按佇列啟用或停用 WRED。對於無損流量類別，請停用 WRED。對於高速埠，也沒有理由啟用 WRED，因為這些埠本來就不應該發生擁塞。

該行為透過 WRED 閾值控制。WRED 閾值定義可以超過佇列共享緩衝區限制（上限）的最大封包數或位元組數。當佇列使用量超過其相應容量時，開始隨機丟包：

- `queueX-packet-use > queueX-shared-packet-cap`，或
- `queueX-byte-use > queueX-shared-byte-cap`。

使用量超過容量越多，丟包機率越高，並在 `queueX-shared-packet-cap + wred-packet-threshold`（或等效位元組數）時達到 100%。

RouterOS 會根據佇列或共享池容量自動選擇實際 WRED 閾值。使用者可以透過 QoS 設定調整閾值。

:::danger
WRED 要求相應的 Tx 佇列使用共享緩衝區（**use-shared-buffers=yes**）。
:::

選擇 WRED 閾值需要在擁塞預測和突發吸收之間進行權衡。設定較高的 WRED 閾值可能會導致更早地限制流量速率，從而解決擁塞。但是，高閾值會導致有限的流量突發中發生丟包，而這些突發原本可以由佇列緩衝區吸收並無損傳輸（如果 WRED 未啟用）。

例如，發起遠端資料庫連線通常在初始化階段以較重流量（“封包突發”）開始，然後流量速率降至“合理”水平。初始化階段的任何丟包都會因需要重傳而導致資料庫連線變慢。因此，建議對此類流量降低 WRED 閾值或完全停用 WRED。相反的情況是影片流，早期擁塞檢測有助於選擇合適的流速率，而不會因重傳損失過多頻寬或犧牲質量級別。

:::info
使用交換器規則（ACL）或其他 QoS 標記技術來區分流量，並將封包放入具有所需 WRED 設定的佇列中。
:::

以下指令碼透過將 TCP/IP 流量重定向到 queue2，僅對其應用 WRED。UDP 和其他封包保留在 queue1 中，因為它們的端點通常無法對早期丟棄做出響應。Queue1 和 queue2 以同等方式排程，不會優先於另一個佇列：

```ros
/interface/ethernet/switch/qos/profile
add name=tcp-wred traffic-class=2 pcp=0 dscp=0

# 将 TCP 流量移到 queue2
/interface/ethernet/switch/rule
add new-qos-profile=tcp-wred ports=ether1,ether2,ether3,ether4 protocol=tcp switch=switch1

# 在 queue1 和 queue2 之间设置相同的调度优先级（权重）
# 仅对 queue2 - TCP 流量应用 WRED
/interface/ethernet/switch/qos/tx-manager/queue/
set [find where traffic-class=1] weight=2 schedule=low-priority-group use-shared-buffers=yes wred=no
set [find where traffic-class=2] weight=2 schedule=low-priority-group use-shared-buffers=yes wred=yes
```

## 顯式擁塞通知（ECN） {#explicit-congestion-notification-ecn}

某些交換晶片型號支援符合 RFC 3168 的硬體級 IP 封包 ECN 標記。此機制的執行方式與 WRED 類似，但在擁塞期間不是丟棄封包，而是在 ECN 欄位中將其標記為 CE（擁塞經歷，二進位制 11）標誌。只有支援 ECN 的 IP 封包才能收到此標記——即 ECN 欄位值設定為 ECT(1) 或 ECT(0)（二進位制 01 或 10）的封包。不支援 ECN 的傳輸封包（ECN=00）永遠不會被標記。如果封包已經帶有 CE 標記（ECN=11），則無論裝置是否經歷擁塞，它都會保留此標記。

透過在所需的 [Tx 管理器佇列](../cli-reference/interface/ethernet/switch/qos/tx-manager/index.md) 上設定 **ecn=yes** 來啟用 ECN 標記。

:::danger
ECN 標記機制要求相應的 Tx 佇列使用共享緩衝區（**use-shared-buffers=yes**）。
:::

當**所有**以下條件滿足時，封包會收到 CE 標記：

1. 封包是 IPv4 或 IPv6。
2. IP 報頭中的 ECN 欄位值為 ECT(1) 或 ECT(0)。
3. 出站埠的 Tx 佇列啟用了 **ecn=yes** 並使用共享緩衝區（**use-shared-buffers=yes**）。
4. 佇列使用量超過共享緩衝區容量：`queueX-packet-use > queueX-shared-packet-cap` 或 `queueX-byte-use > queueX-shared-byte-cap`。

:::danger
由於啟用 ECN（ecn=yes）會阻止丟棄支援 ECN 的封包，如果流量傳送方沒有及時響應擁塞通知，佇列使用量可能會超過 WRED 閾值。
:::

## 基於優先順序的流量控制（PFC） {#priority-based-flow-control-pfc}

基於優先順序的流量控制（PFC）可為最多八個流量類別實現無損執行，確保一個流量類別中的擁塞不會暫停其他類別中的流量。這允許對丟包敏感和可容忍丟包的流量型別在同一網路中共存。

支援 PFC 的交換晶片符合 IEEE 802.1Qbb PFC 標準，這意味著它們可以生成並響應 PFC 幀。當出站埠發生擁塞時，源埠會為受影響的流量類別傳送 PFC 幀。生成的 PFC 幀使用計時器值 0xFFFF 表示暫停（XOFF），0x0 表示恢復（XON），並在優先順序啟用向量中設定相應位。在接收端，PFC 幀會在 PFC 幀指定的持續時間內暫停目標埠上的特定優先順序佇列。

在 RouterOS 中，PFC 配置按配置檔案組織。每個埠可以分配到一個特定的 PFC 配置檔案，該配置檔案定義了要啟用 PFC 的流量類別、傳送 XOFF 和 XON 幀的暫停和恢復閾值，以及分配的埠應傳送和/或接收 PFC 幀。

當出站埠發生擁塞時，會在入站埠上觸發 PFC。必須使用共享緩衝區，才能將入站流量數量與 Tx 佇列中等待的封包關聯起來。對於每個啟用 PFC 的流量類別，請在相應的 Tx 佇列上設定 **use-shared-buffers=yes**。

:::info
RouterOS 實現流量類別與 Tx 佇列之間 1:1 的對映。流量類別為 0 的封包進入 queue0，TC1 進入 queue1，依此類推，直到 TC7 進入 queue7。因此，在本文件中，“流量類別”和“Tx 佇列”這兩個術語可以互換使用。
:::

選擇暫停和恢復閾值時，請考慮傳輸和處理 PFC 幀的延遲。例如，裝置 A 在時間 T 經歷擁塞，向裝置 B 傳送 PFC 暫停幀，B 處理該幀並在時間 T+D 停止傳輸。在增量時間 D 內，裝置 B 會繼續傳送流量。如果裝置 A 將暫停閾值配置為 100%，則它沒有空閒緩衝區可用，封包可能會被丟棄，這對於無損流量類別是不可接受的。設定較低的暫停閾值（例如 80%），可在仍有空閒記憶體吸收增量時間 D 內流量的情況下發送 PFC 暫停幀。同樣的原則適用於恢復閾值。將其設定為 0% 會使裝置在增量時間內保持空閒，從而降低整體吞吐量。

PFC 接收要求為所有相關佇列設定出站速率，以計算暫停時間，即使它與線速匹配。例如，如果 PFC 執行在流量類別 3 上，則分配的埠需要設定 `egress-rate-queue3`。

```routeros
/interface/ethernet/switch/qos/priority-flow-control/add name=pfctc3 traffic-class=3 rx=yes
/interface/ethernet/switch/qos/port/set sfp-sfpplus1,sfp-sfpplus2 pfc=pfctc3 egress-rate-queue3=10G
```
