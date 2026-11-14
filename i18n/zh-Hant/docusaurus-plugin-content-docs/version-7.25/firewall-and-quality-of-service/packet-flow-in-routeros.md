---
sidebar_key: "firewall-and-quality-of-service/packet-flow-in-routeros"
sidebar_position: 2
title: "RouterOS 中的封包流程"
sidebar_label: "RouterOS 中的封包流程"
description: "本頁說明封包如何在 MikroTik RouterOS 中流轉，詳細描述橋接、路由、MPLS 決策與防火牆鏈之間的互動。文中包含示意圖，展示從入口到出口各階段的封包處理過程，並對路由表和防火牆鏈等關鍵元件進行說明。"
tags:
  - 'firewall'
  - 'packet-flow'
source: https://manual.mikrotik.com/docs/7.25/firewall-and-quality-of-service/packet-flow-in-routeros
captured_at: '2026-11-04T11:18:21+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

更高階的防火牆配置或複雜任務（例如流量優先順序劃分、路由策略），在需要利用多個 RouterOS 功能時，要求瞭解：這些功能如何協同工作？在什麼情況下、為什麼會發生什麼？

RouterOS 封包流程圖和流程示例將嘗試回答這些問題。

在單個圖中表示封包的處理過程會非常複雜；因此，封包流程圖被分為三個部分：

- 總體圖。
- 詳細的橋接、路由和 MPLS 流程圖。
- 顯示 prerouting、input、forward、output 和 postrouting 中包含哪些功能及其順序的圖。

### 總體封包流程圖 {#overall-packetflow-diagram}

讓我們先看總體圖。乍一看很複雜，但在我們透過示例講解之後，它會變得清晰得多。

![](/img/54a08457cdf41791.svg)

圖中央有 4 個框：橋接、路由、MPLS 決策和本地路由器程式。例如，如果封包需要透過路由器進行路由，封包將按下圖所示流動。無需深入瞭解每個功能，封包進入 in-interface，路由器判斷它是 IP 流量且需要路由，封包經過所有路由程式並從 out-interface 發出。

![](/img/47875864c1d4173f.webp)讓我們再看另一個示例，說明當封包的目的地是路由器本身時會發生什麼。例如，in-interface 收到一個 ICMP（ping）封包，其目的地是路由器本身，因此封包將進入 *local-in* 處理。封包處理完畢後，路由器內部會生成一個 ICMP（ping）應答（*local-out* 處理），並透過 out-interface 傳送出去。

![](/img/c6b18c0d99ad79af.webp)在繼續舉例之前，先簡單解釋每個框：

- **物理 in-interface** - 路由器接收封包的起點。
- **邏輯 in-interface** - 解封裝後封包（來自隧道、IPsec 等）的起點。
- **Local in** - 發往路由器本身的封包的終點。
- **Interface HTB（分層令牌桶）** - 介面佇列。
- **物理 out-interface** - 封包實際發出前的終點。
- **邏輯 out-interface** - 封包封裝前（發往隧道、IPsec 等）的終點。
- **Local out** - 路由器生成的封包的起點。

現在該深入瞭解橋接、MPLS 和路由流程內部發生了什麼。

![](/img/3d82c42594228f6f.webp)

在繼續舉例之前，先簡單解釋每個框：

- **路由決策** - 遍歷路由表中的路由，為封包的目標 IP 地址查詢匹配項。找到匹配項時，封包將繼續處理；未找到匹配項時，封包將被丟棄。
- **MPLS 決策** - 根據 MPLS 轉發表決定如何處理封包。
- **橋接決策** - 網橋遍歷 MAC 地址表，為封包的目標 MAC 地址查詢匹配項。找到匹配項時，封包將繼續處理；未找到匹配項時，將建立封包的多個副本並泛洪（透過所有網橋埠傳送）。由於網橋介面本身也是眾多目的地之一，單個數據包副本也會到達網橋 input 鏈。使用 `vlan-filtering=yes` 時，因 `/interface/bridge/vlan` 表而不被允許的封包將在此階段被丟棄。
- **use-ip-firewall** - 網橋設定中是否啟用了 '*use-ip-firewall'* 選項。
- **ipsec-policy** - 封包是否匹配任何已配置的 IPsec 策略。

#### 鏈 {#chains}

RouterOS 包含幾個預設鏈。這些鏈允許你在各個點過濾封包：

- **PREROUTING** 鏈：此鏈中的規則適用於剛到達網路介面的封包。此鏈存在於 *nat*、*mangle* 和 *raw* 表中。
- **INPUT** 鏈：此鏈中的規則適用於即將交給本地程式的封包。此鏈存在於 *mangle* 和 *filter* 表中。
- **OUTPUT** 鏈：此處的規則適用於程式剛生成的封包。此鏈存在於 *raw*、*mangle*、nat 和 *filter* 表中。
- **FORWARD** 鏈：此處的規則適用於任何通過當前主機路由的封包。此鏈僅存在於 *mangle* 和 *filter* 表中。
- **POSTROUTING** 鏈：此鏈中的規則適用於即將離開網路介面的封包。此鏈存在於 *nat* 和 *mangle* 表中。

