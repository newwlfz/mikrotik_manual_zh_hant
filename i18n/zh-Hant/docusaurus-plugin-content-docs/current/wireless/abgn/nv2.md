---
sidebar_key: "wireless/abgn/nv2"
sidebar_position: 4
title: "Nv2"
sidebar_label: "Nv2"
description: "Nv2 是 MikroTik 專有的無線協定，使用 TDMA 在 PtMP 網路中實現高效的媒體訪問，支援 Atheros 802.11n 和傳統裝置，無需硬體升級。它提供動態速率選擇、QoS、加密、RADIUS 認證和同步功能，但與其他無線協定不相容。"
tags:
  - 'nv2'
  - 'tdma'
  - 'qos'
source: https://manual.mikrotik.com/docs/wireless/abgn/nv2
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Nv2 是 MikroTik 開發的專有無線協定，用於 Atheros 802.11 無線晶片。它基於 TDMA（分時多重進接）媒體訪問技術，而不是普通 802.11 裝置使用的 CSMA（載波偵聽多路訪問）技術。TDMA 解決了隱藏節點問題並提高了媒體使用效率，從而帶來更好的吞吐量和延遲——尤其是在 PtMP 網路中。

Nv2 受支援於 Atheros 802.11n 晶片以及從 AR5212 開始的傳統 802.11a/b/g 晶片，但不支援較舊的 AR5211 和 AR5210 晶片。這意味著 11n 和傳統裝置都可以加入同一網路，並且實施 Nv2 無需硬體升級。

Nv2 網路中的媒體訪問由 Nv2 接入點控制。AP 將時間劃分為固定大小的“週期”，然後根據 AP 和用戶端上的佇列狀態，動態劃分為下行（AP 到用戶端）和上行（用戶端到 AP）部分。上行時間再根據已連線用戶端的頻寬需求在它們之間分配。每個週期開始時，AP 會廣播排程，告知用戶端何時應傳送以及可以使用多少時間。

為了允許新用戶端連線，Nv2 AP 會定期為“未指定”用戶端分配上行時間。新用戶端使用此間隔向 AP 發起註冊。然後，AP 會估計自身與用戶端之間的傳播延遲，並開始定期為該用戶端排程上行時間，以完成註冊和接收資料。

Nv2 按用戶端實現動態速率選擇，併為資料傳輸實現 ARQ，從而在 Nv2 鏈路上實現可靠通訊。

在 QoS 方面，Nv2 支援可變數量的優先順序佇列，並內建預設 QoS 排程器。這可以透過基於防火牆規則的細粒度 QoS 策略，或透過使用 VLAN 優先順序或 MPLS EXP 位在網路中傳播的優先順序資訊來補充。

Nv2 協定每個介面最多支援 511 個用戶端。

## Nv2 協定實現狀態 {#nv2-protocol-implementation-status}

Nv2 包含以下功能：

| 功能 | 描述 |
|---|---|
| TDMA 媒體訪問 | 用於媒體控制的分時多重進接 |
| WDS 支援 | 無線分佈系統相容性 |
| QoS 支援 | 可變數量的優先順序佇列 |
| 資料加密 | 對傳輸資料進行加密 |
| RADIUS 認證 | 基於 RADIUS 的認證功能 |
| 統計欄位 | 可用的統計和報告欄位 |
| 固定下行模式 | 支援固定下行操作 |
| 上行/下行比率 | 可配置的上行/下行比率支援 |
| Nv2 AP 同步 | 對 AP 同步的實驗性支援 |

## 與其他無線協定的相容性和共存 {#compatibility-and-coexistence-with-other-wireless-protocols}

Nv2 協定不相容也不基於任何其他可用的無線協定或實現，無論其基於 TDMA 還是其他型別。這意味著**只有支援並啟用了 Nv2 的裝置才能加入 Nv2 網路**。

普通 802.11 裝置無法識別 Nv2 AP，也無法連線到 Nv2 AP。支援 Nv2 的 RouterOS 裝置（即執行 RouterOS 5.0rc1 或更高版本）在執行 scan 命令時會看到 Nv2 AP，但只有正確配置後才會連線到 Nv2 AP。

