---
sidebar_key: "bridging-and-switching/macsec"
sidebar_position: 4
title: "MACsec"
sidebar_label: "MACsec"
description: "MACsec 是一種用於乙太網的安全協定，它使用 GCM-AES-128 加密提供機密性、完整性和真實性。RouterOS 支援 MACsec，可手動配置金鑰並且具備有限的硬體加速，需要在裝置之間使用預共享金鑰來建立安全的 Layer2 連線。"
tags:
  - 'macsec'
source: https://manual.mikrotik.com/docs/bridging-and-switching/macsec
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

MACsec（媒體訪問控制安全）協定是一種用於乙太網的標準安全技術，用於確保透過物理介質傳輸的資料的機密性、完整性和真實性。MACsec 由 IEEE 標準 802.1AE 定義。

MACsec 在乙太網上使用 GCM-AES-128 加密，並保護所有 LAN 流量，包括 DHCP、ARP、LLDP 和更高層協定。

:::warning
RouterOS 的 MACsec 實現處於早期階段；它 **不支援** 透過 [Dot1x](../authentication-authorization-accounting/dot1x.md) 進行動態金鑰管理（需要手動配置金鑰），並且硬體加速加密僅在部分產品上逐步推出。
:::

## 基本配置示例 {#basic-configuration-example}

設想 Host1 的 ether1 連線到 Switch 的 ether1，Host2 的 ether1 連線到 Switch 的 ether2。在此示例中，我們將建立兩對 MACsec 介面，並使用網橋在兩臺終端裝置之間建立安全的二層連線。

首先，在 Host1 和 Host2 上配置 MACsec 介面。我們只需指定乙太網介面，RouterOS 就會自動生成連線關聯金鑰（CAK）和連線關聯名稱（CKN）。使用 `print` 命令檢視這些值：

```ros
# Host1
/interface/macsec
add interface=ether1 name=macsec1

[admin@Host1] /interface/macsec/print show-sensitive
Flags: I - inactive, X - disabled, R - running 
 0   name="macsec1" mtu=1468 interface=ether1 status="negotiating" cak=71a7c363794da400dbde595d3926b0e9
     ckn=f2c4660060169391d29d8db8a1f06e5d4b84a128bad06ad43ea2bd4f7d21968f profile=default

# Host2
/interface/macsec
add interface=ether1 name=macsec1

[admin@Host2] /interface/macsec/print show-sensitive
Flags: I - inactive, X - disabled, R - running 
 0   name="macsec1" mtu=1468 interface=ether1 status="negotiating" cak=dc47d94291d19a6bb26a0c393a1af9a4
     ckn=e9bd0811dad1e56f06876aa7715de1855f1aee0baf5982ac8b508d4fc0f162d9 profile=default
```

在 Switch 裝置上，要啟用 MACsec，我們需要為相應的乙太網介面配置匹配的 CAK 和 CKN 值：

```ros
# Switch
/interface/macsec
add comment=Host1 cak=71a7c363794da400dbde595d3926b0e9 ckn=f2c4660060169391d29d8db8a1f06e5d4b84a128bad06ad43ea2bd4f7d21968f interface=ether1 name=macsec1
add comment=Host2 cak=dc47d94291d19a6bb26a0c393a1af9a4 ckn=e9bd0811dad1e56f06876aa7715de1855f1aee0baf5982ac8b508d4fc0f162d9 interface=ether2 name=macsec2
```

預共享金鑰成功交換後，MACsec 金鑰協定（MKA）就會啟用。MKA 負責確保鏈路上 MACsec 的連續性，並決定在點對點連線中哪一側成為金鑰伺服器。金鑰伺服器生成安全關聯金鑰（SAK），僅與鏈路另一端的裝置共享。此 SAK 用於保護透過鏈路的所有資料流量。金鑰伺服器會定期生成新的隨機 SAK，並透過點對點鏈路共享，以維持 MACsec 功能。

在 RouterOS 中，MACsec 介面可以像任何乙太網介面一樣配置。它可以作為帶 IP 地址的可路由介面使用，也可以放入網橋中。在 Host1 和 Host2 上，我們將新增同一網路中的 IP 地址。在 Switch 上，我們將使用網橋。

```ros
# Host1
/ip/address
add address=192.168.10.10/24 interface=macsec1

# Host2
/ip/address
add address=192.168.10.20/24 interface=macsec1

# Switch
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=macsec1
add bridge=bridge1 interface=macsec2
```

最後，使用 ping 確認 Host1 可以訪問 Host2。

```ros
 [admin@Host1] > ping 192.168.10.20
  SEQ HOST                                     SIZE TTL TIME       STATUS
    0 192.168.10.20                              56  64 1ms438us  
    1 192.168.10.20                              56  64 818us     
    2 192.168.10.20                              56  64 791us     
    3 192.168.10.20                              56  64 817us     
    4 192.168.10.20                              56  64 783us     
    sent=5 received=5 packet-loss=0% min-rtt=783us avg-rtt=929us max-rtt=1ms438us
```

## 屬性參考 {#property-reference}

### 介面設定 {#interface-settings}

**子選單：** `/interface/macsec`

MACsec 介面的配置設定。

| 屬性 | 描述 |
| :-- | :-- |
| **cak** (*string*; 預設： ) *[sensitive](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 一個 16 位元組的預共享連線關聯金鑰（CAK）。要啟用 MACsec，請在鏈路兩端配置匹配的 CAK 和 CKN。未指定時，RouterOS 會自動生成隨機值。 |
| **ckn**(*string*; 預設： ) | 一個 32 位元組的連線關聯名稱（CKN）。要啟用 MACsec，請在鏈路兩端配置匹配的 CAK 和 CKN。未指定時，RouterOS 會自動生成隨機值。 |
| **comment** (*string*; 預設： ) | 介面的簡短描述。 |
| **disabled** (*yes \| no*; 預設：**no**) | 更改介面是否被停用。 |
| **interface** (*name*; 預設： ) | 建立 MACsec 的乙太網介面名稱，每個乙太網介面僅限建立一個 MACsec 介面。 |
| **mtu** (*integer*; 預設：**1468**) | 設定最大傳輸單元。`l2mtu` 將根據關聯的 `interface` 自動設定（減去與 MACsec 封裝對應的 32 位元組）。`l2mtu` 無法更改。 |
| **name** (*string*; 預設：**macsec1**) | 介面的名稱。 |
| **profile** (*name*; 預設：**default**) | 設定 MACsec 配置檔案，用於確定點對點連線中的金鑰伺服器。 |
| **status** (*只讀：disabled \|initializing \| invalid \| negotiating \| open-encrypted*) | 顯示當前 MACsec 介面狀態。 |

### 配置檔案設定 {#profile-settings}

**子選單：** `/interface/macsec/profile`

MACsec 配置檔案的配置設定。

| 屬性 | 描述 |
| :-- | :-- |
| **name** (*string*; 預設： ) | 配置檔案的名稱。 |
| **server-priority**(*integer: 0..255*; 預設：**10**) | 設定用於確定點對點連線中金鑰伺服器的優先順序。值越低表示優先順序越高。如果優先順序相同，則 MAC 地址最低的介面將充當金鑰伺服器。 |
