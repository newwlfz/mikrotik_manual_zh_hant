---
sidebar_key: "system-information-and-utilities/services"
sidebar_position: 14
title: "服務"
sidebar_label: "服務"
description: "`/ip/service` 選單列出了 RouterOS 的管理服務（WinBox、SSH、Telnet、FTP、Web 伺服器、API）以及其他功能和容器所監聽的埠。本頁面介紹瞭如何檢視路由器所監聽的埠、將服務限制到受信任的地址、將服務遷移到管理 VRF，並列出了 RouterOS 所使用的埠和 IP 協定。"
tags:
  - 'ip-services'
  - 'firewall'
source: https://manual.mikrotik.com/docs/system-information-and-utilities/services
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

`/ip/service` 選單列出了路由器為管理和訪問提供的服務：WinBox、SSH、Telnet、FTP、Web 伺服器、API 和反向代理。每個服務都有一個埠、它接受用戶端連線的地址和 VRF，對於 TLS 服務，還有一個證書。你不能新增服務，只能更改、停用和啟用現有服務。

同一選單還會顯示動態條目：其他功能和容器正在監聽的埠，以及路由器服務當前開啟的連線。使用該列表可以檢視路由器上哪些埠處於開放狀態，以及防火牆必須允許或阻止哪些流量。

