---
sidebar_key: "virtual-private-networks/pptp"
sidebar_position: 9
title: "PPTP"
sidebar_label: "PPTP"
description: "本頁介紹 MikroTik RouterOS 中 PPTP（點對點隧道協定）的實現，涵蓋用戶端和伺服器配置選項，包括認證方式、MTU/MRRU 設定以及 TCP 埠要求。文中還指出了安全方面的侷限性，並提供了用於 PPTP 用戶端連線的示例設定命令。"
tags:
  - 'pptp'
  - 'vpn'
source: https://manual.mikrotik.com/docs/7.24/virtual-private-networks/pptp
captured_at: '2026-11-04T11:34:56+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Point-to-Point Tunneling Protocol (PPTP) 是一種傳統 VPN 協定，旨在為遠端訪問連線封裝 PPP 流量。PPTP 受到許多作業系統和網路裝置的廣泛支援，因此在以相容性為首要需求的環境中，部署和配置都很簡單。

由於存在多個已知的加密和協定級漏洞，PPTP 不適合用於保護敏感或不可信的網路流量。其使用通常僅限於相容性場景、測試環境或加密強度不是主要需求的網路。

PPTP 不支援 IPv6 傳輸或 IPv6 流量轉發。

PPTP 使用 TCP 埠 1723 進行隧道管理，並使用 Generic Routing Encapsulation（GRE，IP 協定 47）進行資料傳輸，這些由 Internet Assigned Numbers Authority（IANA）分配。為使 PPTP 透過防火牆或路由器正確執行，必須允許並正確轉發 TCP 埠 1723 和 GRE 流量。

PPTP 為每個用戶端會話支援 PPP 身份驗證、加密和計費機制。身份驗證和計費可以在本地執行，也可以透過外部 RADIUS 伺服器執行。

## PPTP 用戶端 {#pptp-client}

### 屬性 {#properties}

