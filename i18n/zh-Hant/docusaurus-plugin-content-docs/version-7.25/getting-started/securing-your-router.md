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
source: https://manual.mikrotik.com/docs/7.25/getting-started/securing-your-router
captured_at: '2026-11-04T11:17:01+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

以下步驟是關於如何在已配置[強防火牆規則](../firewall-and-quality-of-service/firewall/filter.md)的情況下進一步保護裝置的建議。

## RouterOS 版本 {#routeros-version}

首先升級你的 RouterOS 版本。一些較舊版本存在某些已修復的弱點或漏洞。保持裝置更新以確保其安全。要升級，請在 WinBox 或 WebFig 中選擇 **檢查更新**。建議關注我們的[安全公告部落格](https://blog.mikrotik.com)上的公告，以隨時瞭解任何新的安全問題。

## 訪問使用者名稱 {#access-username}

將預設使用者名稱 **admin** 更改為自定義名稱。使用唯一使用者名稱有助於在有人獲得裝置直接物理訪問許可權時保護對路由器的訪問：

```ros
/user/add name=myname password=mypassword group=full
/user/disable admin
```

## 訪問密碼 {#access-password}

MikroTik 路由器要求配置密碼。使用密碼生成器工具建立安全且不重複的密碼。安全密碼應：

- 至少 12 個字元。
- 包含數字、符號、大寫和小寫字母。
- 不是詞典單詞或詞典單詞的組合。
- 在帶引號的密碼中，使用反斜槓（`\$`）轉義 `"`、`\` 和 `$`。未轉義的 `$` 會開始一個變數名：路由器會將 `$` 及其後面的名稱替換為該變數的值（通常為空），密碼會在不知不覺中變短。

```ros
/user/set myname password="!={Ba3N!40TyX+GvKBz?jTLIUcx/,"
```

## 使用者賬戶和組 {#user-accounts-and-groups}

為每位管理員建立一個賬戶，而不是共享單個 `admin` 賬戶，併為每個賬戶分配一個僅包含所需策略的自定義組——內建的 `read` 組可以重啟路由器並檢視敏感配置。對於基於金鑰的登入，請匯入每位管理員的公共 SSH 金鑰；當為使用者分配了金鑰後，該使用者的 SSH 密碼登入將被停用。參見[使用者](../authentication-authorization-accounting/user.md)。

## 保護對裝置的訪問 {#securing-access-to-the-device}

預設情況下，預配置的防火牆會阻止來自 WAN（面向網際網路）介面的所有管理訪問。**這是有意為之——除非你完全瞭解後果，否則不要刪除這些規則。**

:::danger[不要將管理服務暴露到網際網路]
具有對網際網路開放的管理介面的網路裝置會不斷被自動化攻擊掃描和針對。將 WinBox、SSH 或其他管理服務直接暴露到網際網路可能導致：

- **針對登入憑據的暴力破解攻擊**。
- **利用未打補丁的 RouterOS 版本中的已知漏洞**。
- **裝置完全失陷**——攻擊者可以攔截流量、重定向 DNS、安裝惡意軟體，或將路由器用作進一步攻擊的代理。

如果你需要遠端訪問裝置，**請使用 VPN**，例如 [WireGuard](../virtual-private-networks/wireguard.md) 來建立加密隧道。這會使管理流量完全避開公共網際網路。
:::

### 從 WAN 開放管理訪問（高階） {#opening-management-access-from-wan-advanced}

以下防火牆規則適用於無法避免從 WAN 直接訪問管理服務的情況——例如，由 ISP 管理的基礎設施或沒有 VPN 閘道器的站點。**除非你有直接面向網際網路進行管理的特定需求，否則不要應用這些規則。**

這些規則僅允許來自 WAN 介面的 ICMP（ping 和 traceroute）、WinBox 和 SSH，並丟棄其他所有內容：

```ros
/ip/firewall/filter
add chain=input action=accept \
    connection-state=established,related,untracked \
    comment="accept established,related,untracked"
add chain=input action=drop \
    connection-state=invalid \
    comment="drop invalid"
add chain=input action=accept \
    in-interface=ether1 protocol=icmp \
    comment="accept ICMP"
add chain=input action=accept \
    in-interface=ether1 protocol=tcp dst-port=8291 \
    comment="allow WinBox"
add chain=input action=accept \
    in-interface=ether1 protocol=tcp dst-port=22 \
    comment="allow SSH"
add chain=input action=drop \
    in-interface=ether1 \
    comment="block everything else"
```

對於沒有預設配置的路由器，這些規則構成完整的 input 鏈。在具有預設配置的路由器上，`add` 會將它們追加到丟棄來自 LAN 外部所有輸入的規則之後，因此 WAN 連線永遠無法到達它們。在這種情況下，只需在該規則之前新增所需服務的 accept 規則：

```ros
/ip/firewall/filter
add chain=input action=accept \
    in-interface-list=WAN protocol=tcp dst-port=8291 \
    comment="allow WinBox" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
add chain=input action=accept \
    in-interface-list=WAN protocol=tcp dst-port=22 \
    comment="allow SSH" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
```

:::warning
如果公共介面是 PPPoE、LTE 或其他介面型別，應相應地設定 `in-interface`。如果選擇了錯誤的介面，你可能會失去對裝置的訪問。
:::

:::danger[需要額外加固]
從 WAN 開放管理訪問時，你**必須**同時：

- 使用強度高且唯一的密碼（參見 [Access password](#access-password)）。
- 在可能的情況下，將訪問限制為特定的源地址。
- 限制來自同一地址的重複 SSH 連線，如 [SSH 暴力破解防護](../firewall-and-quality-of-service/user-guides/bruteforce-prevention.md) 中所述。
- 保持 RouterOS 更新到最新的穩定版本。
- 監控日誌以發現未經授權的連線嘗試。
:::

你還可以使用 **Allowed Address** 屬性將特定使用者賬戶限制到特定源地址：

```ros
/user/set 0 address=192.168.88.0/24
```

## RouterOS MAC-access {#routeros-mac-access}

RouterOS 包含內建功能選項，可為網路裝置提供便捷的管理訪問。但是，在生產網路中應停用以下服務：**MAC-Telnet, MAC-WinBox,** 和 **MAC-Ping.**

```ros
/tool/mac-server/set allowed-interface-list=none
/tool/mac-server/mac-winbox/set allowed-interface-list=none
/tool/mac-server/ping/set enabled=no
```

## 鄰居發現 {#neighbor-discovery}

MikroTik Neighbor Discovery 協定用於發現和識別網路上的其他 MikroTik 路由器。要在所有介面上停用 Neighbor Discovery，請使用以下命令：

```ros
/ip/neighbor/discovery-settings/set discover-interface-list=none
```

## 頻寬伺服器 {#bandwidth-server}

頻寬伺服器用於測試兩臺 MikroTik 路由器之間的吞吐量。在生產環境中應將其停用：

```ros
/tool/bandwidth-server/set enabled=no
```

## DNS 快取 {#dns-cache}

DNS 快取將已解析的 DNS 查詢結果儲存在路由器本地，從而縮短用戶端裝置向遠端伺服器解析 DNS 請求所需的時間，以提高效能。如果路由器不需要應答來自其他裝置的 DNS 查詢——例如，如果你的網路中有另一臺裝置負責處理 DNS——請關閉遠端請求。這樣路由器只為自己解析名稱，即使防火牆規則允許來自網際網路的 DNS 查詢透過，它也無法應答這些查詢：

```ros
/ip/dns/set allow-remote-requests=no
```

## 附加服務 {#additional-services}

RouterOS 包含若干服務，這些服務可能會根據你的配置而啟用。在生產環境中應停用以下服務：快取代理、SOCKS、UPnP 和 MikroTik Cloud 服務。

```ros
/ip/proxy/set enabled=no
/ip/socks/set enabled=no
/ip/upnp/set enabled=no
/ip/cloud/set ddns-enabled=auto update-time=no
```

在預設的 `ddns-enabled=auto` 下，路由器僅在啟用 Back To Home（遠端回家） 時向 MikroTik 雲註冊 DNS 名稱。`update-time=no` 會阻止路由器從雲設定其時鐘。

## 管理服務埠 {#management-service-ports}

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
/ip/service/set winbox available-from=192.168.88.0/24
```

## 更安全的 SSH 訪問 {#more-secure-ssh-access}

你可以在路由器上啟用更嚴格的 SSH 安全設定。使用 `strong-crypto=yes` 後，SSH 伺服器將停止提供較弱的演算法：128 位、CBC、3DES 和 `none` 加密演算法，SHA-1 和 MD5 MAC，以及使用 SHA-1 的金鑰交換。要應用這些更安全的 SSH 設定，請使用以下命令：

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
