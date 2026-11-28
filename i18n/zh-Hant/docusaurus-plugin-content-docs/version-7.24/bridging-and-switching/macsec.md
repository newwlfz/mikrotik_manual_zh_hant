---
title: "MACsec"
description: "MACsec 是以太網路的的安全性協定，使用 GCM-AES-128 加密提供機密性、完整性與驗證。RouterOS 支援使用手動金鑰設定的 MACsec，並提供有限的硬體加速，需要預共用金鑰才能在設備之間建立安全的 Layer2 連線。"
tags:
  - 'macsec'
source: https://manual.mikrotik.com/docs/7.24/bridging-and-switching/macsec
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

MACsec（Media Access Control Security）通訊協定是一種標準安全技術，用於乙太網路中，以確保透過實體媒介傳輸之資料的機密性、完整性與真實性。MACsec 由 IEEE 標準 802.1AE 定義。

MACsec 在乙太網路上使用 GCM-AES-128 加密，並保護所有 LAN 流量，包括 DHCP、ARP、LLDP 與更高層級通訊協定。

:::warning
RouterOS 的 MACsec 實作仍處於初期階段；**不支援**透過 [Dot1x](/docs/authentication-authorization-accounting/dot1x) 進行動態金鑰管理（需要手動設定金鑰），且硬體加速加密僅在部分產品上陸續推出。
:::

## 基本設定範例 {#basic-configuration-example}

假設 Host1 ether1 連接到 Switch ether1，且 Host2 ether1 連接到 Switch ether2。在此範例中，我們將建立兩組 MACsec 介面配對，並使用 bridge 在兩端設備之間建立安全的 Layer2 連線。

首先，在 Host1 與 Host2 上設定 MACsec 介面。我們只需指定乙太網路介面，RouterOS 會自動產生 Connectivity Association Key（CAK）與 connectivity association name（CKN）。使用 `print` 指令查看這些值：

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

在 Switch 設備上，若要啟用 MACsec，我們需要為適當的乙太網路介面設定相符的 CAK 與 CKN 值：

```ros
# Switch
/interface/macsec
add comment=Host1 cak=71a7c363794da400dbde595d3926b0e9 ckn=f2c4660060169391d29d8db8a1f06e5d4b84a128bad06ad43ea2bd4f7d21968f interface=ether1 name=macsec1
add comment=Host2 cak=dc47d94291d19a6bb26a0c393a1af9a4 ckn=e9bd0811dad1e56f06876aa7715de1855f1aee0baf5982ac8b508d4fc0f162d9 interface=ether2 name=macsec2
```

一旦預共用金鑰成功交換，MACsec Key Agreement（MKA）通訊協定便會啟動。MKA 負責確保鏈路上 MACsec 的持續運作，並決定點對點連線中由哪一端擔任 key server。key server 會產生 Secure Association Key（SAK），且僅與鏈路另一端的設備共用。此 SAK 用於保護通過該鏈路的所有資料流量。key server 會定期產生新的隨機 SAK，並透過點對點鏈路共用，以維持 MACsec 功能。

在 RouterOS 中，MACsec 介面可以像任何 Ethernet 介面一樣設定。它可以作為具有 IP 位址的可路由介面使用，或放入 bridge 中。在 Host1 與 Host2 上，我們將新增同一網路的 IP 位址。在 Switch 上，我們將使用 bridge。

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

最後，使用 ping 確認 Host1 可以連線到 Host2。

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

MACsec 介面的設定。

| Property | Description |
| :-- | :-- |
| **cak** (*string*; Default: ) *[sensitive](/docs/getting-started/configuration-management/list-of-menus-with-sensitive-parameters)* | 16 位元組的預先共用 connectivity association key（CAK）。若要啟用 MACsec，請在鏈路兩端設定相符的 CAK 與 CKN。若未指定，RouterOS 會自動產生隨機值。 |
| **ckn**(*string*; Default: ) | 32 位元組的 connectivity association name（CKN）。若要啟用 MACsec，請在鏈路兩端設定相符的 CAK 與 CKN。若未指定，RouterOS 會自動產生隨機值。 |
| **comment** (*string*; Default: ) | 介面的簡短描述。 |
| **disabled** (*yes \| no*; Default: **no**) | 變更介面是否停用。 |
| **interface** (*name*; Default: ) | 建立 MACsec 的 Ethernet 介面名稱，每個 Ethernet 僅限一個 MACsec 介面。 |
| **mtu** (*integer*; Default: **1468**) | 設定最大傳輸單位。`l2mtu` 會根據關聯的 `interface` 自動設定（扣除 MACsec 封裝所需的 32 位元組）。`l2mtu` 無法變更。 |
| **name** (*string*; Default: **macsec1**) | 介面名稱。 |
| **profile** (*name*; Default: **default**) | 設定 MACsec profile，用於判斷點對點連線中的 key server。 |
| **status** (*read-only: disabled \|initializing \| invalid \| negotiating \| open-encrypted*) | 顯示目前 MACsec 介面狀態。 |

### 設定檔設定 {#profile-settings}

**子選單：** `/interface/macsec/profile`

MACsec 設定檔的設定。

| 屬性 | 說明 |
| :-- | :-- |
| **name** (*string*; Default: ) | 設定檔名稱。 |
| **server-priority**(*integer: 0..255*; Default: **10**) | 設定點對點連線中用於決定 key server 的優先順序。數值越低表示優先順序越高。若優先順序相同，MAC 位址最小的介面將作為 key server。 |
