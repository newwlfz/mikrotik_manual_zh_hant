---
sidebar_key: "firewall-and-quality-of-service/queues/htb-hierarchical-token-bucket"
sidebar_position: 1
title: "HTB（分層令牌桶）"
sidebar_label: "HTB"
description: "HTB（Hierarchical Token Bucket）是 RouterOS 中的一種佇列規則，用於速率限制和突發處理，使用令牌桶演算法透過可配置的容量和限制來管理資料速率。"
tags:
  - 'htb'
  - 'queues'
  - 'bandwidth-control'
source: https://manual.mikrotik.com/docs/7.25/firewall-and-quality-of-service/queues/htb-hierarchical-token-bucket
captured_at: '2026-11-04T11:16:25+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 簡介 {#introduction}

HTB（Hierarchical Token Bucket）是一種分類排隊規則，適用於速率限制和突發處理。本文將專門聚焦 RouterOS 中的這些 HTB 方面，因為我們使用修改版本來實現 Simple Queue 和 Queue Tree 等功能。

## 令牌桶演算法（圖中紅色部分） {#token-bucket-algorithm-red-part-of-the-diagram}

令牌桶演算法基於一個類比：令牌以位元組表示，並以特定速率新增到桶中。桶本身具有指定容量。

如果桶已滿，新到達的令牌會被丟棄。

**桶容量 = bucket-size \* max-limit**

- **bucket size**（0..10，預設值：0.1）

在允許任何封包透過佇列之前，會檢查佇列桶，以確定它在那一刻是否已經包含足夠的令牌。

如果是，則移除（“兌現”）相應數量的令牌，並允許該封包透過佇列。

如果否，則封包會停留在封包等待佇列的開頭，直到有足夠數量的令牌可用。

在多級佇列結構的情況下，子佇列中使用的令牌也會被“計入”其父佇列。換句話說——子佇列從其父佇列“借用”令牌。

### 封包佇列（圖中藍色部分） {#packet-queue-blue-part-of-the-diagram}

此封包佇列的大小、順序、封包如何加入此佇列以及何時丟棄封包，由以下各項決定：

- **queue-type** - [佇列](./index.md)
- **queue-size** - [佇列大小](./queue-size.md)

### 令牌速率選擇（圖中黑色部分） {#token-rate-selection-black-part-of-the-diagram}

任意給定時間的最大令牌速率等於這些值中的最高活動值：

- **limit-at**（*NUMBER/NUMBER*）：到目標的保證上傳/下載資料速率。
- **max-limit**（*NUMBER/NUMBER*）：允許到目標的最大上傳/下載資料速率。
- **burst-limit**（*NUMBER/NUMBER*）：當 'burst' 處於活動狀態時，允許到目標的最大上傳/下載資料速率。

**burst-limit** 僅在 'burst' 處於允許狀態時生效——更多資訊見：[佇列突發](./queue-burst.md)

當 **limit-at** 為最高值時，需要發放額外令牌，以補償所有未從其父佇列借用的缺失令牌。

### 示意圖 {#the-diagram}

![](/img/9a50fc5a9449fae0.webp)

### Bucket Size 實際應用 {#bucket-size-in-action}

讓我們進行一個簡單設定：發往和來自一個 IP 地址的所有流量都用 packet-mark 標記：

```ros
/ip/firewall/mangle
add chain=forward action=mark-connection connection-mark=no-mark src-address=192.168.88.101 new-connection-mark=pc1_conn
add chain=forward action=mark-connection connection-mark=no-mark dst-address=192.168.88.101 new-connection-mark=pc1_conn
add chain=forward action=mark-packet connection-mark=pc1_conn new-packet-mark=pc1_traffic
```

#### 預設佇列桶 {#default-queue-bucket}

```ros
/queue/tree
add name=download parent=Local packet-mark=pc1_traffic max-limit=10M
add name=upload parent=Public packet-mark=pc1_traffic max-limit=10M
```

在這種情況下，bucket-size=0.1，因此 bucket-capacity= 0.1 x 10M = 1M。

如果桶已滿（也就是說，用戶端有一段時間沒有使用佇列的全部容量），接下來的 1Mb 流量就可以不受限制地透過佇列。

#### 大佇列桶 {#large-queue-bucket}

```ros
/queue/tree
add name=download parent=Local packet-mark=pc1_traffic max-limit=10M bucket-size=10
add name=upload parent=Public packet-mark=pc1_traffic max-limit=10M bucket-size=10
```

讓我們嘗試將同樣的邏輯應用於 bucket size 處於最大值的情況：

在這種情況下，bucket-size=10，因此 bucket-capacity= 10 x 10M = 100M。

