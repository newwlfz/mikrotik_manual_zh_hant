---
sidebar_key: "containers/veth"
sidebar_position: 2
title: "VETH"
sidebar_label: "VETH"
description: "VETH（Virtual Ethernet）為 RouterOS 中的容器提供網路連線，充當虛擬介面，支援靜態 IP 和 DHCP 分配的 IP、SLAAC，並可整合到網橋或路由配置中。"
tags:
  - 'veth'
  - 'ipv6'
source: https://manual.mikrotik.com/docs/7.24/containers/veth
captured_at: '2026-11-04T11:27:46+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

VETH（Virtual Ethernet）是一種虛擬網路介面，為容器提供網路連線。它充當連線 RouterOS 與容器的虛擬乙太網埠，使容器能夠與其他介面和網路通訊。

VETH 介面的行為類似於標準乙太網介面。可以為它們分配靜態 IPv4 和 IPv6 地址，透過 DHCP 用戶端獲取地址，並支援 SLAAC。此外，VETH 介面可以像物理介面一樣參與橋接或路由配置。

## 基本配置示例 {#basic-configuration-example}

配置 VETH 有多種方式。以下是一些簡單示例。

```ros
# 带 DHCP-client 的 VETH
/interface/veth/add dhcp=yes

# 带静态地址的 VETH
/interface/veth/add address=10.1.1.10/24 gateway=10.1.1.1 
```

配置介面後，你可以將其分配給容器。  
容器應獲取由 DHCP 伺服器分配的 IP 或靜態地址。

## 屬性 {#properties}

### VETH {#veth}

**子選單：** `/interface/veth/add`

VETH 介面的配置設定。

| 引數 | 型別 | 預設值 | 說明 |
| :-- | :-- | :-- | :-- |
| **address** | IPv4/IPv6 地址 | **None** | 將分配給介面的 IPv4 或 IPv6 地址 |
| **gateway** | IPv4 地址 | **None** | IPv4 閘道器地址 |
| **gateway6** | IPv6 地址 | **None** | IPv6 閘道器地址 |
| **mac-address** | MAC 地址 | **None** | 介面 MAC 地址 |
| **container-mac-address** | MAC 地址 | **None** | 將分配給容器的 MAC 地址 |
| **dhcp** | yes / no | **no** | 在介面上啟用 DHCP 用戶端 |
| **name** | string | **None** | 介面名稱 |
