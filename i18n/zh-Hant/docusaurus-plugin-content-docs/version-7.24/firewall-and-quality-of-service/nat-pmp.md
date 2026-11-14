---
sidebar_key: "firewall-and-quality-of-service/nat-pmp"
sidebar_position: 6
title: "NAT-PMP"
sidebar_label: "NAT-PMP"
description: "NAT-PMP 是一種協定，它透過動態 NAT 規則將內部 IPv4 地址對映到外部地址，從而實現透明的點對點連線，並在用戶端和伺服器端分別使用 UDP 埠 5350 和 5351。"
tags:
  - 'nat-pmp'
source: https://manual.mikrotik.com/docs/7.24/firewall-and-quality-of-service/nat-pmp
captured_at: '2026-11-04T11:28:13+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

NAT Port Mapping Protocol (NAT-PMP) 是一種用於個人計算機以及支援網路的智慧裝置或家電實現透明點對點網路連線的協定。

該協定透過獲取 NAT 閘道器的外部 IPv4 地址來工作，從而允許用戶端透過建立動態 NAT 規則，將其外部 IPv4 地址和埠告知可能希望與其通訊的對等端。

NAT-PMP 在用戶端使用 UDP 埠號 5350，在伺服器端使用 5351。

PMP 有兩種介面型別：**internal**（本地用戶端連線到的介面）和 **external**（Internet 連線到的介面）。路由器上只能有一個活動的 external 介面，並且該介面上具有“公網”IP 地址

:::warning
路由器只能有一個活動的 **external** 介面，並且該介面上具有“公網”IP 地址。NAT-PMP **internal** 介面可以為任何子網建立 NAT 對映，而不僅僅是 internal 介面上存在的子網，因此在設定 **internal** 介面時必須謹慎。
:::

有關 NAT PMP 的更多詳細資訊，請參見 [**RFC 6886**](https://www.rfc-editor.org/rfc/rfc6886)

NAT-PMP 配置可從 `/ip/nat-pmp` 選單訪問。

## 配置示例 {#configuration-example}

![](/img/a8f12d6db929635a.webp)

假設我們已經具備上圖所示的基本家庭網路設定。

在啟用 PMP-NAT 之前，我們需要對發出的 LAN 封包進行偽裝。

```ros
/ip/firewall/nat
add action=masquerade chain=srcnat out-interface=ether1
```

現在我們可以啟用 PMP 並新增 internal、external 介面：

```ros
/ip/nat-pmp/set enable=yes
/ip/nat-pmp/interfaces> add interface=ether1 type=external disabled=no
/ip/nat-pmp/interfaces> add interface=ether2 type=internal disabled=no

```

當來自 internal 介面側的用戶端傳送 PMP 請求時，路由器上會建立動態 NAT 規則：

```text
[admin@MikroTik] > ip firewall nat print 
Flags: X - disabled, I - invalid, D - dynamic 

0 chain=srcnat action=masquerade out-interface=ether1

1 D ;;; nat-pmp 192.168.88.10: ApplicationX
chain=dstnat action=dst-nat to-addresses=192.168.88.10 to-ports=55000 protocol=tcp 
dst-address=10.0.0.1 in-interface=ether1 dst-port=55000

2 D ;;; nat-pmp 192.168.88.10: ApplicationX
chain=dstnat action=dst-nat to-addresses=192.168.88.10 to-ports=55000 protocol=udp 
dst-address=10.0.0.1 in-interface=ether1 dst-port=55000

```

## 屬性 {#properties}

### 通用屬性 {#general-properties}

可從 `/ip/nat-pmp` 選單訪問。

| 屬性 | 描述 |
| :-- | :-- |
| **enabled** (*yes \| no*) | 啟用 NAT-PMP 服務 |

### NAT PMP 介面 {#nat-pmp-interfaces}

可從 `/ip/nat-pmp/interfaces` 選單訪問。

| 屬性 | 描述 |
| :-- | :-- |
| **interface** (*string*; 預設值：) | PMP 將在其上執行的介面名稱 |
| **type** (*external \| internal*) | PMP 介面型別：<span className="ros-background-accent-green-bolder"><code>external</code></span> - 分配了全域性 IP 地址的介面<span className="ros-background-accent-green-bolder"><code>internal</code></span> - 用戶端連線到的路由器本地介面 |
| **forced-ip** (*Ip*; 預設值：) | 允許指定當 external 介面有多個可用 IP 時使用哪個公網 IP。 |

:::warning
在涉及 VLAN 的更復雜設定中，如果 VLAN 介面是 LAN 的一部分，為使 PMP 正常工作，應將 VLAN 介面本身指定為 internal 介面。
:::
