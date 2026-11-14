---
sidebar_key: "wireless/abgn/hwmpplus-mesh"
sidebar_position: 2
title: "HWMPplus 網狀網"
sidebar_label: "HWMPplus 網狀網"
description: "本頁介紹 MikroTik RouterOS 中的 HWMP+ 網狀協定，這是一種使用 Hybrid Wireless Mesh Protocol 的無線網狀網路二層路由解決方案。內容涵蓋介面屬性、埠配置、FDB 狀態，幷包含一個動態 WDS 鏈路整合的示例。"
tags:
  - 'mesh'
  - 'hwmpplus'
source: https://manual.mikrotik.com/docs/7.24/wireless/abgn/hwmpplus-mesh
captured_at: '2026-11-04T11:35:34+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

**子選單：** `/interface/mesh`

HWMP+ 是 MikroTik 專用的二層路由協定，用於無線 Mesh 網路。它基於 IEEE 802.11s 草案標準中的 Hybrid Wireless Mesh Protocol (HWMP)。在 Mesh 環境中，可用它代替（Rapid）Spanning Tree 協定，以確保無環的最優路由。

但是，HWMP+ 協定與 IEEE 802.11s 草案標準中的 HWMP 不相容。

請注意，為網路使用的分發系統不必是 Wireless Distribution System (WDS)。HWMP+ Mesh 路由不僅支援 WDS 介面，還支援 Mesh 內部的乙太網介面。因此，你可以使用簡單的基於乙太網的分發系統，也可以同時組合 WDS 和乙太網鏈路！

:::warning
HWMPplus 在  [Wifi](../wifi/index.md) 介面上不受支援，但可在 [Wireless](./index.md) 介面上使用。
:::

## 屬性 {#properties}

### Mesh {#mesh}

| 屬性 | 描述 |
| :-- | :-- |
| **admin-mac** (*MAC 地址*；**預設：00:00:00:00:00:00)** | 管理分配的 MAC 地址，在 **auto-mac** 設定停用時使用 |
| **arp** (*disabled \| enabled \| proxy-arp \| reply-only*；預設：**enabled**) | Address Resolution Protocol 設定 |
| **auto-mac** (*boolean*；預設：**no**) | 如果停用，則 **admin-mac** 的值將用作 Mesh 介面的 MAC 地址；否則，如果存在埠，將使用某個埠的地址 |
| **hwmp-default-hoplimit** (*integer: 1..255*；預設：) | 生成的路由協定封包的最大跳數；HWMP+ 封包被轉發 "hoplimit" 次後將被丟棄 |
| **hwmp-prep-lifetime** (*time*；預設：**5m**) | 由收到的 PREP 或 PREQ 訊息建立的路由的生存時間 |
| **hwmp-preq-destination-only** (*boolean*；預設：**yes**) | 是否只有目的節點可以響應 HWMP+ PREQ 訊息 |
| **hwmp-preq-reply-and-forward** (*boolean*；預設：**yes**) | 中間節點在響應 HWMP+ PREQ 訊息後是否應轉發該訊息。僅在 **hwmp-preq-destination-only** 停用時有用 |
| **hwmp-preq-retries** (*integer*；預設：**2**) | 在認為某個地址不可達之前，重試到該特定 MAC 地址的路由發現的次數 |
| **hwmp-preq-waiting-time** (*time*；預設：**4s**) | 等待對第一個 PREQ 訊息響應的時長。請注意，對於後續 PREQ，等待時間會按指數增加 |
| **hwmp-rann-interval** (*time*；預設：**10s**) | 傳送 HWMP+ RANN 訊息的頻率 |
| **hwmp-rann-lifetime** (*time*；預設：**1s**) | 由收到的 RANN 訊息建立的路由的生存時間 |
| **hwmp-rann-propagation-delay** (*time*；預設：**0.5s**) | 傳播 RANN 訊息前等待的時長。單位為秒 |
| **mesh-portal** (*boolean*；預設：**no**) | 此介面是否為 Mesh 網路中的門戶 |
| **mtu** (*number*；預設：**1500**) | 最大傳輸單元大小 |
| **name** (*string*；預設：) | 介面名稱 |
| **reoptimize-paths** (*boolean*；預設：**no**) | 是否定期傳送 PREQ 訊息以查詢已知的 MAC 地址。如果網路拓撲經常變化，啟用此設定會很有用。請注意，如果沒有收到對重新最佳化 PREQ 的回覆，現有路徑仍會保留（直到超時） |