有關應停用哪些服務、如何更改 SSH 埠以及如何使用防火牆保護管理訪問的建議，請參見[保護路由器安全](../getting-started/securing-your-router.md#management-service-ports)。

| 服務 | 預設埠 | 用途 |
| :-- | :-- | :-- |
| `ftp` | 21 | 與路由器儲存之間進行 FTP 檔案傳輸 |
| `ssh` | 22 | SSH 訪問 |
| `telnet` | 23 | Telnet 訪問 |
| `www` | 80 | 透過 HTTP 提供 Web 伺服器：WebFig、REST API 和圖表 |
| `www-ssl` | 443 | 透過 HTTPS 提供 Web 伺服器；需要證書，參見[啟用 HTTPS](../management-tools/webfig.md#enable-https) |
| `winbox` | 8291 | [WinBox](../management-tools/winbox.md)、MikroTik 移動應用和 The Dude |
| `api` | 8728 | [API](../developer-guides/api/index.md) |
| `api-ssl` | 8729 | 基於 TLS 的 API |
| `reverse-proxy` | 443 | [反向代理](../network-management/proxy/reverse-proxy.md)；僅當至少存在一條已啟用的規則時才監聽 |

## 檢視路由器監聽的埠 {#see-what-the-router-listens-on}

動態條目會顯示 RouterOS 功能和容器正在監聽的埠，以及到路由器服務的開放連線：

```ros
/ip/service/print where dynamic
```

```text
Flags: D - DYNAMIC; c - CONNECTION
Columns: NAME, PORT, PROTO, LOCAL, REMOTE
#    NAME       PORT  PROTO  LOCAL          REMOTE
3 Dc ssh          22  tcp    192.168.88.1   192.168.88.10:53163
4 D  resolver     53  tcp
5 D  resolver     53  udp
0 D  btest      2000  tcp
1 D  discover   5678  udp
2 D  cloud     54103  udp
```

- 僅帶有 `D` 標誌的條目是功能正在監聽的埠。`NAME` 是功能或程式，例如 `resolver` 表示 DNS 伺服器，`btest` 表示[頻寬測試](../diagnostics-monitoring-and-troubleshooting/bandwidth-test.md)伺服器，`discover` 表示[鄰居發現](./neighbor-discovery.md)，`cloud` 表示 [MikroTik 雲](../network-management/cloud/communication-mikrotik-cloud-servers.md)服務用來與雲伺服器通訊的本地埠。
- 帶有 `c` 標誌的條目是到某個服務的開放連線。`LOCAL` 是路由器的地址，`REMOTE` 是用戶端的地址和埠。
- 容器正在監聽的埠還會顯示 `NETNS` 和 `CONTAINER` 列：網路名稱空間和容器的名稱。

當某個功能開始監聽時，就會出現一個條目。例如，當你在 [`/ip/dns`](../network-management/dns.md) 中設定 `allow-remote-requests=yes` 時，埠 53 上的 `resolver` 條目就會出現。路由器會在動態條目的埠以及已啟用服務的埠（`/ip/service/print` 中沒有 `X` 標誌的條目）上接受連線。沒有埠的 IP 協定（例如 GRE 或 OSPF）不在該列表中；本頁末尾的表格列出了它們。功能等待用戶端的埠（例如 `resolver` 或 `btest`）就是防火牆 input 鏈必須為需要它們的用戶端放行、並對其他所有用戶端阻止的埠；預設防火牆已經會丟棄從網際網路到這些埠的連線。你無法在 `/ip/service` 中更改動態條目；請改為在其各自的選單中更改或停用相應功能。

## 限制誰可以使用服務 {#limit-who-can-use-a-service}

要僅接受來自 LAN 和 VPN 用戶端的 WinBox 和 SSH 連線：

```ros
/ip/service/set winbox,ssh available-from=192.168.88.0/24,10.8.0.0/24
/ip/service/print proplist=name,port,available-from where !dynamic
```

```text
Flags: X - DISABLED, I - INVALID
Columns: NAME, PORT, AVAILABLE-FROM
 #   NAME           PORT  AVAILABLE-FROM
 6   ftp              21
 7   ssh              22  192.168.88.0/24
                          10.8.0.0/24
 8   telnet           23
 9   www              80
10 X www-ssl         443
11   reverse-proxy   443
12   winbox         8291  192.168.88.0/24
                          10.8.0.0/24
13   api            8728
14   api-ssl        8729
```

`available-from` 接受一組 IPv4 和 IPv6 字首，例如 `10.5.101.0/24,2001:db8:fade::/64`。空列表表示任意地址。僅包含 IPv4 字首的列表會拒絕所有 IPv6 用戶端；請新增需要訪問的 IPv6 字首。

:::warning
請包含你管理路由器時所使用的地址。更改後，路由器會拒絕來自其他地址的新連線；如果你下一次登入來自列表之外的地址，也會被拒絕。
:::

來自其他地址的用戶端仍然可以開啟 TCP 連線，隨後路由器會在不向該用戶端提供服務的情況下關閉它，因此埠掃描仍會發現該埠處於開放狀態。`available-from` 適合在可信網路內限制訪問。要阻止來自網際網路和其他不可信網路的訪問，請在防火牆 input 鏈中丟棄流量，如[保護路由器安全](../getting-started/securing-your-router.md#securing-access-to-the-device)中所述。

## 在 VRF 中執行管理服務 {#run-management-services-in-a-vrf}

管理 VRF 會將管理訪問與路由器所服務的網路隔離開。要使 WinBox 和 SSH 僅透過專用管理埠 `ether5` 可用，該埠具有管理地址（例如 10.99.0.1/24）：

```ros
/ip/vrf/add name=mgmt interfaces=ether5
/ip/service/set winbox,ssh vrf=mgmt
```

服務只會在其 VRF 中監聽。進行此更改後，路由器會拒絕透過主路由表中的地址發起的 WinBox 和 SSH 連線，並且僅透過 `ether5` 提供這些連線。有關 VRF 的更多資訊，請參見 [VRF](../user-guides/routing-and-networking-protocols/vrf.md)。

:::warning
進行此更改後，WinBox 和 SSH 只能透過該 VRF 的介面訪問。透過其他介面進入的會話，或在 `ether5` 加入該 VRF 之前透過它進入的會話，都會被切斷。請同時執行這兩條命令，再次透過 `ether5` 連線，並保留另一種進入方式，例如 MAC WinBox。
:::

## 在 WinBox 中管理服務 {#manage-services-in-winbox}

開啟 **IP > Services**。該列表還可能顯示動態監聽器和活動連線；請開啟可配置的服務行（例如 `winbox`），而不是動態連線條目。使用 **Find** 按名稱查詢服務。

1. 在服務對話方塊中檢查 **Port**。更改它會改變用戶端連線時必須使用的埠。
2. 使用 **Available From** 旁的 **+** 控制元件輸入應具有訪問許可權的用戶端地址或子網，然後選擇 **OK**。在限制你當前連線所使用的服務之前，請包含你的管理計算機的地址。空列表不會限制用戶端地址。

![WinBox IP Service dialog for the winbox service](/img/a78155bbd65df0ef.webp)

要在不更改埠的情況下關閉未使用的服務，請在 Services 列表中選擇其行，然後選擇 **Disable**。選擇 **Enable** 可再次啟用它。

## Web 伺服器 {#web-server}

Web 伺服器為其各個部分提供了單獨的設定：主頁、WebFig、圖表、REST API 以及 CRL、SCEP 和 ACME 端點。`-plain` 設定控制 HTTP 連線（`www` 服務），`-secure` 設定控制 HTTPS 連線（`www-ssl` 服務）。所有部分預設啟用。有關這些設定，請參見 [`/ip/service/webserver` CLI 參考](../cli-reference/ip/service/webserver.md)。

## 協定和埠 {#protocols-and-ports}

以下表格列出了 RouterOS 使用的埠和 IP 協定。大多數埠是功能啟用時路由器監聽的埠。有些是用戶端埠：DHCP 用戶端在 UDP 埠 68 上接收回復，DHCPv6 用戶端在 UDP 埠 546 上接收回復。FTP 伺服器不監聽 TCP 埠 20：在主動模式下，其資料連線從該埠發出。對於 [OpenFlow](../network-management/openflow.md)，路由器會連線到控制器，其地址和埠由 `/openflow` 中的 `controllers` 設定，例如 TCP 埠 6653，並且不監聽埠。

### TCP 埠 {#tcp-ports}

| 埠 | 使用者 |
| :-- | :-- |
| 21 | FTP（`ftp` 服務） |
| 22 | SSH（`ssh` 服務） |
| 23 | Telnet（`telnet` 服務） |
| 53 | [DNS](../network-management/dns.md) 伺服器，當 `allow-remote-requests=yes` 時 |
| 80 | HTTP（`www` 服務） |
| 179 | [BGP](../user-guides/routing-and-networking-protocols/unicast/bgp/index.md) |
| 443 | HTTPS（`www-ssl` 服務）和[反向代理](../network-management/proxy/reverse-proxy.md)（`reverse-proxy` 服務） |
| 646 | [LDP](../user-guides/routing-and-networking-protocols/mpls/ldp.md) 傳輸會話 |
| 1080 | [SOCKS](../network-management/socks/index.md) 代理 |
| 1194 | [OpenVPN](../virtual-private-networks/openvpn.md) 伺服器 |
| 1723 | [PPTP](../virtual-private-networks/pptp.md) 伺服器 |
| 2000 | [頻寬測試](../diagnostics-monitoring-and-troubleshooting/bandwidth-test.md)伺服器 |
| 2828 | [UPnP](../firewall-and-quality-of-service/upnp.md) 控制，位於內部介面上 |
| 5246 | [CAPsMAN](../wireless/wifi/capsman.md)（用於 WiFi） |
| 8080 | [Web 代理](../network-management/proxy/web-proxy.md)，預設埠 |
| 8291 | [WinBox](../management-tools/winbox.md)（`winbox` 服務） |
| 8728 | [API](../developer-guides/api/index.md)（`api` 服務） |
| 8729 | 基於 TLS 的 API（`api-ssl` 服務） |

### UDP 埠 {#udp-ports}

| 埠 | 使用者 |
| :-- | :-- |
| 53 | [DNS](../network-management/dns.md) 伺服器，當 `allow-remote-requests=yes` 時 |
| 67 | [DHCP 伺服器](../network-management/dhcp/server.md) |
| 68 | [DHCP 用戶端](../network-management/dhcp/client.md)（用戶端埠） |
| 69 | [TFTP](./tftp.md) 伺服器 |
| 123 | [NTP](./ntp.md) 伺服器 |
| 161 | [SNMP](../diagnostics-monitoring-and-troubleshooting/snmp.md) |
| 500 | 用於 [IPsec](../virtual-private-networks/ipsec/index.md) 的 IKE |
| 520 | [RIP](../user-guides/routing-and-networking-protocols/unicast/rip.md) |
| 521 | RIPng |
| 546 | [DHCPv6 用戶端](../network-management/dhcp/dhcpv6-client.md)（用戶端埠） |
| 547 | [DHCPv6 伺服器](../network-management/dhcp/dhcpv6-server.md) |
| 646 | [LDP](../user-guides/routing-and-networking-protocols/mpls/ldp.md) hello 訊息 |
| 1701 | [L2TP](../virtual-private-networks/l2tp/index.md) |
| 1900 | [UPnP](../firewall-and-quality-of-service/upnp.md) 發現（SSDP），位於內部介面上 |
| 3799 | [RADIUS](../authentication-authorization-accounting/radius.md) 傳入請求（CoA 和 disconnect） |
| 4500 | IPsec NAT 穿透 |
| 5246 | CAPsMAN 控制，用於 [WiFi](../wireless/wifi/capsman.md) 和[傳統無線](../wireless/abgn/capsman/ap-controller-capsman.md) |
| 5247 | CAPsMAN 資料，用於傳統無線 |
| 5350 | [NAT-PMP](../firewall-and-quality-of-service/nat-pmp.md) 通告，路由器將其傳送到 224.0.0.1 上的用戶端 |
| 5351 | [NAT-PMP](../firewall-and-quality-of-service/nat-pmp.md) 伺服器 |
| 5678 | MikroTik 鄰居發現協定（[MNDP](./neighbor-discovery.md)） |
| 20561 | MAC Telnet、MAC WinBox 和 MAC ping（[MAC 伺服器](../management-tools/mac-server.md)） |
| `listen-port` | [WireGuard](../virtual-private-networks/wireguard.md)：在每個介面上設定的埠 |

:::note
MAC Telnet、MAC WinBox 和 MAC ping 在第 2 層工作：封包被定址到路由器的 MAC 地址，並攜帶 IP 地址 0.0.0.0 和 255.255.255.255。IP 防火牆不會阻止它們：即使某條過濾規則丟棄了 UDP 埠 20561，MAC 伺服器仍會響應。要限制 MAC 訪問，請在 [`/tool/mac-server`](../management-tools/mac-server.md) 中設定 `allowed-interface-list`。
:::

### IP 協定 {#ip-protocols}

| 協定 | 使用者 |
| :-- | :-- |
| 1 | ICMP |
| 2 | IGMP（[IGMP 代理](../user-guides/routing-and-networking-protocols/multicast/igmp-proxy.md)） |
| 4 | [IPIP](../virtual-private-networks/ipip.md) 隧道 |
| 41 | IPv6 封裝（[6to4](../virtual-private-networks/6to4.md)） |
| 46 | 用於 [MPLS 流量工程](../user-guides/routing-and-networking-protocols/mpls/traffic-eng.md) 的 RSVP |
| 47 | GRE：[PPTP](../virtual-private-networks/pptp.md)、[EoIP](../virtual-private-networks/eoip.md) 和 [GRE](../virtual-private-networks/gre.md) 隧道 |
| 50 | 用於 [IPsec](../virtual-private-networks/ipsec/index.md) 的 ESP |
| 51 | 用於 IPsec 的 AH |
| 58 | ICMPv6，包括 IPv6 鄰居發現 |
| 89 | [OSPF](../user-guides/routing-and-networking-protocols/unicast/ospf/index.md) |
| 103 | PIM（[PIM-SM](../user-guides/routing-and-networking-protocols/multicast/pim-sm.md)） |
| 112 | [VRRP](../high-availability-solutions/vrrp.md) |

有關所有屬性，請參見 CLI 參考中的 [`/ip/service`](../cli-reference/ip/service/index.md) 和 [`/ip/service/webserver`](../cli-reference/ip/service/webserver.md)。
