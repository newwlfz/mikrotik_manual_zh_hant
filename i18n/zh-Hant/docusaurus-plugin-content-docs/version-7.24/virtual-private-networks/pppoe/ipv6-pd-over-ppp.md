---
sidebar_key: "virtual-private-networks/pppoe/ipv6-pd-over-ppp"
sidebar_position: 1
title: "基於 PPP 的 IPv6 PD"
sidebar_label: "基於 PPP 的 IPv6 PD"
description: "本頁演示如何在 RouterOS 中透過 PPPoE 配置 IPv6 字首委派（IPv6 Prefix Delegation），展示如何在伺服器和用戶端上設定 DHCPv6-PD 地址池，包括介面配置以及動態字首委派的驗證。"
tags:
  - 'ipv6'
  - 'dhcpv6'
  - 'ppp'
source: https://manual.mikrotik.com/docs/7.24/virtual-private-networks/pppoe/ipv6-pd-over-ppp
captured_at: '2026-11-04T11:34:38+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

此示例演示如何設定 PPPoE 伺服器和用戶端以使用 IPv6 字首委派。

IPv6 字首可以透過 PPP 介面進行委派。當用戶端連線時，PPP 會自動新增一個動態的 [DHCPv6-PD 伺服器](../../network-management/dhcp.md#dhcpv6-server)。這樣就能在 PPP 介面上執行 DHCPv6 用戶端。

### 配置 {#configuration}

### 伺服器 {#server}

PPP 配置檔案下的 dhcpv6-pd-pool 引數用於啟用 PPP-PD。PPP 將使用指定的 [IPv6 pool](../../cli-reference/ipv6/pool/index.md) 來建立動態 DHCP 伺服器。

因此，第一步是新增一個 IPv6 地址池：

```ros
/ipv6/pool
add name=myPool prefix=2001:db8:7501:ff00::/60 prefix-length=62
```

現在我們可以配置一個 PPP 配置檔案並新增一個 PPPoE 伺服器

```ros
/ppp/profile/set default dhcpv6-pd-pool=myPool

/interface/pppoe-server/server 
add service-name=test interface=ether1
```

### 用戶端 {#client}

在用戶端側，我們需要設定 PPPoE 用戶端介面並在其上執行 DHCP 用戶端。

```ros
/interface/pppoe-client
add name=client-test interface=ether1 user=a1 service-name=test

/ipv6/dhcp-client 
add interface=client-test pool-name=ppp-test pool-prefix-length=64
```

### 測試狀態 {#testing-status}

在伺服器側，檢查是否已新增動態 DHCP 伺服器，以及字首是否已繫結到特定用戶端：

```ros
[admin@RB1100] /ipv6/dhcp-server> print 
Flags: D - dynamic, X - disabled, I - invalid 
 #    NAME              INTERFACE            ADDRESS-POOL            LEASE-TIME
 0 D  <pppoe-a1>        <pppoe-a1>           myPool                  3d        

[admin@RB1100] /ipv6/dhcp-server/binding> print 
Flags: X - disabled, D - dynamic 
 #   ADDRESS                                        DU       IAID SER.. STATUS 
 1 D 2001:db8:7501:ff04::/62                                  247 <pp.. bound  
 
```

在用戶端側，檢查 DHCP 用戶端是否已繫結，以及地址池是否已新增：

```ros
[admin@x86-test] /ipv6/dhcp-client> print 
Flags: D - dynamic, X - disabled, I - invalid 
 #    INTERFACE           STATUS        PREFIX                            EXPIRES-AFTER  
0    client-test          bound         2001:db8:7501:ff04::/62           2d23h18m17s  

[admin@x86-test] /ipv6/pool> print 
Flags: D - dynamic 
 #   NAME                        PREFIX                                   PREFIX-LENGTH
 0 D ppp-test                    2001:db8:7501:ff04::/62                             64
```
