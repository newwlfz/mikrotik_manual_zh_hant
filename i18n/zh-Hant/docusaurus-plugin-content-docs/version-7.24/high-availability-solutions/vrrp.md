---
sidebar_key: "high-availability-solutions/vrrp"
sidebar_position: 5
title: "VRRP"
sidebar_label: "VRRP"
description: "本頁介紹 MikroTik RouterOS 中的虛擬路由冗餘協定（VRRP），說明它如何透過 IPv4/IPv6 組播通訊以及路由器之間基於優先順序的選舉來提供路由器冗餘。內容涵蓋 VRRP 配置、虛擬 MAC 地址分配、owner/master/backup 角色，並強調版本相容性以及對 VRRPv 中已棄用認證功能的警告"
tags:
  - 'vrrp'
  - 'routing-redundancy'
source: https://manual.mikrotik.com/docs/7.24/high-availability-solutions/vrrp
captured_at: '2026-11-04T11:29:58+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 概述 {#summary}

本章介紹 RouterOS 中對虛擬路由器冗餘協定（VRRP）的支援。

在較大的 LAN 上，通常會使用動態路由協定（OSPF 或 RIP）；然而，有多種因素可能使使用動態路由協定變得不理想。一種替代方案是使用靜態路由，但如果靜態配置的第一跳發生故障，主機將無法與其他主機通訊。

在 IPv6 網路中，主機透過接收鄰居發現（ND）協定使用的路由器通告來了解路由器。ND 已經具有確定不可達路由器的內建機制。然而，檢測不可達路由器最多可能需要 38 秒。可以更改引數並加快檢測速度，但這會增加 ND 流量的開銷，尤其是在有大量主機時。VRRP 允許在 3 秒內檢測到不可達路由器，且不會帶來額外的流量開銷。

虛擬路由器冗餘協定（VRRP）透過將多臺路由器組合成一個稱為*虛擬路由器*（VR）的邏輯組來提供解決方案。RouterOS 中的 VRRP 實現基於 VRRPv2 RFC 3768 和 VRRPv3 RFC 5798。

建議所有使用同一 VRID 實現 VRRP 的裝置都使用相同版本的 RouterOS。

:::warning
根據 RFC，VRRP v3 的認證已棄用。

:::

## 協定概述 {#protocol-overview}

![](/img/0340e63898c1565e.webp)

VRRP 的目的是與關聯到虛擬路由器 ID 的所有 VRRP 路由器通訊，並透過它們之間基於優先順序的選舉過程來支援路由器冗餘。

所有訊息傳遞均透過使用協定 112（VRRP）的 IPv4 或 IPv6 組播封包完成。IPv4 封包的目標地址是 *224.0.0.18*，IPv6 的目標地址是 *FF02:0:0:0:0:0:0:12*。封包的源地址始終是傳送該封包的介面的主 IP 地址。在 IPv6 網路中，源地址是介面的鏈路本地地址。

這些封包始終以 TTL=255 傳送，並且不會由路由器轉發。如果由於任何原因，路由器收到 TTL 更低的封包，該封包將被丟棄。

每個 VR 節點都有一個分配的 MAC 地址。此 MAC 地址用作 Master 傳送的所有周期性訊息的源地址。

虛擬路由器由 VRID 和一組對映的 IPv4 或 IPv6 地址定義。Master 路由器被稱為所對映 IPv4/IPv6 地址的 **Owner**。在 IPv4 和 IPv6 中使用相同的 VRID 沒有限制；不過，它們將是兩個不同的虛擬路由器。

只有 Master 路由器會發送週期性 Advertisement 報文，以儘量減少流量。只有當 Backup 具有更高優先順序且未禁止搶佔時，Backup 才會嘗試搶佔 Master。

:::tip
屬於同一 VR 的所有 VRRP 路由器必須配置相同的 advertisement interval。如果間隔不匹配，路由器將丟棄收到的 advertisement packet。

:::

## 虛擬路由器（VR） {#virtual-router-vr}

虛擬路由器（VR）由一個 Owner 路由器和屬於同一網路的一個或多個 backup 路由器組成。

VR 包括：

