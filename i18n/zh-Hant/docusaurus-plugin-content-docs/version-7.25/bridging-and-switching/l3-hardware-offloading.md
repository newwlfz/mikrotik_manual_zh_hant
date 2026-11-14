---
sidebar_key: "bridging-and-switching/l3-hardware-offloading"
sidebar_position: 2
title: "L3 硬體解除安裝"
sidebar_label: "L3 硬體解除安裝"
description: "L3 Hardware Offloading 透過將 CPU 密集型任務解除安裝到交換晶片，實現線速路由。本頁詳細介紹如何為整個交換器、單個埠配置 L3HW，以及如何配置 IPv6 支援和 FastTrack 解除安裝等全域性設定，並給出關於可能影響現有連線的警告。"
tags:
  - 'l3hw'
  - 'switching'
source: https://manual.mikrotik.com/docs/7.25/bridging-and-switching/l3-hardware-offloading
captured_at: '2026-11-04T11:14:21+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

**三層硬體解除安裝**（**L3HW**，也稱為 IP 交換或 HW 路由）允許將部分路由器功能解除安裝到交換晶片上。這使得路由封包時能夠達到線速，而僅靠 CPU 根本無法做到。

## 交換器配置 {#switch-configuration}

要啟用三層硬體解除安裝，請為交換器設定 `l3-hw-offloading=yes`：

```ros
/interface/ethernet/switch/set 0 l3-hw-offloading=yes
```

### 交換器埠配置 {#switch-port-configuration}

可以為每個物理交換器埠配置三層硬體解除安裝。例如：

```ros
/interface/ethernet/switch/port/set sfp-sfpplus1 l3-hw-offloading=yes
```

請注意，交換器和埠的 l3hw 設定不同：

- 為交換器設定 `l3-hw-offloading``=no` 會完全停用解除安裝——所有封包都將由 CPU 路由。
- 但是，為交換器埠設定 `l3-hw-offloading``=no` 僅會停用往返該特定埠的硬體路由。此外，該埠仍可參與 Fasttrack 連線解除安裝。

要啟用完整的硬體路由，請在所有交換器埠上啟用 l3hw：

```ros
/interface/ethernet/switch/set 0 l3-hw-offloading=yes
/interface/ethernet/switch/port/set [find] l3-hw-offloading=yes
```

要使所有封包先經過 CPU，並僅解除安裝 Fasttrack 連線，請在所有埠上停用 l3hw，但在交換晶片本身上保持啟用：

```ros
/interface/ethernet/switch/set 0 l3-hw-offloading=yes
/interface/ethernet/switch/port/set [find] l3-hw-offloading=no
```

:::info
**當入埠和出埠都設定了 `l3-hw-offloading=yes` 時，封包由硬體路由。**

如果入埠和出埠都設定了 `l3-hw-offloading=no`，封包將經過 CPU/防火牆，同時僅解除安裝 Fasttrack 連線。

可以透過僅在出埠上設定 `l3-hw-offloading=no` 來讓封包經過 CPU/防火牆。然而，僅在入埠上設定 `l3-hw-offloading=no` 可能導致不可預測的行為，例如封包仍可能由硬體路由並完全繞過 CPU/防火牆。
:::

下一個示例在所有埠上啟用硬體路由，但上行埠（sfp-sfpplus16）除外。往返 sfp-sfpplus16 的封包將進入 CPU，因此會接受防火牆/NAT 處理。

```ros
/interface/ethernet/switch/set 0 l3-hw-offloading=yes
/interface/ethernet/switch/port/set [find] l3-hw-offloading=yes
/interface/ethernet/switch/port/set sfp-sfpplus16 l3-hw-offloading=no
```

:::warning
現有連線可能不受 `l3-hw-offloading` 設定更改的影響。
:::

### L3HW 設定 {#l3hw-settings}

設定選單 [`/interface/ethernet/switch/l3hw-settings`](../cli-reference/interface/ethernet/switch/l3hw-settings/index.md) 可用於根據設定需求調整 L3HW 行為。

### 介面列表 {#interface-lists}

無法直接使用介面列表來控制 `l3-hw-offloading`，因為介面列表可能包含虛擬介面（例如 VLAN），而 `l3-hw-offloading` 設定只能應用於物理交換器埠。例如，如果同一個交換器埠（trunk 埠）上執行著兩個 VLAN 介面（vlan20 和 vlan30），則無法在 vlan20 上啟用硬體路由而同時在 vlan30 上保持停用。

但是，介面列表可以用作埠選擇器。以下示例演示如何在 LAN 埠（屬於 "LAN" 介面列表的埠）上啟用硬體路由，並在 WAN 埠上停用它：

```ros
:foreach i in=[/interface/list/member/find where list=LAN] do={
    /interface/ethernet/switch/port/set [/interface/list/member/get $i interface] l3-hw-offloading=yes
}

:foreach i in=[/interface/list/member/find where list=WAN] do={
    /interface/ethernet/switch/port/set [/interface/list/member/get $i interface] l3-hw-offloading=no
}
```

請注意，由於介面列表不直接用於硬體路由控制，**修改介面列表也不會自動反映到 l3hw 更改中**。例如，將交換器埠新增到 "LAN" 介面列表並不會自動在其上啟用 `l3-hw-offloading`。使用者必須重新執行上述指令碼才能應用更改。

### MTU {#mtu}

硬體最多支援 8 個 MTU 配置檔案，這意味著使用者最多可為介面設定 8 個不同的 MTU 值：預設值 1500 + 七個自定義值。

:::tip
建議在更改介面上的 MTU/L2MTU 值時停用 `l3-hw-offloading`。
:::

**MTU 更改示例**

```ros
/interface/ethernet/switch/set 0 l3-hw-offloading=no
/interface/set sfp-sfpplus1 mtu=9000 l2mtu=9022
/interface/set sfp-sfpplus2 mtu=9000 l2mtu=9022
/interface/set sfp-sfpplus3 mtu=10000 l2mtu=10022
/interface/ethernet/switch/set 0 l3-hw-offloading=yes
```

### 二層依賴 {#layer-2-dependency}

三層硬體處理位於二層硬體處理之上。因此，L3HW 解除安裝要求底層介面啟用 L2HW 解除安裝。後者預設啟用，但有一些例外。例如，帶有 Marvell Prestera 交換器的 MikroTik 裝置僅支援一個硬體網橋。如果有多個網橋，其他網橋由 CPU 處理，並且不受 L3HW 影響。

另一個例子是 ACL 規則。如果規則將流量重定向到 CPU 進行軟體處理，則不會觸發硬體路由（L3HW）：

