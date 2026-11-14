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
source: https://manual.mikrotik.com/docs/7.25/virtual-private-networks/sstp
captured_at: '2026-11-04T11:23:24+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Secure Socket Tunneling Protocol (SSTP) 將 Point-to-Point Protocol (PPP) 流量封裝在 Transport Layer Security (TLS) 會話中，以透過網際網路提供安全的遠端訪問。SSTP 透過 TCP 埠 443 使用 HTTPS，使 VPN 流量能夠穿過大多數防火牆、網路地址轉換（NAT）裝置和通常允許標準 Web 流量的代理伺服器。

SSTP 透過 TLS 支援強加密、身份驗證和資料完整性，有助於保護傳輸中的資料免遭截獲或篡改。由於依賴 TCP，SSTP 可以在不穩定的網路條件下提供可靠的連線，但與基於 UDP 的 VPN 協定相比，它會帶來額外的開銷。

SSTP 常用於其他 VPN 協定（例如 PPTP、L2TP/IPsec 或使用非標準埠的 OpenVPN）被網路限制阻止的環境。

## 簡介 {#introduction}

SSTP 連線機制：

![](/img/bf2c8b57ee4c0808.webp)

1. 從用戶端到伺服器建立 TCP 連線（預設使用埠 443）。
2. SSL 驗證伺服器證書。如果證書有效，則建立連線；否則連線被拒絕（參見下面的說明）。
3. 用戶端在 HTTPS 會話內傳送 SSTP 控制封包，從而在雙方建立 SSTP 狀態機。
4. 透過 SSTP 進行 PPP 協商。用戶端向伺服器進行身份驗證，並將 IP 地址繫結到 SSTP 介面。

此時 SSTP 隧道已建立，可以開始封包封裝。

:::warning
從 v5.0beta2 開始，SSTP 無需證書即可執行，並且可以使用任何可用的認證型別。此功能僅在兩個 MikroTik 路由器之間有效，因為它不符合 Microsoft 標準。否則，要建立安全隧道，應使用 **mschap** 認證以及來自同一證書鏈的用戶端/伺服器證書。

**警告：** 從 7.15beta10 版本開始，已新增 TLS SNI 支援；如果勾選了“Add SNI”複選框或在 CLI 中設定，則會將擴充套件新增到 client hello 封包中：

`/interface/sstp-client/set` add-sni=yes
:::

## 證書 {#certificates}

要建立安全的 SSTP 隧道，需要證書。在伺服器上，身份驗證僅透過使用者名稱和密碼完成；而在用戶端上，伺服器透過伺服器證書進行身份驗證。用戶端還使用該證書以加密方式繫結 SSL 和 PPP 身份驗證——用戶端透過 SSTP 連線向伺服器傳送一個特殊值，該值由 PPP 身份驗證期間生成的金鑰資料和伺服器證書派生而來。這使伺服器能夠檢查兩個通道是否安全。

如果 SSTP 用戶端位於 Windows PC 上，使用自簽名證書建立安全 SSTP 隧道的唯一方法是在 SSTP 伺服器上匯入“伺服器”證書，並在 Windows PC 的[受信任根](https://technet.microsoft.com/en-us/library/dd458982.aspx)中新增 CA 證書。

:::warning
如果伺服器證書由 Windows 已知的 CA 頒發，則 Windows 用戶端無需向受信任根儲存額外匯入任何證書即可工作。

**注意：** 如果 SSTP 使用證書，RSA 金鑰長度必須至少為 472 位。更短的金鑰被視為安全威脅。
:::

在 RouterOS 用戶端上，類似的配置是匯入 CA 證書並啟用 verify-server-certificate 選項。在這種情況下，不可能發生中間人攻擊。

在兩臺 MikroTik 路由器之間，也可以建立不帶證書的不安全隧道。在這種情況下，透過 SSTP 隧道傳輸的資料使用匿名 DH，中間人攻擊很容易實現。此方案與 Windows 用戶端不相容。

也可以透過使用用戶端證書新增額外授權來建立安全的 SSTP 隧道。配置要求如下：

- 伺服器和用戶端均需證書。
- 伺服器和用戶端均啟用驗證選項。

此方案無法用於 Windows 用戶端，因為無法在 Windows 上設定用戶端證書。

#### 證書錯誤訊息 {#certificate-error-messages}

當 SSL 握手失敗時，你會看到以下證書錯誤之一：

- **證書尚未生效** - 證書的 notBefore 日期晚於當前時間。
- **證書已過期** - 證書到期日期早於當前時間。
- **證書用途無效** - 提供的證書無法用於指定用途。
- **證書鏈中存在自簽名證書** - 證書鏈可以用不受信任的證書構建，但無法在本地找到根證書。
- **無法在本地獲取頒發者證書** - CA 證書未在本地匯入。
- **伺服器 IP 地址與證書不匹配** - 已啟用伺服器地址驗證，但證書中提供的地址與伺服器地址不匹配。

## 快速示例 {#quick-example}

![](/img/4d5265d637905a20.webp)

### SSTP 用戶端 {#sstp-client}

此示例建立一個不帶證書的簡單 SSTP 用戶端：

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

Configure a PPP secret for a particular user, then enable the SSTP server:

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
