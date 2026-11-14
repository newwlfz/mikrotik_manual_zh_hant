---
sidebar_key: "network-management/dhcp/relay"
sidebar_position: 3
title: "DHCP 中繼"
sidebar_label: "DHCP 中繼"
description: "DHCP 中繼將來自用戶端的 DHCP 和 DHCPv6 請求轉發到另一個網路中的 DHCP 伺服器，並可選提供中繼代理資訊（option 82）以及 VRF 支援。"
tags:
  - 'dhcp'
  - 'dhcpv6'
source: https://manual.mikrotik.com/docs/network-management/dhcp/relay
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

DHCP 中繼會把一個網路中 DHCP 用戶端的請求轉發到另一個網路中的 DHCP 伺服器，並把回覆送回用戶端。當一臺集中式 DHCP 伺服器為多個與其沒有直接連線的網路提供服務時，可使用它。關於中繼和 DHCP 伺服器如何協同工作，請參見 [DHCP 概念](./index.md)。

## DHCPv4 中繼 {#dhcpv4-relay}

**子選單：** `/ip/dhcp-relay`

DHCP 中繼會在其介面上監聽 DHCP 請求，並把每個請求轉發給 `dhcp-server` 中列出的每一臺 DHCP 伺服器；它不會從中選擇一臺。它會把 `local-address`（未設定 `local-address` 時則為其介面的一個地址）寫入所轉發請求的閘道器地址欄位（`giaddr`）。DHCP 伺服器會把回覆傳送到該地址，並用它來區分中繼：請把伺服器的 `relay` 屬性設定為中繼的地址，如下例所示。新建中繼預設處於停用狀態，因此新增後請啟用它們。

所有中繼屬性都在 [`/ip/dhcp-relay`](../../cli-reference/ip/dhcp-relay/index.md) CLI 參考中說明。

### 中繼代理資訊（option 82） {#relay-agent-information-option-82}

當 `add-relay-info=yes` 時，中繼會把中繼代理資訊選項（option 82）新增到它轉發的請求中。電路 ID 是請求進入的中繼介面的 MAC 地址，遠端 ID 是用戶端的 MAC 地址，或 `relay-info-remote-id` 中設定的文字。

RouterOS DHCP 伺服器會在租約中顯示這些值（`active-agent-circuit-id`、`active-agent-remote-id`），並將它們傳遞給租約指令碼。靜態租約可以用這些值（`agent-circuit-id`、`agent-remote-id`）來匹配用戶端，即使用戶端的 MAC 地址不同；當 `dynamic-lease-identifiers=opt-82` 時，伺服器僅透過 option 82 識別用戶端。

### 配置示例 {#configuration-example}

在此示例中，一臺路由器 DHCP-Server 為兩個網路 192.168.1.0/24 和 192.168.2.0/24 分配地址，這兩個網路位於另一臺路由器 DHCP-Relay 之後。

![DHCP-Server (public 10.1.0.2, local 192.168.0.1) connected to DHCP-Relay (192.168.0.2), which serves 192.168.1.0/24 on Local1 (192.168.1.1) and 192.168.2.0/24 on Local2 (192.168.2.1)](/img/84cd8b761999e3b8.webp)

這些路由器具有以下地址。在 DHCP-Server 上：

```ros
/ip/address/add address=192.168.0.1/24 interface=To-DHCP-Relay
/ip/address/add address=10.1.0.2/24 interface=Public
```

在 DHCP-Relay 上：

```ros
/ip/address/add address=192.168.0.2/24 interface=To-DHCP-Server
/ip/address/add address=192.168.1.1/24 interface=Local1
/ip/address/add address=192.168.2.1/24 interface=Local2
```

#### DHCP 伺服器設定 {#dhcp-server-setup}

在 DHCP-Server 上，為每個被中繼的網路新增一個池、一個 DHCP 伺服器和一個網路。兩個伺服器都執行在朝向中繼的介面上；`relay` 屬性使每個伺服器只應答從其網路（由該網路中中繼的地址標識）中繼來的請求：

```ros
/ip/pool/add name=Local1-Pool ranges=192.168.1.11-192.168.1.100
/ip/pool/add name=Local2-Pool ranges=192.168.2.11-192.168.2.100
/ip/dhcp-server/add interface=To-DHCP-Relay relay=192.168.1.1 address-pool=Local1-Pool name=DHCP-1
/ip/dhcp-server/add interface=To-DHCP-Relay relay=192.168.2.1 address-pool=Local2-Pool name=DHCP-2
/ip/dhcp-server/network/add address=192.168.1.0/24 gateway=192.168.1.1 dns-server=159.148.60.20
/ip/dhcp-server/network/add address=192.168.2.0/24 gateway=192.168.2.1 dns-server=159.148.60.20
```

