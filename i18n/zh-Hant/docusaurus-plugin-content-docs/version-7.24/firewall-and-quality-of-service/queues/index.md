---
sidebar_key: "firewall-and-quality-of-service/queues/index"
sidebar_position: 3
title: "佇列"
sidebar_label: "佇列"
description: "本頁介紹 MikroTik RouterOS 的佇列與頻寬管理，涵蓋 HTB、PCQ、burst 行為以及用於流量整形的佇列型別。文中說明了如何使用 `/queue/simple` 和 `/queue/tree` 配置簡單佇列與高階佇列，並詳細介紹了速率限制原理、CIR/MIR 的定義，以及有關佇列順序和目標匹配的注意事項。"
tags:
  - 'queues'
  - 'htb'
  - 'qos'
source: https://manual.mikrotik.com/docs/7.24/firewall-and-quality-of-service/queues
captured_at: '2026-11-04T11:28:19+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本節介紹 RouterOS 的佇列和頻寬管理。使用它來配置 HTB、PCQ、突發行為、佇列大小以及用於流量整形的佇列型別。

<DocCardList />

## 概述 {#overview}

佇列是一組封包，它們按照預定義的結構方法共同等待由網路裝置傳輸。排隊的工作方式幾乎與銀行或超市採用的方法相同，客戶根據到達順序接受服務。

佇列用於：

- 限制特定 IP 地址、子網、協定、埠等的資料速率。
- 限制點對點流量。
- 封包優先順序劃分。
- 配置流量突發以加速流量。
- 應用不同的基於時間的限制。
- 在使用者之間平均共享可用流量，或根據通道負載共享。

MikroTik RouterOS 中的佇列實現基於分層令牌桶（HTB）。HTB 允許建立分層佇列結構，並確定佇列之間的關係。這些分層結構可以附加在兩個不同位置。[封包流示意圖](../packet-flow-in-routeros.md) 說明了 *input* 和 *postrouting* 鏈。

在 RouterOS 中配置佇列有兩種不同方式：

- `/queue/simple` 選單 - 旨在簡化簡單的日常佇列任務（例如單個用戶端上傳/下載限制、p2p 流量限制等）的配置。
- `/queue/tree` 選單 - 用於實現高階佇列任務（例如全域性優先順序策略和 `/user/group` 限制）。需要來自 [`/ip/firewall/mangle`](../firewall/mangle.md) 功能的已標記封包流。

RouterOS 提供了在 8 個級別配置佇列的可能性 - 第一級是來自 `/queue/interface` 選單的介面佇列，其他 7 級是可在簡單佇列和/或佇列樹中建立的低級別佇列。

### 速率限制原則 {#rate-limitation-principles}

速率限制用於控制網路介面上傳送或接收的流量速率。速率小於或等於指定速率的流量會被髮送，而超過該速率的流量會被丟棄或延遲。

速率限制可以透過兩種方式執行：

1. 丟棄所有超過速率限制的封包 – ***速率限制（丟棄器或整形器）*** *（當 queue-size=0 時為 100% 速率限制器）*。
2. 將超過特定速率限制的封包在佇列中延遲，並在可能時傳輸它們 – ***速率均衡（排程器）***（當 *queue-size=unlimited* 時為 100% 速率均衡）。

下圖說明了*速率限制*和速率*均衡*之間的區別：

![](/img/d27732f6214ea1c4.webp)

如你所見，在第一種情況下，所有流量都超過特定速率並被丟棄。在另一種情況下，流量超過特定速率，在佇列中被延遲，並在可能時稍後傳輸，但請注意，只有在佇列未滿時封包才能被延遲。如果佇列緩衝區中沒有更多空間，封包將被丟棄。

對於每個佇列，我們可以定義兩個速率限制：

- **CIR**（承諾資訊速率）–（RouterOS 中的 **limit-at**）在最壞情況下，該流將獲得此數量的流量速率，而不管其他流量流如何。在任何給定時間，頻寬都不應低於此承諾速率。
- **MIR**（最大資訊速率）–（RouterOS 中的 **max-limit**）在最佳情況下，如果頻寬有任何空閒部分，該流可獲得的最大可用資料速率。

## 簡單佇列 {#simple-queue}

**子選單：** `/queue/simple`

