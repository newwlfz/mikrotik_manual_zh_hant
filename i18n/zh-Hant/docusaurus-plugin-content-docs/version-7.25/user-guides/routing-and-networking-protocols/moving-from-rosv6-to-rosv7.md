---
sidebar_key: "routing-and-networking-protocols/moving-from-rosv6-to-rosv7"
sidebar_position: 2
title: "從 ROSv6 遷移到 ROSv7"
sidebar_label: "從 ROSv6 遷移到 ROSv7"
description: "本頁介紹從 RouterOS v6 到 v7 的過渡，重點說明關鍵變化，例如路由表限制增加、新的 `/routing/table` 和 `/routing/rule` 選單、路由處理速度提升，以及策略路由方面的差異。文中包含配置自定義路由表、多 WAN 設定以及排查 mangle 規則衝突的示例。"
tags:
  - 'ospf'
  - 'bgp'
  - 'rip'
  - 'routing'
slug: /user-guides/routing-and-networking-protocols/moving-from-rosv6-to-rosv7
source: https://manual.mikrotik.com/docs/7.25/user-guides/routing-and-networking-protocols/moving-from-rosv6-to-rosv7
captured_at: '2026-11-04T11:22:22+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

預設情況下，所有路由都會像以前一樣加入 "main" 路由表。從配置角度看，最大的區別是路由表限制增加、路由表監控方式不同，以及路由如何加入特定路由表（見下一個示例）。
V7 引入了新選單 `/routing/route`，它顯示所有地址族路由以及所有被過濾的路由及其所有可能的路由屬性。`/ip/route` 和 `/ipv6/route` 選單用於新增靜態路由，併為簡單起見只顯示基本路由屬性。

