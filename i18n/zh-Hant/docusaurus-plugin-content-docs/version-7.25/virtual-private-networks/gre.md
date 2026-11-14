---
sidebar_key: "virtual-private-networks/gre"
sidebar_position: 3
title: "GRE"
sidebar_label: "GRE"
description: "通用路由封裝（GRE）是一種隧道協定，用於透過 IP 封裝各種網路協定，在 RouterOS 中以虛擬介面的形式實現，並可選啟用 keepalive，以及 MTU、MSS clamping 和 DSCP 設定等屬性，以實現可靠的流量轉發。"
tags:
  - 'gre'
source: https://manual.mikrotik.com/docs/7.25/virtual-private-networks/gre
captured_at: '2026-11-04T11:23:04+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Generic Routing Encapsulation (GRE) 是一種隧道協定，最初由 Cisco 開發，用於在 IP 網路上封裝各種網路層協定。它在隧道端點之間建立虛擬點對點鏈路，允許不同的協定流量透過路由基礎設施傳輸。

GRE 作為無狀態隧道執行，行為類似於 IPIP 和 EoIP。由於端點之間不維護會話狀態，即使遠端端點變得不可達，流量仍會繼續朝向該端點轉發。這可能導致流量被黑洞，直到路由重新收斂或隧道狀態發生變化。

在 RouterOS 中，GRE 介面作為虛擬介面實現，可根據所需拓撲用於路由和橋接網路設計。

為了改進故障檢測，RouterOS 為 GRE 隧道包含可選的 keepalive 機制。Keepalive 監控遠端端點的可達性，並可在對端停止響應時自動停用隧道介面，從而降低流量被髮送到非活動隧道的風險。

:::tip
GRE 隧道會增加 24 位元組開銷（4 位元組 GRE 頭部 + 20 位元組 IP 頭部）。GRE 隧道只能轉發 IP 和 IPv6 封包（EtherType 0x0800 和 0x86DD）。當 GRE 隧道用作路由閘道器時，不要使用 "Check gateway" 選項的 "arp" 值。
:::

GRE 在 [`/interface/gre`](../cli-reference/interface/gre.md) 和 [`/interface/gre6`](../cli-reference/interface/gre6.md) 選單中配置。

## 配置示例 {#setup-example}

本示例的目標是透過網際網路在兩個遠端站點之間實現三層連通性。

![](/img/6412953c9c3ec94f.webp)

該示例使用兩個站點：**Site1** 的本地網路範圍為 10.1.101.0/24，**Site2** 的本地網路範圍為 10.1.202.0/24。

第一步是建立 GRE 隧道。站點 1 上的路由器：

```ros
/interface/gre/add name=myGre remote-address=192.168.90.1 local-address=192.168.80.1
```

站點 2 上的路由器：

```ros
/interface/gre/add name=myGre remote-address=192.168.80.1 local-address=192.168.90.1
```

:::warning
在此示例中，未配置 keepalive，因此即使遠端隧道端點不可達，隧道介面仍具有 **running** 標誌。
:::

現在，設定隧道地址和正確的路由。站點 1 上的路由器：

```ros
/ip/address/add address=172.16.1.1/30 interface=myGre
/ip/route/add dst-address=10.1.202.0/24 gateway=172.16.1.2
```

站點 2 上的路由器：

```ros
/ip/address/add address=172.16.1.2/30 interface=myGre
/ip/route/add dst-address=10.1.101.0/24 gateway=172.16.1.1
```

此時，兩個站點已透過 GRE 隧道實現三層連通性。
