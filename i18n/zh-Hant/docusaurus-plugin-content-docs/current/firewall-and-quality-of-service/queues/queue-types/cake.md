---
sidebar_key: "firewall-and-quality-of-service/queues/queue-types/cake"
sidebar_position: 1
title: "CAKE"
sidebar_label: "CAKE"
description: "CAKE（Common Applications Kept Enhanced）是 RouterOS 的一種高階佇列管理演算法，它透過頻寬整形、流隔離和基於 RTT 的擁塞控制來最佳化網路流量處理。它支援 Diffserv 優先順序、ACK 過濾、NAT 處理，以及針對不同鏈路技術的多種開銷補償方案。"
tags:
  - 'cake'
  - 'diffserv'
  - 'flow-isolation'
source: https://manual.mikrotik.com/docs/firewall-and-quality-of-service/queues/queue-types/cake
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

CAKE（Common Applications Kept Enhanced）是一種具備整形能力的佇列規則，它結合了 COBALT 主動佇列管理、deficit 模式整形器、DRR++ 流隔離、簡化的 DiffServ 處理以及鏈路層開銷補償。

CAKE 旨在透過實用的預設值和極少的調優來保持公平性並將緩衝膨脹降到最低。

## 何時使用 CAKE {#when-to-use-cake}

在共享瓶頸上，當大流量傳輸會增加延遲，或某臺主機可能獨佔可用容量時，請使用 CAKE。典型示例包括由多個用戶端共享的網際網路連線、較慢的上行鏈路或非對稱連線。

CAKE 可以：

- 在鏈路繁忙時保持低延遲。
- 在主機之間以及它們各自的連線之間共享容量。
- 針對鏈路層開銷進行整形。
- 應用簡單的 DiffServ 策略。
- 在高度非對稱鏈路上過濾冗餘的 TCP 確認。

CAKE 只能控制經過其佇列的流量。它無法糾正 Wi-Fi 干擾、路由器 CPU 不足或網路中其他位置的佇列，除非其整形器配置為低於該瓶頸的速率。

當你需要每流公平性和主動佇列管理且希望 CPU 佔用更低時，請使用 FQ-CoDel。當你還需要每主機公平性、帶鏈路層補償的整合整形器、DiffServ 處理或 ACK 過濾時，請使用 CAKE。

## 基本配置 {#basic-configuration}

CAKE 是一種佇列型別，而不是完整的流量匹配規則。在 `/queue/type` 下建立 CAKE 條目會定義一個可複用的佇列配置檔案，但它本身不處理任何流量。請將該配置檔案分配給 Simple Queue、Queue Tree 或 Interface Queue。有關完整的屬性列表和可接受值，請參閱生成的 [`/queue/type` CLI 參考](../../../cli-reference/queue/type.md)。

以下示例將相同的 CAKE 配置檔案應用於 Simple Queue 的兩個方向。HTB 提供上傳和下載限制，因此 CAKE 的內部整形器保持不限速：

```ros
/queue/type
add name=cake-default kind=cake cake-bandwidth=0 cake-nat=yes

/queue/simple
add name=internet-cake target=192.168.88.0/24 max-limit=20M/100M queue=cake-default/cake-default
```

在 `max-limit=20M/100M` 和 `queue=cake-default/cake-default` 中，第一個值是上傳，第二個是下載。請將 target 和速率替換為適合該網路的值。被 FastTrack 處理的流量會繞過此 Simple Queue，因此對於該佇列必須處理的流量，請停用 FastTrack。

:::note
僅在 `kind=cake` 的佇列型別上設定 `cake-bandwidth`。它控制 CAKE qdisc 內建的整形器。

Simple Queue 和 Queue Tree 條目使用 HTB。它們的 `limit-at` (CIR) 和 `max-limit` (MIR) 引數在 HTB 層面控制速率。當你將 CAKE 佇列型別分配給這些條目之一時，CAKE 作為 HTB 下的葉子 qdisc 執行。

當 HTB 應控制流量速率時，保留 `cake-bandwidth=0`。此值使 CAKE 的整形器不受限制，但 CAKE 繼續提供主動佇列管理、流隔離和 DiffServ 處理。當 CAKE 也應進行流量整形時，設定 `cake-bandwidth`。如果同時配置 `cake-bandwidth` 和 HTB 速率限制，流量將透過兩個整形器。
:::

## 推薦的起始配置 {#recommended-starting-points}

