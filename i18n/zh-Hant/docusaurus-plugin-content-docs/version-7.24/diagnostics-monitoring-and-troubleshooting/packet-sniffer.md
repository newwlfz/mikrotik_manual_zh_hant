---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/packet-sniffer"
sidebar_position: 4
title: "封包嗅探器"
sidebar_label: "封包嗅探器"
description: "Packet Sniffer 是一款 MikroTik RouterOS 工具，用於捕獲和分析網路封包，以診斷問題或檢測安全威脅。它支援按 IP、MAC、埠、協定等過濾，並可將封包儲存為 PCAPNG 格式或將其流式傳輸到 PC 進行分析。"
tags:
  - 'packet-sniffer'
  - 'filtering'
source: https://manual.mikrotik.com/docs/7.24/diagnostics-monitoring-and-troubleshooting/packet-sniffer
captured_at: '2026-11-04T11:28:03+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

A packet sniffer 是一種工具，可以捕獲並分析發往路由器、從路由器發出或經過路由器的封包。封包嗅探在診斷網路或防範網路攻擊時非常有用。

:::warning
啟用了用戶端到用戶端轉發的無線用戶端之間的單播流量將不會對嗅探器工具可見。

**警告：** 在網橋上啟用硬體解除安裝後處理的封包將不可見（未知單播、廣播和組播等泛洪流量可能可見）。

**提示：** 嗅探器會在封包進入防火牆之前（direction=rx）或離開防火牆之後（direction=tx）捕獲封包。
:::

## 封包嗅探器配置 {#packet-sniffer-configuration}

RouterOS 內建嗅探器允許你基於各種協定捕獲封包。

在以下示例中，我們將配置嗅探器來匹配經過 ether1 介面的封包：

```ros
[admin@MikroTik] > /tool/sniffer/start interface=ether1           
[admin@MikroTik] > /tool/sniffer/stop                             
[admin@MikroTik] > /tool/sniffer/save file-name=/flash/test.pcap            
MikroTik] > /file/print where name~"test" 
Columns: NAME, TYPE, SIZE, CREATION-TIME
#  NAME        TYPE  SIZE  CREATION-TIME       
9  flash/test.pcap  file  3696  2019-12-04 10:48:16
```