- VRID 配置在每臺 VRRP 路由器上。
- 每臺路由器上都配置相同的虛擬 IP。
- 每臺路由器上都配置 Owner 和 Backup。對於給定的 VR，只能有一個 Owner。

### 虛擬 MAC 地址 {#virtual-mac-address}

VRRP 會根據 VRRP 封包的標準 MAC 字首和 VRID 編號，自動為 VRRP 介面分配 MAC 地址。前五個八位組為 00:00:5E:00:01，最後一個八位組為配置的 VRID。例如，如果虛擬路由器的 VRID 為 49，則虛擬 MAC 地址將為 *00:00:5E:00:01:31*。

:::warning
虛擬 MAC 地址不能手動設定或編輯。

:::

### 所有者 {#owner}

VR 的 Owner 路由器是預設的 Master 路由器，並作為該 VR 中所有子網的 Owner 執行。Owner 路由器上的優先順序必須為最高值（255），且虛擬 IP 與真實 IP 相同（擁有該虛擬 IP 地址）。

:::warning
RouterOS 不能配置為 Owner。除非將非 RouterOS 裝置設定為 owner，否則純虛擬 IP 配置是唯一有效的配置。

:::

### 主 {#master}

VR 中的 Master 路由器充當其配置所在網路的物理閘道器。Master 的選擇由優先順序值控制。Master 狀態描述 Master 路由器的行為。在示例網路中，**R1** 是 Master 路由器。當 R1 不再可用時，R2 成為 Master。

### 備份 {#backup}

VR 必須至少包含一個 Backup 路由器。Backup 路由器必須配置與該 VR 的 Master 相同的虛擬 IP。Backup 路由器的預設優先順序為 100。當前 Master 路由器不再可用時，優先順序最高的 Backup 路由器將成為當前 Master。每當具有更高優先順序的路由器變為可用時，它就會切換為 Master。有時不需要此行為。要覆蓋此行為，應停用搶佔模式。

### 虛擬地址 {#virtual-address}

![](/img/8599472e34cd8357.webp)

與 VR 關聯的虛擬 IP 必須相同，並在所有 VR 節點上設定。所有虛擬地址和真實地址都應來自同一網路。

:::warning
RouterOS 不能配置為 Owner。VRRP 地址和真實 IP 地址不應相同。

:::

如果 VR 的 Master 關聯了多個 IP 地址，則屬於同一 VR 的 Backup 路由器也必須關聯相同的虛擬 IP 地址集合。如果 Master 上的虛擬地址不在 Backup 上，則存在配置錯誤，VRRP 通告報文將被丟棄。

所有虛擬路由器成員都可以配置為虛擬 IP 與物理 IP 不同。這種虛擬地址可以稱為浮動或純虛擬 IP 地址。此設定的優點是為管理員提供了靈活性。由於虛擬 IP 地址不是任何參與路由器的真實地址，管理員可以更改這些物理路由器或其地址，而無需重新配置虛擬路由器本身。

在 IPv6 網路中，第一個地址始終是與 VR 關聯的鏈路本地地址。如果配置了多個 IPv6 地址，則它們會在鏈路本地地址之後新增到通告報文中。

### IPv4 ARP {#ipv4-arp}

給定 VR 的 Master 使用該 VR 分配的 MAC 地址響應 ARP 請求。虛擬 MAC 地址還用作 Master 傳送的通告報文的源 MAC 地址。對於非虛擬 IP 地址的 ARP 請求，路由器使用系統 MAC 地址進行響應。Backup 路由器不響應虛擬 IP 的 ARP 請求。

### IPv6 ND {#ipv6-nd}

您可能知道，在 IPv6 網路中，使用鄰居發現協定而不是 ARP。當路由器成為 Master 時，會針對與虛擬路由器關聯的每個 IPv6 地址傳送帶有 Router Flag 的非請求 ND 鄰居通告。

## VRRP 狀態機 {#vrrp-state-machine}

![](/img/2ab58b3889e511d8.webp)

從圖中可以看到，每個 VRRP 節點可以處於以下三種狀態之一：

- Init 狀態
- Backup 狀態
- Master 狀態

### Init 狀態 {#init-state}