#### 用於停用特定埠硬體處理的 ACL 規則 {#acl-rule-to-disable-hardware-processing-on-a-specific-port}

```ros
/interface/ethernet/switch/rule/add switch=switch1 ports=ether1 redirect-to-cpu=yes
```

:::tip
建議在配置二層時關閉 L3HW 解除安裝。
:::

為確保三層在軟體和硬體兩方面都與二層保持同步，我們建議在配置二層功能時停用 L3HW。該建議適用於以下配置：

- 新增/移除/啟用/停用網橋。
- 向網橋新增/從網橋移除交換器埠。
- 繫結交換器埠 / 移除繫結。
- 更改 VLAN 設定。
- 更改交換器埠上的 MTU/L2MTU。
- 更改乙太網（MAC）地址。

簡而言之，在 `/interface/bridge/` 和 `/interface/vlan/` 下進行更改時，請停用 `l3-hw-offloading`：

#### 二層配置模板 {#layer-2-configuration-template}

```ros
/interface/ethernet/switch/set 0 l3-hw-offloading=no

/interface/bridge
# 在此处放置 bridge 配置更改

/interface/vlan
# 定义/更改 VLAN 接口
/interface/ethernet/switch/set 0 l3-hw-offloading=yes
```

### MAC telnet {#mac-telnet}

當在 **98DX8xxx**、**98DX4xxx,** 或 **98DX325x** 交換晶片上啟用 L3HW 解除安裝時，MAC telnet 存在限制。來自 MAC Telnet 的封包會被丟棄且不會到達 CPU，因此對裝置的訪問將失敗。

如果希望將 MAC telnet 與 L3HW 結合使用，可以建立特定的 ACL 規則來強制這些封包進入 CPU。

例如，如果需要在 sfp-sfpplus1 和 sfp-sfpplus2 上使用 MAC telnet 訪問，則需要新增此 ACL 規則。使用 `ports` 設定還可以選擇更多介面。

```ros
/interface/ethernet/switch/rule
add dst-port=20561 ports=sfp-sfpplus1,sfp-sfpplus2 protocol=udp redirect-to-cpu=yes switch=switch1
```

### VLAN 間路由 {#inter-vlan-routing}

由於 L3HW 依賴於 L2HW，而 L2HW 負責 VLAN 處理，因此 VLAN 間*硬體*路由通常需要底層有硬體網橋。即使某個 VLAN 只有一個帶標籤的埠成員，該埠也必須是網橋成員，並且 VLAN 介面必須分配給網橋。

配備 Marvell 98DX7xxx 系列交換晶片的裝置是一個例外——它們還支援直接在乙太網交換器埠上建立的 VLAN 介面之間的硬體路由，無需網橋：

`/interface/vlan/add interface=ether2 name=vlan20 vlan-id=20`

在所有其他 L3HW 裝置上，不要將 VLAN 介面直接分配給交換器埠——此類介面不會被解除安裝，其流量由 CPU 路由。請改為將 VLAN 介面分配給網橋。這樣，VLAN 配置會被解除安裝到硬體，並且在啟用 L3HW 的情況下，流量會經過 VLAN 間硬體路由。

#### VLAN 配置示例 {#vlan-configuration-example}

```ros
/interface/ethernet/switch/set 0 l3-hw-offloading=no
/interface/bridge/port/add bridge=bridge interface=ether2
/interface/bridge/vlan/add bridge=bridge tagged=bridge,ether2 vlan-ids=20
/interface/vlan/add interface=bridge name=vlan20 vlan-id=20
/ip/address/add address=192.0.2.1/24 interface=vlan20
/interface/bridge/set bridge vlan-filtering=yes
/interface/ethernet/switch/set 0 l3-hw-offloading=yes
```

:::info
對於 VLAN 間路由，網橋介面必須是每個可路由的 `/interface/bridge/vlan/` 條目的帶標籤成員。
:::

### 按 VLAN 解除安裝 {#per-vlan-offloading}

可以使用 `/interface/vlan` 選單中的 `l3-hw-offloading=yes|no` 設定，為各個 VLAN 介面配置 L3HW 解除安裝。這樣可以更精細地控制哪些 VLAN（及其相關路由）被解除安裝到交換晶片，哪些由 CPU 處理。不再需要為了停用特定 VLAN 的 L3HW 路由而在交換器埠上停用 L3HW。

僅當滿足以下所有條件時，VLAN 介面才會被解除安裝（獲得 H 標記）：

- VLAN 介面設定了 `l3-hw-offloading=yes`。
- VLAN 介面建立在硬體解除安裝的、啟用 vlan-filtering 的網橋上，或者在 98DX7xxx 交換器上，直接建立在乙太網交換器埠上。
- 所有涉及的交換器埠都設定了 l3-hw-offloading=yes——對於網橋情況，是 VLAN 的所有成員埠；對於直接建立在交換器埠上的 VLAN 介面，是父埠。

對於 VLAN 間路由，入站和出站 VLAN 都必須被硬體解除安裝，否則封包會被髮送到 CPU。

:::info
如果某個交換器埠承載多個具有不同 L3HW 設定的 VLAN，請保持該埠的 `l3-hw-offloading=yes`。
:::

### L3HW MAC 地址範圍限制（僅限 DX2000/DX3000 系列） {#l3hw-mac-address-range-limitation-dx2000dx3000-series-only}

Marvell Prestera DX2000 和 DX3000 交換晶片存在硬體限制，對於每個介面，只能配置 MAC 地址的最後一個（最低有效）位元組。其他五個（最高有效）位元組是全域性配置的，因此對於所有介面（交換器埠、網橋、VLAN）必須相同。換句話說，MAC 地址必須採用 "**XX:XX:XX:XX:XX:??**" 格式，其中：

- "**XX:XX:XX:XX:XX**" 部分對所有介面都是通用的。
- "**??**" 是可變部分。

**此要求僅適用於三層（路由）。** 二層（橋接）不使用交換器的乙太網地址。此外，它不適用於網橋埠，因為網橋埠使用網橋的 MAC 地址。

五個位元組必須相同的要求適用於：

- 啟用了硬體路由的獨立交換器埠（不是網橋成員）（`l3-hw-offloading=yes`）。
- 網橋本身。
- VLAN 介面（預設使用網橋 MAC 地址的介面）。

## 路由配置 {#route-configuration}

---

### 抑制硬體解除安裝 {#suppressing-hw-offload}

預設情況下，所有路由都是硬體候選路由。為了進一步微調要解除安裝的流量，每條路由都有一個選項可以停用/啟用 **`suppress-hw-offload`**。

