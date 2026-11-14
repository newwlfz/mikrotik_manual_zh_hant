---
sidebar_key: "system-information-and-utilities/services"
sidebar_position: 15
title: "服務"
sidebar_label: "服務"
description: "本頁面介紹 MikroTik RouterOS 中的 IP/Services 部分，詳細說明 Telnet、FTP、SSH 和 WinBox 等預設服務及其配置屬性，例如地址限制、埠、TLS 版本和會話限制。文中還提供了用於管理服務訪問控制的示例。"
tags:
  - 'ip-services'
  - 'firewall'
source: https://manual.mikrotik.com/docs/7.24/system-information-and-utilities/services
captured_at: '2026-11-04T11:33:46+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

IP/Services 列出了各種 MikroTik RouterOS 服務和容器所使用的協定和埠，包括用於傳入連線的那些。

它有助於確定哪些 MikroTik 服務（或容器）正在監聽特定埠，以及如果你想要限制或允許訪問某些服務，需要阻止或允許什麼。

可以從 IP/Services 部分配置的預設服務：

| 屬性 | 描述 |
| :-- | :-- |
| **telnet** | Telnet 服務 |
| **ftp** | FTP 服務 |
| **www** | WebFig HTTP 服務 |
| **ssh** | SSH 服務 |
| **www-ssl** | WebFig HTTPS 服務 |
| **api** | API 服務 |
| **winbox** | 負責 WinBox 工具訪問，以及 MikroTik 智慧手機應用和 Dude |
| **api-ssl** | 基於 SSL 的 API 服務 |
| **reverse-proxy** | 反向代理服務 |

## 屬性 {#properties}

請注意，無法新增新服務，只允許修改現有服務。

**子選單：** `/ip/service`

| 屬性 | 描述 |
| :-- | :-- |
| **address** (*IP address/netmask \| IPv6/0..128*; 預設值： ) | 服務可訪問的 IP/IPv6 字首列表。設定此引數後，封包不會在網路層被丟棄，但來自與指定地址不匹配的源的訪問將被拒絕。此選項最適合用於限制受信任網路內的訪問。  要阻止來自外部或不受信任網路的訪問，我們建議改用防火牆。 |
| **certificate** (*name*; 預設值：**none**) | 特定服務所使用的證書名稱。僅適用於依賴證書的服務（*www-ssl、api-ssl*） |
| **name** (*name*; 預設值：**none**) | 服務名稱 |
| **max-sessions**(*integer: 1..1000*; 預設值：20) | 服務的最大併發會話數 |
| **port** (*integer: 1..65535*; 預設值： ) | 特定服務監聽的埠 |
| ***tls-version*** (*any* \| *only-1.2*; 預設值：**any**) | 指定特定服務允許的 TLS 版本 |
| **vrf** (*name*; 預設值：**main**) | 指定特定服務要使用的 VRF 例項 |

### 只讀屬性 {#read-only-properties}

| 屬性 | 描述 |
| :-- | :-- |
| **Container** | 監聽該埠的容器名稱 |
| **Local** | 用於該連線的路由器本地地址 |
| **Remote** | 建立到該服務連線的遠端地址 |

### 示例 {#example}

例如，僅允許從特定 IP/IPv6 地址範圍訪問 API

```ros
[admin@dzeltenais_burkaans] /ip/service/set api address=10.5.101.0/24,2001:db8:fade::/64
[admin@dzeltenais_burkaans] /ip/service/print where !dynamic      
Flags: X - DISABLED, I - INVALID
Columns: NAME, PORT, PROTO, ADDRESS, CERTIFICATE, VRF, MAX-SESSIONS
 #   NAME     PORT  PROTO  ADDRESS             CERTIFICATE  VRF   MAX-SESSIONS
 0   ftp        21  tcp                                     main            20
 1   ssh        22  tcp                                     main            20
 2   telnet     23  tcp                                     main            20
 7   www        80  tcp                                     main            20
 9 X www-ssl   443  tcp                        none         main            20
13   winbox   8291  tcp                                     main            20
15   api      8728  tcp    10.5.101.0/24                    main            20
                           2001:db8:fade::/64                                 
16   api-ssl  8729  tcp                        none         main            20
```

