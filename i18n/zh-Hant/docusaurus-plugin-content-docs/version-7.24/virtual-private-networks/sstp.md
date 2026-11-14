---
sidebar_key: "virtual-private-networks/sstp"
sidebar_position: 10
title: "SSTP"
sidebar_label: "SSTP"
description: "SSTP 使用 TLS 加密透過 HTTPS 提供安全的遠端訪問，使 VPN 連線能夠穿過防火牆和 NAT 裝置。本頁面詳細介紹了 SSTP 用戶端和伺服器屬性，包括身份驗證、加密設定以及 MikroTik RouterOS 的連線管理選項。"
tags:
  - 'sstp'
  - 'vpn'
  - 'tls'
source: https://manual.mikrotik.com/docs/7.24/virtual-private-networks/sstp
captured_at: '2026-11-04T11:34:48+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Secure Socket Tunneling Protocol (SSTP) 將 Point-to-Point Protocol (PPP) 流量封裝在 Transport Layer Security (TLS) 會話中，以透過網際網路提供安全的遠端訪問。SSTP 透過 TCP 埠 443 使用 HTTPS，使 VPN 流量能夠穿過大多數防火牆、網路地址轉換（NAT）裝置和通常允許標準 Web 流量的代理伺服器。

SSTP 透過 TLS 支援強加密、認證和資料完整性，有助於保護傳輸中的資料免受攔截或篡改。由於依賴 TCP，SSTP 可以在不穩定的網路條件下提供可靠連線，儘管與基於 UDP 的 VPN 協定相比，它可能會引入額外開銷。

SSTP 常用於其他 VPN 協定（例如 PPTP、L2TP/IPsec，或執行在非標準埠上的 OpenVPN）可能被網路限制阻止的環境。

## 簡介 {#introduction}

讓我們看一下 SSTP 連線機制：

![](/img/bf2c8b57ee4c0808.webp)

1. 從用戶端到伺服器建立 TCP 連線（預設使用埠 443）。
2. SSL 驗證伺服器證書。如果證書有效，則建立連線；否則，連線將被拒絕。（但請參見下面的註釋）。
3. 用戶端在 HTTPS 會話內傳送 SSTP 控制封包，從而在兩端建立 SSTP 狀態機。
4. 透過 SSTP 進行 PPP 協商。用戶端向伺服器認證，並將 IP 地址繫結到 SSTP 介面。

此時 SSTP 隧道已建立，可以開始封包封裝。

:::warning
從 v5.0beta2 開始，SSTP 無需證書即可執行，並且可以使用任何可用的認證型別。此功能僅在兩臺 MikroTik 路由器之間有效，因為它不符合 Microsoft 標準。否則，要建立安全隧道，應使用 **mschap** 認證以及來自同一證書鏈的用戶端/伺服器證書。

**警告：** 從 7.15beta10 版本開始已新增 TLS SNI 支援；如果勾選 "Add SNI" 複選框或在 CLI 中設定，則擴充套件會被新增到 Client Hello 封包中：

`/interface/sstp-client/set` add-sni=yes
:::

## SSTP 用戶端 {#sstp-client}

### 屬性 {#properties}