由於 Nv2 不使用 CSMA 技術，它可能會干擾同一通道上的其他網路。同樣，其他網路也可能干擾 Nv2 網路，因為所有非 Nv2 訊號都會被當作噪聲。

關於相容性和共存的關鍵點如下：

* 只有 RouterOS 裝置才能加入 Nv2 網路。
* 只有 RouterOS 裝置在掃描時才能看到 Nv2 AP。
* Nv2 網路會干擾同一通道上的其他網路。
* Nv2 網路可能會受到同一通道上任何其他網路的影響，無論該網路是否為 Nv2。
* 啟用了 Nv2 的裝置不會連線到任何其他基於 TDMA 的網路。

## Nv2 與 Nstreme 和 802.11 的比較 {#how-nv2-compares-with-nstreme-and-80211}

### Nv2 與 802.11 {#nv2-vs-80211}

Nv2 與 802.11 的主要區別：

* 媒體訪問由 AP 排程——這消除了隱藏節點問題，並允許實施集中式媒體訪問策略——AP 控制每個用戶端使用多少時間，並且可以根據某種策略為用戶端分配時間，而不是讓每個裝置競爭媒體訪問。
* 降低傳播延遲開銷——Nv2 中沒有逐幀 ACK——這顯著提高了吞吐量，尤其是在長距離鏈路上，資料幀及隨後的 ACK 幀的傳播延遲會顯著降低媒體使用效率。
* 降低每幀開銷——Nv2 實現幀聚合和分片，以最大化分配的媒體使用率並降低每幀開銷（幀間間隔、前導碼）。

### Nv2 與 Nstreme {#nv2-vs-nstreme}

Nv2 與 Nstreme 的主要區別：

* 降低輪詢開銷——Nv2 AP 不逐個輪詢用戶端，而是廣播上行排程，為多個用戶端分配時間；這可以視為“組輪詢”——不會把時間浪費在逐個輪詢每個用戶端上，從而為實際資料傳輸留出更多時間。這提高了吞吐量，尤其是在 PtMP 配置中。
* 降低傳播延遲開銷——Nv2 不必逐個輪詢每個用戶端；這允許根據到用戶端的估計距離（傳播延遲）建立上行排程，從而使媒體使用效率最高。這提高了吞吐量，尤其是在 PtMP 配置中。
* 更好地控制延遲——降低的開銷、可調整的週期大小和 QoS 功能可以更好地控制網路中的延遲。

## 配置 Nv2 {#configuring-nv2}

**wireless-protocol** 設定控制選擇和使用哪種無線協定。請注意，此設定的含義取決於介面角色（AP 或用戶端），而介面角色取決於介面 **mode** 設定。下表中列出了 **wireless-protocol** 的可能值及其含義。

| 值 | AP | 用戶端 |
| :-- | :-- | :-- |
| unspecified | 根據舊的 **nstreme** 設定建立 nstreme 或 802.11 網路 | 根據舊的 **nstreme** 設定連線到 nstreme 或 802.11 網路 |
| any | 與 **unspecified** 相同 | 掃描所有匹配網路，無論使用何種協定，並使用所選網路的協定進行連線 |
| 802.11 | 建立 802.11 網路 | 僅連線到 802.11 網路 |
| nstreme | 建立 Nstreme 網路 | 僅連線到 Nstreme 網路 |
| Nv2 | 建立 Nv2 網路 | 僅連線到 Nv2 網路 |
| Nv2-nstreme-802.11 | 建立 Nv2 網路 | 掃描 Nv2 網路；如果找到合適的網路，則連線；否則掃描 Nstreme 網路；如果找到合適的網路，則連線；否則掃描 802.11 網路，如果找到合適的網路，則連線。 |
| Nv2-nstreme | 建立 Nv2 網路 | 掃描 Nv2 網路；如果找到合適的網路，則連線；否則掃描 Nstreme 網路，如果找到合適的網路，則連線 |

請注意，**wireless-protocol** 的值 **Nv2-nstreme-802.11** 和 **Nv2-nstreme** **並不**指定某種混合或特殊型別的協定——實現這些值是為了簡化用戶端配置，適用於用戶端必須連線的網路協定可能變化的情況。使用這些值有助於將網路遷移到 Nv2 協定。

