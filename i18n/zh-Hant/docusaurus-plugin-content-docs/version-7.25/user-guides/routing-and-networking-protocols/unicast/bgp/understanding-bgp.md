---
sidebar_key: "routing-and-networking-protocols/unicast/bgp/understanding-bgp"
sidebar_position: 1
title: "理解 BGP"
sidebar_label: "理解 BGP"
description: "BGP 協定基礎概述。"
tags:
  - 'routing'
  - 'bgp'
slug: /user-guides/routing-and-networking-protocols/unicast/bgp/understanding-bgp
source: https://manual.mikrotik.com/docs/7.25/user-guides/routing-and-networking-protocols/unicast/bgp/understanding-bgp
captured_at: '2026-11-04T11:22:45+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

**邊界閘道器協定**（**BGP**）是一種外部閘道器協定（**EGP**）。它可用於建立域間動態路由系統。當網路拓撲發生變化時，該系統會自動更新 BGP 路由器上的路由表。

BGP 是一種基於**路徑向量**演算法的自治系統間路由協定。它在整個網際網路範圍內交換路由資訊，是唯一為在網際網路規模下執行並處理與不相關路由域之間的多條連線而設計的協定。

BGP 的設計目標是讓管理員能夠實施精細的路由策略。它交換的不是網路拓撲資訊，而是可達性資訊。因此，BGP 更適合 **inter-AS** 環境以及資訊饋送之類的特殊場景。如果需要在網路中啟用動態路由，請改用 OSPF。

:::info
SMIPS 裝置（hAP lite、hAP lite TC 和 hAP mini）不支援 BGP。
:::

## 術語 {#terminology}

- **AS** - 自治系統（Autonomous System），指由單一技術管理機構管理、具有共同度量集合的一組路由器。
- **ASN** - 自治系統號（Autonomous System Number），是自治系統的唯一識別符號。ASN 可以是私有或公有的。公有 ASN 在全球範圍內唯一，由 RIPE 等監管機構分配。
- **AS Path** - 路由所經過的自治系統序列。
- **Path Attributes** - 包含有關 AS 路徑的附加資訊，用於路由策略。
- **Routing policy** - 一組規則，用於控制路由資訊的重分發，並在多條可用路徑中選擇最佳路徑。
- **NLRI** - 網路層可達性資訊（Network Layer Reachability Information），是在 BGP 對等體之間交換的內容，表示如何到達各個字首。
- **IGP** - 內部閘道器協定，例如 OSPF 或 ISIS。
- **EGP** - 外部閘道器協定，例如 BGP。
- **RR** - 路由反射器（route reflector），是一種在 **iBGP** 發言者之間反射路由資訊的 BGP 路由器，可免除全互聯連線的需求。
- **Route server** - 不參與流量轉發的 BGP 路由器。此類路由通常甚至不會被安裝到 FIB 中。
- **Loopback address** - 配置在可作為環回介面的 dummy bridge 介面上的 /32（IPv4）或 /128（IPv6）地址。

BGP 連線有兩種型別：

- **iBGP** - 連線同一 AS 中對等體的“內部”鏈路。
- **eBGP** - 連線屬於兩個不同 AS 的對等體的“外部”鏈路。

## 協定基礎 {#protocol-basics}

BGP 路由器藉助傳輸協定交換可達性資訊；就 BGP 而言，該協定是 TCP（埠 179）。在建立 TCP 連線後，這些路由器交換 **OPEN** 訊息，以協商並確認雙方支援的能力。

在就能使用的功能達成一致後，會話即被視為**已建立**，對等體可以開始透過 **UPDATE** 訊息交換 NLRI。這些訊息指明瞭路由到達目標網路（NLRI 字首）所應經過的 AS 序列（AS Path）。

對等體最初會交換各自完整的路由表，在初始交換之後，隨著路由表變化，會發送增量更新。因此，BGP 不需要對整個 BGP 路由表進行週期性重新整理。

BGP 維護路由表版本號，在連線存續期間，任意兩個給定對等體之間的該版本號必須相同。

**KEEPALIVE** 訊息會被定期傳送，以確保連線處於正常執行狀態。如果在 **Hold Time** 間隔內未收到這些訊息，連線將關閉。

為響應錯誤或特殊情況，可以生成 **NOTIFICATION** 訊息併發送給遠端對等體；該訊息型別同時也指示連線是否應立即關閉。

一個 AS 可能擁有多個 BGP 發言者，併為其 AS 提供中轉服務。這意味著 BGP 發言者必須在 AS 內部保持一致的路由檢視。為保證 AS 外部路由檢視的一致性，AS 內的所有 BGP 路由器彼此之間建立直接的 **iBGP** 連線（全互聯），或者採用**路由反射器**方案。