簡單佇列是為特定目標限制流量的一種簡單方法。此外，你可以使用簡單佇列來構建高階 QoS 應用。它們具有有用的整合功能：

- 點對點流量排隊。
- 在選定的時間間隔應用佇列規則。
- 優先順序劃分。
- 使用來自 *`/ip/firewall/mangle`* 的多個數據包標記。
- 雙向流量的流量整形（排程）（對上傳 + 下載總量使用一個限制）。

:::warning
簡單佇列具有嚴格的順序 - 每個封包都必須經過每個佇列，直到到達某個條件符合封包引數的佇列，或者直到到達佇列列表末尾。例如，在有 1000 個佇列的情況下，發往最後一個佇列的封包需要經過 999 個佇列才能到達目的地。

:::

:::warning
簡單佇列目標基於 src 和 dst 地址匹配封包。如果 src 地址匹配目標，則為上傳；如果 dst 匹配目標，則為下載。但是，如果你的連線中 src 和 dst 都匹配目標，那麼此類封包將始終被計為下載，因為兩者都匹配 dst（對於兩個方向上的每個單獨封包），而在 RouterOS 中，這只是與目標比較的第一項。簡單佇列應配置為流量只能匹配 src 或 dst 地址，而不能同時匹配兩者。

:::

#### 流識別符號 {#flow-identifiers}

- **target**（多選：IP 地址/掩碼或介面）：**Target** 應從目標的角度來看待。如果你想限制使用者的上傳能力，請設定 "target upload"。

這兩個屬性中的每一個都可用於確定哪個方向是目標上傳，哪個是下載。請小心為同一個佇列配置這兩個選項 - 如果它們指向相反方向，佇列將無法工作。如果既未指定 **target** 的值，也未指定 **interface** 的值，佇列將無法區分上傳和下載，並且會對所有流量限制兩次。

#### 其他屬性 {#other-properties}

- **name**（文字）：唯一佇列識別符號，可用作其他佇列的 **parent** 選項值。
- **direction**（*both* | *upload* | *download*）：指定要限制的方向：
  - *both* - 限制下載和上傳流量。
  - *upload* - 僅限制發往目標的流量。
  - *download* - 僅限制來自目標的流量。
- **time**（*TIME-TIME,sun,mon,tue,wed,thu,fri,sat* - *TIME* 為本地時間，所有星期名稱都是可選的；預設：未設定）：允許你指定特定佇列處於活動狀態的時間。路由器必須具有正確的時間設定。
- **dst-address**（IP 地址/掩碼）：允許你僅選擇特定流（從目標地址到該目標地址）進行限制，說明什麼是 target、什麼是 dst、什麼是上傳、什麼不是。
- **packet-marks**（以逗號分隔的封包標記名稱列表）：允許使用來自 `/ip/firewall/mangle` 的已標記封包。請檢視 RouterOS [封包流示意圖](../packet-flow-in-routeros.md)。必須在簡單佇列之前（在 *global-in* HTB 佇列之前）標記封包，否則目標的下載限制將無法工作。*global-in* 之前唯一的 mangle 鏈是 *prerouting*。

#### HTB 屬性 {#htb-properties}

