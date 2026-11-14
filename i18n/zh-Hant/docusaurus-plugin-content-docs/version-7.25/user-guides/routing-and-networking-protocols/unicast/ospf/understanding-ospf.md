---
sidebar_key: "routing-and-networking-protocols/unicast/ospf/understanding-ospf"
sidebar_position: 1
title: "理解 OSPF"
sidebar_label: "理解 OSPF"
description: "OSPF 協定基礎知識概述。"
tags:
  - 'routing'
  - 'ospf'
slug: /user-guides/routing-and-networking-protocols/unicast/ospf/understanding-ospf
source: https://manual.mikrotik.com/docs/7.25/user-guides/routing-and-networking-protocols/unicast/ospf/understanding-ospf
captured_at: '2026-11-04T11:22:53+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

OSPF 是一種內部閘道器協定（IGP），用於在同一自治系統（AS）中的路由器之間分發路由資訊。

該協定基於鏈路狀態技術，與 RIP 等距離向量協定相比具有多項優勢：

- 不存在跳數限制。
- 使用組播地址傳送路由資訊更新。
- 僅當網路拓撲發生變化時才傳送更新。
- 透過將路由器劃分為區域，以邏輯方式定義網路。
- 注入 AS 的外部路由會被傳遞並標記。

但是，OSPF 也有一些缺點：

- OSPF 對 CPU 和記憶體消耗較大，因為 SPF 演算法必須維護多份路由資訊副本。
- 實現起來比 RIP 更復雜。

## 術語 {#terminology}

請檢視以下術語以瞭解 OSPF 的工作方式。你將在整個文件中遇到這些術語。

- **鄰居**：執行 OSPF 且相鄰介面分配到同一區域的已連線（鄰接）路由器。除非手動配置鄰居，否則 Hello 封包會發現鄰居。
- **鄰接關係**：路由器與其對應 DR 和 BDR 之間的邏輯連線。除非形成鄰接關係，否則路由器不會交換路由資訊。
- **鏈路**：分配到任意給定網路的路由器介面或網路。
- **介面**：路由器上的物理介面。當將介面新增到 OSPF 後，它將成為用於構建鏈路資料庫的鏈路。
- **LSA**：鏈路狀態通告（Link State Advertisement），一種包含鏈路狀態和路由資訊的封包，在 OSPF 鄰居之間共享。
- **DR**：指定路由器（Designated Router），為最小化形成的鄰接關係數量而選擇的路由器。OSPF 在廣播網路中使用此選項。
- **BDR**：備用指定路由器（Backup Designated Router），DR 的熱備份。BDR 接收來自相鄰路由器的所有路由更新，但不泛洪 LSA 更新。
- **[區域](./areas-and-virtual-links.md)**：用於建立分層網路的邏輯分組。
- **ABR**：區域邊界路由器（Area Border Router），連線到多個區域的路由器。ABR 負責所連線區域之間的彙總和更新抑制。
- **ASBR**：自治系統邊界路由器（Autonomous System Boundary Router），連線到外部網路（位於不同 AS 中）的路由器。當在該路由器上將來自其他協定的路由匯入 OSPF 時，該路由器就成為 ASBR。
- **NBMA**：非廣播多路訪問網路（Non-broadcast multi-access networks）。這些網路允許多路訪問，但不具備廣播能力。必須在此類網路上手動配置 OSPF 鄰居。
- **廣播**：具備廣播能力的網路。例如，乙太網。
- **點對點**：不需要 DR 和 BDR 的網路型別。
- **Router-ID**：用於標識 OSPF 路由器的 IP 地址。如果未手動配置 OSPF [`router-id`](../../../../cli-reference/routing/ospf/instance.md#router-id)，則路由器會使用其已分配的某個 IP 地址作為 Router-ID。
- **鏈路狀態**：兩臺路由器之間鏈路的狀態。它定義了路由器介面與其相鄰路由器之間的關係。
- **開銷**：鏈路狀態協定為每條鏈路分配的值。[`cost`](../../../../cli-reference/routing/ospf/interface-template.md#cost) 值取決於介質速度。每個路由器介面在其輸出側都有一個關聯開銷，稱為介面輸出開銷。
- **自治系統**：一組使用共同路由協定交換路由資訊的路由器。

## 支援的標準 {#supported-standards}

- RFC [2328](https://tools.ietf.org/html/rfc2328) - OSPF 版本 2
- RFC [3101](https://tools.ietf.org/html/rfc3101) - OSPF 非完全末梢區域（NSSA）選項
- RFC [3630](https://tools.ietf.org/html/rfc3630) - OSPF 版本 2 的流量工程（TE）擴充套件
- RFC [4577](https://tools.ietf.org/html/rfc4577) - OSPF 作為 BGP/MPLS IP 虛擬專用網路（VPN）的提供商/客戶邊緣協定
- RFC [5329](https://tools.ietf.org/html/rfc5329) - OSPF 版本 3 的流量工程擴充套件
- RFC [5340](https://tools.ietf.org/html/rfc5340) - 用於 IPv6 的 OSPF
- RFC [5643](https://tools.ietf.org/html/rfc5643) - OSPFv3 管理資訊庫
- RFC [6549](https://tools.ietf.org/html/rfc6549) - OSPFv2 多例項擴充套件
- RFC [6565](https://tools.ietf.org/html/rfc6565) - OSPFv3 作為提供商邊緣到客戶邊緣（PE-CE）路由協定
- RFC [6845](https://tools.ietf.org/html/rfc6845) - OSPF 混合廣播和點對多點介面型別
- RFC [7471](https://tools.ietf.org/html/rfc7471) - OSPF 流量工程（TE）度量擴充套件
