---
title: "Layer2 設定錯誤"
description: "本頁說明 MikroTik RouterOS 中的 Layer2 設定錯誤，重點在於硬體卸載橋接設定不當與埠隔離等問題。文中說明低吞吐量、高 CPU 使用率，以及硬體卸載旗標不正確等徵兆，並提供缺乏埠隔離支援的設備之解決方案。"
tags:
  - 'bridging'
  - 'hardware-offloading'
  - 'mac-learning'
source: https://manual.mikrotik.com/docs/7.24/bridging-and-switching/user-guides/layer2-misconfiguration
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

---

有些設定在設計上已知存在重大缺陷，應盡可能避免。設定錯誤的 Layer2 有時會造成難以偵測的網路錯誤、隨機的效能下降、網路中特定區段無法連線、特定網路服務異常，或整個網路故障。本頁將列出一些常見及較不常見、會在網路中造成問題的設定。

## 單一交換器晶片上的 Bridge {#bridges-on-a-single-switch-chip}

---

請考量以下情境。你有一台內建交換器晶片的設備，需要將特定埠彼此隔離。為此，你建立了多個 bridge，並在它們之上啟用硬體卸載。由於每個 bridge 位於不同的 Layer2 網域，Layer2 訊框不會在這些 bridge 之間轉送。因此，每個 bridge 中的埠會與其他 bridge 上的埠隔離。

### 設定 {#configuration}

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

在簡單的效能測試後，你可能會發現其中一個 bridge 能以線速轉送流量，而第二個、第三個等 bridge 無法轉送與第一個 bridge 相同量的資料。另一個徵兆可能是需要路由的封包存在極高的延遲。快速檢查後，你可能會發現 CPU 始終處於滿載狀態。這是因為硬體卸載並非在所有 bridge 上都可用，而只在其中一個 bridge 上可用。檢查硬體卸載狀態時，你會發現只有一個 bridge 已啟用該功能：

```ros
[admin@MikroTik] > /interface/bridge/port/print
Flags: X - disabled, I - inactive, D - dynamic, H - hw-offload 
 #     INTERFACE                                 BRIDGE                                 HW
 0   H ether1                                    bridge1                                yes
 1   H ether2                                    bridge1                                yes
 2     ether3                                    bridge2                                yes
 3     ether4                                    bridge2                                yes
```

只有一個 bridge 具有硬體卸載旗標的原因，是該設備不支援埠隔離。如果不支援埠隔離，則只有一個 bridge 能將流量卸載至交換器晶片。

### 徵兆 {#symptoms}

以下是可能由這類設定錯誤造成的症狀：

- 橋接埠缺少「H」旗標。
- 吞吐量偏低。
- CPU 使用率偏高。

### 解決方案 {#solution}

並非所有設備都支援埠隔離。目前只有 CRS1xx/CRS2xx 系列設備支援，且同時只支援 7 個已隔離並由硬體卸載的橋接。其他設備必須使用 CPU 在其他橋接上轉送封包。這通常是硬體限制，可能需要改用不同的設備。Bridge split-horizon 參數是一項軟體功能，會停用硬體卸載；而使用 bridge filter 規則時，需要啟用將所有封包轉送至 CPU，這也需要停用硬體卸載。你可以使用 `hw=yes` 旗標控制哪個橋接要由硬體卸載，並對其他橋接設定 `hw=no`，例如：

```ros
/interface/bridge/port/set [find where bridge=bridge1] hw=no
/interface/bridge/port/set [find where bridge=bridge2] hw=yes
```

有時可以重新調整網路拓撲以使用 VLAN，這是隔離 Layer2 網路的正確做法。

## 啟用硬體卸載與 MAC 學習時的封包流程 {#packet-flow-with-hardware-offloading-and-mac-learning}

---

請考量以下情境：你已設定橋接並啟用硬體卸載，以最大化設備的吞吐量；因此，你的設備會以交換器模式運作，但你想使用 [Sniffer](/docs/diagnostics-monitoring-and-troubleshooting/packet-sniffer) 或 [Torch](/docs/diagnostics-monitoring-and-troubleshooting/torch) 工具進行除錯，或者你可能想實作封包日誌記錄。