### 埠 {#port}

| 屬性 | 描述 |
| :-- | :-- |
| **active-port-type** (*read-only: wireless \| WDS \| ethernet-mesh \| ethernet-bridge \| ethernet-mixed*；預設：) | 實際使用的埠型別和狀態 |
| **hello-interval** (*time*；預設：**10s**) | 傳送 HWMP+ Hello 訊息之間的最大間隔。僅用於乙太網型別埠 |
| **interface** (*interface name*；預設：) | 要加入 Mesh 的介面名稱 |
| **mesh** (*interface name*；預設：) | 此埠所屬的 Mesh 介面 |
| **path-cost** (*integer: 0..65535*；預設：**10**) | 到介面的路徑開銷，路由協定用它來確定“最佳”路徑 |
| **port-type** (*WDS \| auto \| ethernet \| wireless*；預設：) | 要使用的埠型別 auto - 埠型別根據底層介面的型別自動確定 WDS - 一個 Wireless Distribution System 介面。遠端 MAC 地址從無線連線資料中學習 ethernet - 遠端 MAC 地址從 HWMP+ Hello 訊息中學習，或從接收或轉發的流量中的源 MAC 地址學習 wireless - 遠端 MAC 地址從無線連線資料中學習 |

### FDB 狀態 {#fdb-status}

| 屬性 | 描述 |
| :-- | :-- |
| **mac-address** (*MAC address*) | 此 FDB 條目對應的 MAC 地址 |
| **seq-number** (*integer*) | 路由協定中用於避免環路的序列號 |
| **type** (*local \| outsider \| direct \| mesh \| neighbor \| larval \| unknown*) | 此 FDB 條目的型別 local -- MAC 地址屬於本地路由器本身 outsider -- MAC 地址屬於 Mesh 網路外部的裝置 direct -- MAC 地址屬於位於 Mesh 網路中某個介面上的無線用戶端 mesh -- MAC 地址屬於可透過 Mesh 網路訪問的裝置；它可以是 Mesh 網路的內部或外部裝置 neighbor -- MAC 地址屬於與本路由器直接相鄰的 Mesh 路由器 larval -- MAC 地址屬於可透過 Mesh 網路訪問的未知裝置 unknown -- MAC 地址屬於未知裝置 |
| **mesh** (*interface name*) | 此 FDB 條目所屬的 Mesh 介面 |
| **on-interface** (*interface name*) | 用於流量轉發的 Mesh 埠，類似於下一跳值 |
| **lifetime** (*time*) | 如果此條目未用於流量轉發，則剩餘生存時間 |
| **age** (*time*) | 此 FDB 條目的存在時間 |
| **metric** (*integer*) | 路由協定用於確定“最佳”路徑的度量值 |

## 示例 {#example}

![](/img/1760ef1412bdd0ee.webp)

此示例使用靜態 WDS 鏈路，這些鏈路在變為活動狀態時會動態新增為 Mesh 埠。使用兩個不同頻率：一個用於 AP 互連，另一個用於用戶端連線到 AP，因此 AP 必須至少有兩個無線介面。當然，所有連線也可以使用同一頻率，但由於潛在的干擾問題，效果可能不佳。

在所有 AP 上重複此配置：

```ros
/interface/mesh/add disabled=no
/interface/mesh/port/add interface=wlan1 mesh=mesh1
/interface/mesh/port/add interface=wlan2 mesh=mesh1

 # 用于 AP 互连的接口
/interface/wireless/set wlan1 disabled=no ssid=mesh frequency=2437 band=2ghz-b/g/n mode=ap-bridge \
 wds-mode=static-mesh wds-default-bridge=mesh1 

# 用于客户端连接的接口
 /interface/wireless/set wlan2 disabled=no ssid=mesh-clients frequency=5180 band=5ghz-a/n/ac mode=ap-bridge 

# 为每个要连接的 AP 创建一个静态 WDS 接口
/interface/wireless/wds/add disabled=no master-interface=wlan1 name=<descriptive name of remote end> \
 wds-address=<MAC address of remote end> 
```

