---
sidebar_key: "firewall-and-quality-of-service/upnp"
sidebar_position: 7
title: "UPnP"
sidebar_label: "UPnP"
description: "MikroTik RouterOS 支援 UPnP，可實現透明的點對點連線，從而支援動態網路發現和 NAT 穿透。文件涵蓋通用屬性（如介面型別 `internal`/`external`）和安全設定，以及在路由器介面上啟用 UPnP 的配置示例。"
tags:
  - 'upnp'
  - 'nat'
source: https://manual.mikrotik.com/docs/7.24/firewall-and-quality-of-service/upnp
captured_at: '2026-11-04T11:28:26+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

MikroTik RouterOS 支援通用即插即用（UPnP）架構，它可在個人計算機與支援網路的裝置或家電之間實現透明的點對點網路連線。

UPnP 允許在網路中任意控制裝置的指揮下，於任意兩臺裝置之間進行資料通訊。該技術完全獨立於任何特定的物理介質。它支援自動發現的聯網方式，這意味著裝置無需任何初始配置即可動態加入網路。DHCP 和 DNS 伺服器是可選的，如果網路中存在就會被使用。UPnP 實現了一種簡單而強大的 NAT 穿透方案，使用戶端能夠在 NAT 之後獲得完整的雙向點對點網路支援。

UPnP 有兩種介面型別：**internal**（本地用戶端裝置所連線的介面）和 **external**（連線到 Internet 的介面）。路由器只能有一個具有“公網”IP 地址的活動外部介面，而內部介面可以有任意多個，它們全部使用經過源 NAT 轉換的“內部”IP 地址。該協定透過建立動態 NAT 條目規則來工作。

:::info
UPnP 的 **internal** 介面可以為任何子網建立 NAT 對映，而不僅僅是該內部介面上存在的子網，因此在設定 **internal** 介面時必須謹慎。
:::

許多現代應用程式都使用 UPnP 協定，例如大多數 DirectX 遊戲，以及 Windows Messenger 的各種功能，如遠端協助、應用程式共享、檔案傳輸、語音和影片通訊（在防火牆之後）。

## 配置 {#configuration}

### 通用屬性 {#general-properties}

**子選單：** `/ip/upnp`

| 屬性 | 描述 |
| :-- | :-- |
| **allow-disable-external-interface** (*yes \| no*；預設：**yes**) | 是否允許使用者停用路由器的外部介面。此功能（允許使用者無需任何認證過程即可關閉路由器的外部介面）是標準所要求的，但在標準並非為之設計的 UPnP 部署中，它有時並不符合預期或並不受歡迎（該標準主要面向家庭使用者建立自己的區域網路），因此你可以停用此行為 |
| **enabled** (*yes \| no*) | 啟用 UPnP 服務 |
| **show-dummy-rule** (*yes \| no*；預設：**yes**) | 為某些有缺陷的實現啟用一種變通方案，這些實現會錯誤地處理 UPnP 規則缺失的情況（例如彈出錯誤訊息）。此選項會指示伺服器安裝一條虛擬（無意義）的 UPnP 規則，供那些否則無法正常工作的用戶端觀察到 |

:::danger
如果你不關閉 **allow-disable-external-interface**，則本地網路中的任何使用者都能夠（無需任何認證過程）停用路由器的外部介面。
:::

### UPnP 介面 {#upnp-interfaces}

**子選單：** `/ip/upnp/interfaces`

| 屬性 | 描述 |
| :-- | :-- |
| **interface** (*string*；預設：) | uPnP 將在其上執行的介面名稱 |
| **type** (*external \| internal*) | UPnP 介面型別：<span className="ros-background-accent-green-bolder"><code>external</code></span> - 為其分配全域性 IP 地址的介面<code>internal </code>- 用戶端所連線的路由器本地介面 |
| **forced-external-ip** (*Ip*；預設：) | 當外部介面有多個可用 IP 時，允許指定要使用哪個公網 IP。 |

:::warning
在帶 VLAN 的更復雜環境中，若 VLAN 介面被視為 LAN 介面，則必須將 VLAN 介面本身指定為 UPnP 的內部介面，UPnP 才能正常工作。
:::

## 配置示例 {#configuration-example}

![](/img/a8f12d6db929635a.webp)

我們的路由器上已經啟用了偽裝：

```ros
[admin@MikroTik] /ip/upnp> /ip/firewall/nat/print
Flags: X - disabled, I - invalid, D - dynamic
  0   chain=srcnat action=masquerade out-interface=ether1
[admin@MikroTik] /ip/upnp>
```

要啟用 UPnP 功能：

```ros
[admin@MikroTik] /ip/upnp> set enable=yes
[admin@MikroTik] /ip/upnp> print
                             enabled: yes
    allow-disable-external-interface: yes
                     show-dummy-rule: yes
[admin@MikroTik] /ip/upnp>
```

現在，我們只需新增介面：

```ros
[admin@MikroTik] /ip/upnp/interfaces> add interface=ether1 type=external
[admin@MikroTik] /ip/upnp/interfaces> add interface=ether2 type=internal
[admin@MikroTik] /ip/upnp/interfaces> print
Flags: X - disabled
  #   INTERFACE TYPE
  0 X ether1    external
  1 X ether2    internal

[admin@MikroTik] /ip/upnp/interfaces> enable 0,1
```

現在，一旦內部介面一側的用戶端傳送 UPnP 請求，路由器上就會建立動態 NAT 規則，示例規則大致如下：

```ros
[admin@MikroTik] > ip firewall nat print 
Flags: X - disabled, I - invalid, D - dynamic 

0 chain=srcnat action=masquerade out-interface=ether1

1 D ;;; upnp 192.168.88.10: ApplicationX
chain=dstnat action=dst-nat to-addresses=192.168.88.10 to-ports=55000 protocol=tcp 
dst-address=10.0.0.1 in-interface=ether1 dst-port=55000

2 D ;;; upnp 192.168.88.10: ApplicationX
chain=dstnat action=dst-nat to-addresses=192.168.88.10 to-ports=55000 protocol=udp 
dst-address=10.0.0.1 in-interface=ether1 dst-port=55000

```