### 設定 {#configuration-1}

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 hw=yes interface=ether1 learn=yes
add bridge=bridge1 hw=yes interface=ether2 learn=yes
```

### 問題 {#problem-1}

執行 [Sniffer](/docs/diagnostics-monitoring-and-troubleshooting/packet-sniffer) 或 [Torch](/docs/diagnostics-monitoring-and-troubleshooting/torch) 工具擷取封包時，您可能會發現幾乎看不到任何封包，只能看到一些單播封包，但大多數擷取到的是廣播／群播封包，而介面回報通過特定介面的流量，遠大於實際擷取到的流量。如果您將兩個或更多 Ethernet 介面加入 bridge，並啟用 [Hardware Offloading](/docs/bridging-and-switching#bridge-hardware-offloading)，則交換器晶片會用於在連接埠之間轉送封包。若要了解為何只擷取到部分封包，必須先檢查交換器晶片與 CPU 的互連方式。在此範例中，可以使用一般 5-Port Ethernet 路由器的區塊圖：

![Switch Chip Block Diagram](/img/ec5a5a402792668a.webp)

### Symptoms {#symptoms-1}

以下是可能由這類設定錯誤造成的症狀：

- Sniffer 或 Torch 工具看不到封包。
- Filter 規則沒有作用。

### Solution {#solution-1}

對此設備而言，每個 Ethernet 連接埠都連接到交換器晶片，而交換器晶片則透過 CPU 連接埠（有時稱為 **switch-cpu** 連接埠）連接到 CPU。若要讓封包在 Sniffer 或 Torch 工具中可見，封包必須從 Ethernet 連接埠傳送到 CPU 連接埠，這表示封包的目的地必須是 CPU 連接埠（封包的目的 MAC 位址與 bridge 的 MAC 位址相符），或封包的 MAC 位址尚未被學習（封包會泛洪到所有連接埠），此行為是由於 **MAC learning** 所致。

交換器晶片會保存一份 MAC 位址與連接埠的清單，稱為 **Host table**。每當需要轉送封包時，交換器晶片會根據封包的目的 MAC 位址檢查 hosts table，以找出應該用來轉送封包的連接埠。如果交換器晶片找不到目的 MAC 位址，則封包會泛洪到所有連接埠（包括 CPU 連接埠）。在封包原本應從 ether1 轉送到 ether2 的情況下，如果 ether2 後方設備的 MAC 位址已在 host table 中，則封包永遠不會傳送到 CPU，因此 Sniffer 或 Torch 工具將看不到該封包。

目的 MAC 位址已學習的封包不會傳送到 CPU，因為這些封包不會泛洪到所有埠。若確實需要將特定封包傳送到 CPU 以供封包分析器或防火牆使用，可以使用 ACL 規則將封包複製或重新導向到 CPU。以下範例說明如何傳送目的地為 **4C:5E:0C:4D:12:4B** 的封包副本：

```ros
/interface/ethernet/switch/rule
add copy-to-cpu=yes dst-mac-address=4C:5E:0C:4D:12:4B/FF:FF:FF:FF:FF:FF ports=ether1 switch=switch1
```

:::warning
若封包傳送到 CPU，則該封包必須由 CPU 處理；這會增加 CPU 負載。
:::

## LAG 介面與負載平衡 {#lag-interfaces-and-load-balancing}

---

請考量以下情境：你已建立 LAG 介面，以增加 2 個網路節點之間的總頻寬；這些節點通常是交換器。為了測試並確認 LAG 介面是否正常運作，你連接了兩部伺服器來傳輸資料，最常見的做法是使用知名的網路效能量測工具 [Iperf](https://en.wikipedia.org/wiki/Iperf) 測試這類設定。例如，你可能由兩個 Gigabit Ethernet 埠建立 LAG 介面，這會提供一個虛擬介面，可將流量負載平衡到兩個介面，理論上達到 2Gbps 輸送量，而伺服器則使用 10Gbps 介面連接，例如 SFP+。

![LACP Setup](/img/fa65c1f36095531a.webp)

### 設定 {#configuration-2}

以下設定適用於 **SW1** 與 **SW2**：

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

在初步測試後，你會立即發現網路輸送量從未超過 1Gbps 限制，即使伺服器與網路節點（此例中為交換器）的 CPU 負載都很低，輸送量仍僅限於 1Gbps。原因是 LACP（802.ad）會使用 transmit hash policy 判斷流量是否可分散到多個 LAG 成員；在此例中，LAG 介面並不是建立一個 2Gbps 介面，而是一個在可能的情況下可將流量分散到多個 slave 介面的介面。每個封包都會產生一個 transmit hash，用來決定封包要透過哪個 LAG 成員傳送；這是為了避免封包順序錯亂。你可以選擇 transmit hash policy，通常可在 Layer2（MAC）、Layer3（IP）與 Layer4（Port）之間選擇；在 RouterOS 中，可使用 `transmit-hash-policy` 參數選擇。在此例中，由於你將封包傳送到相同的目的 MAC 位址、相同的 IP 位址，且 Iperf 也使用相同的埠，因此所有封包都會產生相同的 transmit hash，無法在 LAG 成員之間進行負載平衡。請注意，即使目的地不同，封包也不一定會分散到 LAG 成員，這是因為標準化的 transmit hash policy 可能為不同目的地產生相同的 transmit hash。例如，若使用 `layer2-and-3` transmit hash policy 且目的 MAC 位址相同，192.168.0.1/192.168.0.2 會被分散，但 192.168.0.2/192.168.0.4 **不會**被分散。

### 症狀 {#symptoms-2}

以下是可能由這類設定錯誤造成的症狀：

- 流量只通過一個 LAG 成員。

### 解決方案 {#solution-2}

選擇適當的 transmit hash policy，並正確測試網路吞吐量。測試這類設定最簡單的方式是使用多個目的地，例如，不要只將資料傳送到一部伺服器，而是將資料傳送到多部伺服器。這會為每個封包產生不同的 transmit hash，並讓 LAG 成員之間得以進行負載平衡。在某些設定中，您可能想要變更 bonding 介面模式，以提高總吞吐量。對於 UDP 流量，`balance-rr` 模式可能已足夠，但可能會對 TCP 流量造成問題。您可以在[這裡](/docs/high-availability-solutions/bonding#bonding-modes)閱讀更多關於為您的設定選擇正確模式的資訊。

## slave 介面上的 VLAN 介面 {#vlan-interface-on-a-slave-interface}

---

請考量以下情境：您已建立 bridge，並且希望 DHCP Server 只將 IP 位址發給特定 tagged VLAN 流量，因此您已建立 VLAN 介面、指定 VLAN ID，並在其上建立 DHCP Server，但因為某些原因，它無法正常運作。

### 設定 {#configuration-3}

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

當你將介面加入橋接器時，橋接器會成為主介面，而所有橋接埠都會成為從屬埠。這表示在橋接埠上接收的所有流量都會由橋接介面擷取，且所有流量都會使用橋接介面而非實體介面轉送至 CPU。因此，在從屬介面上建立的 VLAN 介面永遠不會擷取到任何流量，因為封包在進行任何處理之前，就會立即被轉送至主介面。常見的副作用是部分 DHCP 用戶端可取得 IP 位址，而部分則無法取得。

### 徵狀 {#symptoms-3}

以下是可能由這類設定錯誤造成的徵狀清單：

- DHCP Client/Server 無法正常運作。
- 設備無法連線。
- 橋接器後方的設備無法透過標記流量連線。

### 解決方案 {#solution-3}

變更 VLAN 介面用來監聽流量的介面，並將其改為主介面：

```ros
/interface/vlan/set VLAN99 interface=bridge1
```

## 橋接器中的橋接器上的 VLAN {#vlan-on-a-bridge-in-a-bridge}

---

請考量以下情境：你有一組介面（不必是實體介面），而且希望它們全部位於同一個 Layer2 區段。解決方式是將它們加入單一 bridge，但你要求來自某一個埠的流量要將所有流量標記為特定 VLAN。這可以透過在 bridge 介面上建立 VLAN 介面，並建立另一個 bridge（其中包含這個新建立的 VLAN 介面，以及一個應該對所有接收到的流量加上 VLAN 標籤的介面）來完成。網路示意圖如下：

![VLAN on Bridge in Bridge](/img/fdbfbd53e29c7dbf.webp)

### 設定 {#configuration-4}

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

為了更了解潛在問題，讓我們先查看 bridge host table。

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

**ether1** 與 **ether2** 上的設備需要傳送 VLAN-ID 99 的標記封包，才能抵達 **ether3** 上的主機（其他封包不會被傳往 VLAN 介面，也不會進一步與 ether3 進行橋接）。我們可以在 host table 中看到 **bridge2** 已學習到這些主機。從 **ether3** 傳往 **ether1** 的封包會正確地以標記形式送出，且流量不會在 **bridge1** 中氾濫。但由於 MAC 學習只能在 bridge 埠之間進行，無法在建立於 bridge 介面之上的介面上進行，因此從 **ether2** 傳往 **ether3** 的封包會在 **bridge1** 中氾濫。

此外，如果 **ether3** 後方的設備使用 (R)STP，則 **ether1** 與 **ether2** 會送出標記的 BPDU，這違反 IEEE 802.1W 標準。由於 MAC 學習功能失效且 (R)STP 失效，必須避免這種設定與組態。眾所周知，在某些設定中，這類組態可能會導致你無法透過 MAC telnet 連線到設備。

### 徵狀 {#symptoms-4}

以下是可能由這類錯誤設定造成的徵狀清單：

- 埠遭到 RSTP 封鎖。
- 網路中有迴圈。
- 埠持續抖動。
- 流量被泛洪到所有埠。
- MAC telnet 無法連線。
- 設備無法存取。

### 解決方案 {#solution-4}

使用 bridge VLAN filtering。標記流量的正確方式，是在流量進入 bridge 時指派 VLAN ID。只要為 bridge 埠指定 **PVID** 值，並指定哪些埠是 **tagged**（trunk）埠、哪些埠是 **untagged**（access）埠，即可輕鬆達成此行為。以下是此類設定應如何配置的範例：

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
啟用 `vlan-filtering` 時，您會一併過濾掉送往 CPU 的流量。在啟用 VLAN filtering 之前，請確認您已設定 [Management port](/docs/bridging-and-switching#management-access-configuration)。
:::

## 具有實體介面的 bridge 中的 VLAN {#vlan-in-a-bridge-with-a-physical-interface}

---

與 [bridge 中的 bridge 上的 VLAN](/docs/bridging-and-switching/user-guides/layer2-misconfiguration#vlan-on-a-bridge-in-a-bridge) 非常相似。最常見的使用情境，是您想要將實體介面與 VLAN 進行 bridge（簡化的 trunk/access 埠設定）。在此類設定中，您可能希望在一側送出 tagged 流量，而在另一側送出 untagged 流量。若要達成此目的，請在 trunk 埠（tagged 側）建立 VLAN 介面，然後建立 bridge，並將 VLAN 介面與實體介面（untagged 側）都加入為 bridge 埠。

### 設定 {#configuration-5}

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

此設定與組態在大多數情況下都能運作，但使用 (R/M)STP 時會違反 IEEE 802.1W 標準。如果這是 Layer2 網域中唯一的設備，則不應造成問題，但當有其他廠商的交換器時，就可能發生問題。原因是 bridge 介面上的 RSTP 預設啟用，允許從每個 bridge 埠傳送 Bridge Protocol Data Unit (BPDU)。雖然 **ether2** 正確傳送未標記的 BPDU，但 **VLAN99** 介面身為 bridge 埠，會透過 ether1 傳送已標記的 BPDU。並非所有交換器都能理解已標記的 BPDU。在更複雜的網路中，若特定 VLAN（或 VLAN 群組）存在多種網路拓撲，採用此組態時應採取預防措施。這與混合廠商設備環境中的 MSTP 和 PVSTP(+) 有關。在環狀拓撲中，若特定 VLAN 有多種網路拓撲，交換器上會有一個埠被封鎖，但在 MSTP 和 PVSTP(+) 中，可以為特定 VLAN 開啟路徑；在這種情況下，不支援 PVSTP(+) 的設備可能會移除 BPDU 的標記並轉送 BPDU，結果交換器會收到自己的封包，觸發迴路偵測並封鎖埠。其他協定也可能發生這種情況，但最常見的是 (R)STP。如果交換器使用 BPDU guard 功能，這類組態可能觸發該功能，並導致埠被 STP 封鎖。據回報，使用 6.41 或更新版本時，這類組態可能隨著時間推移，使流量無法透過某些 bridge 埠轉送。這類組態不只會破壞 (R/M)STP，也可能造成迴路警告。這可能是由 MNDP 封包或任何直接從介面送出的封包所造成。

### 症狀 {#symptoms-5}

以下是可能由這類錯誤組態造成的常見症狀清單：

- 埠被 RSTP 封鎖。
- 網路中出現迴路。
- 埠狀態反覆變動。
- 流量隨著時間推移停止轉送。
- BPDU 被其他啟用 RSTP 的設備忽略。

### 解決方案 {#solution-5}

為避免相容性問題，應使用 bridge VLAN filtering。以下範例說明如何透過 bridge VLAN filtering 組態達到相同的流量標記效果：

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
啟用 `vlan-filtering` 時，將會過濾送往 CPU 的流量。啟用 VLAN filtering 前，請確認已設定 [Management port](/docs/bridging-and-switching#management-access-configuration)。
:::

## 實體介面上的 Bridged VLAN {#bridged-vlan-on-physical-interfaces}

---

與 [VLAN on a bridge in a bridge](/docs/bridging-and-switching/user-guides/layer2-misconfiguration#vlan-on-a-bridge-in-a-bridge) 非常相似的情況：請考慮以下情境。你的網路中有幾台交換器，並且使用 VLAN 隔離特定 Layer2 網域，將這些交換器連接到路由器，由路由器指派位址並將流量路由到外部。為了提供備援，你將所有交換器直接連接到路由器並啟用 RSTP，但為了能夠設定 DHCP Server，你決定在每個連接到交換器的實體介面上為每個 VLAN 建立 VLAN 介面，並將這些 VLAN 介面加入 bridge。網路架構圖如下：

![Bridged VLANs](/img/3cff20b2aa3e5fb4.webp)

### 設定 {#configuration-6}

此情況只與路由器部分有關，交換器設定並不重要，只要連接埠處於交換模式即可。路由器設定如下：

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

你可能會發現網路出現一些奇怪的延遲，甚至網路沒有回應。你可能會發現偵測到迴圈（收到帶有自身 MAC 位址的封包），並且有些流量憑空產生。問題發生的原因是，來自 **Router** 上所建立任一 VLAN 介面的廣播封包會從實體介面送出，封包會透過實體介面轉送、通過交換器，再從另一個實體介面接收回來；在此例中，從 **ether1\_v10** 送出的廣播封包會在 **ether2** 上收到，封包會被 **ether2\_v10** 擷取，而 **ether2\_v10** 與 **ether1\_v10** 位於同一個 bridge，因此封包會再次透過相同路徑轉送（迴圈）。(R)STP 不一定總是能偵測到這種迴圈，因為 (R)STP 並不知道任何 VLAN 的存在。未標記流量不會形成迴圈，但標記流量會。在此情境中，很容易發現迴圈，但在更複雜的設定中，並不一定容易偵測出網路設計缺陷。有時候，如果你的網路沒有使用廣播流量，這種網路設計缺陷可能會長時間未被發現；通常，[Neighbor Discovery Protocol](/docs/system-information-and-utilities/neighbor-discovery) 會從 VLAN 介面廣播封包，而在這類設定中通常會觸發迴圈偵測。有時候，擷取觸發迴圈偵測的封包很有用，這可以透過使用 sniffer 並分析封包擷取檔案來完成：

```ros
/tool/sniffer
set filter-mac-address=4C:5E:0C:4D:12:44/FF:FF:FF:FF:FF:FF \
filter-interface=ether1 filter-direction=rx file-name=loop_packet.pcap
```

或者使用更方便的方式，透過日誌：

```ros
/interface/bridge/filter
add action=log chain=forward src-mac-address=4C:5E:0C:4D:12:44/FF:FF:FF:FF:FF:FF
add action=log chain=input src-mac-address=4C:5E:0C:4D:12:44/FF:FF:FF:FF:FF:FF
```

### 徵狀 {#symptoms-6}

以下是可能由這類設定錯誤造成的可能症狀清單：

- 埠遭 (R)STP 封鎖。
- 網路中發生迴圈。
- 吞吐量偏低。
- 埠震盪。
- 無法存取網路。

### 解決方案 {#solution-6}

解決方法是使用 bridge VLAN filtering，讓所有 bridge 都與 IEEE 802.1W 及 IEEE 802.1Q 相容。

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
啟用 `vlan-filtering` 時，將會過濾掉目的地為 CPU 的流量。啟用 VLAN filtering 之前，請確認已設定 [Management port](/docs/bridging-and-switching#management-access-configuration)。
:::

## 橋接 VLAN {#bridged-vlan}

---

這是 [Bridged VLAN on physical interfaces](/docs/bridging-and-switching/user-guides/layer2-misconfiguration#bridged-vlan-on-physical-interfaces) 的簡化情境，但在此案例中，您只是想要將在不同實體介面上建立的兩個或多個 VLAN 橋接在一起。這是一種非常常見的設定方式，值得單獨撰寫一篇文章，因為錯誤設定這類組態已造成多次網路故障。這類設定也用於 VLAN 轉換。

### 設定 {#configuration-7}

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

您可能會發現網路中某些部分無法存取，或某些連線持續抖動。這是因為 (R)STP。這類設定會強制設備送出 tagged BPDU，而其他設備（包括 RouterOS）可能不支援。由於設備收到格式錯誤的封包（執行 (R)STP 時，網路中不應存在 tagged BPDU，因為這違反 IEEE 802.1W 與 IEEE 802.1Q），設備將無法正確解讀封包，並可能出現非預期行為。

### 症狀 {#symptoms-7}

以下是可能由這類錯誤設定造成的症狀清單：

- 埠遭 (R)STP 封鎖。
- 埠抖動。
- 網路無法存取。

### 解決方案 {#solution-7}

最簡單的解決方案是直接在 bridge 上停用 (R)STP：

```ros
/interface/bridge
set bridge1 protocol-mode=none
```

不過仍建議重新撰寫設定，以使用 bridge VLAN filtering：

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
啟用 `vlan-filtering` 時，您將會過濾掉目的地為 CPU 的流量。在啟用 VLAN filtering 之前，請確認您已設定 [Management port](/docs/bridging-and-switching#management-access-configuration)。
:::

## 沒有硬體卸載的 Bridge VLAN filtering {#bridge-vlan-filtering-without-hardware-offloading}

---

請考量以下情境：你發現了新的 bridge VLAN filtering 功能，並決定變更設備上的設定。你有一個非常簡單的 trunk/access 埠設定，而且你喜歡 bridge VLAN filtering 的概念。

### 設定 {#configuration-8}

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

例如，你在 CRS1xx/CRS2xx 系列設備上使用這個設定，並開始發現 CPU 使用率非常高。當執行效能測試檢查網路吞吐量時，你會發現總吞吐量只有應能輕易達到的線速效能的一小部分。問題的原因是並非所有設備都支援硬體層級的 bridge VLAN filtering。所有設備都能設定 bridge VLAN filtering，但只有少數設備能將流量卸載到交換器晶片。如果在內建交換器晶片的設備上使用不適當的設定方式，CPU 將被用於轉送流量。

### 徵兆 {#symptoms-8}

以下是可能由這類錯誤設定造成的徵兆清單：

- bridge 埠上缺少「H」旗標。
- 吞吐量偏低。
- CPU 使用率過高。

### 解決方案 {#solution-8}

使用 bridge VLAN filtering 之前，請確認你的設備在硬體層級是否支援此功能。相容性表格可在 [Bridge Hardware Offloading](/docs/bridging-and-switching#bridge-hardware-offloading) 一節找到。目前每種設備類型都需要不同的設定方式。以下清單列出設備應使用哪種設定，才能利用硬體卸載的優勢：

- [MikroTik devices with Marvell Prestera switch](/docs/bridging-and-switching#bridge-vlan-filtering)
- [CRS1xx/CRS2xx series devices](/docs/bridging-and-switching/user-guides/crs1xx-2xx-series-switches-examples#vlan)
- [Other devices with a switch chip](/docs/bridging-and-switching/switch-chip-features#setup-examples)

## 使用多個交換器晶片的 VLAN filtering {#vlan-filtering-with-multiple-switch-chips}

---

請考量以下情境：你有一台具備兩個或以上交換器晶片的設備，並決定使用單一 bridge，且在硬體層級設定 VLAN filtering（透過 `/interface/ethernet/switch` 選單），讓網路能達到線速效能。這對 RB2011 與 RB3011 系列設備特別相關。在此範例中，假設你想要有一個 trunk 埠，其餘所有埠都是 access 埠，例如 **ether10** 是 trunk 埠，而 **ether1-ether9** 是 access 埠。

### 設定 {#configuration-9}

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

執行幾項測試後，你可能會發現來自 **ether6-ether10** 的封包會如預期轉送，但來自 **ether1-ether5** 的封包不一定會正確轉送（尤其是透過 trunk 埠）。最明顯的問題是，來自 **ether1-ether5** 並通過 **ether10** 的封包會直接被丟棄。這是因為這些埠位於不同的交換器晶片上。這表示無法在硬體層級進行 VLAN filtering，因為交換器晶片無法得知另一個交換器晶片上的 VLAN 表內容。在不同交換器晶片上的埠之間轉送的封包也會由 CPU 處理，這表示你無法達到線速效能。

### 徵兆 {#symptoms-9}

以下是可能因這類設定錯誤而產生的症狀：

- 封包遭到丟棄。
- 吞吐量偏低。

### 解決方案 {#solution-9}

適當的作法是考量此硬體設計，並據此規劃網路拓撲。若要解決此問題，必須建立兩個獨立的 bridge，並在每個交換器晶片上設定 VLAN filtering。這會限制在交換器晶片之間轉送封包的可能性，不過仍可以設定兩個 bridge 之間的路由（若連接在各交換器晶片上的設備使用不同的網路子網）。

有一種方式可以將設備設定為讓所有埠一起交換，同時仍能在硬體層級使用 VLAN filtering，不過此解法有一些注意事項。作法是犧牲每個交換器晶片上的單一 Ethernet 埠，讓其作為 trunk 埠，以在交換器晶片之間轉送封包。這可以透過在兩個交換器晶片之間接上 Ethernet 纜線來完成，例如，在 **ether5** 與 **ether6** 之間接上 Ethernet 纜線，然後假設這些埠為 trunk 埠來重新設定您的設備：

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
對於 100Mbps 交換器晶片，請使用 `default-vlan-id=0`，而非 `default-vlan-id=auto`
:::

## 使用簡化 bridge VLAN 表的 VLAN filtering {#vlan-filtering-with-simplified-bridge-vlan-table}

---

:::info
此問題自 **RouterOS v7.15** 起已解決。動態 VLAN 現在一律建立為獨立項目，不再與靜態設定的項目合併。
:::

您需要建立一個網路設定，讓多個用戶端連接到不同的 access 埠，並依不同的 VLAN 進行隔離。這些流量應加上標籤並傳送至適當的 trunk 埠。Access 埠是使用 pvid 屬性設定。由於 trunk 埠同時用於兩個 VLAN，您決定透過新增單一 bridge VLAN 表項目，並以逗號分隔 VLAN，來簡化設定。當 tagged trunk 埠用於大量 VLAN，甚至特定 VLAN 範圍時，這特別有用（例如 vlan-id=100-200）。請參閱下方的網路圖與設定。

![Switch Multiple Untagged](/img/3205c6726f791982.webp)

### 設定 {#configuration-10}

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

流量已正確從 access 埠轉送並加上標籤至 trunk 埠，但您可能會發現，部分廣播或群播封包實際上會在兩個 untagged access 埠之間氾濫，雖然它們應該位於不同的 VLAN。此外，來自 tagged 埠的廣播與群播流量也會氾濫至兩個 access 埠。這可能會引起一些安全疑慮，因為來自不同網路的流量可能被側錄。當您查看 bridge VLAN 表時，會發現已為 VLAN 10 與 20 建立單一項目，且兩個 untagged 埠都屬於同一個 VLAN 群組。

```ros
[admin@SW1] /interface/bridge/vlan/print where tagged=ether2
Columns: BRIDGE, VLAN-IDS, CURRENT-TAGGED, CURRENT-UNTAGGED
# BRIDGE   VLAN-IDS  CURRENT-TAGGED  CURRENT-UNTAGGED
;;; port with pvid added to untagged group which might cause problems, consider adding a separate VLAN entry
0 bridge1        10  ether2          ether3          
                 20                  ether4     
