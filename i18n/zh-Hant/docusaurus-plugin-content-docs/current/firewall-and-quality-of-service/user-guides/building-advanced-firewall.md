---
sidebar_key: "firewall-and-quality-of-service/user-guides/building-advanced-firewall"
sidebar_position: 2
title: "構建高階防火牆"
sidebar_label: "構建高階防火牆"
description: "本頁介紹如何在 MikroTik RouterOS 上構建高階防火牆：配置介面列表、IPv4 和 IPv6 過濾規則，在接受 ICMP/DHCPv6 的同時阻止無效地址，並管理 WAN 與 LAN 介面之間的流量。"
tags:
  - 'firewall'
source: https://manual.mikrotik.com/docs/firewall-and-quality-of-service/user-guides/building-advanced-firewall
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

基於我們目前討論的所有內容，現在來構建一個高階防火牆。在本示例中，我們將實現儘可能多的防火牆功能，以演示它們如何工作以及何時應正確使用它們。

大部分過濾將在 RAW 防火牆中處理。標準防火牆配置通常只包含一組基本規則，用於接受 established、related 和 untracked 連線，同時丟棄所有並非源自 LAN 介面的其他內容，從而為路由器提供全面保護。

### 介面列表 {#interface-lists}

定義了兩個介面列表：**WAN** 和 **LAN**。這些列表根據介面的網路角色對其進行分組，從而簡化未來的管理。WAN 列表包含連線到全球網際網路的介面，例如本配置中的 *ether1*。LAN 列表包含本地網路介面，例如 bridge 介面。

```ros
/interface/list
  add comment=defconf name=WAN
  add comment=defconf name=LAN
/interface/list/member
  add comment=defconf interface=bridge list=LAN
  add comment=defconf interface=ether1 list=WAN
```

此配置將 bridge 介面分配到 LAN 列表，將 ether1 分配到 WAN 列表，從而能夠跨這些介面組一致地應用防火牆規則。

### 保護裝置 {#protect-the-device}

這裡的主要目標是僅允許從 LAN 訪問路由器，並丟棄其他所有內容。

請注意，這裡也接受 ICMP；它用於接受已透過 RAW 規則的 ICMP 封包。

```ros
/ip/firewall/filter
  add action=accept chain=input comment="defconf: accept ICMP after RAW" protocol=icmp
  add action=accept chain=input comment="defconf: accept established,related,untracked" connection-state=established,related,untracked
  add action=drop chain=input comment="defconf: drop all not coming from LAN" in-interface-list=!LAN
```

IPv6 部分稍微複雜一些，此外，按照 RFC 建議，還接受 UDP traceroute、DHCPv6 用戶端 PD 和 IPSec（IKE、AH、ESP）。

```ros
/ipv6/firewall/filter
add action=accept chain=input comment="defconf: accept ICMPv6 after RAW" protocol=icmpv6
add action=accept chain=input comment="defconf: accept established,related,untracked" connection-state=established,related,untracked
add action=accept chain=input comment="defconf: accept UDP traceroute" dst-port=33434-33534 protocol=udp 
add action=accept chain=input comment="defconf: accept DHCPv6-Client prefix delegation." dst-port=546 protocol=udp src-address=fe80::/10
add action=accept chain=input comment="defconf: accept IKE" dst-port=500,4500 protocol=udp
add action=accept chain=input comment="defconf: accept IPSec AH" protocol=ipsec-ah
add action=accept chain=input comment="defconf: accept IPSec ESP" protocol=ipsec-esp
add action=drop chain=input comment="defconf: drop all not coming from LAN" in-interface-list=!LAN
```

:::warning
在某些使用 DHCPv6 中繼的設定中，封包的源地址可能不在 link-local 範圍內。在這種情況下，必須刪除或調整規則 #4 的 src-address 引數，以接受中繼地址。
:::

### 保護用戶端 {#protect-the-clients}

在配置防火牆規則集之前，請建立一個地址列表，其中包含所有不應被轉發的 IPv4 和 IPv6 地址。此列表可防止無效或保留地址透過您的網路進行路由。

請注意，此列表中包含一個組播地址範圍。由於大多數網路通常不使用組播，因此此條目預設會阻止組播流量。如果您的網路需要組播轉發，請停用此地址列表條目。

