---
sidebar_key: "virtual-private-networks/wireguard"
sidebar_position: 11
title: "WireGuard"
sidebar_label: "WireGuard"
description: "WireGuard 是一種現代 VPN 解決方案，可在各平臺上提供快速、安全的加密，並具備詳細的配置選項，包括私鑰/公鑰、VRF 路由以及用於在裝置之間建立加密隧道的對等節點管理。"
tags:
  - 'wireguard'
  - 'vpn'
source: https://manual.mikrotik.com/docs/7.25/virtual-private-networks/wireguard
captured_at: '2026-11-04T11:23:37+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

WireGuard 是一種簡單、快速且現代的 VPN，採用最先進的密碼學技術。它的目標是比 IPsec 更快、更簡單、更精簡，並且效能遠超 OpenVPN。WireGuard 是一款通用 VPN，既面向嵌入式介面也面向超級計算機而設計，適用於多種不同場景。它最初為 Linux 核心釋出，如今已跨平臺（Windows、macOS、BSD、iOS、Android），可廣泛部署。

## 匯入和匯出 WireGuard {#importing-and-exporting-wireguard}

配置可以透過多種方式完成。可下載示例檔案：[wireguard1.conf](pathname:///assets/wireguard1.conf)。使用前請替換其中的示例金鑰和端點。

### 匯入 WireGuard 配置 {#importing-a-wireguard-configuration}

[`/interface/wireguard/wg-import`](../cli-reference/interface/wireguard/wg-import.md) 接受標準 WireGuard 格式（`[Interface]` / `[Peer]` 段）的配置。一個最小可用的檔案：

```ini
[Interface]  
Address =192.168.88.3/24  
ListenPort = 13533  
PrivateKey = UBLqJEFZZf9wszZSUF2BPWa9dsMX99RbEcxlNfxWffk=
```

將檔案儲存到裝置（例如透過 WebFig/WinBox 的 Files 選單），然後使用以下命令匯入：

```ros
/interface/wireguard/wg-import config-file=wireguard1.conf
```

同一配置也可以不使用檔案、直接透過 `config-string` 引數匯入：

```ros
/interface/wireguard/wg-import config-string="
[Interface]
Address = 192.168.88.3/24
ListenPort = 13533
PrivateKey = UBLqJEFZZf9wszZSUF2BPWa9dsMX99RbEcxlNfxWffk=

[Peer]
PublicKey = EoF7HlFu3fbOnuYbyGqLMJkPZgQk9n3WwONZuJZ6qWc=
Endpoint = 192.0.2.10:51820
AllowedIPs = 0.0.0.0/0
PersistentKeepalive = 25"
```

### 匯出用戶端配置 {#exporting-client-configurations}

用戶端配置（用於手機、筆記型電腦及其他對端裝置）透過 [`/interface/wireguard/peers/show-client-config`](../cli-reference/interface/wireguard/peers/show-client-config.md) 按對端生成——既可以文字形式（`conf` 輸出，或使用 `file` 引數儲存到檔案），也可以二維條碼形式（`qr` 輸出）供 WireGuard 用戶端應用掃描。

生成的配置由對端的 `client-*` 屬性構建（參見 [`/interface/wireguard/peers`](../cli-reference/interface/wireguard/peers/index.md)）。如果對端的 `client-address` 留空，生成的配置中將使用預設地址 `192.168.177.2/24`。

:::note
生成的用戶端配置中的 “**AllowedIPs**” 值為 `0.0.0.0/0, ::/0`。自 RouterOS 7.21 起，可透過對端的 `client-allowed-address` 屬性進行調整；在更早的版本中該值是固定的，只能在遠端對端軟體中更改。
:::

### 匯出 WireGuard 介面 {#exporting-a-wireguard-interface}

[`/interface/wireguard/wg-export`](../cli-reference/interface/wireguard/wg-export.md) 以標準 WireGuard 配置格式寫出所選介面及其對端：

```ros
/interface/wireguard/wg-export [find name=wireguard1] \
    file=wireguard1.conf
```

使用 `wg-import` 匯入此檔案。匯出內容包含 `[Interface]` 和 `[Peer]` 段，但不包含介面的 IP 地址，也不包含 RouterOS 路由和防火牆規則。請在目標路由器上單獨配置這些內容。

如需 RouterOS 配置指令碼，請改用常規的 `/interface/wireguard/export` 命令。請將包含私鑰的匯出檔案和生成的用戶端配置視為機密。

:::note
當你遇到回覆流量源地址錯誤的問題時，使用 NAT 將封包源地址轉換為迴環介面是一種常見的變通方法。此方法有助於在封包經網路路由返回時確保源地址一致且正確。
:::

## 應用示例 {#application-examples}

### 站點到站點 WireGuard 隧道 {#site-to-site-wireguard-tunnel}

考慮下圖所示的設定。兩臺遠端辦公室路由器連線到網際網路，辦公室工作站位於 NAT 之後。每個辦公室都有自己的本地子網，Office1 為 10.1.202.0/24，Office2 為 10.1.101.0/24。兩個遠端辦公室都需要到路由器後方本地網路的安全隧道。

![Two office LANs connected through a WireGuard tunnel between their routers](/img/e82d4ebd9d1188e7.webp)

#### WireGuard 介面配置 {#wireguard-interface-configuration}

首先，在兩個站點上配置 WireGuard 介面，以允許自動生成私鑰和公鑰。兩臺路由器的命令相同：

```ros
/interface/wireguard
add listen-port=13231 name=wireguard1
```

在每臺路由器上讀取公鑰，並且只交換公鑰。

:::warning
遠端裝置永遠不需要私鑰——這正是其被稱為“私鑰”的原因。
:::

**Office1**

```ros
:put [/interface/wireguard/get [find name=wireguard1] public-key]
```

**Office2**

```ros
:put [/interface/wireguard/get [find name=wireguard1] public-key]
```

#### 對等端配置 {#peer-configuration}

對端配置定義了誰可以使用 WireGuard 介面以及可以透過它傳送何種流量。要標識遠端對端，必須同時指定其公鑰和已建立的 WireGuard 介面。將 Office1 上的 `<Office2-public-key>` 替換為在 Office2 上讀取的金鑰，將 Office2 上的 `<Office1-public-key>` 替換為在 Office1 上讀取的金鑰。

**Office1**

```ros
/interface/wireguard/peers
add allowed-address=10.1.101.0/24,10.255.255.2/32 \
    endpoint-address=192.168.80.1 endpoint-port=13231 \
    interface=wireguard1 \
    public-key="<Office2-public-key>"
```

**Office2**

```ros
/interface/wireguard/peers
add allowed-address=10.1.202.0/24,10.255.255.1/32 \
    endpoint-address=192.168.90.1 endpoint-port=13231 \
    interface=wireguard1 \
    public-key="<Office1-public-key>"
```

#### IP 與路由配置 {#ip-and-routing-configuration}

最後，必須配置 IP 和路由資訊，以允許流量透過隧道傳送。

**Office1**

```ros
/ip/address
add address=10.255.255.1/30 interface=wireguard1
/ip/route
add dst-address=10.1.101.0/24 gateway=wireguard1
```

**Office2**

```ros
/ip/address
add address=10.255.255.2/30 interface=wireguard1
/ip/route
add dst-address=10.1.202.0/24 gateway=wireguard1
```

#### 防火牆注意事項 {#firewall-considerations}

預設的 RouterOS 防火牆會阻止隧道正常建立。必須在兩個站點的任何 drop 規則之前，在 `input` 鏈中接受該流量。這些命令會將規則插入到對應鏈中第一條現有規則之前。如果鏈為空，請省略 `place-before`。

**Office1**

```ros
/ip/firewall/filter
add chain=input action=accept \
    dst-port=13231 protocol=udp src-address=192.168.80.1 \
    place-before=([find chain=input]->0)
```

**Office2**

```ros
/ip/firewall/filter
add chain=input action=accept \
    dst-port=13231 protocol=udp src-address=192.168.90.1 \
    place-before=([find chain=input]->0)
```

“forward” 鏈也可能限制子網之間的通訊，因此此類流量同樣應在任何 drop 規則之前被接受。

**Office1**

```ros
/ip/firewall/filter
add chain=forward action=accept \
    dst-address=10.1.202.0/24 src-address=10.1.101.0/24 \
    place-before=([find chain=forward]->0)
add chain=forward action=accept \
    dst-address=10.1.101.0/24 src-address=10.1.202.0/24 \
    place-before=([find chain=forward]->0)
```

**Office2**

```ros
/ip/firewall/filter
add chain=forward action=accept \
    dst-address=10.1.101.0/24 src-address=10.1.202.0/24 \
    place-before=([find chain=forward]->0)
add chain=forward action=accept \
    dst-address=10.1.202.0/24 src-address=10.1.101.0/24 \
    place-before=([find chain=forward]->0)
```

## RoadWarrior WireGuard 隧道 {#roadwarrior-wireguard-tunnel}

### RouterOS 配置 {#routeros-configuration}

新增一個新的 WireGuard 介面，併為其分配 IP 地址。

```ros
/interface/wireguard
add listen-port=13231 name=wireguard1
/ip/address
add address=192.168.100.1/24 interface=wireguard1
```

新增新的 WireGuard 介面會自動生成一對私鑰和公鑰。請在遠端裝置上配置該公鑰。要獲取公鑰值，請執行：

```ros
:put [/interface/wireguard/get [find name=wireguard1] public-key]
```

接下來的步驟中，需要獲取遠端裝置的公鑰。拿到公鑰後，透過指定遠端裝置的公鑰以及允許透過 WireGuard 隧道的允許地址來新增新對端。

```ros
/interface/wireguard/peers
add allowed-address=192.168.100.2/32 interface=wireguard1 \
    public-key="<paste public key from remote device here>"
```

### 防火牆注意事項 {#firewall-considerations-1}

如果你配置了預設或嚴格的防火牆，則需要允許遠端裝置與你的裝置建立 WireGuard 連線。

```ros
/ip/firewall/filter
add chain=input action=accept \
    comment="allow WireGuard" dst-port=13231 protocol=udp \
    place-before=([find chain=input]->0)
```

要允許遠端裝置連線到 RouterOS 服務（例如請求 DNS），請在 input 鏈中允許 WireGuard 子網。

```ros
/ip/firewall/filter
add chain=input action=accept \
    comment="allow WireGuard traffic" in-interface=wireguard1 \
    src-address=192.168.100.0/24 \
    place-before=([find chain=input]->0)
```

或者，將 WireGuard 介面新增到 `LAN` 介面列表。這樣，VPN 對端將獲得匹配此列表的規則所授予的 LAN 訪問許可權；如果 VPN 對端應擁有更少的訪問許可權，請使用單獨的防火牆規則。

```ros
/interface/list/member
add interface=wireguard1 list=LAN
```

### iOS 配置 {#ios-configuration}

從 App Store 下載 WireGuard 應用程式。開啟它並從頭建立新配置。

![WireGuard on iOS with the Create from scratch option selected](/img/e4c782efd1e4a573.webp)

首先，為你的連線指定 `Name`，並選擇 `Generate a keypair`。生成的 `Public key` 是 RouterOS 一側對端配置所必需的。

![New iOS WireGuard configuration with keypair, address and DNS fields](/img/595359132947760c.webp)

在 `Addresses` 欄位中指定一個與 RouterOS 一側配置處於同一子網的 IP 地址。該地址用於通訊。在本示例中，RouterOS 一側使用 `192.168.100.1/24`。你可以在此處使用 `192.168.100.2/24`。

如有必要，配置 `DNS servers`。如果 RouterOS 一側 `/ip/dns` 下的 `allow-remote-requests` 設定為 `yes`，你可以在此處指定遠端 WireGuard IP 地址。

![iOS WireGuard address 192.168.100.2 and DNS server 192.168.100.1](/img/e2f9bce3143b113d.webp)

選擇 `Add peer` 以顯示更多引數。

`Public key` 值是在 RouterOS 一側 WireGuard 介面上生成的公鑰值。

`Endpoint` 是 RouterOS 裝置的 IP 或 DNS 加埠號，iOS 裝置可透過網際網路與其通訊。

`Allowed IPs` 設定為 `0.0.0.0/0`，以允許所有流量透過 WireGuard 隧道傳送。

![iOS peer settings with the router endpoint and Allowed IPs set to 0.0.0.0/0](/img/ff125611431949f1.webp)

如果 RouterOS 裝置位於另一臺 NAT 路由器之後，請在該上游路由器上配置埠轉發，將 WireGuard UDP 埠轉發到 RouterOS 裝置。如果上游路由器執行 RouterOS：

```ros
/ip/firewall/nat
add chain=dstnat action=dst-nat \
    protocol=udp dst-port=13231 in-interface=WAN \
    to-addresses=192.168.1.2 to-ports=13231
```

將 `WAN`、`192.168.1.2` 和 `13231` 替換為適當的上游介面名稱、RouterOS 裝置在上游網路中的 IP 地址以及 WireGuard 監聽埠。

### Windows 配置 {#windows-configuration}

從 [WireGuard](https://www.wireguard.com/install/) 下載 WireGuard 安裝程式並以管理員身份執行。

按 <kbd>Control</kbd>+<kbd>N</kbd> 新增新的空隧道。為介面新增名稱——公鑰應會自動生成。將其複製到 RouterOS 對端配置中。  
將其新增到伺服器配置中。完整配置應如下所示（在 `[Interface]` 段中保留自動生成的 `PrivateKey`）：

```ini
[Interface]
PrivateKey = your_autogenerated_private_key=
Address = 192.168.100.2/24
DNS = 192.168.100.1

[Peer]
PublicKey = your_MikroTik_public_KEY=
AllowedIPs = 0.0.0.0/0
Endpoint = example.com:13231
```

儲存配置並選擇 `Activate`。

## WireGuard 上下文中的 vrf 引數 {#the-vrf-parameter-in-the-wireguard-context}

`vrf` 引數**不**適用於 WireGuard 介面本身（例如 `wg0`、`wg1`），而是適用於用於傳輸加密封包的 **UDP 套接字**。

WireGuard 的執行中有兩個不同的層：

1. **WireGuard 介面**——處理明文（未加密）IP 封包的虛擬網路裝置。進入該介面的出站封包由 WireGuard 加密並透過 UDP 套接字傳送；傳入的加密 UDP 封包由 WireGuard 解密，並作為明文 IP 封包透過該介面交付。
2. **UDP 套接字**——處理加密的 WireGuard 流量，從網路接收加密封包並向網路傳送加密封包。

`vrf` 引數與 **UDP 套接字層**（情況 2）相關。它指定套接字應使用**哪個路由表（VRF）**來確定加密封包的傳送或接收方式。  
這可確保加密流量遵循正確的路由路徑並使用正確的源 IP，從而避免封包可能從錯誤介面或路由發出的問題。  

### 示例 {#example}

> 假設介面 `eth1` 屬於 VRF `foo`。  
> 如果你希望 WireGuard 透過 `eth1` 傳送和接收加密封包，請為 WireGuard 配置 `vrf=foo`。  
> WireGuard 介面（`wg0`）本身處於與內部 UDP 套接字使用的 `vrf` 引數所指定的 VRF 不同的 VRF 中是正常的。

## 多 WAN 設定 {#multi-wan-setup}

WireGuard 本身不存在固有的伺服器-用戶端關係。只要配置中定義了端點，兩端都可以充當端點，並且雙方都會向彼此傳送 UDP 握手訊息。你可以在對端設定中啟用 “responder” 選項來模擬伺服器-用戶端行為，此時“伺服器”對端只回復來自“用戶端”對端的握手訊息，而自身不會發送握手訊息。  
由於這種隧道建立行為，來自 WireGuard 隧道不同端點的握手訊息會被視為兩個獨立連線。  
在存在多條通往“用戶端”對端路徑的設定中，你需要考慮這一點，因為這可能導致“伺服器”透過不同於入站路由的路徑回覆“用戶端”。  
下面是一個配置示例，用於處理此行為並確保“伺服器”使用入站路由回覆“用戶端”。

### 配置示例 {#configuration-example}

本示例不包含 WireGuard 介面配置，因為它適用於具有兩條 WAN 連線的 [RoadWarrior](./wireguard.md#roadwarrior-wireguard-tunnel) 和 [站點到站點](./wireguard.md#site-to-site-wireguard-tunnel) 設定，例如 [PCC](../high-availability-solutions/load-balancing/per-connection-classifier.md) 設定。
`wan2` 和 `wan3` 路由表必須已存在，且各自具有一條透過對應 WAN 到達對端的路由。請替換介面和表名稱以匹配你的配置。output 規則匹配本地 WireGuard 源埠，因為遠端對端可能使用不同的埠。

為使這些規則按預期工作，你需要在 WireGuard 對端設定中啟用 “responder” 選項，否則“伺服器”可能因路由未被標記而透過錯誤的介面傳送握手訊息。

```ros
/ip/firewall/mangle
add chain=prerouting action=add-src-to-address-list \
    address-list=WAN2_WireGuard_clients address-list-timeout=1m \
    dst-port=13231 in-interface=ether2 protocol=udp \
    comment="Track WireGuard peers on WAN2"
add chain=output action=mark-connection \
    dst-address-list=WAN2_WireGuard_clients src-port=13231 \
    new-connection-mark=wan2 protocol=udp \
    comment="Mark WireGuard replies"
add chain=output action=mark-routing \
    connection-mark=wan2 src-port=13231 new-routing-mark=wan2 \
    protocol=udp \
    comment="Route WireGuard replies through WAN2"
add chain=prerouting action=add-src-to-address-list \
    address-list=WAN3_WireGuard_clients address-list-timeout=1m \
    dst-port=13231 in-interface=ether3 protocol=udp \
    comment="Track WireGuard peers on WAN3"
add chain=output action=mark-connection \
    dst-address-list=WAN3_WireGuard_clients src-port=13231 \
    new-connection-mark=wan3 protocol=udp \
    comment="Mark WireGuard replies"
add chain=output action=mark-routing \
    connection-mark=wan3 src-port=13231 new-routing-mark=wan3 \
    protocol=udp \
    comment="Route WireGuard replies through WAN3"
 
/ip/firewall/nat
add chain=srcnat action=masquerade \
    protocol=udp src-port=13231 out-interface=ether2 \
    comment="Use the WAN2 source address"
add chain=srcnat action=masquerade \
    protocol=udp src-port=13231 out-interface=ether3 \
    comment="Use the WAN3 source address"
```

第一條 mangle 規則透過匹配傳入 WireGuard 握手的目標埠來捕獲源 IP 地址，並將其加入列表，隨後該列表用於標記出站 WireGuard 握手。超時機制確保同一源 IP 地址之後可以透過不同的 WAN 介面建立 WireGuard 隧道。  
第二條 mangle 規則標記用於路由標記的連線，並確保在 IP 地址從地址列表中消失且隧道建立後，標記仍保留在連線上。  
第三條 mangle 規則強制封包使用第二條 WAN 介面的正確路由表。  
最後一條 NAT 規則確保封包以正確的源 IP 發出，因為它不會被 mangle 規則調整。如果沒有此規則，封包可能會因具體設定而具有不同的源 IP。
這些規則為 WAN3 重複配置，以確保 WAN3 介面也能與 WireGuard 一起使用。  

這組規則確保 WireGuard 隧道在接收到傳入握手的介面上建立。

## 2FA 設定 {#2fa-setup}

在 RouterOS v7 中，[HotSpot](../authentication-authorization-accounting/hotspot-captive-portal/index.md) 服務可以繫結到 WireGuard 介面。這允許管理員將 WireGuard 的高效能加密與 HotSpot 的強制門戶功能結合起來，支援透過本地資料庫、User Manager 或 RADIUS 進行額外的使用者級身份驗證。OTP 功能進一步增強了安全性。

### 配置示例 {#configuration-example-1}

確保你的裝置上已配置 WireGuard 介面 `wg1`。

在 WireGuard 介面上設定 HotSpot：

```ros
/ip/hotspot/setup
```

在提示選擇 HotSpot 介面時選擇 `wg1`。要在不使用互動式設定的情況下建立伺服器，請配置 HotSpot 配置檔案並使用：

```ros
/ip/hotspot/add interface=wg1
```

完成 HotSpot 設定後，一旦 WireGuard 對端連線，需要額外登入門戶才能繼續。可以使用常規的 HotSpot 使用者名稱/密碼授權。為獲得更好的安全性，請在 `/ip/hotspot/user` 或 `/user-manager/user` 中配置 `otp-secret`。為每個使用者生成唯一的 Base32 金鑰並將其新增到身份驗證器應用。使用前請替換示例金鑰：

```ros
/ip/hotspot/user/add name=peer1 \
    otp-secret=HVR4CFHAFOWFGGFAGSA5JVTIMMPG6GMT
```

你可以找到多個開源 TOTP 生成器工具，它們可以為你提供適當的金鑰和必要選項，以便將其匯入你的 "authenticator" 應用。

設定完成後，在你的裝置上啟動 WireGuard。透過隧道開啟 HotSpot 登入頁面，輸入 HotSpot 使用者名稱以及來自身份驗證器應用的六位基於時間的一次性密碼（TOTP）。WireGuard 對對端金鑰進行身份驗證；HotSpot 登入則單獨授權使用者流量。

你應為 HotSpot 使用 HTTPS 登入頁面，並確保 WireGuard 對端能夠驗證登入頁面證書。