| 使用場景 | 推薦的起始配置 |
| :-- | :-- |
| 由 Simple Queue 或 Queue Tree 提供速率限制 | 保持 `cake-bandwidth=0` 並設定 HTB 的 `max-limit`。CAKE 提供主動佇列管理和公平性，而不會增加第二個整形器。 |
| 由 CAKE 提供速率限制 | 將 `cake-bandwidth` 設定為低於真實瓶頸速率，並配置正確的鏈路層開銷。除非兩個整形層都是有意為之，否則應避免再設定 HTB 速率限制。 |
| 路由器執行 NAT | 設定 `cake-nat=yes` 並保留預設的 `triple-isolate` 流模式。這樣單個 CAKE 例項就能在內部主機之間以及它們的流之間平衡流量。 |
| 下載/上傳比率大於約 10:1 | 僅在較慢方向上的傳送佇列設定 `cake-ack-filter=filter`。 |
| 不信任入口 DSCP 標記 | 設定 `cake-diffserv=besteffort` 以忽略它們，或設定 `cake-wash=yes` 以便在 CAKE 應用其優先順序決策後清除它們。 |

### 方向與佇列位置 {#direction-and-queue-placement}

CAKE 例項只處理經過其掛接佇列的封包。它不會自動處理反方向的流量。

- **Interface Queue：** 介面佇列處理由該介面傳送的封包。對於轉發的用戶端流量，面向 WAN 的傳送介面上的 CAKE 處理上傳，而面向 LAN 的傳送介面上的 CAKE 處理下載。這是兩個獨立的 CAKE 例項。介面佇列不處理該介面接收的封包。
- **Simple Queue：** RouterOS 相對於配置的 target 確定上傳和下載。`queue` 屬性按該順序選擇上傳和下載佇列型別。將 CAKE 佇列型別分配到這兩個位置即可處理兩個方向。
- **Queue Tree：** 每個 Queue Tree 都是單向的。其父級和封包選擇決定了哪些流量經過它的 CAKE 葉子佇列。

當上傳和下載速率或選項不同時，請為每個方向配置單獨的 CAKE 佇列型別。如果 LAN 使用多個出介面，僅掛接到其中一個介面的 Interface Queue 不會處理其他介面傳送的流量。單個 CAKE 例項可以在經過它的許多主機和流之間實現平衡。僅當你需要明確的每用戶端速率限制或 HTB 保證時，才建立單獨的每用戶端佇列。

`cake-autorate-ingress` 名稱指的是 CAKE 的容量估算模式。它不會讓 Interface Queue 處理介面接收的封包，也不會建立反方向佇列。將 WAN 入口重定向到 Intermediate Functional Block（IFB）的 Linux 示例會建立單獨的傳送排隊點；它們不是 RouterOS Interface Queue 的配置說明。

### 選擇整形速率 {#select-the-shaping-rate}

整形器必須成為瓶頸，才能控制佇列延遲。請從低於穩定實測吞吐量的值開始，而不是從服務標稱速率開始。入口整形通常需要更多餘量，因為上游傳送方和 ISP 佇列不在路由器的控制範圍內。在開銷補償正確的情況下，出口整形可以更接近實測鏈路速率執行。

在同時進行上傳和下載負載的情況下驗證該速率，同時測量延遲。僅測試吞吐量的速度測試無法說明互動式流量、語音或其他主機是否仍保持響應。當 CAKE 在主機和流之間共享容量時，單個流的吞吐量下降可能是預期結果。

:::warning
執行整形的 CAKE 例項不會將其封包處理分配到多個 CPU 核心。即使其他核心空閒，CPU 耗盡也可能降低吞吐量並增加延遲。請在目標裝置上測試所需的整形速率。不限速的 CAKE 所需處理量遠低於執行整形的 CAKE。
:::

