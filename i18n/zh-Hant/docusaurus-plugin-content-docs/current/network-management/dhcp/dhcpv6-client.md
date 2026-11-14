---
sidebar_key: "network-management/dhcp/dhcpv6-client"
sidebar_position: 4
title: "DHCPv6 用戶端"
sidebar_label: "DHCPv6 用戶端"
description: "RouterOS DHCPv6 用戶端從 DHCPv6 伺服器請求 IPv6 地址和委派字首（DHCPv6-PD），將收到的字首新增到 IPv6 地址池，並可在狀態變化時執行指令碼。"
tags:
  - 'dhcpv6'
  - 'ipv6'
source: https://manual.mikrotik.com/docs/network-management/dhcp/dhcpv6-client
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

**子選單：** `/ipv6/dhcp-client`

DHCPv6 用戶端從 DHCPv6 伺服器請求 IPv6 配置。它通常用於面向 ISP 的介面上，以接收用於本地網路的委派字首。`request` 屬性選擇用戶端請求的內容，一個用戶端可以請求以下多項：

- `prefix`：委派字首（DHCPv6-PD）。用戶端會將收到的字首新增到動態 IPv6 池（`pool-name`）中，你可以從該池為本地介面分配地址並向主機通告這些地址。池的生存期跟隨委派字首，並在用戶端每次續租時延長。
- `address`：一個 IPv6 地址，用戶端會將其作為動態 /128 地址新增到自己的介面上。
- `info`：僅其他設定，例如 DNS 伺服器，不包含地址或字首。

收到的 DNS 伺服器由路由器的 DNS 解析器（`use-peer-dns`）使用。DHCPv6 不提供預設閘道器，但用戶端可以透過 `add-default-route` 新增一條指向 DHCPv6 伺服器的預設路由。

用戶端使用路由器的 DUID（路由器的 DHCPv6 伺服器也會使用該 DUID）以及基於用戶端所執行介面的身份關聯識別符號（IAID）來標識自身。關於 DHCPv6 與 IPv4 的 DHCP 有何不同，請參閱 [DHCP 概念](./index.md)。

## 配置示例 {#configuration-examples}

### 簡單的 DHCPv6 用戶端 {#simple-dhcpv6-client}

本示例請求一個字首，並將其新增到一個分發 /64 字首的 IPv6 池中：

```ros
/ipv6/dhcp-client/add request=prefix pool-name=test-ipv6 pool-prefix-length=64 interface=ether13
```

當用戶端處於 bound 狀態時，會顯示收到的字首以及直到其過期的時間：

```ros
[admin@MikroTik] > /ipv6/dhcp-client/print
Columns: INTERFACE, STATUS, REQUEST, PREFIX
# INTERFACE  STATUS  REQUEST  PREFIX
0 ether13    bound   prefix   2001:db8:7501:ff04::/62, 2d23h11m53s
```

該字首也會被新增到動態池中，並帶有該字首的生存期：

```ros
[admin@MikroTik] > /ipv6/pool/print
Flags: D - DYNAMIC
Columns: NAME, PREFIX, PREFIX-LENGTH, ACTUAL-PREFIX, VALID-LIFETIME, PREFERRED-LIFETIME
#   NAME       PREFIX                   PREFIX-LENGTH  ACTUAL-PREFIX            VALID-LIFETIME  PREFERRED-LIFETIME
0 D test-ipv6  2001:db8:7501:ff04::/62             64  2001:db8:7501:ff04::/62  2d23h11m53s     2d15h59m53s
```

現在你可以從該池為其他介面分配地址，如下例所示。

### 使用收到的字首進行本地 RA {#use-received-prefix-for-local-ra}

考慮以下設定：

![R1 gets the prefix 2001:db8::/62 from the ISP gateway fe80::1:1 and delegates /64 prefixes to CE1 and CE2, which each use ::1/64 on their LAN](/img/443bb0b3b79cfaa3.webp)