```

### 徵狀 {#symptoms-10}

- 流量在不同 VLAN 之間氾濫
- 紅色警告：`port with pvid added to untagged group which might cause problems, consider adding a separate VLAN entry`

### 解決方案 {#solution-10}

當 access 埠使用 pvid 屬性設定時，它們會動態新增至適當的 VLAN 項目。建立具有多個 VLAN 或 VLAN 範圍的靜態 VLAN 項目後，具有相符 pvid 的 untagged access 埠也會被包含在相同的 VLAN 群組或範圍中。使用單一設定行定義大量 VLAN 可能很有用，但設定 access 埠時應特別小心。在此範例中，應建立個別的 VLAN 項目：

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=ether2 untagged=ether3 vlan-ids=10
add bridge=bridge1 tagged=ether2 untagged=ether4 vlan-ids=20
```

## 主介面上的 MTU {#mtu-on-the-master-interface}

---

請考量以下情境：你已建立一個 bridge，將幾個介面加入其中，並在 bridge 介面上建立 VLAN 介面，但你需要增加 VLAN 介面的 MTU 大小，以便接收較大的封包。

### 設定 {#configuration-11}

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

當你嘗試增加 VLAN 介面的 MTU 大小時，會收到 RouterOS **Could not set MTU** 錯誤。這可能發生在你嘗試將 MTU 設定為大於 L2MTU 時。在此情況下，你需要在所有 slave 介面上增加 L2MTU 大小，這將會更新 bridge 介面上的 L2MTU 大小。完成後，你就能在 VLAN 介面上設定較大的 MTU。相同的原則也適用於 bond 介面。只有當所有實體 slave 介面都設定了適當的 L2MTU 時，你才能在 VLAN、MPLS、VPLS、Bonding 及其他介面上增加 MTU。