如果桶已滿（也就是說，用戶端有一段時間沒有使用佇列的全部容量），接下來的 100Mb 流量就可以不受限制地透過佇列。

因此你可以獲得：

- 10 秒的 20Mbps 傳輸速度。
- 2 秒的 60Mbps 傳輸突發。
- 約 100ms 的 1Gbps 傳輸突發。

因此可以看到，桶允許透過佇列的流量具有一定型別的“突發性”。該行為類似於普通 burst 功能，但沒有突發的上限。如果在佇列結構中利用 bucket size，就可以避免這個缺陷：

#### 大子佇列桶，小父佇列桶 {#large-child-queue-bucket-small-parent-queue-bucket}

```ros
/queue/tree
add name=download_parent parent=Local max-limit=20M
add name=download parent=download_parent packet-mark=pc1_traffic max-limit=10M bucket-size=10
add name=upload_parent parent=Public max-limit=20M
add name=upload parent=upload_parent packet-mark=pc1_traffic max-limit=10M bucket-size=10
```

在這種情況下：

- 父佇列 bucket-size=0.1，bucket-capacity= 0.1 x 20M = 2M
- 子佇列 bucket-size=10，bucket-capacity= 10 x 10M = 100M

父佇列會比子佇列更快耗盡令牌；由於子佇列始終從父佇列借用令牌，整個系統將受限於父佇列的令牌速率——在本例中為 max-limit=20M。該速率將一直維持，直到子佇列耗盡令牌，然後受限於其 10Mbps 的令牌速率。

透過這種方式，我們可以獲得最高持續 10 秒的 20Mbps 突發。

## 配置 {#configuration}

建立 HTB 需要遵循三個基本步驟：

- **匹配並標記流量**——對流進行分類以便後續使用。它由一個或多個匹配引數組成，用於為特定類別選擇封包。
- **建立用於標記流量的規則（策略）**——將特定流量類別放入特定佇列，並定義對每個類別採取的操作。
- **為特定介面附加策略**——為所有介面（global-in、global-out 或 global-total）、特定介面或特定父佇列追加策略。

HTB 允許建立分層佇列結構，並確定佇列之間的關係，例如“父-子”或“子-子”。

一旦佇列至少有一個子佇列，它就會成為**內部**佇列。所有沒有子佇列的佇列都是**葉子**佇列。**葉子**佇列實際消耗流量，**內部**佇列只負責流量分配。所有**葉子**佇列都按同等基礎處理。

在 RouterOS 中，必須指定 **parent** 選項，才能將一個佇列作為子佇列分配給另一個佇列。

### 雙重限制 {#dual-limitation}

HTB 中的每個佇列都有兩個速率限制：

- **CIR**（Committed Information Rate）——（RouterOS 中的 **limit-at**）最壞情況，即無論發生什麼，該流都將獲得此流量（假設我們確實能傳送這麼多資料）。
- **MIR**（Maximal Information Rate）——（RouterOS 中的 **max-limit**）最好情況，即如果其佇列的父佇列有剩餘頻寬，該流可達到的速率。

換句話說，首先會滿足所有佇列的 **limit-at**（**CIR**），只有之後子佇列才會嘗試從父佇列借用必要的資料速率，以達到其 **max-limit**（**MIR**）。

:::warning
無論發生什麼，**CIR** 都會分配給對應佇列（即使超過父佇列的 max-limit）。

:::

因此，為確保按設計最優地使用雙重限制功能，我們建議遵守以下規則：

- 所有子佇列的承諾速率之和必須小於或等於父佇列可用的流量總量；

CIR(parent)\* ≥ CIR(child1) +...+ CIR(childN)\* 如果父佇列是主父佇列 CIR(parent)=MIR(parent)

- 任何子佇列的最大速率必須小於或等於父佇列的最大速率。

MIR（父級）≥ MIR(child1) & MIR（父級）≥ MIR(child2) & ... & MIR（父級）≥ MIR(childN)

# Winbox 中的佇列顏色 {#queue-colors-in-winbox}

- 已使用 0% - 50% 可用流量 - 綠色
- 已使用 50% - 75% 可用流量 - 黃色
- 已使用 75% - 100% 可用流量 - 紅色

#### 優先順序 {#priority}

我們已經知道，無論發生什麼，所有佇列的 **limit-at**（**CIR**）都會被分配。

優先順序負責將父佇列的剩餘流量分配給子佇列，以便它們能夠達到 **max-limit**

優先順序較高的佇列會比優先順序較低的佇列先達到其 **max-limit**。8 是最低優先順序，1 是最高優先順序。

請注意，優先順序僅在以下情況下生效：

- 對於**葉子**佇列——**內部**佇列中的優先順序沒有意義。
- 如果指定了 **max-limit**（不為 0）。

### 示例 {#examples}

