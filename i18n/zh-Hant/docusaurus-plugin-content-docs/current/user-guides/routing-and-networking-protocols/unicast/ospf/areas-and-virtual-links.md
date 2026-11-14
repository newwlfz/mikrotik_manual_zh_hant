---
sidebar_key: "user-guides/routing-and-networking-protocols/unicast/ospf/areas-and-virtual-links"
sidebar_position: 4
title: "區域和虛擬鏈路"
sidebar_label: "區域和虛擬鏈路"
description: "理解 OSPF 區域和虛鏈路的概念。"
tags:
  - 'routing'
  - 'ospf'
source: https://manual.mikrotik.com/docs/user-guides/routing-and-networking-protocols/unicast/ospf/areas-and-virtual-links
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

OSPF 的一個顯著特性是可以將一個 AS 劃分為多個路由區域，每個區域都有自己的一組鄰居。想象一個包含 300 多臺路由器且它們之間有多條鏈路的大型網路。每當鏈路抖動或網路中發生其他拓撲變化時，該變化都會被泛洪到網路中的所有 OSPF 裝置。這會給網路帶來沉重負載，甚至導致停機，因為對於如此大型的網路，[網路收斂](../../routing-decision.md) 可能需要一些時間。

大型單區域網路可能會產生嚴重問題：

- 每當網路拓撲發生變化時，每臺路由器都會重新計算資料庫。該過程會消耗 CPU 資源。
- 每臺路由器都儲存整個鏈路狀態資料庫，該資料庫顯示整個網路的拓撲。這會佔用記憶體資源。
- 路由表的完整副本以及路由表條目數量可能顯著多於網路數量，這會佔用更多記憶體資源。
- 更新大型資料庫需要更多頻寬。

引入區域可以實現更好的資源管理，因為一個區域內部的拓撲變化不會被泛洪到網路中的其他區域。區域概念使網路管理更簡單，並支援區域之間的路由彙總，從而顯著減少每個 OSPF 鄰居上要儲存的資料庫大小。這意味著每個區域都有自己的鏈路狀態資料庫以及相應的最短路徑樹。有關 OSPF 鄰居如何相互發現並同步資料庫的更多資訊，請參見[鄰居關係](./neighbour-relationship.md)。

區域的結構對其他區域不可見。這種知識隔離使得在使用多個區域時協定更具可擴充套件性。路由表計算消耗的 CPU 資源更少，路由流量也會減少。

然而，多區域設定會帶來額外的複雜性。不應將少於 50 臺路由器的區域進行劃分。一個區域中的最大路由器數量主要取決於用於路由表計算的 CPU 能力。