|  |  |
| :-- | :-- |
| **authentication** (*chap, mschap1, mschap2, pap*; 預設： **"all"**) | 允許的認證方法，預設允許所有方法。 |
| **disabled** (*yes \| no*; 預設： **yes**) | 啟用/停用隧道。 |
| **add-default-route** (*yes \| no*; 預設： **no**) | 是否將 SSTP 遠端地址新增為預設路由。 |
| **default-route-distance** (*byte*; 預設： ) | 如果同時選擇了 add-default-route，則設定應用於自動建立的預設路由的距離值。 |
| **mrru** (*integer: 512..65535\|disabled*; 預設： **disabled**) | 鏈路上可接收的最大封包大小。如果封包大於隧道 MTU，它將被拆分為多個數據包，從而允許透過隧道傳送全尺寸 IP 或乙太網封包。 |
| **proxy-port** (*integer*; 預設： **443** ) | 設定代理埠。 |
| **add-sni** (*yes \| no*; 預設： **no**) | 啟用/停用服務。 |
| **dial-on-demand** (*yes \| no*; 預設： **no**) | 僅在產生出站流量時連線。如果選擇此項，則在連線尚未建立時會新增一條閘道器地址來自 10.112.112.0/24 網路的路由。 |
| **name** (*string*; 預設： ) | 介面的描述性名稱。 |
| **tls-version**(*any*\|*only-1.2*; 預設： **any**) | 指定允許使用的 TLS 版本。 |
| **numbers** (*integer;*) | 設定 ROS 中隧道的編號。 |
| **user** (*string*; 預設： ) | 用於認證的使用者名稱。 |
| **certificate** (*string*\|*none*; 預設： **none**) | 用戶端證書的名稱 |
| **http-proxy** (*string*; 預設： ) | 代理地址欄位。 |
| **password** (*string*; 預設： **""**) *[敏感](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 用於認證的密碼。 |
| **verify-server-address-from-certificate** (*yes\|no*; 預設： **no**) | SSTP 用戶端將驗證證書中的伺服器地址。 |
| **verify-server-certificate** (*yes\|no*; 預設： **no**) | SSTP 用戶端將驗證伺服器證書。 |
| **ciphers** (aes256-gcm-sha384 \| aes256-sha; 預設： **all**) | 允許的加密套件。 |
| **keepalive-timeout** (*integer*; 預設：**60**) | 設定 keepalive 超時時間，單位為秒。 |
| **pfs** (*yes \| no \| required* ; 預設： **no**) | 指定使用哪種 TLS 認證。當 pfs=yes 時，TLS 將使用 ECDHE-RSA- 和 DHE-RSA-。為獲得最高安全性，設定 pfs=required 將僅使用 ECDHE。 |
| **comment** (*string*; 預設： ) | 隧道的簡短描述。 |
| **max-mru** (*integer*; 預設： **1500**) | 最大接收單元。 |
| **max-mtu** (*integer*; 預設： **1500**) | 最大傳輸單元。 |
| **port** (*integer*; 預設： **443**) | 要連線的埠。 |
| **connect-to** (*IP\|IPv6*; 預設： ) | SSTP 伺服器的遠端地址。 |
| **profile** (*name*; 預設： **default**) | 指定建立隧道時將使用哪個 PPP 配置檔案。 |

## SSTP 伺服器 {#sstp-server}

### 屬性 {#properties-1}

|  |  |
| :-- | :-- |
| **authentication** (*chap, mschap1, mschap2, pap*; 預設： **"all"**) | 允許的認證方法，預設允許所有方法。 |
| **keepalive-timeout** (*integer*; 預設：**60**) | 設定 keepalive 超時時間，單位為秒。 |
| **port** (*string*; 預設： **443** ) | 設定使用的埠。 |
| **certificate** (*string*\|*none*; 預設： **none**) | 正在使用的證書名稱。 |
| **max-mru** (*integer*; 預設： **1500**) | 最大接收單元。 |
| **max-mtu** (*integer*; 預設： **1500**) | 最大傳輸單元。 |
| **tls-version**(*any*\|*only-1.2*; 預設： **any**) | 指定允許使用的 TLS 版本。 |
| **ciphers** (aes256-gcm-sha384 \| aes256-sha; 預設： **all**) | 允許的加密套件。 |
| **verify-client-certificate** (*yes\|no*; 預設： **no**) | SSTP 伺服器將驗證用戶端證書。 |
| **mrru** (*integer: 512..65535\|disabled*; 預設： **disabled**) | 鏈路上可接收的最大封包大小。如果封包大於隧道 MTU，它將被拆分為多個數據包，從而允許透過隧道傳送全尺寸 IP 或乙太網封包。 |
| **default-profile** (*name*; 預設： **default**) | 指定建立隧道時將使用哪個 PPP 配置檔案。 |
| **enabled** (*yes \| no*; 預設： **no**) | 啟用/停用服務。 |
| **pfs** (*yes \| no \| required* ; 預設： **no**) | 指定使用哪種 TLS 認證。當 pfs=yes 時，TLS 將使用 ECDHE-RSA- 和 DHE-RSA-。為獲得最高安全性，設定 pfs=required 將僅使用 ECDHE。 |

## 證書 {#certificates}

要建立安全的 SSTP 隧道，需要使用證書。在伺服器端，僅透過使用者名稱和密碼進行認證，但在用戶端，伺服器使用伺服器證書進行認證。用戶端還使用該證書以密碼學方式繫結 SSL 和 PPP 認證，這意味著用戶端透過 SSTP 連線向伺服器傳送一個特殊值，該值派生自 PPP 認證期間生成的金鑰資料和伺服器證書。這允許伺服器檢查兩個通道是否都安全。

如果 SSTP 用戶端位於 Windows PC 上，那麼在使用自簽名證書時，建立安全 SSTP 隧道的唯一方法是在 SSTP 伺服器上匯入 "server" 證書，並在 Windows PC 的[受信任根](https://technet.microsoft.com/en-us/library/dd458982.aspx)中新增 CA 證書。

:::warning
如果您的伺服器證書由 Windows 已知的 CA 頒發，那麼 Windows 用戶端無需向受信任根額外匯入任何證書即可工作。

**注意：** 如果證書由 SSTP 使用，RSA 金鑰長度必須至少為 472 位。較短的金鑰被視為安全威脅。
:::

在 RouterOS 用戶端上的類似配置是匯入 CA 證書並啟用 verify-server-certificate 選項。在此場景中，無法進行中間人攻擊。

在兩臺 Mikrotik 路由器之間，也可以完全不使用證書來建立不安全的隧道。在這種情況下，經過 SSTP 隧道的資料使用匿名 DH，中間人攻擊很容易得手。此場景與 Windows 用戶端不相容。

也可以透過使用用戶端證書新增額外授權來建立安全的 SSTP 隧道。配置要求如下：

- 伺服器和用戶端均需證書。
- 伺服器和用戶端均啟用驗證選項。

此場景也無法用於 Windows 用戶端，因為無法在 Windows 上設定用戶端證書。

#### 證書錯誤訊息 {#certificate-error-messages}

當 SSL 握手失敗時，您將看到以下證書錯誤之一：

- **證書尚未生效** - 證書的 notBefore 日期晚於當前時間。
- **證書已過期** - 證書到期日期早於當前時間。
- **證書用途無效** - 提供的證書不能用於指定用途。
- **證書鏈中存在自簽名證書** - 證書鏈可以使用不受信任的證書構建，但無法在本地找到根證書。
- **無法在本地獲取頒發者證書** - CA 證書未在本地匯入。
- **伺服器 IP 地址與證書不匹配** - 已啟用伺服器地址驗證，但證書中提供的地址與伺服器地址不匹配。

## 快速示例 {#quick-example}

![](/img/4d5265d637905a20.webp)

### SSTP 用戶端 {#sstp-client-1}

在以下配置示例中，我們將建立一個不使用證書的簡單 SSTP 用戶端：

```ros
[admin@MikroTik] > /interface/sstp-client/add connect-to=192.168.62.2 disabled=no name=sstp-out1 password=StrongPass profile=default-encryption user=MT-User
[admin@MikroTik] > /interface/sstp-client/print
```

Flags: X - disabled; R - running
 0  R name="sstp-out1" max-mtu=1500 max-mru=1500 mrru=disabled connect-to=192.168.62.2:443
      http-proxy=0.0.0.0:443 certificate=none verify-server-certificate=no
      verify-server-address-from-certificate=yes user="MT-User" password="StrongPass"
      profile=default-encryption keepalive-timeout=60 add-default-route=no dial-on-demand=no
      authentication=pap,chap,mschap1,mschap2 pfs=no tls-version=any

```

### SSTP Server

We will configure PPP secret for a particular user, and afterwards simply enable an SSTP server:

```ros
[admin@MikroTik] > /ppp/secret/add local-address=10.0.0.1 name=MT-User password=StrongPass remote-address=10.0.0.5 service=sstp
[admin@MikroTik] > /interface/sstp-server/server/set default-profile=default-encryption enabled=yes
[admin@MikroTik] > /interface/sstp-server/server/print
                    enabled: yes
                       port: 443
                    max-mtu: 1500
                    max-mru: 1500
                       mrru: disabled
          keepalive-timeout: 60
            default-profile: default-encryption
             authentication: pap,chap,mschap1,mschap2
                certificate: none
  verify-client-certificate: no
                        pfs: no
                tls-version: any
```

:::info
在 P2P 設定中，網路地址將與其他端點的本地地址相同。

**重要：** 與任何其他 PPP 隧道一樣，SSTP 也支援 BCP，這允許它將 SSTP 隧道與本地介面橋接。例如，在路由器透過 ether1 連線到網際網路、工作站和筆記型電腦連線到 ether2 的設定中，兩個本地網路都透過 SSTP 用戶端路由，並且它們不在同一廣播域中。此處使用了 BCP。
:::