```ros
/ip/firewall/address-list
  add address=0.0.0.0/8 comment="defconf: RFC6890" list=no_forward_ipv4
  add address=169.254.0.0/16 comment="defconf: RFC6890" list=no_forward_ipv4
  add address=224.0.0.0/4 comment="defconf: multicast" list=no_forward_ipv4
  add address=255.255.255.255/32 comment="defconf: RFC6890" list=no_forward_ipv4
```

對於 IPv6，應用相同的原則：如果需要組播轉發，請停用地址列表中的組播條目。

```ros
/ipv6/firewall/address-list
  add address=fe80::/10  comment="defconf: RFC6890 Link-Scoped Unicast" list=no_forward_ipv6
  add address=ff00::/8  comment="defconf: multicast" list=no_forward_ipv6
```

Forward 鏈包含的規則比 Input 鏈更多，並執行以下操作：

- 接受 established、related 和 untracked 連線
- 對 established 和 related 連線進行 FastTrack（僅 IPv4）
- 丟棄 invalid 連線狀態
- 丟棄不應被路由的錯誤轉發 IP 地址
- 丟棄從網際網路（WAN 側）發起且未被目標 NAT 的連線嘗試
- 丟棄不應被轉發的 bogon IP 地址

此配置會丟棄所有未被目標 NAT 的 IPv4 封包，以在外部攻擊者知道您的內部 LAN 網路範圍時保護用戶端裝置免受直接攻擊。雖然此規則通常不必要，因為 RAW 過濾已經丟棄了這些封包，但它在 RAW 規則配置被意外修改時提供了額外的安全層。

```ros
/ip/firewall/filter
  add action=accept chain=forward comment="defconf: accept all that matches IPSec policy" ipsec-policy=in,ipsec disabled=yes
  add action=fasttrack-connection chain=forward comment="defconf: fasttrack" connection-state=established,related
  add action=accept chain=forward comment="defconf: accept established,related, untracked" connection-state=established,related,untracked
  add action=drop chain=forward comment="defconf: drop invalid" connection-state=invalid
  add action=drop chain=forward comment="defconf:  drop all from WAN not DSTNATed" connection-nat-state=!dstnat connection-state=new in-interface-list=WAN
  add action=drop chain=forward src-address-list=no_forward_ipv4 comment="defconf: drop bad forward IPs"
  add action=drop chain=forward dst-address-list=no_forward_ipv4 comment="defconf: drop bad forward IPs"
```

IPv6 Forward 鏈遵循類似的結構，並增加了按照 RFC 標準建議接受 IPsec 和 HIP 協定的規則。hop-limit 為 1 的 ICMPv6 封包會被丟棄。

```ros
/ipv6/firewall/filter
add action=accept chain=forward comment="defconf: accept established,related,untracked" connection-state=established,related,untracked
add action=drop chain=forward comment="defconf: drop invalid" connection-state=invalid
add action=drop chain=forward src-address-list=no_forward_ipv6 comment="defconf: drop bad forward IPs"
add action=drop chain=forward dst-address-list=no_forward_ipv6 comment="defconf: drop bad forward IPs"
add action=drop chain=forward comment="defconf: rfc4890 drop hop-limit=1" hop-limit=equal:1 protocol=icmpv6
add action=accept chain=forward comment="defconf: accept ICMPv6 after RAW" protocol=icmpv6
add action=accept chain=forward comment="defconf: accept HIP" protocol=139
add action=accept chain=forward comment="defconf: accept IKE" protocol=udp dst-port=500,4500
add action=accept chain=forward comment="defconf: accept AH" protocol=ipsec-ah
add action=accept chain=forward comment="defconf: accept ESP" protocol=ipsec-esp
add action=accept chain=forward comment="defconf: accept all that matches IPSec policy" ipsec-policy=in,ipsec
add action=drop chain=forward comment="defconf: drop everything else not coming from LAN" in-interface-list=!LAN
```

請注意 IPsec 策略匹配規則。關鍵是 IPsec 封裝流量必須繞過 FastTrack 連線功能。因此，包含了一條已停用的規則，用於接受匹配 IPsec 策略的流量。每當路由器上使用 IPsec 隧道時，請啟用此規則。IPv6 不需要考慮這一點，因為它不支援 FastTrack。