例如，如果我們知道大部分流量流向伺服器所在的網路，我們可以僅對該特定目的地啟用解除安裝：

```ros
/ip/route/set [find where static && dst-address!="192.168.3.0/24"] suppress-hw-offload=yes
```

現在只有到 192.168.3.0/24 的路由具有 H 標記，表明它將是唯一有資格被選擇進行硬體解除安裝的路由：

```ros
[admin@MikroTik] > /ip/route/print where static
Flags: A - ACTIVE; s - STATIC, y - COPY; H - HW-OFFLOADED
Columns: DST-ADDRESS, GATEWAY, DISTANCE
#     DST-ADDRESS       GATEWAY         D
0 As  0.0.0.0/0         172.16.2.1      1
1 As  10.0.0.0/8        10.155.121.254  1
2 AsH 192.168.3.0/24    172.16.2.1      1
```

:::danger
H 標誌並不表示該路由實際上已被硬體解除安裝；它僅表示該路由可以被選中進行硬體解除安裝。
:::

### 路由過濾器 {#routing-filters}

對於 OSPF 和 BGP 等動態路由協定，可以使用[路由過濾器](../user-guides/routing-and-networking-protocols/route-selection-and-filtering.md)來抑制硬體解除安裝。例如，要抑制所有 OSPF 例項路由的硬體解除安裝，請使用 "**`suppress-hw-offload yes`**" 屬性：

```ros
/routing/ospf/instance
set [find name=instance1] in-filter-chain=ospf-input
/routing/filter/rule
add chain="ospf-input" rule="set suppress-hw-offload yes; accept"
```

### 解除安裝 Fasttrack 連線 {#offloading-fasttrack-connections}

防火牆過濾規則具有用於 Fasttrack 的 **`hw-offload`** 選項，允許微調連線解除安裝。由於用於 Fasttrack 連線的硬體記憶體非常有限，我們可以選擇要解除安裝的連線型別，從而受益於接近線速的流量。下一個示例僅解除安裝 TCP 連線，而 UDP 封包透過 CPU 路由，不佔用硬體記憶體：

```ros
/ip/firewall/filter
add action=fasttrack-connection chain=forward connection-state=established,related hw-offload=yes protocol=tcp
add action=fasttrack-connection chain=forward connection-state=established,related hw-offload=no
add action=accept chain=forward connection-state=established,related
```

### 無狀態硬體防火牆 {#stateless-hardware-firewall}