這裡手動新增 WDS 介面，因為使用的是靜態 WDS 模式。如果使用 **wds-mode**=**dynamic-mesh**，所有 WDS 介面都會自動建立。此處指定 **frequency** 和 **band** 引數只是為了生成有效的示例配置；Mesh 協定執行絕不限於這些特定值，也不是針對它們最佳化的。

:::warning
你可能需要增大無線介面的 **disconnect-timeout** 選項，以使協定更穩定。
:::

在實際部署中，你還應使用 `/interface/wireless/security-profile` 來確保無線連線的安全。為簡單起見，這裡不展示該配置。

路由器 A 上的結果（有一個用戶端連線到 wlan2）：

```ros
[admin@A] > /interface/mesh/print
Flags: X - disabled, R - running
0 R name="mesh1" mtu=1500 arp=enabled mac-address=00:0C:42:0C:B5:A4 auto-mac=yes
admin-mac=00:00:00:00:00:00 mesh-portal=no hwmp-default-hoplimit=32
hwmp-preq-waiting-time=4s hwmp-preq-retries=2 hwmp-preq-destination-only=yes
hwmp-preq-reply-and-forward=yes hwmp-prep-lifetime=5m hwmp-rann-interval=10s
hwmp-rann-propagation-delay=1s hwmp-rann-lifetime=22s

[admin@A] > /interface/mesh/port/print detail
Flags: X - disabled, I - inactive, D - dynamic
0 interface=wlan1 mesh=mesh1 path-cost=10 hello-interval=10s port-type=auto port-type-used=wireless
1 interface=wlan2 mesh=mesh1 path-cost=10 hello-interval=10s port-type=auto port-type-used=wireless
2 D interface=router_B mesh=mesh1 path-cost=105 hello-interval=10s port-type=auto port-type-used=WDS
3 D interface=router_D mesh=mesh1 path-cost=76 hello-interval=10s port-type=auto port-type-used=WDS
```

此時 FDB（轉發資料庫）僅包含本地 MAC 地址、可透過本地介面訪問的非 Mesh 節點以及直接 Mesh 鄰居的資訊：

```ros
[admin@A] /interface/mesh/fdb/print
Flags: A - active, R - root
MESH TYPE MAC-ADDRESS ON-INTERFACE LIFETIME AGE
A mesh1 local 00:0C:42:00:00:AA 3m17s
A mesh1 neighbor 00:0C:42:00:00:BB router_B 1m2s
A mesh1 neighbor 00:0C:42:00:00:DD router_D 3m16s
A mesh1 direct 00:0C:42:0C:7A:2B wlan2 2m56s
A mesh1 local 00:0C:42:0C:B5:A4 2m56s

[admin@A] /interface/mesh/fdb/print detail
Flags: A - active, R - root
A mac-address=00:0C:42:00:00:AA type=local age=3m21s mesh=mesh1 metric=0 seqnum=4294967196
A mac-address=00:0C:42:00:00:BB type=neighbor on-interface=router_B age=1m6s mesh=mesh1 metric=132 seqnum=4294967196
A mac-address=00:0C:42:00:00:DD type=neighbor on-interface=router_D age=3m20s mesh=mesh1 metric=79 seqnum=4294967196
A mac-address=00:0C:42:0C:7A:2B type=direct on-interface=wlan2 age=3m mesh=mesh1 metric=10 seqnum=0
A mac-address=00:0C:42:0C:B5:A4 type=local age=3m mesh=mesh1 metric=0 seqnum=0
```

測試 ping 是否正常：

```ros
[admin@A] > /ping 00:0C:42:00:00:CC
00:0C:42:00:00:CC 64 byte ping time=108 ms
00:0C:42:00:00:CC 64 byte ping time=51 ms
00:0C:42:00:00:CC 64 byte ping time=39 ms
00:0C:42:00:00:CC 64 byte ping time=43 ms
4 packets transmitted, 4 packets received, 0% packet loss
round-trip min/avg/max = 39/60.2/108 ms
```

