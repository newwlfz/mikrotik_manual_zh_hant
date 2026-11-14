---
sidebar_key: "getting-started/securing-your-router"
sidebar_position: 3
title: "保護您的路由器"
sidebar_label: "保護您的路由器"
description: "本頁提供 MikroTik RouterOS 的安全建議，包括升級 RouterOS 版本、更改預設使用者名稱和密碼、使用防火牆規則和 VPN 保護訪問、停用 MAC-Telnet 和 Neighbor Discovery 等不必要的服務，以及管理 DNS 快取以增強路由器安全性。"
tags:
  - 'firewall'
  - 'vpn'
  - 'security'
source: https://manual.mikrotik.com/docs/7.24/getting-started/securing-your-router
captured_at: '2026-11-04T11:29:05+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

以下步驟是關於如何在已配置[強防火牆規則](../firewall-and-quality-of-service/firewall/filter.md)的情況下進一步保護裝置的建議。

## RouterOS 版本 {#routeros-version}

首先升級 RouterOS 版本。某些舊版本存在已修復的弱點或漏洞。保持裝置更新以確保安全。在 WinBox 或 WebFig 中點選“檢查更新”進行升級。建議關注我們的[安全公告部落格](https://blog.mikrotik.com)，及時瞭解任何新的安全問題。

## 訪問路由器 {#access-to-a-router}

### 訪問使用者名稱 {#access-username}

將預設使用者名稱 **admin** 更改為自定義名稱。使用唯一使用者名稱有助於在有人獲得裝置直接物理訪問許可權時保護對路由器的訪問：

```ros
/user/add name=myname password=mypassword group=full
/user/disable admin
```

### 訪問密碼 {#access-password}

MikroTik 路由器需要配置密碼。我們建議使用密碼生成工具建立安全且不重複的密碼。所謂安全密碼，是指：

- 至少 12 個字元。
- 包含數字、符號、大寫和小寫字母。
- 不是詞典單詞或詞典單詞的組合。
- 請注意，密碼中的引號字元需要轉義。

```ros
/user/set myname password="!={Ba3N!40TуX+GvKBz?jTLIUcx/,"
```

### 保護對裝置的訪問 {#securing-access-to-the-device}

預配置防火牆預設會阻止 WAN（網際網路側）連線嘗試。這是有意為之——除非你確定連線是安全的，否則不要刪除這些規則。

如果你需要開放對裝置的遠端訪問，我們建議使用虛擬專用網路（VPN），例如 WireGuard，來保護連線。

此處提供了 [WireGuard VPN](../virtual-private-networks/wireguard.md) 的配置指南。

### 管理訪問的防火牆規則 {#firewall-rules-for-management-access}

應使用防火牆規則限制對公網介面上服務的訪問，這些規則會阻止連線到達服務。下面的示例僅允許來自 WAN 介面的 ICMP（ping 和 traceroute）、WinBox 和 SSH，並丟棄其他所有內容：

```ros
/ip/firewall/filter
add chain=input action=accept connection-state=established,related,untracked comment="accept established,related,untracked"
add chain=input action=drop connection-state=invalid comment="drop invalid"
add chain=input in-interface=ether1 action=accept protocol=icmp comment="accept ICMP"
add chain=input in-interface=ether1 action=accept protocol=tcp dst-port=8291 comment="allow WinBox"
add chain=input in-interface=ether1 action=accept protocol=tcp dst-port=22 comment="allow SSH"
add chain=input in-interface=ether1 action=drop comment="block everything else"
```

:::danger
如果公網介面是 PPPoE、LTE 或其他介面型別，則應相應設定 `in-interface`。
:::

你還可以使用 **Allowed Address** 屬性將特定使用者賬戶限制到特定源地址：

```ros
/user/set 0 address=192.168.88.0/24
```

### RouterOS MAC 訪問 {#routeros-mac-access}

RouterOS 包含內建功能選項，可為網路裝置提供便捷的管理訪問。但是，在生產網路中應停用以下服務：**MAC-Telnet, MAC-WinBox,** 和 **MAC-Ping.**

```ros
/tool/mac-server/set allowed-interface-list=none 
/tool/mac-server/mac-winbox/set allowed-interface-list=none 
/tool/mac-server/ping/set enabled=no
```

### 鄰居發現 {#neighbor-discovery}

MikroTik Neighbor Discovery 協定用於發現和識別網路上的其他 MikroTik 路由器。要在所有介面上停用 Neighbor Discovery，請使用以下命令：

```ros
/ip/neighbor/discovery-settings/set discover-interface-list=none
```

### 頻寬伺服器 {#bandwidth-server}

頻寬伺服器用於測試兩臺 MikroTik 路由器之間的吞吐量。在生產環境中應將其停用：

```ros
/tool/bandwidth-server/set enabled=no 
```

### DNS 快取 {#dns-cache}

DNS 快取透過將已解析的 DNS 查詢結果儲存在路由器本地來提高效能，從而減少用戶端裝置向遠端伺服器解析 DNS 請求所需的時間。如果你的路由器不需要 DNS 快取——例如，網路中的另一臺裝置負責 DNS 快取——則應停用此功能以提高安全性：

```ros
/ip/dns/set allow-remote-requests=no
```

### 其他服務 {#additional-services}

RouterOS 包含若干服務，這些服務可能會根據你的配置而啟用。在生產環境中應停用以下服務：快取代理、SOCKS、UPnP 和 MikroTik Cloud 服務。

```ros
/ip/proxy/set enabled=no
/ip/socks/set enabled=no
/ip/upnp/set enabled=no
/ip/cloud/set ddns-enabled=auto update-time=no
```

### 管理服務埠 {#management-service-ports}

在 `/ip/service` 選單中停用你不使用的 RouterOS 管理服務：

```ros
/ip/service/disable telnet,ftp,www,api
```

更改預設 SSH 埠可以減少遭受自動化暴力破解嘗試的風險：

```ros
/ip/service/set ssh port=2200
```

也可以將每個服務限制到特定源地址，但更推薦使用防火牆規則（見上文）實施訪問控制，因為這樣可以阻止連線到達服務：

```ros
/ip/service/set winbox address=192.168.88.0/24
```

### 更安全的 SSH 訪問 {#more-secure-ssh-access}

你可以在路由器上啟用更嚴格的 SSH 安全設定。這包括啟用 aes-128-ctr 加密演算法，以及停用 hmac-sha1 和帶 sha1 的組演算法。要應用這些更安全的 SSH 設定，請使用以下命令：

```ros
/ip/ssh/set strong-crypto=yes
```

## 路由器介面 {#router-interface}

### Ethernet/SFP 介面 {#ethernetsfp-interfaces}

良好做法是停用路由器上所有未使用的介面，以減少對路由器的未經授權訪問：

```ros
/interface/print 
/interface/set X disabled=yes
```

其中 **X** 是未使用介面的編號。

### LCD {#lcd}

某些 RouterBOARD 裝置包含用於顯示系統資訊的 LCD 模組。要保護 LCD 安全，請設定 PIN 碼：

```ros
/lcd/pin/set pin-number=3659 hide-pin-number=yes
```

或者，你可以完全停用 LCD：

```ros
/lcd/set enabled=no
```
