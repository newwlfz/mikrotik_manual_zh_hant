---
sidebar_key: "high-availability-solutions/user-guides/vrrp-configuration-examples"
sidebar_position: 2
title: "VRRP 配置示例"
sidebar_label: "VRRP 配置示例"
description: "本頁提供 MikroTik RouterOS 的基本 VRRP 配置示例，演示如何在兩臺路由器之間設定主備冗餘，並在故障切換期間共享 IP 地址和更新 ARP 表。"
tags:
  - 'vrrp'
source: https://manual.mikrotik.com/docs/7.24/high-availability-solutions/user-guides/vrrp-configuration-examples
captured_at: '2026-11-04T11:30:06+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 基本設定 {#basic-setup}

這是基本的 VRRP 配置示例。

:::info
注意

建議所有使用同一 VRID 實現 VRRP 的裝置都使用相同版本的 RouterOS。

:::

![](/img/0340e63898c1565e.webp)

根據此配置，只要 Master R1 正常工作，所有發往外部網路的流量都會被定向到 R1。但一旦 R1 發生故障，R2 就會接替成為 Master，並開始處理轉發到與 IP(R1) 關聯的介面的封包。在此設定中，路由器 "R2" 在 Backup 期間完全空閒。

## 配置 {#configuration}

### R1 配置 {#r1-configuration}

```ros
/ip/address/add address=192.168.1.10/24 interface=ether1
/interface/vrrp/add interface=ether1 vrid=49 priority=254
/ip/address/add address=192.168.1.1/32 interface=vrrp1
```

### R2 配置 {#r2-configuration}

```ros
/ip/address/add address=192.168.1.20/24 interface=ether1
/interface/vrrp/add interface=ether1 vrid=49
/ip/address/add address=192.168.1.1/32 interface=vrrp1
```

### 測試 {#testing}

首先，檢查兩臺路由器的 VRRP 介面標誌是否正確。在路由器 R1 上，應如下所示。

```ros
/interface/vrrp/print detail
 0   RM name="vrrp1" mtu=1500 mac-address=00:00:5E:00:01:31 arp=enabled interface=ether1 vrid=49 
        priority=254 interval=1 preemption-mode=yes authentication=none password="" on-backup="" 
        on-master="" version=3 v3-protocol=ipv4
```

在路由器 R2 上：

```ros
/interface/vrrp/print detail
 0    B name="vrrp1" mtu=1500 mac-address=00:00:5E:00:01:31 arp=enabled interface=ether1 vrid=49 
        priority=100 interval=1 preemption-mode=yes authentication=none password=""
         on-backup="" on-master="" version=3 v3-protocol=ipv4
```

可以看到，兩臺路由器上的 VRRP 介面 MAC 地址相同。現在要檢查 VRRP 是否正常工作，請嘗試從用戶端 ping 虛擬地址，並檢查 ARP 表項：

```ros
[admin@client] > /ping 192.168.1.1
192.168.1.1 64 byte ping: ttl=64 time=10 ms
192.168.1.1 64 byte ping: ttl=64 time=8 ms
2 packets transmitted, 2 packets received, 0% packet loss
round-trip min/avg/max = 8/9.0/10 ms
```

現在拔掉路由器 R1 上的 ether1 網線。R2 將成為 VRRP Master，用戶端上的 ARP 表不會改變，但流量將開始透過 R2 路由器轉發。

:::info
如果 VRRP 與反向路徑過濾（Reverse Path Filtering）一起使用，建議將 `rp-filter` 設定為 `loose`，否則 VRRP 介面可能無法訪問。

:::

## 負載分擔 {#load-sharing}

在基本配置示例中，R2 在 Backup 狀態期間完全空閒。這種行為可能被視為浪費寶貴的資源。在這種情況下，可以將 R2 路由器設定為某些用戶端的閘道器。
這種配置的明顯優勢是建立負載分擔方案。但這樣做時，R2 路由器不受當前 VRRP 設定的保護。  
要使此設定生效，我們需要兩個虛擬路由器。

![](/img/de347a67c254c189.webp)

V1 虛擬路由器的配置將與基本示例中的配置相同——R1 是 Master，R2 是 Backup 路由器。在 V2 中，Master 是 R2，Backup 是 R1。  
透過這種配置，我們在 R1 和 R2 之間建立負載分擔；此外，我們讓兩臺路由器互為備份，從而建立保護設定。

## 配置 {#configuration-1}

### R1 配置 {#r1-configuration-1}

```ros
/ip/address/add address=192.168.1.1/24 interface=ether1
/interface/vrrp/add interface=ether1 vrid=49 priority=254
/interface/vrrp/add interface=ether1 vrid=77 
/ip/address/add address=192.168.1.253/32 interface=vrrp1
/ip/address/add address=192.168.1.254/32 interface=vrrp2
```

### R2 配置 {#r2-configuration-1}

```ros
/ip/address/add address=192.168.1.2/24 interface=ether1
/interface/vrrp/add interface=ether1 vrid=49
/interface/vrrp/add interface=ether1 vrid=77 priority=254
/ip/address/add address=192.168.1.253/32 interface=vrrp1
/ip/address/add address=192.168.1.254/32 interface=vrrp2
```

## 無搶佔的 VRRP {#vrrp-without-preemption}

每當具有更高優先順序的路由器變為可用時，它就會成為 Master 路由器。有時這並不是期望的行為，可以透過在 VRRP 配置中設定 `preemption-mode=no` 來關閉。

### 配置 {#configuration-2}

我們將使用與基本示例相同的設定。唯一區別是，在配置過程中設定 preemption-mode=no。透過修改現有配置即可輕鬆完成：

```ros
/interface/vrrp/set [find] preemption-mode=no
```

### 測試 {#testing-1}

嘗試關閉 R1 路由器，R2 將成為 Master 路由器，因為它在可用路由器中具有最高優先順序。

現在啟動 R1 路由器，你將看到即使 R1 具有更高優先順序，R2 路由器仍繼續作為 Master。