藉助一組管理策略（路由策略），AS 內的 BGP 發言者就特定目的地應使用哪個入口或出口點達成一致。該資訊透過內部路由協定（**IGP**，例如 OSPF、RIP 或靜態路由）傳達給 AS 的內部路由器。在某些部署中，iBGP 也可以承擔 IGP 協定的角色。

對於某些 BGP 屬性，其處理行為可能因連線型別而異；例如，**LOCAL-PREF** 屬性不會通告給 **eBGP** 對等體。

RouterOS 將配置和會話監控劃分為四個選單：

- instance 選單（[`/routing/bgp/instance`](../../../../cli-reference/routing/bgp/instance.md)）
- connection 選單（[`/routing/bgp/connection`](../../../../cli-reference/routing/bgp/connection.md)）
- sessions 選單（[`/routing/bgp/session`](../../../../cli-reference/routing/bgp/session/index.md)）
- template 選單（[`/routing/bgp/template`](../../../../cli-reference/routing/bgp/template.md)）

## 路由來源 {#route-origin}

首先通告某條路由的 BGP 路由器會為其指定來源，並將其寫入 **ORIGIN** 屬性。  
共有三種來源型別：

- 0 - 路由器最初是透過 **IGP** 學到該路由的。如果路由是透過 BGP [`output.network`](../../../../cli-reference/routing/bgp/connection.md#output.network) 學到的，RouterOS 會賦予該值。
- 1 - 路由器最初是透過 **EGP** 學到該路由的。
- 2 - 來源未知/不完整。如果路由是透過 BGP [`output.redistribute`](../../../../cli-reference/routing/bgp/connection.md#output.redistribute) 學到的，RouterOS 會賦予該值。

## 最佳路徑選擇 {#best-path-selection}

BGP 路由器可以從多個提供商處收到全域性路由表的多份副本，但預設情況下 BGP 只能有一條最佳路徑。為選出最佳路由，BGP 使用**最佳路徑選擇演算法**。

僅當路由有效時，演算法才會對其進行評估。一般來說，滿足以下條件時路由被視為有效：

- 路由的 **NEXT_HOP** 有效且可達
- 從外部對等體收到的 **AS_PATH** 不包含本地 AS
- 路由未被[路由過濾器](../../../../cli-reference/routing/filter/rule.md)拒絕

更多資訊請參閱[下一跳選擇與驗證](./nexthop-selection.md)。

最佳路徑演算法比較的也只是由**單個 BGP 例項**收到的路由。由不同 BGP 例項安裝的路由則由通用演算法比較；即比較路由距離，距離較小的路由優先。

如果滿足所有條件，則執行以下操作：

1. 收到的第一條路徑會被自動視為“最佳路徑”。之後收到的任何路徑都會與第一條收到的路徑比較，以確定新路徑是否更優。
2. 優先選擇 **WEIGHT** 最高的路徑。
   該引數不屬於 BGP 標準，它是為了在本地快速選擇最佳路由而引入的。該引數是路由器本地引數（在 BGP 輸入中透過路由過濾器賦值），無法被通告。未分配 WEIGHT 的路由預設值為 0。
3. 優先選擇 **LOCAL_PREF** 最高的路徑。
   該屬性僅在 AS 內部使用。沒有 LOCAL_PREF 屬性的路徑預設值為 100。
4. 優先選擇 **AS_PATH** 最短的路徑（若 [`ignore-as-path-len`](../../../../cli-reference/routing/bgp/instance.md#ignore-as-path-len) 設定為 **yes**，則跳過此項）。  
   每個 **AS_SET** 無論其集合大小均計為 1。**AS_CONFED_SEQUENCE** 和 **AS_CONFED_SET** 不計入 **AS_PATH** 長度。
5. ~~優先選擇透過 aggregate 或 BGP network 本地產生的路徑~~
6. 優先選擇 [**ORIGIN** 型別](#route-origin)最低的路徑。

   內部閘道器協定（IGP）低於外部閘道器協定（EGP），EGP 低於 INCOMPLETE。

   換言之，**IGP < EGP < INCOMPLETE**。
7. 優先選擇**多出口鑑別器**（MED）最低的路徑。

   路由器僅對具有相同鄰居（最左側）AS 的路徑比較 MED 屬性。確定鄰居 AS 時不考慮聯盟。  
   沒有明確 MED 值的路徑按 MED 為 0 處理。
8. 優先選擇 **eBGP** 路徑而非 **iBGP** 路徑。
9. 如果啟用了 `multipath`，則在此處中斷並將各路徑視為等價。這將安裝 BGP [ECMP](../../routing-decision.md#multipath-ecmp-routes) 路由。
10. 優先選擇 **IGP 度量**最低的路徑。
11. 優先選擇來自 [**router ID**](../../../../cli-reference/routing/bgp/instance.md#router-id) 最低的 BGP 路由器的路由。如果路由攜帶 **ORIGINATOR_ID** 屬性，則使用 **ORIGINATOR_ID** 代替 router ID。
12. 優先選擇**路由反射簇列表**最短的路徑。沒有簇列表的路由視為簇列表長度為 0。
13. 優先選擇來自最低鄰居地址的路徑。

## 多例項 {#multiple-instances}

有時可能需要執行多個 BGP 例項，以支援依賴例項的功能，例如 Layer3 VPN 和 [EVPN](../evpn.md)。RouterOS 允許在 [`/routing/bgp/instance`](../../../../cli-reference/routing/bgp/instance.md) 選單中新增多個例項。

請注意，[最佳路徑選擇](#best-path-selection)不適用於來自不同例項的路由。此外，預設的重分發策略不會重分發從不屬於同一例項的會話收到的 BGP 路由。在此類情況下，如果需要此類重分發，請設定 [`output.redistribute`](../../../../cli-reference/routing/bgp/connection.md#output.redistribute)`=bgp`。

## 支援的標準 {#supported-standards}

- [RFC 4271](https://tools.ietf.org/html/rfc4271) Border Gateway Protocol 4
- [RFC 4456](https://tools.ietf.org/html/rfc4456) BGP Route Reflection
- [RFC 5065](https://tools.ietf.org/html/rfc5065) Autonomous System Confederations for BGP
- [RFC 1997](https://tools.ietf.org/html/rfc1997) BGP Communities Attribute
- [RFC 8092](https://tools.ietf.org/html/rfc8092) BGP Large Communities
- [RFC 4360](https://tools.ietf.org/html/rfc4360)、[5668](https://tools.ietf.org/html/rfc5668) BGP Extended Communities
- [RFC 2385](https://tools.ietf.org/html/rfc2385) TCP MD5 Authentication for BGPv4
- [RFC 5492](https://tools.ietf.org/html/rfc5492) Capabilities Advertisement with BGP-4
- [RFC 2918](https://tools.ietf.org/html/rfc2918) Route Refresh Capability
- [RFC 4760](https://tools.ietf.org/html/rfc4760) Multiprotocol Extensions for BGP-4
- [RFC 2545](https://tools.ietf.org/html/rfc2545) Use of BGP-4 Multiprotocol Extensions for IPv6 Inter-Domain Routing
- [RFC 4893](https://tools.ietf.org/html/rfc4893) BGP Support for Four-octet AS Number Space
- [RFC 4364](https://tools.ietf.org/html/rfc4364) BGP/MPLS IP Virtual Private Networks (VPNs)
- [RFC 4761](https://tools.ietf.org/html/rfc4761) Virtual Private LAN Service (VPLS) Using BGP for Auto-Discovery and Signalling
- draft-ietf-l2vpn-signaling-08 Cisco VPLS BGP-based auto-discovery
- [RFC 6286](https://tools.ietf.org/html/rfc6286) AS-wide Unique BGP Identifier for BGP-4
- [RFC 4273](https://tools.ietf.org/html/rfc4273) SNMP peer table monitoring (OID 1.3.6.1.2.1.15.3.1)（僅 IPv4）
- [RFC 6793](https://www.rfc-editor.org/rfc/rfc6793) 4 位元組 ASN 支援與 Aggregator 屬性。
- [RFC 4486](https://datatracker.ietf.org/doc/html/rfc4486) Subcodes for BGP Cease Notification Message
- [RFC 4659](https://datatracker.ietf.org/doc/html/rfc4659) MPLS VPN Extension for IPv6
- [RFC 8950](https://datatracker.ietf.org/doc/html/rfc8950) Advertising IPv4 Network Layer Reachability Information (NLRI) with an IPv6 Next Hop
- [RFC 6811](https://datatracker.ietf.org/doc/html/rfc6811) BGP Prefix Origin Validation
- [RFC 6996](https://www.rfc-editor.org/rfc/rfc6996.html) Autonomous System (AS) Reservation for Private Use
- [RFC 9234](https://datatracker.ietf.org/doc/rfc9234/) Route Leak Prevention and Detection Using Roles in UPDATE and OPEN Messages
- [RFC 5549](https://datatracker.ietf.org/doc/html/rfc5549) Advertising IPv4 Network Layer Reachability Information with an IPv6 Next Hop
