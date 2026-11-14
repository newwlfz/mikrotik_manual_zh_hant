---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/profiler"
sidebar_position: 15
title: "分析器"
sidebar_label: "分析器"
description: "RouterOS 中的 Profiler 工具會顯示每個程式的 CPU 使用情況，有助於識別佔用資源較高的程式。它支援按核心監控，並按程式型別對 CPU 使用情況進行分類，以便高效偵錯。"
tags:
  - 'cpu-usage'
  - 'profiler'
source: https://manual.mikrotik.com/docs/7.24/diagnostics-monitoring-and-troubleshooting/profiler
captured_at: '2026-11-04T11:28:00+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

The profiler 工具會顯示 RouterOS 中每個正在執行的程式的 CPU 使用率。它有助於識別哪個程式佔用了大部分 CPU 資源。  
觀看我們[關於此功能的影片](https://youtu.be/BkRaW14p8_s)。

```ros
[admin@MikroTik] > /tool/profile
```

在多核系統上，該工具允許指定每個核心的 CPU 使用率。

"CPU" 引數允許指定一個整數，該整數表示某個核心，或兩個預定義值 **all** 和 **total** 之一：

- total - 此值用於顯示所有核心使用率的總和。
- all - 此值用於分別顯示每個可用核心的 CPU 使用率。

在以下示例中，我們將檢視這兩個預定義值：

```ros
[admin@MikroTik] > /tool/profile cpu=all 
NAME             CPU        USAGE       
ethernet         1          0%          
kvm              0          0%          
kvm              1          4.5%        
management       0          0%          
management       1          0.5%        
idle             0          100%        
idle             1          93%         
profiling        0          0%          
profiling        1          2%    

[admin@MikroTik] > /tool/profile cpu=total 
NAME             CPU        USAGE       
ethernet         all        0%          
console          all        0%          
kvm              all        2.7%        
management       all        0%          
idle             all        97.2%       
profiling        all        0%          
bridging         all        0%  
```

## 分類器 {#classifiers}

RouterOS 程式按型別分類，並且為便於偵錯，每種型別的 CPU 使用率會單獨顯示。

| 屬性 | 描述 |
| :-- | :-- |
| backup | 備份服務 |
| bfd | BFD 服務 |
| bgp | BGP 服務 |
| bridging | 橋接服務 |
| btest | 頻寬測試。 |
| certificate | 證書服務 |
| console | 控制檯 |
| container | 容器合計使用率 |
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
| graphing | Graphing 工具 |
| gre | GRE |
| health | 系統監控、系統健康 |
| hotspot | Hotspot 服務 |
| idle | 空閒 CPU 資源 |
| igmp-proxy | IGMP Proxy 服務 |
| internet-detect | Detect Internet 工具 |
| ip-pool | IP Pool 服務 |
| ipsec | IPsec 服務：xfrm - 一組統計資訊，顯示被轉換程式碼丟棄的封包數量及原因。drivers/crypto - 提供對硬體加密加速器訪問的驅動程式。ipsec - 與 Internet Key Exchange (IKE) 協定、Authentication Header (AH)、Encapsulating Security Payload (ESP) 相關的程式。 |
| kvm | KVM 虛擬機器功能 |
| l7-matcher | L7 匹配器 |
| lcd | LCD 介面系統 |
| ldp | 標籤分發協定（LDP） |
| logging | 日誌系統 |
| management | 不同子系統：排程器、網路、檔案管理等。 |
| mpls | MPLS 相關功能 |
| neighbour-discovery | 鄰居發現服務 |
| networking | 網路功能中包含的一組通用服務 |
| ntp | NTP 服務 |
| ospf | OSPF 服務 |
| ovpn | OVPN 服務 |
| pim | 協定無關組播 |
| profiling | Profiler 服務 |
| queue-mgmt | 佇列：簡單佇列、佇列樹、佇列型別 |
| queuing | 中間佇列 |
| radius | RADIUS 服務 |
| radv | IPv6 radv 守護程式日誌訊息服務 |
| remote-access | 無需登入 RouterOS 直接訪問裝置 |
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
| web-proxy | Web 代理 |
| winbox | Winbox |
| wireguard | Wireguard |
| wireless | 使用無線系統的一組通用服務 |
| www | Webfig HTTP 服務 |
| zerotier | ZeroTier |