DHCP 伺服器不需要到用戶端網路的路由：它會把回覆（包括髮給續租用戶端的回覆）傳送回請求來源的路由器。

#### DHCP 中繼設定 {#dhcp-relay-setup}

在 DHCP-Relay 上，在每個本地介面上新增一箇中繼。新建中繼預設處於停用狀態，因此請使用 `disabled=no` 新增它們：

```ros
/ip/dhcp-relay/add name=Local1-Relay interface=Local1 dhcp-server=192.168.0.1 local-address=192.168.1.1 disabled=no
/ip/dhcp-relay/add name=Local2-Relay interface=Local2 dhcp-server=192.168.0.1 local-address=192.168.2.1 disabled=no
```

使用 `/ip/dhcp-relay/monitor` 檢視某個中繼轉發了多少請求以及送達了多少回覆。

### 使用 VRF 的 DHCP 中繼 {#dhcp-relay-with-vrf}

當朝向 DHCP 伺服器的介面與中繼的用戶端介面位於不同 VRF 時，請將 `dhcp-server-vrf` 設定為伺服器側的 VRF。此示例沿用之前的設定，並讓 DHCP-Relay 的每個介面分別位於自己的 VRF 中：

```ros
/ip/vrf
add interfaces=To-DHCP-Server name=vrf_server
add interfaces=Local1 name=vrf1
add interfaces=Local2 name=vrf2
/ip/dhcp-relay/set [find] dhcp-server-vrf=vrf_server
```

伺服器會把回覆傳送到中繼的 `local-address`，該地址位於用戶端 VRF 中，但回覆會到達 `vrf_server` 中的伺服器側介面。請使用 dst-nat 規則將它們重定向到中繼的伺服器側地址：

```ros
/ip/firewall/nat
add action=dst-nat chain=dstnat dst-address=192.168.1.1 dst-port=67 in-interface=To-DHCP-Server protocol=udp src-address=192.168.0.1 to-addresses=192.168.0.2
add action=dst-nat chain=dstnat dst-address=192.168.2.1 dst-port=67 in-interface=To-DHCP-Server protocol=udp src-address=192.168.0.1 to-addresses=192.168.0.2
```

用戶端透過向伺服器傳送單播訊息來續租，因此這些 VRF 還需要到彼此網路的路由：

```ros
/ip/route
add dst-address=192.168.0.0/24 gateway=To-DHCP-Server@vrf_server routing-table=vrf1
add dst-address=192.168.0.0/24 gateway=To-DHCP-Server@vrf_server routing-table=vrf2
add dst-address=192.168.1.0/24 gateway=Local1@vrf1 routing-table=vrf_server
add dst-address=192.168.2.0/24 gateway=Local2@vrf2 routing-table=vrf_server
```

如果沒有 dst-nat 規則，用戶端將無法獲得地址；如果沒有這些路由，用戶端雖能獲得地址，但無法續租。

## DHCPv6 中繼 {#dhcpv6-relay}

**子選單：** `/ipv6/dhcp-relay`

DHCPv6 中繼會轉發其介面上的用戶端傳送給 `dhcp-server` 中列出的伺服器的 DHCPv6 訊息。它會把每條用戶端訊息封裝在 Relay-Forward 訊息中，該訊息還攜帶用戶端的鏈路本地地址、Interface-ID 選項，以及預設情況下用戶端的鏈路層地址（option 79，透過 `dhcp-options` 設定）。除非設定 `link-address`，否則 Relay-Forward 訊息的鏈路地址欄位為 `::`；例如，如果 DHCPv6 伺服器應透過該地址識別用戶端網路，則可將其設定為用戶端網路的一個地址。伺服器向中繼應答，中繼再把回覆傳回用戶端。這樣，一臺 DHCPv6 伺服器就能為多個網路提供服務，而無需與每個網路直接連線。

中繼在 UDP 埠 547 上接收用戶端訊息。如果路由器會過濾入站流量，請在用戶端側介面上允許 UDP 埠 547：RouterOS 的預設防火牆配置會在不屬於 `LAN` 介面列表的介面上丟棄該流量。伺服器的回覆會作為同一連線的一部分被接受。要路由用戶端的流量，路由器還需要啟用 IPv6 轉發，該功能預設已啟用。

所有中繼屬性都在 [`/ipv6/dhcp-relay`](../../cli-reference/ipv6/dhcp-relay/index.md) CLI 參考中說明。

### 通往委派字首的路由 {#routes-to-delegated-prefixes}

當中繼路由器同時是用戶端的閘道器時，它需要到委派給用戶端的字首的路由。當 `store-relayed-bindings=yes` 時，中繼會從伺服器的回覆中讀取繫結，將它們列在 `/ipv6/dhcp-relay/routes` 中，併為每個委派字首新增一條經由用戶端的路由。