路由器 A 必須先發現到路由器 C 的路徑，因此第一次 ping 的時間略長。現在 FDB 還包含 00:0C:42:00:00:CC 的條目，型別為 "mesh"。

另外，測試 ARP 解析是否正常，以及 IP 層 ping 是否正常：

```ros
[admin@A] > /ping 10.4.0.3
10.4.0.3 64 byte ping: ttl=64 time=163 ms
10.4.0.3 64 byte ping: ttl=64 time=46 ms
10.4.0.3 64 byte ping: ttl=64 time=48 ms
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 46/85.6/163 ms
```

#### Mesh 路由跟蹤 {#mesh-traceroute}

還有一個 mesh traceroute 命令，可幫助你確定路由使用了哪些路徑。

例如，對於此網路：

```ros
[admin@1] /interface/mesh/fdb/print
Flags: A - active, R - root
MESH TYPE MAC-ADDRESS ON-INTERFACE LIFETIME AGE
A mesh1 local 00:0C:42:00:00:01 7m1s
A mesh1 mesh 00:0C:42:00:00:02 wds4 17s 4s
A mesh1 mesh 00:0C:42:00:00:12 wds4 4m58s 1s
A mesh1 mesh 00:0C:42:00:00:13 wds4 19s 2s
A mesh1 neighbor 00:0C:42:00:00:16 wds4 7m1s
A mesh1 mesh 00:0C:42:00:00:24 wds4 18s 3s
```

到 00:0C:42:00:00:12 的 traceroute 顯示：

```ros
[admin@1] /interface/mesh/traceroute mesh1 00:0C:42:00:00:12
ADDRESS TIME STATUS
00:0C:42:00:00:16 1ms ttl-exceeded
00:0C:42:00:00:02 2ms ttl-exceeded
00:0C:42:00:00:24 4ms ttl-exceeded
00:0C:42:00:00:13 6ms ttl-exceeded
00:0C:42:00:00:12 6ms success
```

## 協定說明 {#protocol-description}

### 按需模式 {#reactive-mode}

路由器 A 想要發現到 C 的路徑：

![](/img/47c65b5c48bfc40e.webp)  

路由器 C 向 A 傳送單播響應：
![](/img/082c745aa3090e0e.webp)

在按需模式下，HWMP+ 非常類似於 AODV（Ad-hoc On-demand Distance Vector）。所有路徑都按需發現，方式是在網路中泛洪 Path Request (PREQ) 訊息。目的節點或某個擁有到目的地的路徑的路由器會用 Path Response (PREP) 回覆。請注意，如果目的地址屬於某個用戶端，則該用戶端連線的 AP 將作為其代理（即代表它回覆 PREQ）。

此模式最適合行動網路，和/或大部分通訊發生在 Mesh 內部節點之間的情況。

### 主動模式 {#proactive-mode}

根節點透過泛洪 RANN 來宣告自身：

![](/img/73dd8c90f0b07352.webp)  

內部節點用 PREG 響應：
![](/img/7d78350bb549d5cd.webp)  

在主動模式下，會有一些路由器配置為門戶。通常，作為門戶意味著該路由器具有連線到其他網路的介面，即它是 Mesh 網路的入口/出口點。

門戶會透過在網路中泛洪 Root Announcement (RANN) 訊息來宣告自己的存在。內部節點會用 Path Registration (PREG) 訊息回覆。此過程的結果是以門戶為根的路由樹。

到門戶的路由將充當一種預設路由。如果內部路由器不知道到特定目的地的路徑，它會將所有資料轉發到最近的門戶。然後，門戶會在需要時代表該路由器發現路徑。之後資料將流經門戶。除非資料是發往門戶本身或門戶具有介面的某個外部網路，否則這可能導致次優路由。

當大部分流量在內部 Mesh 節點和少數門戶節點之間傳輸時，主動模式最適合。

### 拓撲變化檢測 {#topology-change-detection}