prerouting、input、forward、output 和 postrouting 每個塊都包含更多功能，這些在封包流程圖的第三部分中說明：

![](/img/0724b7c10ff614e8.webp)

在繼續舉例之前，先簡單解釋每個框：

- **Hotspot-in** - 允許捕獲否則會被連線跟蹤丟棄的流量——這樣即使網路設定一團糟，我們的 Hotspot 功能也能提供連線。
- **RAW Prerouting** - RAW 表 prerouting 鏈。
- **連線跟蹤** - 封包由連線跟蹤處理。
- **Mangle Prerouting** - Mangle prerouting 鏈。
- **Mangle Input** - Mangle input 鏈。
- **Filter Input** - 防火牆 filter input 鏈。
- **HTB Global** - 佇列樹。
- **Simple Queues** - 可用於限制特定目標流量的功能。
- **TTL** - 指示路由封包的生存時間（TTL）減 1 的確切位置。如果 TTL 變為 0，封包將被丟棄。
- **Mangle Forward** - Mangle forward 鏈。
- **Filter Forward** - Filter forward 鏈。
- **Accounting** - 認證、授權和計費功能處理。
- **RAW Output** - RAW 表 output 鏈。
- **Mangle Output** - Mangle output 鏈。
- **Filter Output** - 防火牆 filter output 鏈。
- **路由調整** - 這是一種變通方法，允許在 mangle 鏈 output 中設定策略路由（routing-mark）。
- **Mangle Postrouting** - Mangle postrouting 鏈。
- **Src Nat** - 網路地址轉換 srcnat 鏈。
- **Dst Nat** - 網路地址轉換 dstnat 鏈。
- **Hotspot-out** - 對返回用戶端的封包撤銷 hotspot-in 所做的所有操作。

### 路由封包的流程 {#flow-of-routed-packet}

#### 轉發 {#forward}

現在，讓我們看第一個示例，封包透過路由器進行路由，並深入瞭解封包經過哪些功能：

我們已經瞭解到，封包進入 in-interface，路由器判斷它是 IP 封包且需要路由，這裡開始了複雜的過程：

1. 封包進入 prerouting 處理：
   1. 檢查是否存在 hotspot，併為 hotspot 使用修改封包。
   2. 透過 RAW prerouting 鏈處理封包。
   3. 將封包傳送透過連線跟蹤。
   4. 透過 Mangle prerouting 鏈處理封包。
   5. 透過 NAT 的 dst-nat 鏈處理封包。
2. 讓封包透過路由表以做出路由決策。
3. 封包進入 forward 處理：
   1. 檢查 TTL 值。
   2. 透過 Mangle forward 鏈處理封包。
   3. 透過 Filter forward 鏈處理封包。
   4. 將封包傳送到計費程式。
4. 封包進入 postrouting 處理：
   1. 透過 Mangle postrouting 鏈處理封包。
   2. 透過 NAT 的 src-nat 鏈處理封包。
   3. 如果存在 hotspot，撤銷 hotspot-in 中所做的任何修改。
   4. 透過佇列樹（HTB Global）處理封包。
   5. 透過 simple queues 處理封包。
5. 檢查是否存在 IPsec，然後透過 IPsec 策略處理。

![](/img/8dac7fe74227e99a.webp)

![](/img/d45ef1f88a92f873.webp)

#### 輸入 {#input}

我們已經瞭解到，封包進入 in-interface，路由器判斷它是 IP 封包且需要路由，這裡開始了複雜的過程：

1. 當封包的目的地是路由器時（路由 input），會發生非常類似的過程：封包進入 prerouting 處理：
   1. - 檢查是否存在 hotspot，併為 hotspot 使用修改封包。
   2. - 透過 RAW prerouting 鏈處理封包。
   3. - 將封包傳送透過連線跟蹤。
   4. - 透過 Mangle prerouting 鏈處理封包。
   5. - 透過 NAT 的 dst-nat 鏈處理封包。
2. 讓封包透過路由表以做出路由決策。
3. 封包進入 input 處理：
   1. - 透過 Mangle input 鏈處理封包。
   2. - 透過 Filter input 鏈處理封包。
   3. - 透過佇列樹（HTB Global）處理封包。
   4. - 透過 simple queues 處理封包。
4. 檢查是否存在 IPsec，然後透過 IPsec 策略處理。

![](/img/8d210a14ee931fdf.webp)

![](/img/e4c27a683fe133ca.webp)

#### 輸出 {#output}

或者當封包由路由器發起時（路由 output）：

1. 封包由路由器本身發起。
   1. 封包透過路由表以做出路由決策。
2. 封包進入 output 處理。
   1. 透過橋接決策處理封包。
   2. 將封包傳送透過連線跟蹤。
   3. 透過 Mangle output 鏈處理封包。
   4. 透過 Filter output 鏈處理封包。
   5. 將封包傳送到路由調整（策略路由）。
