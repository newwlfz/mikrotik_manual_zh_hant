---
sidebar_key: "firewall-and-quality-of-service/user-guides/ddos-protection"
sidebar_position: 4
title: "DDoS 防護"
sidebar_label: "DDoS 防護"
description: "使用 RouterOS 防火牆規則限制拒絕服務攻擊：使用 dst-limit 按源和目標統計新連線，將超過速率限制的配對放入地址列表，並在 raw 表中丟棄它們。涵蓋檢測的工作原理、其限制、保護路由器本身、使用 TCP SYN cookies 應對 SYN 洪泛，以及為什麼 SYN-ACK 洪泛會作為無效流量被丟棄。"
tags:
  - 'firewall'
  - 'ddos'
  - 'syn-flood'
source: https://manual.mikrotik.com/docs/7.25/firewall-and-quality-of-service/user-guides/ddos-protection
captured_at: '2026-11-04T11:16:11+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

拒絕服務（DoS）或分散式拒絕服務（DDoS）攻擊是一種惡意行為，它透過向目標或其周邊基礎設施傾瀉海量的網際網路流量，試圖擾亂目標伺服器、服務或網路的正常流量。DDoS 攻擊有多種型別，例如 HTTP 洪水、SYN 洪水和 DNS 放大。

![Diagram of a DDoS attack: an attacker controls a botnet of several computers, and all of them send traffic through the gateway to one victim server](/img/d7c46fdda6459931.jpg)

本頁的防火牆規則會統計每個源地址與目標地址之間的新建連線。當某一對地址建立連線的速度超過配置的速率時，兩個地址都會被加入地址列表，raw 表中的一條規則會在連線跟蹤之前丟棄它們之間的流量，從而使洪水攻擊給路由器帶來的開銷儘可能小。

路由器上的任何規則都無法抵禦佔滿網際網路鏈路本身的攻擊：流量到達時已經消耗了頻寬。此類攻擊必須由你的 ISP 在上游進行過濾。

這些規則是對已正確配置的防火牆的補充，而不是替代它。基礎內容請參見[保護你的路由器](../../getting-started/securing-your-router.md)。

## 檢測並丟棄連線洪水 {#detect-and-drop-connection-floods}

```ros
/ip/firewall/filter
add chain=forward action=jump jump-target=detect-ddos \
    connection-state=new
add chain=detect-ddos action=return \
    dst-limit=32,32,src-and-dst-addresses/10s
add chain=detect-ddos action=add-dst-to-address-list \
    address-list=ddos-targets address-list-timeout=10m
add chain=detect-ddos action=add-src-to-address-list \
    address-list=ddos-attackers address-list-timeout=10m
/ip/firewall/raw
add chain=prerouting action=drop \
    src-address-list=ddos-attackers dst-address-list=ddos-targets
```

地址列表不必事先存在：當規則新增第一條條目時，RouterOS 會建立 `ddos-attackers` 和 `ddos-targets`。

在採用預設配置的路由器上，你可以把這條 jump 規則追加到 forward 鏈的末尾。已建立的連線會在鏈中更早的位置被接受，因此只有新建連線會到達這裡：來自 LAN 的連線，以及來自網際網路、被目的 NAT 規則轉發到路由器後方主機的連線。

對於此類埠轉發的服務，raw 規則不會匹配。raw 表在目的 NAT 之前處理封包，因此它看到的目標是路由器的公網地址，而 `ddos-targets` 中儲存的是路由器後方主機的地址。要同時丟棄這些洪水，請新增一條 filter 規則，在 NAT 之後、預設 fasttrack 規則之前丟棄已列入列表的地址對：

```ros
/ip/firewall/filter/add chain=forward action=drop \
    src-address-list=ddos-attackers dst-address-list=ddos-targets \
    comment="drop DDoS pairs after destination NAT" \
    place-before=[find comment="defconf: fasttrack"]
```

### 檢測的工作原理 {#how-the-detection-works}

1. 第一條規則把經過路由器的每個新建連線送入 `detect-ddos` 鏈。
2. 只要該地址對保持在 `dst-limit=32,32,src-and-dst-addresses/10s` 的限制之內，`return` 規則就會把連線送回 forward 鏈。格式為 `rate[/time],burst,mode[/expire]`：
   - `32` - 速率：每秒 32 個新建連線（時間間隔預設為一秒）。
   - `32` - 突發量：一個地址對可以無需等待地建立 32 個連線；額度按速率恢復，最多恢復到突發量。
   - `src-and-dst-addresses` - 每個源地址與目標地址對單獨計數。
   - `10s` - 某個地址對若 10 秒內沒有傳送任何資料，就會被遺忘。
