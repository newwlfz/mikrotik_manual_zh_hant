---
sidebar_key: "high-availability-solutions/user-guides/bonding-examples"
sidebar_position: 1
title: "繫結示例"
sidebar_label: "繫結示例"
description: "本頁演示如何使用 MikroTik RouterOS 在兩條無線鏈路上繫結 EoIP 隧道，展示建立繫結介面並驗證跨鏈路流量分佈的配置步驟。"
tags:
  - 'bonding'
  - 'eoip'
source: https://manual.mikrotik.com/docs/7.25/high-availability-solutions/user-guides/bonding-examples
captured_at: '2026-11-04T11:17:46+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 在兩條無線鏈路上繫結 EoIP 隧道 {#bonding-eoip-tunnels-over-two-wireless-links}

這是一個將多個網路介面聚合為單個管道的示例。特別展示瞭如何聚合多個虛擬（EoIP）介面以獲得最大吞吐量（MT），並著重考慮可用性。

### 網路拓撲圖 {#network-diagram}

兩臺路由器 R1 和 R2 透過無線鏈路互連。兩側的無線介面都已分配 IP 地址。

### ![](/img/1bca9f117f589ad6.webp)配置 {#configuration}

繫結只能用於 OSI 第 2 層（乙太網級）連線。因此，需要在每條無線鏈路上建立 EoIP 介面。具體操作如下：

在路由器 R1 上：

```ros
/interface/eoip/add remote-address=10.0.1.1 tunnel-id=1 
/interface/eoip/add remote-address=10.2.2.1 tunnel-id=2
```

在路由器 R2 上：

```ros
/interface/eoip/add remote-address=10.0.1.2 tunnel-id=1 
/interface/eoip/add remote-address=10.2.2.2 tunnel-id=2
```

第二步是新增 bonding 介面，並將 EoIP 介面指定為其從屬介面：

R1:

```ros
/interface/bonding/add slaves=eoip-tunnel1,eoip-tunnel2 mode=balance-rr
```

R2:

```ros
/interface/bonding/add slaves=eoip-tunnel1,eoip-tunnel2 mode=balance-rr
```

最後一步是為 bonding 介面新增 IP 地址：

R1:

```ros
/ip/address/add address=192.168.0.1/24 interface=bonding1
```

R2:

```ros
/ip/address/add address=192.168.0.2/24 interface=bonding1
```

### 測試配置 {#test-the-configuration}

現在兩臺路由器可以使用 192.168.0.0/24 網路中的地址相互訪問。要驗證 bonding 介面的功能，請執行以下操作：

R1:

```ros
/interface/monitor-traffic eoip-tunnel1,eoip-tunnel2
```

R2:

```ros
/tool/bandwidth-test 192.168.0.1 direction=transmit
```

應當可以看到流量均勻分佈到兩個 EoIP 介面上：

```ros
/int monitor-traffic eoip-tunnel1,eoip-tunnel2              
    received-packets-per-second: 685      685                                  
       received-bits-per-second: 8.0Mbps  8.0Mbps                              
        sent-packets-per-second: 21       20                                   
           sent-bits-per-second: 11.9kbps 11.0kbps                             
    received-packets-per-second: 898      899                                  
       received-bits-per-second: 10.6Mbps 10.6Mbps                             
        sent-packets-per-second: 20       21                                   
           sent-bits-per-second: 11.0kbps 11.9kbps                             
    received-packets-per-second: 975      975                                  
       received-bits-per-second: 11.5Mbps 11.5Mbps                             
        sent-packets-per-second: 22       22                                   
           sent-bits-per-second: 12.4kbps 12.3kbps                             
    received-packets-per-second: 980      980                                  
       received-bits-per-second: 11.6Mbps 11.6Mbps                             
        sent-packets-per-second: 21       21                                   
           sent-bits-per-second: 11.9kbps 11.8kbps                             
    received-packets-per-second: 977      977                                  
       received-bits-per-second: 11.6Mbps 11.5Mbps                             
        sent-packets-per-second: 21       21                                   
           sent-bits-per-second: 11.9kbps 11.8kbps                             
-- [Q quit|D dump|C-z pause]
```

### 鏈路監控 {#link-monitoring}

很容易注意到，使用上述配置時，只要任一單條鏈路發生故障，bonding 介面的吞吐量就會驟降。這是因為沒有執行鏈路監控；因此，bonding 驅動無法感知底層鏈路的問題。在大多數 bonding 配置中，啟用鏈路監控是必須的。要啟用 ARP 鏈路監控，請執行以下操作：

#### R1 {#r1}

```ros
/interface/bonding/set bonding1 link-monitoring=arp arp-ip-targets=192.168.0.2
```

#### R2 {#r2}

```ros
/interface/bonding/set bonding1 link-monitoring=arp arp-ip-targets=192.168.0.1
```