3. 封包進入 postrouting 處理。
   1. - 透過 Mangle postrouting 鏈處理封包。
   2. - 透過 NAT 的 src-nat 鏈處理封包。
   3. - 如果存在 hotspot，撤銷 hotspot-in 中所做的任何修改。
   4. - 透過佇列樹（HTB Global）處理封包。
   5. - 透過 simple queues 處理封包。
4. 檢查是否存在 IPsec，然後透過 IPsec 策略處理。

![](/img/d7ee665d35fc59eb.webp)![](/img/bbe918f99502e362.webp)

### 橋接封包的流程 {#flow-of-bridged-packet}

下面討論 RouterOS 中的一般橋接過程。大多數封包將始終遵循相同的處理路徑，但在某些配置下（例如啟用 VLAN 過濾、horizon、STP、DHCP 或 IGMP snooping 時），某些封包可能會被區別對待。請訪問橋接手冊以獲取更具體的資訊。

#### ![](/img/936d1582966e9a76.webp) {#}

#### 橋接轉發 {#bridge-forward}

Bridge forward 是封包從一個網橋埠轉發到另一個網橋埠時發生的過程，本質上是在同一網路上連線多個裝置。在 in-interface 上收到封包後，裝置判斷 in-interface 是網橋埠，因此封包透過橋接過程：

1. 封包透過網橋 NAT dst-nat 鏈，其中可以更改 MAC 目的地和優先順序，除此之外，封包可以被簡單地接受、丟棄或標記。
2. 檢查網橋設定中是否啟用了 use-ip-firewall 選項。
3. 讓封包透過網橋主機表以做出轉發決策。最終被泛洪的封包（例如廣播、組播、未知單播流量）會按網橋埠複製，然後在 bridge forward 鏈中進一步處理。使用 `vlan-filtering=yes` 時，因 `/interface/bridge/vlan` 表而不被允許的封包將在此階段被丟棄。
4. 封包透過網橋 filter forward 鏈，其中可以更改優先順序，或者封包可以被簡單地接受、丟棄或標記。
5. 檢查網橋設定中是否啟用了 use-ip-firewall 選項。
6. 封包透過網橋 NAT src-nat 鏈，其中可以更改 MAC 源和優先順序，除此之外，封包可以被簡單地接受、丟棄或標記。
7. 檢查網橋設定中是否啟用了 use-ip-firewall 選項。

![](/img/19c0854c81bd23fd.webp)

:::info
**對於 RouterOS v6：**  
當啟用網橋 `vlan-filtering` 時，接收到的未標記封包可能會在 "DST-NAT" 塊之前被封裝到 VLAN 頭中，這意味著這些封包可以使用 `mac-protocol=vlan` 和 `vlan-encap` 設定進行過濾。如果出介面的 `frame-types` 設定為 `admit-all` 或 `admit-only-untagged-and-priority-tagged`，則可能發生封裝。

已標記的封包可能會在 "BRIDGING DECISION" 塊上被解封裝，這意味著這些封包將不再匹配 `mac-protocol=vlan` 和 `vlan-encap` 設定。如果封包的 VLAN ID 與出埠的未標記 VLAN 成員資格匹配，則可能發生解封裝。  
  
**對於 RouterOS v7 及更新版本：**

當啟用網橋 `vlan-filtering` 時，接收到的未標記封包可能會在 "BRIDGING-DECISION" 塊上被封裝到 VLAN 頭中，這意味著這些封包可以使用 `mac-protocol=vlan` 和 `vlan-encap` 設定進行過濾。如果出介面的 `frame-types` 設定為 `admit-all` 或 `admit-only-untagged-and-priority-tagged`，則可能發生封裝。

已標記的封包可能會在 "BRIDGING DECISION" 塊上被解封裝，這意味著這些封包將不再匹配 `mac-protocol=vlan` 和 `vlan-encap` 設定。如果封包的 VLAN ID 與出埠的未標記 VLAN 成員資格匹配，則可能發生解封裝。
:::

#### 橋接輸入 {#bridge-input}

Bridge input 是封包目的地為網橋介面時發生的過程。最常見的情況是你需要訪問網橋介面上執行的某些服務（例如 DHCP 伺服器），或者需要將流量路由到其他網路。最初的步驟與 bridge forward 過程類似——在 in-interface 上收到封包後，裝置判斷 in-interface 是網橋埠，因此它透過橋接過程：

1. 封包透過網橋 NAT dst-nat 鏈，其中可以更改 MAC 目的地和優先順序，除此之外，封包可以被簡單地接受、丟棄或標記。
2. 檢查網橋設定中是否啟用了 use-ip-firewall 選項。
3. 讓封包透過網橋主機表以做出轉發決策。目標 MAC 地址與網橋 MAC 地址匹配的封包將被傳遞到網橋 input 鏈。最終被泛洪的封包（例如廣播、組播、未知單播流量）也會到達網橋 input 鏈，因為網橋介面本身也是眾多目的地之一。
4. 封包透過網橋 filter input 鏈，其中可以更改優先順序，或者封包可以被簡單地接受、丟棄或標記。

![](/img/c086efd5882264c9.webp)

