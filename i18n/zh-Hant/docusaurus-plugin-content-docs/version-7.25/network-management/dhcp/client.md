---
sidebar_key: "network-management/dhcp/client"
sidebar_position: 1
title: "DHCP 用戶端"
sidebar_label: "DHCP 用戶端"
description: "RouterOS DHCP 用戶端從 DHCP 伺服器獲取介面的 IPv4 地址和網路設定。本頁說明用戶端會從租約中應用哪些內容、它會請求和傳送哪些選項、它會新增哪些路由，以及租約指令碼示例。"
tags:
  - 'dhcp'
source: https://manual.mikrotik.com/docs/7.25/network-management/dhcp/client
captured_at: '2026-11-04T11:21:03+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

**子選單：** `/ip/dhcp-client`

DHCP 用戶端從 DHCP 伺服器獲取介面的 IPv4 地址和網路設定。它通常用於將路由器連線到 ISP 或其他上游網路的介面，並且可以在任何類似乙太網的介面上啟用。有關 DHCP 交換、租約和續訂的工作方式，請參閱 [DHCP 概念](./index.md)。

當用戶端獲得租約時，它會將收到的設定應用到路由器：

- IP 地址和子網掩碼會作為動態地址新增到介面。
- 透過收到的閘道器的動態預設路由，或收到的無類靜態路由（選項 121），會被新增到路由表。`add-default-route` 屬性控制此行為。
- 收到的 DNS 伺服器會被新增到 DNS 解析器的動態伺服器（`use-peer-dns`），收到的 NTP 伺服器會被新增到 NTP 用戶端的伺服器（`use-peer-ntp`）。

用戶端在租約到期前續訂租約。當租約丟失或用戶端被停用時，動態地址和路由會被移除。

## 配置示例 {#configuration-examples}

### 簡單 DHCP 用戶端 {#simple-dhcp-client}

在 ether1 介面上新增 DHCP 用戶端：

```ros
/ip/dhcp-client/add interface=ether1
```

使用 `print detail` 檢視用戶端獲得的租約及其收到的設定：

```ros
[admin@MikroTik] > /ip/dhcp-client/print detail
 0   name="client1" interface=ether1 add-default-route=yes default-route-distance=1
     default-route-tables=default check-gateway=none use-peer-dns=yes use-peer-ntp=yes
     allow-reconfigure=no use-broadcast=both dhcp-options=hostname,clientid
     status=bound address=192.168.0.65/24 gateway=192.168.0.1 dhcp-server=192.168.0.1
     primary-dns=192.168.0.1 primary-ntp=192.168.0.1 expires-after=9m44s
```

## DHCP 選項 {#dhcp-options}

用戶端向 DHCP 伺服器請求以下選項：

- 選項 1 - 子網掩碼。
- 選項 3 - 閘道器地址。
- 選項 6 - DNS 伺服器地址。
- 選項 15 - 域名。
- 選項 33 - 靜態路由。
- 選項 42 - NTP 伺服器地址。
- 選項 43 - 廠商特定資訊。
- 選項 121 - 無類靜態路由。
- 選項 138 - CAPWAP 訪問控制器地址。

用戶端傳送其 `dhcp-options` 屬性中列出的選項，這些選項從 `/ip/dhcp-client/option` 中定義的選項中選擇。有三個預定義選項：

| 名稱 | 程式碼 | 值 |
| :-- | --: | :-- |
| clientid\_duid | 61 | 0xff$(CLIENT\_DUID) |
| clientid | 61 | 0x01$(CLIENT\_MAC) |
| hostname | 12 | $(HOSTNAME) |

預設情況下，用戶端傳送 `hostname` 和 `clientid`：將路由器的身份作為其主機名，以及基於用戶端介面 MAC 地址的用戶端識別符號。要改為透過路由器的 DUID 標識用戶端（RFC 4361），請在 `dhcp-options` 中將 `clientid` 替換為 `clientid_duid`。選項值使用與 DHCP 伺服器選項相同的語法。它們可以包含的變數列在 [`/ip/dhcp-client/option`](../../cli-reference/ip/dhcp-client/option.md) 參考中。

## 屬性 {#properties}

DHCP 用戶端的所有屬性、狀態值和命令都在 [`/ip/dhcp-client`](../../cli-reference/ip/dhcp-client/index.md) CLI 參考中描述。用戶端新增的路由需要進一步說明。

### 來自租約的路由 {#routes-from-the-lease}

`add-default-route` 屬性控制用戶端新增哪些收到的路由：

- `yes`（預設）：當伺服器傳送無類靜態路由（選項 121）時，用戶端會新增這些路由，否則新增透過收到的閘道器（選項 3）的預設路由。當存在選項 121 時，選項 3 中的閘道器會被忽略，這是 RFC 3442 的要求，因此伺服器必須在選項 121 中包含預設路由。
- `special-classless`：用戶端同時新增無類靜態路由和透過收到的閘道器的預設路由。當伺服器傳送不帶預設路由的無類靜態路由，且預設路由仍應來自選項 3 時，請使用它。
- `no`：用戶端不新增任何路由。

