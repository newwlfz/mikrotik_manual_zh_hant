---
sidebar_key: "high-availability-solutions/load-balancing/per-connection-classifier"
sidebar_position: 2
title: "每連線分類器"
sidebar_label: "每連線分類器"
description: "MikroTik RouterOS 中的每連線分類器（PCC）使用源/目標地址和埠等 IP 報頭欄位將流量劃分為流，並透過雜湊進行負載均衡，從而將連線分佈到各鏈路上。"
tags:
  - 'per-connection-classifier'
  - 'packet-matching'
  - 'hashing'
source: https://manual.mikrotik.com/docs/high-availability-solutions/load-balancing/per-connection-classifier
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

PCC 匹配器允許你將流量劃分為均等的流，並能夠將具有特定選項集的報文保留在同一個特定流中（你可以從 src-address、src-port、dst-address、dst-port 中指定這組選項）

### 理論 {#theory}

PCC 從 IP 頭中提取選定欄位，並在雜湊演算法的幫助下將選定欄位轉換為一個 32 位值。然後將該值除以指定的 *Denominator*，再把餘數與指定的 *Remainder* 進行比較；如果相等，則捕獲該報文。你可以從頭部中選擇 src-address、dst-address、src-port、dst-port 用於此操作。

:::danger
在 Hotspot（強制門戶）場景下，PCC 不是有效方法——因為目前 Hotspot 使用 web-proxy，而且它只使用預設路由表。

:::

```ros
per-connection-classifier=
PerConnectionClassifier ::= [!]ValuesToHash:Denominator/Remainder
  Remainder ::= 0..4294967295    (integer number)
  Denominator ::= 1..4294967295    (integer number)
  ValuesToHash ::= both-addresses|both-ports|dst-address-and-port|
  src-address|src-port|both-addresses-and-ports|dst-address|dst-port|src-address-and-port 
```

### 示例 {#example}

此配置將根據源地址和埠把所有連線分為 3 組

```ros
/ip/firewall/mangle/add chain=prerouting action=mark-connection \
 new-connection-mark=1st_conn per-connection-classifier=src-address-and-port:3/0
/ip/firewall/mangle/add chain=prerouting action=mark-connection \
  new-connection-mark=2nd_conn per-connection-classifier=src-address-and-port:3/1
/ip/firewall/mangle/add chain=prerouting action=mark-connection \
  new-connection-mark=3rd_conn per-connection-classifier=src-address-and-port:3/2
```

### PCC 的工作原理 {#how-pcc-works}

本文旨在用簡單的語言解釋 PCC 如何工作。官方手冊 wiki 頁面中的定義寫道：“PCC 從 IP 頭中提取選定欄位，並在雜湊演算法的幫助下將選定欄位轉換為一個 32 位值。然後將該值除以指定的 Denominator，再把餘數與指定的 Remainder 進行比較；如果相等，則捕獲該報文。你可以從頭部中選擇 src-address、dst-address、src-port、dst-port 用於此操作。”，可用欄位的完整列表為：“both-addresses|both-ports|dst-address-and-port|src-address|src-port|both-addresses-and-ports|dst-address|dst-port|src-address-and-port”。如果你理解那個定義，這篇文章對你來說就沒有什麼有趣的內容。

首先，以下是理解該定義所必需的術語。

IP 報文有一個包含若干欄位的頭部。其中兩個欄位是報文的源 IP 地址和報文的目的 IP 地址。TCP 和 UDP 報文也有包含源埠和目的埠的頭部。

分母和餘數是取模運算的組成部分。取模運算會在你將兩個數相除時產生剩下的整數，並且只取結果的整數部分。它用 % 符號表示。下面是一些例子：3 % 3 = 0，因為 3 能被 3 整除。4 % 3 = 1，因為 4 之前能被 3 整除的最大數是 3，且 4 - 3 = 1。5 % 3 是 2，因為 5 之前能被 3 整除的最大數是 3，且 5 - 3 = 2。6 % 3 = 0，因為 6 能被 3 整除。

雜湊是一種接收輸入併產生輸出的函式。雜湊具有許多有趣的特性，但本文唯一重要的是雜湊函式具有確定性。這意味著，當你給雜湊函式輸入 'hello' 並得到輸出 '1' 時，你可以相信，如果你再次輸入 'hello'，它還會產生輸出 '1'。當你給雜湊函式相同的輸入時，它總是會產生相同的輸出。PCC 使用哪種確切的雜湊演算法並不重要，因此在本討論中，我們假設當你給它輸入 IP 地址和埠時，它只是把 IP 地址的各個八位組按十進位制數相加，同時也加上埠，然後取最後一位數字作為輸出。下面是一個例子：

