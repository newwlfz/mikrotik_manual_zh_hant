---
sidebar_key: "virtual-private-networks/openvpn"
sidebar_position: 7
title: "OpenVPN"
sidebar_label: "OpenVPN"
description: "OpenVPN 是一種安全的 VPN 協定，提供二層/三層隧道、IPv4/IPv6 支援，以及靈活的傳輸協定（UDP/TCP）。它支援用戶端-伺服器部署，具備可配置的身份驗證、加密演算法和路由管理。RouterOS 上的 OpenVPN 存在一些限制，例如缺少 LZO 壓縮和 NCP 自動協商，同時提供基於 TLS 的身份驗證以及可匯入的"
tags:
  - 'openvpn'
  - 'tls'
source: https://manual.mikrotik.com/docs/7.25/virtual-private-networks/openvpn
captured_at: '2026-11-04T11:23:15+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

OpenVPN 是一種基於 SSL/TLS 安全模型的 VPN 協定，廣泛用於在不受信任的網路上提供安全的遠端訪問和站點到站點連線。它支援二層和三層隧道模式，可根據部署需求傳輸乙太網幀或路由 IP 流量。

OpenVPN 同時支援 IPv4 和 IPv6 流量，並可跨多種網路拓撲執行。

OpenVPN 可用於多種平臺，包括 Linux、Windows、macOS 和其他作業系統。其配置結構在各平臺間基本一致，從而簡化了混合環境中的部署、維護和互操作。

OpenVPN 可透過 User Datagram Protocol (UDP) 或 Transmission Control Protocol (TCP) 執行，允許管理員選擇最適合其網路需求的傳輸協定。多個 VPN 會話可複用到單個 TCP 或 UDP 埠上。

OpenVPN 還可以透過 HTTP 和 SOCKS 代理伺服器執行，這有助於在出站連線受限的網路環境中使用。其靈活性、強大的加密支援以及廣泛的平臺相容性，使 OpenVPN 成為一種常用的 VPN 解決方案。

## 限制 {#limitations}

ROS 有自己的 OpenVPN 實現，但並非所有功能都受支援，並且並非所有不受支援的功能都已列出。值得注意的不受支援功能包括：

- LZO 壓縮（**已棄用**）。通常不建議使用壓縮。使用壓縮的 VPN 隧道容易受到 VORACLE 攻擊。
- NCP 自動協商。連線到 ROS OpenVPN 伺服器時，必須在 `.ovpn` 檔案中指定加密演算法。

OpenVPN 使用者名稱限制為 27 個字元，密碼限制為 1000 個字元。

## tls-crypt、tls-crypt v2 {#tls-crypt-tls-crypt-v2}

為改進 TLS 身份驗證，`tls-crypt` 支援已在版本 `7.17rc3` 中新增。

`tls-crypt` 和 `tls-crypt v2` 僅由 OVPN 用戶端在以下設定下支援：

- 伺服器配置中使用 `auth SHA256` 且沒有 `key-direction`。
- 用戶端配置中使用 `auth SHA256` 和 `key-direction 1`。

## 示例配置檔案 {#example-configuration-files}

[client-1.ovpn](pathname:///assets/291241994_client-1.ovpn)
[server-1.conf](pathname:///assets/291241995_server-1.conf)

## 示例 {#example}

### 設定概覽 {#setup-overview}

![](/img/0b0a9eebe9f16be2.webp)

假設辦公室公網 IP 地址為 `2.2.2.2`，並且兩個遠端 OVPN 用戶端需要訪問位於辦公室閘道器後面的 `10.5.8.20` 主機和 `192.168.55.0/24` 網路。

### 建立證書 {#creating-certificates}

所有證書都可以在 RouterOS 伺服器上使用證書管理器建立。[參見示例 >>](../authentication-authorization-accounting/certificates.md)

對於最簡單的設定，只需要 OVPN 伺服器證書。

### 伺服器配置 {#server-config}

第一步是建立用於分配用戶端地址的 IP 池，然後建立使用者賬戶。

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

也可以為 OVPN 用戶端準備 `.ovpn` 檔案，該檔案可以輕鬆匯入到終端裝置。**伺服器必須啟用所需的用戶端證書選項，匯出才能正常工作。**

```ros
/interface/ovpn-server/server/export-client-configuration ca-certificate=ca.crt  client-certificate=cert_e
xport_rw-client.crt  client-cert-key=cert_export_rw-client.key server-address=1.1.1.1 server=ovpn-server1 
```

:::info
確保路由器日期位於已安裝證書的有效期內。為避免證書驗證問題，請在伺服器和用戶端上都啟用 **NTP** 日期同步。
:::

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

也可以從 `.ovpn` 配置檔案匯入 OVPN 用戶端配置。該檔案通常由 OVPN 伺服器提供，並且已經包含所需配置，因此只需手動配置少量引數。

```ros
/interface/ovpn-client/import-ovpn-configuration ovpn-password=securepassword \
key-passphrase=certificatekeypassphrase ovpn-user=myuserid skip-cert-import=no 
```

OVPN 用戶端支援 TLS 認證。`tls-auth` 配置只能透過匯入 `.ovpn` 配置檔案來新增。tls-auth 需要生成共享金鑰，該金鑰必須包含在用戶端 `.ovpn` 配置檔案中。

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

```
non-null auth in GCM mode is supported.
```

### 推送路由 {#push-route}

推送路由支援已在 `7.14` 版本中新增。最大輸入限制為 1400 個字元或 37 條路由。IPv6 支援已在 `7.21_ab220` 版本中新增。
示例：`route network/IP [netmask] [gateway] [metric]`。

```ros
/interface/ovpn-server/server/set 0 push-routes-ipv6="fdaa::/64,2001:db8::/32"
```

### VRF 支援 {#vrf-support}

從 7.17 版本開始支援，並引入了若干配置變更。如果您使用的是最新版本，請參考此示例：

```ros
      /interface/ovpn-server/server
        add disabled=no certificate=yourcert auth=sha1 cipher=aes128-cbc require-client-certificate=yes protocol=tcp name=ovpn-server1 vrf=main
```