處理 IPsec 流量的另一種方法是新增 RAW 規則，這將在本文件的 RAW 部分中介紹。

### 偽裝本地網路 {#masquerade-local-network}

為了讓路由器後面的本地裝置能夠訪問網際網路，必須對本地網路進行偽裝。在大多數情況下，建議使用 src-nat 而不是 masquerade，但是，在 WAN 地址為動態地址的情況下，這是唯一的選擇。

```ros
/ip/firewall/nat
  add action=accept chain=srcnat comment="defconf: accept all that matches IPSec policy" ipsec-policy=out,ipsec disabled=yes
  add action=masquerade chain=srcnat comment="defconf: masquerade" out-interface-list=WAN
```

請注意這條已停用的策略匹配規則，與防火牆過濾器中相同，必須將 IPSec 流量排除在 NAT 之外（除非在特定場景中，IPsec 策略配置為匹配經過 NAT 的地址）。因此，每當路由器上使用 IPsec 隧道時，都必須啟用此規則。

## RAW 過濾 {#raw-filtering}

### IPv4 地址列表 {#ipv4-address-lists}

在設定 RAW 規則之前，讓我們建立一些過濾策略所需的地址列表。將以 RFC 6890 作為參考。

首先，*address-list* 包含所有不能用作 src/dst/轉發等的 IPv4 地址（如果看到此類地址，將立即丟棄）

```ros
/ip/firewall/address-list
  add address=127.0.0.0/8 comment="defconf: RFC6890" list=bad_ipv4
  add address=192.0.0.0/24 comment="defconf: RFC6890" list=bad_ipv4
  add address=192.0.2.0/24 comment="defconf: RFC6890 documentation" list=bad_ipv4
  add address=198.51.100.0/24 comment="defconf: RFC6890 documentation" list=bad_ipv4
  add address=203.0.113.0/24 comment="defconf: RFC6890 documentation" list=bad_ipv4
  add address=240.0.0.0/4 comment="defconf: RFC6890 reserved" list=bad_ipv4
```

另一個地址列表包含所有無法在全球範圍內路由的 IPv4 地址。

```ros
/ip/firewall/address-list
  add address=0.0.0.0/8 comment="defconf: RFC6890" list=not_global_ipv4
  add address=10.0.0.0/8 comment="defconf: RFC6890" list=not_global_ipv4
  add address=100.64.0.0/10 comment="defconf: RFC6890" list=not_global_ipv4
  add address=169.254.0.0/16 comment="defconf: RFC6890" list=not_global_ipv4
  add address=172.16.0.0/12 comment="defconf: RFC6890" list=not_global_ipv4
  add address=192.0.0.0/29 comment="defconf: RFC6890" list=not_global_ipv4
  add address=192.168.0.0/16 comment="defconf: RFC6890" list=not_global_ipv4
  add address=198.18.0.0/15 comment="defconf: RFC6890 benchmark" list=not_global_ipv4
  add address=255.255.255.255/32 comment="defconf: RFC6890" list=not_global_ipv4
```

最後兩個地址列表用於不能用作目標地址或源地址的地址。

```ros
/ip/firewall/address-list
  add address=224.0.0.0/4 comment="defconf: multicast" list=bad_src_ipv4
  add address=255.255.255.255/32 comment="defconf: RFC6890" list=bad_src_ipv4
  add address=0.0.0.0/8 comment="defconf: RFC6890" list=bad_dst_ipv4
  add address=224.0.0.0/4 comment="defconf: RFC6890" list=bad_dst_ipv4
```

### IPv4 RAW 規則 {#ipv4-raw-rules}

RAW IPv4 規則將執行以下操作：