大多數 Nv2 設定僅對 Nv2 AP 有意義——Nv2 用戶端會自動採用 AP 的必要設定。以下設定與 Nv2 AP 相關：

* **Nv2-queue-count**——指定 Nv2 網路中使用的優先順序佇列數量。有關更多詳細資訊，請參閱 [Nv2 網路中的 QoS](#qos-in-nv2-network)。
* **Nv2-qos**——控制幀到優先順序佇列的對映策略。有關更多詳細資訊，請參閱 [Nv2 網路中的 QoS](#qos-in-nv2-network)。
* **Nv2-cell-radius**——指定 Nv2 網路中到最遠用戶端的距離，單位為 km。此設定會影響 AP 為用戶端分配用於發起連線的競爭時隙大小，也會影響用於估計到用戶端距離的時隙大小。如果此設定過小，距離較遠的用戶端可能無法連線，和/或斷開並出現“ranging timeout”錯誤。儘管在正常執行期間此設定的影響應該可以忽略不計，但為了保持最大效能，建議非必要不要增大此設定，這樣 AP 就不會預留實際上從未使用的時間，而是將其分配給實際資料傳輸。
* **tdma-period-size**——指定 Nv2 AP 用於媒體訪問排程的時間週期大小，單位為 ms。較小的週期有可能降低延遲（因為 AP 可以更早地為用戶端分配時間），但會增加協定開銷，從而降低吞吐量。另一方面，增大週期會提高吞吐量，但也會增加延遲。對於特別長的鏈路，可能需要增大此值才能獲得可接受的吞吐量。這種必要性可能源於下行（從 AP 到用戶端）和上行（從用戶端到 AP）資料之間存在“傳播間隙”，在此期間不會發生資料傳輸。這個間隙是必要的，因為用戶端必須收到來自 AP 的最後一幀——這發生在 AP 傳輸經過傳播延遲之後，只有到這時用戶端才能傳輸——結果，來自用戶端的幀會在用戶端傳輸經過傳播延遲之後到達 AP（因此該間隙為傳播延遲的兩倍）。距離越長，每個週期中所需的傳播間隙就越大。如果傳播間隙佔週期的很大一部分，實際吞吐量可能變得不可接受，此時應以增加延遲為代價增大週期大小。基本上，必須仔細選擇此設定的值，以最大化吞吐量，同時將延遲保持在可接受水平。
* **Nv2-mode**——指定使用動態或固定下行/上行比率。預設值為 "dynamic-downlink"。

"sync-master"——作用等同於 nv2-mode=fixed-downlink（因此使用 nv2-downlink-ratio），但允許從裝置同步到此主裝置；"sync-slave"——嘗試同步到主裝置（或已同步的從裝置），並從主裝置採用 period-size 和下行比率設定。

* **Nv2-downlink-ratio**——指定 Nv2 下行比率。上行比率根據 downlink-ratio 值自動計算。使用 dynamic-downlink 模式時，當鏈路完全飽和，也會使用 downlink-ratio。最小值為 20，最大值為 80。預設值為 50。

以下設定在 Nv2 AP 和 Nv2 用戶端上都很重要：

* **Nv2-security**——指定 Nv2 安全模式，有關更多詳細資訊，請參閱 [Nv2 網路中的安全](#security-in-nv2-network)。
* **Nv2-preshared-key**——指定要使用的預共享金鑰，有關更多詳細資訊，請參閱 [Nv2 網路中的安全](#security-in-nv2-network)。
* **nv2-sync-secret**——指定用於 Nv2 同步的金鑰。主裝置和從裝置上的金鑰應匹配，才能建立同步狀態。

## 遷移到 Nv2 {#migrating-to-nv2}

使用 **wireless-protocol** 設定可以非常簡單地在現有網路中遷移或評估 Nv2 協定，並儘可能減少停機時間。以下是推薦步驟：

* 將 AP 升級到支援 Nv2 的版本，但暫時不要在 AP 上啟用 Nv2。
* 將用戶端升級到支援 Nv2 的版本。
* 將所有用戶端配置為 **wireless-protocol=Nv2-nstreme-802.11**。用戶端仍會使用之前使用的協定連線到 AP，因為 AP 尚未切換到 Nv2。
* 在 AP 上配置 Nv2 相關設定。
* 如果需要使用資料加密和安全認證，請在 AP 和用戶端上配置 Nv2 安全相關設定（請參閱 [Nv2 網路中的安全](#security-in-nv2-network)）。
* 在 AP 上設定 **wireless-protocol=Nv2**。這會使 AP 切換到 Nv2 協定。用戶端現在應使用 Nv2 協定連線。
* 如果遇到問題，只需將其改回 AP 之前使用的協定，即可輕鬆切換回之前的協定。
* 微調 Nv2 相關設定，以獲得可接受的延遲和吞吐量。
* 實施 QoS 策略以獲得最大效能。

基本故障排除指南：

* 用戶端連線困難或斷開並出現“ranging timeout”錯誤——檢查 **Nv2-cell-radius** 設定是否設定得當。
* 儘管訊號和速率正常，但長距離鏈路的吞吐量卻意外偏低——嘗試增大 **tdma-period-size** 設定。

## Nv2 AP 同步 {#nv2-ap-synchronization}

此功能透過減少相互之間的干擾，使同一位置上的多個 MikroTik Nv2 AP 以更好的方式共存。此功能會同步同一頻率上 AP 的傳送/接收時間視窗，使所有已同步的 MikroTik Nv2 AP 在同一時間傳送/接收。這樣一來，就可以在同一位置為多個 AP 複用同一無線頻率，從而在頻率規劃方面提供更大的靈活性。

要建立 Nv2 同步設定：

* 對於 Nv2 同步，應選擇一個主 Nv2 AP，並同時指定 "nv2-mode=sync-master" 和 "nv2-sync-secret"。
* 對於 Nv2 從 AP，應使用與主 AP 相同的無線頻率，並指定 "nv2-mode=sync-slave"，且使用與主 AP 配置中相同的 "nv2-sync-secret"。
* 啟用主 AP 後，從 AP 會嘗試透過將指定的 "nv2-sync-secret" 與其匹配來開始搜尋主 AP。
* 找到主 AP 後，從 AP 會計算到主 AP 的距離，因為主 AP 可能並不位於同一位置。
* 然後，從 AP 開始作為 AP 執行，並採用已同步主 AP 的週期大小和下行比率。
* 此外，從 AP 投入執行後，其他從 AP 可以使用此從 AP 進行同步。
* 從 AP 會定期監聽主 AP，檢查 "nv2-sync-secret" 是否仍然匹配，並再次採用相應引數。如果停用/啟用主 AP 介面，所有從裝置也會被停用，並從頭開始同步過程。
* 如果主 AP 停止工作，從 AP 也會停止工作，因為它們沒有同步資訊。

### 配置示例 {#configuration-example}

主 AP：

```
 /interface/wireless/set wlan1 mode=ap-bridge ssid=Sector1 frequency=5220 nv2-mode=sync-master nv2-preshared-key=clients1 nv2-sync-secret=Tower1
```

從 AP：

```
 /interface/wireless/set wlan1 mode=ap-bridge ssid=Sector2 frequency=5220 nv2-mode=sync-slave nv2-preshared-key=clients2 nv2-sync-secret=Tower1
```

在從 AP 上監控介面：

```
[admin@SlaveAP] /interface/wireless> monitor wlan1
                   status: running-ap
                  channel: 5220/20/an
        wireless-protocol: nv2
              noise-floor: -110dBm
       registered-clients: 1
    authenticated-clients: 1
           nv2-sync-state: synced
          nv2-sync-master: 4C:5E:0C:57:84:38
        nv2-sync-distance: 1
     nv2-sync-period-size: 2
  nv2-sync-downlink-ratio: 50
```

主 AP 上的偵錯日誌：

```
 09:22:08 wireless,debug wlan1: 4C:5E:0C:57:85:BE attempts to sync
```

從 AP 上的偵錯日誌：

```
09:22:08 wireless,debug wlan1: attempting to sync to 4C:5E:0C:57:84:38 
09:22:09 wireless,debug wlan1: synced to 4C:5E:0C:57:84:38 
```

## Nv2 網路中的 QoS {#qos-in-nv2-network}

Nv2 中的 QoS 透過可變數量的優先順序佇列實現。根據 802.1D-2004 推薦的規則，只有當所有更高優先順序佇列都為空時，才會考慮傳輸某個佇列。在實踐中，這意味著首先會發送來自更高優先順序佇列的所有幀，然後才會考慮下一個佇列。因此，必須謹慎設計 QoS 策略，以免更高優先順序佇列使較低優先順序佇列得不到服務。

Nv2 網路中的 QoS 策略由 AP 控制，用戶端會採用來自 AP 的策略。在 AP 上，QoS 策略透過 **Nv2-queue-count** 和 **Nv2-qos** 引數配置。**Nv2-queue-count** 引數指定使用的優先順序佇列數量。幀到佇列的對映由 **Nv2-qos** 引數控制。

### Nv2-qos=default {#nv2-qosdefault}

在此模式下，出站幀首先由內建 QoS 策略演算法檢查，該演算法根據封包型別和大小選擇佇列。如果內建規則不匹配，則根據幀優先順序欄位選擇佇列，與 **Nv2-qos=frame-priority** 模式中一樣。

### Nv2-qos=frame-priority {#nv2-qosframe-priority}

在此模式下，QoS 佇列根據幀優先順序欄位選擇。請注意，幀優先順序欄位並不是標頭中的某個欄位，因此它僅在封包由給定裝置處理期間有效。幀優先順序欄位必須由防火牆規則顯式設定，或由幀轉發過程根據入口優先順序隱式設定，例如根據 MPLS EXP 位。有關幀優先順序欄位的更多資訊，請參閱：

* [EXP 位和 MPLS 排隊](../../user-guides/routing-and-networking-protocols/mpls/exp-bit-and-mpls-queuing.md)
* [WMM 和 VLAN 優先順序](../../bridging-and-switching/user-guides/wmm-and-vlan-priority.md)

根據 802.1D 推薦的使用者優先順序到流量類別對映，佇列基於幀優先順序進行選擇。對映取決於可用佇列數量（**Nv2-queue-count** 引數）。例如，如果佇列數量為 4，則對映如下（請注意此對映與 WMM 使用的對映有何相似之處）：

* 優先順序 0、3 -> 佇列 0。
* 優先順序 1、2 -> 佇列 1。
* 優先順序 4、5 -> 佇列 2。
* 優先順序 6、7 -> 佇列 3。

如果佇列數量為 2（預設），則對映如下：

* 優先順序 0、1、2、3 -> 佇列 0。
* 優先順序 4、5、6、7 -> 佇列 1。

如果佇列數量為 8（可能的最大值），則對映如下：

* 優先順序 1 -> 佇列 0。
* 優先順序 2 -> 佇列 1。
* 優先順序 0 -> 佇列 2。
* 優先順序 3 -> 佇列 3。
* 優先順序 4 -> 佇列 4。
* 優先順序 5 -> 佇列 5。
* 優先順序 6 -> 佇列 6。
* 優先順序 7 -> 佇列 7。

有關其他對映、這些對映的原理討論以及推薦實踐，請參閱 802.1D-2004。

## Nv2 網路中的安全 {#security-in-nv2-network}

Nv2 安全實現具有以下功能：

* 使用 128 位金鑰的 AES-CCM 進行硬體加速資料加密。
* 用於金鑰管理的 4 次握手（類似於 802.11i）。
* 預共享金鑰認證方法（類似於 802.11i）。
* 定期更新的組金鑰（用於廣播和多播資料）。

作為專有協定，Nv2 不使用 802.11 的安全機制，因此安全配置有所不同。使用 Nv2 協定的介面會忽略 **security-profile** 設定。相反，安全透過以下介面設定進行配置：

* **Nv2-security**——此設定啟用/停用 Nv2 網路中的安全功能。請注意，當 AP 上啟用安全功能時，它不會接受停用了安全功能的用戶端。同樣，啟用了安全功能的用戶端不會連線到不安全的 AP。
* **Nv2-preshared-key**——用於認證的預共享金鑰。資料加密金鑰在 4 次握手期間從預共享金鑰派生。兩臺裝置必須使用相同的預共享金鑰才能建立連線。如果預共享金鑰不同，連線將超時，因為對方將無法正確解析金鑰交換訊息。
