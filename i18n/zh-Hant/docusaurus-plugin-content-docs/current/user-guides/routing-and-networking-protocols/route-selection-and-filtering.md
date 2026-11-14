---
sidebar_key: "user-guides/routing-and-networking-protocols/route-selection-and-filtering"
sidebar_position: 10
title: "路由選擇和過濾"
sidebar_label: "路由選擇和過濾"
description: "MikroTik RouterOS 中的路由過濾使用類似指令碼的語法，根據條件匹配字首並修改路由距離；其屬性對於匹配器和動作而言，分為可讀或可讀/可寫兩類。"
tags:
  - 'routing-filtering'
  - 'route-selection'
  - 'bgp'
source: https://manual.mikrotik.com/docs/user-guides/routing-and-networking-protocols/route-selection-and-filtering
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 路由過濾 {#route-filtering}

### 過濾器語法 {#filter-syntax}

路由過濾規則使用類似指令碼的語法。以下示例匹配來自子網 192.168.1.0/24 且字首長度大於 24 的字首，並將預設 distance 加 1。如果沒有匹配，則將預設 distance 減 1。

```ros
/routing/filter/rule
  add chain=myChain \
  rule="if (dst in 192.168.1.0/24 && dst-len>24) {set distance +1; accept} else {set distance -1; accept}"
```

一條過濾規則可以由多個匹配器和動作組成：

```text
if ( [matchers] ) { [actions] } else { [actions] }
```

屬性有兩種型別：

- 僅可讀 —— 值只讀且無法重寫的屬性。它們只能由匹配器使用。
- 可讀/可寫 —— 值可讀且可寫的屬性。它們可由過濾動作和匹配器使用。

僅對於數值屬性，可讀屬性可以透過其他可讀屬性或帶布林運算子的常量值進行匹配。

```text
[matchers]:
[prop readable] [bool operator] [prop readable]

[actions]:
[action] [prop writeable] [value]
```

如果匹配器只有一種可能的操作，則不需要布林運算子。

不帶布林運算子的示例：

```text
if ( protocol connected ) { accept }
```

帶布林運算子的示例：

```text
if ( bgp-med < 30 ) { accept }
```

對於可讀標誌屬性，匹配器不需要布林運算子或值。

```text
if ( ospf-dn ) { reject }
```

:::info
路由過濾鏈的預設動作是 `reject`。
:::

#### 僅可讀屬性 {#only-readable-properties}

| 屬性 | 型別 | 描述 |
| :-- | :-- | :-- |
| ***數值屬性*** |  |  |
| `dst-len` |  | 目的字首長度 |
| `bgp-path-len` |  | 當前 BGP AS-PATH 長度 |
| `bgp-input-local-as` |  | 字首傳送到的本地對等體的 AS 號 |
| `bgp-input-remote-as` |  | 接收字首的遠端對等體的 AS 號 |
| `bgp-output-local-as` |  | 將通告該字首的對等體的 AS 號 |
| `bgp-output-remote-as` |  | 將向前綴通告到的對等體的 AS 號 |
| `ospf-metric` |  | 當前 OSPF 度量 |
| `ospf-tag` |  | 當前 OSPF 標籤 |
| `rip-metric` |  | 當前 RIP 度量 |
| `rip-tag` |  | 當前 RIP 標籤 |
| ***標誌屬性*** |  |  |
| `active` |  | 指示路由是否處於活動狀態 |
| `bgp-atomic-aggregate` |  |  |
| `bgp-communities-empty` |  | 指示 BGP Communities 屬性是否為空 |
| `bgp-ext-communities-empty` |  | 指示 BGP Extended Communities 屬性是否為空 |
| `bgp-large-communities-empty` |  | 指示 BGP Large Communities 屬性是否為空 |
| `bgp-network` |  | 指示該字首是否源自 BGP 網路 |
| `ospf-dn` |  | 指示該 OSPF 路由是否設定了 DN 位。 |
| ***字首屬性*** |  |  |
| `dst` |  | 目的地 |
| `ospf-fwd` |  | 當前 OSPF 轉發地址 |
| `bgp-input-local-addr` |  | 字首傳送到的本地對等體的 IP 地址 |
| `bgp-input-remote-addr` |  | 接收字首的遠端對等體的 IP 地址 |
| `bgp-output-local-addr` |  | 將通告該字首的對等體的 IP 地址 |
| `bgp-output-remote-addr` |  | 將向前綴通告到的對等體的 IP 地址 |
| 其他屬性 |  |  |
| `afi` | `ipv4 \| ipv6 \| l2vpn \| l2vpn-cisco \| vpnv4 \| vpnv6` | 路由的地址族。 |
| `bgp-as-path` | `numeric_regexp` | AS 路徑 [正則表示式匹配](#as-path-regexp-matching) |
| `bgp-as-path-slow-legacy` | `string_regexp` | **已棄用**。極其緩慢的舊式 AS 路徑匹配。此引數僅應在從舊 ROS v6 配置遷移時作為臨時匹配器使用。[閱讀更多>>](#as-path-regexp-matching) |
| `chain` | `chain_name` |  |
| `origin` | `string` | 匹配路由的 origin 例項，例如，它可以匹配從特定 OSPF 例項匯入的路由：`if (origin <instance_name>) {}` |
| `ospf-type` | `ext1 \| ext2 \| inter \| intra \| nssa1 \| nssa2` | OSPF 路由的型別：<br/><ul><li>ext1 - 外部（Type 5 LSA），使用 type1 度量</li><li>ext2 - 外部（Type 5 LSA），使用 type2 度量</li><li>inter - 區域間路由（Type 3 LSA）</li><li>intra - 區域內路由（Type 1/2 LSA）</li><li>nssa1 - Type 7 LSA，使用 type1 度量</li><li>nssa2 - Type 7 LSA，使用 type2 度量</li></ul> |
| `protocol` | `bgp \| connected \| dhcp \| fantasy \| modem \| ospf \| rip \| static \| slaac \| vpn` | 路由匯入時所使用的協定型別。 |
| `rpki` | `invalid \| unknown \| valid \| unverified` | [RPKI](./unicast/rpki.md) 字首源驗證狀態 |
| `rpki-aspa` | `invalid \| unknown \| valid \| unverified` | 對 AS 路徑的 [ASPA](./unicast/rpki.md#aspa-validation) 驗證狀態 |
| `rtab` | `routing_table_name` | 路由匯入來源的路由表名稱 |
| `vrf` | `vrf_name` | 路由匯入來源的 VRF 名稱 |

#### 可寫屬性 {#writeable-properties}

| 屬性 | 型別 | 描述 |
| :-- | :-- | :-- |
| ***數值屬性*** |  |  |
| `distance` |  | 路由 distance |
| `scope` |  |  |
| `scope-target` |  | 目標 scope |
| `bgp-weight` |  | BGP WEIGHT 屬性 |
| `bgp-med` |  | BGP MED 屬性是路由器本地的。它也用於 iBGP 對等體的輸出。 |
| `bgp-out-med` |  | 要傳送給遠端對等體的 BGP MED 屬性。應在 eBGP 對等體的輸出鏈中使用。 |
| `bgp-local-pref` |  | BGP LOCALPREF 屬性 |
| `bgp-igp-metric` |  | BGP IGP 度量 |
| `bgp-path-peer-prepend` |  | 預置最後接收到的遠端對等體的 ASN。如果該字首源自本路由器，則此引數在路由器的輸出中不會產生任何作用，因為此時 ASN 還不存在。    如果在 BGP 輸入中用作匹配器，則可以過濾超過一定預置次數的字首。例如，如果遠端對等體將其 ASN 預置了 5 次，但我們希望最多允許 4 次預置的 ASN，則可以使用：`if (bgp-path-peer-prepend > 4) {reject}`    此引數還會覆蓋從遠端對等體接收到的任何預置，例如，如果遠端對等體將其 AS 預置了 3 次，我們可以透過在 BGP 輸入中設定 `bgp-path-peer-prepend 1` 來移除該預置 |
| `bgp-path-prepend` |  | 預置路由器的 ASN，應在 BGP 輸出中使用。 |
| `ospf-ext-metric` |  | OSPF 外部路由度量值 |
| `ospf-ext-tag` |  | OSPF 外部路由標籤 |
| `rip-ext-metric` |  | RIP 外部路由度量值 |
| `rip-ext-tag` |  | RIP 外部路由標籤 |
| ***標誌屬性*** |  |  |
| `ospf-ext-dn` |  | 外部 OSPF 路由的 DN 位 |
| `blackhole` |  | 黑洞路由 |
| `suppress-hw-offload` |  | 是否[抑制 L3 硬體解除安裝](../../bridging-and-switching/l3-hardware-offloading.md#suppressing-hw-offload) |
| `use-te-nexthop` |  |  |
| ***其他屬性*** |  |  |
| `gw` | `ipv4/6 address` | IPv4/IPv6 地址或介面名稱。在 BGP 輸出的情況下，可以在以下設定中調整閘道器：是 BGP 反射器；nexthop-choice 設定為 propagate；不是 eBGP 且未設定 nexthop-choice=force-self。 |
| `gw-ll` | `ipv6 address` | IPv6 鏈路本地下一跳屬性。在 BGP 輸出的情況下，可以在以下設定中調整閘道器：是 BGP 反射器；nexthop-choice 設定為 propagate；不是 eBGP 且未設定 `nexthop-choice=force-self`。 |
| `gw-interface` | `interface_name` | 閘道器的介面部分。當需要為下一跳附加特定介面時使用，例如（`1.2.3.4%ether1`） |
| `gw-check` | `none \| arp \| icmp \| bfd \| bfd-mh` |  |
| `pref-src` | `ipv4/6 address` |  |
| `bgp-origin` | `igp \| egp \| incomplete` |  |
| `ospf-ext-fwd` | `ipv4/6 address` | 外部 OSPF 路由的轉發地址 |
| `ospf-ext-type` | `type1 \| type2` | OSPF 外部路由型別 |
| `comment` | `string` |  |
| `bgp-communities` | `inline_community_set \| community_list_name` | BGP Communities 屬性定義於 [RFC 1997](https://tools.ietf.org/html/rfc1997)。每個 community 的大小為 32 位。 |
| `bgp-ext-communities` | `inline_ext_community_set \| ext_community_list_name` | BGP Extended Communities 屬性定義於 [RFC 4360](https://datatracker.ietf.org/doc/html/rfc8092)。RouterOS 會解析 `site-of-origin`（字首為 `soo:`）和 `route-target`（字首為 `rt:`）擴充套件 community。例如，`set bgp-ext-communities rt:1111:2.3.4.5;` 可以設定/匹配 64 位十六進位制的 RAW 擴充套件 community 值，例如，`set bgp-ext-communities 0x.........;` |
| `bgp-large-communities` | `inline_large_community_set \| large_community_list_name` | BGP Large Communities 屬性定義於 [RFC 8092](https://datatracker.ietf.org/doc/html/rfc8092)。適用於所有 ASN，包括 32 位 ASN。每個 community 長度為 12 位元組，由 3 部分組成：`global_admin:local_part_1:local_part_2`。 |

#### 命令 {#commands}

| 命令 | 引數 | 描述 |
| :-- | :-- | :-- |
| `accept` |  | 接受匹配的字首並停止處理該鏈。 |
| `reject` |  | 拒絕匹配的字首並停止處理該鏈，該字首將在記憶體中儲存為 "filtered"，並且不會成為被選為最佳路徑的候選。 |
| `return` |  | 返回父鏈 |
| `jump` | `jump chain_name` | 跳轉到指定鏈 |
| `unset` | `unset prop_name` | 用於取消設定以下屬性的值：`pref-src, bgp-med, bgp-out-med, bgp-local-pref` |
| `append` |  | 追加到列表或字串末尾。可以追加以下屬性值：`bgp-communities, bgp-ext-communities, bgp-large-communities, comment` |
| `filter` |  | 刪除操作的逆操作（刪除除指定值以外的所有內容）。可以過濾以下屬性的值：`bgp-communities, bgp-ext-communities, bgp-large-communities` |
| `delete` |  | 刪除指定屬性的值。可以刪除以下屬性的值：`bgp-communities, bgp-ext-communities, bgp-large-communities` |
| `set` | `prop_writeable value` | 該命令用於為可寫屬性設定新值。可以從匹配型別的其他可讀屬性設定值。對於數值屬性，可以在值前加上 +/-，這會將當前屬性值增加或減少給定數量。例如，`set bgp-local-pref +1` 會將當前 LOCAL\_PREF 增加一，或從另一個可讀數值屬性中提取值，`set distance +ospf-ext-metric` |
| `rpki-verify` | `rpki_group_name` | 從指定 RPKI 組在當前鏈中啟用 [RPKI](./unicast/rpki.md) 字首源驗證。 |
| `rpki-aspa-verify` | `rpki_group_name` | 從指定 RPKI 組在當前鏈中啟用 [ASPA](./unicast/rpki.md#aspa-validation) 驗證。 |

#### 運算子 {#operators}

##### 匹配器運算子 {#matcher-operators}

| 運算子 | 描述 | 示例 |
| :-- | :-- | :-- |
| `&&` | 邏輯 AND 運算子 | `if (dst in 192.168.0.0/16 && dst-len in 16-32) {reject;}` |
| `\|\|` | 邏輯 OR 運算子 | `if (dst in 192.168.0.0/16 \|\| dst-len in 16-32) {reject;}` |
| `not` | 邏輯 NOT 運算子 | `if (not bgp-network) {reject; }` |

##### 數值屬性運算子 {#num-prop-operators}

| 運算子 | 描述 |
| :-- | :-- |
| `in` | 如果值在提供的數值範圍內，則返回 true。數值範圍可以用以下格式表示：`{int..int}`、`{int-int}` |
| `==` | 如果數值相等，則返回 true |
| `!=` | 如果數值不相等，則返回 true |
| `>` | 如果左側數值大於右側數值，則返回 true |
| `<` | 如果左側數值小於右側數值，則返回 true |
| `>=` | 如果左側數值大於或等於右側數值，則返回 true |
| `<=` | 如果左側數值小於或等於右側數值，則返回 true |

##### 字首運算子 {#prefix-operators}

| 運算子 | 描述 |
| :-- | :-- |
| `in` | 如果該字首是所提供網路的子網，則返回 true。如果使用運算子來匹配地址列表中的字首（例如 `dst in list_name`），則它只會匹配完全相同的字首。 |
| `!=` | 如果字首不等於所提供的值，則返回 true |
| `==` | 如果字首等於所提供的值，則返回 true |

:::info
地址列表在設計上匹配主機地址，這意味著它也會匹配屬於地址列表中任何範圍的 /32 字首。要排除 /32 字首使其不被通告的變通方法是使用 dst-len：`if (dst in list_name && dst-len < 32) {}`
:::

##### BGP Community 運算子 {#bgp-community-operators}

| 運算子 | 描述 | 示例 |
| :-- | :-- | :-- |
| `equal` | 如果提供的社群等於路由的屬性值，則返回 true |  |
| `equal-list` | 如果提供的 `community-list` 中的社群等於路由的屬性值，則返回 true |  |
| `any` | 如果路由的屬性值包含所提供社群中的至少一個，則返回 true |  |
| `any-list` | 如果路由的屬性值包含所提供列表中的至少一個社群，則返回 true |  |
| `includes` | 如果路由的屬性值包含指定的社群，則返回 true |  |
| `includes-list` | 如果路由的屬性值包含指定 `communities-list` 中的所有社群，則返回 true |  |
| `subset` | 如果路由的社群子集與列表中的社群匹配，則返回 true | `1:1,3:3` 將匹配 `1:1,2:2,3:3` |
| `subset-list` | 與 `subset` 相同，但匹配社群列表中的社群。 |  |
| `any-regexp` | 與 `any` 相同，但透過 [regexp](#community-regexp-matching) 匹配 |  |
| `subset-regexp` | 與 `subset` 相同，但透過 [regexp](#community-regexp-matching) 匹配 |  |

:::info
如果路由不攜帶 community 屬性（該屬性為空或不存在），則 "any" 匹配器（`any`、`any-list`、`any-regexp`）返回 false — 沒有可供匹配的 community。"subset" 匹配器（`subset`、`subset-list`、`subset-regexp`）對空屬性返回 true，因為空集是任何集合的子集。要顯式檢查屬性是否為空，請使用 `bgp-communities-empty`、`bgp-ext-communities-empty` 或 `bgp-large-communities-empty`。
:::

##### 字串運算子 {#string-operators}

| 運算子 | 描述 |
| :-- | :-- |
| `find` | 檢查提供的子字串是否是屬性值的一部分 |
| `regexp` | 對屬性值進行字串正則表示式匹配 |

### 刪除 BGP Community {#deleting-bgp-communities}

路由過濾器允許使用 `delete` 命令清除 BGP community。`delete` 命令根據 community 的型別接受多個引數：

- **communities**：
  - `wk` - 將匹配並移除知名社群。
  - `other` - 將匹配並移除其他非知名社群。
  - `regexp` - 用於匹配應刪除社群的 regexp 模式。
  - `<community-list name>` - 從指定的 `community-list` 中刪除社群，包括匹配列表 `regexp` 條目的社群。
- **ext-communities**：
  - `rt` - 將匹配並移除 **RouteTarget**。
  - `soo` - 將匹配並移除 **Site-of-Origin**。
  - `other` - 將匹配並移除既不是 **RT** 也不是 **SOO** 的其他擴充套件社群。
  - `regexp` - 用於匹配應刪除擴充套件社群的 regexp 模式。
  - `<community-ext-list name>` - 從指定的 `community-ext-list` 中刪除社群，包括匹配列表 `regexp` 條目的擴充套件社群。
- **large-communities**：
  - `all` - 移除所有內容。
  - `regexp` - 用於匹配應刪除大型社群的 regexp 模式。
  - `<community-large-list name>` - 從指定的 `community-large-list` 中刪除大型社群，包括匹配列表 `regexp` 條目的大型社群。

可以指定多種 community 型別，例如刪除所有 SOO、其他型別的擴充套件 community 以及 community-ext 列表中的特定 RT：

```ros
/routing/filter/community-ext-list
add list=myRTList communities="rt:1.1.1.1:222"
/routing/filter/rule
add chain=myChain rule="delete bgp-ext-communities soo,other,myRTList;"
```

例如，刪除屬於管理域 65551 的所有大型社群，無論其餘值是什麼：

```ros
/routing/filter/rule
add chain=myChain rule="delete bgp-large-communities regexp \"^65551:[0-9]+:[0-9]+$\""
```

### AS-PATH 正則表示式匹配 {#as-path-regexp-matching}

AS 路徑是自治系統號（ASN）的序列。例如，AS 路徑 `123 456 789` 表示該路由源自 AS 789，並在到達目的地之前經過了 AS 456。要應用路由策略，可使用正則表示式（regexp）匹配 AS 路徑中的特定 AS 號或 AS 號集合。

處理 AS 路徑資料有兩種常見方式：

- 將整個 AS 路徑轉換為字串，並讓正則表示式對該字串進行操作（ROS v6 或 Cisco 風格）。
- 讓正則表示式將每個 AS 路徑條目作為數字進行操作（ROS v7、Juniper 風格）。

第一種方法按字元匹配。第二種方法按 AS 號匹配。與字串匹配方式相比，第二種方法更快且佔用資源更少。

這一變化要求管理員使用新的正則表示式策略。來自 RouterOS v6 的舊正則表示式模式不能直接複製貼上，因為它們可能導致語法錯誤或意外結果。

以這個基本的 AS 路徑過濾規則為例：

```ros
/routing/filter/rule
add chain=myChain rule="if (bgp-as-path .1234.) {accept}"
```

此正則表示式模式匹配 AS 路徑中間任意位置的 ASN 1234。使用舊式字串匹配方法時，相同的模式會匹配任何包含至少六個字元的 ASN 且包含子字串 `1234` 的 AS 路徑。等效的舊式模式是 `._1234_.`。

例如，舊式字串模式 `1234[5-9]` 會匹配字串中任意位置的 12345 到 12349。這會產生諸如 `12345 3434` 和 `11 9123467 22` 這樣的匹配。使用新式匹配器時，相同的模式會匹配包含精確 ASN 1234 後跟 5 到 9 的 ASN 的 AS 路徑，例如 `1234 7 111` 或 `111 1234 5 222`。它不匹配 `12345 3434`。

:::danger
在不同實現之間複製正則表示式模式可能會產生意外或危險的結果。

不要直接從 ROS v6 或 Cisco 配置中複製正則表示式模式，它們並不直接相容。在某些場景下，這可能導致意外甚至危險的配置。
:::

:::info
必須存在 AS-Path 引數，正則表示式匹配器才會被應用。這意味著無法使用正則表示式（即 `^$`）匹配不存在（空）的 AS-Path。應改用 `bgp-path-len`。
:::

#### 正則表示式測試工具 {#regex-testing-tool}

RouterOS 內建了正則表示式檢查工具，可幫助管理員驗證正則表示式。此工具還支援 num-list 值，因此你可以在將正則表示式應用到路由過濾器之前，針對任何 AS 路徑進行測試。

```ros
/routing/filter/num-list/add list=test range=100-1500

/routing/filter/test-as-path-regexp regexp="[[:test:]]5678\$" as-path="1234,5678"
```

#### 支援的運算子 {#supported-operators}

| 運算子 | 描述 | 示例 | 示例說明 | 示例匹配 |
| :-- | :-- | :-- | :-- | :-- |
| `^` | 表示路徑的開頭 | `^1234` | 將匹配以 ASN 1234 開頭的 AS 路徑 |  |
| `$` | 表示路徑的結尾 | `1234$` | 將匹配源 ASN 為 1234 的 AS 路徑 |  |
| `*` | 所列 ASN 出現零次或多次 | `^1234*$` | 將匹配空 AS 路徑，或 ASN 1234 可能出現多次也可能不出現的 AS 路徑 | **匹配：**  1234  1234 1234 1234  空路徑  **不匹配：**  1234 5678 |
| `+` | 所列 ASN 出現一次或多次 | `1234+` | 將匹配 ASN 1234 至少出現一次的 AS 路徑 | **匹配：**  1234  3 1234 6  **不匹配：**  12345 678 |
| `?` | 所列 ASN 出現零次或一次 | `^1234? 5678` | 將匹配可能以出現一次的 ASN 1234 開頭、也可能不是的 AS 路徑。 | **匹配**：  5678  1234 5678  **不匹配：**  1234 1234 5678  12345 5678 |
| `.` | 任意 ASN 出現一次 | `^.$` | 將匹配長度為 1 的任何 AS 路徑。 | **匹配：**  12345  45678  **不匹配：**  1234 5678 |
|  `\|`  | 匹配兩側兩個 ASN 之一 | `^(1234\|5678)` | 將匹配以 ASN 1234 或 5678 開頭的 AS 路徑 | **匹配**：  1234  5678  1234 5678  **不匹配：**  91011 |
| `[ ]`  `[^ ]` | 表示 AS 號的集合，其中列表中的一個 AS 號必須匹配。  在左方括號後使用 ^ 可對集合取反。  還可以使用 [[:numset\_name:]] 引用 [num-list](#community-and-num-lists) 中預定義的 num-list | `^[1234 5678 1-100]` | 將匹配以 1234 或 5678 或 1 到 100 範圍內的 AS 號開頭的 AS 路徑 | **匹配：**  1234  99  5678  **不匹配：**  101 |
| `()` | 要匹配的正則表示式項分組 | `^(1234$\|5678)` | 將匹配以 1234 開頭和結尾的 AS 路徑，或以 5678 開頭的 AS 路徑 | **匹配：**  1234  5678 9999  **不匹配：**  1234 5678 |

:::warning
不支援重複範圍 {}。
:::

### Community 和 Num 列表 {#community-and-num-lists}

可以從 `/routing/filter/num-list` 選單配置常用數字列表。這些數字列表可在過濾規則中使用，以簡化過濾器設定過程。

類似地，你還可以定義 community、擴充套件 community 和 large community 列表。Community 集合可用於匹配、追加和設定。

例如，匹配列表中的 community 並清除該屬性：

```ros
/routing/filter/community-list
add communities=111:222 list=myCommunityList

/routing/filter/rule
add chain=myChain rule="if (bgp-communities equal-list myCommunityList) {delete bgp-communities wk,other; accept;}"
```

社群列表中的每個條目要麼是一組具體社群值（`communities` 引數），要麼是正則表示式模式（`regexp` 引數），這兩個引數在每個條目中互斥。單個列表可以混合兩種型別的條目：

```ros
/routing/filter/community-list/add list=myList communities=65551:100
/routing/filter/community-list/add list=myList regexp="^65551:.*"
```

### 社群正則表示式匹配 {#community-regexp-matching}

與作用於 AS 號的 AS-path 正則表示式匹配不同，社群正則表示式匹配作用於屬性的 **字串表示**。正則表示式應用於屬性中 **每個單獨社群** 的列印形式，即路由 `print detail` 輸出中顯示的相同形式：

| 社群型別 | 字串表示 | 示例 |
| :-- | :-- | :-- |
| BGP 社群（RFC 1997） | `asn:value`，兩個欄位均為十進位制。知名社群用其名稱表示：`internet`、`graceful-shutdown`、`accept-own`、`accept-own-nh`、`filter-4`、`filter-6`、`filter-xlate-4`、`filter-xlate-6`、`LLGR-stale`、`no-LLGR`、`blackhole`、`no-export`、`no-advertise`、`local-as`、`nopeer` | <code>65551:100</code><br/><code>no-export</code> |
| BGP 擴充套件社群（RFC 4360） | 型別化形式：`rt:`（route target）或 `soo:`（site of origin）字首後跟採用 `asn:value`、`ipv4:value` 或 `asn4:value` 形式的值（寫入四位元組欄位的兩位元組 AS 號會帶 `L` 字尾列印）。其他可識別的型別列印為 `encap:`、`es-label:`、`es-import:` 或 `mobility:` 值；所有其他擴充套件社群列印為 `raw:<hex>` | <code>rt:65551:100</code><br/><code>soo:1.2.3.4:5</code><br/><code>rt:65000L:10</code> |
| BGP 大型社群（RFC 8092） | `global-admin:local-part-1:local-part-2`，每個欄位列印為十進位制 32 位整數。三個欄位始終存在，包括零值 | `65551:0:100` |

該正則表示式使用與路由過濾器中的 `comment regexp` 匹配器相同的 RouterOS 正則表示式引擎。其語法類似 POSIX ERE，支援 `^`、`$`、`.`、`*`、`+`、`?`、`|`、`()` 以及字元類 `[ ]`、`[^ ]`。不支援重複次數界限 `{n,m}`。反斜槓轉義單個字面字元，因此 `\d` 匹配字母 `d`。數字請使用 `[0-9]`。匹配區分大小寫且不錨定。使用 `^` 和 `$` 匹配整個字串。指令碼中的 `~` 運算子使用不同的正則表示式實現，因此模式並不總是可互換。

例如，拒絕攜帶來自管理域 7010 的任何大型社群的路由：

```ros
/routing/filter/community-large-list/add list=lcom7010 regexp="^7010:[0-9]+:[0-9]+$"

/routing/filter/rule
add chain=bgp-in rule="if (bgp-large-communities any-list lcom7010) {reject;}"
```

社群列表中的正則表示式條目可用於匹配（`any-list`、`includes-list`、`subset-list`、`equal-list`），也可與 `delete`/`filter` 命令一起使用；在後一種情況下，匹配列表中某個正則表示式條目的社群會被移除。只有具有具體社群值的條目才會由 `append` 和 `set` 命令寫入；正則表示式是匹配模式，而不是可寫入屬性的值。請注意，使用不包含具體值的列表（空列表或僅含正則表示式的列表）執行 `set` 會將屬性替換為空集（清除它），而在這種情況下 `append` 不執行任何操作。

## 路由選擇 {#route-selection}

路由選擇規則控制如何從可用的候選路由中選擇輸出路由。預設情況下，如果未設定選擇規則，則輸出會選擇最佳路由。

以下路由表顯示了兩個候選路由和一個最佳路由。預設情況下，當 BGP 選擇要傳送出去的路由時，它會選擇活動路由。

```text
[admin@4] /routing/route> print where dst-address=1.0.0.0/24
Flags: A - ACTIVE; b, y - COPY
Columns: DST-ADDRESS, GATEWAY, AFI, DISTANCE, SCOPE, TARGET-SCOPE, IMMEDIATE-GW
   DST-ADDRESS  GATEWAY         AFI  DISTANCE  SCOPE  TARGET-SCOPE  IMMEDIATE-GW
 b 1.0.0.0/24   10.155.101.217  ip4        19     40            30  10.155.109.254%ether1
Ab 1.0.0.0/24   10.155.101.232  ip4        20     40            30  10.155.109.254%ether1
 b 1.0.0.0/24   10.155.101.231  ip4        20     40            30  10.155.109.254%ether1
```

如果需要優先選擇非活動路由，請使用選擇規則。

RouterOS 中的選擇規則從 `/routing/filter/select-rule` 選單配置。

選擇規則還可以呼叫路由過濾器，從而由過濾規則來選擇路由。例如，要模擬預設的輸出選擇，請使用以下規則集：

```ros
/routing/filter/rule
add chain=get_active rule="if (active) {accept}"

/routing/filter/select-rule
add chain=my_select_chain do-where=get_active
```

選擇規則還可用於限制為 BGP Add-path 選取多少條額外路徑，例如最多 3 條路徑：

```ros
/routing/filter/select-rule add chain=select-for-addpath do-take=3
```

## 路由過濾嚮導 {#routing-filter-wizard}

由於使用類似指令碼的語法編寫過濾規則較為複雜，因此引入了路由過濾嚮導，它可以生成類似 ROSv6 語法的過濾規則。

快速演示：

```routeros
[admin@CCR2004_2XS_111] /routing/filter> filter-wizard <tab>
action        dst                   ospf-type         scope-target      set-gw-check                use-te-nexthop
afi           dst-len               protocol          set-bgp-...       set-scope
bgp-...       gateway               routing-table     set-blackhole     set-scope-target
blackhole     jump-target-chain     rpki              set-comment       set-suppress-hw-offload
chain         match-chain           rpki-verify       set-distance      set-use-te-nexthop
distance      ospf-metric           scope             set-gateway       suppress-hw-offload

[admin@CCR2004_2XS_111] /routing/filter> filter-wizard action=accept chain=vpn-in afi=vpnv4 set-bgp-ext-communities=rt:2:2
  result: Filter rule 'if (afi vpnv4) { set bgp-ext-communities rt:2:2; accept; }' added

[admin@CCR2004_2XS_111] /routing/filter> /routing/filter/rule/print
Flags: X - disabled, I - inactive
 0   ;;; added by filter-wizard
     chain=vpn-in rule="if (afi vpnv4) { set bgp-ext-communities rt:2:2; accept; }"
```

過濾嚮導會將規則新增到列表末尾，併為其添加註釋 `added by filter-wizard`。

當你嘗試新增包含不可接受值的過濾器時，返回的錯誤會列印到 CLI，並以 `route,error` 主題記錄到系統日誌中。

```routeros
[admin@CCR2004_2XS_111] /routing/filter> filter-wizard action=accept chain=vpn-in afi=vpnv4 match-chain=vpn-in
  result: Error adding 'if (chain vpn-in && afi vpnv4) { accept; }'match with 'vpn-in' creates chain loop (6)

[admin@CCR2004_2XS_111] /routing/filter> /log/print
 2025-05-19 13:05:15 route,error Error adding 'if (chain vpn-in && afi vpnv4) { accept; }'match with 'vpn-in' creates chain loop (6)

```