- ISP 將字首 2001:DB8::/62 路由到路由器 R1。
- 路由器 R1 執行 DHCPv6 伺服器，以將 /64 字首委派給客戶路由器 CE1 和 CE2。
- 路由器 CE1 和 CE2 上的 DHCP 用戶端從 DHCP 伺服器（R1）接收委派的 /64 字首。
- 用戶端路由器使用接收到的字首在本地介面上設定 RA。

**配置**

**R1**

```ros
/ipv6/route
add gateway=fe80::1:1%to-ISP

/ipv6/pool
add name=myPool prefix=2001:db8::/62 prefix-length=64

/ipv6/dhcp-server
add prefix-pool=myPool disabled=no interface=to-CE-routers lease-time=3m name=server1
```

**CE1**

```ros
/ipv6/dhcp-client
add interface=to-R1 request=prefix pool-name=my-ipv6

/ipv6/address
add address=::1/64 from-pool=my-ipv6 interface=to-clients advertise=yes
```

**CE2**

```ros
/ipv6/dhcp-client
add interface=to-R1 request=prefix pool-name=my-ipv6
/ipv6/address/add address=::1/64 from-pool=my-ipv6 interface=to-clients advertise=yes
```

**檢查狀態**

檢查每個 CE 路由器是否收到了自己的字首。

在伺服器上：

```ros
[admin@R1] /ipv6/dhcp-server/binding> print
Flags: X - disabled, D - dynamic
 #   ADDRESS            DUID          IAID  SERVER   STATUS
 1 D 2001:db8:0:1::/64  0019d1393536   566  server1  bound
 2 D 2001:db8:0:2::/64  0019d1393535   565  server1  bound
```

在用戶端上：

```ros
[admin@CE1] /ipv6/dhcp-client> print
Flags: D - dynamic, X - disabled, I - invalid
 #   INTERFACE  STATUS  REQUEST  PREFIX
 0   to-R1      bound   prefix   2001:db8:0:1::/64

[admin@CE1] /ipv6/dhcp-client> /ipv6/pool/print
Flags: D - dynamic
 #   NAME     PREFIX             PREFIX-LENGTH
 0 D my-ipv6  2001:db8:0:1::/64             64
```

來自池的地址會新增到 LAN 介面：

```ros
[admin@CE1] /ipv6/address> print
Flags: X - disabled, I - invalid, D - dynamic, G - global, L - link-local
 #    ADDRESS              FROM-POOL  INTERFACE   ADVERTISE
 0  G 2001:db8:0:1::1/64   my-ipv6    to-clients  yes
...
```

池使用情況顯示某個地址使用了池的一部分：

```ros
[admin@CE1] /ipv6/pool/used> print
POOL     PREFIX             OWNER    INFO
my-ipv6  2001:db8:0:1::/64  Address  to-clients
```

## 屬性 {#properties}

DHCPv6 用戶端的所有屬性、狀態值和命令（包括指令碼接收的變數）在 [`/ipv6/dhcp-client`](../../cli-reference/ipv6/dhcp-client/index.md) CLI 參考中進行了描述。以下行為需要進一步說明。

### 伺服器發起的續租 {#server-initiated-renewal}

使用 `allow-reconfigure=yes` 時，用戶端會接受來自 DHCPv6 伺服器的 Reconfigure 訊息，並在收到此類訊息時立即續租。啟用了 `use-reconfigure=yes` 的 RouterOS DHCPv6 伺服器會在其設定（例如租期）發生變化時自行傳送此類訊息，因此用戶端無需等待續租時間即可獲取更改。

## IAID {#iaid}

要確定將使用什麼 IAID，請將執行 DHCP 用戶端的介面的內部 ID 從十六進位制轉換為十進位制。

例如，DHCP 用戶端執行在介面 PPPoE-out1 上。要獲取內部 ID，請使用以下命令：

```ros
[admin@t36] /interface> :put [find name="pppoe-out1"] 
*15
```

現在將十六進位制值 15 轉換為十進位制，即可得到 IAID=21。要使用不同的 IAID，請為地址設定 `custom-iana-id`，為字首設定 `custom-iapd-id`。
