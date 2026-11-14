---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/traceroute"
sidebar_position: 2
title: "跟蹤路由"
sidebar_label: "跟蹤路由"
description: "RouterOS traceroute 工具：列出到主機的路徑上的路由器，讀取每一跳的丟包和往返統計資訊，找出路徑在何處中斷、形成環路或被過濾，並從 VRF 或選定的源地址進行跟蹤。"
tags:
  - 'traceroute'
source: https://manual.mikrotik.com/docs/7.25/diagnostics-monitoring-and-troubleshooting/traceroute
captured_at: '2026-11-04T11:15:32+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Traceroute 會列出封包在前往遠端主機的途中經過的路由器，並針對每臺路由器顯示它響應了多少個探測包以及響應耗時。可用它來定位連線失敗或變慢的位置：是在你自己的網路中、在 ISP 閘道器處，還是更遠的地方。如果只想測試某臺主機是否有響應，請使用 [ping](./ping.md)。

Traceroute 依賴於 IP 頭中的生存時間（TTL）欄位，該欄位用於防止路由環路：每臺路由器在轉發封包時會將其 TTL 減一，當 TTL 減到零時，路由器丟棄該封包並向傳送方回送一條 ICMP time exceeded 訊息。Traceroute 發出的第一個探測包 TTL 為 1，因此路徑上的第一臺路由器會響應；下一個探測包 TTL 為 2，可以到達第二臺路由器，依此類推，直到探測包到達目的地，由目的地自身響應探測包。

RouterOS 使用 ICMP echo request 作為探測包，最遠探測 30 跳。一輪結束後，它會啟動下一輪，最多每秒一輪，並像 `mtr` 工具那樣為每一跳儲存統計資訊，直到你用 <kbd>Control</kbd>+<kbd>C</kbd> 停止它，或者它已完成 `count` 輪，或已執行滿 `duration`。其他系統有類似的工具：類 Unix 系統上的 `traceroute` 或 `tracepath`，以及 Windows 上的 `tracert`。

## 跟蹤到主機的路徑 {#trace-the-path-to-a-host}

要跟蹤到某臺伺服器的路徑，並進行三輪探測：

```ros
/tool/traceroute 198.51.100.10 count=3
```

```text
Columns: ADDRESS, LOSS, SENT, LAST, AVG, BEST, WORST, STD-DEV
#  ADDRESS        LOSS  SENT  LAST   AVG  BEST  WORST  STD-DEV
0  203.0.113.1    0%       3  0.3ms  0.4  0.3   0.4          0
1  203.0.113.6    0%       3  0.4ms  0.4  0.4   0.4          0
2  198.51.100.10  0%       3  0.5ms  0.5  0.5   0.5          0
```

封包在到達伺服器之前經過兩臺路由器，203.0.113.1 和 203.0.113.6。`#` 列從 0 開始，因此第 0 行是第一跳。每輪結束後表格會原地更新。各列含義如下：

- `ADDRESS` - 為該跳做出響應的路由器的地址：即它傳送響應時使用的地址，通常是指向你這一側的介面地址。
- `LOSS` - 發往該跳的探測包中沒有得到響應的比例。
- `SENT` - 發往該跳的探測包數量。
- `LAST`、`AVG`、`BEST`、`WORST` - 最近一次響應的往返時間，以及平均、最短和最長往返時間，單位為毫秒。當最近一次探測沒有得到響應時，`LAST` 顯示 `timeout`。
- `STD-DEV` - 往返時間的標準差，單位為毫秒：即各輪之間往返時間的波動程度。
- `STATUS` - 當某一跳返回的是錯誤而不是 time exceeded 時顯示，例如防火牆拒絕了該流量。

## 顯示主機名 {#show-host-names}

設定 `use-dns=yes` 後，traceroute 會顯示每一跳的主機名而不是其地址。路由器透過自身的 [DNS 解析器](../network-management/dns.md)以反向 DNS 查詢來解析這些名稱，因此沒有反向 DNS 記錄的那一跳仍會顯示其地址。目的地也可以是主機名：

```ros
/tool/traceroute server.example.com count=3 use-dns=yes
```

```text
Columns: ADDRESS, LOSS, SENT, LAST, AVG, BEST, WORST, STD-DEV
#  ADDRESS                 LOSS  SENT  LAST   AVG  BEST  WORST  STD-DEV
0  edge1.isp.example.net.  0%       3  0.4ms  0.5  0.4   0.5    0
1  core1.isp.example.net.  0%       3  0.4ms  0.5  0.4   0.6    0.1
2  server.example.com.     0%       3  0.6ms  0.6  0.5   0.7    0.1
```

主機名可以顯示出某臺路由器屬於哪個網路或哪個位置。

## 找出路徑中斷的位置 {#find-where-the-path-breaks}

當某臺主機沒有響應時，traceroute 會顯示封包能到達多遠。以下每種輸出展示一種典型結果。

### 後續跳不再響應 {#hops-stop-answering}