### 徵狀 {#symptoms-11}

以下是可能由這類設定錯誤造成的徵狀清單：

- 無法變更 MTU。

### 解決方案 {#solution-11}

在變更 master 介面的 MTU 之前，請先增加 slave 介面的 L2MTU。

```ros
/interface/ethernet
set ether1,ether2 l2mtu=9018
/interface/vlan
set VLAN99 mtu=9000
```

## MTU 不一致 {#mtu-inconsistency}

---

請考量以下情境：你的網路中有多部設備。其中大多數作為網路中的交換器／橋接器使用，而某些端點則負責接收與處理流量。為了降低網路中的額外負擔，你決定增加 MTU 大小，因此你在兩個端點都設定了較大的 MTU 大小，但開始發現有些封包被丟棄。

![MTU Issues](/img/e87e9a6138906e63.webp)

### 設定 {#configuration-12}

在此案例中，兩個端點可以是任何類型的設備，我們假設它們都是 Linux 伺服器，並且要傳輸大量資料。在這種情境下，你可能已在 **ServerA** 與 **ServerB** 上將介面 MTU 設為 9000，而在你的 **Switch** 上，可能設定了類似以下的內容：

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add interface=ether1 bridge=bridge1
add interface=ether2 bridge=bridge1
```

### 問題 {#problem-12}

這是一個非常簡單的問題，但在較大的網路中可能難以偵測。例如，ping 可能正常運作，因為一般 ping 封包的長度為 70 位元組（Ethernet 標頭 14 位元組、IPv4 標頭 20 位元組、ICMP 標頭 8 位元組、ICMP 酬載 28 位元組），但資料傳輸可能無法正常運作。某些封包可能無法被轉送的原因是，執行 RouterOS 的 MikroTik 設備預設將 MTU 設為 1500，並將 L2MTU 設為約 1580 位元組（視設備而定），但 Ethernet 介面會悄悄丟棄任何不符合 L2MTU 大小的內容。請注意，L2MTU 參數與 x86 或 CHR 設備無關。對於僅負責轉送封包的設備，不需要增加 MTU 大小；只需要增加 L2MTU 大小。RouterOS 不允許你將 MTU 大小增加到大於 L2MTU 大小。如果你需要讓介面接收封包，且設備需要處理該封包而不只是轉送它，例如在路由的情況下，則必須同時增加 L2MTU 與 MTU 大小；但如果你只使用 IP 流量（支援封包分段），且不介意封包被分段，則可以將介面上的 MTU 大小保持為預設值。你可以使用 ping 工具確認所有設備都能轉送 jumbo frames：

```ros
/ping 192.168.88.1 size=9000 do-not-fragment
```

請記得，L2MTU 與 MTU 大小必須大於或等於傳送 ping 封包的設備上，傳送與接收 ping 封包的大小，因為 ping（ICMP）是透過第 3 層從介面送出的 IP 流量。

### 症狀 {#symptoms-12}

以下是可能由這類設定錯誤造成的症狀：

- 網頁無法載入，但 ping 正常。
- 通道丟棄流量。
- 特定協定無法運作。
- 大量封包遺失。

### 解決方案 {#solution-12}

增加 **Switch** 上的 L2MTU 大小：

```ros
/interface/ethernet
set ether1,ether2 l2mtu=9000
```

如果流量經過封裝（VLAN、VPN、MPLS、VPLS 或其他），則可能需要考慮設定更大的 L2MTU 大小。在此情境下，基於上述原因，不需要增加 MTU 大小。

:::warning
完整訊框 MTU 與 L2MTU 不同。L2MTU 大小不包含 Ethernet 標頭（14 位元組）與 CRC 檢查碼（FCS）欄位。FCS 欄位會由 Ethernet 驅動程式移除，RouterOS 永遠不會在任何封包中顯示額外的 4 位元組。例如，若將 MTU 與 L2MTU 設為 9000，則完整訊框 MTU 為 9014 位元組。使用 "`/tool/sniffer/quick`" 指令擷取封包時，也可以觀察到這一點。
:::

## Bridge 與保留的 MAC 位址 {#bridge-and-reserved-mac-addresses}

---

請考量以下情境：你想要以透明方式將兩個網路段橋接在一起，無論它們是 EoIP 這類通道介面、Wireless 介面、Ethernet 介面，或任何其他可加入 bridge 的介面類型。這類設定可讓你無縫連接兩台設備，就像兩者之間只有一條實體纜線。這有時稱為從 **DeviceA** 到 **DeviceB** 的 **transparent bridge**。

### 設定 {#configuration-13}

**DeviceA** 與 **DeviceB** 兩台設備都應該有非常相似的設定。

```ros
/interface/bridge
add name=bridge1 protocol-mode=rstp
/interface/bridge/port
add interface=ether1 bridge=bridge1
add interface=eoip1 bridge=bridge1
```

### 問題 {#problem-13}

兩台設備都能彼此通訊，但某些通訊協定無法正常運作。原因是，一旦你使用任何 STP 變體（STP、RSTP、MSTP），就會讓 bridge 符合 IEEE 802.1D 與 IEEE 802.1Q。這些標準建議，目的地為 **01:80:C2:00:00:0X** 的封包**不應**被轉送。當 bridge 中只加入 2 個埠時，不應使用 (R/M)STP，因為 2 個介面不可能形成迴圈；若確實發生迴圈，原因在別處，應在另一個 bridge 上修正。由於 transparent bridge 設定中不需要 (R/M)STP，因此可以停用。一旦停用 (R/M)STP，RouterOS bridge 就不符合 IEEE 802.1D 與 IEEE 802.1Q，因此會轉送目的地為 **01:80:C2:00:00:0X** 的封包。

### 徵狀 {#symptoms-13}

以下是可能由這類設定錯誤造成的症狀清單：

- LLDP 鄰居未顯示。
- 802.1x 驗證（dot1x）無法運作。
- LACP 介面未通過流量。

### 解決方案 {#solution-13}

可以部分停用對 IEEE 802.1D 與 IEEE 802.1Q 的相容性；做法是變更 bridge protocol mode。

```ros
/interface/bridge
set bridge1 protocol-mode=none
```

:::danger
IEEE 802.1x 標準設計用於交換器與用戶端之間直接連線。若可在交換器與用戶端之間接入設備，就會產生安全威脅。因此，不建議停用對 IEEE 802.1D 與 IEEE 802.1Q 的相容性，而應設計適當的網路拓撲。
:::

## 無線鏈路之間的 Bonding {#bonding-between-wireless-links}

---

請考量以下情境：你已設定多條 Wireless 鏈路，為了達到最大輸送量並同時具備備援，你決定將 Ethernet 介面放入 bond，並依據要轉送的流量選擇特定的 bonding mode。此情境可套用於任何在彼此未直接相連的鏈路之間建立 bonding 介面的情況。

![LACP over WLAN](/img/2de2fccfd3fb0dad.webp)

### 設定 {#configuration-14}

以下設定適用於 **R1** 與 **R2**：

```ros
/interface/bonding
add mode=802.3ad name=bond1 slaves=ether1,ether2 transmit-hash-policy=layer-2-and-3
/ip/address
add address=192.168.1.X/24 interface=bond1
```

下列設定與 **AP1**、**AP2**、**ST1** 與 **ST2** 相關，其中 **X** 對應每個設備的 IP 位址。

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

雖然 **R1** 與 **R2** 之間的流量轉送正常，負載平衡與鏈路容錯移轉也正常運作，但 **R1** 與 **R2** 之間的設備並非隨時都可存取，或部分設備完全無法存取（在多數情況下是 **AP2** 與 **ST2** 無法存取）。檢查問題後，您可能會發現封包並非總是透過所需的 bonding slave 轉送，因此永遠不會被您嘗試存取的設備接收。這是網路設計與 bonding 通訊協定的限制。當封包需要透過 bonding 介面傳送時（在此情況下，您可能嘗試將 ICMP 封包傳送至 **AP2** 或 **ST2**），bonding 介面會根據所選的 bonding mode 與 transmit-hash-policy 產生雜湊，並選取要用來傳送封包的介面，而不論目的地是否只能透過特定介面到達。部分設備可存取，是因為產生的雜湊符合設備所在的介面，但也可能未選取所需的介面，而導致設備無法存取。只有 broadcast bonding mode 沒有這種通訊協定限制，但此 bonding mode 的適用情境非常有限。

### 徵狀 {#symptoms-14}

以下是可能由這類設定錯誤造成的徵狀清單：

- 連線受限
- 鏈路不穩定（在 balance-rr 的情況下）

### 解決方案 {#solution-14}

bonding 介面不應使用間接鏈路連接，不過仍可建立變通方法。此變通方法的概念是找到一種方式，略過透過 bonding 介面傳送封包。有多種方式可強制封包不透過 bonding 介面傳送，但基本上，解決方式是在實體介面上建立新的介面，並將這些新建立的介面加入 bond，而不是加入實體介面。其中一種作法是為每個實體介面建立 EoIP 隧道，但這會產生極大的額外負擔，並降低整體吞吐量。您應該改為在每個實體介面上建立 VLAN 介面。這會產生小得多的額外負擔，且不會明顯影響整體效能。以下是 **R1** 與 **R2** 應如何重新設定的範例：

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

**AP1** 與 **ST1** 只需要更新 IP 位址為正確的子網路：

```ros
/ip/address
add address=192.168.11.X/24 interface=bridge1
```

相同的變更也必須套用到 **AP2** 與 **ST2**（請確保使用正確的子網路）：

```ros
/ip/address
add address=192.168.22.X/24 interface=bridge1
```

使用這種方式，您可以建立最少的額外負擔，並且需要進行的設定變更最少。

:::warning
LACP (802.3ad) 不適用於設備的 bonding slave 未直接連接的環境，在此情況下，如果兩台路由器之間有 Wireless 連線，不建議使用 LACP。LACP 要求兩個 bonding slave 具有相同的連線速度，而 Wireless 連線可能隨時變更速率，這會降低整體效能與穩定性。應改用其他 bonding 模式。
:::

## 頻寬測試 {#bandwidth-testing}

---

請考慮以下情境：您在兩台設備之間建立了一條連線。這可以是任何連線，例如 Ethernet 纜線、wireless 連線、隧道或任何其他連線。您決定要測試該連線的頻寬，但為了方便起見，您決定使用正在執行該連線的相同設備開始測試。

![Bad Bandwidth Setup](/img/590e348e86dd552a.webp)

### 問題 {#problem-15}

當您開始 [Bandwidth test](/docs/diagnostics-monitoring-and-troubleshooting/bandwidth-test) 或 [Traffic generator](/docs/diagnostics-monitoring-and-troubleshooting/traffic-generator) 時，您會發現吞吐量遠低於預期。對於應該能夠每秒轉發數十 Gigabit (Gbps) 的高效能路由器，您會發現每秒只轉發了幾個 Gigabit。發生這種情況的原因是您使用的測試方法。您不應該在使用同一台路由器產生流量的同時，於該路由器上測試吞吐量，因為這會增加 CPU 的額外負載，進而降低總吞吐量。

### 症狀 {#symptoms-15}

以下是可能由這類設定錯誤造成的症狀：

- 低吞吐量。
- CPU 使用率過高。

### 解決方案 {#solution-15}

使用適當的測試方法。請勿使用 Bandwidth-test 測試大容量鏈路，也不要在正在測試的同一台設備上執行任何會產生流量的工具。請妥善設計網路，以便在兩端都能連接可產生與接收流量的設備。如果你熟悉 **Iperf**，應該很清楚這個概念。請記得，在真實環境中，路由器或交換器不會產生大量流量（至少不應該；否則可能表示已有安全問題），流量是由伺服器／用戶端產生，而路由器／交換器負責轉送流量（並在適當情況下對流量進行一些處理）。

![Good Bandwidth Setup](/img/94426a9891add21a.webp)

## Bridge split-horizon 使用方式 {#bridge-split-horizon-usage}

---

請考慮以下情境：你有一個 bridge，需要將某些 bridge 埠彼此隔離。可以選擇使用內建交換器晶片在特定交換器晶片上隔離特定埠，也可以使用 bridge 防火牆規則防止特定埠將任何流量傳送至其他埠，還可以在 PVLAN 類型的設定中使用 port isolation 隔離埠，但也可以使用以軟體為基礎的 bridge split-horizon 解決方案（這會停用所有交換器晶片的硬體卸載）。

### 設定 {#configuration-15}

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

在每個埠上設定 bridge split-horizon 後，你開始發現埠之間仍然可以互相傳送資料。原因是誤用了 bridge split-horizon。bridge 埠只是無法與位於同一 horizon 的埠通訊，例如 horizon=1 無法與 horizon=1 通訊，但可以與 horizon=2、horizon=3 等通訊。

### 徵狀 {#symptoms-16}

以下是可能由這類設定錯誤造成的症狀清單：

- 流量會在不同的 bridge split-horizon 之間轉送。

### 解決方案 {#solution-16}

請設定適當的 bridge split-horizon 值。如果你想要讓各埠彼此隔離（PPPoE 設定的常見情境），且每個埠只能與 bridge 本身通訊，則所有埠都必須位於相同的 bridge split-horizon。

```ros
/interface/bridge/port
set [f] horizon=1
```

:::warning
將所有 bridge 埠設定在相同的 bridge split-horizon，會使流量只能到達 bridge 介面本身，接著封包只能被路由。當你希望其他設備篩選特定流量時，這很有用。類似行為也可以使用 bridge filter rules 達成。
:::

## 不支援的 SFP 模組 {#unsupported-sfp-modules}

---

請考量以下情境：你決定使用光纖纜線，透過 SFP 或 SFP+ 光學模組將設備互相連接，但為了方便起見，你決定使用現有的 SFP 光學模組。

### 問題 {#problem-17}

當你設定設備，讓使用這些 SFP 光學模組的埠具備連線能力時，可能會發現連線不是正常運作，就是出現隨機連線問題。有許多廠商製造 SFP 光學模組，但並非所有廠商都嚴格遵循 SFP MSA、SFF 與 IEEE 802.3 標準，這可能導致無法預測的相容性問題；在 MikroTik 設備中使用不知名或不支援的 SFP 光學模組時，這是相當常見的問題。

### 徵狀 {#symptoms-17}

以下是可能由這類錯誤設定造成的徵狀清單：

- SFP 介面無法建立連線。
- 隨機封包遺失。
- 連線不穩定（震盪）。
- SFP 模組在重新啟動後無法運作。
- SFP 模組在電源循環後無法運作。
- SFP 模組只有單側運作。

### 解決方案 {#solution-17}

請只使用支援的 SFP 模組。若打算使用由 MikroTik 製造的 SFP 模組，請務必查看 [SFP 相容性對照表](/docs/wired-connections/mikrotik-wired-interface-compatibility)。也有其他 SFP 模組可與 MikroTik 設備搭配運作。請查看 [支援的周邊裝置對照表](/docs/hardware/peripherals#sfp-modules)，找出其他已確認可與 MikroTik 設備搭配運作的 SFP 模組。某些不支援的模組在特定速度與自動協商下可能無法正常運作。你可以嘗試停用自動協商，並手動設定連線速度。