| 屬性 | 描述 |
| :-- | :-- |
| **add-default-route** (*yes \| no*；預設：**no**) | 是否將 PPTP 遠端地址新增為預設路由。 |
| **allow** (*mschap2 \| mschap1 \| chap \| pap*；預設：**mschap2, mschap1, chap, pap**) | 允許的身份驗證方法。 |
| **connect-to** (*IP*；預設：) | PPTP 伺服器的遠端地址 |
| **default-route-distance** (*byte [0..255]*；預設：**1**) | 如果同時選擇了 add-default-route，則設定應用於自動建立的預設路由的距離值 |
| **dial-on-demand** (*yes \| no*；預設：**no**) | 僅在生成出站流量時才連線到 PPTP 伺服器。如果選中，則在連線尚未建立期間，將新增閘道器地址來自 10.112.112.0/24 網路的路由。 |
| **disabled** (*yes \| no*；預設：**yes**) | 介面是否被停用。預設情況下為停用狀態 |
| **keepalive-timeout** (*integer*；預設：**60**) | 設定 keepalive 超時時間（秒）。 |
| **max-mru** (*integer*；預設：**1450**) | 最大接收單元。PPTP 介面在不進行封包分片的情況下能夠接收的最大封包大小。 |
| **max-mtu** (*integer*；預設：**1450**) | 最大傳輸單元。PPTP 介面在不進行封包分片的情況下能夠傳送的最大封包大小。 |
| **mrru** (*disabled \| integer*；預設：**disabled**) | 鏈路上能夠接收的最大封包大小。如果封包大於隧道 MTU，它將被拆分為多個數據包，從而允許透過隧道傳送完整大小的 IP 或乙太網封包。 |
| **name** (*string*；預設：) | 介面的描述性名稱。 |
| **password** (*string*；預設：**""**) *[敏感](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 用於身份驗證的密碼。 |
| **profile** (*name*；預設：**default-encryption**) |  |
| **user** (*string*；預設：) | 用於身份驗證的使用者名稱。 |

## PPTP 伺服器 {#pptp-server}

**子選單：** `/interface/pptp-server`

為每個建立到指定伺服器的隧道建立一個介面。PPTP 伺服器配置中有兩種型別的介面：

- 如果需要引用為特定使用者建立的特定介面名稱（在防火牆規則或其他位置），則透過管理方式新增靜態介面。
- 每當使用者連線且其使用者名稱不匹配任何現有靜態條目時（或者在該條目已經處於活動狀態的情況下，因為不能有兩個單獨的隧道介面使用同一名稱引用），動態介面會自動新增到此列表。

動態介面在使用者連線時出現，並在使用者斷開連線後消失，因此無法在路由器配置（例如防火牆）中引用為該使用者建立的隧道。因此，如果該使用者需要持久規則，請為其建立靜態條目。否則，使用動態配置是安全的。

:::warning
無論哪種情況，都必須正確配置 PPP 使用者——靜態條目不能替代 PPP 配置。
:::

### *屬性* {#properties-1}

| 屬性 | 描述 |
| :-- | :-- |
| **authentication** (*pap \| chap \| mschap1 \| mschap2*；預設：**mschap1,mschap2**) | 伺服器將接受的身份驗證方法。 |
| **default-profile** (*name*；預設：**default-encryption**) |  |
| **enabled** (*yes \| no*；預設：**no**) | 定義 PPTP 伺服器是否啟用。 |
| **keepalive-timeout** (*time*；預設：**30**) | 如果伺服器在 keepalive 週期內未收到任何封包，它將每秒傳送 keepalive 封包，共傳送五次。如果伺服器未收到用戶端響應，則在 5 秒後斷開連線。日誌將顯示 5 條 "LCP missed echo reply" 訊息，然後斷開連線。 |
| **max-mru** (*integer*；預設：**1450**) | 最大接收單元。PPTP 介面在不進行封包分片的情況下能夠接收的最大封包大小。 |
| **max-mtu** (*integer*；預設：**1450**) | 最大傳輸單元。PPTP 介面在不進行封包分片的情況下能夠傳送的最大封包大小。 |
| **mrru** (*disabled \| integer*；預設：**disabled**) | 鏈路上能夠接收的最大封包大小。如果封包大於隧道 MTU，它將被拆分為多個數據包，從而允許透過隧道傳送完整大小的 IP 或乙太網封包。 |

## 示例 {#example}

![](/img/35df5d1aa3979ebf.webp)

### PPTP 用戶端 {#pptp-client-1}

以下示例演示如何設定使用者名稱為 "MT-User"、密碼為 "StrongPass"、伺服器為 192.168.62.2 的 PPTP 用戶端：

```ros
[admin@MikroTik] > /interface/pptp-client/add connect-to=192.168.62.2 disabled=no name=pptp-out1 password=StrongPass user=MT-User
[admin@MikroTik] > /interface/pptp-client/print 
Flags: X - disabled; R - running 
 0  R name="pptp-out1" max-mtu=1450 max-mru=1450 mrru=disabled connect-to=192.168.62.2 user="MT-User" 
      password="StrongPass" profile=default-encryption keepalive-timeout=60 add-default-route=no 
      dial-on-demand=no allow=pap,chap,mschap1,mschap2 
```

### PPTP 伺服器 {#pptp-server-1}

在另一端，我們只需啟用 PPTP 伺服器併為特定使用者建立 PPP secret：

```ros
[admin@MikroTik] >  /interface/pptp-server/server/set enabled=yes
[admin@MikroTik] >  /ppp/secret/add local-address=10.0.0.1 name=MT-User password=StrongPass profile=default-encryption remote-address=10.0.0.5 service=pptp
[admin@MikroTik] >  interface pptp-server print
Flags: D - dynamic; R - running
Columns: NAME, USER, MTU, CLIENT-ADDRESS, UPTIME, ENCODING
#      NAME            USER     MTU  CLIENT-ADDRESS  UPTIM  ENCODING         
0  DR  <pptp-MT-User>  MT-User  1450  192.168.51.3   44m8s  MPPE128 stateless
```