- **parent**（父簡單佇列的名稱，或 *none*）：將此佇列指定為所選目標的子佇列。目標佇列可以是 HTB 佇列或任何其他先前建立的簡單佇列。為了讓流量到達子佇列，父佇列必須捕獲所有必要的流量。
- **priority**（1..8）：將一個子佇列優先於另一個子佇列。在父佇列上不起作用（如果佇列至少有一個子佇列）。1 是最高優先順序，8 是最低優先順序。具有較高優先順序的子佇列將有機會比具有較低優先順序的子佇列先達到其 **max-limit**。優先順序與突發無關。
- **queue**（*SOMETHING/SOMETHING*）：選擇上傳/下載佇列的型別。佇列型別可以在 [`/queue/type`](#queue-types) 中建立。
- **limit-at**（*NUMBER/NUMBER*）：為目標保證的正常上傳/下載資料速率。
- **max-limit**（*NUMBER/NUMBER*）：允許目標達到的最大上傳/下載資料速率。
- **burst-limit**（*NUMBER/NUMBER*）：突發活動時可達到的最大上傳/下載資料速率。
- **burst-time**（*TIME/TIME*）：計算平均上傳/下載資料速率的時間段，以秒為單位。（這不是實際突發的時間）。
- **burst-threshold**（*NUMBER/NUMBER*）：當平均資料速率低於此值時 - 允許突發；一旦平均資料速率達到此值 - 拒絕突發。（基本上這是突發開/關開關）。為了獲得最佳突發行為，此值應高於 **limit-at** 值並低於 **max-limit** 值。

以及 *global-total* HTB 佇列的對應選項：

- **total-queue**（*SOMETHING/SOMETHING*）：對應於 **queue**。
- **total-limit-at**（*NUMBER/NUMBER*）：對應於 **limit-at**。
- **total-max-limit**（*NUMBER/NUMBER*）：對應於 **max-limit**。
- **total-burst-limit**（*NUMBER/NUMBER*）：對應於 **burst-limit**。
- **total-burst-time**（*TIME/TIME*）：對應於 **burst-time**。
- **total-burst-threshold**（*NUMBER/NUMBER*）：對應於 **burst-threshold**。

良好實踐建議：

子佇列的 limit-at 值之和必須小於或等於父佇列的 max-limit。每個子佇列的 max-limit 必須小於父佇列的 max-limit。這樣，你將把一些流量留給其他子佇列，它們將能夠獲得流量，而無需與其他子佇列爭奪。

#### 統計資訊 {#statistics}

- **rate**（只讀/只讀）：佇列平均透過資料速率，單位為位元組每秒。
- **packet-rate**（只讀/只讀）：佇列平均透過資料速率，單位為封包每秒。
- **bytes**（只讀/只讀）：此佇列處理的位元組數。
- **packets**（只讀/只讀）：此佇列處理的封包數。
- **queued-bytes**（只讀/只讀）：佇列中等待的位元組數。
- **queued-packets**（只讀/只讀）：佇列中等待的封包數。
- **dropped**（只讀/只讀）：丟棄的封包數。
- **borrows**（只讀/只讀）：超過其 "limit-at" 值透過佇列的封包（並且未被使用並從其他佇列取走）。
- **lends**（只讀/只讀）：低於其 "limit-at" 值透過佇列的封包，或者如果佇列是父佇列 - 所有子佇列借用封包的總和。
- **pcq-queues**（只讀/只讀）：如果佇列型別為 PCQ，則為 PCQ 子流的數量。

以及 *global-total* HTB 佇列的對應選項：

- **total-rate**（只讀）：對應於 *rate*。
- **total-packet-rate**（只讀）：對應於 *packet-rate*。
- **total-bytes**（只讀）：對應於 *bytes*。
- **total-packets**（只讀）：對應於 *packets*。
- **total-queued-bytes**（只讀）：對應於 *queued-bytes*。
- **total-queued-packets**（只讀）：對應於 *queued-packets*。
- **total-dropped**（只讀）：對應於 *dropped*。
- **total-lends**（只讀）：對應於 *lends*。
- **total-borrows**（只讀）：對應於 *borrows*。
- **total-pcq-queues**（只讀）：對應於 *pcq-queues*。

### 配置示例 {#configuration-example}

在以下示例中，我們有一臺 SOHO 裝置，連線了兩臺裝置：PC 和伺服器。

![](/img/df7f01e5e41c5241.jpg)

在此情況下，我們有一條來自 ISP 的 15 Mbps 連線可用。我們希望確保伺服器收到足夠的流量，因此我們將配置一個帶有 *limit-at* 引數的簡單佇列，以保證伺服器獲得 5Mbps：

```ros
/queue/simple
add limit-at=5M/5M max-limit=15M/15M name=queue1 target=192.168.88.251/32
```

就是這樣。無論其他流量流如何，伺服器都將獲得 5 Mbps 的流量速率。如果你使用的是預設配置，請確保針對此特定流量停用了 FastTrack 規則，否則它將繞過簡單佇列，簡單佇列將無法工作。

## 佇列樹 {#queue-tree}

**子選單：** `/queue/tree`

佇列樹僅在其中一個 HTB 中建立單向佇列。它也是在單獨介面上新增佇列的唯一方法。這樣可以簡化 mangle 配置 - 你不需要為下載和上傳分別設定標記 - 只有上傳流量會到達 Public 介面，只有下載流量會到達 Private 介面。與簡單佇列的主要區別在於，佇列樹不是有序的 - 所有流量一起透過它。

### 配置示例 {#configuration-example-1}

在以下示例中，我們將標記來自預配置的 *in-interface-list=LAN* 的所有封包，並基於這些封包標記使用佇列樹限制流量。

讓我們建立防火牆地址列表：

```ros
[admin@MikroTik] > /ip/firewall/address-list
add address=www.youtube.com list=Youtube
[admin@MikroTik] > ip firewall address-list print
Flags: X - disabled, D - dynamic 
 #   LIST                                                       ADDRESS                                                                        CREATION-TIME        TIMEOUT             
 0   Youtube                                                    www.youtube.com                                                                2019-10-17 14:47:11
 1 D ;;; www.youtube.com
     Youtube                                                    216.58.211.14                                                                  2019-10-17 14:47:11
 2 D ;;; www.youtube.com
     Youtube                                                    216.58.207.238                                                                 2019-10-17 14:47:11
 3 D ;;; www.youtube.com
     Youtube                                                    216.58.207.206                                                                 2019-10-17 14:47:11
 4 D ;;; www.youtube.com
     Youtube                                                    172.217.21.174                                                                 2019-10-17 14:47:11
 5 D ;;; www.youtube.com
     Youtube                                                    216.58.211.142                                                                 2019-10-17 14:47:11
 6 D ;;; www.youtube.com
     Youtube                                                    172.217.22.174                                                                 2019-10-17 14:47:21
 7 D ;;; www.youtube.com
     Youtube                                                    172.217.21.142                                                                 2019-10-17 14:52:21

```

使用防火牆 mangle 功能標記封包：

```ros
[admin@MikroTik] > /ip/firewall/mangle
add action=mark-packet chain=forward dst-address-list=Youtube in-interface-list=LAN new-packet-mark=pmark-Youtube passthrough=yes
```

基於先前標記的封包配置佇列樹：

```ros
[admin@MikroTik] /queue/tree
add max-limit=5M name=Limiting-Youtube packet-mark=pmark-Youtube parent=global
```

檢查佇列樹統計資訊以確保流量已匹配：

```ros
[admin@MikroTik] > queue tree print stats
Flags: X - disabled, I - invalid 
 0   name="Limiting-Youtube" parent=global packet-mark=pmark-Youtube rate=0 packet-rate=0 queued-bytes=0 queued-packets=0 bytes=67887 packets=355 dropped=0 
```

## 佇列型別 {#queue-types}

**子選單：** `/queue/type`

此子選單列出預設建立的佇列型別，並允許新增新的使用者特定型別。

預設情況下，RouterOS 建立以下預定義佇列型別：

```ros
[admin@MikroTik] > /queue/type/print
Flags: * - default 
 0 * name="default" kind=pfifo pfifo-limit=50 

 1 * name="ethernet-default" kind=pfifo pfifo-limit=50 

 2 * name="wireless-default" kind=sfq sfq-perturb=5 sfq-allot=1514 

 3 * name="synchronous-default" kind=red red-limit=60 red-min-threshold=10 red-max-threshold=50 red-burst=20 red-avg-packet=1000 

 4 * name="hotspot-default" kind=sfq sfq-perturb=5 sfq-allot=1514 

 5 * name="pcq-upload-default" kind=pcq pcq-rate=0 pcq-limit=50KiB pcq-classifier=src-address pcq-total-limit=2000KiB pcq-burst-rate=0 pcq-burst-threshold=0 pcq-burst-time=10s pcq-src-address-mask=32 
     pcq-dst-address-mask=32 pcq-src-address6-mask=128 pcq-dst-address6-mask=128 

 6 * name="pcq-download-default" kind=pcq pcq-rate=0 pcq-limit=50KiB pcq-classifier=dst-address pcq-total-limit=2000KiB pcq-burst-rate=0 pcq-burst-threshold=0 pcq-burst-time=10s pcq-src-address-mask=32 
     pcq-dst-address-mask=32 pcq-src-address6-mask=128 pcq-dst-address6-mask=128 

 7 * name="only-hardware-queue" kind=none 

 8 * name="multi-queue-ethernet-default" kind=mq-pfifo mq-pfifo-limit=50 

 9 * name="default-small" kind=pfifo pfifo-limit=10
```

所有 MikroTik 產品都有預設佇列型別 "**only-hardware-queue"**，其 "kind=none"。 "only-hardware-queue" 使介面僅保留一個硬體傳送描述符環形緩衝區，該緩衝區本身充當佇列。通常，傳送描述符環形緩衝區中至少可以排隊 100 個數據包用於傳送。傳送描述符環形緩衝區的大小以及其中可排隊的封包數量因不同型別的乙太網 MAC 而異。沒有軟體佇列在 SMP 系統上尤其有益，因為它消除了從不同 CPU/核心同步訪問它的需求，而這是資源密集型的。能夠設定 "only-hardware-queue" 需要乙太網驅動程式的支援，因此僅適用於某些乙太網介面，這些介面主要見於 RouterBOARD。

**"multi-queue-ethernet-default"** 在具有支援多個傳送佇列的乙太網介面並且具有 Linux 驅動程式對多個傳送佇列支援的 SMP 系統上可能是有益的。透過為每個硬體佇列設定一個軟體佇列，花在同步訪問它們上的時間可能會更少。

:::warning
僅當沒有以特定介面作為父級的 `/queue/tree` 條目時，only-hardware-queue 和 multi-queue-ethernet-default 帶來的改進才會存在。

:::

### 種類 {#kinds}

佇列種類是封包處理演算法。種類描述接下來將按順序傳輸哪一個封包。RouterOS 支援以下排隊種類：

- FIFO（BFIFO、PFIFO、MQ PFIFO）
- RED
- SFQ
- PCQ

#### FIFO {#fifo}

這些種類基於 FIFO 演算法（先進先出）。**PFIFO** 和 **BFIFO** 的區別在於一個以封包為單位衡量，另一個以位元組為單位衡量。這些佇列使用 **pfifo-limit** 和 **bfifo-limit** 引數。

每個無法入隊的封包（如果佇列已滿）都會被丟棄。較大的佇列大小會增加延遲，但能更好地利用通道。

**MQ-PFIFO** 是支援多個傳送佇列的 *pfifo*。此佇列在具有支援多個傳送佇列的乙太網介面並且具有 Linux 驅動程式對多個傳送佇列支援（主要是在 x86 平臺上）的 SMP 系統上是有益的。此種類使用 **mq-pfifo-limit** 引數。

#### RED {#red}

隨機早期丟棄是一種排隊機制，它透過控制平均佇列大小來嘗試避免網路擁塞。平均佇列大小與兩個閾值進行比較：最小閾值（min<sub>th</sub>）和最大閾值（max<sub>th</sub>）。如果平均佇列大小（avg<sub>q</sub>）小於最小閾值，則不丟棄任何封包。當平均佇列大小大於最大閾值時，所有傳入封包都會被丟棄。但如果平均佇列大小介於最小閾值和最大閾值之間，封包將以機率 P<sub>d</sub> 被隨機丟棄，其中機率恰好是平均佇列大小的函式：P<sub>d</sub> = P<sub>max</sub>(avg<sub>q</sub> – min<sub>th</sub>)/ (max<sub>th</sub> - min<sub>th</sub>)。如果平均佇列增長，丟棄傳入封包的機率也會增長。P<sub>max</sub> 是一個比率，可以調整封包丟棄機率的突變程度（最簡單的情況下 P<sub>max</sub> 可以等於 1）。8.2 圖顯示了 RED 演算法中的封包丟棄機率。

![](/img/70b89eafe9395bb5.webp)

#### SFQ {#sfq}

隨機公平排隊（SFQ）透過雜湊和輪詢演算法來保證。SFQ 之所以稱為 "Stochastic"，是因為它實際上並不為每個流分配佇列；它有一個演算法，使用雜湊演算法將流量分配到有限數量的佇列（1024）上。

流量流可以透過 4 個選項（*src-address、dst-address、src-port* 和 *dst-port*）唯一標識，因此 SFQ 雜湊演算法使用這些引數將封包分類到 1024 個可能子流之一。然後，輪詢演算法將開始向所有子流分配可用頻寬，每輪給予 **sfq-allot** 位元組的流量。整個 SFQ 佇列可以包含 128 個數據包，並且有 1024 個子流可用。8.3 圖顯示了 SFQ 操作：

![](/img/d7a57b8def263041.webp)

#### PCQ {#pcq}

PCQ 演算法非常簡單 - 首先，它使用選定的分類器將一個子流與另一個子流區分開，然後對每個子流應用單獨的 FIFO 佇列大小和限制，然後將所有子流組合在一起，並應用全域性佇列大小和限制。

PCQ 引數：

- **pcq-classifier**（dst-address | dst-port | src-address | src-port；預設：""）：子流識別符號的選擇。
- **pcq-rate**（數字）：每個子流的最大可用資料速率。
- **pcq-limit**（數字）：單個子流的佇列大小（以 KiB 為單位）。
- **pcq-total-limit**（數字）：所有子流中排隊資料的最大量（以 KiB 為單位）。

 可以透過 **pcq-rate** 選項為子流分配速度限制。如果 "pcq-rate=0"，子流將平均分配可用流量。

![](/img/9063cae055390196.webp)

例如，與其有 100 個下載限制為 1000kbps 的佇列，我們可以有一個包含 100 個子流的 PCQ 佇列。

PCQ 具有與簡單佇列和佇列樹相同的突發實現：

- **pcq-burst-rate**（數字）：當允許子流突發時可達到的最大上傳/下載資料速率。
- **pcq-burst-threshold**（數字）：這是突發開/關開關的值。
- **pcq-burst-time**（時間）：計算平均資料速率的時間段（以秒為單位）。（這不是實際突發的時間）。

PCQ 還允許使用不同大小的 IPv4 和 IPv6 網路作為子流識別符號。以前它被鎖定為單個 IP 地址。這樣做主要是為了 IPv6，因為從 ISP 的角度來看，客戶將由 /64 網路表示，但客戶網路中的裝置將是 /128。PCQ 可用於這兩種場景以及更多場景。PCQ 引數：

- **pcq-dst-address-mask**（數字）：將用作 dst-address 子流識別符號的 IPv4 網路大小。
- **pcq-src-address-mask**（數字）：將用作 src-address 子流識別符號的 IPv4 網路大小。
- **pcq-dst-address6-mask**（數字）：將用作 dst-address 子流識別符號的 IPv6 網路大小。
- **pcq-src-address6-mask**（數字）：將用作 src-address 子流識別符號的 IPv6 網路大小。

:::info
以下佇列種類 CoDel、FQ-Codel 和 CAKE 自 RouterOS 版本 7.1beta3 起可用。

:::

#### CoDel {#codel}

CoDel（受控延遲主動佇列管理）演算法使用本地最小佇列作為持久佇列的度量；類似地，它使用最小延遲引數作為常駐佇列延遲的度量。佇列大小使用封包在佇列中的駐留時間計算。

**屬性**

| **屬性** | **描述** |
| :-- | :-- |
| **codel-ce-threshold** (*預設*: ) | 使用 ECN 標記超過配置閾值的封包。 |
| **codel-ecn** (*預設*: **no**) | 該選項用於標記封包而不是丟棄它們。 |
| **codel-interval** (*預設*: **100ms**) | 間隔應設定為透過瓶頸的最壞情況 RTT 的數量級，以便端點有足夠的時間做出反應。 |
| **codel-limit** (*預設*: **1000**) | 佇列限制。達到限制時，傳入封包會被丟棄。 |
| **codel-target** (*預設*: **5ms**) | 表示可接受的最小持久佇列延遲。 |

#### FQ-Codel {#fq-codel}

CoDel - 帶受控延遲（CoDel）的公平排隊（FQ）使用隨機確定的模型將傳入封包分類到不同流中，並用於為使用該佇列的所有流提供公平的頻寬份額。每個流都使用 CoDel 排隊規則進行管理，該規則內部使用 FIFO 演算法。

**屬性**

| **屬性** | **描述** |
| :-- | :-- |
| **fq-codel-ce-threshold** (*預設*: ) | 使用 ECN 標記超過配置閾值的封包。 |
| **fq-codel-ecn** (*預設*: **yes**) | 該選項用於標記封包而不是丟棄它們。 |
| **fq-codel-flows** (預設: **1024**) | 傳入封包被分類到的流數量。 |
| **fq-codel-interval** (*預設*: **100ms**) | 間隔應設定為透過瓶頸的最壞情況 RTT 的數量級，以便端點有足夠的時間做出反應。 |
| **fq-codel-limit** (*預設*: **10240**) | 佇列限制。達到限制時，傳入封包會被丟棄。 |
| **fq-codel-memlimit** (預設: **32.0MiB**) | 可在此 FQ-CoDel 例項中排隊的總位元組數。將從 *fq-codel-limit* 引數強制執行。 |
| **fq-codel-quantum** (*預設*: **1514**) | 公平排隊演算法中用作“赤字”的位元組數。預設值（1514 位元組）對應於乙太網 MTU 加上 14 位元組的硬體頭長度。 |
| **fq-codel-target** (*預設*: **5ms**) | 表示可接受的最小持久佇列延遲。 |

#### CAKE {#cake}

CAKE - Common Applications Kept Enhanced（CAKE）被實現為 Linux 核心的*佇列規則*（qdisc），它使用 COBALT（結合 Codel 和 BLUE 的 AQM 演算法）以及 DRR++ 的變體來進行流隔離。換句話說，Cake 的基本設計目標是使用者友好性。所有設定都是可選的；預設設定被選擇為在大多數常見部署中實用。在大多數情況下，配置僅需要一個頻寬引數即可獲得有用的結果。

**屬性**

| **屬性** | **描述** |
| :-- | :-- |
| **cake-ack-filter** *(預設:* **none** ) |  |
| **cake-atm** *(預設:* ) | 補償 ATM 信元成幀，這通常見於 ADSL 鏈路。 |
| **cake-autorate-ingress** *(yes/no, 預設:* ) | 基於到達此 qdisc 的流量進行自動容量估計。這在蜂窩鏈路上最可能有用，因為蜂窩鏈路的質量往往會隨機變化。 頻寬限制引數可以與其一起使用，以指定初始估計值。整形器將定期設定為略低於估計速率的頻寬。 此估計器無法估計其下游鏈路的頻寬。 |
| **cake-bandwidth** *(預設:* ) | 設定整形器頻寬。 |
| **cake-diffserv** *(預設:* **diffserv3**) | CAKE 可以根據 Diffserv 欄位將流量劃分為“tin”：diffserv4 提供具有四個 tin 的通用 Diffserv 實現：Bulk（CS1），6.25% 閾值，通常為低優先順序。Best Effort（general），100% 閾值。Video（AF4x、AF3x、CS3、AF2x、CS2、TOS4、TOS1），50% 閾值。Voice（CS7、CS6、EF、VA、CS5、CS4），25% 閾值。diffserv3（預設）提供具有三個 tin 的簡單通用 Diffserv 實現：Bulk（CS1），6.25% 閾值，通常為低優先順序。Best Effort（general），100% 閾值。Voice（CS7、CS6、EF、VA、TOS4），25% 閾值，縮短的 Codel 間隔。 |
| **cake-flowmode** *(dsthost/dual-dsthost/dual-srchost/flowblind/flows/hosts/srchost/triple-isolate, 預設:* **triple-isolate**) | flowblind - 停用流隔離；所有流量都透過每個 tin 的單個佇列。srchost - 流僅由源地址定義。 dsthost 流僅由目的地址定義。 hosts - 流由源-目的主機對定義。這是主機隔離，而不是流隔離。flows - 流由源地址、目的地址、傳輸協定、源埠和目的埠組成的整個 5 元組定義。這是 SFQ 和 fq_codel 執行的流隔離型別。dual-srchost 流由 5 元組定義，公平性首先應用於源地址，然後應用於各個流。適用於從 LAN 到 Internet 的出站流量，無論 LAN 主機使用多少流，它都能防止任何 LAN 主機獨佔上行鏈路。dual-dsthost 流由 5 元組定義，公平性首先應用於目的地址，然後應用於各個流。適用於從 Internet 到 LAN 的入站流量，無論 LAN 主機使用多少流，它都能防止任何 LAN 主機獨佔下行鏈路。triple-isolate - 流由 5 元組定義，公平性會智慧地應用於源*和*目的地址（即不只是按主機對），並且也應用於各個流。nat 指示 Cake 在應用流隔離規則之前執行 NAT 查詢，以確定封包的真實地址和埠號，從而提高 NAT “內部”主機之間的公平性。這在 "flowblind" 或 "flows" 模式下，或者如果 NAT 在不同主機上執行時，沒有實際效果。nonat（預設）Cake 將不執行 NAT 查詢。將使用 Cake 所連線介面直接可見的地址和埠號來執行流隔離。 |
| **cake-memlimit** *(預設:* ) | 將 Cake 消耗的記憶體限制為 LIMIT 位元組。預設情況下，該限制根據頻寬和 RTT 設定計算。 |
| **cake-mpu** *( -64 ... 256, 預設:* ) | 將每個封包（包括開銷）向上舍入到最小長度 BYTES。 |
| **cake-nat** *(預設:* **no)** | 指示 Cake 在應用流隔離規則之前執行 NAT 查詢。 |
| **cake-overhead** *( -64 ... 256, 預設:* ) | 將 BYTES 新增到每個封包的大小。BYTES 可以為負。 |
| **cake-overhead-scheme** *(預設:* ) |  |
| **cake-rtt** *(預設:* **100ms** ) | 手動指定 RTT。預設值 100ms 適用於大多數 Internet 流量。 |
| **cake-rtt-scheme** *(datacentre/internet/interplanetary/lan/metro/none/oceanic/regional/satellite, 預設:* ) | datacentre - 僅用於極高效能的 10GigE+ 網路。相當於 RTT 100us。lan - 用於家庭或辦公室中的純乙太網（非 Wi-Fi）網路。在為 Internet 接入鏈路進行整形時不要使用此項。相當於 RTT 1ms。metro - 用於主要位於單個城市內的流量。相當於 RTT 10ms。 regional 用於主要位於歐洲國家範圍內的流量。相當於 RTT 30ms。internet（預設）適用於大多數 Internet 流量。相當於 RTT 100ms。oceanic - 用於通常延遲高於平均值的 Internet 流量，例如澳大拉西亞居民所經歷的延遲。相當於 RTT 300ms。satellite - 用於透過地球靜止衛星的流量。相當於 RTT 1000ms。interplanetary - 如此命名是因為木星距離地球約 1 光時。使用此項可（幾乎）完全停用 AQM 操作。相當於 RTT 3600s。 |
| **cake-wash** *(預設:* **no** ) | 在優先順序排隊發生之後，應用 wash 選項清除所有額外的 DiffServ（但不包括 ECN 位）。 |

## 介面佇列 {#interface-queue}

**子選單：** `/queue/interface`

在透過介面傳送資料之前，資料會由佇列處理。此子選單列出 RouterOS 中所有可用介面，並允許更改特定介面的佇列型別。該列表是自動生成的。

```ros
[admin@MikroTik] > /queue/interface/print
Columns: INTERFACE, QUEUE, ACTIVE-QUEUE
# INTERFACE QUEUE ACTIVE-QUEUE
0 ether1 only-hardware-queue only-hardware-queue
1 ether2 only-hardware-queue only-hardware-queue
2 ether3 only-hardware-queue only-hardware-queue
3 ether4 only-hardware-queue only-hardware-queue
4 ether5 only-hardware-queue only-hardware-queue
5 ether6 only-hardware-queue only-hardware-queue
6 ether7 only-hardware-queue only-hardware-queue
7 ether8 only-hardware-queue only-hardware-queue
8 ether9 only-hardware-queue only-hardware-queue
9 ether10 only-hardware-queue only-hardware-queue
10 sfp-sfpplus1 only-hardware-queue only-hardware-queue
11 wlan1 wireless-default wireless-default
12 wlan2 wireless-default wireless-default 
```

## GUI 中的佇列負載視覺化 {#queue-load-visualization-in-gui}

在 Winbox 和 Webfig 中，綠色、黃色或紅色圖示會根據 max-limit 視覺化每個簡單佇列和佇列樹的使用情況。

|  |  |
| :-- | :-- |
| ![](/img/1f52670cd4d93071.png)  | 已使用 max-limit 的 0% - 50% |
| ![](/img/f8e7c3da41d98ac0.png)  | 已使用 max-limit 的 >50% - 75% |
| ![](/img/30756a75a5193bf3.png)  | 已使用 max-limit 的 >75% - 100% |
