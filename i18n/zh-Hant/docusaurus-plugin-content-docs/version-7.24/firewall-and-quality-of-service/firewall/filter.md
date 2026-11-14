---
sidebar_key: "firewall-and-quality-of-service/firewall/filter"
sidebar_position: 3
title: "篩選"
sidebar_label: "篩選"
description: "MikroTik RouterOS 中的防火牆過濾器透過預定義的鏈（input、forward、output）允許或阻止流量，並可透過選項接受特定服務或丟棄惡意封包，從而控制封包流。IPv4 的配置透過 `/ip/firewall/filter` 完成，IPv6 的配置透過 `/ipv6/firewall/filter` 完成，文中還提供了保護路由器和 LAN 裝置的示例。"
tags:
  - 'firewall'
  - 'filtering'
source: https://manual.mikrotik.com/docs/7.24/firewall-and-quality-of-service/firewall/filter
captured_at: '2026-11-04T11:28:11+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

防火牆過濾器用於允許或阻止轉發到本地網路、源自路由器或發往路由器的特定封包。

設定過濾有兩種方法：

- 允許特定流量，並丟棄其餘所有流量。
- 僅丟棄惡意流量，允許其餘所有流量。

這兩種方法都有優缺點；例如，從安全形度來看，第一種方法安全得多，但每當需要接受新服務的流量時，都需要管理員介入。這種策略可以很好地控制流量，並降低因服務配置錯誤而遭到入侵的可能性。

另一方面，在保護客戶網路時，接受使用者可能使用的所有服務將是一場管理噩夢。因此，在高階設定中，仔細規劃防火牆至關重要。

防火牆過濾器由三個無法刪除的預定義鏈組成：

![](/img/654f8f9e527fd6f8.webp)

- **input** - 用於處理透過某個介面**進入路由器**的封包，其目標 IP 地址是路由器的某個地址。經過路由器的封包不會按 input 鏈的規則進行處理。
- **forward** - 用於處理**經過路由器**的封包。
- **output** - 用於處理**源自路由器**並透過某個介面離開路由器的封包。經過路由器的封包不會按 output 鏈的規則進行處理。

防火牆過濾器配置可從 IPv4 的 `/ip/firewall/filter` 選單和 IPv6 的 `/ipv6/firewall/filter` 選單訪問。

## 防火牆示例 {#firewall-example}

我們來看一個基本的防火牆示例，用於保護路由器本身以及路由器後面的用戶端，適用於 IPv4 和 IPv6 協定。

### IPv4 防火牆 {#ipv4-firewall}

#### 保護路由器本身 {#protect-the-router-itself}

設定防火牆時遵循的經驗法則：

- 處理 `new` 連線以減少路由器負載。
- 接受你需要的流量。
- `drop` 其餘所有流量；可以設定 `log=yes` 來記錄部分攻擊者，但請記住，在嚴重攻擊時這可能會增加 CPU 負載。

我們始終先接受已知且已接受的連線，因此第一條規則應該是接受 "established" 和 "related" 連線。

```ros
/ip/firewall/filter
add action=accept chain=input comment="default configuration" connection-state=established,related
```

現在我們可以繼續接受一些新連線，在我們的示例中，我們希望允許從任何地址訪問 ICMP 協定，而其他所有流量只允許來自 192.168.88.2-192.168.88.254 地址範圍。為此，我們建立一個地址列表和兩條防火牆規則。

```ros
/ip/firewall/address-list
add address=192.168.88.2-192.168.88.254 list=allowed_to_router
/ip/firewall/filter
add action=accept chain=input src-address-list=allowed_to_router
add action=accept chain=input protocol=icmp

```

最後，我們丟棄其餘所有流量：

```ros
add action=drop chain=input
```

剛剛建立的完整規則集：

```ros
/ip/firewall/filter
add action=accept chain=input comment="default configuration" connection-state=established,related
add action=accept chain=input src-address-list=allowed_to_router
add action=accept chain=input protocol=icmp
add action=drop chain=input
/ip/firewall/address-list
add address=192.168.88.2-192.168.88.254 list=allowed_to_router
```

#### 保護 LAN 裝置 {#protect-the-lan-devices}

保護使用者的概念非常相似，不同之處在於這裡我們阻止不需要的流量，並接受其餘所有流量。

首先，我們將建立一個名為 "not\_in\_internet" 的 `address-list`，用於防火牆過濾規則：

