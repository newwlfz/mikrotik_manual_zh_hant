---
sidebar_key: "user-guides/routing-and-networking-protocols/unicast/bfd"
sidebar_position: 1
title: "BFD"
sidebar_label: "BFD"
description: "雙向轉發檢測（BFD）是一種低延遲協定，用於檢測網路路徑中的故障，其執行獨立於路由協定。它使用 UDP 封裝，埠可配置，並支援多跳會話，但目前缺少回顯模式和認證。配置涉及在 RouterOS CLI 中指定介面、地址和 VRF。"
tags:
  - 'routing'
source: https://manual.mikrotik.com/docs/user-guides/routing-and-networking-protocols/unicast/bfd
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

**雙向轉發檢測**（**BFD**）是一種低開銷、短時協定，用於檢測兩個轉發引擎之間雙向路徑上的故障。這包括物理介面、子介面、資料鏈路，以及儘可能包括轉發引擎本身，且延遲都非常低。它獨立於介質、資料協定和路由協定執行。

**BFD** 是一種 hello 協定，用於檢查雙向鄰居可達性。它提供亞秒級鏈路故障檢測，並且不同於協定 hello 定時器，它不特定於任何路由協定。

**Control** 資料封裝在目的埠為 3784 的 **UDP** 幀中；埠 4784 用於多跳路徑。源埠範圍是 49152 – 65535。  
**Echo** 封裝在目的埠為 3785 的 UDP 幀中。

標準與技術：

- [RFC 5880 雙向轉發檢測（BFD）](https://datatracker.ietf.org/doc/rfc5880/)
- [RFC 5881 用於 IPv4 和 IPv6 的 BFD](https://datatracker.ietf.org/doc/rfc5881/)
- [RFC 5882 BFD 的通用應用](https://datatracker.ietf.org/doc/rfc5882/)
- [RFC 5883 用於多跳路徑的雙向轉發檢測（BFD）](https://datatracker.ietf.org/doc/rfc5883/)

## 尚不支援的功能 {#features-not-yet-supported}

- Echo 模式。
- 為 ip route 閘道器啟用 BFD。
- 認證。

## 配置 {#configuration}

允許或禁止 **BFD** 會話可透過 [`/routing/bfd/configuration`](../../../cli-reference/routing/bfd/configuration.md) 選單完成。例如：

```ros
/routing bfd configuration
add interfaces=sfp12 forbid-bfd=yes
add interfaces=static
```

配置條目對順序敏感，這意味著在上面的示例中，我們顯式禁止 "sfp12" 介面上的 BFD 會話（使用 [`forbid-bfd`](../../../cli-reference/routing/bfd/configuration.md#forbid-bfd)），並允許屬於 "static" 介面列表的其餘介面上的 BFD 會話。

為了能夠過濾多跳會話，可使用 [`addresses`](../../../cli-reference/routing/bfd/configuration.md#addresses) 或 [`address-list`](../../../cli-reference/routing/bfd/configuration.md#address-list) 屬性來匹配目標地址，以及相應的 [`vrf`](../../../cli-reference/routing/bfd/configuration.md#vrf)（如果會話未執行在 "main" VRF 中）。

```ros
/ip firewall address-list
add address=10.155.255.183 list=bgp_allow_bfd
add address=10.155.255.217 list=bgp_allow_bfd

/routing bfd configuration
add addresses=111.111.0.0/16 vrf=vrf1
add address-list=bgp_allow_bfd
```

任何未在配置中顯式列出的內容預設都被禁止。

### BFD 與 BGP {#bfd-with-bgp}

要為 [BGP](./bgp/index.md) 會話啟用 BFD，請在 [`/routing/bgp/connection`](../../../cli-reference/routing/bgp/connection.md#use-bfd) 選單中的所需條目上設定 [`use-bfd`](../../../cli-reference/routing/bgp/connection.md)。

當關聯的 BFD 會話處於 down 狀態時，BGP 會話輸出會顯示出來：

```ros
[admin@dr_02_BGP_MUM] /routing/bgp/session> print 
Flags: E - established 
 0 E ;;; BFD session down
     name="ovpn_test1-1" 
     remote.address=111.111.11.11@vrf1 .as=65530 .id=10.155.101.217 
     .capabilities=mp,rr,as4 .hold-time=infinity .messages=40717 
     .bytes=3436281 .eor="" 
     local.address=111.111.11.12@vrf1 .as=555 .id=111.111.11.12 
     .capabilities=mp,rr,gr,as4 .messages=1 .bytes=19 .eor="" 
     output.procid=20 
     input.procid=20 .filter=bgp-in ebgp 
     hold-time=infinity use-bfd=yes uptime=3s210ms 
     last-started=2023-05-19 09:54:04 prefix-count=3853 
```

### BFD 與 OSPF {#bfd-with-ospf}

要為 [OSPF](./ospf/index.md) 鄰居啟用 BFD，請在 [`/routing/ospf/interface-template`](../../../cli-reference/routing/ospf/interface-template.md#use-bfd) 選單中的所需條目上設定 [`use-bfd`](../../../cli-reference/routing/ospf/interface-template.md)。

## 會話狀態 {#session-status}

在 [`/routing/bfd/session`](../../../cli-reference/routing/bfd/session.md) 選單中檢視當前會話的狀態：

```ros
[admin@dr_02_BGP_MUM] /routing/bfd/session> print 
Flags: U - up, I - inactive 
 0 I ;;; BFD forbidden for destination address
     multihop=yes remote-address=10.155.101.183 local-address="" desired-tx-interval=0ms required-min-rx=0ms 
     multiplier=0 

 1   multihop=no remote-address=111.111.11.11%ovpn-out1@vrf1 local-address=111.111.11.12@vrf1 state=down 
     state-changes=0 desired-tx-interval=200ms required-min-rx=200ms remote-min-rx=1us multiplier=5 
     packets-rx=0 packets-tx=7674 
```

BFD 會選擇本地 tx 間隔和遠端最小 rx 間隔中的較大者作為期望傳送間隔。如果會話未建立，期望最小 tx 間隔預設為 1 秒。
