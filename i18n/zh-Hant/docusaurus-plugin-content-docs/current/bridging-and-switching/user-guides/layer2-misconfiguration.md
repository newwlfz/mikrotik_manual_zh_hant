---
sidebar_key: "bridging-and-switching/user-guides/layer2-misconfiguration"
sidebar_position: 5
title: "Layer2 配置錯誤"
sidebar_label: "Layer2 配置錯誤"
description: "本頁介紹 MikroTik RouterOS 中的二層（Layer2）配置錯誤，重點討論橋接配置不當並啟用硬體解除安裝以及埠隔離等問題。文中說明了吞吐量偏低、CPU 佔用過高以及硬體解除安裝標誌不正確等症狀，並針對不支援埠隔離的裝置給出瞭解決方案。"
tags:
  - 'bridging'
  - 'hardware-offloading'
  - 'mac-learning'
source: https://manual.mikrotik.com/docs/bridging-and-switching/user-guides/layer2-misconfiguration
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

---

有些配置在設計上就存在重大缺陷，應儘可能避免。配置錯誤的 Layer2 有時會導致難以檢測的網路錯誤、隨機效能下降、網路中的某些網段不可達、某些網路服務執行異常，甚至整個網路故障。本頁將介紹一些常見以及不太常見的、會導致網路問題的配置。

## 單個交換晶片上的網橋 {#bridges-on-a-single-switch-chip}

---

考慮以下場景。你有一臺帶內建交換晶片的裝置，並且需要將某些埠彼此隔離。因此，你建立了多個網橋並在其上啟用了硬體解除安裝。由於每個網橋位於不同的 Layer2 域，Layer2 幀不會在這些網橋之間轉發。結果是，每個網橋中的埠與其他網橋上的埠相互隔離。

### 配置 {#configuration}

```ros
/interface/bridge
add name=bridge1
add name=bridge2
/interface/bridge/port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether2
add bridge=bridge2 interface=ether3
add bridge=bridge2 interface=ether4
```

### 問題 {#problem}

經過一次簡單的效能測試後，你可能會注意到一個網橋能夠以線速轉發流量，而第二個、第三個等網橋無法像第一個網橋那樣轉發那麼多資料。另一個症狀可能是需要路由的封包存在巨大延遲。快速檢查後，你可能會注意到 CPU 始終處於滿載狀態。這是因為硬體解除安裝並非在所有網橋上可用，而只在一個網橋上可用。透過檢查硬體解除安裝狀態，你會注意到只有一個網橋啟用了它：

```ros
[admin@MikroTik] > /interface/bridge/port/print
Flags: X - disabled, I - inactive, D - dynamic, H - hw-offload 
 #     INTERFACE                                 BRIDGE                                 HW
 0   H ether1                                    bridge1                                yes
 1   H ether2                                    bridge1                                yes
 2     ether3                                    bridge2                                yes
 3     ether4                                    bridge2                                yes
```

只有一個網橋具有硬體解除安裝標誌的原因是裝置不支援埠隔離。如果不支援埠隔離，那麼只有一個網橋能夠將流量解除安裝到交換晶片。

### 症狀 {#symptoms}

以下是此類錯誤配置可能導致的症狀列表：

- 網橋埠缺少 "H" 標誌。
- 吞吐量低。
- CPU 使用率高。

### 解決方案 {#solution}

並非所有裝置都支援埠隔離。目前只有 CRS1xx/CRS2xx 系列裝置支援它，並且同時只支援 7 個隔離且硬體解除安裝的網橋。其他裝置將不得不使用 CPU 在其他網橋上轉發封包。這通常是硬體限制，可能需要更換裝置。Bridge split-horizon 引數是一種軟體功能，會停用硬體解除安裝；使用網橋過濾規則時，需要啟用將所有封包轉發到 CPU，這要求停用硬體解除安裝。你可以透過 `hw=yes` 標誌控制哪個網橋進行硬體解除安裝，並將其他網橋設定為 `hw=no`，例如：

```ros
/interface/bridge/port/set [find where bridge=bridge1] hw=no
/interface/bridge/port/set [find where bridge=bridge2] hw=yes
```

有時可以重構網路拓撲以使用 VLAN，這是隔離 Layer2 網路的正確方式。

## 啟用硬體解除安裝和 MAC 學習時的封包流 {#packet-flow-with-hardware-offloading-and-mac-learning}

---

考慮以下場景：你設定了一個網橋並啟用了硬體解除安裝，以便最大化裝置吞吐量；結果，你的裝置像交換器一樣工作，但你想使用 [封包嗅探器](../../diagnostics-monitoring-and-troubleshooting/packet-sniffer.md) 或 [Torch](../../diagnostics-monitoring-and-troubleshooting/torch.md) 工具進行偵錯，或者也許你想實現封包日誌記錄。

