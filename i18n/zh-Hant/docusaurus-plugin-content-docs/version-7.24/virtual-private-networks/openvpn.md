---
sidebar_key: "virtual-private-networks/openvpn"
sidebar_position: 7
title: "OpenVPN"
sidebar_label: "OpenVPN"
description: "OpenVPN 是一種安全的 VPN 協定，提供二層/三層隧道、IPv4/IPv6 支援，以及靈活的傳輸協定（UDP/TCP）。它支援用戶端-伺服器部署，具備可配置的身份驗證、加密演算法和路由管理。RouterOS 上的 OpenVPN 存在一些限制，例如缺少 LZO 壓縮和 NCP 自動協商，同時提供基於 TLS 的身份驗證以及可匯入的"
tags:
  - 'openvpn'
  - 'tls'
source: https://manual.mikrotik.com/docs/7.24/virtual-private-networks/openvpn
captured_at: '2026-11-04T11:34:48+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

OpenVPN 是一種基於 SSL/TLS 安全模型的 VPN 協定，廣泛用於在不受信任的網路上提供安全的遠端訪問和站點到站點連線。它支援二層和三層隧道模式，可根據部署需求傳輸乙太網幀或路由 IP 流量。

OpenVPN 同時支援 IPv4 和 IPv6 流量，並可跨多種網路拓撲執行。

OpenVPN 可用於多種平臺，包括 Linux、Windows、macOS 和其他作業系統。其配置結構在各平臺間基本一致，從而簡化了混合環境中的部署、維護和互操作。

OpenVPN 可透過 User Datagram Protocol (UDP) 或 Transmission Control Protocol (TCP) 執行，允許管理員選擇最適合其網路需求的傳輸協定。多個 VPN 會話可複用到單個 TCP 或 UDP 埠上。

OpenVPN 還可以透過 HTTP 和 SOCKS 代理伺服器執行，這在出站連線受限的網路環境中可能很有用。其靈活性、強大的加密支援以及廣泛的平臺相容性使 OpenVPN 成為一種常用的 VPN 解決方案。

## 限制 {#limitations}

ROS 有自己的 OpenVPN 實現，但並非支援所有 OpenVPN 功能，並且並非所有不受支援的功能都會列出。目前，值得注意的不受支援的 OpenVPN 功能包括：

- LZO 壓縮。\*\*已棄用\*\* 通常不建議使用壓縮。使用壓縮的 VPN 隧道容易受到 VORACLE 攻擊。
- NCP 自動協商。連線到 ROS OpenVPN 伺服器時，必須在 `.ovpn` 檔案中指定 cipher。

OpenVPN 使用者名稱限制為 27 個字元，密碼限制為 233 個字元。從版本 `7.18_ab253` 開始，密碼限制已增加到 1000 個字元。

## OVPN 用戶端 {#ovpn-client}

