---
sidebar_key: "wireless/user-guides/wireless-station-modes"
sidebar_position: 2
title: "無線站點模式"
sidebar_label: "無線站點模式"
description: "本頁介紹 MikroTik RouterOS 無線 station 模式，說明它們在 L2 地址處理和橋接適用性方面的差異。內容涵蓋標準 station 模式、用於 WDS 連線的 station-wds 以及 pseudobridge 模式，幷包含適用性矩陣和協定支援詳情。"
tags:
  - 'station-modes'
  - 'l2-bridging'
  - 'wireless-protocols'
source: https://manual.mikrotik.com/docs/7.24/wireless/user-guides/wireless-station-modes
captured_at: '2026-11-04T11:35:40+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 概述 {#overview}

任何 *station* 模式下的無線介面都會搜尋可接受的接入點（AP）並連線到它。站點與 AP 之間的連線行為會因所使用的 *station* 模式型別而略有不同，因此必須針對給定應用和裝置選擇正確的模式。本文試圖描述可用 *station* 模式之間的差異。

*station* 模式之間的主要區別在於 L2 地址如何被處理並在無線鏈路上轉發。這直接影響無線鏈路作為 L2 橋接基礎設施一部分的能力。

如果不需要透過無線鏈路進行 L2 橋接——例如在路由或 MPLS 交換網路中——建議使用基本的 **mode=station** 設定，這將提供最高效率。