```ros
/ip/firewall/address-list
add address=0.0.0.0/8 comment=RFC6890 list=not_in_internet
add address=172.16.0.0/12 comment=RFC6890 list=not_in_internet
add address=192.168.0.0/16 comment=RFC6890 list=not_in_internet
add address=10.0.0.0/8 comment=RFC6890 list=not_in_internet
add address=169.254.0.0/16 comment=RFC6890 list=not_in_internet
add address=127.0.0.0/8 comment=RFC6890 list=not_in_internet
add address=224.0.0.0/4 comment=Multicast list=not_in_internet
add address=198.18.0.0/15 comment=RFC6890 list=not_in_internet
add address=192.0.0.0/24 comment=RFC6890 list=not_in_internet
add address=192.0.2.0/24 comment=RFC6890 list=not_in_internet
add address=198.51.100.0/24 comment=RFC6890 list=not_in_internet
add address=203.0.113.0/24 comment=RFC6890 list=not_in_internet
add address=100.64.0.0/10 comment=RFC6890 list=not_in_internet
add address=240.0.0.0/4 comment=RFC6890 list=not_in_internet
```

防火牆過濾規則簡要說明：

- 帶有 *connection-state=established,related* 的封包會被加入 FastTrack 以獲得更快的資料吞吐量，防火牆將只處理新連線。
- 丟棄 *invalid* 連線，並使用字首 "invalid" 記錄它們。
- 丟棄從本地網路嘗試訪問非公共地址的流量；此前已應用 *address-list=not\_in\_internet*；"bridge" 是本地網路介面；使用字首 "!public\_from\_LAN" 記錄（log=yes）這些嘗試。
- 丟棄未經過 NAT 的傳入封包；ether1 是公共介面；使用 "!NAT" 字首記錄嘗試。
- 跳轉到 ICMP 鏈以丟棄不需要的 ICMP 訊息。
- 丟棄來自網際網路的傳入封包，這些封包不是公共 IP 地址；ether1 是公共介面；使用字首 "!public" 記錄嘗試。
- 丟棄來自 LAN 但沒有 LAN IP 的封包；192.168.88.0/24 是本地網路子網。

```ros
/ip/firewall/filter
add action=fasttrack-connection chain=forward comment=FastTrack connection-state=established,related
add action=accept chain=forward comment="Established, Related" connection-state=established,related
add action=drop chain=forward comment="Drop invalid" connection-state=invalid log=yes log-prefix=invalid
add action=drop chain=forward comment="Drop tries to reach not public addresses from LAN" dst-address-list=not_in_internet in-interface=bridge log=yes log-prefix=!public_from_LAN out-interface=!bridge
add action=drop chain=forward comment="Drop incoming packets that are not NAT`ted" connection-nat-state=!dstnat connection-state=new in-interface=ether1 log=yes log-prefix=!NAT
add action=jump chain=forward protocol=icmp jump-target=icmp comment="jump to ICMP filters"
add action=drop chain=forward comment="Drop incoming from internet which is not public IP" in-interface=ether1 log=yes log-prefix=!public src-address-list=not_in_internet
add action=drop chain=forward comment="Drop packets from LAN that do not have LAN IP" in-interface=bridge log=yes log-prefix=LAN_!LAN src-address=!192.168.88.0/24
```

在 "icmp" 鏈中只允許需要的 ICMP 程式碼：

```ros
/ip/firewall/filter
  add chain=icmp protocol=icmp icmp-options=0:0 action=accept \
    comment="echo reply"
  add chain=icmp protocol=icmp icmp-options=3:0 action=accept \
    comment="net unreachable"
  add chain=icmp protocol=icmp icmp-options=3:1 action=accept \
    comment="host unreachable"
  add chain=icmp protocol=icmp icmp-options=3:4 action=accept \
    comment="host unreachable fragmentation required"
  add chain=icmp protocol=icmp icmp-options=8:0 action=accept \
    comment="allow echo request"
  add chain=icmp protocol=icmp icmp-options=11:0 action=accept \
    comment="allow time exceed"
  add chain=icmp protocol=icmp icmp-options=12:0 action=accept \
    comment="allow parameter bad"
  add chain=icmp action=drop comment="deny all other types"