```ros
/tool/traceroute 198.51.100.10 count=1 max-hops=4
```

```text
Columns: ADDRESS, LOSS, SENT, LAST, AVG, BEST, WORST, STD-DEV
#  ADDRESS      LOSS  SENT  LAST     AVG  BEST  WORST  STD-DEV
0  203.0.113.1  0%       1  0.4ms    0.4  0.4   0.4          0
1               100%     1  timeout
2               100%     1  timeout
3               100%     1  timeout
```

第一臺路由器有響應，而它之後的都不響應。問題出在最後一臺有響應的跳之後：可能是鏈路中斷、缺少路由、缺少返回你地址的路由（例如你以 `src-address` 設為某個 LAN 地址進行跟蹤，而遠端網路沒有回程路由到該地址），或者是有防火牆在不作響應的情況下丟棄了封包。請檢查路由器 203.0.113.1：檢查它到目的地的路由，以及它到下一跳的鏈路。如果不設定 `max-hops`，跟蹤會繼續以超時狀態進行，最多到 30 跳。

當路徑上的所有路由器都有響應、但目的地本身丟棄了 ICMP echo request 時，也會出現同樣的輸出：最後一臺路由器之後的行保持為空。請對目的地執行 [Ping](./ping.md)，或者當目的地位於直連子網時使用 [ARP ping](./ping.md#find-a-host-that-does-not-answer-ping)。

### 某臺路由器拒絕該流量 {#a-router-rejects-the-traffic}

```ros
/tool/traceroute 198.51.100.10 count=1
```

```text
Columns: ADDRESS, LOSS, SENT, LAST, AVG, BEST, WORST, STD-DEV, STATUS
#  ADDRESS      LOSS  SENT  LAST   AVG  BEST  WORST  STD-DEV  STATUS
0  203.0.113.1  0%       1  0.4ms  0.4  0.4   0.4          0
1  203.0.113.1  0%       1  0.3ms  0.3  0.3   0.3          0  host unreachable from 203.0.113.1
2               0%       0  0ms
```

路由器 203.0.113.1 對第二個探測包返回了錯誤而不是將其轉發，跟蹤就此結束；它之後的那一行空行表示探測包沒有到達的那一跳。`host unreachable from 203.0.113.1` 表示該路由器無法把封包投遞到主機；使用 `reject-with=icmp-host-unreachable` 拒絕封包的防火牆規則會給出相同的響應。`network unreachable from 203.0.113.1` 表示該路由器沒有到目的地網路的路由，或者有防火牆規則以預設的 `reject` 動作拒絕了該封包。`packet filtered from 203.0.113.1` 表示該路由器上的防火牆以 administratively prohibited 為由拒絕了該封包（`reject-with=icmp-admin-prohibited`）；[ping](./ping.md) 會把同樣的響應顯示為 `admin prohibited`。

### 同樣的路由器重複出現 {#the-same-routers-repeat}

```ros
/tool/traceroute 198.51.100.10 count=1 max-hops=8
```

```text
Columns: ADDRESS, LOSS, SENT, LAST, AVG, BEST, WORST, STD-DEV
#  ADDRESS      LOSS  SENT  LAST   AVG  BEST  WORST  STD-DEV
0  203.0.113.1  0%       1  0.4ms  0.4  0.4   0.4          0
1  203.0.113.6  0%       1  0.4ms  0.4  0.4   0.4          0
2  203.0.113.1  0%       1  0.4ms  0.4  0.4   0.4          0
3  203.0.113.6  0%       1  0.6ms  0.6  0.6   0.6          0
4  203.0.113.1  0%       1  0.5ms  0.5  0.5   0.5          0
5  203.0.113.6  0%       1  0.6ms  0.6  0.6   0.6          0
6  203.0.113.1  0%       1  0.7ms  0.7  0.7   0.7          0
7  203.0.113.6  0%       1  0.8ms  0.8  0.8   0.8          0
```

兩臺路由器交替出現：這是一個路由環路。它們各自把目的地路由到對方，因此封包在兩者之間來回轉發，直到 TTL 耗盡。請檢查這兩臺路由器上到目的地的路由。此時對目的地執行 [ping](./ping.md) 會收到其中一臺路由器返回的 `TTL exceeded`，而不是正常回復。

路由器 203.0.113.1 從與來自你這一側的探測包不同的介面上收到來自 203.0.113.6 的環路封包，但它每次都用自己指向你這一側的地址做出響應。

### 某一跳顯示丟包，而後續跳不丟包 {#one-hop-shows-loss-later-hops-do-not}

```ros
/tool/traceroute 198.51.100.10 count=10
```

```text
Columns: ADDRESS, LOSS, SENT, LAST, AVG, BEST, WORST, STD-DEV
#  ADDRESS        LOSS  SENT  LAST     AVG  BEST  WORST  STD-DEV
0  203.0.113.1    0%      10  0.2ms    0.2  0.2   0.4    0.1
1  203.0.113.6    90%     10  timeout  0.4  0.4   0.4    0
2  198.51.100.10  0%      10  0.8ms    0.8  0.5   0.8    0.1
```

路由器 203.0.113.6 在十個探測包中只響應了一個，但所有經過同一臺路由器發往伺服器的探測包都得到了響應。許多路由器會限制其傳送 time exceeded 訊息的頻率，或給這類訊息較低的優先順序，因此沒有延續到後續跳的丟包並不是路徑上的真實丟包。真正的丟包從某一跳開始，並會出現在它之後的每一跳上。完全不傳送 time exceeded 訊息的路由器會顯示為一跳 100% 丟包且無地址，夾在有響應的各跳之間。

### 往返時間增長 {#round-trip-times-grow}

某一跳的往返時間包含從該路由器返回你這一側的路徑。若往返時間在某一跳上升，並在之後的每一跳都保持更高，說明該跳之前存在一條速度慢、距離遠或擁塞的鏈路。若只有某一跳的往返時間偏高或 `STD-DEV` 很大，而其後的時間正常，說明這臺路由器響應慢，而不是經過它的流量慢。

## 找出 MTU 較小的那一跳 {#find-the-hop-with-the-smaller-mtu}

使用 `do-not-fragment` 並設定較大的 `size` 後，探測包無法被分片，而必須把這些包轉發到 MTU 較小鏈路上的路由器會改為返回錯誤：

```ros
/tool/traceroute 198.51.100.10 size=1500 do-not-fragment count=1
```

```text
Columns: ADDRESS, LOSS, SENT, LAST, AVG, BEST, WORST, STD-DEV, STATUS
#  ADDRESS      LOSS  SENT  LAST   AVG  BEST  WORST  STD-DEV  STATUS
0  203.0.113.1  0%       1  0.5ms  0.5  0.5   0.5          0
1  203.0.113.6  0%       1  0.6ms  0.6  0.6   0.6          0
2  203.0.113.6  0%       1  0.6ms  0.6  0.6   0.6          0  fragmentation needed from 203.0.113.6
3               0%       0  0ms
```

路由器 203.0.113.6 上有較小的鏈路。要找出路徑的 MTU，請參閱 ping 頁面中的 [查詢路徑 MTU](./ping.md#find-the-path-mtu)。

## 從 VRF 或指定源地址進行跟蹤 {#trace-from-a-vrf-or-a-specific-source}

預設情況下，traceroute 使用主路由表、以出口介面的地址傳送探測包。在運營商路由器上，客戶網路通常位於 [VRF](../user-guides/routing-and-networking-protocols/vrf.md) 中；`vrf` 會跟蹤客戶流量所走的路徑：

```ros
/tool/traceroute 198.51.100.10 vrf=customer1
```

`vrf` 只接受 VRF。為策略路由建立的路由表不是 VRF，命令會拒絕它。

要按某個特定網路所看到的流量路徑進行跟蹤，例如從 LAN 地址而不是 WAN 地址出發，請設定探測包的源地址。匹配該源地址的[路由規則](../user-guides/routing-and-networking-protocols/policy-routing.md)也會作用於探測包，因此 `src-address` 也能跟蹤策略路由表所走的路徑：

```ros
/tool/traceroute 198.51.100.10 src-address=192.168.88.1
```

`interface` 會從某一個介面發出探測包。當該介面上沒有覆蓋目的地的路由時，路由器會把目的地視為該介面上的直連地址併為其傳送 ARP 請求，因此跟蹤只會一直超時。

## 技術細節 {#technical-details}

### 探測包 {#probes}

- 探測包是 ICMP echo request。`size` 是整個 IP 包的大小：預設的 28 位元組是一個 IPv4 頭加一個不帶任何負載的 ICMP 頭。
- 一輪中的第一個探測包 TTL 為 1，之後每個探測包依次加一。一個探測包最多等待 `timeout`（預設 1 秒）以獲得響應；一旦響應到達或超時時間到，就立即傳送下一個探測包。
- 當目的地做出響應、某臺路由器返回 destination unreachable 訊息，或已發出 `max-hops`（預設 30）個探測包時，該輪結束。下一輪在該輪結束後開始，最早在上一輪開始後一秒。
- 使用 `protocol=udp` 時，探測包是發往 `port`（預設 33434）的 UDP 封包。目的埠對每個探測包都相同；源埠則逐跳變化。目的地會以 ICMP port unreachable 訊息代替 echo reply 做出響應。

### WinBox 和 WebFig 中的主機名 {#host-names-in-winbox-and-webfig}

當你在 WinBox 4 或 WebFig 的 Tools > Traceroute 中輸入主機名時，路由器會使用自身的 [DNS 解析器](../network-management/dns.md)解析該名稱。WinBox 3 則在其執行所在的計算機上解析該名稱。

有關所有引數，請參閱 CLI 參考中的 [`/tool/traceroute`](../cli-reference/tool/traceroute.md)。
