---
sidebar_key: "virtual-private-networks/gre"
sidebar_position: 3
title: "GRE"
sidebar_label: "GRE"
description: "通用路由封裝（GRE）是一種隧道協定，用於透過 IP 封裝各種網路協定，在 RouterOS 中以虛擬介面的形式實現，並可選啟用 keepalive，以及 MTU、MSS clamping 和 DSCP 設定等屬性，以實現可靠的流量轉發。"
tags:
  - 'gre'
source: https://manual.mikrotik.com/docs/7.24/virtual-private-networks/gre
captured_at: '2026-11-04T11:34:29+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Generic Routing Encapsulation (GRE) 是一種隧道協定，最初由 Cisco 開發，用於在 IP 網路上封裝各種網路層協定。它在隧道端點之間建立虛擬點對點鏈路，允許不同的協定流量透過路由基礎設施傳輸。

GRE 作為無狀態隧道執行，行為類似於 IPIP 和 EoIP。由於端點之間不維護會話狀態，即使遠端端點變得不可達，流量也可能繼續被轉發到該遠端端點，這可能導致流量被黑洞化，直到路由重新收斂或隧道狀態發生變化。

在 RouterOS 中，GRE 介面作為虛擬介面實現，可根據所需拓撲用於路由和橋接網路設計。

為了改進故障檢測，RouterOS 為 GRE 隧道包含可選的 keepalive 機制。Keepalive 監控遠端端點的可達性，並可在對端停止響應時自動停用隧道介面，從而降低流量被髮送到非活動隧道的風險。

:::tip
GRE 隧道會增加 24 位元組開銷（4 位元組 gre 頭 + 20 位元組 IP 頭）。GRE 隧道只能轉發 IP 和 IPv6 封包（乙太網型別 800 和 86dd）。當 GRE 隧道用作路由閘道器時，不要使用 "Check gateway" 選項的 "arp"。
:::
**子選單：** `/interface/gre`

## 屬性 {#properties}

| 屬性 | 描述 |
| :-- | :-- |
| **allow-fast-path** (*yes \| no*; 預設值：**yes**) | 是否允許 FastPath 處理。如果使用 IPsec 隧道，則必須停用。 |
| **clamp-tcp-mss** (*yes \| no*; 預設值：**yes**) | 控制是否更改收到的 TCP SYN 封包的 MSS 大小。啟用後，如果當前 MSS 大小超過隧道介面 MTU（考慮 TCP/IP 開銷），路由器將更改收到的 TCP SYN 封包的 MSS 大小。收到的封裝封包仍將包含原始 MSS，只有在解封裝後才會更改 MSS。 |
| **comment** (*string*; Default: ) | 隧道的簡短描述。 |
| **disabled** (*yes \| no*; Default: **no**) | 啟用/停用隧道。 |
| **dont-fragment** (*inherit \| no*; 預設值：**no**) | 是否在相關封包中包含 DF 位：  *no* - 如果需要則分片，*inherit* - 使用原始封包的 Don't Fragment 標誌。  （不使用 Don't Fragment 時：inherit - 封包可能被分片）。 |
| **dscp** (*inherit \| integer [0-63]*; 預設值：) | 將 Gre 頭中的 dscp 值設定為固定值，或繼承從隧道流量中獲取的 dscp 值 |
| **ipsec-secret** (*string*; 預設值：) *[敏感](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 指定 secret 後，路由器會向 remote-address 新增動態 IPsec 對等體，並使用預共享金鑰和策略（預設情況下 phase2 使用 sha1/aes128cbc）。 |
| **keepalive** (*integer[/time],integer 0..4294967295*; 預設值：**10s,10**) | 隧道 keepalive 引數設定即使隧道遠端端不可用，隧道 running 標誌仍將保留的時間間隔。如果配置的時間和重試次數失敗，則移除介面 running 標誌。引數按以下格式寫入：`KeepaliveInterval,KeepaliveRetries`，其中 KeepaliveInterval 是時間間隔，KeepaliveRetries 是重試嘗試次數。預設情況下，keepalive 設定為 10 秒和 10 次重試。 |
| **l2mtu** (*integer [0..65536]*; 預設值：**65535**) | 二層最大傳輸單元。 |
| **local-address** (*IP*; 預設值：**0.0.0.0**) | 將用於本地隧道端的 IP 地址。如果設定為 0.0.0.0，則將使用出介面的 IP 地址。 |
| **mtu** (*integer [0..65536]*; 預設值：**1476**) | 三層最大傳輸單元。 |
| **name** (*string*; Default: ) | 隧道名稱。 |
| **remote-address** (*IP*; 預設值：) | 遠端隧道端的 IP 地址。 |

## 配置示例 {#setup-example}

本示例的目標是透過網際網路在兩個遠端站點之間實現三層連通性

![](/img/6412953c9c3ec94f.webp)

我們有兩個站點，**Site1** 的本地網路範圍為 10.1.101.0/24，**Site2** 的本地網路範圍為 10.1.202.0/24。

第一步是建立 GRE 隧道。站點 1 上的路由器：

```ros
/interface/gre/add name=myGre remote-address=192.168.90.1 local-address=192.168.80.1
```

站點 2 上的路由器：

```ros
/interface/gre/add name=myGre remote-address=192.168.80.1 local-address=192.168.90.1
```

如您所見，隧道配置非常簡單。

:::warning
在此示例中，未配置 keepalive，因此即使遠端隧道端不可達，隧道介面仍將具有 **running** 標誌
:::

現在我們只需要設定隧道地址和正確的路由。站點 1 上的路由器：

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
