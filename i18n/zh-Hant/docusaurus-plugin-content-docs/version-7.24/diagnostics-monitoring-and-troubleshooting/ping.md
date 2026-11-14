---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/ping"
sidebar_position: 1
title: "Ping"
sidebar_label: "Ping"
description: "本頁面介紹 MikroTik RouterOS 的 Ping 工具，該工具使用 ICMP Echo 訊息來測試主機連通性並測量往返延遲。頁面解釋了 TTL、interval、count 等引數，並支援 IPv4/IPv6 地址和 DNS 名稱。文中還簡要提及了 MAC Ping 在多播發現場景中的應用。"
tags:
  - 'icmp'
  - 'ping'
source: https://manual.mikrotik.com/docs/7.24/diagnostics-monitoring-and-troubleshooting/ping
captured_at: '2026-11-04T11:28:00+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

[*Ping CLI 參考*](../cli-reference/tool/ping.md)

Ping 使用 Internet Control Message Protocol (ICMP) Echo 訊息來判斷遠端主機是活動還是非活動，並確定與其通訊時的往返延遲。Ping 工具向主機發送 ICMP（型別 8）訊息，並等待 ICMP echo-reply（型別 0）。這些事件之間的間隔稱為往返時間。如果到間隔結束仍未收到響應（稱為 pong），則認為已超時。報告的第二個重要引數是 TTL（Time to Live）。封包經過的每臺機器都會將其遞減。只有當 TTL 大於源與目標之間的路由器數量時，封包才會到達目的地。

### 快速示例 {#quick-example}

RouterOS Ping 工具允許配置各種附加引數，例如：

- arp-ping
- address
- src-address
- count
- dscp
- interface
- interval
- routing-table
- size
- ttl

讓我們看一個非常簡單的示例：

```ros
[admin@MikroTik] > /tool/ping address=10.155.126.252 count=5 interval=200ms  
  SEQ HOST                                     SIZE TTL TIME  STATUS                                                                                                                                                                              
    0 10.155.126.252                             56  64 0ms  
    1 10.155.126.252                             56  64 0ms  
    2 10.155.126.252                             56  64 0ms  
    3 10.155.126.252                             56  64 0ms  
    4 10.155.126.252                             56  64 0ms  
    sent=5 received=5 packet-loss=0% min-rtt=0ms avg-rtt=0ms max-rtt=0ms 
```

使用更短的 CLI 命令也可以實現相同效果：

```ros
[admin@MikroTik] > /ping 10.155.126.252 count=5 interval=50ms               
  SEQ HOST                                     SIZE TTL TIME  STATUS                                                                                                                                                                              
    0 10.155.126.252                             56  64 0ms  
    1 10.155.126.252                             56  64 0ms  
    2 10.155.126.252                             56  64 0ms  
    3 10.155.126.252                             56  64 0ms  
    4 10.155.126.252                             56  64 0ms  
    sent=5 received=5 packet-loss=0% min-rtt=0ms avg-rtt=0ms max-rtt=0ms
```

也可以 ping 一個組播地址來發現屬於某個組播組的所有主機：

```ros
[admin@MikroTik] > /ping ff02::1
HOST                                    SIZE  TTL TIME  STATUS                                         
fe80::20c:42ff:fe49:fceb                56    64  1ms   echo reply                                     
fe80::20c:42ff:fe72:a1b0                56    64  1ms   echo reply                                     
fe80::20c:42ff:fe28:7945                56    64  1ms   echo reply                                     
fe80::21a:4dff:fe5d:8e56                56    64  3ms   echo reply                                     
    sent=1 received=4 packet-loss=-300% min-rtt=1ms avg-rtt=1ms max-rtt=3ms 
```

透過 DNS 名稱 ping：

```ros
[admin@MikroTik]  > /ping www.google.com count=5 interval=50ms
  SEQ HOST                                     SIZE TTL TIME  STATUS                                                                                                                                                                              
    0 216.58.207.228                             56  51 14ms 
    1 216.58.207.228                             56  51 13ms 
    2 216.58.207.228                             56  51 13ms 
    3 216.58.207.228                             56  51 13ms 
    4 216.58.207.228                             56  51 13ms 
    sent=5 received=5 packet-loss=0% min-rtt=13ms avg-rtt=13ms max-rtt=14ms
```

:::info
當你在 ping 中使用域名和 CLI 時，路由器將使用 [DNS](../network-management/dns.md) 來解析地址。當你使用 [WinBox](../management-tools/winbox.md) 的 Tools/Ping 時，將使用你計算機的 DNS 來解析給定地址。
:::

### MAC Ping {#mac-ping}

此子選單允許啟用 [MAC Ping 伺服器](../management-tools/mac-server.md)。

啟用 MAC ping 後，同一廣播域中的其他主機可以使用 ping 工具來 ping 一個 MAC 地址：

```ros
[admin@MikroTik]  > /tool/mac-server/ping/set enabled=yes 
```

Ping MAC 地址：

```ros
[admin@MikroTik]  > /ping 00:0C:42:72:A1:B0
HOST                                    SIZE  TTL TIME  STATUS                                         
00:0C:42:72:A1:B0                       56        0ms  
00:0C:42:72:A1:B0                       56        0ms  
    sent=2 received=2 packet-loss=0% min-rtt=0ms avg-rtt=0ms max-rtt=0ms 
```

:::info
預設情況下，MAC ping 會嘗試透過所有活動介面到達目標。如果目標可透過多個介面到達，這可能會產生不必要的流量和重複回覆。要將 MAC ping 限制到特定介面，請使用介面選擇器（在 MAC 地址後追加 `%`，後跟介面名稱）。例如：`/ping 00:11:22:33:44:55%ether1`
:::
