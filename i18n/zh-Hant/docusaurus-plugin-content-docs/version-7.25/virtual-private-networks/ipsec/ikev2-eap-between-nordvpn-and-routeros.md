---
sidebar_key: "virtual-private-networks/ipsec/ikev2-eap-between-nordvpn-and-routeros"
sidebar_position: 1
title: "NordVPN 與 RouterOS 之間的 IKEv2 EAP"
sidebar_label: "NordVPN 與 RouterOS 之間的 IKEv2 EAP"
description: "本頁指導使用者在 RouterOS v6.45+ 中使用 EAP 認證配置到 NordVPN 伺服器的 IKEv2 加密隧道，涵蓋根 CA 安裝、伺服器主機名查詢、帶 Phase 1/2 配置檔案和策略的 IPsec 隧道設定、用於 EAP 認證的模式配置，以及對端/身份憑據設定。"
tags:
  - 'ikev2'
  - 'ipsec'
  - 'vpn'
source: https://manual.mikrotik.com/docs/7.25/virtual-private-networks/ipsec/ikev2-eap-between-nordvpn-and-routeros
captured_at: '2026-11-04T11:23:16+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

從 RouterOS v6.45 開始，可以使用 EAP 認證與 NordVPN 伺服器建立 IKEv2 安全隧道。本手冊頁說明如何配置。

![](/img/fd0c91032452ce11.webp)

### 安裝根 CA {#installing-the-root-ca}

首先下載並匯入 NordVPN 根 CA 證書。

```
/tool/fetch url="https://downloads.nordvpn.com/certificates/root.der"
/certificate/import file-name=root.der

```

現在 System/Certificates 選單中應該已有受信任的 NordVPN Root CA 證書。

```
[admin@MikroTik] > /certificate/print where name~"root.der"
Flags: K - private-key, L - crl, C - smart-card-key, A - authority, I - issued, R - revoked, E - expired, T - trusted 
 #         NAME            COMMON-NAME            SUBJECT-ALT-NAME                                         FINGERPRINT           
 0       T root.der_0      NordVPN Root CA                                                                 8b5a495db498a6c2c8c...

```

### 查詢伺服器的主機名 {#finding-out-the-servers-hostname}

訪問 [https://nordvpn.com/servers/tools/](https://nordvpn.com/servers/tools/) 並查詢推薦伺服器的主機名。在本例中，它是 lv20.nordvpn.com。

![](/img/691115748c0365fa.webp)

### 設定 IPsec 隧道 {#setting-up-the-ipsec-tunnel}

建議建立單獨的 Phase 1 配置檔案和 Phase 2 提議配置，以免干擾任何現有或未來的 IPsec 配置。

```
/ip/ipsec/profile
add name=NordVPN
/ip/ipsec/proposal
add name=NordVPN pfs-group=none

```

雖然可以使用預設策略模板生成策略，但最好建立新的策略組和模板，將此配置與任何其他 IPsec 配置分開。

```
/ip/ipsec/policy/group
add name=NordVPN
/ip/ipsec/policy
add dst-address=0.0.0.0/0 group=NordVPN proposal=NordVPN src-address=0.0.0.0/0 template=yes

```

建立一個 responder=no 的新 mode config 條目，該條目將從伺服器請求配置引數。

```
/ip/ipsec/mode-config
add name=NordVPN responder=no

```

最後，建立 peer 和 identity 配置。在 username 和 password 引數中指定你的 NordVPN 憑據。

```
/ip/ipsec/peer
add address=lv20.nordvpn.com exchange-mode=ike2 name=NordVPN profile=NordVPN
/ip/ipsec/identity
add auth-method=eap certificate="" eap-methods=eap-mschapv2 generate-policy=port-strict mode-config=NordVPN peer=NordVPN policy-template-group=NordVPN username=support@mikrotik.com password=secret

```

驗證連線已成功建立。

```
/ip/ipsec
active-peers print
installed-sa print

```

### 選擇透過隧道傳送的內容 {#choosing-what-to-send-over-the-tunnel}

如果檢視生成的動態策略，可以看到只有源地址為特定地址（由 mode config 接收）的流量才會透過隧道傳送。但在大多數情況下，路由器需要將特定裝置或網路路由到隧道中。在這種情況下，我們可以使用源 NAT 將封包的源地址更改為與 mode config 地址匹配。由於 mode config 地址是動態的，因此無法建立靜態源 NAT 規則。在 RouterOS 中，可以為 mode config 用戶端生成動態源 NAT 規則。

#### 選項 1：透過隧道傳送所有流量 {#option-1-sending-all-traffic-over-the-tunnel}

在此示例中，路由器後面有一個本地網路 10.5.8.0/24，我們希望將該網路的所有流量都透過隧道傳送。首先，我們必須建立一個包含本地網路的新 IP/Firewall/Address 列表。

```
/ip/firewall/address-list
add address=10.5.8.0/24 list=local
```

也可以僅指定單個主機，將其所有流量透過隧道傳送。示例：

```
/ip/firewall/address-list
add address=10.5.8.120 list=local
add address=10.5.8.23 list=local

```

完成後，我們可以將新建的 IP/Firewall/Address 列表分配給 mode config 配置。

```
/ip/ipsec/mode-config
set [ find name=NordVPN ] src-address-list=local
```

驗證隧道建立時會正確動態生成源 NAT 規則。

```
[admin@MikroTik] > /ip/firewall/nat/print 
Flags: X - disabled, I - invalid, D - dynamic 
 0  D ;;; ipsec mode-config
      chain=srcnat action=src-nat to-addresses=192.168.77.254 src-address-list=local dst-address-list=!local

```

:::info
警告

確保動態 mode config 地址不屬於本地網路。

**重要：** 也可以組合兩個選項（1 和 2），僅允許特定本地地址/網路訪問特定地址。
:::

#### 選項 2：透過隧道訪問特定地址 {#option-2-accessing-certain-addresses-over-the-tunnel}

還可以使用 Mangle 防火牆中的 connection-mark 引數，僅將特定流量透過隧道傳送。它的工作方式與選項 1 類似——會根據 mode config 下配置的 connection-mark 引數生成動態 NAT 規則。

首先，在 mode config 配置中設定 connection-mark。

```
/ip/ipsec/mode-config
set [ find name=NordVPN ] connection-mark=NordVPN

```

完成後，將使用伺服器提供的動態地址生成 NAT 規則：

```
[admin@MikroTik] > /ip/firewall/nat/print 
Flags: X - disabled, I - invalid, D - dynamic 
 0  D ;;; ipsec mode-config
      chain=srcnat action=src-nat to-addresses=192.168.77.254 connection-mark=NordVPN 

```

之後，可以使用 Mangle 防火牆將此 connection-mark 應用於任何流量。在此示例中，透過隧道授予對 [mikrotik.com](http://mikrotik.com) 和 8.8.8.8 的訪問許可權。

建立新的地址列表：

```
/ip/firewall/address-list
add address=mikrotik.com list=VPN
add address=8.8.8.8 list=VPN

```

將 connection-mark 應用於與建立的地址列表匹配的流量：

```
/ip/firewall/mangle
add action=mark-connection chain=prerouting dst-address-list=VPN new-connection-mark=NordVPN passthrough=yes

```

:::info
也可以組合兩個選項（1 和 2），僅允許特定本地地址/網路訪問特定地址
:::