給雜湊函式輸入 1.1.1.1 作為源 IP 地址、10000 作為源 TCP 埠、2.2.2.2 作為目的 IP 地址、80 作為目的 TCP 埠。輸出將是 1+1+1+1+10000+2+2+2+2+80 = 10092。最後一位是 2，因此雜湊輸出為 2。每次給它輸入這組 IP 地址和埠時，它都會產生 2。

此時需要注意，儘管 PCC 最常用於在多個線路之間分攤負載，但 PCC 本身與路由、路由標記或分攤負載完全無關。PCC 只是一種匹配報文的方式，並不直接與隨後標記這些匹配報文的動作相關，即使那才是它的主要用途。

以下是常用於 PCC 的三行配置及其解釋：

```ros
/ip/firewall/mangle/add chain=prerouting action=mark-connection \
 new-connection-mark=1st_conn per-connection-classifier=src-address-and-port:3/0
/ip/firewall/mangle/add chain=prerouting action=mark-connection \
  new-connection-mark=2nd_conn per-connection-classifier=src-address-and-port:3/1
/ip/firewall/mangle/add chain=prerouting action=mark-connection \
  new-connection-mark=3rd_conn per-connection-classifier=src-address-and-port:3/2
```

下面說明不同欄位選項在報文匹配中的含義；這些欄位將被送入雜湊演算法（並且，就在多條鏈路之間分攤負載而言，會決定報文將被放到哪條鏈路上）。請記住，當給雜湊函式相同的輸入時，它總是會產生相同的輸出：

- src-address：用戶端的源地址始終相同，因此來自某個特定用戶端的所有流量將始終匹配同一個 PCC 匹配器，並始終被放到同一條鏈路上。
- dst-address：特定伺服器的目的地址始終相同，因此發往該伺服器（例如 Mikrotik Wiki）的所有流量將始終匹配同一個 PCC 匹配器，並始終被放到同一條鏈路上。
- both-addresses：同一用戶端與伺服器之間的源 IP 和目的 IP 對始終相同，因此某個特定用戶端與特定伺服器（例如你的筆記型電腦和 Mikrotik Wiki）之間的所有流量將始終匹配同一個 PCC 匹配器，並始終被放到同一條鏈路上。
- src-port：用戶端源埠通常在建立連線時隨機選擇，因此在許多連線中，不同的源埠會被送入雜湊函式，不同的 PCC 匹配器會匹配，流量會走不同鏈路。但是，某些用戶端協定總是選擇相同的源埠，而你路由器後面的伺服器很可能總是使用相同的服務埠向它們的用戶端傳送流量。你路由器後面的 Web 伺服器會從其 HTTP (80) 和 HTTPS (443) 埠傳送大部分流量，而這些流量將始終匹配同一個 PCC 匹配器，並被放到同一條鏈路上。
- dst-port：用戶端的目的埠通常是定義明確的服務埠，你的用戶端與 Internet 上的伺服器之間的所有 HTTP (80) 流量將始終匹配同一個 PCC 匹配器，並被放到同一條鏈路上。但是，同一批用戶端進行 HTTPS (443) 流量時可能匹配不同的 PCC 匹配器，並會走不同的鏈路。
- both-ports：由於用戶端埠（通常）是隨機選擇的，兩個埠的組合（通常）也是隨機的，從而會在多條鏈路之間分攤負載。
- src-address-and-port：與 src-port 相同的注意事項。
- dst-address-and-port：與 dst-port 相同的注意事項。
- both-addresses-and-ports：這是在多條鏈路之間分攤流量最隨機的方式，因為它包含的變數數量最多。

需要注意的是，儘管本文討論的雜湊函式經過大幅簡化，並不是現實中使用的函式，但它很好地展示了雜湊函式的另一個特性：兩個完全不同的輸入可能產生相同的輸出。在我們的例子中，3 % 3 = 0，且 6 % 3 = 0；當我們給它輸入 3 時得到 0，給它輸入 6 時也得到 0。PCC 實際使用的函式也是如此，儘管我不知道它具體是什麼，但從定義可知它會輸出一個 32 位值。IP 地址是 32 位，埠是 16 位，因此假設我們使用 both-addresses-and-ports，我們給它輸入 32+32+16+16 = 96 位，卻只收到 32 位輸出，所以它必然會對不同輸入產生相同輸出。這意味著兩個完全無關的連線可能匹配同一個 PCC 匹配器，並被放到同一條線路上。你讓經過 PCC 的連線越多，雜湊函式就越有機會產生不同輸出，PCC 的效果也就越好。

### 配置示例 {#configuration-example}

假設使用以下配置：