- **新增停用的 "accept" 規則** - 可用於快速停用 RAW 過濾，而無需停用所有 RAW 規則。
- **接受** DHCP 發現 - 大多數 DHCP 封包不會被 IP 防火牆看到，但其中一些會，因此請確保它們被接受。
- **丟棄**使用 bogon IP 的封包。
- **丟棄**來自無效 SRC 和 DST IP 的封包。
- **丟棄**來自 WAN 的全域性不可路由 IP。
- **丟棄**來自 LAN 且源地址不等於 192.168.88.0/24（預設 IP 範圍）的封包。
- **丟棄**從 WAN 發來並要轉發到 192.168.88.0/24 網路的封包；如果攻擊者知道內部網路，這將提供保護。
- **丟棄**錯誤的 ICMP、UDP 和 TCP。
- **接受**來自 WAN 和 LAN 的所有其他內容。
- **接受**路由器介面之間的本地流量。
- **丟棄**所有其他內容，以確保任何新新增的介面（例如到服務提供商的 PPPoE 連線）都受到保護，避免意外錯誤配置。

```ros
/ip/firewall/raw
add action=accept chain=prerouting comment="defconf: enable for transparent firewall" disabled=yes
add action=accept chain=prerouting comment="defconf: accept DHCP discover" dst-address=255.255.255.255 dst-port=67 in-interface-list=LAN protocol=udp src-address=0.0.0.0 src-port=68
add action=drop chain=prerouting comment="defconf: drop bogon IP's" src-address-list=bad_ipv4
add action=drop chain=prerouting comment="defconf: drop bogon IP's" dst-address-list=bad_ipv4
add action=drop chain=prerouting comment="defconf: drop bogon IP's" src-address-list=bad_src_ipv4
add action=drop chain=prerouting comment="defconf: drop bogon IP's" dst-address-list=bad_dst_ipv4
add action=drop chain=prerouting comment="defconf: drop non global from WAN" src-address-list=not_global_ipv4 in-interface-list=WAN
add action=drop chain=prerouting comment="defconf: drop forward to local lan from WAN" in-interface-list=WAN dst-address=192.168.88.0/24
add action=drop chain=prerouting comment="defconf: drop local if not from default IP range" in-interface-list=LAN src-address=!192.168.88.0/24
add action=drop chain=prerouting comment="defconf: drop bad UDP" port=0 protocol=udp
add action=jump chain=prerouting comment="defconf: jump to ICMP chain" jump-target=icmp4 protocol=icmp
add action=jump chain=prerouting comment="defconf: jump to TCP chain" jump-target=bad_tcp protocol=tcp
add action=accept chain=prerouting comment="defconf: accept everything else from LAN" in-interface-list=LAN
add action=accept chain=prerouting comment="defconf: accept everything else from WAN" in-interface-list=WAN
add action=accept chain=prerouting comment="defconf: accept local traffic between router interfaces" src-address-type=local
add action=drop chain=prerouting comment="defconf: drop the rest"
```

請注意，我們使用了一些可選鏈，第一個 **TCP** 鏈用於丟棄已知為 *invalid* 的 **TCP** 封包。

```ros
/ip/firewall/raw
add action=drop chain=bad_tcp comment="defconf: TCP flag filter" protocol=tcp tcp-flags=!fin,!syn,!rst,!ack
add action=drop chain=bad_tcp comment=defconf protocol=tcp tcp-flags=fin,syn
add action=drop chain=bad_tcp comment=defconf protocol=tcp tcp-flags=fin,rst
add action=drop chain=bad_tcp comment=defconf protocol=tcp tcp-flags=fin,!ack
add action=drop chain=bad_tcp comment=defconf protocol=tcp tcp-flags=fin,urg
add action=drop chain=bad_tcp comment=defconf protocol=tcp tcp-flags=syn,rst
add action=drop chain=bad_tcp comment=defconf protocol=tcp tcp-flags=rst,urg
add action=drop chain=bad_tcp comment="defconf: TCP port 0 drop" port=0 protocol=tcp
```

另一個鏈用於 **ICMP**。請注意，如果你想要非常嚴格的防火牆，則可以使用這種嚴格的 **ICMP** 過濾，但在大多數情況下，這沒有必要，只會增加路由器 CPU 的負載。大多數情況下，ICMP 速率限制也沒有必要，因為 Linux 核心已經將 ICMP 封包限制為 100pps。