資料流路徑：
![](/img/9ce080b253f40857.webp)

鏈路消失後，錯誤會向上遊傳播：
![](/img/b221bdf77838181d.webp)  

HWMP+ 使用 Path Error (PERR) 訊息通知鏈路已消失。該訊息會傳播到資料來源為止的所有上游節點。源節點在收到 PERR 後會重新啟動路徑發現過程。

## 常見問題 {#faq}

**問：與 RSTP 相比，這有什麼優勢？**

答：它提供最優路由。RSTP 僅用於防止環路。

**問：路由選擇是如何進行的？**

答：發現過程結束後，始終選擇度量值最佳的路由。還有一個配置選項可定期重新最佳化已知路由。

路由度量按各鏈路度量之和計算。

鏈路度量的計算方式與 (R)STP 協定相同：

- 對於乙太網鏈路，度量是靜態配置的（例如，與 OSPF 相同）。
- 對於 WDS 鏈路，度量會根據實際鏈路頻寬動態更新，而頻寬又受無線訊號強度和所選資料傳輸速率影響。

目前，該協定不考慮鏈路上正在使用的頻寬量，但將來也可能會使用這一資訊。

**問：與 OSPF/RIP/三層路由（總體而言）相比，這有什麼優勢？**

答：WDS 網路通常是橋接的，而不是路由的。自配置能力對 Mesh 網路很重要，而路由通常比橋接需要多得多的配置。當然，你始終可以在橋接網路上執行任何 L3 路由協定，但對於 Mesh 網路來說，這通常沒有什麼意義。