以下示例展示了正在監聽或已建立到路由器服務連線的動態服務

```routeros
[admin@dzeltenais_burkaans] /ip/service/print where dynamic  
Flags: D - DYNAMIC; c - CONNECTION
Columns: NAME, NETNS, CONTAINER, PORT, PROTO, LOCAL, REMOTE
 #    NAME        NETNS  CONTAINER  PORT  PROTO  LOCAL         REMOTE            
 3 D  resolver                        53  tcp                                    
 4 D  resolver                        53  udp                                    
 5 D  dhcp                            67  udp                                    
 6 D  dhcpclient                      68  udp                                    
 8 D  snmp                           161  udp                                    
10 D  btest                         2000  tcp                                    
11 D  loader                        3986  tcp                                    
12 D  discover                      5678  udp                                    
14 Dc winbox                        8291  tcp    10.155.221.4  10.145.221.15:51595
17 D  pihole-FTL     16  Pi-hole      53  tcp                                    
18 D  pihole-FTL     16  Pi-hole      53  udp                                    
19 D  lighttpd       16  Pi-hole      80  tcp                                    
28 Dc lighttpd       16  Pi-hole      80  tcp    172.55.1.2    10.145.221.15:52298
29 Dc lighttpd       16  Pi-hole      80  tcp    172.55.1.2    10.145.221.15:52333
30 Dc lighttpd       16  Pi-hole      80  tcp    172.55.1.2    10.145.221.15:52339
31 Dc lighttpd       16  Pi-hole      80  tcp    172.55.1.2    10.145.221.15:52340
32 Dc lighttpd       16  Pi-hole      80  tcp    172.55.1.2    10.145.221.15:52341
33 Dc lighttpd       16  Pi-hole      80  tcp    172.55.1.2    10.145.221.15:52342
26 D  pihole-FTL     16  Pi-hole    4711  tcp
```

## 協定和埠 {#protocols-and-ports}

下表列出了 RouterOS 使用的協定和埠。