### 配置 {#configuration-1}

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 hw=yes interface=ether1 learn=yes
add bridge=bridge1 hw=yes interface=ether2 learn=yes
```

### 問題 {#problem-1}

執行 [封包嗅探器](../../diagnostics-monitoring-and-troubleshooting/packet-sniffer.md) 或 [Torch](../../diagnostics-monitoring-and-troubleshooting/torch.md) 工具捕獲封包時，你可能會注意到幾乎看不到任何封包，只能看到一些單播封包，但捕獲到的大多是廣播/組播封包，而介面報告某些介面中流動的流量遠大於捕獲到的流量。如果將兩個或更多乙太網介面新增到網橋並啟用[硬體解除安裝](../index.md#bridge-hardware-offloading)，那麼交換晶片將用於在埠之間轉發封包。要理解為什麼只捕獲到部分封包，我們必須先檢查交換晶片如何與 CPU 互連。在此示例中，我們可以使用一個通用 5 埠乙太網路由器的框圖：

![Switch Chip Block Diagram](/img/ec5a5a402792668a.webp)

對於此裝置，每個乙太網埠都連線到交換晶片，而交換晶片透過 CPU 埠（有時稱為 **switch-cpu** 埠）連線到 CPU。要讓封包在 Sniffer 或 Torch 工具中可見，封包必須從乙太網埠傳送到 CPU 埠，這意味著封包必須發往 CPU 埠（封包的目標 MAC 地址與網橋的 MAC 地址匹配），或者封包的 MAC 地址尚未被學習（封包被泛洪到所有埠），這種行為是由 **MAC 學習**導致的。

交換晶片維護一份 MAC 地址和埠列表，稱為 **主機表**。每當需要轉發封包時，交換晶片會檢查封包的目標 MAC 地址與主機表，以找出應該使用哪個埠轉發封包。如果交換晶片找不到目標 MAC 地址，則封包會被泛洪到所有埠（包括 CPU 埠）。在封包本應從例如 ether1 轉發到 ether2，且 ether2 後面裝置 MAC 地址在主機表中的情況下，封包永遠不會發送到 CPU，因此對 Sniffer 或 Torch 工具不可見。

### 症狀 {#symptoms-1}

以下是此類錯誤配置可能導致的症狀列表：

- Sniffer 或 Torch 工具看不到封包。
- 過濾規則不生效。

### 解決方案 {#solution-1}

目標 MAC 地址已被學習的封包不會發送到 CPU，因為這些封包不會泛洪到所有埠。如果你確實需要將某些封包傳送到 CPU 以供封包分析器或防火牆使用，則可以使用 ACL 規則將封包複製或重定向到 CPU。以下是傳送發往 **4C:5E:0C:4D:12:4B** 的封包副本的示例：

```ros
/interface/ethernet/switch/rule
add copy-to-cpu=yes dst-mac-address=4C:5E:0C:4D:12:4B/FF:FF:FF:FF:FF:FF ports=ether1 switch=switch1
```

:::warning
如果封包被髮送到 CPU，那麼封包必須由 CPU 處理；這會增加 CPU 負載。
:::

## LAG 介面與負載均衡 {#lag-interfaces-and-load-balancing}

---

考慮以下場景：你建立了一個 LAG 介面，以增加兩個網路節點之間的總頻寬；通常這些節點是交換器。為了測試 LAG 介面是否正常工作，你連線了兩臺傳輸資料的伺服器，最常用的是眾所周知的網路效能測量工具 [Iperf](https://en.wikipedia.org/wiki/Iperf) 來測試此類設定。例如，你可能用兩個千兆乙太網埠組成了一個 LAG 介面，這為你提供了一個虛擬介面，可以在兩個介面上對流量進行負載均衡，理論上可達到 2Gbps 吞吐量，而伺服器使用 10Gbps 介面連線，例如 SFP+。

![LACP Setup](/img/fa65c1f36095531a.webp)

### 配置 {#configuration-2}

以下配置與 **SW1** 和 **SW2** 相關：

```ros
/interface/bonding
add mode=802.3ad name=bond1 slaves=ether1,ether2
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=bond1
add bridge=bridge1 interface=sfp-sfpplus1
```

### 問題 {#problem-2}

初始測試後，你會立即注意到網路吞吐量從未超過 1Gbps 限制，即使伺服器和網路節點（此處為交換器）上的 CPU 負載都很低，但吞吐量仍然僅限 1Gbps。背後的原因是 LACP (802.ad) 使用傳輸雜湊策略來確定流量是否可以在多個 LAG 成員上均衡；在這種情況下，LAG 介面並不會建立一個 2Gbps 介面，而是建立一個在可能時可以在多個從介面上均衡流量的介面。每個封包都會生成一個傳輸雜湊，這決定封包將透過哪個 LAG 成員傳送，這是為了避免封包亂序所必需的；可以選擇傳輸雜湊策略，通常可以在 Layer2 (MAC)、Layer3 (IP) 和 Layer4 (Port) 之間選擇，在 RouterOS 中，可以透過 `transmit-hash-policy` 引數選擇。在這種情況下，由於你將封包傳送到相同的目標 MAC 地址以及相同的 IP 地址，並且 Iperf 也使用相同的埠，因此傳輸雜湊相同，這為所有封包生成相同的傳輸雜湊，LAG 成員之間的負載均衡無法實現。請注意，即使目標不同，封包也不一定總能在 LAG 成員之間均衡，這是因為標準化的傳輸雜湊策略可能為不同目標生成相同的傳輸雜湊，例如，使用 `layer2-and-3` 傳輸雜湊策略且目標 MAC 地址相同時，192.168.0.1/192.168.0.2 會被均衡，但 192.168.0.2/192.168.0.4 **不會**被均衡。

### 症狀 {#symptoms-2}

以下是此類錯誤配置可能導致的症狀列表：

- 流量只經過一個 LAG 成員。

### 解決方案 {#solution-2}

選擇適當的傳輸雜湊策略並正確測試網路吞吐量。測試此類設定的最簡單方法是使用多個目標，例如，不要只向一臺伺服器傳送資料，而是向多臺伺服器傳送資料。這將為每個封包生成不同的傳輸雜湊，並使 LAG 成員之間的負載均衡成為可能。對於某些設定，你可能需要更改繫結介面模式以增加總吞吐量。對於 UDP 流量，`balance-rr` 模式可能足夠，但可能會給 TCP 流量帶來問題。你可以[在此處](../../high-availability-solutions/bonding.md#bonding-modes)閱讀更多關於為你的設定選擇正確模式的內容。

## 從介面上的 VLAN 介面 {#vlan-interface-on-a-slave-interface}

---

考慮以下場景：你建立了一個網橋，並希望 DHCP Server 只向某些帶標籤的 VLAN 流量分配 IP 地址；因此，你建立了一個 VLAN 介面，指定了 VLAN ID，並在其上建立了 DHCP Server，但出於某種原因，它無法正常工作。

### 配置 {#configuration-3}

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add interface=ether1 bridge=bridge1
add interface=ether2 bridge=bridge1
/interface/vlan
add name=VLAN99 interface=ether1 vlan-id=99
/ip/pool
add name=VLAN99_POOL range=192.168.99.100-192.168.99.200
/ip/address/add address=192.168.99.1/24 interface=VLAN99
/ip/dhcp-server
add interface=VLAN99 address-pool=VLAN99_POOL disabled=no
/ip/dhcp-server/network
add address=192.168.99.0/24 gateway=192.168.99.1 dns-server=192.168.99.1
```

### 問題 {#problem-3}

當你將介面新增到網橋時，網橋成為主介面，所有網橋埠成為從埠。這意味著在網橋埠上接收到的所有流量都會被網橋介面捕獲，並且所有流量會使用網橋介面而不是物理介面轉發到 CPU。結果是，在從介面上建立的 VLAN 介面將完全無法捕獲任何流量，因為在執行任何封包處理之前，流量會立即轉發到主介面。通常的副作用是一些 DHCP 用戶端收到 IP 地址，而另一些則沒有。

### 症狀 {#symptoms-3}

以下是此類錯誤配置可能導致的症狀列表：

- DHCP 用戶端/伺服器無法正常工作。
- 裝置不可達。
- 網橋後面的裝置無法透過帶標籤流量訪問。

### 解決方案 {#solution-3}

更改 VLAN 介面監聽流量的介面，將其改為主介面：

```ros
/interface/vlan/set VLAN99 interface=bridge1
```

## 網橋內網橋上的 VLAN {#vlan-on-a-bridge-in-a-bridge}

---

考慮以下場景：你有一組介面（不必是物理介面），並且希望它們都處於同一個 Layer2 段中。解決方案是將它們新增到一個網橋中，但你要求來自一個埠的流量將所有流量標記到某個 VLAN。這可以透過在網橋介面之上建立 VLAN 介面，並建立一個單獨的網橋來實現，該網橋包含這個新建立的 VLAN 介面以及一個應該為所有接收到的流量新增 VLAN 標籤的介面。網路圖如下：

