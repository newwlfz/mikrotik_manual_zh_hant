---
sidebar_key: "virtual-private-networks/wireguard"
sidebar_position: 11
title: "WireGuard"
sidebar_label: "WireGuard"
description: "WireGuard 是一種現代 VPN 解決方案，可在各平臺上提供快速、安全的加密，並具備詳細的配置選項，包括私鑰/公鑰、VRF 路由以及用於在裝置之間建立加密隧道的對等節點管理。"
tags:
  - 'wireguard'
  - 'vpn'
source: https://manual.mikrotik.com/docs/7.24/virtual-private-networks/wireguard
captured_at: '2026-11-04T11:35:21+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

WireGuard 是一種極其簡單卻快速且現代的 VPN，採用先進的密碼學技術。它旨在比 IPsec 更快、更簡單、更精簡、更有用，同時避免大量令人頭疼的問題。它打算比 OpenVPN 具有顯著更好的效能。WireGuard 被設計為一種通用 VPN，既可在嵌入式介面上執行，也可在超級計算機上執行，適用於許多不同場景。它最初面向 Linux 核心釋出，現在已跨平臺（Windows、macOS、BSD、iOS、Android）並可廣泛部署。

## 屬性 {#properties}

| 屬性 | 描述 |
| :-- | :-- |
| **comment** (*string*; Default: ) | 隧道的簡短描述。 |
| **disabled** (*yes \| no*; Default: **no**) | 啟用/停用隧道。 |
| **listen-port** (*integer; Default: 13231*) | WireGuard 服務用於監聽傳入會話的埠。 |
| **mtu** (*integer [0..65536]*; Default: **1420**) | 三層最大傳輸單元。 |
| **name** (*string*; Default: ) | 隧道名稱。 |
| **vrf** (string; Default: **main**) | 為 WireGuard 套接字指定 vrf，更多詳情見下文。 |
| **private-key** (*string*; Default: ) *[敏感](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | base64 私鑰。如果未指定，將在建立介面時自動生成。每個網路介面都有一個私鑰和一個對等端列表。 |

### WireGuard 上下文中的 `vrf` 引數 {#the-vrf-parameter-in-wireguard-context}

:::info
`vrf` 引數**不**適用於 WireGuard 介面本身（例如 `wg0`、`wg1`），而是適用於用於傳輸加密封包的 **UDP 套接字**。

WireGuard 的執行中有兩個不同的層：

1. **WireGuard 介面** — 這是*明文*（未加密）封包流經的虛擬網路裝置。這些封包會被加密並透過 UDP 套接字傳送出去，或者在從 UDP 套接字傳入時被解密。
2. **UDP 套接字** — 這些負責處理*加密*流量：從網路接收加密封包，並將加密封包傳送出去。

`vrf` 引數與 **UDP 套接字層**（情況 2）相關。它指定套接字應使用**哪個路由表（VRF）**來決定加密封包如何傳送或接收。  
這可確保加密流量遵循正確的路由路徑並使用正確的源 IP，從而防止封包可能透過錯誤介面或路由發出的問題。  

#### 示例 {#example}

> 假設介面 `eth1` 屬於 VRF `foo`。  
> 如果你希望 WireGuard 透過 `eth1` 傳送和接收加密封包，應將 WireGuard 配置為 `vrf=foo`。  
> WireGuard 介面（`wg0`）本身與內部 UDP 套接字使用的 `vrf` 引數所指定的 VRF 不同，這是完全正常的。
:::

### 只讀屬性 {#read-only-properties}

| 屬性 | 描述 |
| :-- | :-- |
| **public-key** (*string*) | base64 公鑰由私鑰計算得出。每個對等端都有一個公鑰。公鑰用於對等端之間相互認證。它們可以被傳遞以用於配置檔案。 |
| **running** (*yes \| no*) | 介面是否正在執行。 |

## 對等體 {#peers}

| 屬性 | 描述 |
| :-- | :-- |
| **allowed-address** (*IP/IPv6 prefix*; *Default*: ) | 帶有 CIDR 掩碼的 IP（v4 或 v6）地址列表，來自該對等端的傳入流量允許使用這些地址，發往該對等端的傳出流量也指向這些地址。allowed-address 字首定義該對等端的路由和過濾規則，並且不需要與 WireGuard 介面地址處於同一子網。如果 WireGuard 介面為 192.168.99.1/24，則必須向用戶端輸入 192.168.99.2。透過將此 IP 新增到“Allowed Address”下，即表示只允許這個特定用戶端（例如手機）連線到此對等端配置。allowed-address 範圍不能在一個介面上重疊，因此需要為每個對等端設定自己的範圍。 |
| **comment** *(string; Default: )* | 對等端的簡短描述。 |
| **disabled** *(yes \| no; Default: **no**)* | 啟用/停用對等端。 |
| **endpoint-address** *(IP/Hostname; Default: )* | IP 地址或主機名。WireGuard 使用它在兩個對等端之間建立安全連線。 |
| **endpoint-port** (*integer:0..65535**; Default:* ) | 端點埠是 WireGuard 對等端監聽傳入流量的 UDP 埠。 |
| **interface** (*string; Default:* ) | 該對等端所屬 WireGuard 介面的名稱。 |
| **persistent-keepalive** (*integer:0..65535; Default: 0*) | 以秒為單位的間隔，範圍為 0 到 65535（含），表示向對等端傳送經過認證的空封包的頻率，以持久保持有狀態防火牆或 NAT 對映有效。值為 0 會停用 keepalive。例如，如果介面很少傳送流量，但可能隨時從某個對等端接收流量，並且它位於 NAT 之後，則該介面可能受益於 25 秒的持久 keepalive 間隔。 |
| **preshared-key** (*string; Default:* ) *[敏感](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | base64 預共享金鑰。可選，可以省略。此選項會增加一層對稱金鑰密碼學，並與已有的公鑰密碼學混合，以提供抗量子能力。也可以自動生成，或在系統管理員提供金鑰時手動輸入。 |
| **private-key** *(auto/none; Default: **none**) [敏感](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | base64 私鑰。 |
| **public-key** (*string; Default:* ) | base64 公鑰由私鑰計算得出。每個對等端都有一個公鑰。公鑰用於對等端之間相互認證。它們可以被傳遞以用於配置檔案。 |
| **show-client-config**\**[敏感](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | *將顯示已建立的對等端配置並生成二維條碼，以便在用戶端裝置上更輕鬆地設定對等端。不會影響 WireGuard 伺服器。從 7.21\_ab548 起，檢視二維條碼需要 show-sensitive。* |
| 用於用戶端-伺服器設定場景：當用戶端使用二維條碼匯入配置後，在設定了以下欄位後，帶有 qrcode 的標籤頁中會顯示配置詳情： |  |
| **client-address** *(IP/IPv6 prefix; Default: )* | 當用戶端（例如手機）使用二維條碼匯入時，該 wg 介面的此地址會在該裝置上設定。 |
| **client-dns** *(IP/IPv6 prefix; Default: )* | 指定將 WireGuard 伺服器用作對等端流量的 VPN 閘道器時使用的 DNS。 |
| **client-endpoint***(IP/IPv6 prefix; Default: )* | WireGuard 伺服器的 IP 地址和埠號。 |
| **client-keepalive** (*integer:0..65535; Default: 0*) | 與 **persistent-keepalive** 相同，但位於對等端一側。 |
| **client-listen-port** (*integer:0..65535**; Default:* ) | 此 WireGuard 隧道用於監聽來自對等端的傳入流量的本地埠，也是其發出傳出封包時使用的源埠。 |
| **client-allowed-address *(****IP/IPv6 prefix; Default: ::/0****)*** | 從 7.21 開始，可以配置 Allowed IPs。 |
| **name** (*string; Default:*) | 允許為對等端新增名稱。該名稱將在 WireGuard 日誌中用作對等端的引用。（從 RouterOS 7.15 版本起可用） |
| **responder***(yes \| no; Default:* ***no****)* | 指定該對等端是作為連線發起方，還是僅作為響應方。應在作為“伺服器”供其他裝置作為用戶端連線的 WireGuard 裝置上使用。否則，路由器會反覆嘗試連線 "endpoint-address" 或 "current-endpoint-address"。 |

透過 WireGuard 對等端匯出（配置檔案或二維條碼）提供給用戶端的 "**AllowedIPs**" 配置無法更改，目前會設定為 "0.0.0.0/0, ::/0"。如果需要在遠端修改這些值，必須透過用於 WireGuard 連線的遠端對等端軟體來完成。從 7.21 版本起已新增支援。

## 匯入、匯出 WireGuard {#importing-exporting-wireguard}

配置可以透過多種方式完成，下面是一個簡單的 wg 匯入檔案示例：[export](pathname:///assets/319783040_export)

:::warning
透過二維條碼/檔案在用戶端裝置上匯入時，必須指定最低引數。注意 - 如果用戶端地址欄位留空，則生成二維條碼時會新增預設 IP 地址 [192.168.177.2/24](http://192.168.177.2/24 "Follow link")。

Example:

```
interface: wireguard1
public-key: v/oIzPyFm1FPHrqhytZgsKjU7mUToQHLrW+Tb5e601M=
private-key: KMwxqe/iXAU8Jn9dd1o5pPdHep2blGxNWm9I944/I24=
allowed-address: 192.168.88.3/24
client-address: 192.168.88.3/32
client-endpoint: example.com:13231
```

**警告：** 使用 `/interface/wireguard/wg-import` file= 時，如果 Wireguard 匯入檔案以 # 開頭，可能會遇到 Could not parse 錯誤，請按示例直接使用清理後的檔案：

```
[Interface]  
Address =192.168.88.3/24  
ListenPort = 13533  
PrivateKey = UBLqJEFZZf9wszZSUF2BPWa9dsMX99RbEcxlNfxWffk=
```

**警告：** 從 7.19\_ab41 開始，已新增 config-string 引數，例如，使用此 cli 命令，你可以匯入你的配置：

```
/interface/wireguard/wg-import config-string="  
[Interface]  
Address =192.168.88.3/24  
ListenPort = 13533  
PrivateKey = UBLqJEFZZf9wszZSUF2BPWa9dsMX99RbEcxlNfxWffk=  
[Peer]  
PublicKey = EoF7HlFu3fbOnuYbyGqLMJkPZgQk9n3WwONZuJZ6qWc=  
Endpoint = 199.168.100.10:51820  
AllowedIPs = 0.0.0.0/0  
PersistentKeepalive = 25"
```
:::

### 只讀屬性 {#read-only-properties-1}

| 屬性 | 描述 |
| :-- | :-- |
| **current-endpoint-address** (*IP/IPv6*) | 來自對等端的、經過正確認證的封包的最新源 IP 地址。 |
| **current-endpoint-port** (*integer*) | 來自對等端的、經過正確認證的封包的最新源 IP 埠。 |
| **last-handshake** (*integer*) | 距上次成功握手之後的時間（秒）。 |
| **rx** (*integer*) | 從對等端接收的總位元組數。 |
| **tx** (*integer*) | 向對等端傳送的總位元組數。 |

:::note
當你遇到回覆流量源地址錯誤的問題時，使用 NAT 將封包源地址轉換為你的環回介面是一種常見解決方法。當封包透過網路路由返回時，此方法有助於確保源地址一致且正確。
:::

### 應用示例 {#application-examples}

### 站點到站點 WireGuard 隧道 {#site-to-site-wireguard-tunnel}

考慮如下圖所示的環境。兩臺遠端辦公室路由器連線到網際網路，辦公室工作站位於 NAT 之後。每個辦公室都有自己的本地子網：Office1 為 10.1.202.0/24，Office2 為 10.1.101.0/24。兩個遠端辦公室都需要到路由器後方本地網路的安全隧道。

![](/img/e82d4ebd9d1188e7.webp)

#### WireGuard 介面配置 {#wireguard-interface-configuration}

首先，必須在兩個站點上配置 WireGuard 介面，以允許自動生成私鑰和公鑰。兩臺路由器的命令相同：

```ros
/interface/wireguard
add listen-port=13231 name=wireguard1
```

現在列印介面詳情時，應能看到私鑰和公鑰，以便進行交換。

:::warning
遠端裝置永遠不需要任何私鑰——這正是“私鑰”名稱的由來。
:::

**Office1**

```ros
/interface/wireguard/print 
Flags: X - disabled; R - running 
 0  R name="wireguard1" mtu=1420 listen-port=13231 private-key="yKt9NJ4e5qlaSgh48WnPCDCEkDmq+VsBTt/DDEBWfEo=" 
      public-key="u7gYAg5tkioJDcm3hyS7pm79eADKPs/ZUGON6/fF3iI=" 
```

**Office2**

```ros
/interface/wireguard/print 
Flags: X - disabled; R - running 
 0  R name="wireguard1" mtu=1420 listen-port=13231 private-key="KMwxqe/iXAU8Jn9dd1o5pPdHep2blGxNWm9I944/I24=" 
      public-key="v/oIzPyFm1FPHrqhytZgsKjU7mUToQHLrW+Tb5e601M=" 
```

#### 對等端配置 {#peer-configuration}

對等端配置定義誰可以使用 WireGuard 介面以及可以透過它傳送何種流量。要識別遠端對等端，必須將遠端對等端的公鑰與已建立的 WireGuard 介面一起指定。

**Office1**

```ros
/interface/wireguard/peers
add allowed-address=10.1.101.0/24,10.255.255.2/32 endpoint-address=192.168.80.1 endpoint-port=13231 interface=wireguard1 \
public-key="v/oIzPyFm1FPHrqhytZgsKjU7mUToQHLrW+Tb5e601M="
```

**Office2**

```ros
/interface/wireguard/peers
add allowed-address=10.1.202.0/24,10.255.255.1/32 endpoint-address=192.168.90.1 endpoint-port=13231 interface=wireguard1 \
public-key="u7gYAg5tkioJDcm3hyS7pm79eADKPs/ZUGON6/fF3iI="
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

預設的 RouterOS 防火牆會阻止隧道正常建立。在兩個站點上，都應在任何丟棄規則之前，在 "input" 鏈中接受該流量。

**Office1**

```ros
/ip/firewall/filter
add action=accept chain=input dst-port=13231 protocol=udp src-address=192.168.80.1
```

**Office2**

```ros
/ip/firewall/filter
add action=accept chain=input dst-port=13231 protocol=udp src-address=192.168.90.1
```

此外，"forward" 鏈也可能限制子網之間的通訊，因此此類流量也應在任何丟棄規則之前被接受。

**Office1**

```ros
/ip/firewall/filter
add action=accept chain=forward dst-address=10.1.202.0/24 src-address=10.1.101.0/24
add action=accept chain=forward dst-address=10.1.101.0/24 src-address=10.1.202.0/24
```

**Office2**

```ros
/ip/firewall/filter
add action=accept chain=forward dst-address=10.1.101.0/24 src-address=10.1.202.0/24
add action=accept chain=forward dst-address=10.1.202.0/24 src-address=10.1.101.0/24
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

新增新的 WireGuard 介面會自動生成一對私鑰和公鑰。你需要在遠端裝置上配置公鑰。要獲取公鑰值，只需列印介面詳情。

```ros
[admin@home] > /interface/wireguard/print 
Flags: X - disabled; R - running 
 0  R name="wireguard1" mtu=1420 listen-port=13231 private-key="cBPD6JNvbEQr73gJ7NmwepSrSPK3np381AWGvBk/QkU=" 
      public-key="VmGMh+cwPdb8//NOhuf1i1VIThypkMQrKAO9Y55ghG8=" 
```

接下來的步驟中，你需要獲取遠端裝置的公鑰。拿到公鑰後，透過指定遠端裝置的公鑰以及允許透過 WireGuard 隧道的允許地址來新增新的對等端。

```ros
/interface/wireguard/peers
add allowed-address=192.168.100.2/32 interface=wireguard1 public-key="<paste public key from remote device here>"
```

## 防火牆注意事項 {#firewall-considerations-1}

如果你配置了預設或嚴格的防火牆，則需要允許遠端裝置與你的裝置建立 WireGuard 連線。

```ros
/ip/firewall/filter
add action=accept chain=input comment="allow WireGuard" dst-port=13231 protocol=udp place-before=1
```

要允許遠端裝置連線到 RouterOS 服務（例如請求 DNS），請在 input 鏈中允許 WireGuard 子網。

```ros
/ip/firewall/filter
add action=accept chain=input comment="allow WireGuard traffic" src-address=192.168.100.0/24 place-before=1
```

或者，只需將 WireGuard 介面新增到 "LAN" 介面列表。

```ros
/interface/list/member
add interface=wireguard1 list=LAN
```

### iOS 配置 {#ios-configuration}

從 App Store 下載 WireGuard 應用程式。開啟它並從頭建立新配置。

![](/img/e4c782efd1e4a573.webp)

首先，為你的連線指定一個 "Name"，並選擇生成金鑰對。生成的公鑰對於 RouterOS 側的對等端配置是必需的。

**![](/img/595359132947760c.webp)**

在 "Addresses" 欄位中指定一個與伺服器側配置處於同一子網的 IP 地址。此地址將用於通訊。在本示例中，我們在 RouterOS 側使用了 192.168.100.1/24。你可以在此處使用 192.168.100.2。

如有必要，配置 DNS 伺服器。如果 RouterOS 側的 IP/DNS 部分將 allow-remote-requests 設定為 yes，你可以在此處指定遠端 WireGuard IP 地址。

**![](/img/e2f9bce3143b113d.webp)**

點選 "Add peer"，會顯示更多引數。

"Public key" 值是在 RouterOS 側的 WireGuard 介面上生成的公鑰值。

"Endpoint" 是 RouterOS 裝置的 IP 或 DNS 及埠號，iOS 裝置可以透過網際網路與其通訊。

"Allowed IPs" 設定為 0.0.0.0/0，以允許所有流量透過 WireGuard 隧道傳送。

![](/img/ff125611431949f1.webp)

```ros
Depending on your configuration, you may need to add a NAT rule
chain=dstnat action=dst-nat to-ports=port protocol=udp in-interface=interface dst-port=port
```

### Windows 10 配置 {#windows-10-configuration}

從 WireGuard 下載 WireGuard 安裝程式  
以管理員身份執行。

![](/img/8e2cdd2818ccadf4.webp)

按 <kbd>Control</kbd>+<kbd>N</kbd> 新增新的空隧道，為介面新增名稱，Public key 應自動生成。將其複製到 RouterOS 對等端配置。  
將其新增到伺服器配置中，因此完整配置如下所示（將自動生成的 PrivateKey 保留在 [Interface] 部分：

```actionscript3
[Interface]
PrivateKey = your_autogenerated_private_key=
Address = 192.168.100.2/24
DNS = 192.168.100.1

[Peer]
PublicKey = your_MikroTik_public_KEY=
AllowedIPs = 0.0.0.0/0
Endpoint = example.com:13231
```

儲存並激活

## 多 WAN 設定 {#multi-wan-setup}

對於 WireGuard，不存在伺服器-用戶端關係；兩端都可以充當端點，並且如果其配置中定義了對等端，兩端都會相互發送 UDP 握手訊息（並非總是如此，因為可以在對等端設定中啟用 "responder" 選項，這將允許你模擬伺服器-用戶端行為：作為“伺服器”的對等端只會回覆來自“用戶端”對等端的握手訊息，而不會自行傳送握手訊息）。  
由於上述隧道建立特性，來自 WireGuard 隧道不同端點的握手訊息會被視為兩個獨立連線。  
對於到“用戶端”對等端存在多條路徑的設定，我們需要考慮這一點，因為這可能導致“伺服器”不透過傳入路由，而是根據設定透過其他路由回覆“用戶端”。  
下面你可以看到一個配置示例，說明如何處理此行為，並確保“伺服器”使用傳入路由回覆“用戶端”。

### 配置示例 {#configuration-example}

此示例不包含 WireGuard 介面配置，因為它適用於具有兩個 WAN 連線的 [RoadWarrior](./wireguard.md#roadwarrior-wireguard-tunnel) 和 [站點到站點](./wireguard.md#site-to-site-wireguard-tunnel) 設定，例如 [PCC](../high-availability-solutions/load-balancing/per-connection-classifier.md) 設定。  
為了使這些規則按預期工作，你需要在 WireGuard 對等端設定中啟用 "responder" 選項，因為路由未被標記時，“伺服器”可能會透過錯誤的介面傳送握手訊息。

```ros
/ip/firewall/mangle 
add action=add-src-to-address-list chain=prerouting address-list=WAN2_WireGuard_clients address-list-timeout=1m dst-port=13231 in-interface=ether2 protocol=udp comment="add source IP address of WAN2 incoming WireGuard traffic to address list"
add action=mark-connection chain=output dst-address-list=WAN2_WireGuard_clients dst-port=13231 new-connection-mark=wan2 protocol=udp comment="mark WireGuard connection to the client peer by checking destination address from the address list" 
add action=mark-routing chain=output connection-mark=wan2 dst-port=13231 new-routing-mark=wan2 protocol=udp comment="ensure that WireGuard traffic uses routing table associated with the WAN2 incoming interface"
add action=add-src-to-address-list chain=prerouting address-list=WAN3_WireGuard_clients address-list-timeout=1m dst-port=13231 in-interface=ether3 protocol=udp comment="add source IP address of WAN3 incoming WireGuard traffic to address list"
add action=mark-connection chain=output dst-address-list=WAN3_WireGuard_clients dst-port=13231 new-connection-mark=wan3 protocol=udp comment="mark WireGuard connection to the client peer by checking destination address from the address list" 
add action=mark-routing chain=output connection-mark=wan3 dst-port=13231 new-routing-mark=wan3 protocol=udp comment="ensure that WireGuard traffic uses routing table associated with the WAN3 incoming interface"
 
/ip/firewall/nat 
add action=masquerade chain=srcnat log=yes out-interface=ether2 comment="ensure that packet has source IP of WAN2 interface"
add action=masquerade chain=srcnat log=yes out-interface=ether3 comment="ensure that packet has source IP of WAN3 interface"
```

第一條 mangle 規則用於透過匹配傳入 WireGuard 握手的目標埠來捕獲源 IP 地址，並將其新增到列表中，該列表隨後將用作標記傳出 WireGuard 握手的方式。超時用於確保將來同一源 IP 地址可以使用不同的 WAN 介面建立 WireGuard 隧道。  
第二條 mangle 規則標記連線，這些連線隨後用於標記路由，並確保當 IP 地址從地址列表中消失且隧道建立後，標記仍保留在連線上。  
第三條 mangle 規則用於強制封包使用第二個 WAN 介面的正確路由表。  
最後一條 NAT 規則是必需的，以確保封包以正確的源 IP 傳送出去，因為它不會被 mangle 規則調整；如果未實施該規則，封包可能會根據設定而具有不同的源 IP。
如你所見，這些規則針對 WAN3 進行了重複，以確保 WAN3 介面也可用於 WireGuard。  
  
此規則集確保 WireGuard 隧道在接收傳入握手的介面上建立。

## 2FA 設定 {#2fa-setup}

[HotSpot](../authentication-authorization-accounting/hotspot-captive-portal/index.md) 服務可以在 RouterOSv7 中繫結到 WireGuard 介面。這允許管理員將 WireGuard 的高效能加密與 HotSpot 的強制門戶功能結合起來，支援透過本地資料庫、User Manager 或 RADIUS 進行額外的使用者級認證，而 OTP 功能可以進一步增強安全性。

### 配置示例 {#configuration-example-1}

確保你的裝置上已配置 Wireguard 介面：

```routeros
/interface/wireguard> print 
Flags: X - DISABLED; R - RUNNING 
 0  R name="wg1" mtu=1420 listen-port=49422 
      public-key="MikroTikMikroTikMikroTik=" 
```

在 Wireguard 介面上設定 HotSpot：

```routeros
/ip/hotspot> setup 
Select interface to run HotSpot on 
hotspot interface: wg1

or
/ip/hotspot/add interface=wg1

*Supported from 7.22
```

完成 HotSpot 設定後，一旦 Wireguard 對等端連線，就需要額外登入門戶才能繼續。可以使用常規的 HotSpot 使用者名稱/密碼授權。為了提高安全性，可以使用 `/ip/hotspot/user` 的 otp-password 或 `/user-manager/user` 的 totp-password 欄位。新增具有 totp-secret 的使用者：

```routeros
/ip/hotspot/user/add name=peer1 totp-secret=HVR4CFHAFOWFGGFAGSA5JVTIMMPG6GMT
```

你可以找到多個開源 TOTP 生成器工具，它們可以為你提供適當的金鑰和必要選項，以便將其匯入你的 "authenticator" 應用。

設定完成後，在你的裝置上啟動 Wireguard；在 Wireguard/HotSpot 伺服器成功授權後，將提示 HotSpot 登入頁面，你需要從 "authenticator" 應用輸入 HotSpot 使用者名稱和 totp 6 位密碼（每 30 秒變化一次）。

強烈建議為 HotSpot 使用 HTTPS 登入頁面，並確保 Wireguard 對等端具有驗證登入頁面證書的選項。