有關路由的更深入資訊，請參閱本文 ([IP 路由](../../getting-started/networking-fundamentals/index.md).

另一個新變化是，最常見的路由列印請求由路由程式處理，與 v6 相比顯著提高了速度。

## 路由表的使用與策略路由 {#use-of-routing-tables-and-policy-routing}

與 v6 的主要區別在於，在配置中任何地方引用路由表之前，必須先將其新增到 `/routing/table` 選單。  並且，如果打算讓路由表將路由推送到 FIB，則應指定 **fib** 引數。
路由規則配置相同，只是選單位置不同（現在不再是 `/ip route rule`，而是 `/routing/rule`）。

讓我們考慮一個基本示例：我們只想在名為 myTable 的路由表中將 8.8.8.8 解析到閘道器 172.16.1.1：

```ros
/routing/table/add name=myTable fib
/routing/rule/add dst-address=8.8.8.8 action=lookup-only-in-table table=myTable
/ip/route/add dst-address=8.8.8.8 gateway=172.16.1.1@main routing-table=myTable
```

除了路由規則之外，您還可以使用 mangle 用 routing-mark 標記封包，就像在 ROSv6 中一樣。

使用 mangle 設定 routing-mark 時，請注意不要標記 "local" 流量。如果您的規則也標記本地流量，那麼路由器的 IP 地址將不可達，因為預設情況下，mangle 位於列表首位並覆蓋本地查詢：

```routeros
[admin@CCR2004_2XS_111] /routing/rule> print
Flags: X - disabled, I - inactive; * - default
 0  * action=mangle

 1  * action=lookup vrf

 2  * action=unreachable vrf

 3  * action=lookup table=local

 4  * action=lookup table=main
```

例如，一個基本的多 WAN 設定：

```ros
/routing/table/add name=myTable fib
/ip/address
add address=192.168.1.1/24 interface=LAN
add address=1.1.1.2/24 interface=WAN1
add address=2.2.2.2/24 interface=WAN2
/ip/route
add gateway=1.1.1.1@main routing-table=myTable
add gateway=2.2.2.1
/ip/firewall/mangle/add in-interface=LAN action=mark-routing new-routing-mark=myTable
```

來自 LAN 介面、目標地址為 192.168.1.1 的封包將被 mangle 規則標記，並由 "myTable" 路由表處理。在該表中，到達 192.168.1.1 的唯一路由是預設路由，這意味著該封包將被轉發到 1.1.1.1 閘道器。

有兩種方法可以解決此問題：

- 透過向 mangle 規則新增 **`!dst-address-type=local`**，將 local 排除在標記之外。
- 在 `/routing/rule` 選單中，將第一條規則（action=mangle）移到（action=lookup table=local）下方。

使用哪種方法取決於設定的複雜程度。

## 下一跳查詢 {#nexthop-lookup}

考慮一個來自 v6 的示例：

```ros
/ip/route/add dst-address=10.0.1.0/24 gateway=10.0.0.1
    scope=50 target-scope=30 comment=A
/ip/route/add dst-address=10.0.2.0/24 gateway=10.0.0.1
    scope=30 target-scope=20 comment=B
/ip/route/add dst-address=10.0.0.0/24 scope=20 gateway=WHATEVER
    comment=C
```

閘道器 10.0.0.1 透過 C 使用最小的引用 scope（來自路由 B 的 scope 20）進行遞迴解析，並且兩條路由都處於活動狀態。現在我們同時更改 A 和 B：

```ros
/ip/route/set A target-scope=10
```

突然，應用對路由 A 的更新會使路由 B 的閘道器變為非活動狀態。這是因為在 v6 中，每個地址只有一個閘道器物件。

v7 為每個地址保留多個閘道器物件，每個 scope 和閘道器檢查的組合對應一個物件。

當更改路由的 `target-scope` 或閘道器檢查時，ROS v7 ***不會影響其他路由***，而在 v6 中則會影響。在 v7 中，target-scope 和閘道器檢查是內部附加到閘道器而不是路由的屬性。

## OSPF 配置 {#ospf-configuration}

OSPFv3 和 OSPFv2 現在合併到一個選單 `/routing/ospf` 中。撰寫本文時，沒有預設例項和區域。
要啟動 OSPFv2 和 OSPF v3 例項，首先需要為每個例項建立一個例項，然後為每個例項新增一個區域。

```ros
/routing/ospf/instance
add name=v2inst version=2 router-id=1.2.3.4
add name=v3inst version=3 router-id=1.2.3.4
/routing/ospf/area
add name=backbone_v2 area-id=0.0.0.0 instance=v2inst
add name=backbone_v3 area-id=0.0.0.0 instance=v3inst
```

此時，您已準備好在網路介面上啟動 OSPF。對於 IPv6，您可以新增要執行 OSPF 的介面（與 ROSv6 相同），或者新增 IPv6 網路。在第二種情況下，OSPF 將自動檢測介面。以下是一些介面配置示例：

```ros
/routing/ospf/interface-template
add network=192.168.0.0/24 area=backbone_v2
add network=2001:db8::/64 area=backbone_v3
add network=ether1 area=backbone_v3
```

ROSv7 使用模板將介面與模板匹配，並應用匹配模板中的配置。  OSPF 選單 `interface` 和 `neighbor` 包含只讀條目，僅用於狀態監控。

RouteOS 允許直接透過路由過濾器控制路由重分發，而無需 `redistribute` 引數。這為從哪些協定重分發哪些路由提供了更大的靈活性。
例如，假設您只想重分發來自 192.168.0.0/16 網路範圍的靜態 IPv4 路由。

**選項 1：**

```ros
/routing/ospf/instance
set v2inst out-filter-chain=ospf_out redistribute=static
```

```ros
/routing/filter/rule/add chain=ospf_out rule="if (dst in 192.168.0.0/16) {accept}"
```

**選項 2：**

```ros
/routing/filter/rule/add chain=ospf_out rule="if (protocol static && dst in 192.168.0.0/16) {accept}"
```

:::warning
路由過濾鏈的預設動作是 "reject"
:::

## BGP 配置 {#bgp-configuration}

與 ROSv6 相比，BGP 配置進行了徹底重新設計。第一個也是最大的區別是不再有 `instance` 和 **`peer`** 配置選單。取而代之的是 **`connection`**、**`template`** 和 **`session`** 選單。
這種結構的原因是要嚴格區分負責連線的引數和 BGP 協定特定的引數。

讓我們從 Template 開始。它包含所有與 BGP 協定相關的配置選項。它可以用作動態對等體的模板，也可以將類似配置應用到一組對等體。請注意，這與 Cisco 裝置上的對等體組不同，後者不僅僅是共同配置。

預設情況下，有一個預設模板，要求您設定自己的 AS。

```ros
/routing/bgp/template/set default as=65533
```

:::info
從 v7.1beta4 開始，模板引數暴露在 "connection" 配置中。這意味著模板不再是必需的，從而可以更輕鬆地進行基本 BGP 連線設定，類似於 ROSv6 中的方式。
:::

大多數引數與 ROSv6 類似，不同的是有些引數分組到 output 和 input 部分，使配置更易讀，也更容易理解該選項是應用於輸入還是輸出。如果您熟悉 CapsMan，那麼語法是相同的，例如，要指定輸出選擇鏈，您可以設定 `output.filter-chain=myBgpChain`。

您甚至可以從另一個模板繼承模板引數，例如：

```ros
/routing/bgp/template
add name=myAsTemplate as=65500 output.filter-chain=myAsFilter
set default template=myAsTemplate
```

新路由配置的另一個重要方面是全域性 Router ID，它設定 router-id 並將對等體分組到一個例項中。RouterOS 會新增一個預設 ID，該 ID 從任意介面的最高 IP 中選擇 instance-id。預設 BGP 模板預設設定為使用 "default" ID。
如果出於任何原因需要調整或新增新例項，可以在 `/routing/id` 選單中完成。

非常有趣的引數是 **`input.``affinity`** `and` **`output.affinity`**；它們允許控制活動會話的輸入和輸出將在哪個程式中處理：

- **alone** - 每個會話的輸入和輸出在其自己的程式中處理，當有很多核心和很多對等體時，這很可能是最佳選項。
- **afi, instance, vrf, remote-as** - 嘗試在具有類似引數的程式中執行新會話的輸入/輸出。
- **main** - 在主程式中執行輸入/輸出（在單核上甚至可能在核心數較少的多核裝置上可能提高效能）。
- **input** - 在與輸入相同的程式中執行輸出（僅可為 output affinity 設定）。

現在我們已經為模板設定了引數，可以新增 BGP 連線。最小引數集是 `remote.address`、`template, connect`、`listen` 和 `local.role`

Connect 和 listen 引數指定對等體是嘗試連線並監聽遠端地址，還是隻連線或只監聽。在對等體使用多跳連線的設定中，也可能必須配置 `local.address`（就像 ROSv6 中的 `update-source` 一樣）。

:::warning
並非必須指定遠端 AS 號。ROS v7 可以從 open 訊息中確定遠端 ASN。只有當您想接受來自該特定 AS 的連線時，才應指定遠端 AS。
:::

對等體角色現在是一個必需引數。對於基本設定，您可以直接使用 ibgp、ebgp（有關可用角色的更多資訊，請參閱相應的 [RFC 草案]( https://datatracker.ietf.org/doc/draft-ietf-idr-bgp-open-policy/?include_text=1)）。請記住，目前草案中描述的能力、community 和過濾尚未實現。

非常基本的 iBGP 設定，用於在整個本地網路上監聽連線：

```ros
/routing/bgp/connection
add remote.address=10.155.101.0/24 listen=yes template=default local.role=ibgp
```

現在您可以從 `/routing/bgp/session` 選單監控所有已連線和未連線對等體的狀態。

所有路由程式的其他有用偵錯資訊可以從 `/routing/stats` 選單監控

```text
[admin@v7_ccr_bgp] /routing/stats/process> print interval=1
Columns: TASKS, PRIVATE-MEM-BLOCKS, SHARED-MEM-BLOCKS, PSS, RSS, VMS, RETIRED, ID, PID, RPID, PROCESS-TIME, KERNEL-TIME, CUR-B>
# TASKS PRIVATE-M SHARED-ME PSS RSS VMS RET ID PID R PROCESS-TI KERN>
0 routing tables 12.2MiB 20.0MiB 18.7MiB 42.2MiB 83.4MiB 8 main 319 0 19s750ms 8s50>
rib >
connected networks >
1 fib 512.0KiB 0 7.4MiB 30.9MiB 83.4MiB fib 384 1 5s160ms 22s5>
2 ospf 1024.0KiB 1024.0KiB 5.9MiB 25.9MiB 83.4MiB 382 ospf 388 1 1m42s170ms 1m31>
connected networks >
3 fantasy 512.0KiB 0 2061.0KiB 5.9MiB 83.4MiB fantasy 389 1 1s410ms 870m>
4 configuration and reporting 40.0MiB 512.0KiB 45.0MiB 64.8MiB 83.4MiB static 390 1 12s550ms 1s17>
5 rip 768.0KiB 0 5.3MiB 24.7MiB 83.4MiB rip 387 1 1s380ms 1s20>
connected networks >
6 /routing/policy/configuration 512.0KiB 256.0KiB 2189.0KiB 6.0MiB 83.4MiB policy 385 1 1s540ms 1s20>
7 BGP service 768.0KiB 0 2445.0KiB 6.2MiB 83.4MiB bgp 386 1 6s170ms 9s38>
8 BGP Input 10.155.101.217 8.8MiB 6.0MiB 15.6MiB 38.5MiB 83.4MiB 20 21338 1 25s170ms 3s23>
BGP Output 10.155.101.217 >
9 Global memory 256.0KiB global 0 0 >
-- [Q quit|D dump|C-z pause|right]
```

路由過濾與 ROSv6 略有不同。在 BGP 模板中，您現在可以指定 output.filter-chain、output.filter-select、input.filter 以及若干 input.accept-\* 選項。

現在 input.accept-\* 允許在傳入訊息甚至還未被解析和儲存到記憶體之前直接對其進行過濾，從而顯著減少記憶體使用。常規輸入過濾鏈只能拒絕字首，這意味著它仍會佔用記憶體，並會在 `/routing/route` 表中顯示為 "not active, filtered"。

一個非常基本的 BGP 輸入過濾器示例：接受來自 192.168.0.0/16 子網的字首而不修改任何屬性。對於其他字首，從收到的 local pref 值中減去 1，並將 IGP metric 設定為來自 OSPF ext 的值。此外，我們將只接受地址列表中的特定字首，以減少記憶體使用。

```ros
/ip/firewall/address-list
add list=bgp_list address=192.168.1.0/24
add list=bgp_list address=192.168.0.0/24
add list=bgp_list address=172.16.0.0/24

/routing/bgp/template
set default input.filter=bgp_in .accept-nlri=bgp_list

```

```ros
/routing/filter/rule
add chain=bgp_in rule="if (dst in 192.168.0.0/16) {accept}"
add chain=bgp_in rule="set bgp-local-pref -1; set bgp-igp-metric ospf-ext-metric; accept"
```

:::danger
如果未指定路由過濾鏈，BGP 將嘗試通告它在路由表中能找到的每條活動路由
:::

:::info
路由過濾鏈的預設動作是 `reject`。
:::

### 監控通告 {#monitoring-advertisements}

RouterOS v7 預設停用 BGP 輸出監控。這可以在具有大型路由表的設定中顯著減少資源使用。

要能夠檢視輸出通告，應採取以下幾個步驟：

- 在 BGP 連線配置中啟用 "output.keep-sent-attributes"。
- 從 BGP 會話選單執行 "dump-saved-advertisements"。
- 從 `/routing/stats/pcap` 選單檢視儲存的輸出。

```ros
[admin@arm-bgp] /routing/bgp/connection>  set 0 output.keep-sent-attributes=yes
[admin@arm-bgp] /routing/bgp/session> print
Flags: E - established
 0 E remote.address=10.155.101.183 .as=444 .id=192.168.44.2 .refused-cap-opt=no .capabilities=mp,rr,gr,as4
     .afi=ip,ipv6 .messages=4 .bytes=219 .eor=""
     local.address=10.155.101.186 .as=456 .id=10.155.255.186 .capabilities=mp,rr,gr,as4 .afi=ip,ipv6
     .messages=1 .bytes=19 .eor=""
     output.procid=66 .filter-chain=bgp_out .network=bgp-nets .keep-sent-attributes=yes
     input.procid=66 ebgp
     hold-time=3m keepalive-time=1m uptime=4s30ms

[admin@arm-bgp] /routing/bgp/session> dump-saved-advertisements 0 save-to=test_out.pcap

```

### 網路 {#networks}

最後，您可能會注意到 **`network`** 選單不見了，並且可能想知道如何通告自己的網路。現在網路被新增到防火牆地址列表，並在 BGP 配置中引用。
以下是 ROSv6 網路配置：

```ros
/routing bgp network add network=192.168.0.0/24 synchronize=yes
/ip route add dst-address=192.168.0.0/24 type=blackhole
```

在 v7 中會轉換為：

```ros
/ip/firewall/address-list
add list=bgp-networks address=192.168.0.0/24

/ip/route
add dst-address=192.168.0.0/24 blackhole

/routing/bgp/connection
set peer_name output.network=bgp-networks
```

還可以為每個 BGP 網路自動建立 blackhole 路由：

```ros
/routing/bgp/connection
set peer_name output.network-blackhole=yes
```

僅新增一個網路時需要做更多配置，但當您需要處理大量網路時，這提供了簡便性。v7 甚至允許為每個 BGP 連線指定自己的網路集。

:::warning
在 v7 中無法關閉與 IGP 路由的同步（只有當相應的 IGP 路由存在於路由表中時，該網路才會被通告）。
:::

## 路由過濾器 {#routing-filters}

從 ROSv7.1beta4 開始，路由過濾器配置已改為類似指令碼的配置。規則現在可以具有 "if .. then" 語法，以根據 "if" 語句中的條件設定引數或應用動作。

多個沒有動作的規則會堆疊在單個規則中，並像防火牆一樣按順序執行，原因是 "set" 引數的順序很重要，而且每行寫一個 "set" 可以更容易地自上而下理解應用了哪些動作。

例如，匹配靜態預設路由並應用 accept 動作可以寫在一個配置規則中：

```ros
/routing/filter/rule
add chain=ospf_in rule="if (dst==0.0.0.0/0 && protocol static) { accept }"
```

例如，ROSv6 規則 `/routing/filter/add chain=ospf_in prefix=172.16.0.0/16 prefix-length=24 protocol=static action=accept` 轉換為 ROSv7 後為：

```ros
/routing/filter/rule
add chain=ospf_in rule="if (dst in 172.16.0.0/16 && dst-len==24 && protocol static) { accept }"
```

另一個示例是匹配來自 172.16.0.0/16 範圍且字首長度等於 24 的字首，並設定 BGP med 和 prepend 值

```ros
/routing/filter/rule
add chain=BGP_OUT rule="if (dst-len==24 && dst in 172.16.0.0/16) { \n
    set bgp-med 20; set bgp-path-prepend 2; accept }"
```

也可以像這樣匹配字首長度範圍

```ros
/routing/filter/rule
add chain=BGP_OUT rule="if (dst-len>13 && dst-len<31 && dst in 172.16.0.0/16) { accept }"
```

過濾規則現在可用於從 community 列表中匹配或設定 community、large community 和 extended community：

```ros
/routing/filter/rule
add chain=bgp_in rule="set bgp-large-communities 200001:200001:10 "
```

如果有很多 community 集需要在多個規則中應用，則可以定義 community 集並使用它們來匹配或設定：

```ros
/routing/filter/large-community-set
add set=myLargeComSet communities=200001:200001:10

/routing/filter/rule
add chain=bgp_in rule="append bgp-large-communities myLargeComSet "
```

由於 route-target 編碼在 extended community 屬性中，要更改或匹配 RT，您需要操作 extended community 屬性，例如：

```ros
/routing/filter/rule
add chain=bgp_in rule="set bgp-ext-communities rt:327824:20 "
```

## RPKI {#rpki}

RouterOS 實現了 RTR 用戶端。您連線到伺服器，伺服器將傳送路由有效性資訊。然後，該資訊可用於在路由過濾器中透過 "rpki-validate" 針對某個組驗證路由，進一步在過濾器中可以使用 "match-rpki" 匹配確切狀態。

有關更多資訊，請參閱 [RPKI](./unicast/rpki.md) 文件。

## RIP 配置 {#rip-configuration}

要啟動 RIP，應配置例項。在那裡您應選擇 RIP 將重分發哪些路由，以及是否重分發預設路由。

```ros
/routing/rip/instance
add name=instance1 originate-default=never redistribute=connected,static
```

然後應配置 interface-template。在 ROS 版本 7 中，不再像版本 6 那樣需要定義網路。

```ros
/routing/rip/interface-template
add interfaces=ether1 instance=instance1
```

現在一臺路由器上的基本配置已完成。RIP 鄰居路由器應以類似方式配置。

在 ROS v7 中，僅當有路由要傳送和/或接收時，鄰居才會出現。

ROSv6 中的字首列表已棄用，現在所有過濾都必須由路由過濾器完成。