雖然連線跟蹤和有狀態防火牆只能由 CPU 執行，但硬體可以透過[交換器規則 (ACL)](./marvell-prestera-switch-chip-features.md#switch-rules-acl)執行無狀態防火牆。下一個示例阻止（在硬體層面）從 ether1 訪問 MySQL 伺服器，並將來自 ether2 和 ether3 的封包重定向到 CPU/防火牆：

```ros
/interface/ethernet/switch/rule
add switch=switch1 dst-address=10.0.1.2/32 dst-port=3306 ports=ether1 new-dst-ports=""
add switch=switch1 dst-address=10.0.1.2/32 dst-port=3306 ports=ether2,ether3 redirect-to-cpu=yes
```

### 交換器規則 (ACL) 與 Fasttrack 硬體解除安裝 {#switch-rules-acl-vs-fasttrack-hw-offloading}

某些防火牆規則既可以透過[交換器規則 (ACL)](./marvell-prestera-switch-chip-features.md#switch-rules-acl)實現，也可以透過 CPU [防火牆過濾器](../firewall-and-quality-of-service/firewall/filter.md) + Fasttrack 硬體解除安裝實現。兩種選項都能提供接近線速的效能。那麼問題是要使用哪一種？

首先，[並非所有裝置都支援 Fasttrack 硬體解除安裝](./l3-hardware-offloading.md#l3hw-device-support)，並且在沒有硬體解除安裝的情況下，防火牆過濾器僅使用軟體路由，這比其硬體對應方案慢得多。其次，即使 Fasttrack 硬體解除安裝是一個選項，經驗法則是：

:::tip
只要有可能，就始終使用交換器規則（ACL）。
:::

交換器規則與 Fasttrack 連線共享硬體記憶體。但是，會為每個 Fasttrack 連線分配硬體資源，而單條 ACL 規則可以匹配多個連線。例如，如果有一個訪客 WiFi 網路連線到 sfp-sfpplus1 VLAN 10，並且你不希望它訪問內部網路，只需建立一條 ACL 規則：

```ros
/interface/ethernet/switch/rule
add switch=switch1 ports=sfp-sfpplus1 vlan-id=10 dst-address=10.0.0.0/8 new-dst-ports=""
```

匹配的封包將在硬體層面被丟棄。這比讓*所有*訪客封包進入 CPU 進行防火牆過濾要好得多。

當然，ACL 規則無法匹配所有內容。例如，ACL 規則無法過濾連線狀態：接受已建立連線，丟棄其他連線。這時 Fasttrack 硬體解除安裝就派上用場——預設將封包重定向到 CPU 進行防火牆過濾，然後解除安裝已建立的 Fasttrack 連線。但是，為整個交換器或埠停用 `l3-hw-offloading` 並不是唯一的選擇。

:::info
使用 `redirect-to-cpu=yes` 定義 ACL 規則，而不是在交換器埠上設定 `l3-hw-offloading=no`，以縮小進入 CPU 的流量範圍。
:::

### 硬體解除安裝的 VRF {#hardware-offloaded-vrf}

[98DX8xxx、98DX4xxx、98DX325x、98CX8410](#ccr2xxx-crs3xx-crs5xx-switch-98dx8xxx-and-98dx4xxx-series) 和 [98DX7xxx](#crs8xx-switch-98dx7xxx-series) 交換晶片支援硬體解除安裝的 VRF。 [98DX3xxx 和 98DX2xxx](#crs3xx-switch-98dx3xxx-and-98dx2xxx-series) 系列不支援。

如果路由位於 VRF 中且出介面支援 L3HW，交換晶片將路由該封包。你可以將任何支援 L3HW 的介面（乙太網、繫結、網橋、VLAN）與 VRF 關聯。始終將主介面與 VRF 關聯，而不是與標記了 `S`（從屬）標誌的介面關聯，例如網橋埠或繫結埠。Fasttrack、NAT 和 VXLAN 解除安裝僅限於 `main` 路由表。

VRF 在 `/ip/vrf` 下配置。有關更多詳細資訊，請參閱 [VRF](../user-guides/routing-and-networking-protocols/vrf.md) 手冊。

98DX8208、98DX8212、98DX8332、98DX3257、98DX3255 最多支援 512 個 VRF 表。所有其他受支援的交換晶片最多支援 1024 個。

#### 透過 ACL 分配 VRF {#vrf-assignment-via-acl}

L3HW 支援使用 ACL 交換器規則為入站流量分配 VRF。`/interface/ethernet/switch/rule` 中的 `new-vrf` 選項允許將匹配的封包定向到特定 VRF 表。

在不支援 VRF 的交換器（98DX3xxx 和 98DX2xxx 系列）上，將 `new-vrf` 設定為 `main` 以外的任何值都會導致 `redirect-to-cpu=yes`。

有關 ACL 規則的更多詳細資訊，請參閱[交換器規則 (ACL)](./marvell-prestera-switch-chip-features.md#switch-rules-acl)。

## 配置示例 {#configuration-examples}

---

### 上行埠位於防火牆/NAT 之後的 VLAN 間路由 {#inter-vlan-routing-with-upstream-port-behind-firewallnat}

此示例演示如何在保持防火牆和 NAT 在上行埠上執行的同時，受益於接近線速的 VLAN 間路由。此外，到上行埠的 Fasttrack 連線也會被解除安裝到硬體，從而將流量速度提升到接近線速水平。VLAN 間流量完全由硬體路由，不進入 CPU/防火牆，因此不會佔用 Fasttrack 連線的硬體記憶體。

我們使用 **CRS317-1G-16S+** 型號，設定如下：

- sfp1-sfp4 - 橋接埠，VLAN ID 20，未標記。
- sfp5-sfp8 - 橋接埠，VLAN ID 30，未標記。
- sfp16 - 上行埠。
- ether1 - 管理埠。

設定介面列表以便於訪問：

### 介面列表 {#interface-lists-1}

```ros
/interface/list
add name=LAN
add name=WAN
add name=MGMT 

/interface/list/member
add interface=sfp-sfpplus1 list=LAN
add interface=sfp-sfpplus2 list=LAN
add interface=sfp-sfpplus3 list=LAN
add interface=sfp-sfpplus4 list=LAN
add interface=sfp-sfpplus5 list=LAN
add interface=sfp-sfpplus6 list=LAN
add interface=sfp-sfpplus7 list=LAN
add interface=sfp-sfpplus8 list=LAN
add interface=sfp-sfpplus16 list=WAN
add interface=ether1 list=MGMT 
```

### 網橋設定 {#bridge-setup}

```ros
/interface/bridge
add name=bridge vlan-filtering=yes

/interface/bridge/port
add bridge=bridge interface=sfp-sfpplus1 pvid=20
add bridge=bridge interface=sfp-sfpplus2 pvid=20
add bridge=bridge interface=sfp-sfpplus3 pvid=20
add bridge=bridge interface=sfp-sfpplus4 pvid=20
add bridge=bridge interface=sfp-sfpplus5 pvid=30
add bridge=bridge interface=sfp-sfpplus6 pvid=30
add bridge=bridge interface=sfp-sfpplus7 pvid=30
add bridge=bridge interface=sfp-sfpplus8 pvid=30

/interface/bridge/vlan
add bridge=bridge tagged=bridge untagged=sfp-sfpplus1,sfp-sfpplus2,sfp-sfpplus3,sfp-sfpplus4 vlan-ids=20
add bridge=bridge tagged=bridge untagged=sfp-sfpplus5,sfp-sfpplus6,sfp-sfpplus7,sfp-sfpplus8 vlan-ids=30
```

路由需要專用 VLAN 介面。對於標準二層 VLAN 橋接（不使用 VLAN 間路由），可以省略下一步。

#### 用於路由的 VLAN 介面設定 {#vlan-interface-setup-for-routing}

```ros
/interface/vlan
add interface=bridge name=vlan20 vlan-id=20
add interface=bridge name=vlan30 vlan-id=30

/ip/address
add address=192.168.20.17/24 interface=vlan20 network=192.168.20.0
add address=192.168.30.17/24 interface=vlan30 network=192.168.30.0
```

配置管理埠和上行埠、基本防火牆、NAT，並啟用 Fasttrack 連線的硬體解除安裝：

#### 防火牆設定 {#firewall-setup}

```ros
/ip/address
add address=192.168.88.1/24 interface=ether1
add address=10.0.0.17/24 interface=sfp-sfpplus16

/ip/route
add gateway=10.0.0.1

/ip/firewall/filter
add action=fasttrack-connection chain=forward connection-state=established,related hw-offload=yes
add action=accept chain=forward connection-state=established,related

/ip/firewall/nat
add action=masquerade chain=srcnat out-interface-list=WAN
```

此時，所有路由仍由 CPU 執行。在交換晶片上啟用硬體路由：

#### 啟用三層硬體解除安裝 {#enable-layer-3-hardware-offloading}

```ros
# 在 LAN 端口上启用完全硬件路由
:foreach i in=[/interface/list/member/find where list=LAN] do={ 
    /interface/ethernet/switch/port/set [/interface/list/member/get $i interface] l3-hw-offloading=yes 
} 

# 在 WAN 或 Management 端口上禁用完全硬件路由
:foreach i in=[/interface/list/member/find where list=WAN or list=MGMT] do={ 
    /interface/ethernet/switch/port/set [/interface/list/member/get $i interface] l3-hw-offloading=no 
}

# 在交换芯片上激活三层硬件卸载
/interface/ethernet/switch/set 0 l3-hw-offloading=yes
```

結果：

- 在同一 VLAN 內（例如 sfp1-sfp4），流量由硬體在二層轉發 *(L2HW)*。
- VLAN 間流量（例如 sfp1-sfp5）由硬體在三層路由 *(L3HW).*
- 往返 WAN 埠的流量首先由 CPU/防火牆處理。然後 Fasttrack 連線被解除安裝到硬體 *(硬體加速的 L4 有狀態防火牆).* NAT 同時應用於 CPU 和硬體處理的封包。
- 到管理埠的流量受防火牆保護。

## 典型錯誤配置 {#typical-misconfiguration}

---
以下是配置三層硬體解除安裝時常見的使用者錯誤。

### 交換器埠或繫結上的 VLAN 介面 {#vlan-interface-on-a-switch-port-or-bond}

```ros
/interface/vlan
add name=vlan10 vlan-id=10 interface=sfp-sfpplus1
add name=vlan20 vlan-id=20 interface=bond1
```

由於二層依賴性，在大多數裝置上，只有在硬體解除安裝的、啟用 vlan-filtering 的網橋上建立的 VLAN 介面才能進行 L3HW 解除安裝。正確的配置是：

```ros
/interface/bridge/port
add bridge=bridge1 interface=sfp-sfpplus1 frame-types=admit-only-vlan-tagged
add bridge=bridge1 interface=bond1 frame-types=admit-only-vlan-tagged
 
/interface/bridge/vlan
add bridge=bridge1 tagged=bridge1,sfp-sfpplus1 vlan-ids=10
add bridge=bridge1 tagged=bridge1,bond1 vlan-ids=20
 
/interface/vlan
add name=vlan10 vlan-id=10 interface=bridge1
add name=vlan20 vlan-id=20 interface=bridge1
```

:::warning
如果在不支援解除安裝此類介面的裝置上直接在 Ethernet 或 bonding 介面上建立 VLAN 介面（參見 [VLAN 間路由](#inter-vlan-routing)），封包可能會被錯誤地解除安裝——繞過 CPU 處理（例如防火牆和 NAT），並導致未定義行為。

如果需要這種型別的配置，必須在 `/interface/ethernet/switch/port` 選單下透過設定 `l3-hw-offloading=no` 來停用相關交換器埠上的 L3HW 解除安裝。
:::

### 未將網橋介面新增到 /interface/bridge/vlan/ {#not-adding-the-bridge-interface-to-interfacebridgevlan}

對於 VLAN 間路由，網橋介面本身需要新增到給定 VLAN 的標記成員中。在下一個示例中，VLAN 間路由在 VLAN 10 和 11 之間正常工作，但封包不會路由到 VLAN 20。

```ros
/interface/bridge/vlan
add bridge=bridge1 vlan-ids=10 tagged=bridge1,sfp-sfpplus1
add bridge=bridge1 vlan-ids=11 tagged=bridge1 untagged=sfp-sfpplus2,sfp-sfpplus3 
add bridge=bridge1 vlan-ids=20 tagged=sfp-sfpplus1 untagged=sfp-sfpplus4,sfp-sfpplus5
```

上述示例並不總是意味著錯誤。有時，你可能希望裝置在某些/所有 VLAN 中充當簡單的二層交換器。只需確保你是有意設定這種行為，而不是由於錯誤。

### 建立多個網橋 {#creating-multiple-bridges}

裝置僅支援一個硬體網橋。如果建立了多個網橋，只有一個網橋獲得硬體解除安裝。對於二層來說，這意味著其他網橋採用軟體轉發；而在 L3HW 的情況下，多個網橋可能導致未定義行為。

:::tip
與其建立多個橋接，不如建立一個橋接，並透過 VLAN filtering 隔離 L2 網路。
:::

### 使用不屬於該交換器的埠 {#using-ports-that-do-not-belong-to-the-switch}

某些裝置有兩個交換晶片，或者管理埠直接連線到 CPU。例如，**CRS312-4C+8XG** 有一個 **ether9** 埠連線到單獨的交換晶片。嘗試將此埠新增到網橋或讓其參與 L3HW 設定會導致意外結果。把管理埠留給管理用途！

```ros
[admin@crs312] /interface/ethernet/switch> print
Columns: NAME, TYPE, L3-HW-OFFLOADING
# NAME     TYPE              L3-HW-OFFLOADING
0 switch1  Marvell-98DX8212  yes            
1 switch2  Atheros-8227      no   
           
[admin@crs312] /interface/ethernet/switch> port print
Columns: NAME, SWITCH, L3-HW-OFFLOADING, STORM-RATE
 # NAME         SWITCH   L3-HW-OFFLOADING  STORM-RATE
 0 ether9       switch2                             
 1 ether1       switch1  yes                      100
 2 ether2       switch1  yes                      100
 3 ether3       switch1  yes                      100
 4 ether4       switch1  yes                      100
 5 ether5       switch1  yes                      100
 6 ether6       switch1  yes                      100
 7 ether7       switch1  yes                      100
 8 ether8       switch1  yes                      100
 9 combo1       switch1  yes                      100
10 combo2       switch1  yes                      100
11 combo3       switch1  yes                      100
12 combo4       switch1  yes                      100
13 switch1-cpu  switch1                           100
14 switch2-cpu  switch2
```

### 過度依賴 Fasttrack 硬體解除安裝 {#relying-on-fasttrack-hw-offloading-too-much}

由於 Fasttrack 硬體解除安裝以零配置開銷提供接近線速的效能，使用者傾向於將其用作預設解決方案。但是，硬體 Fasttrack 連線數量非常有限，其他流量只能留給 CPU。請嘗試儘可能使用硬體路由，透過交換器 ACL 規則將 CPU 流量降至最低，然後使用防火牆過濾規則微調要解除安裝哪些 Fasttrack 連線。

### 嘗試解除安裝慢路徑連線 {#trying-to-offload-slow-path-connections}

使用某些配置（例如啟用網橋 "**use-ip-firewall**" 設定、建立網橋 nat/filter 規則）或執行 sniffer 或 torch 等特定功能，可能會停用 RouterOS [FastPath](../firewall-and-quality-of-service/packet-flow-in-routeros.md#fast-path)，從而影響正確進行 FastTrack 和硬體解除安裝連線的能力。如果需要硬體解除安裝的 Fasttrack，請確保沒有停用 FastPath 的設定，並驗證連線是否獲得 "H" 標記，或使用 L3HW [monitor](../cli-reference/interface/ethernet/switch/l3hw-settings/monitor.md) 命令檢視硬體解除安裝連線數量。

## L3HW 功能支援 {#l3hw-feature-support}

- **HW** - 該功能受支援並解除安裝到硬體。
- **CPU** - 該功能受支援，但由軟體（CPU）執行。
- **N/A** - 該功能無法與 L3HW 一起使用。必須完全停用三層硬體解除安裝（**switch** `l3-hw-offloading=no`）才能讓該功能工作。
- **FW** - 該功能要求給定 **switch port** 使用 `l3-hw-offloading=no`。在 **switch** 級別，使用 `l3-hw-offloading=yes`。

| 功能 | 支援 | 備註 | 版本 |
| :-- | :-- | :-- | :-- |
| IPv4 單播路由 | **HW** |  | 7.1 |
| IPv6 單播路由 | **HW** | <br/><code>/interface/ethernet/switch/l3hw-settings/set ipv6-hw=yes</code><br/> | 7.6 |
| IPv4 組播路由 | **CPU** |  |  |
| IPv6 組播路由 | **CPU** |  |  |
| ECMP | **HW** | 多路徑路由。L3HW 使用交換晶片自身的 ECMP 雜湊掩碼，其中包含用於 TCP/UDP 的 L4 埠；對於硬體轉發的 ECMP，配置的雜湊策略會被忽略。FastTrack 解除安裝的連線遵循核心 FIB 查詢，並可能選擇不同的下一跳。[FastPath](../firewall-and-quality-of-service/packet-flow-in-routeros.md#fast-path) 按 L3 快取路由。 | 7.1 |
| 黑洞路由 | **HW** | <br/><code>/ip/route/add dst-address=10.0.99.0/24 blackhole</code><br/> | 7.1 |
| `gateway=<interface_name>` | **CPU/HW** | <br/><code>/ip/route/add dst-address=10.0.0.0/24 gateway=ether1</code><br/><br/> 這僅適用於直連網路。由於 HW 不知道如何傳送 ARP 請求，CPU 會發送 ARP 請求並等待回覆，以便在連線中第一個與 DST IP 地址匹配的接收封包上確定 DST MAC 地址。確定 DST MAC 後，會新增 HW 條目，所有後續封包都將由交換晶片處理。 | 7.1 |
| Bridge | **HW** | 從/到[硬體解除安裝 Bridge](./index.md#bridge-hardware-offloading)介面的路由。 | 7.1 |
| VLAN | **HW** | 在使用 [vlan-filtering](./index.md#bridge-vlan-filtering) 的硬體解除安裝 Bridge 介面上建立的 VLAN 介面之間的路由。 <br/><br/>在 <a href="#crs8xx-switch-98dx7xxx-series">98DX7xxx</a> 交換器上，也支援在直接創建於乙太網交換埠的 VLAN 介面之間路由。 <br/><br/><code>/interface/vlan</code><br/> | 7.1 |
| Bonding | **HW** | 在 Bonding 介面之間路由。 <br/><br/><code>/interface/bonding</code><br/><br/> 只有 <code>802.3ad</code> 和 <code>balance-xor</code> Bonding 模式會被硬體解除安裝。 | 7.1 |
| IPv4 防火牆 | **FW** | 使用者必須選擇 HW 加速路由或防火牆。防火牆規則由 CPU 處理。***Fasttrack*** 連線會被解除安裝到 HW。 | 7.1 |
| IPv4 NAT | **FW** | 應用於已解除安裝 ***Fasttrack*** 連線的 NAT 規則也會由 HW 處理。 | 7.1 |
| MLAG | **N/A** |  |  |
| VRF | **HW** | [硬體解除安裝 VRF](#hardware-offloaded-vrf)。 |  |
| VRRP | **N/A** |  |  |
| Traffic-Flow | **N/A** | L3HW 解除安裝的流量不會透過 [流量監控](../diagnostics-monitoring-and-troubleshooting/traffic-flow/index.md) 報告。 |  |
| VXLAN | **HW** | 支援硬體解除安裝的 [VXLAN](./vxlan.md) 資料平面、VXLAN 封裝和解封裝。這允許在啟用 vlan-filtering 的 Bridge 內進行靜態一對一 VLAN 到 VXLAN 對映。目前，一些已知功能尚未實現。 <br/><strong>Underlay（對封裝後的 VXLAN 封包進行路由）：</strong><br/> 1. 不支援在 ECMP 上使用 VTEP <br/> 2. 不支援在 bond、bridge、VLAN 介面上使用 VTEP（僅支援獨立的路由乙太網介面） <br/> 3. 不支援基於組播的 VTEP <br/> 4. VXLAN 硬體解除安裝僅限於 <code>main</code> 路由表。VTEP 無法在 VRF 內執行。 <br/> 5. VTEP 不支援 IPv6 <br/><strong>Overlay（在乙太網和 VXLAN 之間轉發）：</strong><br/> 1. 不支援在 VXLAN 上新增 VLAN 標籤 <br/> 2. 不支援不同 VXLAN VNI 之間的路由 <br/> 3. VTEP 彼此隔離，且沒有機制控制它們之間的 "horizon"。 <br/> 4. 橋接的 VXLAN 介面不支援 IGMP 偵聽。啟用偵聽時，VXLAN 上的 MDB 條目不會被解除安裝，並且乙太網與 VXLAN 之間的組播流量會受到限制。 <br/> 5. MLAG 不支援橋接的 VXLAN 介面。 <br/><br/><code>/interface/vxlan</code><br/> | 7.18 |
| MTU | **HW** | 硬體最多支援 8 個 MTU 配置檔案。 | 7.1 |
| QinQ 路由 | **CPU** | 堆疊的可路由 VLAN 介面將失去 L3HW 解除安裝，而直接建立在 Bridge 介面上的可路由 VLAN 介面仍可使用 HW 解除安裝。 |  |
| 帶有 IPv6 下一跳的 IPv4 路由，或反之 | **N/A** |  |  |

:::warning
同一流的硬體轉發封包與 FastTrack/CPU 轉發封包混合時，可能選擇不同的 ECMP 下一跳，導致非對稱路由和連線重設。
:::

只有下表列出的裝置支援三層硬體解除安裝。

## L3HW 裝置支援 {#l3hw-device-support}

只有下表列出的裝置支援三層硬體解除安裝。

### CRS3xx：交換器 98DX3xxx 和 98DX2xxx 系列 {#crs3xx-switch-98dx3xxx-and-98dx2xxx-series}

下列裝置基於 **Marvell **98DX224S, 98DX226S****、**98DX2528,** 或 **98DX3236** 交換晶片型號。

:::info
**98DX3255** 和 **98DX3257** 型號是例外，它們具有 98DX8xxx 系列而非 98DX3xxx 系列的功能集。

**注意：** 與其他交換器型號相比，這些裝置缺少以下一些重要功能：

- Fasttrack 和 NAT 連線解除安裝
- 每 VLAN 封包和位元組計數器
- VXLAN 解除安裝
- 硬體解除安裝 VRF。

:::

| 交換晶片 | 型號 | IPv4 路由字首 <sup>1</sup> | IPv6 路由字首 <sup>2</sup> | 下一跳 | 每個字首的 ECMP 路徑 <sup>3</sup> |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **98DX3236** | CRS305-1G-4S+IN <br/> CRS326-24G-2S+ (RM/IN) <br/> CRS328-24P-4S+RM <br/> CRS328-4C-20S-4S+RM | 13312 | 3328 | 4K | 8 |
| **98DX226S** | CRS305-1G-4S+OUT (FiberBox Plus) <br/> CRS310-1G-5S-4S+ (netFiber 9/IN) <br/> CRS310-8G+2S+IN <br/> CRS318-16P-2S+OUT (netPower 16P) <br/> CRS320-8P-8B-4S+RM <br/> CRS418-8P-8G-2S+RM <br/> CRS418-8P-8G-2S+5axQ2axQ-RM | 13312 | 3328 | 4K | 8 |
| **98DX224S** | CRS318-1Fi-15Fr-2S-OUT (netPower 15FR) | 13312 | 3328 | 4K | 8 |
| **98DX2528** | CRS304-4XG-IN | 13312 | 3328 | 4K | 8 |

---

<sup>1</sup> 由於可解除安裝的路由總數有限，具有較高網路掩碼的字首優先由硬體轉發（例如 /32、/30、/29 等）。任何無法放入硬體表的其他字首將由 CPU 處理。直連主機以 /32（IPv4）或 /128（IPv6）路由字首形式解除安裝。主機數量還受 [IP Settings](../cli-reference/ip/settings.md) / [IPv6 Settings](../cli-reference/ipv6/settings.md) 中 max-neighbor-entries 的限制。  
<sup>2</sup> IPv4 和 IPv6 路由表共享相同的硬體記憶體。  
<sup>3</sup> 如果一條路由的路徑數超過硬體 ECMP 限制（X），則只有前 X 條路徑會被解除安裝。

#### 部分解除安裝 {#partial-offloading}

對於 **98DX3xxx**、**98DX2xxx** 交換晶片系列，情況相當簡單：一個 RouterOS 路由條目（/ip/route/）會對映為一個硬體 IPv4 路由字首條目。已連線主機（/32 路由）也會佔用同一張表。只要路由總數（"/ip/route/print count-only"）加上已連線主機數量（"/ip/arp/print count-only where status=reachable or status=stale"）不超過 **13312 (13k)**，所有內容都會被解除安裝。超過該數量後，具有*較短*字首的路由將保留在 CPU 上。

### CCR2xxx、CRS3xx、CRS5xx：交換器 98DX8xxx 和 98DX4xxx 系列 {#ccr2xxx-crs3xx-crs5xx-switch-98dx8xxx-and-98dx4xxx-series}

下列裝置基於 **Marvell 98DX8xxx**、**98DX4xxx** 交換晶片，或 **98DX325x** 型號。

<WideTable>

| 交換晶片 | 型號 | IPv4 路由 <sup>1</sup> | IPv4 主機 <sup>5</sup> | IPv6 路由 <sup>1</sup> | IPv6 主機 <sup>5</sup> | 下一跳 | IPv4 Fasttrack 連線 <sup>2, 3, 4</sup> | IPv4 NAT 條目 <sup>2, 4</sup> | IPv4 Fasttrack/NAT、VXLAN 解除安裝 按 VLAN 的封包/位元組計數器 |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **98DX8208** | CRS309-1G-8S+IN | 最高 36K | 最高 16K | 最高 6K | 最高 12K | 8K | 4.5K | 3.9K | + |
| **98DX8212** | CRS312-4C+8XG-RM | 最高 36K | 最高 16K | 最高 6K | 最高 12K | 8K | 2.25K | 2.25K | + |
| **98DX8216** | CRS317-1G-16S+RM | 最高 240K | 最高 64K | 最高 40K | 最高 48K | 8K | 4.5K | 4K | + |
| **98DX8332** | CRS326-24S+2Q+RM <br/> CRS326-4C+20G+2Q+RM | 最高 36K | 最高 16K | 最高 6K | 最高 12K | 8K | 2.25K | 2.25K | + |
| **98DX3257** <sup>6</sup> | CRS354-48G-4S+2Q+RM <br/> CRS354-48P-4S+2Q+RM | 最高 36K | 最高 16K | 最高 6K | 最高 12K | 8K | 2.25K | 2.25K | + |
| **98DX4310** | CRS504-4XQ (IN/OUT) <br/> CRS510-8XS-2XQ-IN <br/> RDS2216-2XG-4S+4XS-2XQ | 最高 120K | 最高 64K | 最高 20K | 最高 48K | 8K | 4.5K | 4K | + |
| **98CX8410** | CRS520-4XS-16XQ-RM | 最高 240K | 最高 64K | 最高 40K | 最高 48K | 8K | 4.5K | 4K | + |
| **98DX3255** <sup>6</sup> | CCR2116-12G-4S+ | 最高 36K | 最高 16K | 最高 6K | 最高 12K | 8K | 2.25K | 2.25K | + |
| **98DX8525** | CCR2216-1G-12XS-2XQ <br/> CRS518-16XS-2XQ-RM | 最高 120K | 最高 64K | 最高 20K | 最高 48K | 8K | 4.5K | 4K | + |

</WideTable>

<sup>1</sup> 取決於路由表的複雜度。整位元組 IP 字首（/8、/16、/24 等）佔用的硬體空間比其他字首（例如 /22）少。當路由硬體表滿時，只有具有較長子網字首的路由會被解除安裝（/30、/29、/28 等），而 CPU 處理較短的字首。使用者可以透過路由過濾器（針對動態路由）或按交換器埠、靜態路由或 VLAN 抑制硬體解除安裝來微調要解除安裝的路由。IPv4 和 IPv6 路由表共享相同的硬體記憶體。  
<sup>2</sup> 當達到 Fasttrack 或 NAT 條目的硬體限制時，其他連線將回退到 CPU。MikroTik 的智慧連線解除安裝演算法確保流量最大的連線被解除安裝到硬體。  
<sup>3</sup> Fasttrack 連線與 ACL 規則共享相同的硬體記憶體。根據複雜度，一條 ACL 規則可能佔用 3-6 個 Fasttrack 連線的記憶體。  
<sup>4</sup> 如果 Fasttrack 連線需要網路地址轉換，則會建立硬體 NAT 條目。硬體同時支援 SRCNAT 和 DSTNAT。  
<sup>5</sup> DX4000/DX8000 交換晶片將直連主機、IPv4 /32 和 IPv6 /128 路由條目儲存在 FDB 表中而非路由表中。硬體記憶體由常規 FDB L2 條目（MAC）、IPv4 和 IPv6 地址共享。主機數量還受 [IP Settings](../cli-reference/ip/settings.md) / [IPv6 Settings](../cli-reference/ipv6/settings.md) 中 max-neighbor-entries 的限制。  
<sup>6</sup> 該交換晶片具有 DX8000 系列的功能集。

#### 部分解除安裝 {#partial-offloading-1}

**98DX8xxx**、**98DX4xxx** 具有完全不同的路由表。我們不是解除安裝字首，而是必須解除安裝路由索引。整個 IPv4 地址範圍（IPv6 同理）都必須被索引，即 0.0.0.0 - 255.255.255.255。新增新路由條目會觸發索引重建，根據路由表的複雜程度，硬體記憶體會增加 0-5 個條目。這就是為什麼沒有給出確切數字。例如，某些包含 240K 條目的路由表可以完全解除安裝到 CRS317 硬體，而其他包含 160K 條目的路由表則勉強能裝入。不嘗試就永遠不知道。

當索引整個 IP 地址範圍（0.0.0.0 - 255.255.255.255）時，只要還有使用相同下一跳的預設路由（0.0.0.0/0），就可以按需解除安裝任意數量的路由。

例如，在 CCR2216 路由器上建立了大約 950k 條帶 /30 字首的路由，它們都使用相同的下一跳，並帶有一條預設路由。結果，所有路由都被解除安裝，同時 lpm-usage 保持最小。

```routeros
[admin@MikroTik] > /interface/ethernet/switch/l3hw-settings/advanced/monitor 
        ipv4-routes-total: 942338
           ipv4-routes-hw: 942326
          ipv4-routes-cpu:     11
  ipv4-shortest-hw-prefix:      0
               ipv4-hosts:      1
         route-queue-size:      0
         route-queue-rate:      0
       route-process-rate:      0
              nexthop-cap:   8192
            nexthop-usage:     85
    vxlan-mtu-packet-drop:      0
     fasttrack-ipv4-conns:      0
     fasttrack-queue-size:      0
     fasttrack-queue-rate:      0
   fasttrack-process-rate:      0
   fasttrack-hw-min-speed:      0
   fasttrack-hw-offloaded:      0
    fasttrack-hw-unloaded:      0
                  lpm-cap:  27200
                lpm-usage:     11
             lpm-bank-cap:   1360
           lpm-bank-usage:      1
                                0
                                0
                                0
                                1
                                0
                                0
                                0
                                4
                                0
                                0
                                0
                                5
                                0
                                0
                                0
                                0
                                0
                                0
                                0
                  pbr-cap:   8192
                pbr-usage:      0
             pbr-lpm-bank:      2
                nat-usage:      0
```

但是，如果地址範圍中存在 "gaps"，例如不使用預設路由或有多個下一跳，這會消耗硬體表。當路由硬體表滿時，只有具有較長子網字首的路由（/30、/29、/28 等）會被解除安裝，而 CPU 處理較短字首。以下是停用預設路由或使用不同下一跳時發生的情況：硬體表中只能裝入 37k 條帶 /30 字首的路由。這是 CCR2216 的最壞情況。

```routeros
[admin@MikroTik] > /interface/ethernet/switch/l3hw-settings/advanced/monitor 
        ipv4-routes-total: 942337
           ipv4-routes-hw:  37729
          ipv4-routes-cpu: 904608
  ipv4-shortest-hw-prefix:     30
               ipv4-hosts:      1
         route-queue-size:      0
         route-queue-rate:      0
       route-process-rate:      0
              nexthop-cap:   8192
            nexthop-usage:     85
    vxlan-mtu-packet-drop:      0
     fasttrack-ipv4-conns:      0
     fasttrack-queue-size:      0
     fasttrack-queue-rate:      0
   fasttrack-process-rate:      0
   fasttrack-hw-min-speed:      0
   fasttrack-hw-offloaded:      0
    fasttrack-hw-unloaded:      0
                  lpm-cap:  27200
                lpm-usage:  22392
             lpm-bank-cap:   1360
           lpm-bank-usage:   1022
                             1033
                             1027
                             1028
                             1221
                             1033
                             1040
                              678
                             1358
                             1245
                             1254
                             1242
                             1246
                             1249
                             1273
                             1260
                             1101
                             1024
                             1031
                             1027
                  pbr-cap:   8192
                pbr-usage:      0
             pbr-lpm-bank:      2
                nat-usage:      0
```

在許多情況下，預設行為 "僅解除安裝具有較長子網字首的路由" 並不是最優的，尤其是當 CPU 處理的路由與硬體解除安裝路由的比例過高時。發生這種情況時，封包被硬體轉發的機會會顯著下降。

如果硬體記憶體不足併發生部分解除安裝，作為網路管理員，更好的方法是僅解除安裝承載最多流量的路由，而將需求較低的路由保留在 CPU 上，並且不讓部分解除安裝發生。

幸運的是，有幾種方法可以管理這一點。可以按交換器埠和靜態路由進行抑制，也可以[使用多種屬性過濾動態路由](../user-guides/routing-and-networking-protocols/route-selection-and-filtering.md)。一個示例是使用 as-path 過濾需求最大的字首（Google、Meta），而所有其他路由則被抑制 L3HW。

### CRS8xx：交換器 98DX7xxx 系列 {#crs8xx-switch-98dx7xxx-series}

下列裝置基於 **Marvell 98DX7xxx** 交換晶片型號。

:::danger
以下功能的軟體支援仍在開發中，尚不可用：

- FastTrack 和 NAT 連線解除安裝
- VXLAN 解除安裝

:::

<WideTable>

| 交換晶片 | 型號 | IPv4 路由 <sup>1</sup> | IPv4 主機 <sup>2</sup> | IPv6 路由 <sup>1</sup> | IPv6 主機 <sup>2</sup> | 下一跳 | IPv4 Fasttrack 連線 | IPv4 NAT 條目 | VXLAN 解除安裝 | 按 VLAN 的封包/位元組計數器 |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **98DX7335** | CRS812-8DS-2DQ-2DDQ-RM | 最高 240K | 最高 64K | 最高 40K | 最高 48K | 16K | 待公佈 | 待公佈 | 待公佈 | + |
| **98DX7335** | CRS804-4DDQ-hRM | 最高 240K | 最高 64K | 最高 40K | 最高 48K | 16K | 待公佈 | 待公佈 | 待公佈 | + |

</WideTable>

---

<sup>1</sup> 取決於路由表的複雜度。整位元組 IP 字首（/8、/16、/24 等）佔用的硬體空間比其他字首（例如 /22）少。當路由硬體表滿時，只有具有較長子網字首的路由會被解除安裝（/30、/29、/28 等），而 CPU 處理較短的字首。使用者可以透過路由過濾器（針對動態路由）或抑制靜態路由的硬體解除安裝來微調要解除安裝的路由。IPv4 和 IPv6 路由表共享相同的硬體記憶體。  
<sup>2</sup> 98DX7xxx 交換晶片將直連主機、IPv4 /32 路由條目和 IPv6 /128 路由條目儲存在 FDB 表中而非路由表中。硬體記憶體由常規 FDB L2 條目（MAC）、IPv4 地址和 IPv6 地址共享。主機數量還受 [IP Settings](../cli-reference/ip/settings.md) / [IPv6 Settings](../cli-reference/ipv6/settings.md) 中 max-neighbor-entries 的限制。