![VLAN on Bridge in Bridge](/img/fdbfbd53e29c7dbf.webp)

### 配置 {#configuration-4}

```ros
/interface/bridge
add name=bridge1
add name=bridge2
/interface/vlan
add interface=bridge1 name=VLAN vlan-id=99
/interface/bridge/port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether2
add bridge=bridge2 interface=VLAN
add bridge=bridge2 interface=ether3
```

### 問題 {#problem-4}

為了更好地理解底層問題，我們先檢視網橋主機表。

```ros
[admin@switch] /interface/bridge/host/print where !local 
Flags: X - disabled, I - invalid, D - dynamic, L - local, E - external 
 #       MAC-ADDRESS        VID ON-INTERFACE    BRIDGE
 0   D   CC:2D:E0:E4:B3:A1      ether1          bridge1
 1   D   CC:2D:E0:E4:B3:A2      ether2          bridge1
 2   D   CC:2D:E0:E4:B3:A1      VLAN            bridge2
 3   D   CC:2D:E0:E4:B3:A2      VLAN            bridge2
 4   D   CC:2D:E0:E4:B3:A3      ether3          bridge2
```

**ether1** 和 **ether2** 上的裝置需要傳送帶有 VLAN-ID 99 的帶標籤封包，才能到達 **ether3** 上的主機（其他封包不會傳遞到 VLAN 介面並進一步與 ether3 橋接）。我們可以在主機表中看到 **bridge2** 已學習這些主機。從 **ether3** 發往 **ether1** 的封包將正確地以帶標籤方式傳送出去，並且流量不會在 **bridge1** 中泛洪。但由於 MAC 學習只能在網橋埠之間進行，而不能在網橋介面之上建立的介面上進行，因此從 **ether2** 傳送到 **ether3** 的封包將在 **bridge1** 中泛洪。

此外，如果 **ether3** 後面的裝置使用 (R)STP，那麼 **ether1** 和 **ether2** 將傳送帶標籤的 BPDU，這違反了 IEEE 802.1W 標準。由於 MAC 學習功能損壞以及 (R)STP 損壞，必須避免這種設定和配置。還已知在某些設定中，這種配置會阻止你透過 MAC telnet 連線到裝置。

### 症狀 {#symptoms-4}

以下是此類錯誤配置可能導致的症狀列表：

- 埠被 RSTP 阻塞。
- 網路中出現環路。
- 埠抖動。
- 流量被泛洪到所有埠。
- MAC telnet 無法連線。
- 裝置不可訪問。

### 解決方案 {#solution-4}

使用網橋 VLAN 過濾。標記流量的正確方式是在流量進入網橋時分配 VLAN ID。透過為網橋埠指定 **PVID** 值，並指定哪些埠是 **tagged**（trunk）埠、哪些是 **untagged**（access）埠，可以輕鬆實現這種行為。以下是此類設定本應如何配置的示例：

```ros
/interface/bridge
add name=bridge1 vlan-filtering=yes
/interface/bridge/port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=ether3 pvid=99
/interface/bridge/vlan
add bridge=bridge1 tagged=ether1,ether2 untagged=ether3 vlan-ids=99
```

