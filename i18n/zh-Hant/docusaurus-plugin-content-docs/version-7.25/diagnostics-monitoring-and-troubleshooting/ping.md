---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/ping"
sidebar_position: 1
title: "Ping"
sidebar_label: "Ping"
description: "RouterOS ping 工具：檢查主機或網際網路是否可達，讀取每個回覆的狀態，查詢路徑 MTU，從選定的地址、介面或 VRF 發起 ping，使用 ARP 和 ND ping 訪問阻止 ICMP 的主機，發現 IPv6 主機，ping MAC 地址，並在指令碼中使用 ping。"
tags:
  - 'icmp'
  - 'ping'
source: https://manual.mikrotik.com/docs/7.25/diagnostics-monitoring-and-troubleshooting/ping
captured_at: '2026-11-04T11:15:28+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Ping 檢查主機是否響應以及響應需要多長時間。路由器向主機發送 Internet Control Message Protocol (ICMP) 回顯請求（型別 8），主機則用回顯應答（型別 0）逐一回應。請求與其應答之間的時間就是往返時間。如果某個請求的應答未在 `interval`（預設 1 秒）內到達，則會報告為超時。

每個應答還會顯示其生存時間（TTL）。每臺轉發封包的路由器都會將其 TTL 減一，TTL 耗盡的封包會被丟棄。TTL 列顯示應答到達時的 TTL，因此它大致說明應答經過了多少臺路由器：大多數系統以 TTL 64、128 或 255 傳送，所以到達時 TTL 為 62 的應答經過了兩臺路由器。路由器傳送自己的請求時使用 TTL 255（IPv4）或跳數限制 64（IPv6）。

`/ping` 是 `/tool/ping` 的簡寫形式。要查明封包在路徑上的何處停止，請使用 [跟蹤路由](./traceroute.md)。

## 檢查主機是否可達 {#check-that-a-host-is-reachable}

要檢查網際網路連線，請先 ping 一個公共地址，然後 ping 一個名稱：

```ros
/ping 1.1.1.1 count=3
```

```text
  SEQ HOST                                     SIZE TTL TIME       STATUS
    0 1.1.1.1                                    56  60 1ms45us
    1 1.1.1.1                                    56  60 1ms89us
    2 1.1.1.1                                    56  60 1ms163us
    sent=3 received=3 packet-loss=0% min-rtt=1ms45us avg-rtt=1ms99us max-rtt=1ms163us
```

```ros
/ping mikrotik.com count=3
```

```text
  SEQ HOST                                     SIZE TTL TIME       STATUS
    0 159.148.172.205                            56  55 1ms582us
    1 159.148.172.205                            56  55 1ms450us
    2 159.148.172.205                            56  55 1ms513us
    sent=3 received=3 packet-loss=0% min-rtt=1ms450us avg-rtt=1ms515us max-rtt=1ms582us
```