這些路由採用 `default-route-distance` 中設定的距離（預設為 1），並進入 `default-route-tables` 中列出的路由表。`default` 條目是主路由表，或者當用戶端介面屬於 VRF 時是 VRF 路由表。條目也可以設定自己的距離，例如 `default-route-tables=backup:5`。

如果已存在另一條預設路由，則使用距離較小的路由。當距離相等時，兩條路由都處於活動狀態，流量在它們之間共享（ECMP）。使用 `default-route-distance` 控制首選哪條路由，使用 `check-gateway` 在其閘道器無響應時停止使用某條路由。

## 指令碼示例 {#script-examples}

租約指令碼接收的變數在 [`/ip/dhcp-client`](../../cli-reference/ip/dhcp-client/index.md) CLI 參考的 `script` 屬性中列出。

### 租約指令碼示例 {#lease-script-example}

此示例透過收到的閘道器向 `WAN1` 路由表新增一條預設路由，在閘道器更改時更新該路由，並在租約結束時移除它。請先建立路由表，然後使用指令碼新增用戶端：

:::warning
請注意，某些變數可能在特定選單中為保留變數，無法在那裡使用。有關詳細資訊，請參閱[保留變數名](../../developer-guides/scripting/index.md#reserved-variable-names)。
:::

```ros
/routing/table/add name=WAN1 fib
/ip/dhcp-client/add interface=ether2 add-default-route=no script={
    :local count [/ip/route/print count-only where comment="WAN1"]
    :if ($bound=1) do={
        :if ($count = 0) do={
            /ip/route/add gateway=$"gateway-address" comment="WAN1" routing-table=WAN1
        } else={
            :if ($count = 1) do={
                :local test [/ip/route/find where comment="WAN1"]
                :if ([/ip/route/get $test gateway] != $"gateway-address") do={
                    /ip/route/set $test gateway=$"gateway-address"
                }
            } else={
                :error "Multiple routes found"
            }
        }
    } else={
        /ip/route/remove [find comment="WAN1"]
    }
}
```

### 使用收到的選項 43 設定 ACS URL {#using-received-option-43-to-set-the-acs-url}

DHCP 伺服器可以在供應商特定資訊選項（選項 43）中傳送 TR-069 自動配置伺服器（ACS）的 URL。用戶端指令碼在 `vendor-specific` 變數中接收此選項，因此可以在租約繫結時設定 TR-069 用戶端的 ACS URL。TR-069 用戶端是一個單獨的軟體包。

```ros
/ip/dhcp-client/set [find interface=ether1] script={
    :if ($bound=1) do={
        /tr069-client/set acs-url=$"vendor-specific"
    }
}
```

### 租約子網外的預設閘道器 {#default-gateway-outside-the-leased-subnet}

某些 DHCP 伺服器傳送的閘道器（選項 3）不在租約子網中。例如，伺服器提供 192.168.88.100/24，閘道器為 172.16.1.1。用戶端新增的預設路由隨後會保持非活動狀態，因為無法訪問閘道器：

```ros
[admin@MikroTik] > /ip/route/print
Flags: D - DYNAMIC; I - INACTIVE, A - ACTIVE; c - CONNECT, d - DHCP
Columns: DST-ADDRESS, GATEWAY, DISTANCE
    DST-ADDRESS      GATEWAY     DISTANCE
DId 0.0.0.0/0        172.16.1.1         1
DAc 192.168.88.0/24  ether1             0
```

要使閘道器可達，請將租約地址再次新增為 /32 地址，並以閘道器作為其網路。這會建立一條到閘道器的直連路由。請在用戶端指令碼中執行此操作，該指令碼會接收租約地址、閘道器和介面：

```ros
/ip/dhcp-client/set [find interface=ether1] script={
    /ip/address/add address=($"lease-address" . "/32") network=$"gateway-address" interface=$interface
}
```

這個簡短指令碼會在每次新租約時新增另一個地址。以下指令碼保留單個地址，並在租約地址或閘道器更改時替換它：

```ros
/ip/dhcp-client/set [find interface=ether1] script={
    /ip/address {
        :local ipId [find where comment="dhcpL address"]
        :if ($ipId != "") do={
            :if (!([get $ipId address] = ($"lease-address" . "/32") && [get $ipId network]=$"gateway-address")) do={
                remove $ipId
                add address=($"lease-address" . "/32") network=$"gateway-address" interface=$interface comment="dhcpL address"
            }
        } else={
            add address=($"lease-address" . "/32") network=$"gateway-address" interface=$interface comment="dhcpL address"
        }
    }
}
```
