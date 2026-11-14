---
sidebar_key: "virtual-private-networks/l2tp/index"
sidebar_position: 2
title: "L2TP"
sidebar_label: "L2TP"
description: "本頁面介紹 MikroTik RouterOS 的 L2TP 配置,涵蓋用戶端與伺服器的設定,包括 authentication methods、MTU/MRRU 設定、IPsec 整合,以及在 Layer Two Tunneling Protocol 場景下的動態介面管理。"
tags:
  - 'l2tp'
  - 'ppp'
  - 'ipsec'
source: https://manual.mikrotik.com/docs/7.24/virtual-private-networks/l2tp
captured_at: '2026-11-04T11:34:37+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本節涵蓋 L2TP 示例。可用於配置 LAC 和 LNS 場景以及相關的 L2TP 互操作案例。

<DocCardList />

二層隧道協定 "L2TP" 透過允許 L2 和 PPP 端點位於由分組交換網路互連的不同裝置上，擴充套件了 PPP 模型。L2TP 為每個 L2TP 連線包含 PPP 認證和計費。每個連線的完整認證和計費可以透過 RADIUS 用戶端或本地完成。L2TP 流量對控制包和封包均使用 UDP 協定。UDP 埠 1701 僅用於鏈路建立，後續流量使用任意可用的 UDP 埠（可能是也可能不是 1701）。這意味著，透過允許 UDP 流量路由透過防火牆或路由器，L2TP 可與大多數防火牆和路由器（即使使用 NAT）一起使用。L2TP 標準定義於 [RFC 2661](https://tools.ietf.org/html/rfc2661)。L2TPv3 支援在 7.1 版本中新增。它支援 IPv4 和 IPv6。

## 簡介 {#introduction}

將 L2TP 像任何其他隧道協定一樣使用（無論是否加密）可能很有用。L2TP 標準指出，加密資料最安全的方式是使用 L2TP over IPsec（請注意，這是 Microsoft L2TP 用戶端的預設模式），因為特定隧道的所有 L2TP 控制包和封包在 IPsec 系統看來都是同質的 UDP/IP 封包。

支援 Multilink PPP (MP)，以提供 MRRU（傳輸完整大小 1500 及更大封包的能力）以及透過 PPP 鏈路的橋接（使用 Bridge Control Protocol (BCP)，它允許透過 PPP 鏈路傳送原始乙太網幀）。透過這種方式，可以在沒有 EoIP 的情況下設定橋接。網橋中應具有管理性設定的 MAC 地址或類似乙太網的介面，因為 PPP 鏈路沒有 MAC 地址。

:::warning
L2TP 不為隧道流量提供加密機制。可使用 IPsec 提供額外的安全層。
:::

## L2TP 用戶端 {#l2tp-client}

### 屬性 {#properties}

| 屬性 | 描述 |
| :-- | :-- |
| **add-default-route** (*yes \| no*; 預設：**no**) | 是否將 L2TP 遠端地址新增為預設路由。 |
| **allow** (*mschap2 \| mschap1 \| chap \| pap*；預設：**mschap2, mschap1, chap, pap**) | 允許的身份驗證方法。 |
| **connect-to** (*IP\|IPv6*; 預設： ) | L2TP 伺服器的遠端地址（如果該地址位於 VRF 表中，則應指定 VRF）  `/interface/l2tp-client``add connect-to=192.168.88.1@vrf1 name=l2tp-out1 user=l2tp-client)`    |
| **comment** (*string*; Default: ) | 隧道的簡短描述。 |
| **default-route-distance** (*byte*; 預設： ) | 自 v6.2 起，如果還選擇了 add-default-route，則設定應用於自動建立預設路由的距離值 |
| **dial-on-demand** (*yes \| no*; 預設：**no**) | 僅在生成出站流量時才連線。如果選擇，則在連線尚未建立時會新增一條閘道器地址來自 10.112.112.0/24 網路的路由。 |
| **disabled** (*yes \| no*; 預設：**yes**) | 啟用/停用隧道。 |
| **keepalive-timeout** (*integer [1..4294967295]*; 預設：**60s**) | 自 v6.0rc13 起，隧道保活超時時間（秒）。 |
| **max-mru** (*integer*; 預設：**1450**) | 最大接收單元。L2TP 介面能夠在無封包分片的情況下接收的最大封包大小。 |
| **max-mtu** (*integer*; 預設：**1450**) | 最大傳輸單元。L2TP 介面能夠在無封包分片的情況下發送的最大封包大小。 |
| **mrru** (*disabled \| integer*；預設：**disabled**) | 鏈路上能夠接收的最大封包大小。如果封包大於隧道 MTU，它將被拆分為多個數據包，從而允許透過隧道傳送完整大小的 IP 或乙太網封包。 |
| **name** (*string*; 預設： ) | 介面的描述性名稱。 |
| **password** (*string*; 預設： **""**) *[敏感](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 用於認證的密碼。 |
| **profile** (*name*; 預設：**default-encryption**) | 指定建立隧道時將使用哪個 PPP 配置檔案配置。 |
| **user** (*string*; 預設： ) | 用於認證的使用者名稱。 |
| **use-ipsec** (*yes \| no*; 預設：**no**) | 當啟用此選項時，會新增動態 IPSec 對等體配置和策略（傳輸模式），以將 L2TP 連線封裝到 IPSec 隧道中。**警告：** 同一 NAT 後的多個 L2tp/ipsec 用戶端在此模式下將無法工作。要實現此類場景，請停用 use-ipsec，併為用戶端設定靜態策略，同時啟用 tunnel=yes、level=unique 設定。     |
| **allow-fast-path** (*yes \| no*; 預設： ) | 允許在 Linux 核心中不經額外處理轉發封包。 |
| **l2tp-proto-version** ( l2tpv2 *\| l2tpv3-ip \| l2tpv3-udp \| l2tpv3*; 預設： **l2tpv2** ) | 指定協定版本。 |
| **l2tpv3-cookie-length** ( 0 *\| 4-bytes \| 8-bytes* ; 預設： **0** ) | 配置 L2TPv3 偽線靜態會話 cookie。 |
| **l2tpv3-digest-hash** (*md5 \| none \| sha1* ; 預設：**md5** ) | 指定要使用的雜湊函式。 |
| **use-peer-dns** (*yes \| no \| exclusively*; 預設： **no**  ) | 使用對端 DNS。 |
| **copy-from** | 複製已建立的對等體。 |
| **src-address** | 指定源地址。 |
| **l2tpv3-circuit-id** | 設定虛擬電路識別符號，以繫結 L2TPv3 控制通道的一端。 |
| **ipsec-secret** (*string*; 預設： ) *[敏感](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 啟用 use-ipsec 時使用的預共享金鑰。 |

## L2TP 伺服器 {#l2tp-server}

對於建立到給定伺服器的每個隧道，都會建立一個介面。L2TP 伺服器配置中有兩種型別的介面：

- 如果需要引用為特定使用者建立的特定介面名稱（在防火牆規則或其他位置），則會以管理方式新增靜態介面。
- 每當使用者連線且其使用者名稱不匹配任何現有靜態條目時（或者在該條目已處於活動狀態的情況下，因為不能有兩個單獨的隧道介面以相同名稱引用），動態介面會自動新增到此列表。

動態介面在使用者連線時出現，並在使用者斷開連線後消失，因此無法在路由器配置中（例如在防火牆中）引用為該使用者建立的隧道，所以如果需要為該使用者設定持久規則，請為其建立靜態條目。否則，使用動態配置是安全的。

:::warning
無論哪種情況，都必須正確配置 PPP 使用者——靜態條目不能替代 PPP 配置。
:::

### 屬性 {#properties-1}

| 屬性 | 描述 |
| :-- | :-- |
| **authentication** (*pap \| chap \| mschap1 \| mschap2*; 預設：**mschap1,mschap2**) | 伺服器將接受的認證方法。 |
| **default-profile** (*name*; 預設：**default-encryption**) | 要使用的預設配置檔案 |
| **enabled** (*yes \| no*; 預設：**no**) | 定義是否啟用 L2TP 伺服器。 |
| **max-mru** (*integer*; 預設：**1450**) | 最大接收單元。L2TP 介面能夠在無封包分片的情況下接收的最大封包大小。 |
| **keepalive-timeout** (*integer*; 預設：**30**) | 如果伺服器在 keepalive-timeout 期間未收到任何封包，它將每秒傳送保活封包，共五次。如果伺服器仍未收到用戶端的任何響應，則用戶端將在 5 秒後斷開連線。日誌將顯示 5 條 "LCP missed echo reply" 訊息，然後斷開連線。 |
| **max-mtu** (*integer*; 預設：**1450**) | 最大傳輸單元。L2TP 介面能夠在無封包分片的情況下發送的最大封包大小。 |
| **use-ipsec** (*no \| yes \| require*; 預設：**no**) | 當啟用此選項時，會新增動態 IPSec 對等體配置，以適應大多數 L2TP 遠端接入（road-warrior）設定。當選擇 require 時，伺服器將僅接受那些封裝在 IPSec 隧道中的 L2TP 連線嘗試。 |
| **ipsec-secret** (*string*; 預設： ) *[敏感](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 啟用 use-ipsec 時使用的預共享金鑰 |
| **accept-proto-version** ( all *\|* l2tpv2 *\|* l2tpv3; 預設：**all** ) cli-only | 指定協定版本。 |
| **accept-pseudowire-type** ( all *\|* ether *\|* ppp; 預設：**all** ) | 為特定偽線型別設定偽線信令協定。 |
| **allow-fast-path** (*no \| yes*; 預設：**no** ) | 在 Linux 核心中不經額外處理轉發封包。 |
| **caller-id-type** ( ip-address *\|* number; 預設：**ip-address**) | 如果多個用戶端使用相同的源 IP 地址，請將 id 型別設定為 number。 |
| **max-sessions** ( unlimited / number; 預設：**unlimited** ) | 設定所需會話數。 |
| **one-session-per-host**( *no \| yes*; 預設：**no** ) | 允許每個主機一個會話。 |
| **l2tpv3-circuit-id** (預設： ) | 設定虛擬電路識別符號，以繫結 L2TPv3 控制通道的一端。 |
| **l2tpv3-cookie-length** (0 *\|* 4-bytes *\|* 8-bytes; 預設：**0** ) | 配置 L2TP 偽線靜態會話 cookie。 |
| **l2tpv3-digest-hash** ( md5 *\|* none *\|* sha1; 預設：**md5** ) | 指定要使用的雜湊函式。 |
| **l2tpv3-ether-interface-list** (預設： ) | 設定介面列表，例如預設的 all、dynamic、none、static。 |
| **mrru** (*disabled \| integer*; 預設：**disabled**) | 鏈路上可接收的最大封包大小。如果封包大於隧道 MTU，它將被拆分為多個數據包，從而允許透過隧道傳送完整大小的 IP 或乙太網封包。 |

## 快速示例 {#quick-example}

![](/img/f2cf148d94cfeff8.webp)

### L2TP 伺服器 {#l2tp-server-1}

在伺服器端，我們將啟用 L2TP-server 併為特定使用者建立 PPP 配置檔案：

```ros
[admin@MikroTik] > /interface/l2tp-server/server/set enabled=yes
[admin@MikroTik] > /ppp/secret/add local-address=10.0.0.2 name=MT-User password=StrongPass profile=default-encryption remote-address=10.0.0.1 service=l2tp
```

### L2TP 用戶端 {#l2tp-client-1}

RouterOS 中的 L2TP 用戶端設定非常簡單。在以下示例中，我們已經有一個預配置的 3 臺裝置設定。我們將更詳細地瞭解如何使用使用者名稱 "MT-User"、密碼 "StrongPass" 和伺服器 192.168.51.3 設定 L2TP 用戶端：

```ros
[admin@MikroTik] > /interface/l2tp-client \
add connect-to=192.168.51.3 disabled=no name=MT-User password=StrongPass user=MT-User
[admin@MikroTik] > /interface/l2tp-client/print 
Flags: X - disabled, R - running 
0 R name="MT-User" max-mtu=1450 max-mru=1450 mrru=disabled connect-to=192.168.51.3 user="MT-User" 
password="StrongPass" profile=default-encryption keepalive-timeout=60 use-ipsec=no ipsec-secret="" 
allow-fast-path=no add-default-route=no dial-on-demand=no allow=pap,chap,mschap1,mschap2
```

## L2TP Ether {#l2tp-ether}

## 概述 {#overview}

二層隧道協定版本 3（L2TPv3）由網際網路工程任務組（IETF）的 [RFC 3931](https://tools.ietf.org/html/rfc3931) 定義。它對原始 L2TP 引入了各種改進，允許在 L2TP 內封裝二層（L2）有效載荷。更準確地說，L2TPv3 概述了使用 L2 虛擬專用網路（VPN）跨越 IP 核心網路隧道傳輸二層有效載荷的協定。

要建立 **L2TP Ether** 隧道，必須在 **用戶端側** 建立 **L2TP Ether 介面**，同時必須在 **遠端（伺服器）側** 啟用 **L2TP 伺服器**。一旦兩側配置正確，它們之間會自動建立一個 **動態介面**，形成跨越 IP 網路的透明二層連線。

---

##### **伺服器側（L2TP 伺服器）** {#server-side-l2tp-server}

`/interface/l2tp-server/server/set enabled=yes`

##### **用戶端側（L2TP Ether 介面）** {#client-side-l2tp-ether-interface}

`/interface/l2tp-ether/add` connect-to=1.1.1.1 disabled=no

## 屬性 {#properties-2}

| 屬性 | 描述 |
| :-- | :-- |
| **connect-to** ( *IP*; 預設： ) | L2TP 伺服器的遠端地址。  |
| **comment** ( *string*; 預設： ) | 隧道的簡短描述。 |
| **disabled** ( *yes \| no*; 預設：**yes**) | 啟用/停用隧道。 |
| **mac-address** ( string; 預設：**auto**) | 設定介面所需的 MAC 地址。 |
| **unmanaged-mode** ( *yes \| no*; 預設：**no**) | 將非託管模式設定為活動狀態。將可以進行附加設定的配置，例如：**peer-cookie, send-cookie, local-tunnel-id, local-session-id, remote-tunnel-id, remote-session-id, local-address.** |
| **local-tunnel-id ( string; 預設：disabled)** | 設定 local-tunnel-id 的值；需要整數。 |
| **local-session-id ( string; 預設：disabled)** | 設定 local-session-id 的值；需要整數。 |
| **remote-tunnel-id (** string; 預設：**disabled)** | 設定 remote-tunnel-id 的值；需要整數。 |
| **remote-session-id (** string; 預設：**disabled)** | 設定 remote-session-id 的值；需要整數。 |
| **peer-cookie (** string; 預設：**disabled)** | 設定可選的對端 cookie。要啟用 cookie，請輸入遠端 cookie 值（應為 8 或 16 個字元的十六進位制字串值）；要停用，請留空。 |
| **send-cookie (** string; 預設：**disabled)** | 設定可選 cookie。要啟用 cookie，請輸入遠端 cookie 值（應為 8 或 16 個字元的十六進位制字串值）；要停用，請留空。 |
| **mtu** (*auto*; 預設：**1420**) | 最大傳輸單元。L2TP 介面能夠在無封包分片的情況下發送的最大封包大小。 |
| **name** (*string*; 預設： ) | 介面的描述性名稱。 |
| **local-address** (*IP address*; 預設： ) | 為 **非託管** 模式設定本地地址。 |
| **use-ipsec** (*yes \| no*; 預設：**no**) | 當啟用此選項時，會新增動態 IPSec 對等體配置和策略，以將 L2TP 連線封裝到 IPSec 隧道中。 |
| **allow-fast-path** (*yes \| no*; 預設：**no** ) | 允許在 Linux 核心中不經額外處理轉發封包。 |
| **l2tp-proto-version** ( *l2tpv3-ip \| l2tpv3-udp* ; 預設：***l2tpv3-udp***) | 指定協定版本。 |
| **cookie-length** ( 0 *\| 4-bytes \| 8-bytes* ; 預設： **0** ) | 配置 L2TPv3 偽線靜態會話 cookie。 |
| **digest-hash** (*md5 \| none \| sha1* ; 預設：**md5** ) | 指定要使用的雜湊函式。 |
| **use-l2-specific-sublayer** ( *yes \| no*; 預設：**no**) | 啟用 L2TPv3 乙太網偽線二層預設子層。 |
| **circuit-id** | 設定虛擬電路識別符號，以繫結 L2TPv3 控制通道的一端。這用作每個冗餘偽線的識別符號。 |
| **ipsec-secret** (*string*; 預設： ) *[敏感](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 啟用 use-ipsec 時使用的預共享金鑰。 |
