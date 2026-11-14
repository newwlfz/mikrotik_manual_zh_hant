---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/profiler"
sidebar_position: 15
title: "分析器"
sidebar_label: "分析器"
description: "Profiler 工具顯示每個 RouterOS 程式分類器的 CPU 使用情況，可按總和或按核心顯示，用於識別哪個程式消耗 CPU 資源。"
tags:
  - 'cpu-usage'
  - 'profiler'
source: https://manual.mikrotik.com/docs/diagnostics-monitoring-and-troubleshooting/profiler
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Profiler 工具顯示 RouterOS 中執行的每個程式的 CPU 使用率。它有助於識別哪個程式佔用了大部分 CPU 資源。請參閱[關於此功能的影片](https://youtu.be/BkRaW14p8_s)。

```ros
[admin@MikroTik] > /tool/profile
```

程式按型別（分類器）分組，例如 `wireless`、`bridging` 或 `console`，並且每個分類器的 CPU 使用率單獨顯示。只顯示有正在執行程式的分類器，因此行取決於裝置和所使用的功能。

在多核系統上，`cpu` 引數選擇檢視：`cpu=total`（預設）彙總所有核心的使用率，`cpu=all` 分別顯示每個核心，並帶有每核心的 `cpuN` 彙總行，而 `cpu=<number>` 僅顯示該核心。下面的示例演示了這兩種檢視。
如果沒有 `duration`，分析會持續重新整理，直到你停止它；`freeze-frame-interval`（以秒為單位）設定多久列印一個新幀，並且每個幀顯示自上一幀以來測得的用量。使用 `duration` 時，工具會在給定的秒數後停止。在取樣資料到達之前，最初的一兩幀只顯示 `total` 行。

如需不帶程式拆分的簡單每核心負載摘要（例如用於指令碼），請使用 [`/system/resource/cpu/print`](../cli-reference/system/resource/cpu.md)。

## 查詢繁忙程式 {#find-a-busy-process}

失控指令碼會使一個核心保持繁忙。在彙總檢視（`cpu=total`）中，4 核路由器中一個核心 100% 的使用率會顯示為 25%：

```ros
[admin@MikroTik] > /tool/profile cpu=total freeze-frame-interval=1 duration=5
Columns: NAME, USAGE
NAME            USAGE
interface-mgmt  0%   
bridging        0%   
console         25.1%
resource-mgmt   0%   
ssh             0%   
total           25.1%
```

`console` 佔用 CPU 表明指令碼或 console 會話活動（此處為指令碼迴圈）。每核心檢視會在 `cpuN` 行中顯示確切的核心及其總計：

```ros
[admin@MikroTik] > /tool/profile cpu=all freeze-frame-interval=1 duration=3
Columns: NAME, CPU, USAGE
NAME         CPU  USAGE
console        0  95.5%
cpu0              95.5%
console        1  0.5% 
wireless       1  0.5% 
kernel         1  0.5% 
cpu1              1.5% 
console        2  4%   
certificate    2  0.5% 
cpu2              4.5% 
console        3  0.5% 
cpu3              0.5% 
```

## 分類器 {#classifiers}

RouterOS 程式按型別分類，並且每種型別的 CPU 使用率會單獨顯示，以便於偵錯。除了下面的功能分類器之外，還可能出現 `kernel`、`ipc`、`interface-mgmt` 和 `resource-mgmt` 等系統行；任何沒有分類器的內容都歸入 `unclassified` 下：

| 屬性 | 描述 |
| :-- | :-- |
| backup | 備份服務 |
| bfd | BFD 服務 |
| bgp | BGP 服務 |
| bridging | 橋接服務 |
| btest | 頻寬測試。 |
| certificate | 證書服務 |
| console | 控制檯 |
| container | 容器綜合使用情況 |
| dhcp | DHCP-Server 和 DHCP-Client 服務 |
| disk | 儲存相關服務 |
| dns | DNS 相關服務 |
| dude | The Dude 軟體包服務 |
| e-mail | 電子郵件工具 |
| encrypting | 加密程式 |
| eoip | EoIP |
| ethernet | 乙太網相關屬性，例如鏈路速度、自動協商、雙工模式、監控收發器診斷資訊等。 |
| fetcher | Fetch 工具 |
| fileman | 檔案管理器 |
| firewall | 防火牆相關程式 |
| firewall-mgmt | 防火牆管理：過濾、NAT、Mangle |
| flash | 儲存相關服務 |
| ftp | FTP 服務 |
| gps | GPS 服務 |
| graphing | 圖形繪製工具 |
| gre | GRE |
| health | 系統監控、系統健康狀況 |
| hotspot | Hotspot 服務 |
| idle | 空閒 CPU 資源 |
| igmp-proxy | IGMP Proxy 服務 |
| internet-detect | Detect Internet 工具 |
| ip-pool | IP Pool 服務 |
| ipsec | IPsec 服務：xfrm - 一組統計資訊，顯示由轉換程式碼丟棄的封包數量及原因。drivers/crypto - 提供對硬體加密加速器訪問的驅動程式。ipsec - 與 Internet Key Exchange (IKE) 協定、Authentication Header (AH)、Encapsulating Security Payload (ESP) 相關的程式。 |
| kvm | KVM 虛擬機器功能 |
| l7-matcher | L7 匹配器 |
| lcd | LCD 介面系統 |
| ldp | 標籤分發協定（LDP） |
| logging | 日誌系統 |
| management | 不同的子系統：排程器、網路、檔案管理等。 |
| mpls | MPLS 相關功能 |
| neighbor-discovery | 鄰居發現服務 |
| networking | 網路中所包含的一組通用服務 |
| ntp | NTP 服務 |
| ospf | OSPF 服務 |
| ovpn | OVPN 服務 |
| pim | 協定無關組播 |
| profiling | Profiler 服務 |
| queue-mgmt | 佇列：Simple queues、Queue tree、Queue types |
| queuing | 中間佇列 |
| radius | RADIUS 服務 |
| radvd | IPv6 Router Advertisement 守護程式 (radvd) 服務 |
| remote-access | 無需登入 RouterOS 即可直接訪問裝置 |
| rip | 路由資訊協定 |
| routing | 路由相關服務 |
| serial | 序列控制檯和終端工具 |
| sniffing | 封包 Sniffer 工具 |
| snmp | SNMP |
| socks | 套接字安全 |
| spi | 儲存相關服務 |
| ssh | SSH 伺服器 |
| ssl | SSL |
| supout.rif | supout.rif 檔案生成 |
| telnet | Telnet 服務 |
| tftp | TFTP 服務 |
| traffic-accounting | Traffic-Flow 日誌系統 |
| traffic-flow | Traffic-Flow 系統 |
| unclassified | 未由此分類器定義的程式或服務 |
| upnp | UPnP 協定 |
| usb | USB 功能 |
| user-manager | User Manager 服務 |
| vrrp | VRRP |
| web-proxy | 網頁代理 |
| winbox | Winbox |
| wireguard | Wireguard |
| wireless | 使用無線系統的一組通用服務 |
| www | Webfig HTTP 服務 |
| zerotier | ZeroTier |

有關所有引數，請參見 [`/tool/profile`](../cli-reference/tool/profile.md) CLI 參考。