:::warning
由於 Mesh 協定不包含最佳化的二層組播轉發，最好避免在 Mesh 網路上轉發任何組播流量（包括 OSPF）。如果需要 OSPF，則必須改為配置使用單播模式的 [OSPF NBMA](../../user-guides/routing-and-networking-protocols/unicast/ospf/neighbour-relationship.md#discovery-on-nbma-subnets) 鄰居。
:::

**問：效能/CPU 要求如何？**

答：如果配置得當，協定本身佔用的資源將遠少於（例如）OSPF。單個路由器上的資料轉發效能應接近橋接的效能。

**問：它如何與使用 RSTP 的現有 Mesh 部署協同工作？**

答：RSTP 網路的內部結構對 Mesh 協定是透明的（因為 Mesh hello 封包會在 RSTP 網路內部轉發）。Mesh 會將 RSTP 網路中兩個入口點之間的路徑視為單個段。另一方面，Mesh 網路對 RSTP 不是透明的，因為 RSTP hello 封包不會在 Mesh 網路內部轉發。

:::warning
如果 Mesh 網路在兩個或多個點連線到 RSTP 網路，則可能出現路由環路！
:::

請注意，如果兩個接入點之間有 WDS 鏈路，則兩端必須具有相同的配置（兩端都作為 Mesh 中的埠，或兩端都作為橋接介面中的埠）。

你也可以將橋接介面作為 Mesh 埠（例如，以便使用橋接防火牆）。

**問：可以有多個網路入口/出口點嗎？**

答：如果入口/出口點配置為門戶（即使用主動模式），Mesh 網路內的每個路由器都會選擇最近的門戶並將所有資料轉發到該門戶。然後，門戶會在需要時代表該路由器發現路徑。

**問：如何控制或過濾 Mesh 流量？**

答：目前唯一的方法是使用橋接防火牆。建立一個橋接介面，將 WDS 介面和/或乙太網介面放入該橋接，然後將該橋接放入 Mesh 介面。接著配置橋接防火牆規則。

要匹配用於 Mesh 流量封裝的 MAC 協定，請使用 MAC 協定號 0x9AAA；要匹配 Mesh 路由流量，請使用 MAC 協定號 0x9AAB。例如：

```ros
/interface/bridge/settings/set use-ip-firewall=yes 
/interface/bridge/filter/add chain=input action=log mac-protocol=0x9aaa 
/interface/bridge/filter/add chain=input action=log mac-protocol=0x9aab
```

:::warning
完全可能建立無法工作的混合 Mesh/橋接部署（例如，將 *問題示例 1* 中的交換器替換為橋接）。推薦的始終有效的故障安全方法是：為每個物理介面建立一個單獨的橋接介面；然後將所有這些橋接介面新增為 Mesh 埠。
:::

## 高階主題 {#advanced-topics}

我們都知道，容易做出有問題的二層橋接或路由配置，並且可能很難偵錯（與三層路由配置相比）。因此，這裡給出幾個可能會給你帶來問題的錯誤配置示例。請避免它們！

### 問題示例 1：Mesh 內部的乙太網交換器 {#problematic-example-1-ethernet-switch-inside-a-mesh}

*路由器 A 在 Mesh 外部；其餘所有路由器都在內部。對於路由器 B、C、D，所有介面都新增為 Mesh 埠*：
![](/img/92bc53a2f8c65140.webp)

路由器 A 將無法與路由器 C 可靠通訊。當 D 是乙太網的指定路由器時，問題就會顯現；如果 B 承擔此角色，則一切正常。問題的主要原因是乙太網交換器上的 MAC 地址學習。

考慮一下當路由器 A 想向 C 傳送資料時會發生什麼。我們假設路由器 A 要麼知道路徑，要麼將資料泛洪到所有介面。無論哪種方式，資料都會到達交換器。交換器對目的 MAC 地址一無所知，因此會將資料轉發給 B 和 D。

現在會發生什麼：

1. B 在 Mesh 介面上收到該封包。由於該 MAC 地址不是 B 本地的，並且 B 知道自己不是乙太網網路的指定路由器，因此它直接忽略該封包。
2. D 在 Mesh 介面上收到該封包。由於該 MAC 地址不是 D 本地的，並且 D 是乙太網網路的指定路由器，因此它啟動到 C 的路徑發現過程。

路徑發現完成後，D 得知可透過 B 到達 C。現在 D 封裝該封包並將其轉發回乙太網網路。封裝後的封包由交換器轉發，由 B 接收並轉發，然後由 C 接收。到目前為止一切正常。

現在 C 很可能會響應該封包。由於 B 已經知道 A 在哪裡，它會解封裝並轉發回覆封包。但現在交換器會學習到：可透過 B 到達 C 的 MAC 地址！這意味著，下次從 A 發往 C 的資料到達時，交換器將*僅*把資料轉發給 B（而 B 當然會靜默忽略該封包）！

相反，如果 B 承擔指定路由器的角色，則一切正常，因為流量不必兩次經過乙太網交換器。

***故障排除***：要麼避免這種部署，要麼在交換器上停用 MAC 地址學習。請注意，在許多交換器上這是不可能的。

另請注意，如果滿足以下任一條件，就不會有問題：

- 路由器 A 支援 HWMP+，並已配置使用 HWMP+。
- 或者將乙太網交換器替換為支援 HWMP+ 且已將乙太網介面新增為 Mesh 埠的路由器。

### 問題示例 2：無線模式 {#problematic-example-2-wireless-modes}

*考慮這個（無效的）配置示例*...*路由器 A 和 B 在 Mesh 內部，路由器 C 在外部。對於路由器 A 和 B，所有介面都新增為 Mesh 埠：*

![](/img/1e417ebd5022491a.webp)

現在無法在路由器 B 上橋接 wlan1 和 wlan2。如果你瞭解 WDS 的工作原理，原因就相當明顯。WDS 通訊使用四地址幀。這是因為對於無線多跳轉發，你需要知道中間跳的地址，以及原始傳送方和最終接收方的地址。相比之下，非 WDS 的 802.11 通訊在一幀中僅包含三個 MAC 地址。這就是為什麼在 station 模式下無法進行多跳轉發。

***故障排除***取決於你想實現什麼：

1. 如果你希望路由器 C 充當中繼器（用於無線或乙太網流量），請配置路由器 B 和路由器 C 之間的 WDS 鏈路，並在所有節點上執行 Mesh 路由協定。
2. 在其他情況下，將路由器 B 上的 wlan2 配置為 AP 模式，並將路由器 C 上的 WLAN 配置為 station 模式。