| 屬性 | 描述 |
| :-- | :-- |
| **add-default-route** (*yes* \| *no*; 預設：**no**) | 是否將 OVPN 遠端地址新增為預設路由。 |
| **auth** (*md5* \| *sha1* \| *null* \| *sha256* \| *sha512*; 預設：**sha1**) | 允許的身份驗證方法。 |
| **certificate** (*string* \| *none*; 預設：**none**) | 用戶端證書的名稱 |
| **cipher** (*null* \| *aes128-cbc* \| *aes128-gcm* \| *aes192-cbc* \| *aes192-gcm* \| *aes256-cbc* \| *aes256-gcm* \| *blowfish128*; 預設：**blowfish128**) | 允許的加密演算法。為了使用 GCM 型別的加密演算法，必須將 "auth" 引數設定為 "null"，因為如果使用 GCM 加密演算法，它也負責 "auth"。 |
| **comment** (*string*; 預設： ) | 條目的描述性名稱 |
| **connect-to** (*IP\|IPv6*; 預設： ) | OVPN 伺服器的遠端地址。 |
| **disabled** (*yes* \| *no*; 預設：**yes**) | 介面是否被停用。預設情況下為停用狀態。 |
| **mac-address** (*MAC*; 預設： ) | OVPN 介面的 MAC 地址。如果未指定，將自動生成。 |
| **max-mtu** (*integer*; 預設：**1500**) | 最大傳輸單元。OVPN 介面能夠在不進行分片的情況下發送的最大封包大小。 |
| **mode** (*ip* \| *ethernet*; 預設：**ip**) | 三層或二層隧道模式（也可稱為 tun、tap） |
| **name** (*string*; 預設： ) | 介面的描述性名稱。 |
| **password** (*string*; 預設：**""**) *[敏感](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 用於身份驗證的密碼。密碼值長度不應超過 1000 個字元。 |
| **port** (*integer*; 預設：**1194**) | 要連線到的埠。 |
| **profile** (*name*; 預設：**default**) | 指定建立隧道時將使用哪個 PPP 配置檔案配置。 |
| **protocol** (*tcp*\| *udp*; 預設：**tcp**) | 指示與遠端端點連線時要使用的協定。 |
| **verify-server-certificate**(*yes* \| *no*; 預設：**no**) | 將證書的 CN 或 SAN 與 "connect-to" 引數進行核對。IP 或主機名必須存在於伺服器證書中。 |
| **tls-version** (*any*\|*only-1.2*; 預設：**any**) | 指定允許使用哪些 TLS 版本 |
| **use-peer-dns**(*yes* \| *no*; 預設：**no**) | 是否將 OVPN 伺服器提供的 DNS 伺服器新增到 IP/DNS 配置中。 |
| **route-nopull** (*yes* \| *no*; 預設：**no**) | 指定是否允許 OVPN 伺服器向 OVPN 用戶端例項路由表新增路由。 |
| **user** (*string*; 預設： ) | 用於身份驗證的使用者名稱。 |

也可以從 `.ovpn` 配置檔案匯入 OVPN 用戶端配置。該檔案通常由 OVPN 伺服器提供，並且已經包含所需配置，因此只需手動配置少量引數。

```ros
/interface/ovpn-client/import-ovpn-configuration ovpn-password=securepassword \
key-passphrase=certificatekeypassphrase ovpn-user=myuserid skip-cert-import=no 
```

OVPN 用戶端支援 TLS 身份驗證。`tls-auth` 配置只能透過匯入 `.ovpn` 配置檔案來新增。使用 `tls-auth` 需要生成共享金鑰，並且該金鑰必須包含在用戶端 `.ovpn` 配置檔案中。

ROS 用戶端需要使用者名稱和密碼。身份驗證由伺服器端管理。如果伺服器支援 TLS 身份驗證，則使用者名稱會被忽略。

```ros
key-direction 1
<tls-auth>
#
# 2048 bit OpenVPN static key
#
-----BEGIN OpenVPN Static key V1-----
-----END OpenVPN Static key V1-----
</tls-auth>
```

```ros
7.17beta5 added support to allow non-null auth in gcm mode.
```

## Tls-crypt、tls-crypt v2 {#tls-crypt-tls-crypt-v2}

為改進 TLS 身份驗證，`tls-crypt` 支援已在版本 `7.17rc3` 中新增。

`tls-crypt` 和 `tls-crypt v2` 僅由 OVPN 用戶端在以下設定下支援：

- 伺服器配置中使用 `auth SHA256` 且沒有 `key-direction`；
- 用戶端配置中需要使用 `auth SHA256` 和 `key-direction 1`，身份驗證才能正常工作。

## 示例配置檔案 {#example-configuration-files}

[client-1.ovpn](pathname:///assets/291241994_client-1.ovpn)
[server-1.conf](pathname:///assets/291241995_server-1.conf)

## OVPN 伺服器 {#ovpn-server}

**子選單：** `/interface/ovpn-server`

為連線到指定伺服器的每個隧道建立一個介面。OVPN 伺服器配置中有兩種型別的介面：

- 靜態介面是在需要引用為特定使用者建立的特定介面名稱時（例如在防火牆規則或其他位置）由管理員手動新增的介面。
- 當用戶連線且其使用者名稱與任何現有靜態條目都不匹配時，或者匹配的靜態條目已經處於活動狀態時，動態介面會自動新增到此列表中，因為兩個獨立的隧道介面不能使用相同名稱。

動態介面在使用者連線時出現，並在使用者斷開連線後消失。因此，無法在路由器配置中（例如在防火牆規則中）引用為該使用者建立的隧道。如果需要對使用者使用持久規則，請建立靜態條目。否則，動態配置就足夠了。

:::warning
升級到版本 `7.17` 後，由於支援多個伺服器，OVPN 伺服器會獲得自己的配置。

配置中會出現一個已停用且已分配 MAC 地址的 OVPN 伺服器：
`/interface/ovpn-server/server/add mac-address=99:99:99:99:99:99 name=ovpn-server1`

**警告：** 在這兩種情況下，都必須正確配置 PPP 使用者。靜態條目不能替代 PPP 配置。
:::

### 伺服器配置 {#server-configuration}

#### 屬性 {#properties}

| 屬性 | 描述 |
| :-- | :-- |
| **auth** (*md5* \| *sha1* \| *null* \| *sha256* \| *sha512*; 預設：**sha1,md5,sha256,sha512**) | 伺服器將接受的身份驗證方法。 |
| **certificate** (*name* \| *none*; 預設：**none**) | OVPN 伺服器將使用的證書名稱。 |
| **cipher** (*null* \| *aes128-cbc* \| *aes128-gcm* \| *aes192-cbc* \| *aes192-gcm* \| *aes256-cbc* \| *aes256-gcm* \| *blowfish128*; 預設：**aes128-cbc,blowfish128**) | 允許的加密演算法。 |
| **default-profile** (*name*; 預設：**default**) | 要使用的預設配置檔案。 |
| **disabled** (*yes* \| *no*; 預設：**yes**) | 定義 OVPN 伺服器是否啟用。 |
| **protocol (*tcp*\| *udp*; 預設：tcp)** | 指示與遠端端點連線時要使用的協定。 |
| **keepalive-timeout** (*integer* \| *disabled*; 預設：**60**) | 定義時間週期（以秒為單位），經過該時間後路由器開始每秒傳送 keepalive 封包。如果在該時間段內（即 2 \* keepalive-timeout）沒有流量且沒有收到 keepalive 響應，則未響應的用戶端會被宣佈為斷開連線 |
| **mac-address** (*MAC*; 預設： ) | 伺服器自動生成的 MAC 地址。 |
| **max-mtu** (*integer*; 預設：**1500**) | 最大傳輸單元。OVPN 介面能夠在不進行分片的情況下發送的最大封包大小。 |
| **mode** (*ip* \| *ethernet*; 預設：**ip**) | 三層或二層隧道模式（也可稱為 tun、tap） |
| **name** *(string)* | 伺服器名稱 |
| **netmask** (*integer*; 預設：**24**) | 應用於用戶端的子網掩碼。 |
| **port** (*integer*; 預設：**1194**) | 執行伺服器的埠。 |
| **require-client-certificate** (*yes* \| *no*; 預設：**no**) | 如果設定為 yes，則伺服器會檢查用戶端證書是否屬於同一證書鏈。 |
| **redirect-gateway** (*def1* \| *disabled* \| *ipv6;* 預設：**disabled**) | 指定 OVPN 用戶端必須向路由表新增何種路由。`def1` – 使用此標誌可透過 0.0.0.0/1 和 128.0.0.0/1 而不是 0.0.0.0/0 來覆蓋預設閘道器。這樣做的好處是覆蓋但不消除原始預設閘道器。`disabled` - 不向 OVPN 用戶端傳送 redirect-gateway 標誌。`ipv6` - 在用戶端將 IPv6 路由重定向到隧道中。其工作方式與 def1 標誌類似，即新增更具體的 IPv6 路由（2000::/4 和 3000::/4），覆蓋整個 IPv6 單播空間。 |
| **enable-tun-ipv6** (y*es* \| *no;* 預設：**no**) | 指定此 OVPN 伺服器是否應支援 IPv6 IP 隧道模式。 |
| **ipv6-prefix-len** (*integer;* 預設：**64**) | 在伺服器端生成 OVPN 介面時將使用的 IPv6 地址的 IPv6 字首長度。 |
| **reneg-sec** (*integer;* 預設：**3600)** | 金鑰重新協商秒數，即伺服器定期為資料通道重新協商金鑰的時間。 |
| **push-routes** (*string*; 預設： ) | 推送路由支援已在 7.14 中新增，最大可能輸入限制為 1400 個字元或 37 條推送路由。IPv6 支援已在 7.21\_ab220 中新增。 |
| **tls-version** (any\| *only-1.2 ;* 預設：**any** ) | TLS 協定設定。 |
| **tun-server-ipv6** (*IPv6 prefix;* 預設：**::**) | 在伺服器端生成 OVPN 介面時將使用的 IPv6 字首地址。 |
| **user-auth-method** (*mschap2 \| pap ; 預設 **pap***) | 預設使用 pap 身份驗證方法；如果希望伺服器使用 chap 質詢進行身份驗證，請在伺服器設定中設定 mschap2。 |
| **vrf** () | 用於監聽連線嘗試的 VRF |

也可以為 OVPN 用戶端準備 `.ovpn` 檔案，該檔案可以輕鬆匯入到終端裝置。**伺服器必須啟用所需的用戶端證書選項，匯出才能正常工作。**

```ros
/interface/ovpn-server/server/export-client-configuration ca-certificate=ca.crt  client-certificate=cert_e
xport_rw-client.crt  client-cert-key=cert_export_rw-client.key server-address=1.1.1.1 server=ovpn-server1 
```

:::info
路由器的日期處於已安裝證書的有效期內非常重要。為避免證書驗證問題，請在伺服器和用戶端上都啟用 **NTP** 日期同步。
:::

## 示例 {#example}

### 設定概覽 {#setup-overview}

![](/img/0b0a9eebe9f16be2.webp)

假設辦公室公網 IP 地址為 `2.2.2.2`，並且兩個遠端 OVPN 用戶端需要訪問位於辦公室閘道器後面的 `10.5.8.20` 主機和 `192.168.55.0/24` 網路。

### 建立證書 {#creating-certificates}

所有證書都可以使用證書管理器在 RouterOS 伺服器上建立。[參見示例 >>](../authentication-authorization-accounting/certificates.md)

對於最簡單的設定，只需要 OVPN 伺服器證書。

### 伺服器配置 {#server-config}

第一步是建立將從中分配用戶端地址的 IP 池，然後建立使用者賬戶。

```ros
/ip/pool/add name=ovpn-pool range=192.168.77.2-192.168.77.254

/ppp/profile/add name=ovpn local-address=192.168.77.1 remote-address=ovpn-pool
/ppp/secret
add name=client1 password=123 profile=ovpn
add name=client2 password=234 profile=ovpn
```

假設伺服器證書已經建立，並且名稱為 `server`。

```ros
/interface/ovpn-server/server/add disabled=no certificate=server name=myServer
```

### 用戶端配置 {#client-config}

手動新增希望透過隧道訪問的網路。

```ros
/interface/ovpn-client
add name=ovpn-client1 connect-to=2.2.2.2 user=client1 password=123 disabled=no
/ip/route 
add dst-address=10.5.8.20 gateway=ovpn-client1
add dst-address=192.168.55.0/24 gateway=ovpn-client1
/ip/firewall/nat/add chain=srcnat action=masquerade out-interface=ovpn-client1
```

### 推送路由 {#push-route}

推送路由支援已在版本 `7.14` 中新增。最大輸入限制為 \*\*1400\*\* 個字元或 37 條路由。IPv6 支援已在版本 `7.21_ab220` 中新增。  
示例：`route network/IP [netmask] [gateway] [metric]`。

```ros
/interface/ovpn-server/server/set 0 push-routes-ipv6="fdaa::/64,2001:db8::/32"
```

### VRF 支援 {#vrf-support}

從 \*\*版本 7.17\*\* 開始添加了支援，並引入了若干配置更改。如果您使用的是最新版本，請參考此示例：

```ros
      /interface/ovpn-server/server
        add disabled=no certificate=yourcert auth=sha1 cipher=aes128-cbc require-client-certificate=yes protocol=tcp name=ovpn-server1 vrf=main
```
