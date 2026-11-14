---
sidebar_key: "getting-started/networking-fundamentals/ipv6-addresses"
sidebar_position: 1
title: "IPv6 地址"
sidebar_label: "IPv6 地址"
description: "本頁介紹 MikroTik RouterOS 中的 IPv6 定址，涵蓋其相較於 IPv4 的優勢、地址型別與語法、使用零壓縮的簡化表示法、字首表示法，以及不存在廣播地址、由組播地址取代的情況。"
tags:
  - 'fundamentals'
  - 'ip'
  - 'ipv6'
source: https://manual.mikrotik.com/docs/7.25/getting-started/networking-fundamentals/ipv6-addresses
captured_at: '2026-11-04T11:16:44+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

網際網路協定第 6 版（IPv6）是網際網路協定（IP）的較新版本。最初預計它會在足夠短的時間內取代 IPv4，但就目前來看，這兩個版本似乎會在可預見的未來在網際網路上共存。儘管如此，隨著未分配 IPv4 地址池耗盡之日臨近，IPv6 變得越來越重要。

- 四個主要優勢：

- 大得多的地址空間；
- 支援無狀態和有狀態地址自動配置；
- 內建安全性；
- 新的報頭格式（更快的轉發）。

與 IPv4 中的 4 位元組地址相比，IPv6 使用 16 位元組地址。IPv6 地址語法和型別在 [RFC 4291](https://tools.ietf.org/html/rfc4291) 中描述。

IPv6 地址型別有多種，可透過其字首識別。RouterOS 區分以下型別：

- 組播（字首為 ff00::/8）
- 鏈路本地（字首為 fe80::/10）
- 唯一本地地址（字首為 fc00::/7）
- 環回（地址 ::1/128）
- 未指定（地址 ::/128）
- 其他（所有其他地址，包括已廢棄的站點本地地址，以及 [RFC 4193](https://tools.ietf.org/html/rfc4193) 唯一本地地址；它們都被視為全域性單播）。

IPv6 與 IPv4 地址的一個區別是，IPv6 會為每個支援 IPv6 的活動介面自動生成一個 **link-local** IPv6 地址。

IPv6 地址的表示方式與 IPv4 地址略有不同。對於 IPv6，128 位地址被劃分為八個 16 位塊，每個 16 位塊被轉換為 4 位十六進位制數，並用冒號分隔。所得表示形式稱為冒號十六進位制表示法。

在下面的示例中，二進位制格式的 IPv6 地址被轉換為冒號十六進位制表示法

```
0010000000000001 0000010001110000 0001111100001001 0000000100110001
0000000000000000 0000000000000000 0000000000000000 0000000000001001
```

```
2001:0470:1f09:0131:0000:0000:0000:0009
```

可以透過刪除每個塊中的前導零來進一步簡化 IPv6 地址：

```
2001:470:1f09:131:0:0:0:9
```

如你所見，IPv6 地址可能包含很長的零序列。這個連續序列可以壓縮為 **::**

```
2001:470:1f09:131::9
```

:::note
零壓縮只能使用一次。否則，你將無法確定每個雙冒號例項所代表的 0 位數量
:::

IPv6 字首以 **address/prefix-length** 格式書寫。與 IPv4 不同，不能使用網路掩碼的十進位制表示法。字首示例：

```
2001:470:1f09:131::/64
2001:db8:1234::/48
2607:f580::/32
2000::/3
```

IPv6 網路中沒有 **廣播地址**，廣播功能已完全被組播取代。

### 單播地址 {#unicast-addresses}

發往單播地址的封包只交付給單個介面。屬於這一組的有：

- 全域性唯一地址，可用於連線到任何位置的全域性範圍地址；
- 鏈路本地地址；
- 唯一本地地址（ULA RFC4193）
- 站點本地地址（FEC0::/10）— 已棄用；
- 特殊用途地址；
- 相容性地址；

全域性單播地址可以透過 **Stateless Address auto-configuration.** 自動分配給節點。

### 鏈路本地地址 {#link-local-address}

每個啟用 IPv6 的介面都需要鏈路本地地址，即使沒有 IPv6 路由，應用程式也可能依賴鏈路本地地址的存在，這就是為什麼每個活動介面都會使用其介面識別符號（如果存在 MAC 地址，則根據 MAC 地址計算 EUI-64）自動生成鏈路本地地址。地址字首始終為 **FE80::/64**，並且 IPv6 路由器絕不會將鏈路本地流量轉發到鏈路之外。

這些地址可與 IPv4 的自動配置地址 169.254.0.0/16 相類比。

IPv6 鄰居發現過程也需要鏈路本地地址。

:::info
如果介面被設定為橋接埠，則介面特定的鏈路本地地址會被移除，只保留橋接的鏈路本地地址
:::

### 唯一本地地址 {#unique-local-address}

唯一本地地址（ULA）保留用於家庭和企業環境中的本地使用，這些地址不會在公共地址空間中路由，相當於 IPv4 私有地址範圍。

保留地址範圍為 **fc00::/7**

### 特殊用途地址 {#special-purpose-address}

| 地址                             | 描述                                                                                                                                                  |
|:--|:--|
| **未指定地址（::/128）** | 從不會分配給介面或用作目標地址，僅用於表示地址不存在。相當於 IPv4 的 0.0.0.0 地址。 |
| **環回地址（::1/128）**   | 用於標識環回介面，使節點能夠向自身傳送封包。它相當於 IPv4 的環回地址 127.0.0.1。         |
| **2002::/16**                    | 此字首用於 6to4 定址。這裡還會使用 IPv4 網路 192.88.99.0/24 中的一個地址。                                          |
| **2001:db8::/32**                | 保留用於文件的地址範圍。這些地址絕不應被視為源地址或目標地址。                                                    |
| **2001:0010::/28**               | Orchid 固定期限實驗。不應被視為源地址或目標地址                                                                           |
| **2001:0002::/48**               | 用於基準測試，不應被視為源地址或目標地址                                                                                    |
| **2001:0000::/32**               | Teredo                                                                                                                                                |

#### 相容性地址 {#compatibility-address}

| 地址                     | 描述                                                                                                                                                                                                                                                                                                                                                                                                                   |
|:--|:--|
| **IPv4 相容地址** | 由透過 IPv4 基礎設施與 IPv6 通訊的雙棧節點使用。當 IPv4 相容地址用作 IPv6 目標地址時，IPv6 流量會自動用 IPv4 報頭封裝，並透過 IPv4 基礎設施傳送到目標。該地址按以下格式書寫 `::w.x.y.z`，其中 w.x.y.z 是公共 IPv4 地址的點分十進位制表示。 |
| **IPv4 對映地址**     | 用於向 IPv6 節點表示僅支援 IPv4 的節點。它僅用於內部表示。IPv4 對映地址絕不會用作 IPv6 封包的源地址或目標地址。IPv6 協定不支援使用 IPv4 對映地址。該地址按以下格式書寫：`::ffff:w.x.y.z`，其中 `w.x.y.z` 是公共 IPv4 地址的點分十進位制表示。          |

### 組播地址 {#multicast-address}

最重要的組播方面是：

- 流量傳送到單個地址，但由多臺主機處理；
- 組成員關係是動態的，允許主機隨時加入和離開組；
- 在 IPv6 中，使用 Multicast Listener Discovery（MLD）訊息來確定網段（也稱為鏈路或子網）上的組成員關係；
- 主機可以向組的地址傳送流量，而無需屬於相應的組。

單個 IPv6 組播地址標識每個組播組。每個組保留的 IPv6 地址由該組的所有主機成員共享，這些成員偵聽並接收發送到該組地址的任何 IPv6 訊息。

組播地址由以下部分組成：

- 組播地址中的前 8 位始終為 1111 1111（十六進位制格式為 FF）。
- 標誌使用第 9 到第 12 位，表示此組播地址是否為預定義（well-known）。如果是 well-known，則所有位均為 0。
- Scope ID 指示組播地址屬於哪個範圍，例如 Scope ID=2 是鏈路本地範圍。
- 組 ID 用於指定組播組。存在預定義的組 ID，例如 Group ID=1 - 所有節點。因此，如果組播地址是 ff02::1，則表示 Scope ID=2 且 Group ID=1，指示鏈路本地範圍內的所有節點。這類似於 IPv4 上的廣播。

以下是保留用於組播的 IPv6 地址表：

| 地址               | 描述                                                                                                                                                                                                                                                |
|:--|:--|
| **FF02::1**           | 全節點地址用於到達同一鏈路上的所有節點。                                                                                                                                                                                         |
| **FF02::2**           | 全路由器地址用於到達同一鏈路上的所有路由器。                                                                                                                                                                                     |
| **FF02::5**           | 全 Open Shortest Path First（OSPF）路由器地址用於到達同一鏈路上的所有 OSPF 路由器。                                                                                                                                                 |
| **FF02::6**           | 全 OSPF 指定路由器地址用於到達同一鏈路上的所有 OSPF 指定路由器。                                                                                                                                                    |
| **FF02::1:FFXX:XXXX** | 請求節點地址用於地址解析過程，以將鏈路本地節點的 IPv6 地址解析為其鏈路層地址。請求節點地址的最後 24 位（XX:XXXX）是 IPv6 單播地址的最後 24 位。 |

下表是保留用於 IPv6 組播並在 Internet Assigned Numbers Authority（IANA）註冊的 IPv6 組播地址的部分列表。有關已分配地址的完整列表，請閱讀 [IANA 文件。](https://www.iana.org/assignments/ipv6-multicast-addresses/ipv6-multicast-addresses.xhtml)

組播地址可用於發現網路中的節點。例如，發現所有節點

```text
mrz@bumba:/media/aaa/ver$ ping6 ff02::1%eth0
PING ff02::1%eth0(ff02::1) 56 data bytes
64 bytes from fe80::21a:4dff:fe5d:8e56: icmp_seq=1 ttl=64 time=0.037 ms
64 bytes from fe80::20c:42ff:fe0d:2c38: icmp_seq=1 ttl=64 time=4.03 ms (DUP!)
64 bytes from fe80::20c:42ff:fe28:7945: icmp_seq=1 ttl=64 time=5.59 ms (DUP!)
64 bytes from fe80::20c:42ff:fe49:fce5: icmp_seq=1 ttl=64 time=5.60 ms (DUP!)
64 bytes from fe80::20c:42ff:fe21:f1ec: icmp_seq=1 ttl=64 time=5.88 ms (DUP!)
64 bytes from fe80::20c:42ff:fe72:a1b0: icmp_seq=1 ttl=64 time=6.70 ms (DUP!)
```

發現所有路由器

```text
mrz@bumba:/media/aaa/ver$ ping6 ff02::2%eth0
PING ff02::2%eth0(ff02::2) 56 data bytes
64 bytes from fe80::20c:42ff:fe28:7945: icmp_seq=1 ttl=64 time=0.672 ms
64 bytes from fe80::20c:42ff:fe0d:2c38: icmp_seq=1 ttl=64 time=1.44 ms (DUP!)
```

### 任播地址 {#anycast-address}

任播地址是 IPv6 中引入的一種新地址型別。

任播是一種新的網路正規化，支援面向服務的地址，其中可以將相同地址分配給提供特定服務的多個節點。任播封包（具有任播目標地址的封包）會交付給具有相同任播地址的其中一個節點。

任播地址不會分配特定地址範圍。它是從單播地址範圍中分配的。

### 介面識別符號 {#interface-identifier}

IPv6 地址的最後 64 位是介面識別符號，它對於該 IPv6 地址的 64 位字首是唯一的。確定介面識別符號有幾種方法：

- EUI-64；
- 隨機生成以提供一定程度的匿名性；
- 手動配置。

### EUI-64 {#eui-64}

網路介面卡的傳統介面識別符號是 48 位 MAC 地址。此地址由 24 位製造商 ID 和 24 位板卡 ID 組成。

IEEE EUI-64 是網路介面地址的新標準。公司 ID 的長度仍為 24 位，但擴充套件 ID 為 40 位，從而為網路介面卡建立大得多的地址空間。

要從介面 MAC 地址建立 EUI-64 地址：

- 將 0xFFFE 插入到 MAC 地址中的製造商 ID 和板卡 ID 之間。
- 第一個位元組的第七位被反轉。

我們以以下 MAC 地址 00:0C:42:28:79:45 為例。

![](/img/f3620667a3db82e8.png)

上圖說明了轉換過程。當結果轉換為冒號十六進位制表示法時，我們得到介面識別符號 `20C:42FF:FE28:7945`。因此，相應的鏈路本地地址是

```
FE80::20C:42FF:FE28:7945/64
```

在 RouterOS 中，如果配置了地址的 EUI-64 引數，則該地址的最後 64 位會使用介面識別符號自動生成和更新。在這種情況下，最後幾位必須配置為零。示例：

```ros
[admin@MikroTik] > ipv6 address add address=fc00:3::/64 interface=ether3 eui-64=yes
[admin@MikroTik] > ipv6 address print
Flags: X - disabled, I - invalid, D - dynamic, G - global, L - link-local
#    ADDRESS                                     INTERFACE                  ADVERTISE
...
5  G fc00:3::20c:42ff:fe1d:3d4/64                ether3                     yes
[admin@MikroTik] > interface ethernet set ether3 mac-address=10:00:00:00:00:01
[admin@MikroTik] > ipv6 address print
Flags: X - disabled, I - invalid, D - dynamic, G - global, L - link-local
#    ADDRESS                                     INTERFACE                  ADVERTISE
...
5  G fc00:3::1200:ff:fe00:1/64                   ether3                     yes
```

### 配置 IPv6 地址 {#configuring-ipv6-address}

此示例展示如何在兩個路由器之間使用全域性 IPv6 地址設定簡單定址。

R1 配置：

```ros
/ipv6 address
add address=2001:DB8::1/64 interface=ether1 advertise=no
```

R2 配置：

```ros
/ipv6 address
add address=2001:DB8::2/64 interface=ether1 advertise=no
```

檢查地址列表：

```text
[admin@R1] /ipv6 address> print
Flags: X - disabled, I - invalid, D - dynamic, G - global, L - link-local
#    ADDRESS                                     FROM-POOL INTERFACE     ADVERTISE
0  G 2001:db8::1/64                                        ether1        no
3 DL fe80::219:d1ff:fe39:3535/64                           ether1        no
```

請注意，我們新增的地址具有 G 標誌，表示該地址可以全域性路由。介面上還有一個鏈路本地地址，它是為每個支援 IPv6 的介面自動建立的。

測試連通性：

```text
[admin@R1] /ipv6 address> /ping 2001:DB8::2
HOST                                     SIZE TTL TIME  STATUS
2001:db8::2                 56  64 12ms  echo reply
2001:db8::2                 56  64 0ms   echo reply
    sent=2 received=2 packet-loss=0% min-rtt=0ms avg-rtt=6ms max-rtt=12ms
```

### SLAAC IPv6 地址 {#slaac-ipv6-address}

如果在 [`/ipv6/settings`](../../cli-reference/ipv6/settings.md) 選單下啟用了 `accept-router-advertisements` 選項，並且路由器接收到路由器通告封包，則 SLAAC IPv6 地址會自動分配給接收通告的介面。此地址具有 DG 標誌，表示該地址是動態且全域性的。此類地址會顯示 valid 和 lifetime 引數。

```text
[admin@R1] /ipv6/address/print detail where dynamic && global 
Flags: X - disabled, I - invalid, D - dynamic; G - global, L - link-local 
 0 DG address=2001:db8::ba69:f4ff:fe84:545/64 from-pool="" interface=ether1 
      actual-interface=test_fp eui-64=no advertise=no no-dad=no valid=4w2d 
      preferred=1w 
```

如果接受 SLAAC 地址，則還會生成指向 Internet 的動態路由。如果通告封包中指定了限制，該路由也會包含這些限制。例如，hop-limit 和 MTU。如果在同一介面上接收到多個地址，則使用每個介面的 MTU 值中的最低值。

```text
[admin@R1] /routing/route/print detail where slaac 
Flags: X - disabled, F - filtered, U - unreachable, A - active; 
c - connect, s - static, r - rip, b - bgp, o - ospf, d - dhcp, v - vpn, m - modem, a - ldp-address, l - ldp-mapping, g - slaac, y - bgp-mpls-vpn; 
H - hw-offloaded; + - ecmp, B - blackhole 
 Ag + afi=ip6 contribution=active dst-address=::/0 routing-table=main 
       pref-src="" gateway=fe80::ba69:f4ff:fe84:7b2%ether1
       immediate-gw=fe80::ba69:f4ff:fe84:7b2%ether1 distance=1 scope=30 
       target-scope=10 belongs-to="slaac" mtu=1400 hoplimit=10 
       debug.fwp-ptr=0x201C2C00 
```