![](/img/a70a4d47aaab6e28.webp)

### IP 地址 {#ip-addresses}

```ros
/ip/address
add address=10.10.4.100/24 interface=ether_ISP1 network=10.10.4.0
add address=10.10.5.100/24 interface=ether_ISP2 network=10.10.5.0
add address=192.168.100.1/24 interface=ether_LAN network=192.168.100.0
```

路由器有兩個上游（ISP）介面，地址分別為 10.10.4.100/24 和 10.10.5.100/24。LAN 介面的 IP 地址為 192.168.100.1/24。

我們新增兩個新的路由表，稍後將使用它們：

```ros
/routing/table
add disabled=no fib name=ISP1_table
add disabled=no fib name=ISP2_table
```

### 策略路由 {#policy-routing}

```ros
/ip/firewall/mangle
add action=accept chain=prerouting dst-address=10.10.4.0/24 in-interface=ether_LAN
add action=accept chain=prerouting dst-address=10.10.5.0/24 in-interface=ether_LAN
```

透過策略路由，可以強制所有流量發往特定閘道器，即使流量是從直連網路發往該閘道器以外的主機。這樣會產生路由環路，並且將無法與這些主機通訊。為避免這種情況，我們需要允許發往連線網路的流量使用預設路由表。

```ros
add action=mark-connection chain=input connection-state=new in-interface=ether_ISP1 new-connection-mark=ISP1
add action=mark-connection chain=input connection-state=new in-interface=ether_ISP2 new-connection-mark=ISP2

add action=mark-connection chain=output connection-mark=no-mark connection-state=new new-connection-mark=ISP1 per-connection-classifier=both-addresses:2/0
add action=mark-connection chain=output connection-mark=no-mark connection-state=new new-connection-mark=ISP2 per-connection-classifier=both-addresses:2/1
```

首先，必須管理從外部發起的連線——回覆必須透過請求進入時所用的同一介面（使用同一公網 IP）離開。我們將標記所有新的傳入連線，以記住使用的是哪個介面。

```ros
add action=mark-connection chain=prerouting connection-mark=no-mark connection-state=new dst-address-type=!local in-interface=ether_LAN new-connection-mark=ISP1 per-connection-classifier=both-addresses:2/0
add action=mark-connection chain=prerouting connection-mark=no-mark connection-state=new dst-address-type=!local in-interface=ether_LAN new-connection-mark=ISP2 per-connection-classifier=both-addresses:2/1
```

mark-routing 動作只能在 mangle 的 output 和 prerouting 鏈中使用，但 mangle 的 prerouting 鏈會捕獲所有發往路由器本身的流量。為避免這種情況，我們將使用 dst-address-type=!local。並且藉助新的 PCC，我們將根據源地址和目的地址把流量分為兩組。

```ros
add action=mark-routing chain=output connection-mark=ISP1 new-routing-mark=ISP1_table
add action=mark-routing chain=prerouting connection-mark=ISP1 in-interface=ether_LAN new-routing-mark=ISP1_table

add action=mark-routing chain=output connection-mark=ISP2 new-routing-mark=ISP2_table
add action=mark-routing chain=prerouting connection-mark=ISP2 in-interface=ether_LAN new-routing-mark=ISP2_table
```

然後，我們需要用適當的標記來標記來自這些連線的所有報文。由於只有發往 Internet 的流量才需要策略路由，請不要忘記指定 in-interface 選項。

```ros
/ip/route
add check-gateway=ping disabled=no dst-address=0.0.0.0/0 gateway=10.10.4.1 routing-table=ISP1_table suppress-hw-offload=no
add check-gateway=ping disabled=no dst-address=0.0.0.0/0 gateway=10.10.5.1 routing-table=ISP2_table suppress-hw-offload=no
```

為每個 routing-mark 建立一條路由

```ros
add distance=1 dst-address=0.0.0.0/0 gateway=10.10.4.1
add distance=2 dst-address=0.0.0.0/0 gateway=10.10.5.1
```

要啟用故障轉移，必須要有這樣的路由：當其他路由因閘道器故障而變為非活動狀態時，它們會立即接管。（並且只有在 check-gateway 選項處於活動狀態時才會發生這種情況）

### NAT {#nat}

```ros
/ip/firewall/nat
add action=masquerade chain=srcnat out-interface=ether_ISP1
add action=masquerade chain=srcnat out-interface=ether_ISP2
```

由於路由決策已經完成，我們只需要規則來為所有出站報文修正源地址。如果該報文透過 ether\_ISP1 離開，它將被 NAT 為 10.10.4.100；如果透過 ether\_ISP2 離開，則被 NAT 為 10.10.5.100