```ros
/ip/firewall/raw
add action=accept chain=icmp4 comment="defconf: echo reply" icmp-options=0:0 limit=5,10:packet protocol=icmp
add action=accept chain=icmp4 comment="defconf: net unreachable" icmp-options=3:0 protocol=icmp
add action=accept chain=icmp4 comment="defconf: host unreachable" icmp-options=3:1 protocol=icmp
add action=accept chain=icmp4 comment="defconf: protocol unreachable" icmp-options=3:2 protocol=icmp
add action=accept chain=icmp4 comment="defconf: port unreachable" icmp-options=3:3 protocol=icmp
add action=accept chain=icmp4 comment="defconf: fragmentation needed" icmp-options=3:4 protocol=icmp
add action=accept chain=icmp4 comment="defconf: echo" icmp-options=8:0 limit=5,10:packet protocol=icmp
add action=accept chain=icmp4 comment="defconf: time exceeded " icmp-options=11:0-255 protocol=icmp
add action=drop chain=icmp4 comment="defconf: drop other icmp" protocol=icmp
```

### IPv6 地址列表 {#ipv6-address-lists}

#### 應立即丟棄的 IPv6 地址列表 {#list-of-ipv6-addresses-that-should-be-dropped-instantly}

```ros
/ipv6/firewall/address-list
add address=::1/128 comment="defconf: RFC6890 lo" list=bad_ipv6
add address=::ffff:0:0/96 comment="defconf: RFC6890 IPv4 mapped" list=bad_ipv6
add address=2001::/23 comment="defconf: RFC6890" list=bad_ipv6
add address=2001:db8::/32 comment="defconf: RFC6890 documentation" list=bad_ipv6
add address=2001:10::/28 comment="defconf: RFC6890 orchid" list=bad_ipv6
add address=::/96 comment="defconf: ipv4 compat" list=bad_ipv6
```

#### 全域性不可路由的 IPv6 地址列表 {#list-of-ipv6-addresses-that-are-not-globally-routable}

```ros
/ipv6/firewall/address-list
add address=100::/64 comment="defconf: RFC6890 Discard-only" list=not_global_ipv6
add address=2001::/32 comment="defconf: RFC6890 TEREDO" list=not_global_ipv6
add address=2001:2::/48 comment="defconf: RFC6890 Benchmark" list=not_global_ipv6
add address=fc00::/7 comment="defconf: RFC6890 Unique-Local" list=not_global_ipv6
```

#### 作為無效目標地址的地址列表 {#list-of-addresses-as-an-invalid-destination-address}

```ros
/ipv6/firewall/address-list/add address=::/128 comment="defconf: unspecified" list=bad_dst_ipv6
```

#### 作為無效源地址的地址列表 {#list-of-addresses-as-an-invalid-source-address}

```ros
/ipv6/firewall/address-list
  add address=::/128 comment="defconf: unspecified" list=bad_src_ipv6
  add address=ff00::/8  comment="defconf: multicast" list=bad_src_ipv6
```

### IPv6 RAW 規則 {#ipv6-raw-rules}

RAW IPv6 規則將執行以下操作：

- **新增一條停用的 accept 規則** - 可用於快速停用 RAW 過濾，而無需停用所有 RAW 規則。
- **丟棄**使用 bogon IP 的封包。
- **丟棄**來自無效 SRC 和 DST IP 的封包。
- **丟棄**來自 WAN 的全域性不可路由 IP。
- **丟棄**錯誤的 ICMP。
- **接受**來自 WAN 和 LAN 的所有其他內容。
- **丟棄**所有其他內容，以確保任何新新增的介面（例如到服務提供商的 PPPoE 連線）都受到保護，避免意外錯誤配置。

```ros
/ipv6/firewall/raw
add action=accept chain=prerouting comment="defconf: enable for transparent firewall" disabled=yes
add action=accept chain=prerouting comment="defconf: RFC4291, section 2.7.1" src-address=::/128 dst-address=ff02:0:0:0:0:1:ff00::/104 icmp-options=135 protocol=icmpv6
add action=drop chain=prerouting comment="defconf: drop bogon IP's" src-address-list=bad_ipv6
add action=drop chain=prerouting comment="defconf: drop bogon IP's" dst-address-list=bad_ipv6
add action=drop chain=prerouting comment="defconf: drop packets with bad SRC ipv6" src-address-list=bad_src_ipv6
add action=drop chain=prerouting comment="defconf: drop packets with bad dst ipv6" dst-address-list=bad_dst_ipv6
add action=drop chain=prerouting comment="defconf: drop non global from WAN" src-address-list=not_global_ipv6 in-interface-list=WAN
add action=jump chain=prerouting comment="defconf: jump to ICMPv6 chain" jump-target=icmp6 protocol=icmpv6
add action=accept chain=prerouting comment="defconf: accept local multicast scope" dst-address=ff02::/16
add action=drop chain=prerouting comment="defconf: drop other multicast destinations" dst-address=ff00::/8
add action=accept chain=prerouting comment="defconf: accept everything else from WAN" in-interface-list=WAN
add action=accept chain=prerouting comment="defconf: accept everything else from LAN" in-interface-list=LAN
add action=drop chain=prerouting comment="defconf: drop the rest"
```