此狀態的目的是等待 Startup 事件。收到此事件後，將執行以下操作：

- 如果優先順序為 255：
- \* 對於 IPv4，傳送通告報文並廣播 ARP 請求。
- \* 對於 IPv6，針對與虛擬路由器關聯的每個 IPv6 地址傳送非請求 ND 鄰居通告，並將目標地址設定為與 VR 關聯的鏈路本地地址。
- \* 轉換到 MASTER 狀態。
- 否則轉換到 BACKUP 狀態。

### Backup 狀態 {#backup-state}

處於 Backup 狀態時：

- 在 IPv4 網路中，節點不響應 ARP 請求，也不轉發與 VR 關聯的 IP 的流量。
- 在 IPv6 網路中，節點不響應 ND 鄰居請求訊息，也不為 VR 關聯的 IPv6 地址傳送 ND 路由器通告。

路由器的主要任務是接收通告報文並檢查 Master 節點是否可用。

Backup 路由器會在以下兩種情況下自行轉換到 Master 狀態：

- 如果通告報文中的優先順序為 0。
- 當 Preemption\_Mode 設定為 yes，且 ADVERTISEMENT 中的優先順序低於本地優先順序時。

轉換到 Master 狀態後，節點會：

- 在 IPv4 中廣播免費 ARP 請求。
- 在 IPv6 中針對每個關聯的 IPv6 地址傳送非請求 ND 鄰居通告。

在其他情況下，通告報文將被丟棄。收到 shutdown 事件後，轉換到 Init 狀態。

:::warning
如果 Owner 路由器變為可用，則忽略搶佔模式。

:::

### Master 狀態 {#master-state}

當設定為 MASTER 狀態時，節點會作為與 VR 關聯的 IPv4/IPv6 地址的轉發路由器執行。

在 IPv4 網路中，Master 節點響應針對與 VR 關聯的 IPv4 地址的 ARP 請求。在 IPv6 網路中，Master 節點會：

- 響應針對關聯 IPv6 地址的 ND 鄰居請求訊息。
- 針對關聯的 IPv6 地址傳送 ND 路由器通告。

如果 Master 節點收到通告報文：

- 如果優先順序為 0，立即傳送通告。
- 如果通告報文中的優先順序大於節點優先順序，則轉換到 Backup 狀態。
- 如果通告報文中的優先順序等於節點優先順序，且傳送方的主 IP 地址大於本地主 IP 地址，則轉換到 Backup 狀態。
- 在其他情況下忽略通告。

收到 shutdown 事件時，傳送 priority=0 的通告報文並轉換到 Init 狀態。

### 連線跟蹤同步 {#connection-tracking-synchronization}

與不同的高可用性功能類似，RouterOS v7 支援 VRRP 連線跟蹤同步。

VRRP 連線跟蹤同步要求 RouterOS [連線跟蹤](../firewall-and-quality-of-service/connection-tracking.md) 正在執行。預設情況下，連線跟蹤以 `auto` 模式工作。如果 VRRP 裝置不包含任何防火牆規則，則需要手動啟用連線跟蹤：

```ros
/ip/firewall/connection/tracking/set enabled=yes
```

要同步連線跟蹤條目，請按如下方式配置裝置：

```ros
/interface/vrrp/set vrrp1 sync-connection-tracking=yes
```

在日誌部分驗證配置：

```ros
16:14:06 vrrp,info vrrp1 now MASTER, master down timer
16:14:06 vrrp,info vrrp1 stop CONNTRACK
16:14:06 vrrp,info vrrp1 starting CONNTRACK MASTER
```

連線跟蹤條目僅從 Master 同步到 Backup 裝置。

當同時啟用 `sync-connection-tracking` 和 `preemption-mode`，且具有更高 VRRP 優先順序的路由器上線時，連線會先同步，然後具有更高優先順序的路由器才會成為 VRRP Master。

:::tip
如果在兩臺裝置之間配置了多個 VRRP 介面並且需要 `sync-connection-tracking=yes`，則只能在一個 VRRP 介面上啟用它，最好是指定為 `group-authority` 的那個介面。

:::