```

### IPv6 防火牆 {#ipv6-firewall}

#### 保護路由器本身 {#protect-the-router-itself-1}

與 IPv4 設定非常相似，只是我們必須處理 IPv6 正常工作所需的更多協定。

首先，我們建立一個 `address-list`，用於允許訪問裝置：

```ros
/ipv6/firewall/address-list/add address=fd12:672e:6f65:8899::/64 list=allowed
```

IPv6 防火牆過濾規則簡要說明：

- 處理 *new* 封包，接受 *established/related* 封包。
- 從 Internet（公共）介面/介面列表中丟棄 *link-local* 地址。
- 接受來自 *link-local* 地址對路由器的訪問，接受用於管理目的的 *multicast* 地址，接受你的源 *address-list* 以訪問路由器。
- 丟棄其餘所有流量。

```ros
/ipv6/firewall/filter
add action=accept chain=input comment="allow established and related" connection-state=established,related
add chain=input action=accept protocol=icmpv6 comment="accept ICMPv6"
add chain=input action=accept protocol=udp port=33434-33534 comment="defconf: accept UDP traceroute"
add chain=input action=accept protocol=udp dst-port=546 src-address=fe80::/10 comment="accept DHCPv6-Client prefix delegation."
add action=drop chain=input in-interface=in_interface_name log=yes log-prefix=dropLL_from_public src-address=fe80::/10
add action=accept chain=input comment="allow allowed addresses" src-address-list=allowed
add action=drop chain=input
/ipv6/firewall/address-list
add address=fe80::/10 list=allowed
add address=xxxx::/48 list=allowed
add address=ff02::/16 comment=multicast list=allowed
```

:::warning
在某些使用 DHCPv6 中繼的設定中，封包的源地址可能不在 link-local 範圍內。在這種情況下，必須刪除或調整規則 #4 的 src-address 引數，以接受中繼地址。
:::

#### 保護 LAN 裝置 {#protect-the-lan-devices-1}

這一步比 IPv4 中更重要。在 IPv4 設定中，用戶端大多擁有本地地址範圍內的地址，並透過 NAT 轉換為公共 IP，因此它們無法從公共網路直接訪問。

IPv6 則是另一回事。在大多數常見設定中，啟用 IPv6 會使你的用戶端可從公共網路訪問，因此必須使用適當的防火牆過濾規則來保護你的客戶。

簡而言之，非常基本的 LAN 保護應該：

- 接受 *established/related*，並處理 *new* 封包。
- 丟棄 *invalid* 封包。
- 接受 ICMPv6 封包。
- 僅接受源自你的用戶端到公共網路的 *new* 連線。
- 丟棄其餘所有流量。

```ros
/ipv6/firewall/filter
add action=accept chain=forward comment=established,related connection-state=established,related
add action=drop chain=forward comment=invalid connection-state=invalid log=yes log-prefix=ipv6,invalid
add action=accept chain=forward comment=icmpv6 in-interface=!in_interface_name protocol=icmpv6
add action=accept chain=forward comment="local network" in-interface=!in_interface_name src-address-list=allowed
add action=drop chain=forward log-prefix=IPV6
```

## RAW 過濾 {#raw-filtering}

防火牆 RAW 表允許在連線跟蹤之前有選擇地繞過或丟棄封包，從而顯著降低 CPU 負載。該工具對於緩解 DoS/DDoS 攻擊非常有用。

RAW 過濾器配置可從 IPv4 的 `/ip/firewall/raw` 選單和 IPv6 的 `/ipv6/firewall/raw` 選單訪問。

RAW 表沒有依賴連線跟蹤的匹配器（例如 connection-state、layer7 等）。
如果封包被標記為繞過連線跟蹤，則不會進行封包分片重組。

此外，RAW 防火牆只能在兩個鏈中設定規則：

- **prerouting** - 用於處理進入路由器的任何封包。
- **output** - 用於處理源自路由器並透過某個介面離開路由器的封包。經過路由器的封包不會按 output 鏈的規則進行處理。

### 基本 RAW 示例 {#basic-raw-example}

假設我們有 OSPF 配置，但由於連線跟蹤，OSPF 出現了鄰接問題。我們可以使用 RAW 規則來解決此問題，方法是不將 OSPF 封包傳送到連線跟蹤。

```ros
/ip/firewall/raw
add chain=prerouting protocol=ospf action=notrack
add chain=output protocol=ospf action=notrack
```

## 閱讀更多 {#read-more}

- [構建高階防火牆](../user-guides/building-advanced-firewall.md)
- [連線速率](../user-guides/connection-rate.md)
- [SSH 暴力破解防護](../user-guides/bruteforce-prevention.md)
- [Syn/DoS 防護](../user-guides/ddos-protection.md)