在本節中，我們將分析 HTB 的實際應用。為此，我們將採用一個 HTB 結構，並透過改變 HTB 需要回收的傳入流量以及更改一些選項，嘗試涵蓋所有可能的情況和功能。

#### 結構 {#structure}

我們的 HTB 結構將包含 5 個佇列：

- **Queue01** 內部佇列，有兩個子佇列——**Queue02** 和 **Queue03**
- **Queue02** 內部佇列，有兩個子佇列——**Queue04** 和 **Queue05**
- **Queue03** 葉子佇列
- **Queue04** 葉子佇列
- **Queue05** 葉子佇列

**Queue03**、**Queue04** 和 **Queue05** 是始終需要 10Mbps 的用戶端。出介面能夠處理 10Mbps 的流量。

#### 示例 1：常見情況 {#example-1-usual-case}

![](/img/6471583db1f39245.webp)

- **Queue01** limit-at=0Mbps max-limit=10Mbps
- **Queue02** limit-at=4Mbps max-limit=10Mbps
- **Queue03** limit-at=6Mbps max-limit=10Mbps priority=1
- **Queue04** limit-at=2Mbps max-limit=10Mbps priority=3
- **Queue05** limit-at=2Mbps max-limit=10Mbps priority=5

#### 示例 1 的結果 {#result-of-example-1}

- **Queue03** 將獲得 6Mbps。
- **Queue04** 將獲得 2Mbps。
- **Queue05** 將獲得 2Mbps。
- **說明：** HTB 的構建方式使得在滿足所有 **limit-at** 後，主佇列不再有可分配的吞吐量。

#### 示例 2：帶 max-limit 的常見情況 {#example-2-usual-case-with-max-limit}

![](/img/bf53f5b2e1d05693.webp)

- **Queue01** limit-at=0Mbps max-limit=10Mbps
- **Queue02** limit-at=4Mbps max-limit=10Mbps
- **Queue03** limit-at=2Mbps max-limit=10Mbps priority=3
- **Queue04** limit-at=2Mbps max-limit=10Mbps priority=1
- **Queue05** limit-at=2Mbps max-limit=10Mbps priority=5

#### 示例 2 的結果 {#result-of-example-2}

- **Queue03** 將獲得 2Mbps。
- **Queue04** 將獲得 6Mbps。
- **Queue05** 將獲得 2Mbps。
- **說明：** 在滿足所有 **limit-at** 後，HTB 會將吞吐量分配給優先順序最高的佇列。

#### 示例 3：內部佇列 limit-at {#example-3-inner-queue-limit-at}

![](/img/676b7895208fbed6.webp)

- **Queue01** limit-at=0Mbps max-limit=10Mbps。
- **Queue02** limit-at=8Mbps max-limit=10Mbps。
- **Queue03** limit-at=2Mbps max-limit=10Mbps priority=1。
- **Queue04** limit-at=2Mbps max-limit=10Mbps priority=3。
- **Queue05** limit-at=2Mbps max-limit=10Mbps priority=5。

#### 示例 3 的結果 {#result-of-example-3}

- **Queue03** 將獲得 2Mbps。
- **Queue04** 將獲得 6Mbps。
- **Queue05** 將獲得 2Mbps。
- **說明：** 在滿足所有 **limit-at** 後，HTB 會將吞吐量分配給優先順序最高的佇列。但在本例中，**內部**佇列 **Queue02** 指定了 **limit-at**，因此它為佇列 **Queue04** 和 **Queue05** 預留了 8Mbps 的吞吐量。在這兩者中，**Queue04** 的優先順序最高，因此它獲得了額外吞吐量。

#### 示例 4：葉子佇列 limit-at {#example-4-leaf-queue-limit-at}

![](/img/8897e6539e058049.webp)

- **Queue01** limit-at=0Mbps max-limit=10Mbps。
- **Queue02** limit-at=4Mbps max-limit=10Mbps。
- **Queue03** limit-at=6Mbps max-limit=10Mbps priority=1。
- **Queue04** limit-at=2Mbps max-limit=10Mbps priority=3。
- **Queue05** limit-at=12Mbps max-limit=15Mbps priority=5。

#### 示例 4 的結果 {#result-of-example-4}

- **Queue03** 將獲得約 3Mbps。
- **Queue04** 將獲得約 1Mbps。
- **Queue05** 將獲得約 6Mbps。
- **說明：** 僅在滿足所有 **limit-at** 時，HTB 就被迫分配 20Mbps——6Mbps 給 **Queue03**、2Mbps 給 **Queue04**、12Mbps 給 **Queue05**，但我們的出介面只能處理 10Mbps。由於出介面佇列通常是 FIFO，吞吐量分配將保持 6:2:12 或 3:1:6 的比例。