## 配置 VRRP {#configuring-vrrp}

### IPv4 {#ipv4}

設定虛擬路由器非常簡單，只需執行兩個操作——建立 VRRP 介面並設定虛擬路由器的 IP 地址。

例如，將 VRRP 新增到 ether1，並將 VR 的地址設定為 192.168.1.1

```ros
/interface/vrrp/add name=vrrp1 interface=ether1
/ip/address/add address=192.168.1.2/24 interface=ether1
/ip/address/add address=192.168.1.1/32 interface=vrrp1
```

請注意，新增 VRRP 時只指定了 'interface' 引數。它是唯一需要手動設定的引數。其他引數如果未指定，將設定為其預設值：`vrid=1, priority=100` 和 `authentication=none`。

:::warning
如果 VRRP 上配置的地址與路由器任何其他介面上的地址屬於同一子網，則 VRRP 介面上的地址必須使用 /32 子網掩碼。

:::

在 VRRP 能夠正確執行之前，ether1 上需要有一個正確的 IP 地址。在此示例中，它是 192.168.1.2/24。

### IPv6 {#ipv6}

要使 VRRP 在 IPv6 網路中工作，必須啟用幾個附加選項——需要 v3 支援，並且協定型別應設定為 IPv6：

```ros
/interface/vrrp/add name=vrrp1 interface=ether1 version=3 v3-protocol=ipv6
```

現在 VRRP 介面已設定好，我們可以新增全域性地址並啟用 ND 通告：

```ros
/ipv6/address/add address=FEC0:0:0:FFFF::1/64 advertise=yes interface=vrrp1
```

不需要像 IPv4 情況那樣進行額外的地址配置。IPv6 使用鏈路本地地址在節點之間通訊。

## 引數 {#parameters}

VRRP 介面引數。

**子選單：** `/interface/vrrp`

##### 可寫設定 {#writable-settings}