![](/img/9ea2d8342282c898.png#gh-light-mode-only)
![](/img/5a10dfe626a5e2b8.png#gh-dark-mode-only)

OSPF 區域具有唯一的 32 位標識（Area ID）。Area ID 為 0.0.0.0 的區域（稱為骨幹區域）是主區域，任何其他區域都應連線到該區域。連線到多個區域的路由器稱為 **ABR**（區域邊界路由器），其主要職責是在所連線的區域之間進行彙總和更新抑制。連線到另一個路由域的路由器稱為 **ASBR**（自治系統邊界路由器）。

每個區域都有自己的鏈路狀態資料庫，由描述該區域中所有路由器如何互連的 router-LSA 和 network-LSA 組成。區域拓撲的詳細資訊對其他所有區域隱藏。Router-LSA 和 network-LSA 不會泛洪到區域邊界之外。區域邊界路由器（**ABR**）透過 OSPF summary-LSA 將一個區域的編址資訊洩漏到另一個區域。這使路由器在將資料轉發到來自另一區域的目的地時能夠選擇最佳的區域邊界路由器，這稱為**區域內路由**。有關如何計算路由表的更多資訊，請參見[路由表計算](./routing-calculation.md)。

區域之間的路由資訊交換本質上是一種距離向量演算法。為防止諸如計數到無窮大之類的演算法收斂問題，所有區域都必須直接連線到**骨幹區域**，從而形成簡單的中心輻射型拓撲。骨幹區域的 area-ID 始終為 0.0.0.0，且不能更改。有關路由決策過程的更多資訊，請參見[路由決策](../../routing-decision.md)。

在 [`/routing/ospf/area`](../../../../cli-reference/routing/ospf/area/index.md) 選單中配置 RouterOS 區域。例如，以下是一個 ABR 路由器的配置，該路由器連線了多個區域、一個 Stub 區域和一個預設區域：

```ros
/routing/ospf/area
add name=backbone_v2 area-id=0.0.0.0 instance=v2inst
add name=stub_area area-id=1.1.1.1 instance=v2inst type=stub
add name=another_area area-id=2.2.2.2 instance=v2inst type=default
```

OSPF 可以有 5 種區域型別，由 [`type`](../../../../cli-reference/routing/ospf/area/index.md#type) 引數配置。每種區域型別定義該區域支援哪些型別的 LSA：

- 標準/預設 - 可以在此區域中傳輸 OSPF 封包。它支援 1、2、3、4 和 5 類 LSA。
- 骨幹 - 如前所述，這是任何其他區域所連線的主區域。它基本上與標準區域相同，但使用 ID 0.0.0.0 標識。
- [Stub](#stub-area) - 此區域不接受任何外部路由。
- [Totally stubby](#totally-stubby-area) - Stub 區域的一種變體。
- [Not-so-stubby (NSSA)](#nssa) - Stub 區域的一種變體。

## LSA 型別 {#lsa-types}

在繼續詳細瞭解每種區域型別之前，請先熟悉 LSA 型別：

- ***type 1*** - （Router LSA）由區域內的路由器傳送，包括直接連線鏈路的列表。這些 LSA 不會跨越 ABR 或 ASBR。
- ***type 2*** - （Network LSA）為區域中的每個“傳輸網路”生成。傳輸網路至少有兩臺直接連線的 OSPF 路由器。乙太網就是傳輸網路的一個示例。Type 2 LSA 列出組成該傳輸網路的每臺所連線路由器，並由 DR 生成。
- ***type 3*** - （Summary LSA）ABR 傳送 Type 3 Summary LSA。Type 3 LSA 將一個區域擁有的任何網路通告給 OSPF AS 中的其他區域。預設情況下，OSPF 會為始發區域中定義的每個子網通告 Type 3 LSA，這可能導致泛洪問題。應在 ABR 上使用手動彙總。
- ***type 4*** - （ASBR-Summary LSA）通告 ASBR 地址並顯示 ASBR 所在位置，通告其地址而不是其路由表。
- ***type 5*** - （External LSA）通告透過 ASBR 學到的路由，並泛洪到除 Stub 區域之外的所有區域。此 LSA 分為兩個子型別：***external type 1*** 和 ***external type 2***。
- ***type 6*** - （Group Membership LSA）為 OSPF 的多播擴充套件定義，RouterOS 不使用。
- ***type 7*** - Type 7 LSA 向 ABR 通知匯入 NSSA 區域的外部路由。然後，區域邊界路由器將這些 LSA 轉換為 **type 5** 外部 LSA，並將它們泛洪到 OSPF 網路的其餘部分。
- ***type 8*** - External Attributes LSA（OSPFv2）/ link-local LSA（OSPFv3）。
- ***type 9*** - Link-Local Scope Opaque（OSPFv2）/ Intra Area Prefix LSA（OSPFv3）。此型別的 LSA 不會泛洪到本地（子）網路之外。
- ***type 10*** - Area Local Scope Opaque。此型別的 LSA 不會泛洪到其關聯區域的範圍之外。
- ***type 11*** - Opaque LSA，會泛洪到整個 AS（作用域與 **type 5** 相同）。它不會在 stub 區域和 NSSA 中泛洪。

:::note
如果沒有任何 ASBR，則網路中沒有 LSA Type 4 和 Type 5。
:::

## 標準區域 {#standard-area}

此區域支援 1、2、3、4 和 5 類 LSA。

![](/img/9645f9b3ee7f9728.jpg#gh-light-mode-only)
![](/img/40a928bda151d8ac.png#gh-dark-mode-only)

一個帶有預設區域的簡單多區域網路。在此示例中，area1 中的所有網路都會泛洪到骨幹，而骨幹中的所有網路都會泛洪到 area1。

**R1**

```ros
/ip/address/add address=10.0.3.1/24 interface=ether1
/ip/address/add address=10.0.2.1/24 interface=ether2
/routing/ospf/instance
add name=v2inst version=2 router-id=1.0.0.1
/routing/ospf/area
add name=backbone_v2 area-id=0.0.0.0 instance=v2inst
add name=area1 area-id=1.1.1.1 type=default instance=v2inst
/routing/ospf/interface-template
add networks=10.0.2.0/24 area=backbone_v2
add networks=10.0.3.0/24 area=area1
```

**R2**

```ros
/ip/address/add address=10.0.1.1/24 interface=ether2
/ip/address/add address=10.0.2.2/24 interface=ether1
/routing/ospf/instance
add name=v2inst version=2 router-id=1.0.0.2
/routing/ospf/area
add name=backbone_v2 area-id=0.0.0.0 instance=v2inst
/routing/ospf/interface-template
add networks=10.0.2.0/24 area=backbone_v2
add networks=10.0.1.0/24 area=backbone_v2
```

**R3**

```ros
/ip/address/add address=10.0.3.2/24 interface=ether2
/ip/address/add address=10.0.4.1/24 interface=ether1
/routing/ospf/instance
add name=v2inst version=2 router-id=1.0.0.3
/routing/ospf/area
add name=area1 area-id=1.1.1.1 type=default instance=v2inst
/routing/ospf/interface-template
add networks=10.0.3.0/24 area=area1
add networks=10.0.4.0/24 area=area1
```

## Stub 區域 {#stub-area}

Stub 區域的主要目的是防止此類區域承載外部路由。從這些區域到外部世界的路由基於[預設路由](#external-routing-information-and-default-route)。Stub 區域可減小區域中的資料庫大小以及該區域中路由器的記憶體需求。

![](/img/cfd7aadcf0fea194.jpg#gh-light-mode-only)
![](/img/68d33098a30f4218.png#gh-dark-mode-only)

Stub 區域有一些限制。ASBR 路由器不能位於該區域內部，並且 Stub 區域不能用作虛擬鏈路的傳輸區域。存在這些限制是因為 Stub 區域被配置為不承載外部路由。

此區域支援 1、2 和 3 類 LSA。

考慮上一個示例。Area1 被配置為 Stub 區域，這意味著路由器 R2 和 R3 除了預設路由外，不會從骨幹區域接收任何路由資訊。

R1:

```ros
/routing/ospf/instance
add name=v2inst version=2 router-id=1.0.0.1
/routing/ospf/area
add name=backbone_v2 area-id=0.0.0.0 instance=v2inst
add name=area1 area-id=1.1.1.1 type=stub instance=v2inst

/routing/ospf/interface-template
add networks=10.0.0.0/24 area=backbone_v2
add networks=10.0.1.0/24 area=area1
add networks=10.0.3.0/24 area=area1
```

R2:

```ros
/routing/ospf/instance
add name=v2inst version=2 router-id=1.0.0.2
/routing/ospf/area
add name=area1 area-id=1.1.1.1 type=stub instance=v2inst
/routing/ospf/interface-template
add networks=10.0.1.0/24 area=area1
```

R3:

```ros
/routing/ospf/instance
add name=v2inst version=2 router-id=1.0.0.3
/routing/ospf/area
add name=area1 area-id=1.1.1.1 type=stub instance=v2inst
/routing/ospf/interface-template
add networks=10.0.3.0/24 area=area1
```

如果未設定 [`default-cost`](../../../../cli-reference/routing/ospf/area/index.md#default-cost) 引數，則不會產生 stub 區域的 type-3 預設 LSA。

## 完全 Stubby 區域 {#totally-stubby-area}

完全 Stubby 區域是 Stub 區域的擴充套件。完全 Stubby 區域會阻止外部路由和彙總（區域間）路由進入該區域。只有區域內路由會注入該區域。完全 Stubby 區域配置為帶有附加 [`no-summaries`](../../../../cli-reference/routing/ospf/area/index.md#no-summaries) 標誌的 Stub 區域。此區域支援 Type 1、Type 2 LSA 以及帶預設路由的 Type 3 LSA。

```ros
/routing/ospf/area
add name=totally_stubby_area area-id=1.1.1.1 instance=v2inst type=stub no-summaries
```

## NSSA {#nssa}

Not-so-stubby area（NSSA）適用於需要注入外部路由，但不需要注入 type 5 LSA 路由的情況。NSSA RFC 參考另請參見[理解 OSPF](./understanding-ospf.md#supported-standards)。

![](/img/2679895c4a889aa5.jpg#gh-light-mode-only)
![](/img/6550f8718446a2a6.png#gh-dark-mode-only)

插圖顯示了兩個區域（骨幹和 area1）以及到位於 area1 中路由器的 RIP 連線。Area1 必須配置為 Stub 區域，但還必須將外部 RIP 路由注入骨幹。在這種情況下，Area1 應配置為 NSSA。

該配置示例不涵蓋 [RIP](../rip.md) 配置。

**R1**

```ros
/routing/ospf/instance
add name=v2inst version=2 router-id=1.0.0.1
/routing/ospf/area
add name=backbone_v2 area-id=0.0.0.0 instance=v2inst
add name=area1 area-id=1.1.1.1 type=nssa instance=v2inst
/routing/ospf/interface-template
add networks=10.0.0.0/24 area=backbone_v2
add networks=10.0.1.0/24 area=area1
```

**R2**

```ros
/routing/ospf/instance
add name=v2inst version=2 router-id=1.0.0.2
/routing/ospf/area
add name=area1 area-id=1.1.1.1 type=nssa instance=v2inst
/routing/ospf/interface-template
add networks=10.0.1.0/24 area=area1
```

:::info
虛擬鏈路不能跨越 NSSA 區域使用。使用 [`nssa-translator`](../../../../cli-reference/routing/ospf/area/index.md#nssa-translator) 引數控制 type-7 到 type-5 LSA 的轉換。
:::

## 外部路由資訊和預設路由 {#external-routing-information-and-default-route}

在 OSPF 路由域的邊緣，可以找到稱為 **AS 邊界路由器（ASBR）** 的路由器，它們執行其他路由協定之一。這些路由器的職責是將從其他路由協定學到的路由資訊匯入 OSPF 路由域。根據度量型別，可以在兩個不同級別匯入外部路由。

- Type1 - OSPF 度量是內部 OSPF 開銷與外部路由開銷之和。
- Type2 - OSPF 度量僅等於外部路由開銷。

:::tip
Type 1 外部路徑始終優先於 Type 2 外部路徑。當所有路徑都是 Type 2 外部路徑時，始終優先選擇通告的 Type 2 度量最小的路徑。（RFC2328）
:::

可以透過多種方式匯入外部路由，並按所列順序處理：

- 選擇與 [`redistribute`](../../../../cli-reference/routing/ospf/instance.md#redistribute) 或 [`originate-default`](../../../../cli-reference/routing/ospf/instance.md#originate-default) 例項引數匹配的路由。
- 如果指定了輸出路由過濾鏈：
  - 如果使用了 [`redistribute`](../../../../cli-reference/routing/ospf/instance.md#redistribute) 或 [`originate-default`](../../../../cli-reference/routing/ospf/instance.md#originate-default) 引數，則僅處理選中的路由。
  - 否則，處理所有活動路由。
- 在 [`out-filter-select`](../../../../cli-reference/routing/ospf/instance.md#out-filter-select) 中處理選中的路由。

仍然需要[路由過濾器](../../route-selection-and-filtering.md)來設定路由開銷和型別（在需要時）。

以下配置示例選擇並重分發所有靜態路由和 RIP 路由：

```ros
/routing/ospf/instance
add name=v2inst version=2 router-id=1.2.3.4 redistribute=static,rip
```

預設路由的重分發是一種特殊情況，此時應使用 `originate-default` 引數：

```ros
/routing/ospf/instance
set v2inst originate-default=if-installed
```

當重分發由 `originate-default` 和 `redistribute` 引數控制時，會為預設路由過濾引入一些邊界情況。

- 如果啟用了 `redistribute`，則選擇與 redistribute 引數匹配的所有路由。
- 如果 `originate-default=never`，則預設路由將被拒絕。
- 將選中的路由（如果未設定 redistribute 引數，則為所有路由）透過 [`out-filter-select`](../../../../cli-reference/routing/ospf/instance.md#out-filter-select) 執行（如果已配置）。
- 將選中的路由透過 [`out-filter-chain`](../../../../cli-reference/routing/ospf/instance.md#out-filter-chain) 執行（如果已配置）。路由過濾器參考請參見 [`/routing/filter`](../../../../cli-reference/routing/filter/rule.md)。
- 如果 [`originate-default`](../../../../cli-reference/routing/ospf/instance.md#originate-default) 設定為 `always` 或 `if-installed`：
  - OSPF 會建立一個不帶屬性的虛擬預設路由。
  - 將此路由透過 [`out-filter-chain`](../../../../cli-reference/routing/ospf/instance.md#out-filter-chain) 執行，其中可以應用屬性，但操作會被忽略（始終接受）。

有關重分發值的完整列表，請參見 [`/routing/ospf/instance`](../../../../cli-reference/routing/ospf/instance.md)。

## 路由彙總 {#route-summarization}

路由彙總將多條路由合併為單個通告。它在區域邊界（區域邊界路由器）處完成。

應朝骨幹方向進行彙總。這樣，骨幹會接收所有聚合路由，並將它們注入其他區域時已經過彙總。彙總有兩種型別：區域間路由彙總和外部路由彙總。

區域間路由彙總在區域邊界（ABR）上生效。它不適用於透過重分發注入 OSPF 的外部路由。預設情況下，ABR 會為特定區域中的每條路由建立一個 summary LSA，並在相鄰區域中通告它。

範圍允許為多條路由僅建立一個 summary LSA，並向相鄰區域僅傳送單個通告，或者完全抑制通告。

如果使用 [`advertise`](../../../../cli-reference/routing/ospf/area/range.md) 引數配置了範圍，則當特定區域在該範圍下有任何路由時，會為每個範圍通告單個 summary LSA。否則（當 `advertise` 引數被停用時），不會建立任何 summary LSA，也不會在區域邊界之外通告。

可以從 [`/routing/ospf/area/range`](../../../../cli-reference/routing/ospf/area/range.md) 選單配置區域間路由彙總。

考慮兩個區域：骨幹和 area1。Area1 有若干來自 10.0.0.0/16 範圍的 /24 路由，並且當可以彙總時，不必用每個 /24 子網泛洪骨幹區域。在將 area1 連線到骨幹的路由器上，可以設定區域範圍：

```ros
/routing/ospf/area/range
add prefix=10.0.0.0/16 area=area1 advertise=yes cost=10
```

有關 [`advertise`](../../../../cli-reference/routing/ospf/area/range.md) 和 [`cost`](../../../../cli-reference/routing/ospf/area/range.md) 引數參考，請參見 [`/routing/ospf/area/range`](../../../../cli-reference/routing/ospf/area/range.md#cost)。

:::info
對於活動範圍（即至少有一條來自指定區域的 OSPF 路由落在其下），會建立一條型別為 'blackhole' 的路由並安裝到路由表中。
:::

外部路由彙總可以透過使用[路由過濾器](../../route-selection-and-filtering.md)來實現。考慮與上一個相同的示例，不同之處在於 area1 具有從其他協定重分發的 /24 路由。要傳送單個彙總 LSA，請新增一條[黑洞路由](../../../../cli-reference/ip/route/index.md)，並配置適當的 [`/routing/filter/rule`](../../../../cli-reference/routing/filter/rule.md) 以僅接受彙總後的路由：

```ros
/ip/route/add dst-address=10.0.0.0/16 blackhole
/routing/ospf/instance
set v2inst out-filter-chain=ospf_out
/routing/filter/rule
add chain=ospf_out rule="if (dst == 10.0.0.0/16) {accept} else {reject}"
```

## 虛擬鏈路 {#virtual-link}

所有 OSPF 區域都必須連線到骨幹區域，但有時無法進行物理連線。為克服此限制，可以使用**虛擬鏈路**以邏輯方式連線區域。

可以使用虛擬鏈路的兩種常見場景：

- 將碎片化的骨幹區域粘合在一起。
- 連線沒有直接連線到骨幹的遠端區域。

### 分割區骨幹 {#partitioned-backbone}

OSPF 允許使用虛擬鏈路連線骨幹區域的不連續部分。當兩個分離的 OSPF 網絡合併為一個大型網路時，可能需要這樣做。可以在分別從兩側接觸骨幹區域並具有共同區域的獨立 ABR 之間配置虛擬鏈路。

![](/img/ef8fd4be4ae15662.jpg#gh-light-mode-only)
![](/img/618a626465d2c05c.png#gh-dark-mode-only)

當不存在共同區域時，可以建立額外區域作為傳輸區域。上一張圖展示了這一點。

當非骨幹區域被分割區時，不需要為它們使用虛擬鏈路。OSPF 不會主動嘗試修復區域分割區。當區域被分割區時，每個組成部分只會成為單獨的區域。骨幹在新區域之間執行路由。某些目的地可透過**區域內**路由到達。區域分割區需要**區域間**路由。

但是，要在分割區後保持完整路由，地址範圍不得拆分到區域分割區的多個組成部分中。考慮使用 [BFD](../bfd.md) 在虛擬鏈路上實現更快的故障檢測。

### 無到骨幹的物理連線 {#no-physical-connection-to-a-backbone}

區域可能沒有到骨幹的物理連線。虛擬鏈路為斷開連線的區域提供到骨幹的邏輯路徑。必須在共享共同區域的兩個 ABR 之間建立鏈路，其中一個 ABR 連線到骨幹。

![](/img/e642c0bd34f2b743.jpg#gh-light-mode-only)
![](/img/2a58e5cf11fcca93.png#gh-dark-mode-only)

R1 和 R2 都是 ABR，並且 R1 連線到骨幹區域。Area2 將用作**傳輸區域**，而 R1 是進入骨幹區域的**入口點**。必須在兩臺路由器上配置虛擬鏈路。

在 [`/routing/ospf/interface`](../../../../cli-reference/routing/ospf/interface.md) 選單中新增虛擬鏈路配置。必須在兩臺路由器上配置 [`vlink-transit-area`](../../../../cli-reference/routing/ospf/interface.md#vlink-transit-area) 和 [`vlink-neighbor-id`](../../../../cli-reference/routing/ospf/interface.md#vlink-neighbor-id) 引數。基於該圖的配置如下：

R1:

```ros
/routing/ospf/interface
add vlink-transit-area=area2 area=backbone_v2 type=virtual-link vlink-neighbor-id=2.2.2.2
```

R2:

```ros
/routing/ospf/interface
add vlink-transit-area=area2 area=backbone_v2 type=virtual-link vlink-neighbor-id=1.1.1.1
```