3. 當某個地址對超出限制時，`return` 規則不再匹配。接下來的兩條規則會把目標地址加入 `ddos-targets`，把源地址加入 `ddos-attackers`，有效期均為 10 分鐘。
4. raw 規則會丟棄從任何已列入列表的攻擊者發往任何已列入列表的目標的所有流量，直到條目過期。對於埠轉發的目標，則由上一節的 filter 規則來丟棄。

使用這些規則時，某個源地址以最快速度向某個目標地址發起新建連線，會有略多於 32 個連線透過：突發量加上突發期間速率所允許的連線數。下一個連線會把兩個地址都加入列表，此後 raw 規則就會丟棄它們之間的所有流量。

### 檢測的侷限 {#limits-of-the-detection}

- 速率是按每個源地址與目標地址對計數的。如果來自多個源地址的攻擊各自保持在每秒 32 個新建連線以下，就不會被檢測到。
- 一個繁忙的合法用戶端，例如代理伺服器或某個辦公室的 NAT 閘道器，向同一臺伺服器可能超過每秒 32 個新建連線。請提高速率，或者在 jump 規則之前接受來自此類地址的連線。
- 這些規則只監視轉發的流量（`chain=forward`）。若要同時監視發往路由器自身的連線，請把同樣的 jump 規則新增到 input 鏈：

  ```ros
  /ip/firewall/filter/add chain=input action=jump \
      jump-target=detect-ddos connection-state=new
  ```

### 檢查與解除封鎖 {#check-and-unblock}

列出檢測到的地址對以及每個條目剩餘的時間，並檢視 raw 規則（以及對於埠轉發服務而言的 filter 規則）丟棄了多少封包：

```ros
/ip/firewall/address-list/print where list~"^ddos-"
/ip/firewall/raw/print stats
/ip/firewall/filter/print stats where comment~"DDoS pairs"
```

要釋放某個被誤列入列表的地址，請從兩個列表中刪除它的條目：

```ros
/ip/firewall/address-list/remove \
    [find list~"^ddos-" address=198.51.100.7]
```

## 防禦 SYN 洪水 {#protect-against-syn-floods}

SYN 洪水是一種 DoS 攻擊形式，攻擊者向目標系統連續傳送大量 SYN 請求，試圖消耗足夠的伺服器資源，使系統無法響應合法流量。對於路由器自身的 TCP 服務，請開啟 TCP SYN cookies（預設值為 `no`）：

```ros
/ip/settings/set tcp-syncookies=yes
```

此後，當某個套接字的 SYN 積壓佇列溢位時，RouterOS 會發送 SYN cookie。SYN cookie 是一個包含小型加密雜湊的 SYN-ACK 封包，響應的用戶端會在其 ACK 封包中回顯該雜湊。如果路由器在回覆封包中看不到這個 cookie，就會把該連線視為偽造並丟棄。SYN cookies 會阻止使用 TCP 擴充套件，這可能使某些服務降級，例如 SMTP 中繼。

## SYN-ACK 洪水 {#syn-ack-floods}

SYN-ACK 洪水是一種攻擊方法，它向目標伺服器高速傳送偽造的 SYN-ACK 封包。伺服器需要大量資源來亂序處理這些封包（在通常的 SYN、SYN-ACK、ACK TCP 三次握手之外）。它可能忙於處理攻擊流量，以致無法處理合法流量，攻擊者由此達成 DoS/DDoS 狀態。

不屬於任何已跟蹤連線的 SYN-ACK 具有 `connection-state=invalid`，在 `loose-tcp-tracking=yes`（預設值）時也是如此。此類封包永遠不會到達 `detect-ddos` 鏈，因為該鏈只能看到新建連線。預設配置會在 input 和 forward 鏈中丟棄無效封包；請保留這些規則以阻止 SYN-ACK 洪水。

## 相關主題 {#related-topics}

- [SSH 暴力破解防護](./bruteforce-prevention.md)以相同的方式使用地址列表，保護路由器自身的 SSH 服務免遭密碼猜測。
- [埠敲門](./port-knocking.md)讓管理埠保持關閉，直到用戶端傳送正確的連線嘗試序列。
- [連線跟蹤](../connection-tracking.md)解釋了這些規則所匹配的連線狀態。

關於所有規則屬性，請參見 CLI 參考中的 [`/ip/firewall/filter`](../../cli-reference/ip/firewall/filter/index.md)、[`/ip/firewall/raw`](../../cli-reference/ip/firewall/raw/index.md) 和 [`/ip/settings`](../../cli-reference/ip/settings.md)。