:::note
被 FastTrack 處理的流量會繞過 `parent=global` 的 Simple Queue 和 Queue Tree。直接以介面為父級的 Queue Tree 可以處理被 FastTrack 處理的流量。請參閱 [FastTrack](../../connection-tracking.md#fasttrack)。
:::

## 開銷補償 {#overhead-compensation}

CAKE 必須知道每個封包在瓶頸鍊路上佔用多少時間。CAKE 可見的封包大小可能不包含成幀、封裝或包間開銷。如果沒有補償，配置的整形器可能傳送得略快於真實鏈路，從而導致佇列在其他位置堆積。

優先選擇與瓶頸技術匹配的 `cake-overhead-scheme`。方案會設定相關開銷、最小封包單元（MPU）以及 ATM 或 PTM 補償。僅當封裝已知且沒有匹配的預設時，才使用手動值。

| 方案 | 行為 |
| :-- | :-- |
| `raw` | 停用開銷補償。當 CAKE 可見的封包大小已經代表瓶頸所使用的單位時使用。 |
| `convervative` | 有意高估未知開銷。它等效於 48 位元組開銷並帶 ATM 補償。RouterOS 對此值使用拼寫 `convervative`。 |
| `ethernet` | 計入乙太網前導碼、幀間隔和幀校驗序列。它等效於 38 位元組開銷、84 位元組的 MPU，且無 ATM 或 PTM 補償。 |
| `via-ethernet` | 當 CAKE 收到完整乙太網幀而不是原始 IP 封包時，對另一個方案進行調整。僅將其作為修飾符與適用的基礎方案一起使用。 |
| `ether-vlan` | 為 IEEE 802.1Q VLAN 頭增加 4 位元組。將其與適用的基礎方案組合使用。 |
| `docsis` | 匹配 DOCSIS 頭端整形和計量所使用的乙太網幀大小。它等效於 18 位元組開銷、64 位元組的 MPU，且無 ATM 或 PTM 補償。 |
| ADSL 方案 | 選擇 `ipoa-vcmux`、`ipoa-llcsnap`、`bridged-vcmux`、`bridged-llcsnap`、`pppoa-vcmux`、`pppoa-llc`、`pppoe-vcmux` 或 `pppoe-llcsnap` 以匹配封裝。這些方案包含 ATM 信元補償。 |
| `pppoe-ptm` 或 `bridged-ptm` | 選擇匹配的 VDSL2 封裝。這些方案包含 PTM 補償。 |

對於手動配置，`cake-overhead` 接受 -64 到 256 位元組的值。`cake-mpu` 接受 0 到 256 位元組的值，且不能為負數。對於 ATM 信元成幀，請設定 `cake-atm=atm`；對於 PTM 編碼，請設定 `cake-atm=ptm`。

## RTT 方案 {#rtt-schemes}

CAKE 佇列規則使用往返時間（RTT）來調整其主動佇列管理引數。除非已知典型流量的 RTT，否則請保留預設的 `internet` 方案。較短的方案反應更快，但低於實際路徑 RTT 的值可能會降低長壽命流的吞吐量，尤其是在低速率鏈路上。該設定不需要與每個流精確匹配；實際 RTT 在大致一個數量級以內通常都能很好地工作。

對於大多數本地網路，請使用 `metro` 而不是 `lan`。`lan` 的激進時間常數可能過早發出擁塞訊號、降低吞吐量，並留下過少的排隊流量供公平性邏輯使用。請僅將其保留用於受控的純乙太網網路；在對網際網路接入鏈路進行整形時不要使用它。

以下是你可以使用的 RTT 設定、它們的含義以及可能使用它們的場景：

1. `cake-rtt`：手動指定 RTT，例如 `cake-rtt=100ms`。
2. `cake-rtt-scheme=datacentre`：假定 RTT 為 100 微秒。僅用於效能極高的資料中心網路。
3. `cake-rtt-scheme=lan`：假定 RTT 為 1 毫秒。僅用於受控的純乙太網網路，不用於網際網路接入鏈路。
4. `cake-rtt-scheme=metro`：假定 RTT 為 10 毫秒。用於大多數本地網路或同一城市內的流量。
5. `cake-rtt-scheme=regional`：假定 RTT 為 30 毫秒。用於區域內或國家內的流量。
6. `cake-rtt-scheme=internet`：假定 RTT 為 100 毫秒。適用於典型的網際網路流量。
7. `cake-rtt-scheme=oceanic`：假定 RTT 為 300 毫秒。用於延遲持續高於平均水平的網際網路流量。
8. `cake-rtt-scheme=satellite`：假定 RTT 為 1000 毫秒。用於地球同步衛星路徑。
9. `cake-rtt-scheme=interplanetary`：假定 RTT 為 3600 秒，並且幾乎完全停用主動佇列管理（AQM）操作。它不適用於普通網路配置。

對於衛星和其他高延遲鏈路，當預設與路徑不匹配時，請設定實測 RTT。預設是起點，而不是測量值。

## 流隔離 {#flow-isolation}

CAKE 透過源地址和目的地址、傳輸協定以及源埠和目的埠來識別流。它將流放入單獨的佇列並公平地排程它們。這樣，當大流量使用同一鏈路時，稀疏的低速率流仍能保持響應。

- `cake-flowmode=triple-isolate`：在源主機、目的主機和各個流之間應用公平性。這是預設值，也是典型閘道器的推薦起點。
- `cake-flowmode=dual-srchost`：先在源主機之間應用公平性，再在各主機的流之間應用公平性。當源地址標識需要平衡的訂閱者或裝置時使用。
- `cake-flowmode=dual-dsthost`：先在目的主機之間應用公平性，再在各主機的流之間應用公平性。當目的地址標識需要平衡的訂閱者或裝置時使用。
- `cake-flowmode=srchost`：僅在源地址之間應用公平性。
- `cake-flowmode=dsthost`：僅在目的地址之間應用公平性。
- `cake-flowmode=hosts`：在源主機和目的主機對之間應用公平性。
- `cake-flowmode=flows`：僅在完整的五元組流之間應用公平性。
- `cake-flowmode=flowblind`：停用流隔離，並將每個 tin 的所有流量放入一個佇列。

當路由器執行 NAT 時，請設定 `cake-nat=yes`，以便 CAKE 能夠隔離內部地址和埠。除非拓撲需要特定的方向模式，否則請保留 `triple-isolate`。常被複制的組合——上傳使用 `dual-srchost`、下載使用 `dual-dsthost`——主要適用於 CAKE 已經能夠看到所需主機地址而無需 NAT 查詢的情況。當另一臺裝置執行 NAT，或硬體解除安裝的流量繞過 CAKE 時，NAT 查詢不會生效。

## ACK 過濾器 {#ack-filter}

ACK 過濾會在冗餘 TCP 確認封包占用狹窄傳送鏈路的容量之前將其移除。請從 `cake-ack-filter=filter` 開始；僅在測試表明額外過濾不會降低 TCP 效能後，才使用 `cake-ack-filter=aggressive`。設定 `cake-ack-filter=none` 可停用它。

僅在高度非對稱連線的較慢一側的傳送佇列上啟用 ACK 過濾。當下載/上傳比率超過約 10:1 時，它才會變得相關。不要在接收佇列上啟用它：ACK 封包通常不會在那裡堆積，而且過濾器會消耗額外的 CPU。

ACK 過濾無法檢查加密流量（例如 WireGuard 或 IPsec 隧道）內部的 ACK 封包。請在明文 TCP ACK 封包可見的位置應用它。

## DiffServ {#diffserv}

差分服務（DiffServ）根據封包的差分服務程式碼點（DSCP）對其進行分類，並將它們放入稱為 tin 的 CAKE 流量類別中。CAKE 在 tin 之間應用軟優先順序：每個 tin 都會獲得服務，並且可以借用未使用的容量。百分比閾值不是固定頻寬限制。例如，當其他 tin 空閒時，Best Effort 可以使用鏈路的 100%。

- `cake-diffserv=diffserv3`（預設）：提供 Bulk（CS1 和 LE）、Best Effort（一般流量）和 Voice（CS7、CS6、EF、VA 和 TOS4）tin。它們的閾值分別為 6.25%、100% 和 25%。Voice 使用更短的 CoDel 間隔。
- `cake-diffserv=diffserv4`：提供 Bulk（CS1 和 LE）、Best Effort（一般流量）、Video（AF4x、AF3x、CS3、AF2x、CS2、TOS4 和 TOS1）和 Voice（CS7、CS6、EF、VA、CS5 和 CS4）tin。它們的閾值分別為 6.25%、100%、50% 和 25%。
- `cake-diffserv=diffserv8`：為具有精心設計且詳細的 DSCP 策略的網路提供八個 tin。
- `cake-diffserv=besteffort`：停用優先順序排隊，並將所有流量放入一個 tin。當 DSCP 標記不存在或不應影響排程時使用。
- `cake-diffserv=precedence`：使用舊式 IP 優先順序解釋。在新配置中應避免使用此模式。

CAKE 本身不會建立可信的分類。僅當你信任接收到的 DSCP 標記，或透過一致的本地策略設定它們時，才使用 DiffServ 模式。錯誤的高優先順序標記可能會使流量獲得非預期的服務。

## Wash {#wash}

`cake-wash=yes` 選項會在 CAKE 使用 DSCP 標記做出優先順序決策後清除這些標記。它不會清除顯式擁塞通知（ECN）位。

當下一跳網路不得繼承現有 DSCP 策略時，請在 DiffServ 域邊界啟用 `cake-wash=yes`。如果不信任入站標記且這些標記不應影響排程，請使用 `cake-diffserv=besteffort`；再加上 `cake-wash=yes` 還會在轉發封包之前清除這些標記。

## Autorate 入口 {#autorate-ingress}

`cake-autorate-ingress` 選項根據入口封包的到達時間估算容量，並調整 CAKE 的內部整形器。可選的 `cake-bandwidth` 值提供其初始估算值。

該估算器僅觀察到達此 CAKE 例項的流量。它無法測量更下游的瓶頸，並且必須接收到足夠的流量後才能提高其估算值。因此，容量變化大或變化快的鏈路（例如 LTE 和 5G）可能產生不穩定或意外偏低的速率。

:::warning
在生產使用之前，請在實際鏈路上測試 `cake-autorate-ingress`。它是 CAKE 的內建估算器，與持續測量延遲並更新整形器的外部自適應速率實現不同。當可預測的延遲和吞吐量比跟隨每一次容量變化更重要時，請使用低於可靠鏈路容量的固定速率。
:::

當打算由 HTB 控制速率時，請不要啟用 `cake-autorate-ingress`。該選項改變的是 CAKE 的整形器，而不是 HTB 的 `max-limit`。