路由器使用自己的 [DNS](../network-management/dns.md) 設定解析名稱。當地址有應答而名稱沒有時，說明連線正常，問題出在 DNS 配置。無法解析的名稱會失敗並顯示 `failure: resolve failed`；請參閱 DNS 頁面上的 [檢查與故障排除](../network-management/dns.md#check-and-troubleshoot)。在 [WinBox](../management-tools/winbox.md) 4 和 [WebFig](../management-tools/webfig.md) 中，Tools > Ping 會把名稱傳送給路由器，由路由器也使用其 DNS 進行解析；WinBox 3 則在其執行的計算機上解析名稱。

每一行代表一個應答：

- `SEQ` - 該行所應答請求的編號。
- `HOST` - 應答來自的地址：主機，或路徑上傳送錯誤的路由器。
- `SIZE` - 接收封包的大小，以位元組為單位。
- `TTL` - 接收封包的 TTL。
- `TIME` - 往返時間。
- `STATUS` - IPv4 應答為空，IPv6 應答為 `echo reply`；否則表示出錯原因。

最後一行彙總本次執行：傳送的請求數、收到的應答數、丟失請求的比例，以及最短、平均和最長往返時間。如果不指定 `count`，ping 會一直執行，直到你用 <kbd>Control</kbd>+<kbd>C</kbd> 停止它。

## 讀取狀態列 {#read-the-status-column}

| 狀態 | 含義 |
| :-- | :-- |
| `timeout` | 在 `interval` 內沒有應答到達。主機宕機、不響應 ping、路徑上的防火牆丟棄請求或應答，或者往返時間長於 `interval`。 |
| `net unreachable` | `HOST` 中顯示的路由器沒有通往目標網路的路由，或者那裡的防火牆規則使用預設 `reject` 動作拒絕該封包。 |
| `host unreachable` | `HOST` 中顯示的路由器報告無法到達該主機，或者那裡的防火牆規則使用 `reject-with=icmp-host-unreachable` 拒絕該封包。 |
| `admin prohibited` | `HOST` 中顯示的路由器上的防火牆規則使用 `reject-with=icmp-admin-prohibited` 拒絕該封包。Traceroute 會將同樣的應答顯示為 `packet filtered`。 |
| `TTL exceeded` | TTL 在 `HOST` 中顯示的路由器上耗盡。通常是路由環路。 |
| `fragmentation needed and DF set` | `HOST` 中顯示的路由器必須透過 MTU 更小的鏈路轉發該封包，而 Don't Fragment 標誌阻止了這樣做。 |
| `packet too large and cannot be fragmented` | 封包大於出介面的 MTU，或大於路由器已學習到的路徑 MTU，並且已設定 Don't Fragment 標誌。 |
| `no route to host` | 路由器沒有通往該地址的路由。對於 ND ping，該地址不在直連子網上。 |
| `echo reply` | IPv6 回顯應答。IPv4 應答的狀態列留空。 |

路由環路會讓封包在兩臺路由器之間來回傳送，直到其 TTL 耗盡。TTL 最先耗盡的路由器會報告該情況：

```ros
/ping 198.51.100.10 count=2
```

```text
  SEQ HOST                                     SIZE TTL TIME       STATUS
    0 203.0.113.1                                84  64 20ms894us  TTL exceeded
    1 203.0.113.1                                84  64 20ms404us  TTL exceeded
    sent=2 received=0 packet-loss=100%
```

## 查詢路徑 MTU {#find-the-path-mtu}

當路徑上某條鏈路的 MTU（最大傳輸單元）比其周圍鏈路更小（例如 PPPoE 連線或隧道）時，小封包能透過，大封包會丟失：ping 正常，但網頁只能部分載入，檔案傳輸會停滯。要找出能穿過該路徑的最大封包，請使用 Don't Fragment 標誌進行 ping。先從 1500 開始，PPPoE 連線則從 1492 開始，然後降低 `size`，直到有應答到達：能收到應答的最大大小就是路徑 MTU。

`size` 是整個 IP 封包的大小，包括 IP 頭。`size=1500` 是乙太網鏈路上的全尺寸封包，相當於 Windows 上的 `ping -l 1472` 和 Linux 上的 `ping -s 1472`，後者只計算資料部分。對於 IPv6，頭部為 40 位元組，因此 `size=1500` 相當於 `ping -s 1452`。

```ros
/ping 198.51.100.10 size=1500 do-not-fragment count=2
```

```text
  SEQ HOST                                     SIZE TTL TIME       STATUS
    0 203.0.113.6                               576  63 893us      fragmentation needed and DF set
    1                                                              packet too large and cannot be fragmented
    sent=2 received=0 packet-loss=100%
```

203.0.113.6 處的路由器連線著 MTU 更小的鏈路，並用 `fragmentation needed and DF set` 應答第一個請求；`SIZE` 576 是該錯誤訊息的大小，而不是 MTU。該訊息會告知路由器該鏈路的 MTU，路由器會在一段時間內將其記為此目標的路徑 MTU：隨後更大的 ping 會立即失敗並顯示 `packet too large and cannot be fragmented`，而不會離開路由器。當 `size` 大於出介面的 MTU 時，也會出現相同的狀態。

```ros
/ping 198.51.100.10 size=1401 do-not-fragment count=1
```

```text
  SEQ HOST                                     SIZE TTL TIME       STATUS
    0                                                              packet too large and cannot be fragmented
    sent=1 received=0 packet-loss=100%
```

```ros
/ping 198.51.100.10 size=1400 do-not-fragment count=2
```

```text
  SEQ HOST                                     SIZE TTL TIME       STATUS
    0 198.51.100.10                            1400  62 1ms347us
    1 198.51.100.10                            1400  62 1ms41us
    sent=2 received=2 packet-loss=0% min-rtt=1ms41us avg-rtt=1ms194us max-rtt=1ms347us
```

1400 是能收到應答的最大大小：路徑 MTU 為 1400 位元組。如果不使用 `do-not-fragment`，更大的 ping 會被分片並收到應答，因此不會顯示 MTU 問題。當路徑上的防火牆丟棄“需要分片”訊息時，超過路徑 MTU 的 ping 只會超時。

要檢視路徑上哪臺路由器連線著更小的鏈路，請執行 [帶 `do-not-fragment` 的 traceroute](./traceroute.md#find-the-hop-with-the-smaller-mtu)。要讓 TCP 連線跨越此類鏈路正常工作，請使用 [mangle 規則](../firewall-and-quality-of-service/firewall/mangle.md#change-mss) 鉗制 TCP MSS。

## 從指定地址、介面或 VRF 執行 Ping {#ping-from-a-specific-address-interface-or-vrf}

預設情況下，路由器會像處理其他流量一樣選擇源地址：如果路由設定了 `pref-src`，則使用該值，否則使用出介面的地址。測試所需的地址並不總是這個地址。例如，[IPsec](../virtual-private-networks/ipsec/index.md) 站點到站點隧道只承載兩個 LAN 之間的流量：從路由器 WAN 地址向遠端 LAN 傳送的 ping 不匹配 IPsec 策略，因此不會進入隧道。要測試隧道，請從路由器的 LAN 地址執行 ping：

```ros
/ping 192.168.2.10 src-address=192.168.88.1 count=3
```

`interface=` 設定請求離開時所經過的介面。當沒有經過該介面且覆蓋目標的路由時，路由器會把目標視為該介面上直連，併為其傳送 ARP 請求。ARP ping、發往全域性地址的 ND ping，以及發往 IPv6 鏈路本地地址的 ping 都需要 `interface=`。

`vrf=` 會在 [VRF](../user-guides/routing-and-networking-protocols/vrf.md) 中傳送 ping：

```ros
/ping 10.0.0.1 vrf=customer1 count=3
```

只接受 VRF。為策略路由而存在的路由表不是 VRF，ping 會被拒絕並顯示 `input does not match any value of vrf`。要測試這樣的表，請將 `src-address` 設定為某個地址，使 [路由規則](../user-guides/routing-and-networking-protocols/policy-routing.md) 將該地址傳送到該表：這些規則適用於路由器自身的 ping。

## 查詢不響應 ping 的主機 {#find-a-host-that-does-not-answer-ping}

許多主機會丟棄 ICMP 回顯請求，例如啟用了防火牆的計算機，因此正常工作的主機可能看起來像是宕機：

```ros
/ping 192.168.88.20 count=2
```

```text
  SEQ HOST                                     SIZE TTL TIME       STATUS
    0 192.168.88.20                                                timeout
    1 192.168.88.20                                                timeout
    sent=2 received=0 packet-loss=100%
```

與路由器在同一子網中的主機仍必須應答 ARP，否則它無法接收任何流量。使用 `arp-ping=yes` 時，路由器傳送 ARP 請求而不是 ICMP 回顯請求，`HOST` 會顯示做出應答的主機的 MAC 地址。ARP ping 適用於直連子網上的 IPv4 地址，並且需要 `interface=`，即在該子網上具有路由器地址的介面（預設配置中為 `bridge`）；如果不指定，ping 會失敗並顯示 `interface needs to be specified for arp ping`。

```ros
/ping 192.168.88.20 arp-ping=yes interface=bridge count=2
```

```text
  SEQ HOST                                     SIZE TTL TIME       STATUS
    0 FE:14:80:BE:47:5B                                 386us
    1 FE:14:80:BE:47:5B                                 346us
    sent=2 received=2 packet-loss=0% min-rtt=346us avg-rtt=366us max-rtt=386us
```

要查明哪個裝置具有該 MAC 地址，請在 [DHCP 伺服器租約](../network-management/dhcp/server.md#leases) 中查詢，或檢視裝置標籤。

對於 IPv6，`nd-ping=yes` 透過鄰居發現實現相同的功能：路由器傳送鄰居請求（NS）而不是 ICMPv6 回顯請求，並將鄰居通告（NA）計為應答。它可確認主機存在且鄰居發現正常工作，即使主機上過濾或關閉了 ICMPv6 回顯。ND ping 僅適用於直連 IPv6 子網上的地址；其他子網上的地址會返回 `no route to host` 錯誤。全域性地址需要 `interface=`，否則 ping 會失敗並顯示 `interface needs to be specified for ND ping`；鏈路本地地址在其 `%interface` 字尾中帶有介面：

```ros
/ping fe80::fc14:80ff:febe:475b%ether1 nd-ping=yes count=2
```

```text
  SEQ HOST                                     SIZE TTL TIME       STATUS
    0 fe80::fc14:80ff:febe:475b                         622us
    1 fe80::fc14:80ff:febe:475b                         581us
    sent=2 received=2 packet-loss=0% min-rtt=581us avg-rtt=601us max-rtt=622us
```

```ros
/ping 2001:db8:0:1::2 nd-ping=yes interface=ether1
```

在 WinBox 中，Tools > Ping 在 ARP Ping 旁邊有一個 ND Ping 複選框，並帶有一個介面選擇器。

## 發現鏈路上的 IPv6 主機 {#discover-ipv6-hosts-on-a-link}

大多數 IPv6 主機會應答傳送到全節點組播地址 `ff02::1` 的回顯請求；防火牆丟棄此類請求的主機則不會。在某個介面上 ping 該地址，可列出該鏈路上的 IPv6 主機：

```ros
/ping ff02::1%ether1 count=2
```

```text
  SEQ HOST                                     SIZE TTL TIME       STATUS
    0 fe80::fc89:f0ff:fe95:7d86                  56  64 395us      echo reply
    0 fe80::fc14:80ff:febe:475b                  56  64 1ms87us    echo reply
    sent=1 received=2 packet-loss=-100% min-rtt=395us avg-rtt=741us max-rtt=1ms87us
```

所有主機都會應答同一個請求，因此多行會共享同一個 `SEQ`，並且列表中包含路由器在該介面上的自身地址。每個應答都會計入 `count` 和彙總行，因此彙總行顯示的應答數會多於請求數。

## Ping 一個 MAC 地址 {#ping-a-mac-address}

MAC ping 可在同一二層網段上，無需 IP 配置，透過 MAC 地址訪問 MikroTik 裝置。當目標的 MAC ping 伺服器啟用時（預設已啟用），目標會做出應答（請參閱 [MAC 伺服器](../management-tools/mac-server.md)）：

```ros
/tool/mac-server/ping/set enabled=yes
```

Ping 該 MAC 地址，並在 `%` 後指定介面：

```ros
/ping FE:14:80:BE:47:5B%ether1 count=2
```

```text
  SEQ HOST                                     SIZE TTL TIME       STATUS
    0 FE:14:80:BE:47:5B                          70     775us
    1 FE:14:80:BE:47:5B                          70     579us
    sent=2 received=2 packet-loss=0% min-rtt=579us avg-rtt=677us max-rtt=775us
```

如果沒有 `%interface` 字尾，路由器會從每個介面發出每個請求。這會增加所有介面上的流量，並且當目標可透過多個介面到達時會返回重複應答。

## 在指令碼中使用 ping {#use-ping-in-a-script}

在指令碼中，ping 返回其收到的應答數：

```ros
:if ([/ping 198.51.100.10 count=3] = 0) do={
    :log warning "Server 198.51.100.10 does not answer"
}
```

當地址是無法解析的名稱時，ping 會失敗並顯示 `resolve failed`，並停止指令碼；將它放入 `:do { ... } on-error={ ... }` 中以處理這種情況。要定期執行該檢查，請將指令碼新增到 [排程器](../system-information-and-utilities/scheduler.md)。

使用 `as-value` 時，ping 會為每個應答返回一個條目，包含應答的 `host`、`seq`、`size`、`ttl` 和 `time`，失敗時則包含其 `status`。要持續監視主機並在其宕機或恢復時執行指令碼，請使用 [網路監控](./netwatch.md)，而不是定時 ping。

## 技術細節 {#technical-details}

### 封包大小 {#packet-size}

`size` 設定整個封包的大小，包括 IP 頭：IPv4 為 28 到 65535 位元組，IPv6 為 48 到 65535 位元組（更小的 IPv6 大小會失敗並顯示 `packet size is too small`），預設 56。大於出介面 MTU 的封包會被分片，除非設定了 `do-not-fragment`。`SIZE` 列顯示接收封包的大小；對於來自路由器的錯誤訊息，該值為該訊息的大小（本頁示例中為 576 和 84）。

### 間隔與計數 {#interval-and-count}

路由器每隔 `interval` 傳送一個請求，範圍為 10 ms 到 5 s，預設 1 s。晚於 `interval` 到達的應答會被計為超時，因此在往返時間較長的鏈路上（例如衛星鏈路或擁塞的移動鏈路），請將 `interval` 提高到往返時間以上。如果不指定 `count`，它會持續傳送請求，直到你停止它。

### TTL 與跳數限制 {#ttl-and-hop-limit}

`ttl` 設定 IPv4 請求的 TTL 和 IPv6 請求的跳數限制，範圍為 1 到 255。如果不指定，IPv4 請求以 TTL 255 發出，IPv6 請求以跳數限制 64 發出。

### DSCP {#dscp}

`dscp` 設定請求 IP 頭中的差異化服務程式碼點，範圍為 0 到 63。`dscp=46`（Expedited Forwarding）會得到 `0xb8` 的 ToS 位元組。可用它檢查路徑如何處理某個 QoS 類別的流量。

### 鏈路本地地址 {#link-local-addresses}

IPv6 鏈路本地地址（`fe80::/10`）存在於每條鏈路上，因此需要以介面作為字尾：`fe80::1%ether1`。

有關所有引數，請參閱 [`/tool/ping` CLI 參考](../cli-reference/tool/ping.md)。