#### 橋接輸出 {#bridge-output}

Bridge output 是封包應透過一個或多個網橋埠離開裝置時發生的過程。最常見的情況是網橋介面本身嘗試訪問連線到某個網橋埠的裝置（例如，網橋介面上執行的 DHCP 伺服器響應 DHCP 用戶端時）。在封包由其他更高級別的 RouterOS 程式處理完畢，並且裝置最終判斷出介面是網橋之後，封包透過橋接過程：

1. 讓封包透過網橋主機表以做出轉發決策。最終被泛洪的封包（例如廣播、組播、未知單播流量）會按網橋埠複製，然後在 bridge output 鏈中進一步處理。
2. 封包透過網橋 filter output 鏈，其中可以更改優先順序，或者封包可以被簡單地接受、丟棄或標記。
3. 封包透過網橋 NAT src-nat 鏈，其中可以更改 MAC 源和優先順序，除此之外，封包可以被簡單地接受、丟棄或標記。
4. 檢查網橋設定中是否啟用了 use-ip-firewall 選項。

![](/img/c29c9ee3aa3a635e.webp)

#### 啟用防火牆時的 Forward {#forward-with-firewall-enabled}

在某些網路配置中，你可能需要為橋接流量在路由鏈上啟用額外處理，例如使用 simple queues 或 IP 防火牆。這可以在網橋設定中啟用 use-ip-firewall 時完成。請注意，額外處理將消耗更多 CPU 資源來處理這些封包。所有步驟已在前面幾點中討論過；下面是回顧：

1. 封包透過網橋 NAT dst-nat 鏈。
2. 啟用 use-ip-firewall 選項後，封包將在 prerouting 鏈中進一步處理。
3. 封包進入 prerouting 處理。
4. 讓封包透過網橋主機表以做出轉發決策。
5. 封包透過網橋 filter forward 鏈。
6. 啟用 use-ip-firewall 選項後，封包將在路由 forward 鏈中進一步處理。
7. 封包進入路由 forward 處理。
8. 封包透過網橋 NAT src-nat 鏈。
9. 啟用 use-ip-firewall 選項後，封包將在 postrouting 鏈中進一步處理。
10. 封包進入 postrouting 處理。

![](/img/ca8f80b20d2e4d28.webp)![](/img/f1ae5b79a33340c3.webp)

### 硬體解除安裝封包的流程 {#flow-of-hardware-offloaded-packet}