你可以從檔案部分下載捕獲的封包。然後可以使用 [Wireshark](https://www.wireshark.org/) 等封包分析器來分析檔案：

![](/img/51eba29d22b6b595.webp)

如果你將封包流式傳輸到 PC 並使用 Wireshark，為確保只檢視流式傳輸的資料，需要應用與嗅探器所用埠匹配的過濾器；預設使用 37008。此外，建議使用 `filter-stream=yes`。

![](/img/8c085953276cc99e.png)

:::warning
請注意，嗅探到的封包將保留 10 分鐘。如果需要永久儲存，請設定 "file-name" 直接儲存它們，或如前所述執行 "save" 命令。

**重要：** 從 RouterOS 7.20 開始，嗅探器工具以 PCAPNG 格式儲存捕獲的封包。[流量生成器](./traffic-generator.md) 功能從 RouterOS 7.21 開始支援 PCAPNG 格式。
:::

**子選單：** `/tool/sniffer`

| 屬性 | 描述 |
| :-- | :-- |
| **file-limit** (*integer 10..4294967295[KiB]*；預設值：**1000KiB**) | 檔案大小限制。達到限制時，嗅探器將停止。 |
| **file-name** (*string*；預設值：) | 儲存嗅探到的封包的檔名。 |
| **filter-cpu** (*integer*；預設值：) | 用作過濾器的 CPU 核心。 |
| **filter-ip-address** (*ip/mask[,ip/mask]（最多 16 項）*；預設值：) | 最多 16 個用作過濾器的 IP 地址。 |
| **filter-dst-ip-address** (*ip/mask[,ip/mask]（最多 16 項）*；預設值：) | 最多 16 個用作過濾器的 IP 目標地址。 |
| **filter-src-ip-address** (*ip/mask[,ip/mask]（最多 16 項）*；預設值：) | 最多 16 個用作過濾器的 IP 源地址。 |
| **filter-ipv6-address** (*ipv6/mask[,ipv6/mask]（最多 16 項）*；預設值：) | 最多 16 個用作過濾器的 IPv6 地址。 |
| **filter-dst-ipv6-address** (*ipv6/mask[,ipv6/mask]（最多 16 項）*；預設值：) | 最多 16 個用作過濾器的 IPv6 目標地址。 |
| **filter-src-ipv6-address** (*ipv6/mask[,ipv6/mask]（最多 16 項）*；預設值：) | 最多 16 個用作過濾器的 IPv6 源地址。 |
| **filter-mac-address** (*mac/mask[,mac/mask]（最多 16 項）*；預設值：) | 最多 16 個用作過濾器的 MAC 地址和 MAC 地址掩碼。 |
| **filter-dst-mac-address** (*mac/mask[,mac/mask]（最多 16 項）*；預設值：) | 最多 16 個用作過濾器的 MAC 目標地址和 MAC 地址掩碼。 |
| **filter-src-mac-address** (*mac/mask[,mac/mask]（最多 16 項）*；預設值：) | 最多 16 個用作過濾器的 MAC 源地址和 MAC 地址掩碼。 |
| **filter-port** (*[!]port[,port]（最多 16 項）*；預設值：) | 最多 16 個逗號分隔的埠用作過濾器。還提供預定義埠名稱列表，例如 ssh 和 telnet。 |
| **filter-dst-port** (*[!]port[,port]（最多 16 項）*；預設值：) | 最多 16 個逗號分隔的目標埠用作過濾器。還提供預定義埠名稱列表，例如 ssh 和 telnet。 |
| **filter-src-port** (*[!]port[,port]（最多 16 項）*；預設值：) | 最多 16 個逗號分隔的源埠用作過濾器。還提供預定義埠名稱列表，例如 ssh 和 telnet。 |
| **filter-ip-protocol** (*[!]protocol[,protocol]（最多 16 項）*；預設值：) | 最多 16 個逗號分隔的 IP/IPv6 協定用作過濾器。IP 協定（可以使用協定編號代替協定名稱）：ipsec-ah - IPsec AH protocolipsec-esp - IPsec ESP protocolddp - datagram delivery protocolegp - exterior gateway protocolggp - gateway-gateway protocolgre - general routing encapsulationhmp - host monitoring protocolidpr-cmtp - idpr control message transporticmp - internet control message protocolicmpv6 - internet control message protocol v6igmp - internet group management protocolipencap - ip encapsulated in ipipip - ip encapsulationencap - ip encapsulationiso-tp4 - iso transport protocol class 4ospf - open shortest path firstpup - parc universal packet protocolpim - protocol independent multicastrspf - radio shortest path firstrdp - reliable datagram protocolst - st datagram modetcp - transmission control protocoludp - user datagram protocolvmtp - versatile message transportvrrp - virtual router redundancy protocolxns-idp - xerox xns idpxtp - xpress transfer protocol |
| **filter-mac-protocol**(*[!]protocol[,protocol]（最多 16 項）*；預設值：) | 最多 16 個逗號分隔的條目用作過濾器。MAC 協定（可以使用協定編號代替協定名稱）：802.2 - 802.2 Frames (0x0004)arp - Address Resolution Protocol (0x0806)capsman - CAPsMAN to CAP MAC layer connection (0x88BB)dot1x - EAPoL IEEE 802.1X (0x888E)homeplug-av - HomePlug AV MME (0x88E1)ip - Internet Protocol version 4 (0x0800)ipv6 - Internet Protocol Version 6 (0x86DD)ipx - Internetwork Packet Exchange (0x8137)lacp - Link Aggregation Control Protocol (0x8809)lldp - Link Layer Discovery Protocol (0x88CC)loop-protect - Loop Protect Protocol (0x9003)macsec - MAC security IEEE 802.1AE (0x88E5)mpls-multicast - MPLS multicast (0x8848)mpls-unicast - MPLS unicast (0x8847)mvrp - Multiple VLAN Registration protocol (0x88F5)packing-compr - Encapsulated packets with compressed IP packing (0x9001)packing-simple - Encapsulated packets with simple IP packing (0x9000)pppoe - PPPoE Session Stage (0x8864)pppoe-discovery - PPPoE Discovery Stage (0x8863)rarp - Reverse Address Resolution Protocol (0x8035)romon - Router Management Overlay Network RoMON (0x88BF)service-vlan - Provider Bridging (IEEE 802.1ad) &amp; Shortest Path Bridging IEEE 802.1aq (0x88A8)vlan - VLAN-tagged frame (IEEE 802.1Q) and Shortest Path Bridging IEEE 802.1aq with NNI compatibility (0x8100) |
| **filter-stream** (*yes \| no*；預設值：**yes**) | 發往嗅探器伺服器的嗅探封包將被忽略。 |
| **filter-size** (*integer[-integer]:0..65535*；預設值：) | 按指定大小或大小範圍（位元組）過濾封包。 |
| **filter-direction**(*any \| rx \| tx*；預設值：) | 指定將應用過濾的方向。 |
| **filter-interface** (*all \| name*；預設值：**all**) | 嗅探器執行所在的介面名稱。**all** 表示嗅探器將在所有介面上嗅探封包。 |
| **filter-operator-between-entries** (*and \| or*；預設值：**or**) | 更改具有多個條目的過濾器邏輯。 |
| **filter-vlan** (*integer[,integer]:0..4095*；預設值：) | 最多 16 個用作過濾器的 VLAN ID。 |
| **memory-limit**(*integer 10..4294967295[KiB]*；預設值：**100KiB**) | 用於儲存嗅探資料的記憶體大小。 |
| **memory-scroll** (*yes \| no*；預設值：**yes**) | 達到記憶體限制時是否覆蓋較舊的嗅探資料。 |
| **only-headers**(*yes \| no*；預設值：**no**) | 僅在記憶體中儲存封包的頭部，而不是整個封包。 |
| **show-frame (*yes \| no*；預設值：no)** | 在命令列中執行快速嗅探器時是否檢視幀內容。 |
| **streaming-enabled** (*yes \| no*；預設值：**no**) | 定義是否將嗅探到的封包傳送到流伺服器。 |
| **streaming-server** (*IP*；預設值：**0.0.0.0**) | Tazmen Sniffer Protocol (TZSP) 流接收器。 |
| **streaming-port** (*port*；預設值：**37008** ) | 將 TZSP 封包流式傳輸到的埠。 |

:::danger
`file-size` 限制不應配置為超過可用空閒記憶體！
:::

### 封包嗅探器快速模式 {#packet-sniffer-quick-mode}

快速模式會在封包被過濾出來時顯示結果，並使用大小受限的封包緩衝區。可以為過濾設定多個屬性。如果未設定任何屬性，則將使用當前配置。

```ros
[admin@MikroTik] > /tool/sniffer/quick ip-protocol=icmp
Columns: INTERFace, TIME, NUm, DIr, SRC-MAC, DST-MAC, SRC-ADDRESS, DST-ADDRESS, PROTOCOl, SIze, Cpu, FP
INTERF  TIME    NU  DI  SRC-MAC            DST-MAC            SRC-ADDRESS     DST-ADDRESS     PROTOCO  SI  C  FP
ether7  35.472  79  <-  6C:3B:6B:ED:83:69  6C:3B:6B:ED:81:83  10.155.126.252  10.155.126.253  ip:icmp  70  7  no
ether7  35.472  80  ->  6C:3B:6B:ED:81:83  6C:3B:6B:ED:83:69  10.155.126.253  10.155.126.252  ip:icmp  70  7  no
ether1  35.595  81  <-  6C:3B:6B:ED:83:63  6C:3B:6B:ED:81:7D  172.24.24.2     172.24.24.1     ip:icmp  70  4  no
ether1  35.595  82  ->  6C:3B:6B:ED:81:7D  6C:3B:6B:ED:83:63  172.24.24.1     172.24.24.2     ip:icmp  70  4  no
ether7  36.457  83  <-  6C:3B:6B:ED:83:69  6C:3B:6B:ED:81:83  10.155.126.252  10.155.126.253  ip:icmp  70  7  no
ether7  36.457  84  ->  6C:3B:6B:ED:81:83  6C:3B:6B:ED:83:69  10.155.126.253  10.155.126.252  ip:icmp  70  7  no
ether1  36.6    85  <-  6C:3B:6B:ED:83:63  6C:3B:6B:ED:81:7D  172.24.24.2     172.24.24.1     ip:icmp  70  4  no
ether1  36.6    86  ->  6C:3B:6B:ED:81:7D  6C:3B:6B:ED:83:63  172.24.24.1     172.24.24.2     ip:icmp  70  4  no
```

:::warning
除非設定了 *fast-path* 引數，否則在同一介面上使用封包嗅探器時，Traffic-Generator 封包將不可見。
:::

### 封包嗅探器協定 {#packet-sniffer-protocols}

在此子選單中，可以檢視所有嗅探到的協定及其在總嗅探量中的佔比。

```ros
[admin@MikroTik] /tool/sniffer/protocol> print 
 # PROTOCOL IP-PROTOCOL PORT                                     PACKETS      BYTES        SHARE
 0 802.2                                                              1         60        0.05%
 1 ip                                                               215     100377       99.04%
 2 arp                                                                2        120        0.11%
 3 ipv6                                                               6        788        0.77%
 4 ip       tcp                                                     210      99981       98.65%
 5 ip       udp                                                       3        228        0.22%
 6 ip       ospf                                                      2        168        0.16%
 7 ip       tcp         8291 (winbox)                               210      99981       98.65%
 8 ip       tcp         36771                                       210      99981       98.65%
 9 ip       udp         646                                           3        228        0.22%
```

### 封包嗅探器主機 {#packet-sniffer-host}

該子選單顯示參與了你所嗅探的資料交換的主機列表。

```ros
[admin@MikroTik] /tool/sniffer/host> print 
 # ADDRESS         RATE                PEEK-RATE           TOTAL            
 0 10.5.101.3      0bps/0bps           0bps/720bps         0/90             
 1 10.5.101.10     0bps/0bps           175.0kbps/19.7kbps  61231/7011       
 2 10.5.101.13     0bps/0bps           0bps/608bps         0/76             
 3 10.5.101.14     0bps/0bps           0bps/976bps         0/212            
 4 10.5.101.15     0bps/0bps           19.7kbps/175.0kbps  7011/61231       
 5 224.0.0.2       0bps/0bps           608bps/0bps         76/0             
 6 224.0.0.5       0bps/0bps           1440bps/0bps        302/0 
```

### 封包嗅探器連線 {#packet-sniffer-connections}

在這裡可以獲取在嗅探期間監視到的連線列表。

```ros
[admin@MikroTik] /tool/sniffer/connection> print
Flags: A - active
  #   SRC-ADDRESS       DST-ADDRESS             BYTES     RESENDS   MSS
  0 A 10.0.0.241:1839   10.0.0.181:23 (telnet)  6/42      60/0      0/0
  1 A 10.0.0.144:2265   10.0.0.181:22 (ssh)     504/252   504/0     0/0
```