請注意，使用了可選的 **ICMP** 鏈。如果你想要非常嚴格的防火牆，則可以使用這種嚴格的 **ICMP** 過濾，但在大多數情況下，這沒有必要，只會增加路由器 CPU 的負載。大多數情況下，ICMP 速率限制也沒有必要，因為 Linux 核心已經將 ICMP 封包限制為 100pps。

```ros
/ipv6/firewall/raw
# 请注意，不同的操作系统发出的数据包具有不同的默认 TTL 值
add action=drop chain=icmp6 comment="defconf: rfc4890 drop ll if hop-limit!=255" dst-address=fe80::/10 hop-limit=not-equal:255 protocol=icmpv6
add action=accept chain=icmp6 comment="defconf: dst unreachable" icmp-options=1:0-255 protocol=icmpv6
add action=accept chain=icmp6 comment="defconf: packet too big" icmp-options=2:0-255 protocol=icmpv6
add action=accept chain=icmp6 comment="defconf: limit exceeded" icmp-options=3:0-1 protocol=icmpv6
add action=accept chain=icmp6 comment="defconf: bad header" icmp-options=4:0-2 protocol=icmpv6
add action=accept chain=icmp6 comment="defconf: Mobile home agent address discovery" icmp-options=144:0-255 protocol=icmpv6
add action=accept chain=icmp6 comment="defconf: Mobile home agent address discovery" icmp-options=145:0-255 protocol=icmpv6
add action=accept chain=icmp6 comment="defconf: Mobile prefix solic" icmp-options=146:0-255 protocol=icmpv6
add action=accept chain=icmp6 comment="defconf: Mobile prefix advert" icmp-options=147:0-255 protocol=icmpv6
add action=accept chain=icmp6 comment="defconf: echo request limit 5,10" icmp-options=128:0-255 limit=5,10:packet protocol=icmpv6
add action=accept chain=icmp6 comment="defconf: echo reply limit 5,10" icmp-options=129:0-255 limit=5,10:packet protocol=icmpv6
add action=accept chain=icmp6 comment="defconf: rfc4890 router solic limit 5,10 only LAN" hop-limit=equal:255 icmp-options=133:0-255 in-interface-list=LAN limit=5,10:packet protocol=icmpv6
add action=accept chain=icmp6 comment="defconf: rfc4890 router advert limit 5,10 only LAN" hop-limit=equal:255 icmp-options=134:0-255 in-interface-list=LAN limit=5,10:packet protocol=icmpv6
add action=accept chain=icmp6 comment="defconf: rfc4890 neighbor solic limit 5,10 only LAN" hop-limit=equal:255 icmp-options=135:0-255 in-interface-list=LAN limit=5,10:packet protocol=icmpv6
add action=accept chain=icmp6 comment="defconf: rfc4890 neighbor advert limit 5,10 only LAN" hop-limit=equal:255 icmp-options=136:0-255 in-interface-list=LAN limit=5,10:packet protocol=icmpv6
add action=accept chain=icmp6 comment="defconf: rfc4890 inverse ND solic limit 5,10 only LAN" hop-limit=equal:255 icmp-options=141:0-255 in-interface-list=LAN limit=5,10:packet protocol=icmpv6
add action=accept chain=icmp6 comment="defconf: rfc4890 inverse ND advert limit 5,10 only LAN" hop-limit=equal:255 icmp-options=142:0-255 in-interface-list=LAN limit=5,10:packet protocol=icmpv6
add action=drop chain=icmp6 comment="defconf: drop other icmp" protocol=icmpv6

```