| 協定/埠 | 描述 |
| :-- | :-- |
| **20/tcp** | FTP 資料連線 |
| **21/tcp** | FTP 控制連線 |
| **22/tcp** | Secure Shell (SSH) 遠端登入協定 |
| **23/tcp** | Telnet 協定 |
| <strong>53/tcp 53/udp</strong> | DNS |
| **67/udp** | Bootstrap protocol 或 [DHCP Server](../network-management/dhcp.md#dhcp-server) |
| **68/udp** | Bootstrap protocol 或 [DHCP Client](../network-management/dhcp.md#dhcp-client) |
| <strong>80/tcp</strong> | 全球資訊網 HTTP |
| <strong>123/udp</strong> | 網路時間協定（[NTP](./ntp.md) |
| <strong>161/udp</strong> | 簡單網路管理協定（[SNMP](../diagnostics-monitoring-and-troubleshooting/snmp.md) |
| <strong>179/tcp</strong> | 邊界閘道器協定（[BGP](../user-guides/routing-and-networking-protocols/unicast/bgp/index.md) |
| **443/tcp** | Secure Socket Layer (SSL) 加密 HTTP |
| **500/udp** | Internet Key Exchange (IKE) 協定 |
| **520/udp 521/udp** | [RIP](../user-guides/routing-and-networking-protocols/unicast/rip.md) 路由協定 |
| **546/udp** | [DHCPv6 Client](../network-management/dhcp.md) 訊息 |
| **547/udp** | [DHCPv6 Server](../network-management/dhcp.md) 訊息 |
| **646/tcp** | [LDP](../user-guides/routing-and-networking-protocols/mpls/ldp.md) 傳輸會話 |
| **646/udp** | [LDP](../user-guides/routing-and-networking-protocols/mpls/ldp.md) hello 協定 |
| **1080/tcp** | [SOCKS](../network-management/socks/index.md) 代理協定 |
| **1698/udp 1699/udp** | RSVP TE 隧道 |
| <strong>1701/udp</strong> | 二層隧道協定（[L2TP](../virtual-private-networks/l2tp/index.md)） |
| <strong>1723/tcp</strong> | 點對點隧道協定（[PPTP](../virtual-private-networks/pptp.md)） |
| <strong>1900/udp 2828/tcp</strong> | 通用即插即用（[uPnP](../firewall-and-quality-of-service/upnp.md)） |
| **1966/udp** | MME 發起方訊息流量 |
| **1966/tcp** | MME 閘道器協定 |
| **2000/tcp** | 頻寬測試伺服器 |
| <strong>5246,5247/udp</strong> | [CAPsMAN](../wireless/abgn/capsman/ap-controller-capsman.md) |
| **5350/udp** | NAT-PMP 用戶端 |
| **5351/udp** | NAT-PMP 伺服器 |
| <strong>5678/udp</strong> | Mikrotik 鄰居發現協定 |
| **6343/tcp** | 預設 OpenFlow 埠 |
| **8080/tcp** | HTTP Web 代理 |
| <strong>8291/tcp</strong> | [Winbox](../management-tools/winbox.md) |
| <strong>8728/tcp</strong> | [API](../developer-guides/api/index.md) |
| <strong>8729/tcp</strong> | API-SSL |
| <strong>20561/udp</strong> | MAC winbox |
| **/1** | ICMP |
| **/2** | [IGMP 代理](../user-guides/routing-and-networking-protocols/multicast/igmp-proxy.md) |
| **/4** | [IPIP](../virtual-private-networks/ipip.md) 封裝 |
| **/41** | IPv6（封裝） |
| **/46** | RSVP TE 隧道 |
| **/47** | General Routing Encapsulation (GRE) - 用於 PPTP 和 [EoIP](../virtual-private-networks/eoip.md) 隧道 |
| <strong>/50</strong> | 用於 IPv4 的封裝安全載荷 (ESP) |
| <strong>/51</strong> | 用於 IPv4 的認證頭 (AH) |
| **/89** | [OSPF](../user-guides/routing-and-networking-protocols/unicast/ospf/index.md) 路由協定 |
| **/103** | [PIM-SM](../user-guides/routing-and-networking-protocols/multicast/pim-sm.md) |
| **/112** | [VRRP](../high-availability-solutions/vrrp.md) |

## Web 伺服器 {#web-server}

下表列出了可為 Web 服務啟用/停用的屬性。所有屬性預設均已啟用，如有需要可以停用。

在此表中，“plain”指 HTTP 連線，“secure”指 HTTPS 連線。

| 屬性 | 描述 |
| :-- | :-- |
| index-plain: (預設值：**yes**) | 主頁/登入頁（當 webfig-plain 和 graphs-plain 被停用時，可以停用此屬性） |
| webfig-plain: (預設值：**yes**) | WebFig 介面 |
| graphs-plain: (預設值：**yes**) | 圖表頁面 |
| rest-plain: (預設值：**yes**) | REST API 支援 |
| crl-plain: (預設值：**yes**) | CRL（證書吊銷列表） |
| scep-plain: (預設值：**yes**) | SCEP（Simple Certificate Enrollment Protocol） |
| acme-plain: (預設值：**yes**) | ACME 挑戰 |
| index-secure: (預設值：**yes**) | 主頁/登入頁（當 webfig-secure 和 graphs-secure 被停用時，可以停用此屬性） |
| webfig-secure: (預設值：**yes**) | WebFig 介面 |
| graphs-secure: (預設值：**yes**) | 圖表頁面 |
| rest-secure: (預設值：**yes**) | REST API 支援 |