:::danger
啟用 `vlan-filtering` 後，你將過濾掉髮往 CPU 的流量；在啟用 VLAN 過濾之前，應確保設定好[管理埠](../index.md#management-access-configuration)。
:::

## 帶有物理介面的網橋中的 VLAN {#vlan-in-a-bridge-with-a-physical-interface}

---

與[網橋內網橋上的 VLAN](./layer2-misconfiguration.md#vlan-on-a-bridge-in-a-bridge)非常相似。最常見的用例是將物理介面與 VLAN 橋接（簡化的 trunk/access 埠設定）。在這種設定中，你可能希望在一側傳送帶標籤流量，在另一側傳送不帶標籤流量。為此，你在 trunk 埠（帶標籤側）上建立 VLAN 介面，然後建立網橋，並將 VLAN 介面和物理介面（不帶標籤側）都新增為網橋埠。

### 配置 {#configuration-5}

```ros
/interface/vlan
add interface=ether1 name=VLAN99 vlan-id=99
/interface/bridge
add name=bridge1
/interface/bridge/port
add interface=ether2 bridge=bridge1
add interface=VLAN99 bridge=bridge1
```

### 問題 {#problem-5}

這種設定和配置在大多數情況下可以工作，但在使用 (R/M)STP 時違反了 IEEE 802.1W 標準。如果這是你 Layer2 域中的唯一裝置，那麼這不應導致問題，但當存在其他廠商交換器時可能會出現問題。原因是網橋介面上的 RSTP 預設啟用，允許從每個網橋埠傳送網橋協定資料單元 (BPDU)。雖然 **ether2** 正確地傳送不帶標籤的 BPDU，但作為網橋埠的 **VLAN99** 介面會透過 ether1 傳送帶標籤的 BPDU。並非所有交換器都能理解帶標籤的 BPDU。在更復雜的網路中，某些（組）VLAN 存在多個網路拓撲時，採用此配置應謹慎。這與混合廠商裝置中的 MSTP 和 PVSTP(+) 相關。在具有多個 VLAN 網路拓撲的環形拓撲中，交換器的一個埠會被阻塞，但在 MSTP 和 PVSTP(+) 中，可以為某個 VLAN 開啟一條路徑；在這種情況下，不支援 PVSTP(+) 的裝置可能會去除 BPDU 的標籤並轉發 BPDU，結果交換器將收到自己的封包，觸發環路檢測並阻塞埠。這也會發生在其他協定上，但 (R)STP 是最常見的情況。如果交換器使用 BPDU guard 功能，那麼這種型別的配置可能觸發它並導致埠被 STP 阻塞。據報道，在使用 6.41 或更高版本時，這種型別的配置會隨時間推移阻止流量在某些網橋埠上轉發。這種型別的配置不僅會破壞 (R/M)STP，還可能導致環路警告。這可能由 MNDP 封包或從介面直接傳送出的任何其他封包引起。

### 症狀 {#symptoms-5}

以下是此類錯誤配置可能導致的症狀列表：

- 埠被 RSTP 阻塞。
- 網路中出現環路。
- 埠抖動。
- 流量隨時間推移停止轉發。
- BPDU 被其他啟用了 RSTP 的裝置忽略。

### 解決方案 {#solution-5}

為避免相容性問題，應使用網橋 VLAN 過濾。下面你可以找到一個示例，說明如何透過網橋 VLAN 過濾配置實現相同的流量標記效果：

```ros
/interface/bridge
add name=bridge1 vlan-filtering=yes
/interface/bridge/port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether2 pvid=99
/interface/bridge/vlan
add bridge=bridge1 tagged=ether1 untagged=ether2 vlan-ids=99
```

:::danger
啟用 `vlan-filtering` 後，您將過濾掉髮往 CPU 的流量。在啟用 VLAN 過濾之前，應確保已設定[管理埠](../index.md#management-access-configuration)。
:::

## 物理介面上的橋接 VLAN {#bridged-vlan-on-physical-interfaces}

---

與[網橋內網橋上的 VLAN](./layer2-misconfiguration.md#vlan-on-a-bridge-in-a-bridge)非常相似：考慮以下場景。你的網路中有幾臺交換器，並使用 VLAN 隔離某些 Layer2 域，並將這些交換器連線到一臺路由器，由該路由器分配地址並將流量路由到外部網路。為了實現冗餘，你將所有交換器直接連線到路由器並啟用了 RSTP，但為了能夠設定 DHCP Server，你決定可以在每個連線到交換器的物理介面上為每個 VLAN 建立一個 VLAN 介面，並將這些 VLAN 介面新增到網橋中。網路圖如下：

![Bridged VLANs](/img/3cff20b2aa3e5fb4.webp)

### 配置 {#configuration-6}

此案例只涉及路由器部分，交換器配置並不重要，只要埠處於交換狀態即可。路由器配置如下：

```ros
/interface/bridge
add name=bridge10
add name=bridge20
/interface/vlan
add interface=ether1 name=ether1_v10 vlan-id=10
add interface=ether1 name=ether1_v20 vlan-id=20
add interface=ether2 name=ether2_v10 vlan-id=10
add interface=ether2 name=ether2_v20 vlan-id=20
/interface/bridge/port
add bridge=bridge10 interface=ether1_v10
add bridge=bridge10 interface=ether2_v10
add bridge=bridge20 interface=ether1_v20
add bridge=bridge20 interface=ether2_v20
```

### 問題 {#problem-6}

你可能會注意到網路出現一些奇怪的延遲，甚至網路無響應。你可能會注意到檢測到環路（收到帶有自己 MAC 地址的封包），並且一些流量不知從何處生成。問題發生的原因是，來自 **Router** 上建立的任一 VLAN 介面的廣播封包將被髮送出物理介面，該封包將透過物理介面、經過交換器轉發，並會在另一個物理介面上被接收；在這種情況下，從 **ether1\_v10** 傳送出的廣播封包將在 **ether2** 上被接收，該封包將被 **ether2\_v10** 捕獲，而 **ether2\_v10** 與 **ether1\_v10** 橋接，並會再次透過相同路徑轉發（環路）。(R)STP 可能並不總能檢測到此環路，因為 (R)STP 不知道任何 VLAN。不帶標籤流量不存在環路，但帶標籤流量存在環路。在此場景中，環路相當明顯，但在更復雜的設定中，並不總是容易發現網路設計缺陷。有時如果網路不使用廣播流量，這種網路設計缺陷可能會在很長時間內不被注意到；通常，[鄰居發現](../../system-information-and-utilities/neighbor-discovery.md) 會從 VLAN 介面廣播封包，並通常會在這種設定中觸發環路檢測。有時捕獲觸發環路檢測的封包很有用，這可以透過使用 sniffer 並分析封包捕獲檔案來完成：

```ros
/tool/sniffer
set filter-mac-address=4C:5E:0C:4D:12:44/FF:FF:FF:FF:FF:FF \
filter-interface=ether1 filter-direction=rx file-name=loop_packet.pcap
```

或者使用日誌的更便捷方式：

```ros
/interface/bridge/filter
add action=log chain=forward src-mac-address=4C:5E:0C:4D:12:44/FF:FF:FF:FF:FF:FF
add action=log chain=input src-mac-address=4C:5E:0C:4D:12:44/FF:FF:FF:FF:FF:FF
```

### 症狀 {#symptoms-6}

以下是此類錯誤配置可能導致的症狀列表：

- 埠被 (R)STP 阻塞。
- 網路中出現環路。
- 吞吐量低。
- 埠抖動。
- 網路不可訪問。

### 解決方案 {#solution-6}

解決方案是使用網橋 VLAN 過濾，使所有網橋相容 IEEE 802.1W 和 IEEE 802.1Q。

```ros
/interface/bridge
add name=bridge vlan-filtering=yes
/interface/bridge/port
add bridge=bridge interface=ether1
add bridge=bridge interface=ether2
/interface/bridge/vlan
add bridge=bridge tagged=ether1,ether2,bridge vlan-ids=10
add bridge=bridge tagged=ether1,ether2,bridge vlan-ids=20
/interface/vlan
add name=vlan10 interface=bridge vlan-id=10
add name=vlan20 interface=bridge vlan-id=20
```

:::danger
啟用 `vlan-filtering` 後，您將過濾掉髮往 CPU 的流量。在啟用 VLAN 過濾之前，應確保已設定[管理埠](../index.md#management-access-configuration)。
:::

## 橋接 VLAN {#bridged-vlan}

---

[物理介面上的橋接 VLAN](./layer2-misconfiguration.md#bridged-vlan-on-physical-interfaces)的一個更簡化場景，但在這種情況下，你只是想將不同物理介面上建立的兩個或多個 VLAN 橋接在一起。這是一種非常常見的設定型別，值得單獨寫一篇文章，因為錯誤配置這種型別的設定已經導致了多次網路故障。這種型別的設定也用於 VLAN 轉換。

### 配置 {#configuration-7}

```ros
/interface/vlan
add interface=ether1 name=ether1_v10 vlan-id=10
add interface=ether2 name=ether2_v10 vlan-id=10
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether1_v10
add bridge=bridge1 interface=ether2_v10
```

### 問題 {#problem-7}

你可能會注意到網路的某些部分不可訪問和/或某些鏈路持續抖動。這是由於 (R)STP。這種型別的配置會強制裝置傳送帶標籤的 BPDU，而其他裝置（包括 RouterOS）可能不支援這些 BPDU。由於裝置收到格式錯誤的封包（執行 (R)STP 時，網路中不應存在帶標籤的 BPDU，這違反了 IEEE 802.1W 和 IEEE 802.1Q），裝置將無法正確解釋該封包，並可能出現意外行為。

### 症狀 {#symptoms-7}

以下是此類錯誤配置可能導致的症狀列表：

- 埠被 (R)STP 阻塞。
- 埠抖動。
- 網路不可訪問。

### 解決方案 {#solution-7}

最簡單的解決方案是直接在網橋上停用 (R)STP：

```ros
/interface/bridge
set bridge1 protocol-mode=none
```

不過仍建議重寫配置以使用網橋 VLAN 過濾：

```ros
/interface/bridge
add name=bridge1 vlan-filtering=yes
/interface/bridge/port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether2
/interface/bridge/vlan
add bridge=bridge1 tagged=ether1,ether2 vlan-ids=10
```

:::danger
啟用 `vlan-filtering` 後，您將過濾掉髮往 CPU 的流量。在啟用 VLAN 過濾之前，應確保已設定[管理埠](../index.md#management-access-configuration)。
:::

## 不使用硬體解除安裝的網橋 VLAN 過濾 {#bridge-vlan-filtering-without-hardware-offloading}

---

考慮以下場景：你發現了新的網橋 VLAN 過濾功能，並決定更改裝置上的配置。你有一個非常簡單的 trunk/access 埠設定，並且喜歡網橋 VLAN 過濾的概念。

### 配置 {#configuration-8}

```ros
/interface/bridge
add name=bridge1 vlan-filtering=yes
/interface/bridge/port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether2 pvid=20
add bridge=bridge1 interface=ether3 pvid=30
add bridge=bridge1 interface=ether4 pvid=40
/interface/bridge/vlan
add bridge=bridge1 tagged=ether1 untagged=ether2 vlan-ids=20
add bridge=bridge1 tagged=ether1 untagged=ether3 vlan-ids=30
add bridge=bridge1 tagged=ether1 untagged=ether4 vlan-ids=40
```

### 問題 {#problem-8}

例如，你在 CRS1xx/CRS2xx 系列裝置上使用此配置，並開始注意到 CPU 使用率非常高；執行效能測試以檢查網路吞吐量時，你注意到總吞吐量只是它本應輕鬆達到的線速效能的一小部分。問題的原因是並非所有裝置都在硬體級別支援網橋 VLAN 過濾。所有裝置都可以配置網橋 VLAN 過濾，但只有少數裝置能夠將流量解除安裝到交換晶片。如果在帶內建交換晶片的裝置上使用了不恰當的配置方法，那麼將使用 CPU 轉發流量。

### 症狀 {#symptoms-8}

以下是此類錯誤配置可能導致的症狀列表：

- 網橋埠缺少 "H" 標誌。
- 吞吐量低。
- CPU 使用率高。

### 解決方案 {#solution-8}

在使用網橋 VLAN 過濾之前，請檢查你的裝置是否在硬體級別支援它。相容性表可在[網橋硬體解除安裝](../index.md#bridge-hardware-offloading)部分找到。目前每種裝置型別都需要不同的配置方法。以下是裝置上應使用哪種配置以利用硬體解除安裝優勢的列表：

- [配備 Marvell Prestera 交換晶片的 MikroTik 裝置](../index.md#bridge-vlan-filtering)
- [CRS1xx/CRS2xx 系列裝置](./crs1xx-2xx-series-switches-examples.md#vlan)
- [其他帶交換晶片的裝置](../switch-chip-features.md#setup-examples)

## 具有多個交換晶片的裝置上的交換晶片 VLAN {#switch-chip-vlans-on-devices-with-several-switch-chips}

---

本節在交換晶片選單 `/interface/ethernet/switch` 中配置 VLAN，而不是使用網橋的 `vlan-filtering` 屬性。考慮以下場景：您有一臺具有兩個或更多交換晶片的裝置，並且您決定使用單個網橋，在硬體層面的交換晶片中設定 VLAN，以便在網路中達到線速效能。這對於 RB2011 和 RB3011 系列裝置非常相關。在此示例中，假設您希望有一個 Trunk 埠，而所有其他埠都是接入埠，例如，**ether10** 是我們的 Trunk 埠，**ether1-ether9** 是我們的接入埠。

### 配置 {#configuration-9}

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=ether3
add bridge=bridge1 interface=ether4
add bridge=bridge1 interface=ether5
add bridge=bridge1 interface=ether6
add bridge=bridge1 interface=ether7
add bridge=bridge1 interface=ether8
add bridge=bridge1 interface=ether9
add bridge=bridge1 interface=ether10
/interface/vlan
add interface=bridge1 name=VLAN10 vlan-id=10
/interface/ethernet/switch/port
set ether1,ether2,ether3,ether4,ether5,ether6,ether7,ether8,ether9 default-vlan-id=10 vlan-header=always-strip vlan-mode=secure
set ether10 vlan-header=add-if-missing vlan-mode=secure
set switch1-cpu,switch2-cpu vlan-mode=secure
/interface/ethernet/switch/vlan
add ports=ether1,ether2,ether3,ether4,ether5,switch1-cpu switch=switch1 vlan-id=10
add ports=ether6,ether7,ether8,ether9,ether10,switch2-cpu switch=switch2 vlan-id=10
```

### 問題 {#problem-9}

執行幾次測試後，你可能會注意到來自 **ether6-ether10** 的封包按預期轉發，但來自 **ether1-ether5** 的封包並不總是正確轉發（尤其是透過 trunk 埠時）。最明顯的問題是透過 **ether10** 的來自 **ether1-ether5** 的封包會被直接丟棄。這是因為這些埠位於不同的交換晶片上。這意味著無法在硬體級別進行 VLAN 過濾，因為交換晶片不知道另一個交換晶片上的 VLAN 表內容。在不同交換晶片上的埠之間轉發的封包也會由 CPU 處理，這意味著你無法達到線速效能。

### 症狀 {#symptoms-9}

以下是此類錯誤配置可能導致的症狀列表：

- 封包被丟棄。
- 吞吐量低。

### 解決方案 {#solution-9}

正確的解決方案是考慮這種硬體設計並相應地規劃網路拓撲。要解決此問題，必須建立兩個單獨的網橋，並在每個交換晶片上配置 VLAN 過濾。這限制了在交換晶片之間轉發封包的可能性，不過可以在兩個網橋之間配置路由（如果每個交換晶片上連線的裝置使用不同的網路子網）。

有一種方法可以配置裝置，使所有埠一起交換，同時仍能在硬體級別使用 VLAN 過濾，不過此解決方案有一些注意事項。思路是犧牲每個交換晶片上的一個乙太網埠，將其作為 trunk 埠在交換晶片之間轉發封包，這可以透過在兩個交換晶片之間插入乙太網線纜來實現；例如，讓我們在 **ether5** 和 **ether6** 之間插入乙太網線纜，然後假設這些埠是 trunk 埠來重新配置裝置：

```ros
/interface/bridge/port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=ether3
add bridge=bridge1 interface=ether4
add bridge=bridge1 interface=ether5
add bridge=bridge2 interface=ether6
add bridge=bridge2 interface=ether7
add bridge=bridge2 interface=ether8
add bridge=bridge2 interface=ether9
add bridge=bridge2 interface=ether10
/interface/ethernet/switch/port
set ether1,ether2,ether3,ether4,ether7,ether8,ether9 default-vlan-id=10 vlan-header=always-strip vlan-mode=secure
set ether5,ether6,ether10 vlan-header=add-if-missing vlan-mode=secure default-vlan-id=auto
set switch1-cpu,switch2-cpu vlan-mode=secure
/interface/ethernet/switch/vlan
add ports=ether1,ether2,ether3,ether4,ether5,switch1-cpu switch=switch1 vlan-id=10
add ports=ether6,ether7,ether8,ether9,ether10,switch2-cpu switch=switch2 vlan-id=10
```

:::warning
對於 100Mbps 交換晶片，請使用 `default-vlan-id=0` 而不是 `default-vlan-id=auto`
:::

## 使用簡化網橋 VLAN 表的 VLAN 過濾 {#vlan-filtering-with-simplified-bridge-vlan-table}

---

:::info
此問題自 **RouterOS v7.15** 起已解決。動態 VLAN 現在始終作為單獨條目建立，不再與靜態配置的條目合併。
:::

你需要建立一個網路設定，其中多個用戶端連線到單獨的 access 埠，並由不同的 VLAN 隔離。這些流量應被標記併發送到適當的 trunk 埠。Access 埠使用 pvid 屬性配置。由於 trunk 埠在兩個 VLAN 上都使用，你決定透過新增單個網橋 VLAN 表條目並用逗號分隔 VLAN 來簡化配置。當帶標籤的 trunk 埠用於大量 VLAN 甚至某些 VLAN 範圍（例如 vlan-id=100-200）時，這尤其有用。請參見下面的網路圖和配置。

![Switch Multiple Untagged](/img/3205c6726f791982.webp)

### 配置 {#configuration-10}

```ros
/interface/bridge
add name=bridge1 vlan-filtering=yes
/interface/bridge/port
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=ether3 pvid=10
add bridge=bridge1 interface=ether4 pvid=20
/interface/bridge/vlan
add bridge=bridge1 tagged=ether2 vlan-ids=10,20
```

### 問題 {#problem-10}

流量會正確地從 access 埠轉發並標記到 trunk 埠，但你可能會注意到一些廣播或組播封包實際上在兩個不帶標籤的 access 埠之間泛洪，儘管它們應該位於不同的 VLAN 上。此外，來自帶標籤埠的廣播和組播流量也會泛洪到兩個 access 埠。這可能引起一些安全問題，因為可以嗅探來自不同網路的流量。檢視網橋 VLAN 表時，你注意到為 VLAN 10 和 20 建立了單個條目，並且兩個不帶標籤埠都屬於同一個 VLAN 組。

```ros
[admin@SW1] /interface/bridge/vlan/print where tagged=ether2
Columns: BRIDGE, VLAN-IDS, CURRENT-TAGGED, CURRENT-UNTAGGED
# BRIDGE   VLAN-IDS  CURRENT-TAGGED  CURRENT-UNTAGGED
;;; port with pvid added to untagged group which might cause problems, consider adding a separate VLAN entry
0 bridge1        10  ether2          ether3          
                 20                  ether4     
```

### 症狀 {#symptoms-10}

- 流量在不同 VLAN 之間泛洪
- 紅色警告：`port with pvid added to untagged group which might cause problems, consider adding a separate VLAN entry`

### 解決方案 {#solution-10}

當 access 埠使用 pvid 屬性配置後，它們會被動態新增到相應的 VLAN 條目中。建立包含多個 VLAN 或 VLAN 範圍的靜態 VLAN 條目後，具有匹配 pvid 的不帶標籤 access 埠也會被包含在同一 VLAN 組或範圍中。使用單條配置行定義大量 VLAN 可能很有用，但在配置 access 埠時應格外小心。對於此示例，應建立單獨的 VLAN 條目：

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=ether2 untagged=ether3 vlan-ids=10
add bridge=bridge1 tagged=ether2 untagged=ether4 vlan-ids=20
```

## 主介面上的 MTU {#mtu-on-the-master-interface}

---

考慮以下場景：你建立了一個網橋，向其中添加了幾個介面，並在網橋介面之上建立了一個 VLAN 介面，但你需要增大 VLAN 介面上的 MTU 大小以接收更大的封包。

### 配置 {#configuration-11}

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether2
/interface/vlan
add interface=bridge1 name=VLAN99 vlan-id=99
```

### 問題 {#problem-11}

當你嘗試增大 VLAN 介面上的 MTU 大小時，會收到 RouterOS **Could not set MTU** 錯誤。當你嘗試設定大於 L2MTU 的 MTU 時，就會發生這種情況。在這種情況下，你需要增大所有從介面上的 L2MTU 大小，這將更新網橋介面上的 L2MTU 大小。完成此操作後，你將能夠在 VLAN 介面上設定更大的 MTU。同樣的原則適用於 bond 介面。只有當所有物理從介面都設定了適當的 L2MTU 時，你才能增大 VLAN、MPLS、VPLS、Bonding 和其他介面上的 MTU。

### 症狀 {#symptoms-11}

以下是此類錯誤配置可能導致的症狀列表：

- 無法更改 MTU。

### 解決方案 {#solution-11}

在更改主介面上的 MTU 之前，增大從介面上的 L2MTU。

```ros
/interface/ethernet
set ether1,ether2 l2mtu=9018
/interface/vlan
set VLAN99 mtu=9000
```

## MTU 不一致 {#mtu-inconsistency}

---

考慮以下場景：你的網路中有多臺裝置。大多數裝置在網路中用作交換器/網橋，並且有一些端點應該接收和處理流量。為了減少網路中的開銷，你決定增大 MTU 大小，因此在兩個端點上設定了更大的 MTU 大小，但你開始注意到一些封包被丟棄。

![MTU Issues](/img/e87e9a6138906e63.webp)

### 配置 {#configuration-12}

在這種情況下，兩個端點可以是任何型別的裝置，我們假設它們都是 Linux 伺服器，應該傳輸大量資料。在這種場景中，你可能在 **ServerA** 和 **ServerB** 上將介面 MTU 設定為 9000，而在你的 **Switch** 上，你可能設定了類似以下內容：

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add interface=ether1 bridge=bridge1
add interface=ether2 bridge=bridge1
```

### 問題 {#problem-12}

這是一個非常簡單的問題，但在較大的網路中可能很難檢測。例如，ping 可能正常工作，因為一般 ping 封包長度為 70 位元組（14 位元組乙太網頭、20 位元組 IPv4 頭、8 位元組 ICMP 頭、28 位元組 ICMP 負載），但資料傳輸可能無法正常工作。某些封包可能無法轉發的原因是，執行 RouterOS 的 MikroTik 裝置預設將 MTU 設定為 1500，將 L2MTU 設定為約 1580 位元組（取決於裝置），但乙太網介面會靜默丟棄任何不適合 L2MTU 大小的內容。請注意，L2MTU 引數與 x86 或 CHR 裝置無關。對於只應轉發封包的裝置，無需增大 MTU 大小；只需要增大 L2MTU 大小。RouterOS 不允許你將 MTU 大小增大到大於 L2MTU 大小。如果你需要在介面上接收封包，並且裝置需要處理該封包而不僅僅是轉發它，例如在路由的情況下，那麼需要增大 L2MTU 和 MTU 大小，但如果你只使用 IP 流量（支援封包分片）並且不介意封包被分片，則可以將介面上的 MTU 大小保留為預設值。你可以使用 ping 工具確保所有裝置都能轉發巨型幀：

```ros
/ping 192.168.88.1 size=9000 do-not-fragment
```

請記住，在你傳送 ping 封包的源裝置和目標裝置上，L2MTU 和 MTU 大小需要大於或等於 ping 封包大小，因為 ping (ICMP) 是透過 Layer3 從介面傳送出去的 IP 流量。

### 症狀 {#symptoms-12}

以下是此類錯誤配置可能導致的症狀列表：

- 網頁無法載入，但 ping 正常工作。
- 隧道丟棄流量。
- 特定協定異常。
- 大量丟包。

### 解決方案 {#solution-12}

增大 **Switch** 上的 L2MTU 大小：

```ros
/interface/ethernet
set ether1,ether2 l2mtu=9000
```

如果你的流量被封裝（VLAN、VPN、MPLS、VPLS 或其他），那麼你可能需要考慮設定更大的 L2MTU 大小。在此場景中，由於上述原因，不需要增大 MTU 大小。

:::warning
完整幀 MTU 與 L2MTU 不同。L2MTU 大小不包括乙太網頭（14 位元組）和 CRC 校驗和 (FCS) 欄位。FCS 欄位由乙太網驅動剝離，RouterOS 永遠不會向任何封包顯示額外的 4 位元組。例如，如果將 MTU 和 L2MTU 設定為 9000，則完整幀 MTU 長度為 9014 位元組。使用 "`/tool/sniffer/quick"` 命令嗅探封包時也可以觀察到這一點。
:::

## 網橋與保留 MAC 地址 {#bridge-and-reserved-mac-addresses}

---

考慮以下場景：你希望將兩個網段透明地橋接在一起，無論是 EoIP 等隧道介面、無線介面、乙太網介面，還是任何其他可以新增到網橋的介面型別。這種設定允許你將兩臺裝置無縫連線起來，就像它們之間只有一根物理線纜一樣。這有時被稱為從 **DeviceA** 到 **DeviceB** 的**透明網橋**。

### 配置 {#configuration-13}

對於 **DeviceA** 和 **DeviceB** 兩臺裝置，應使用非常相似的配置。

```ros
/interface/bridge
add name=bridge1 protocol-mode=rstp
/interface/bridge/port
add interface=ether1 bridge=bridge1
add interface=eoip1 bridge=bridge1
```

### 問題 {#problem-13}

兩臺裝置能夠相互通訊，但某些協定無法正常工作。原因是，一旦使用任何 STP 變體（STP、RSTP、MSTP），你就使網橋符合 IEEE 802.1D 和 IEEE 802.1Q。這些標準建議發往 **01:80:C2:00:00:0X** 的封包**不應**被轉發。在網橋中只添加了 2 個埠的情況下，不應使用 (R/M)STP，因為 2 個介面不可能產生環路；如果確實出現環路，原因在別處，應在不同的網橋上修復。由於透明網橋設定中不需要 (R/M)STP，因此可以將其停用。一旦停用 (R/M)STP，RouterOS 網橋就不再符合 IEEE 802.1D 和 IEEE 802.1Q，因此將轉發發往 **01:80:C2:00:00:0X** 的封包。

### 症狀 {#symptoms-13}

以下是此類錯誤配置可能導致的症狀列表：

- LLDP 鄰居不顯示。
- 802.1x 認證 (dot1x) 不工作。
- LACP 介面不轉發流量。

### 解決方案 {#solution-13}

可以部分停用對 IEEE 802.1D 和 IEEE 802.1Q 的符合性；這可以透過更改網橋協定模式來完成。

```ros
/interface/bridge
set bridge1 protocol-mode=none
```

:::danger
IEEE 802.1x 標準旨在直接在交換器和用戶端之間使用。如果可以在交換器和用戶端之間連線裝置，那麼這會帶來安全威脅。因此，不建議停用對 IEEE 802.1D 和 IEEE 802.1Q 的符合性，而應設計適當的網路拓撲。
:::

## 無線鏈路之間的繫結 {#bonding-between-wireless-links}

---

考慮以下場景：你設定了多條無線鏈路，為了實現最大吞吐量並同時實現冗餘，你決定將乙太網介面放入一個 bond 中，並根據轉發的流量選擇了某種繫結模式。此場景適用於在彼此不直接連線的鏈路之間建立繫結介面的任何情況。

![LACP over WLAN](/img/2de2fccfd3fb0dad.webp)

### 配置 {#configuration-14}

以下配置與 **R1** 和 **R2** 相關：

```ros
/interface/bonding
add mode=802.3ad name=bond1 slaves=ether1,ether2 transmit-hash-policy=layer-2-and-3
/ip/address
add address=192.168.1.X/24 interface=bond1
```

以下配置與 **AP1**、**AP2**、**ST1,** 和 **ST2** 相關，其中 **X** 對應每臺裝置的 IP 地址。

```ros
/interface/bridge
add name=bridge1 protocol-mode=none
/interface/bridge/port
add interface=ether1 bridge=bridge1
add interface=wlan1 bridge=bridge1
/ip/address
add address=192.168.1.X/24 interface=bridge1
```

### 問題 {#problem-14}

雖然流量在 **R1** 和 **R2** 之間正常轉發，負載均衡、鏈路故障切換也正常工作，但 **R1** 和 **R2** 之間的裝置並不總是可訪問，或者其中一些完全不可訪問（大多數情況下 **AP2** 和 **ST2** 不可訪問）。檢查問題後，你可能會注意到封包並不總是透過所需的繫結從介面轉發，結果你嘗試訪問的裝置永遠收不到這些封包。這是網路設計和繫結協定的限制。一旦封包需要透過繫結介面傳送出去（在這種情況下，你可能嘗試向 **AP2** 或 **ST2** 傳送 ICMP 封包），繫結介面將根據選定的繫結模式和 transmit-hash-policy 建立雜湊，並選擇一個介面將封包傳送出去，而不考慮目標是否只能透過某個介面到達。有些裝置會可訪問，因為生成的雜湊與裝置所在介面匹配，但也可能不會選擇所需介面，從而導致裝置不可訪問。只有廣播繫結模式沒有這種協定限制，但這種繫結模式的用例非常有限。

### 症狀 {#symptoms-14}

以下是此類錯誤配置可能導致的症狀列表：

- 連線性受限
- 鏈路不穩定（使用 balance-rr 時）

### 解決方案 {#solution-14}

繫結介面不應使用間接鏈路連線，但仍然可以建立變通方法。此變通方法背後的思路是找到一種方法繞過透過繫結介面傳送的封包。有多種方法可以強制封包不透過繫結介面傳送，但本質上解決方案是在物理介面之上建立新介面，並將這些新建立的介面而不是物理介面新增到 bond 中。實現這一點的一種方法是在每個物理介面上建立 EoIP 隧道，但這會產生巨大開銷並降低整體吞吐量。你應該改為在每個物理介面之上建立 VLAN 介面。這產生的開銷小得多，並且不會明顯影響整體效能。以下是 **R1** 和 **R2** 應如何重新配置的示例：

```ros
/interface/vlan
add interface=ether1 name=VLAN_ether1 vlan-id=999
add interface=ether2 name=VLAN_ether2 vlan-id=999
/interface/bonding
add mode=balance-xor name=bond1 slaves=VLAN_ether1,VLAN_ether2 transmit-hash-policy=layer-2-and-3
/ip/address
add address=192.168.1.X/24 interface=bond1
add address=192.168.11.X/24 interface=ether1
add address=192.168.22.X/24 interface=ether2
```

**AP1** 和 **ST1** 只需要將 IP 地址更新為正確的子網：

```ros
/ip/address
add address=192.168.11.X/24 interface=bridge1
```

必須對 **AP2** 和 **ST2** 應用相同的更改（確保使用正確的子網）：

```ros
/ip/address
add address=192.168.22.X/24 interface=bridge1
```

使用這種方法，你產生的開銷最少，並且所需的配置更改也最少。

:::warning
LACP (802.3ad) 不適用於裝置的繫結從介面不直接連線的設定；在這種情況下，如果兩臺路由器之間存在無線鏈路，不建議使用 LACP。LACP 要求兩個繫結從介面具有相同的鏈路速度，無線鏈路可以隨時改變速率，這會降低整體效能和穩定性。應改用其他繫結模式。
:::

## 頻寬測試 {#bandwidth-testing}

---

考慮以下場景：你在兩臺裝置之間設定了一條鏈路。這可以是任何鏈路，乙太網線纜、無線鏈路、隧道或任何其他連線。你決定測試鏈路的頻寬，但為了方便，你決定使用執行該鏈路的同一批裝置開始測試鏈路。

![Bad Bandwidth Setup](/img/590e348e86dd552a.webp)

### 問題 {#problem-15}

一旦開始 [頻寬測試](../../diagnostics-monitoring-and-troubleshooting/bandwidth-test.md) 或 [流量生成器](../../diagnostics-monitoring-and-troubleshooting/traffic-generator.md)，你就會注意到吞吐量遠小於預期。對於非常強大的路由器，它們應該能夠轉發數吉位元每秒 (Gbps)，但你注意到只轉發了幾個吉位元每秒。發生這種情況的原因是你使用的測試方法。你不應使用同一臺路由器生成流量時測試該路由器的吞吐量，因為這會增加 CPU 的額外負載，從而降低總吞吐量。

### 症狀 {#symptoms-15}

以下是此類錯誤配置可能導致的症狀列表：

- 吞吐量低。
- CPU 使用率高。

### 解決方案 {#solution-15}

使用適當的測試方法。不要使用 Bandwidth-test 測試大容量鏈路，也不要在你正在測試的同一臺裝置上執行任何生成流量的工具。正確設計網路，以便可以在兩端連線生成和接收流量的裝置。如果你熟悉 **Iperf**，那麼這個概念應該很清楚。請記住，在現實世界中，路由器或交換器不會生成大量流量（至少不應該，否則可能表明存在安全問題），伺服器/用戶端生成流量，而路由器/交換器轉發流量（並在適當情況下對流量進行一些處理）。

![Good Bandwidth Setup](/img/94426a9891add21a.webp)

## 網橋 split-horizon 的使用 {#bridge-split-horizon-usage}

---

考慮以下場景：你有一個網橋，並且需要將某些網橋埠彼此隔離。在某些交換晶片上可以選擇使用內建交換晶片隔離某些埠，你可以使用網橋防火牆規則防止某些埠向其他埠傳送任何流量，也可以在 PVLAN 型別的設定中使用埠隔離來隔離埠，但還有一種基於軟體的解決方案使用網橋 split-horizon（這會停用所有交換晶片上的硬體解除安裝）。

### 配置 {#configuration-15}

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 horizon=1 hw=no interface=ether1
add bridge=bridge1 horizon=2 hw=no interface=ether2
add bridge=bridge1 horizon=3 hw=no interface=ether3
add bridge=bridge1 horizon=4 hw=no interface=ether4
```

### 問題 {#problem-16}

在每個埠上設定網橋 split-horizon 後，你開始注意到埠仍然能夠相互發送資料。原因是錯誤使用了網橋 split-horizon。網橋埠只是無法與同一 horizon 中的埠通訊，例如，horizon=1 無法與 horizon=1 通訊，但可以與 horizon=2、horizon=3 等通訊。

### 症狀 {#symptoms-16}

以下是此類錯誤配置可能導致的症狀列表：

- 流量在不同的網橋 split-horizon 之間轉發。

### 解決方案 {#solution-16}

將網橋 split-horizon 設定為適當的值。如果你希望將埠彼此隔離（PPPoE 設定的常見場景），並且每個埠只能與網橋本身通訊，那麼所有埠必須處於同一個網橋 split-horizon 中。

```ros
/interface/bridge/port
set [f] horizon=1
```

:::warning
將所有網橋埠設定到同一個網橋 split-horizon 中會導致流量只能到達網橋介面本身，然後封包只能被路由。當你希望其他裝置過濾掉某些流量時，這很有用。使用網橋過濾規則也可以實現類似行為。
:::

## 不受支援的 SFP 模組 {#unsupported-sfp-modules}

---

考慮以下場景：你決定使用光纖線纜，透過 SFP 或 SFP+ 光模組將裝置連線在一起，但為了方便，你決定使用手頭可用的 SFP 光模組。

### 問題 {#problem-17}

一旦你配置裝置在使用這些 SFP 光模組的埠上建立連線，你可能會注意到鏈路要麼正常工作，要麼出現隨機連線問題。有許多廠商製造 SFP 光模組，但並非所有廠商都嚴格遵循 SFP MSA、SFF 和 IEEE 802.3 標準，這可能導致不可預測的相容性問題；在 MikroTik 裝置中使用不知名或不受支援的 SFP 光模組時，這是一個非常常見的問題。

### 症狀 {#symptoms-17}

以下是此類錯誤配置可能導致的症狀列表：

- SFP 介面無法建立鏈路。
- 隨機丟包。
- 鏈路不穩定（抖動）。
- 重啟後 SFP 模組不工作。
- 斷電重啟後 SFP 模組不工作。
- SFP 模組僅在一側工作。

### 解決方案 {#solution-17}

你只應使用受支援的 SFP 模組。如果你打算使用 MikroTik 製造的 SFP 模組，請始終檢查 [SFP 相容性表](../../wired-connections/mikrotik-wired-interface-compatibility.md)。也有其他 SFP 模組可與 MikroTik 裝置配合使用。請檢查[受支援的外設表](../../hardware/peripherals.md#sfp-modules)，以查詢已確認可與 MikroTik 裝置配合使用的其他 SFP 模組。某些不受支援的模組在某些速度和自動協商下可能無法正常工作。你可以嘗試停用自動協商並手動設定鏈路速度。