| 屬性 | 描述 |
| :-- | :-- |
| **arp** (*disabled \| enabled \| proxy-arp \| reply-only*; 預設值：**enabled**) | ARP 解析協定模式。 |
| **arp-timeout**(*integer;* 預設值：**auto**) | 在未從 IP 收到任何封包後，ARP 記錄在 ARP 表中保留多長時間。值 `auto` 等於 IP/Settings 中的 `arp-timeout` 值，預設為 3。 |
| **authentication** (*ah \| none \| simple*; 預設值：**none**) | 用於 VRRP 通告報文的認證方法。- `none` - 僅用於低安全性網路，例如 LAN 上的兩個 VRRP 節點。- `ah` - IP Authentication Header。此演算法可針對配置錯誤、重放攻擊以及報文損壞或修改提供強保護。當您對 LAN 上節點的管理控制有限時，應使用它。使用 HMAC-MD5。- `simple` - 使用明文密碼。可防止本地網路上路由器意外配置錯誤。 |
| **comment** (*string*; 預設值: ) | 介面的簡短描述。 |
| **connection-tracking-mode** (*active-active \| passive-active*; 預設值：**passive-active**) | 指定連線跟蹤同步的模式。此設定僅在啟用 `sync-connection-tracking=yes` 時相關。- `passive-active` - 將此模式用於傳統 VRRP 設定，即一個 Master 和一個或多個 Backup 路由器。在此模式下，只有 Master 裝置透過向 Backup 裝置傳送更新來執行連線跟蹤同步。Backup 裝置不傳送連線跟蹤資料。- `active-active` - 將此模式用於具有多個 VRRP 組以實現負載均衡的設定。每個 VRRP 組都有自己的 Master，這些 Master 可以位於不同的物理裝置上。在 `active-active` 模式下，所有活動 Master 可以相互同步連線跟蹤資料。active-active 模式下的每個 VRRP 組必須使用**唯一的** `connection-tracking-port` 值。在多個組之間複用相同埠可能導致連線跟蹤表不同步。**重要：** 將多個 VRRP 組與 `passive-active` 模式一起使用可能導致連線跟蹤表不同步，因為只有一個 Master 處理同步，其他 Master 不交換跟蹤資料。示例配置：<pre><code>R1`/interface/vrrp`add connection-tracking-mode=active-active connection-tracking-port=8275 interface=ether1 name=vrrp30 priority=100 sync-connection-tracking=yes vrid=1add connection-tracking-mode=active-active connection-tracking-port=8276 interface=ether1 name=vrrp40 priority=100 sync-connection-tracking=yes vrid=2R2`/interface/vrrp`add connection-tracking-mode=active-active connection-tracking-port=8275 interface=ether1 name=vrrp30 priority=55 sync-connection-tracking=yes vrid=1add connection-tracking-mode=active-active connection-tracking-port=8276 interface=ether1 name=vrrp40 priority=155 sync-connection-tracking=yes vrid=2</code></pre> |
| **connection-tracking-port** (*integer;* 預設值：**8275**) | 指定用於連線跟蹤同步的 UDP 埠。此設定僅在啟用 `sync-connection-tracking=yes` 時相關。 |
| **group-authority** (*none \| self \| vrrp-interface;* 預設值：**none**) | 允許將多個 VRRP 介面分組，使它們共享相同的 VRRP 狀態。在一個組內，會選擇一個 group authority 介面。它控制其他組成員的狀態，並且是唯一發送 VRRP 通告的介面。當 group-authority VRRP 介面轉換到 Backup 狀態時，所有組成員也會轉換到 Backup 狀態。如果檢測到任何組成員發生故障，例如由於其父介面鏈路斷開，則所有組成員都會轉換到 failure 狀態。- `none` - VRRP 介面不分組，獨立執行，並具有自己的 VRRP 狀態機。- `self` - VRRP 介面充當 group authority。它控制其他分組的 VRRP 介面的狀態機，並負責傳送和接收 VRRP 通告。- `vrrp-interface` - VRRP 介面是組成員。其狀態機跟隨指定 VRRP 介面的狀態。例如，VRRP 例項執行在 LAN 和 WAN 網路上，且它們之間有 NAT。如果同一裝置上的一個 VRRP 例項是 Master，另一個是 Backup，則由於 NAT 故障，整個網路會出現故障。將 LAN 和 WAN VRRP 介面分組可確保二者要麼都是 VRRP Master，要麼都是 Backup。在 VRRP 組中，VRRP 通告僅由 group authority 傳送。在典型的 WAN+LAN 設定中，應使用 LAN 網路作為 group authority，以將 VRRP 控制流量保留在內部網路中。<pre><code>`/interface/vrrp`add name=vrrp-wan interface=sfp-sfpplus1 vrid=1 priority=100add name=vrrp-lan interface=bridge1 vrid=2 priority=100set [find] group-authority=vrrp-lan</code></pre> |
| **interface** (*string;* 預設值： ) | 將在其上執行 VRRP 例項的介面名稱。 |
| **interval** (*time [10ms..4m15s]*; 預設值：**1s**) | VRRP interval 定義 VRRP Master 路由器向 Backup 路由器傳送 Advertisement 報文的頻率。此間隔直接決定 Backup 接收 keepalive 資訊的頻率，該資訊確認 Master 正在執行。較短的間隔會提高 Advertisement 報文的傳送速率，從而可以更快檢測到 Master 故障，但也會增加對丟包、處理延遲和定時器不準確的敏感性。較長的間隔可減少控制流量並提高穩定性，但代價是故障切換檢測更慢。Master Down 間隔由配置的 VRRP interval 和路由器優先順序推導得出，其計算會允許在觸發故障切換前錯過多個 Advertisement。**警告：** 配置低於 1 秒的 VRRP interval 可能導致不可預測的行為和意外的 Master 角色變更。 |
| **mtu** (*只讀*; 預設值： ) | 三層 MTU 大小。自 RouterOS v7.7 起，VRRP 介面始終使用 slave 介面 MTU。 |
| **name** (*string;* 預設值： ) | VRRP 介面名稱。 |
| **on-backup** (*string;* 預設值： ) | 當節點切換到 Backup 狀態時執行的指令碼。 |
| **on-master** (*string;* 預設值： ) | 當節點切換到 Master 狀態時執行的指令碼。 |
| **on-fail** (*string;* 預設值： ) | 當節點失敗時執行的指令碼。 |
| **password** (*string;* 預設值： ) *[敏感](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 認證所需的密碼。如果不使用認證，可以忽略。 |
| **preemption-mode** (*yes \| no*; 預設值：**yes**) | Master 節點是否始終擁有優先順序。設定為 'no' 時，即使 Backup 節點具有比當前 Master 更高的優先順序，Backup 節點也不會被選舉為 Master，直到當前 Master 失敗。如果 Owner 路由器變為可用，則忽略此設定。 |
| **priority** (*integer: 1..254*; 預設值：**100**) | 用於 Master 選舉演算法的 VRRP 節點優先順序。數字越大表示優先順序越高。'255' 保留給擁有 VR IP 的路由器，'0' 保留給 Master 路由器以表示它正在釋放職責。 |
| **remote-address** (*IPv4;* 預設值： ) | 指定用於連線跟蹤同步的另一個 VRRP 路由器的遠端地址。如果未設定，系統會透過 VRRP 自動檢測遠端地址。僅當 `sync-connection-tracking=yes` 時使用遠端地址。顯式設定遠端地址有以下好處：- 連線跟蹤同步啟動更快，因為無需等待 VRRP 的初始訊息交換來檢測遠端地址。- VRRP Master 選舉更快。- 連線跟蹤資料可以透過不同的網路介面傳送，例如兩臺路由器之間的專用安全線路。同步連線跟蹤使用 UDP 埠 8275。 |
| **v3-checksum-as-v2** (*yes \| no*; 預設值：**no**) | 控制 VRRPv3 IPv4 校驗和是在包含還是不包含 IPv4 偽首部的情況下計算。不同廠商對 RFC 5798 第 5.2.8 節中 IPv4 校驗和計算裡的偽首部有不同解釋。基於 Linux 的實現（包括 FRR）會為 IPv4 和 IPv6 都包含偽首部，而 Cisco 僅為 IPv6 包含偽首部。- `no`（預設值）- 在校驗和計算中包含 IPv4 偽首部。與其他基於 Linux 的 VRRPv3 實現相容。- `yes` - 在校驗和計算中排除 IPv4 偽首部。將此設定用於與 Cisco 及其他不為 IPv4 包含偽首部的廠商相容。此設定僅適用於使用 IPv4 的 VRRPv3。它對 VRRPv3 IPv6 或 VRRPv2 沒有影響。**重要：** 同一虛擬路由器中的所有 VRRP 路由器必須對此設定使用相同的值。值不匹配會導致 "bad checksum" 錯誤，並且 VRRP 通告報文將被丟棄。 |
| **v3-protocol** (*ipv4 \| ipv6*; 預設值：**ipv4**) | VRRPv3 將使用的協定。僅在 **version** 為 3 時有效。 |
| **version** (*integer [2, 3]*; 預設值：**3**) | 要使用的 VRRP 版本。 |
| **vrid** (*integer: 1..255*; 預設值：**1**) | 虛擬路由器識別符號。每個虛擬路由器必須具有唯一的 ID 編號。 |
| **sync-connection-tracking**(*string;* 預設值：**no**) | 將連線跟蹤條目從 Master 同步到 Backup 裝置。VRRP 連線跟蹤同步要求 RouterOS [連線跟蹤](../firewall-and-quality-of-service/connection-tracking.md) 正在執行。 |

##### 只讀標誌 {#read-only-flags}

| 屬性 | 描述 |
| :-- | :-- |
| **backup** | VRRP 介面處於 Backup 狀態。 |
| **disabled** | VRRP 介面已被使用者停用。 |
| **failure** | VRRP 介面處於 failure 狀態，例如由於其父介面鏈路斷開。 |
| **grp-authority** | VRRP 介面為 `group-authority`。它控制其他組成員的狀態，並且是唯一發送 VRRP 通告的介面。 |
| **grp-member** | VRRP 介面是組成員。其狀態機跟隨指定的 `group-authority` 介面的狀態。 |
| **invalid** | VRRP 介面處於 invalid 狀態，例如由於配置錯誤。 |
| **master** | VRRP 介面處於 Master 狀態。 |