特定 *station* 模式的可用性取決於無線網路中使用的 **wireless-protocol** 以及已安裝的驅動程式（[`wireless` 或 `wifi-qcom`](../index.md#which-section-is-for-my-device)）。有關協定中模式支援的資訊，請參閱[適用性矩陣](#applicability-matrix)。即使給定協定不支援特定模式，站點與 AP 之間的連線仍有可能建立。請注意，此類連線在 L2 橋接方面的行為將不符合預期。

## 802.11 對 L2 橋接的限制 {#80211-limitations-for-l2-bridging}

歷史上，802.11 AP 裝置本應能夠在有線網段與無線之間橋接幀，但站點裝置本不應進行 L2 橋接。

考慮以下網路：

```
[X]---[AP]-(     )-[STA]---[Y]
```

其中 X-to-AP 和 STA-to-Y 是有線乙太網鏈路，但 AP-to-STA 是無線連線。根據 802.11，AP 可以透明地在 X 和 STA 之間橋接流量，但無法在 AP 和 Y 之間，或 X 和 Y 之間橋接流量。

802.11 標準規定，站點與 AP 裝置之間的幀必須以所謂的 *3 address* 幀格式傳輸，這意味著幀頭包含 3 個 MAC 地址。從 AP 傳輸到站點的幀具有以下地址：

- 目的地址——站點裝置的地址，也是無線電接收方地址；
- 無線電傳送方地址——AP 的地址；
- 源地址——特定幀的發起方地址。

從站點傳輸到 AP 的幀具有以下地址：

- 無線電接收方地址——AP 的地址；
- 源地址——站點裝置的地址，也是無線電傳送方地址；
- 目的地址。

考慮到每個幀都必須包含無線電傳送方和接收方地址，顯然 *3 address* 幀格式不適合在站點上進行透明 L2 橋接，因為站點無法傳送源地址不同於自身地址的幀（例如來自 Y 的幀），同時 AP 也無法以包含 Y 地址的方式構造幀。

802.11 還包含一種額外的幀格式，即所謂的 *4 address* 幀格式，用於“無線分佈系統”（WDS）——一種以無線方式互連 AP 的系統。在這種格式中會增加一個地址，從而生成包含以下地址的幀頭：

- 無線電接收方地址；
- 無線電傳送方地址；
- 目的地址；
- 源地址。

這種幀格式包含在無線鏈路上進行透明 L2 橋接所需的所有必要資訊。遺憾的是，802.11 未規定應如何建立和管理 WDS 連線，因此 *4 address* 幀格式（以及 WDS）的任何使用都取決於具體實現。

不同的 *station* 模式試圖解決標準 station 模式的缺點，以提供對 L2 橋接的支援。

## 適用性矩陣 {#applicability-matrix}

以下矩陣列出了每種受支援的無線協定和驅動程式可用的 *station* 模式。請注意，802.11 協定有 2 列：**802.11** 指定該模式在“純”802.11 網路中的可用性（連線到任何廠商的 AP 時），而 **ROS 802.11** 指定連線到實現了該模式正常工作所需專有擴充套件的 RouterOS AP 時的可用性。

*該表適用於 RouterOS v5rc11 及更高版本：*

|  | 802.11 | ROS 802.11 `wireless` | nstreme `wireless` | nv2 `wireless` | ROS 802.11 `wifi-qcom` |
| :-- | :-- | :-- | :-- | :-- |  :-- |
| **station** | V | V | V | V | V |
| **station-wds** |  | V | V | V | |
| **station-pseudobridge** | V | V | V |  | V |
| **station-pseudobridge-clone** | V | V | V |  | |
| **station-bridge** |  | V | V | V | V |

## *station* 模式 {#mode-station}

這是一種標準模式，不支援在站點上進行 L2 橋接——嘗試將無線介面加入網橋不會產生預期結果。另一方面，此模式可被視為最高效的模式，因此如果不需要在站點上進行 L2 橋接——例如在路由或 MPLS 交換網路中——就應使用此模式。所有無線協定均支援此模式。

## *station-wds* 模式 {#mode-station-wds}

此模式僅適用於 RouterOS AP。協商連線後，會在 AP 上為給定站點建立一個單獨的 WDS 介面。可以將此介面視為 AP 與給定站點之間的點對點連線——從 WDS 介面發出的任何內容都會交付給該站點（且僅交付給該特定站點），而站點發送給 AP 的任何內容都會從 WDS 介面接收（且不會在 AP 用戶端之間轉發），同時保留 L2 地址。

除連線到非 RouterOS 裝置時使用 802.11 協定的情況外，所有無線協定均支援此模式。與 802.11 協定一起使用時，此模式使用 *4 address* 幀格式；對於其他協定（如 nstreme 或 nv2），則使用協定內部機制。

此模式可安全用於 L2 橋接，並透過單獨的 WDS 介面在 AP 上提供最多的管理控制，例如使用網橋防火牆、用於環路檢測和避免的 RSTP 等。

在 station-wds 模式下，無法連線到由 CAPsMAN 控制的 CAP。

## *station-pseudobridge* 模式 {#mode-station-pseudobridge}

從無線連線的角度看，此模式與標準 station 模式相同。它透過站點中實現的某些服務提供有限的 L2 橋接支援：

- IPv4 封包的 MAC 地址轉換——站點維護 IPv4 到 MAC 的對映表，在向 AP 傳送幀時用自身地址替換源 MAC 地址（以便能夠使用 *3 address* 幀格式），並對從 AP 接收的幀用對映表中的地址替換目的 MAC 地址。對於 VLAN 封裝的幀，也會構建 IPv4 到 MAC 的對映。
- 對其餘協定進行單一 MAC 地址轉換——站點從第一個被轉發的非 IPv4 幀中學習源 MAC 地址，並將其用作反向轉換的預設地址——如果無法執行 IPv4 到 MAC 對映（例如非 IPv4 幀或缺少對映），則使用此 MAC 地址替換從 AP 接收的幀的目的 MAC 地址。

此模式僅限於透過單一 MAC 地址轉換將資料完整地 L2 橋接到連線到站點的一臺裝置，並對 IPv4 幀橋接提供一定支援——將非 IP 協定橋接到多臺裝置將無法工作。此外，MAC 地址轉換會將從 AP 側對站點裝置的訪問限制為基於 IPv4 的訪問——其餘協定將透過單一 MAC 地址轉換進行轉換，而不會由站點本身接收。

除 nv2 外，所有協定均可使用此模式，並且***應儘可能避免***。僅當 AP 不支援更好的 L2 橋接模式（例如使用非 RouterOS AP 時），或僅有一臺終端使用者裝置必須透過站點裝置連線到網路時，使用此模式才有正當理由。

## *station-pseudobridge-clone* 模式 {#mode-station-pseudobridge-clone}

此模式與 *station-pseudobridge* 模式相同，不同之處在於它使用“克隆”的 MAC 地址連線到 AP——該地址要麼是 **station-bridge-clone-mac** 引數中配置的地址（如果已配置），要麼是第一個被轉發幀的源地址。在 AP 看來，這實質上就像是連線到站點的一臺終端使用者裝置連線到了 AP。

## *station-bridge* 模式 {#mode-station-bridge}

此模式僅適用於 RouterOS AP，並在站點裝置上提供對與協定無關的透明 L2 橋接的支援。當使用 **bridge-mode** 引數啟用時，RouterOS AP 會接受處於 *station-bridge* 模式的用戶端。在此模式下，AP 維護一個轉發表，其中包含哪些 MAC 地址可透過哪個站點裝置到達的資訊。

此模式為 MikroTik 專有模式，不能用於連線到其他品牌的裝置。

此模式可安全用於 L2 橋接，並且是首選模式，除非有特定理由使用 *station-wds* 模式。在 station-bridge 模式下，無法連線到由 CAPsMAN 控制的 CAP。