在上一主題中，我們僅討論了軟體橋接，它需要主 CPU 處理才能將封包轉發到正確的網橋埠。大多數 MikroTik 裝置配備了專用交換硬體，即所謂的交換晶片或交換 ASIC。這允許我們將一些橋接功能（例如網橋埠之間的封包轉發或封包過濾）解除安裝到這個專用硬體晶片上，而不消耗任何 CPU 資源。在 RouterOS 中，我們將此功能命名為 Bridge Hardware (HW) Offloading。不同的 MikroTik 裝置可能具有不同的交換晶片，每個晶片可用的功能集也不同，因此請務必訪問本文以獲取更多詳細資訊 - [Bridge Hardware Offloading](../bridging-and-switching/index.md#bridge-hardware-offloading)。

![](/img/ea5afd533506de95.webp)

:::warning
當 out-interface 為硬體解除安裝且網橋 Fast Path 未啟用時，Interface HTB 將無法正常工作。
:::

![](/img/3fcb32a3b81fe833.webp)

- **交換決策** - 很大程度上取決於交換器型號。此塊控制所有與交換相關的任務，例如主機學習、封包轉發、過濾、VLAN 標記/取消標記等。某些交換器配置可能會改變封包流程。
- **switch-cpu 埠** - 用於主 CPU 與其他交換器埠之間通訊的特殊用途交換器埠。請注意，switch-cpu 埠不會在 RouterOS 中除 switch 選單以外的任何地方顯示。任何與軟體相關的配置（例如 interface-list）都無法應用於此埠。到達 CPU 的封包會自動與物理 in-interface 關聯。

然而，硬體解除安裝並不限制裝置只能使用硬體有限的功能；相反，可以同時利用硬體和軟體處理。這確實需要深入理解封包如何透過交換晶片傳輸，以及它們究竟何時被傳遞給主 CPU。

:::info
在 `/interface/ethernet/switch` 選單及其子選單中找到的交換器功能，例如 ACL 規則、映象、入/出速率限制器、QoS 和 L3HW（除 VLAN 間路由外），可能不依賴網橋硬體解除安裝。因此，它們**可能**可以應用於未在硬體解除安裝網橋中配置的介面。
:::

#### 交換器轉發 {#switch-forward}

我們將進一步討論啟用網橋硬體解除安裝且封包在單個交換晶片上的兩個交換埠之間轉發時的封包流程。這是最常見也是最簡單的示例：

1. 交換器檢查 in-interface 是否為硬體解除安裝介面。
2. 交換器讓封包透過交換器主機表以做出轉發決策。如果交換器找到目標 MAC 地址的匹配項，封包將透過物理介面傳送出去。最終被泛洪的封包（例如廣播、組播、未知單播流量）會被複制併發送到每個硬體解除安裝交換器埠。

![](/img/dddbd2a9528c75c7.webp)

#### 交換器到 CPU 輸入 {#switch-to-cpu-input}

此過程發生在物理介面上收到封包，且其目的地是 switch-cpu 埠以進行進一步軟體處理時。通往 switch-cpu 的路徑有兩條。一條是甚至不使用硬體解除安裝和交換的情況（例如用於路由的獨立介面，或故意停用 HW 解除安裝的橋接介面），因此封包只是被傳遞以進行進一步軟體處理。另一條路徑是在 in-interface 上啟用了硬體解除安裝時採用的。這會導致封包透過交換決策，並且交換器可能因各種原因將封包轉發到 switch-cpu 埠：

- 封包的目標 MAC 地址與本地 MAC 地址匹配，例如當封包目的地是本地網橋介面時。
- 封包可能被泛洪到所有交換器埠，包括 switch-cpu 埠，例如收到廣播、組播或未知單播流量時。
- 交換器可能已學習到某些主機只能透過 CPU 訪問（switch-cpu 埠學習將在下一節討論），例如當網橋包含 HW 和非 HW 解除安裝介面（如無線、EoIP 甚至乙太網介面）時。
- 封包被有意複製到 switch-cpu，例如用於封包檢查。
- 封包由交換器配置觸發，應在軟體中處理，例如 DHCP 或 IGMP snooping。

檢視 in-interface 為硬體解除安裝時的封包流程：

1. 交換器檢查 in-interface 是否為硬體解除安裝介面。
2. 讓封包透過交換器主機表以做出轉發決策。如果上述任何一點成立，封包將被轉發到 switch-cpu 埠。
3. 封包透過 switch-cpu 埠離開，並將由 RouterOS 封包流程進一步處理。

![](/img/aa47730474667b9a.webp)

:::warning
任何被交換晶片泛洪的已接收封包，都不會再被軟體網橋泛洪到同一 HW 解除安裝交換器組。這可以防止形成重複封包。
:::

#### CPU 輸出到交換器 {#cpu-output-to-switch}

此過程發生在封包離開 RouterOS 軟體處理並在 switch-cpu 埠上被接收時。同樣，封包可以走兩條路徑。一條是甚至不使用硬體解除安裝和交換的情況（例如用於路由的獨立介面，或故意停用 HW 解除安裝的橋接介面），因此封包只是透過物理 out-interface 傳送出去。另一條路徑是在 out-interface 上啟用了硬體解除安裝時採用的。這會導致封包透過交換決策。就像任何其他交換器埠一樣，交換器會從 switch-cpu 埠上接收的封包中學習源 MAC 地址。當網橋包含 HW 和非 HW 解除安裝介面時，這確實很有用，這樣交換器可以學習哪些幀應轉發到 CPU。檢視 out-interface 為硬體解除安裝時的封包流程：

1. 離開 RouterOS 軟體處理的封包在 switch-cpu 埠上被接收。
2. 交換器檢查 out-interface 是否為硬體解除安裝介面。
3. 交換器讓封包透過交換器主機表以做出轉發決策。如果交換器找到目標 MAC 地址的匹配項，封包將透過物理介面傳送出去。最終被泛洪的封包（例如廣播、組播、未知單播流量）會被複制併發送到每個硬體解除安裝交換器埠。

![](/img/c2e413d83e995a03.webp)

:::warning
軟體網橋透過 HW offloaded 介面傳送泛洪封包時，每個 HW offloaded 交換器組只會傳送一份封包副本，而不是每個 HW offloaded 介面各發送一份。實際的泛洪由交換晶片完成；這樣可以防止產生重複封包。
:::

### MPLS 封包流程 {#flow-of-mpls-packet}

![](/img/3dc66d654b4ce06e.webp)

#### Pop 標籤 {#pop-label}

![](/img/7a74ba782936be6d.webp)

#### Switch 標籤 {#switch-label}

![](/img/ea6fa4d9db09d154.webp)

#### Push 標籤 {#push-label}

![](/img/87c77c70ffb17ec1.webp)

### MPLS IP VPN {#mpls-ip-vpn}

在 VPNv4 環境中，到達 PE 路由器且需要轉發到 CE 路由器的封包並不是典型的“轉發”。

如果入站標籤和目的地都繫結到 VRF，那麼在 MPLS 標籤被彈出之後：

- 如果目的地址屬於路由器本地，則封包被移至 LOCAL\_IN。
- 如果目的地址位於 CE 網路中，則封包被移至 LOCAL\_OUT。

:::danger
從 MPLS 雲轉發到 CE 網路的封包不會出現在 forward 中。
:::

例如，從 src:111.15.0.1 到 dst:111.13.0.1 的流量

```text
[admin@CCR2004_2XS] /mpls/forwarding-table> print 
Flags: L - LDP, P - VPN
Columns: LABEL, VRF, PREFIX, NEXTHOPS
#   LABEL  VRF      PREFIX         NEXTHOPS                                                                                                           
0 P    17  myVrf    111.13.0.0/24  
4 L    20  main     203.0.113.2    { label=impl-null; nh=111.11.0.1; interface=sfp-sfpplus1 }
[admin@CCR2004_2XS] /mpls/forwarding-table>                                                           
...

[admin@CCR2004_2XS] /ip/route> print detail 
Flags: D - dynamic; X - disabled, I - inactive, A - active; c - connect, s - static, r - rip, b - bgp, o - ospf, i - is-is, d - dhcp, v - vpn, m - modem, y - bgp-mpls-vpn; 
H - hw-offloaded; + - ecmp 

   DAc   dst-address=111.11.0.0/24 routing-table=main gateway=sfp-sfpplus1 immediate-gw=sfp-sfpplus1 distance=0 scope=10 suppress-hw-offload=no 
         local-address=111.11.0.2%sfp-sfpplus1 
   DAc   dst-address=203.0.113.1/32 routing-table=main gateway=lo immediate-gw=lo distance=0 scope=10 suppress-hw-offload=no local-address=203.0.113.1%lo 
   DAo   dst-address=203.0.113.2/32 routing-table=main gateway=111.11.0.1%sfp-sfpplus1 immediate-gw=111.11.0.1%sfp-sfpplus1 distance=110 scope=20 target-scope=10 
         suppress-hw-offload=no 
   DAc   dst-address=111.13.0.0/24 routing-table=myVrf gateway=sfp-sfpplus2@myVrf immediate-gw=sfp-sfpplus2 distance=0 scope=10 suppress-hw-offload=no 
         local-address=111.13.0.2%sfp-sfpplus2@myVrf 
   DAy   dst-address=111.15.0.0/24 routing-table=myVrf gateway=203.0.113.2 immediate-gw=111.11.0.1%sfp-sfpplus1 distance=200 scope=40 target-scope=30 suppress-hw-offload=no [admin@CCR2004_2XS] /ip/route>              
```

該封包會出現在 output 和 postrouting 鏈中，因為此時它已經是一個本地產生的封包，其源 MAC 地址等於 vrfInterface：

```text
08:10:55 firewall,info output: in:(unknown 0) out:sfp-sfpplus2, connection-state:established src-mac f2:b5:e9:17:18:3b, proto ICMP (type 8, code 0), 111.15.0.1->111.13.0.1, len 56
08:10:55 firewall,info postrouting: in:myVrf out:sfp-sfpplus2, connection-state:established src-mac f2:b5:e9:17:18:3b, proto ICMP (type 8, code 0), 111.15.0.1->111.13.0.1, len 56
```

另一方面，CE→PE 方向路由的封包在傳送到 MPLS 之前，會像其他任何路由 IP 流量一樣出現在 "forward" 中：

```text
 08:10:55 firewall,info prerouting: in:sfp-sfpplus2 out:(unknown 0), connection-state:established src-mac dc:2c:6e:46:f8:93, proto ICMP (type 0, code 0), 111.13.0.1->111.15.0.1, len 56
 08:10:55 firewall,info forward: in:sfp-sfpplus2 out:sfp-sfpplus1, connection-state:established src-mac dc:2c:6e:46:f8:93, proto ICMP (type 0, code 0), 111.13.0.1->111.15.0.1, len 56
 08:10:55 firewall,info postrouting: in:sfp-sfpplus2 out:sfp-sfpplus1, connection-state:established src-mac dc:2c:6e:46:f8:93, proto ICMP (type 0, code 0), 111.13.0.1->111.15.0.1, len 56
 
```

但也可能存在例外。如果回覆封包的目的 IP 屬於路由器本地，並且連線跟蹤正在執行 NAT 轉換，那麼連線跟蹤會“強制”該封包經過防火牆的 prerouting/forward/postrouting 鏈。

### 邏輯介面 {#logical-interfaces}

到目前為止，我們看到的示例中 in 或 out 介面都是實際的物理介面（乙太網、無線），但如果路由器接收到隧道封裝的封包，封包會如何流動呢？

![](/img/91fe801fb891e2c4.webp)

假設有一個 IPIP 封包進入路由器。由於它是普通的 IPv4 封包，因此會經過所有與路由相關的處理環節（直到圖中的 "J"）。然後路由器會檢查該封包是否需要解封裝。在本例中，它是 IPIP 封包，所以“是”，將封包送去解封裝。之後，封包會再次迴圈經過所有處理環節，但這一次是作為解封裝後的 IPv4 封包。

這一點非常重要，因為封包實際上會兩次經過防火牆，所以如果配置了嚴格的防火牆，那麼既需要為 IPIP 封裝的封包設定 "accept" 規則，也需要為解封裝後的 IP 封包設定 "accept" 規則。

:::info
使用啟用了 `vlan-filtering` 的網橋進行的封包封裝和解封裝與邏輯介面無關。更多細節請參見網橋章節。
:::

### IPSec 策略 {#ipsec-policies}

我們來看另一種隧道型別——IPSec。這種 VPN 沒有邏輯介面，但處理方式類似。

封包不是透過邏輯介面處理，而是透過 IPSec 策略處理。在完成路由決策 (2) 和 input 防火牆處理 (3) 之後，路由器會嘗試將源和目的與 IPsec 策略進行匹配。當策略與封包匹配時，封包會被送去解密 (5)。解密之後，封包再次進入 PREROUTING 處理 (6)，並開始另一輪處理迴圈，但此時處理的是解封裝後的封包。

![](/img/4dea6a04e6bb6979.webp)

同樣的過程也適用於封裝，只是順序相反。第一個 IP 封包先經過各處理環節，然後與 IPsec 策略匹配 (5)，進行封裝 (6)，然後在第二輪迴圈中送去處理 (7-10)。

![](/img/4b030c78a10265d8.webp)

## 快速路徑 {#fast-path}

從目前所學的內容來看，很明顯這樣的封包處理會消耗大量 CPU 資源。為了加速處理，RouterOS v6 首次引入了 FastPath。它的作用是跳過 Linux 核心中的處理，本質上是用部分 RouterOS 功能換取效能。要使 FastPath 生效，需要介面驅動支援以及特定的配置條件。

### Fast Path 的工作原理 {#how-fast-path-works}

FastPath 是一種介面驅動擴充套件，允許驅動直接與特定的 RouterOS 處理環節通訊，並跳過其他所有環節。

![](/img/be678c125b183720.svg)

只有當至少源介面支援 fast path 時，封包才能由 fast path 處理器轉發。要實現完整的快速轉發，還需要目的介面也支援。

目前，RouterOS 有以下 FastPath 處理器：

- IP 流量處理
- FastTrack
- Traffic Generator
- MPLS
- Bridge

滿足以下條件時才會使用 FastPath 處理器：

- 未配置防火牆規則。
- 未配置 simple queue 或 *parent=global* 的 queue tree。
- 未配置 mesh 或 metarouter 介面。
- 未執行 sniffer 或 torch。
- 連線跟蹤未啟用。
- IP accounting 已停用。
- 未配置 VRF（`/ip/vrf` 為空）。
- 未使用 hotspot（`/ip/hotspot` 沒有介面）。
- 未配置 IPSec 策略。
- 未主動使用 `/tool/mac-scan`。
- 未主動使用 `/tool/ip-scan`。

:::warning
如果使用了 FastTrack，無論上述條件是否滿足，封包都會走 FastPath 路徑。
:::

FastPath 按目的地址快取 IPv4 和 IPv6 路由，而不是按 L4 埠或內部頭部快取。因此，ECMP 的 `l4` 和 `l3-inner` 策略不會為 FastPath 快取的流量提供按流分發。

如果介面支援該功能，Traffic Generator 會自動使用 FastPath。

目前，MPLS fast-path 適用於 MPLS 交換流量（以 MPLS 進入路由器且必須以 MPLS 離開路由器的幀）以及執行 VPLS 封裝/解封裝的 VPLS 端點。其他 MPLS 入站和出站流量將照舊處理。

滿足以下條件時會使用 Bridge 處理器：

- 沒有 bridge Calea、filter、NAT 規則。
- *use-ip-firewall* 已停用。
- 沒有 mesh、MetaRouter 介面配置。
- 未執行 sniffer、torch 和 traffic generator。
- bridge vlan-filtering 已停用（自 RouterOS 7.2 版本起該條件已移除）。
- bridge dhcp-snooping 已停用。

:::warning
vlan-filtering 網橋上的 FastPath 不支援 priority-tagged 封包（帶有 VLAN 頭但 VLAN ID = 0 的封包）。這些封包會被重定向到慢速路徑。
:::

支援 FastPath 的介面：

| RouterBoard | 介面 |
| :-- | :-- |
| **RB6xx 系列** | ether1,2 |
| **RB800** | ether1,2 |
| **RB1100 系列** | ether1-11 |
| **所有裝置** | 乙太網介面 |
|  | 無線介面 |
|  | 網橋介面 |
|  | VLAN、VRRP 介面 |
|  | bonding 介面（僅 RX） |
|  | PPPoE、L2TP 介面 |
|  | EoIP、GRE、IPIP、VXLAN 介面。 |
|  | VPLS（從 v7.17 開始） |

EoIP、Gre、IPIP、VXLAN 和 L2TP 介面有一個按介面的設定 *allow-fast-path*。在這些介面上允許 fast path 會帶來副作用：對於經過 fast-path 的封裝封包，會繞過防火牆、連線跟蹤、simple queues、parent=global 的 queue tree、IP accounting、IPsec、hotspot universal client、vrf 分配。此外，封包分片無法在 FastPath 中接收。

:::info
可以透過 `/interface/print stats-detail` 驗證是否正在使用 FastPath
:::

唯一能保證 FastPath 的介面佇列是 only-hardware-queue。如果你需要硬體佇列以外的介面佇列，那麼封包將無法完全走 FastPath，但效能影響不大，因為“介面佇列”是封包流程中的最後一步。

封包可能透過從 FastPath 切換到 SlowPath 而走 Half-FastPath，但反過來不行。因此，例如，如果接收介面支援 FastPath，但出介面不支援，那麼路由器會盡可能由 FastPath 處理器處理封包，然後繼續使用 SlowPath。如果接收介面不支援 FastPath，但出介面支援，那麼封包將全程由 SlowPath 處理。

![](/img/4af1f73d77c10a2d.webp)

## FastTrack {#fasttrack}

Fasttrack 可以理解為 Fast Path + Connection Tracking。它允許將連線標記為 "fast-tracked"，屬於 fast-tracked 連線的封包將被標記為走 fast-path 路徑。此類連線的連線表條目現在會帶有 fast-tracked 標誌。

![](/img/aa98e5eb14f84662.webp)

:::warning
FastTrack 封包會繞過防火牆、連線跟蹤、simple queues、parent=global 的 queue tree、ip traffic-flow、IP accounting、IPSec、hotspot universal client、VRF 分配，因此管理員需要確保 FastTrack 不會干擾其他配置！
:::

為了將連線標記為 fast-tracked，為防火牆 filter 和 mangle 實現了一個新動作 "*fasttrack-connection"*。目前，只有 TCP 和 UDP 連線可以被 fast-tracked，並且為了維護連線跟蹤條目，一些隨機封包仍會被送到慢速路徑。在設計啟用 "fasttrack" 的防火牆時必須考慮到這一點。

FastTrack 處理器還支援源 NAT 和目的 NAT，因此不需要為 NAT 連線設定特殊例外。

:::danger
屬於 fast-tracked 連線的流量走 FastPath，這意味著它不會被其他路由器 L3 處理環節（防火牆、佇列、IPsec、IP accounting、VRF 分配等）看到。Fasttrack 查詢路由發生在設定路由標記之前，因此它只適用於 main 路由表。
:::

在家庭路由器上開始使用此功能的最簡單方法是為所有 *established, related* 連線啟用 "fasttrack"：

```ros
/ip/firewall/filter 
add chain=forward action=fasttrack-connection connection-state=established,related \
  comment="fasttrack established/related"
add chain=forward action=accept connection-state=established,related \
  comment="accept established/related"
```

請注意，第一條規則將 established/related 連線標記為 fast-tracked，第二條規則仍然是必需的，用於接受屬於這些連線的封包。原因是，如前所述，來自 fast-tracked 連線的一些隨機封包仍會經過慢速路徑，並且只有 UDP 和 TCP 會被 fast-tracked，但我們仍然希望接受其他協定的封包。

![](/img/eb9e99053f1967f1.webp)![](/img/6940cdf22b657bb5.webp)

新增 "FastTrack" 規則後，列表頂部會出現一條特殊的虛擬規則。這不是實際規則，而是用於直觀顯示部分流量正走 FastPath，不會到達其他防火牆規則。

:::warning
FastTrack 只能在 main 路由表中處理封包，因此係統管理員有責任不要對經過非 main 路由表的連線（即透過 mangle action=mark-routing 規則處理的連線）進行 FastTrack。否則封包可能會透過 main 路由表被錯誤路由。
:::

只要存在至少一個 fast-tracked 連線跟蹤條目，這些規則就會出現；當最後一個 fast-tracked 連線在連線表中超時後，它們就會消失。

:::warning
連線會一直保持 FastTracked 狀態，直到連線關閉、超時或路由器重啟。
:::

#### 配置示例：排除特定主機使其不被 Fast-Tracked {#configuration-example-excluding-specific-host-from-being-fast-tracked}

```ros
/ip/firewall/filter
add action=accept chain=forward connection-state=established,related src-address=192.168.88.111
add action=accept chain=forward connection-state=established,related dst-address=192.168.88.111
add action=fasttrack-connection chain=forward connection-state=established,related hw-offload=no
add action=accept chain=forward connection-state=established,related
```

在此示例中，我們透過首先用防火牆規則接受主機 192.168.88.111（源和目的均接受），將其排除在 Fast-tracked 之外。思路是——不讓該流量到達 FastTrack 動作。

注意："exclusion" 規則必須放在 fasttrack 過濾器之前；順序很重要。

#### 要求 {#requirements}

滿足以下條件時 FastTrack 才會生效：

- 沒有 mesh、metarouter 介面配置。
- 未執行 sniffer、torch 和 traffic generator。
- 未主動使用 `/tool/mac-scan`。
- 未主動使用 `/tool/ip-scan`。
- 在 IP/Settings 下啟用了 FastPath 和 Route cache（route cache 條件不適用於 RouterOS v7 或更新版本）。
- 如果連線經過網橋介面，則必須啟用 Bridge FastPath。

## 面向視障人士的封包流程 {#packet-flow-for-the-visually-impaired}

以下 DOCX 格式文件以針對視障人士最佳化的方式描述了該圖。描述由 Apex CoVantage 提供，由 Benetech 負責。這些描述不再更新。

- [封包流程，最佳化文件。](https://box.mikrotik.com/f/673207754e4d40638fae/?dl=1)
