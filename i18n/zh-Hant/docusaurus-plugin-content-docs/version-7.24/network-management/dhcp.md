---
sidebar_key: "network-management/dhcp"
sidebar_position: 3
title: "DHCP"
sidebar_label: "DHCP"
description: "MikroTik RouterOS 文件頁面介紹了 DHCP 用戶端功能，說明了如何透過 DHCP 配置和管理 IP 地址分配。其中涵蓋了用戶端屬性，例如預設路由處理、DNS/NTP 整合和 VLAN 優先順序設定，以及只讀狀態指示資訊，例如已分配的 IP 地址和 DHCP 伺服器詳情。"
tags:
  - 'dhcp'
source: https://manual.mikrotik.com/docs/7.24/network-management/dhcp
captured_at: '2026-11-07T17:11:03.548Z'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## DHCP 用戶端 {#dhcp-client}

### 概述 {#summary}

**子選單：** `/ip/dhcp-client`

DHCP（動態主機配置協定）用於在網路中輕鬆分配 IP 地址。MikroTik RouterOS 實現包括伺服器端和用戶端部分，並符合 RFC 2131。

MikroTik RouterOS DHCP 用戶端可以一次在任何類乙太網介面上啟用。用戶端將接受一個地址、網路掩碼、預設閘道器和兩個 DNS 伺服器地址。接收到的 IP 地址將連同相應的網路掩碼新增到介面。預設閘道器將作為動態條目新增到路由表。如果 DHCP 用戶端被停用或未續租地址，動態預設路由將被移除。如果在 DHCP 用戶端獲得預設路由之前已經安裝了預設路由，則 DHCP 用戶端獲得的路由將顯示為 invalid。

RouterOS DHCP 用戶端請求以下選項：

- 選項 1 - 子網掩碼。
- 選項 3 - 閘道器地址。
- 選項 6 - DNS 伺服器地址。
- 選項 15 - 域名。
- 選項 33 - 靜態路由。
- 選項 42 - NTP 伺服器地址。
- 選項 43 - 廠商特定資訊。
- 選項 121 - 無類靜態路由。
- 選項 138 - CAPWAP 訪問控制器地址。

### DHCP 選項 {#dhcp-options}

DHCP 用戶端可以設定傳送給 DHCP 伺服器的選項，例如主機名和 MAC 地址。語法與 DHCP 伺服器選項相同。

目前，選項中可以使用的變數有三個：

- HOSTNAME。
- CLIENT\_MAC - 用戶端介面 MAC 地址。
- CLIENT\_DUID - 路由器的用戶端 DUID，與 DHCPv6 用戶端使用的相同。符合 RFC4361。

DHCP 用戶端預設選項包括以下預設選項：

| 名稱 | code | value |
| :-- | --: | :-- |
| clientid\_duid | 61 | 0xff$(CLIENT\_DUID) |
| clientid | 61 | 0x01$(CLIENT\_MAC) |
| hostname | 12 | $(HOSTNAME) |

### 屬性 {#properties}

| 屬性 | 描述 |
| :-- | :-- |
| **add-default-route** (*yes \| no \| special-classless*; 預設：**yes**) | 是否安裝從 DHCP 伺服器接收的預設路由到路由表中。預設情況下，RouterOS 用戶端遵循 RFC，如果收到無類選項 121，則忽略選項 3。要強制用戶端不忽略選項 3，請設定 *special-classless*。此引數在 v6rc12+ 中可用 yes - 如果收到無類路由則新增，否則新增預設路由（舊行為）special-classless - 如果收到無類路由則新增無類路由，同時新增預設路由（MS 風格） |
| **allow-reconfigure** (*yes \| no*; 預設：**no**) | 允許接收來自 DHCP 伺服器的 Reconfigure（forcerenew）訊息。對於現有 dhcp-client 的更改，請續租。 |
| **check-gateway** *(none \| arp \| bfd \| ping***;** Default: **none)** | 用於檢查路由 [閘道器可達性](../user-guides/routing-and-networking-protocols/routing-decision.md) 的方法。 |
| **client-id** (*string*; 預設：) | 對應於網路管理員或 ISP 建議的設定。如果未指定，將傳送用戶端的 MAC 地址 |
| **comment** (*string*; 預設：) | 用戶端的簡短描述 |
| **default-route-tables** (*table:distance*; 預設：*default*) | 必須新增預設路由的路由表列表。表名前面可以加上 ":x"，其中 x 是安裝路由時使用的距離。 |
| **default-route-distance** (*integer:0..255*; 預設：) | 預設路由距離。 |
| **disabled** (*yes \| no*; 預設：**yes**) | 用戶端是否被停用。 |
| **dscp** (*integer:0..63*; 預設：**0**) | 設定傳出 DHCP 用戶端封包的 DSCP（差分服務程式碼點）值。此值屬於 IP 頭部的一部分，用於指示網路流量所需的服務質量（QoS）級別。 |
| **host-name** (*string*; 預設：) | 傳送給 DHCP 伺服器的用戶端主機名。如果未指定，將使用用戶端的系統標識。 |
| **interface** (*string*; 預設：) | DHCP 用戶端將執行的介面。 |
| **name** (*string;*預設：) | DHCP 用戶端的名稱，如果未指定則由 RouterOS 生成。 |
| **script** (*script*; 預設：) | 當 DHCP 用戶端獲得新租約或丟失現有租約、接收到的閘道器地址或 DNS 伺服器列表發生變化時執行指令碼。事件指令碼可訪問的變數：bound - 1 - 租約已新增/更改；0 - 租約已移除server-address - 伺服器地址lease-address - 伺服器提供的租約地址interface - 配置用戶端的介面名稱gateway-address - 伺服器提供的閘道器地址vendor-specific - 儲存從 DHCP 伺服器收到的選項 43 值lease-options - 從伺服器接收的選項陣列[`示例 >>`](./dns.md) |
| **use-broadcast** (*always* \| *both* \| *never*; 預設：**both**) | 是否在 DHCPDISCOVER 和 DHCPREQUEST 訊息中設定 *broadcast* 位。  *always - broadcast* 位始終設定  *both - broadcast* 位僅在前 15 秒設定  *never - broadcast* 位不設定 |
| **use-peer-dns** (*yes \| no*; 預設：**yes**) | 是否接受 [DHCP 伺服器](./dhcp.md#dhcp-server) 通告的 [DNS](../system-information-and-utilities/ntp.md) 設定。（將覆蓋 `/ip/dns` 子選單中的設定。 |
| **use-peer-ntp** (*yes \| no*; 預設：**yes**) | 是否接受 [DHCP 伺服器](./dhcp.md#dhcp-server) 通告的 [NTP](../bridging-and-switching/vlan.md) 設定。（將覆蓋 `/system/ntp/client` 子選單中的設定） |
| **vlan-priority** (*integer:0..7*; 預設：**0**) | 如果 DHCP 用戶端執行在 [VLAN 介面](../bridging-and-switching/vlan.md)（/interface/vlan）上，可以指定優先順序程式碼點（PCP）值。PCP 是 VLAN 頭部中的 3 位欄位，用於標記 VLAN 內封包的優先順序，從而允許相應地設定流量優先順序。此設定僅適用於 VLAN 介面，並影響傳出 DHCP 用戶端封包的優先順序。 |

#### 只讀屬性 {#read-only-properties}

| 屬性 | 描述 |
| :-- | :-- |
| **address** (*IP/Netmask*) | 由伺服器分配給 DHCP 用戶端的 IP 地址和網路掩碼 |
| **dhcp-server** (*IP*) | DHCP 伺服器的 IP 地址。 |
| **expires-after** (*time*) | 租約到期的時間（由 DHCP 伺服器指定）。 |
| **gateway** (*IP*) | 由 DHCP 伺服器分配的閘道器 IP 地址 |
| **invalid** (*yes \| no*) | 顯示配置是否無效。 |
| **netmask** (*IP*) |  |
| **primary-dns** (*IP*) | 由 DHCP 伺服器分配的第一個 DNS 解析器的 IP 地址 |
| **primary-ntp** (*IP*) | 由 DHCP 伺服器分配的主 NTP 伺服器的 IP 地址 |
| **secondary-dns** (*IP*) | 由 DHCP 伺服器分配的第二個 DNS 解析器的 IP 地址 |
| **secondary-ntp** (*IP*) | 由 DHCP 伺服器分配的輔助 NTP 伺服器的 IP 地址 |
| **status** (*bound \| error \| rebinding... \| requesting... \| searching... \| stopped*) | 顯示 DHCP 用戶端的狀態 |
| **reconfigure-key**(string) | 重新配置認證金鑰 |
| **reconfigure-last-counter** *(integer)* | 接收到的 Reconfigure（*forcerenew*）訊息數量 |
| **custom-source-mac-address** *(MAC)* | DHCP 用戶端使用的自定義源 MAC 地址。 |
| **custom-hostname-suffix** *(string)* | 傳送給 DHCP 伺服器的主機名後附加的字尾。 |
| **caps-managers** *(string)* | 透過 DHCP 選項 138 發現的 CAPsMAN 控制器地址列表。 |

#### 選單專用命令 {#menu-specific-commands}

| 屬性 | 描述 |
| :-- | :-- |
| **release** (*numbers*) | 釋放當前繫結並重啟 DHCP 用戶端 |
| **renew** (*numbers*) | 續租當前租約。如果續租操作未成功，用戶端會嘗試重新初始化租約（即像尚未收到 IP 地址一樣啟動租約請求過程（rebind）） |

### 配置示例 {#configuration-examples}

#### 簡單 DHCP 用戶端 {#simple-dhcp-client}

在 ether1 介面上新增 DHCP 用戶端：

```ros
/ip/dhcp-client/add interface=ether1 disabled=no
```

新增介面後，可以使用 "print" 或 "print detail" 命令檢視 DHCP 用戶端獲取了哪些引數：

```ros
[admin@MikroTik] /ip/dhcp-client> print detail
Flags: X - disabled, I - invalid 
 0   interface=ether1 add-default-route=yes use-peer-dns=yes use-peer-ntp=yes
     status=bound address=192.168.0.65/24 gateway=192.168.0.1
     dhcp-server=192.168.0.1 primary-dns=192.168.0.1 primary-ntp=192.168.0.1
     expires-after=9m44s 
[admin@MikroTik] /ip/dhcp-client>
```

:::warning
如果 DHCP 用戶端使用的介面屬於 VRF 配置的一部分，則預設路由和從 DHCP 伺服器接收的其他路由將被新增到 VRF 路由表。

:::

可以使用以下命令檢查 DHCP 用戶端狀態：

```ros
/ip/dhcp-client/print detail 
```

#### 租約指令碼示例 {#lease-script-example}

可以在 DHCP 用戶端獲得新租約或丟失現有租約時執行指令碼。以下示例指令碼會自動新增 routing-table=WAN1 的預設路由，並在租約到期或移除時刪除它。

:::warning
請注意，某些變數可能在特定選單中保留，不能在那裡使用。更多資訊請參見[此處](../developer-guides/scripting/index.md#reserved-variable-names)。

:::

```ros
/ip/dhcp-client
add add-default-route=no dhcp-options=hostname,clientid disabled=no interface=ether2 script="{\r\
    \n    :local rmark \"WAN1\"\r\
    \n    :local count [/ip/route/print count-only where comment=\"WAN1\"]\r\
    \n    :if (\$bound=1) do={\r\
    \n        :if (\$count = 0) do={\r\
    \n            /ip/route/add gateway=\$\"gateway-address\" comment=\"WAN1\" routing-table=\$rmark\r\
    \n        } else={\r\
    \n            :if (\$count = 1) do={\r\
    \n                :local test [/ip/route/find where comment=\"WAN1\"]\r\
    \n                :if ([/ip/route/get \$test gateway] != \$\"gateway-address\") do={\r\
    \n                    /ip/route/set \$test gateway=\$\"gateway-address\"\r\
    \n                }\r\
    \n            } else={\r\
    \n                :error \"Multiple routes found\"\r\
    \n            }\r\
    \n        }\r\
    \n    } else={\r\
    \n        /ip/route/remove [find comment=\"WAN1\"]\r\
    \n    }\r\
    \n}\r\
    \n"
```

#### 使用接收到的 Option 43 設定 ACS URL {#using-received-option-43-to-set-the-acs-url}

當 DHCP 用戶端租約繫結，並且 DHCP 伺服器傳送的選項配置為傳送它時，可以在 TR069 用戶端設定中設定 *自動配置伺服器（ACS）*URL。示例如下：

```ros
:if ($bound=1) do={
/tr069-client/set acs-url=$"vendor-specific"
}
```

#### 當 'router'（option3）來自不同子網時解析預設閘道器 {#resolve-default-gateway-when-router-option3-is-from-a-different-subnet}

在某些情況下，管理員傾向於設定無法用所提供的 IP 子網解析的 'router' 選項。例如，DHCP 伺服器向用戶端提供 192.168.88.100/24，而選項 3 設定為 172.16.1.1。這將導致預設路由無法解析：

```ros
 #      DST-ADDRESS        PREF-SRC        GATEWAY            DISTANCE
 0  DS  0.0.0.0/0                          172.16.1.1              1
 1 ADC  192.168.88.0/24    192.168.88.100  ether1 
```

要解決此問題，我們需要新增一條 /32 路由以透過 ether1 解析閘道器，這可以透過每次 DHCP 用戶端獲得地址時執行以下指令碼來完成

```ros
/system/script/add name="dhcpL" source={ /ip/address/add address=($"lease-address" . "/32") network=$"gateway-address" interface=$interface }
```

現在我們可以進一步擴充套件指令碼，檢查地址是否已經存在，並在需要更改時刪除舊地址

```ros
/system/script/add name="dhcpL" source={ 
  /ip/address {
    :local ipId [find where comment="dhcpL address"]
    :if ($ipId != "") do={
      :if (!([get $ipId address] = ($"lease-address" . "/32") && [get $ipId network]=$"gateway-address" )) do={
        remove $ipId;
        add address=($"lease-address" . "/32") network=$"gateway-address" \
          interface=$interface comment="dhcpL address"
      }
    } else={
      add address=($"lease-address" . "/32") network=$"gateway-address" \
        interface=$interface comment="dhcpL address"
    }
  }
}
```

## DHCPv6 用戶端 {#dhcpv6-client}

### 概述 {#summary-1}

**子選單：** `/ipv6/dhcp-client`

RouterOS 中的 DHCP-client 能夠作為 DHCPv6-client 和 DHCP-PD 用戶端。因此，它既能夠從 DHCP-PD 伺服器獲取字首，也能夠從 DHCPv6 伺服器獲取 DHCPv6 有狀態地址。

### 屬性 {#properties-1}

| 屬性 | 描述 |
| :-- | :-- |
| **add-default-route** (*yes \| no*; 預設：**no**) | 用戶端連線後是否新增預設 IPv6 路由。 |
| **allow-reconfigure** (*yes \| no*; 預設：**no**) | 允許接收來自 DHCP 伺服器的 Reconfigure（forcerenew）訊息。 |
| **default-route-tables** (*table:distance*; 預設：main) | 必須新增預設路由的路由表列表。表名前面可以加上 ":x"，其中 x 是安裝路由時使用的距離。 |
| **comment** (*string*; 預設：) | 用戶端的簡短描述 |
| **disabled** (*yes \| no*; 預設值：**no**) |  |
| **interface** (*string*; 預設：) | DHCPv6 用戶端將執行的介面。 |
| **pool-name** (*string*; 預設：) | 接收到的 IPv6 字首將新增到的 [IPv6 地址池](../cli-reference/ipv6/pool/index.md) 名稱 |
| **pool-prefix-length** (*integer*; 預設：) | 為接收到的 IPv6 字首新增到的 [IPv6 地址池](../cli-reference/ipv6/pool/index.md) 設定的字首長度引數。字首長度必須大於或等於接收到字首的長度。如果未設定該值，則字首將按從伺服器接收到的長度新增。 |
| **prefix-address-lists**(*string*; 預設：) | 接收到的字首將新增到的防火牆地址列表名稱。 |
| **prefix-hint** (*string*; 預設：) | 包含首選字首長度。 |
| **request** (*prefix, address*; 預設：) | 選擇 DHCPv6 請求將請求地址還是 IPv6 字首，或兩者都請求。 |
| **script** (*string*; 預設：) | 在 DHCP-client 狀態變化時執行此指令碼。可用變數：pd-valid - 用戶端是否已獲取字首；pd-prefix - 用戶端獲取的字首（如果有）；na-valid - 用戶端是否已獲取地址；na-address - 用戶端獲取的地址（如果有）。options - 接收到的選項陣列（僅 ROSv7） |
| **use-peer-dns** (*yes \| no*; 預設：**yes**) | 是否接受 IPv6 DHCP 伺服器通告的 DNS 設定。 |
| **custom-duid** (*hex string*; 預設：) | 允許指定自定義 DUID。 |
| **use-interface-duid**(*yes \| no*; 預設：**no**) | 根據 RFC，DHCPv6 用戶端基於路由器的第一個介面 MAC 地址生成 DUID，而不是基於配置用戶端的介面。啟用此選項後，將覆蓋此要求，並使用用戶端上指定的 "interface" 中的 MAC 地址。 |
| ****validate-server-duid**** (*yes \| no*; 預設：**yes**) | 允許忽略 DHCPv6 伺服器提供的格式不正確的 DUID。仍會檢查最小 DUID 長度是否正確。 |
| **custom-iapd-id**(integer; 預設：) | 允許指定自定義 IAPD ID。 |
| **custom-iana-id**(*integer*; 預設：) | 允許指定自定義 IANA ID。 |

### 只讀屬性 {#read-only-properties-1}

| 屬性 | 描述 |
| :-- | :-- |
| **duid** (*string*) | 傳送給伺服器的自動生成 DUID。DUID 使用路由器上可用的某個 MAC 地址生成。 |
| **request** (*list*) | 指定請求的內容 - 字首、地址或兩者。 |
| **dynamic** (*yes \| no*) |  |
| **expires-after** (*time*) | IPv6 字首到期的時間（由 DHCPv6 伺服器指定）。 |
| **invalid** (*yes \| no*) | 顯示配置是否無效。 |
| **prefix** (*IPv6 prefix*) | 顯示從 DHCPv6-PD 伺服器接收到的 IPv6 字首 |
| **status** (*stopped \| searching \| requesting... \| bound \| renewing \| rebinding \| error \| stopping*) | 顯示 DHCPv6 用戶端的狀態：stopped - dhcpv6 用戶端已停止searching - 傳送 "solicit" 並嘗試獲取 "advertise"requesting - 已傳送 "request"，等待 "reply"bound - 已收到 "reply"。字首已分配。renewing - 已傳送 "renew"，等待 "reply"rebinding - 已傳送 "rebind"，等待 "reply"error - 未及時收到回覆或發生了其他錯誤。stopping - 已傳送 "release" |
| **reconfigure-key**(string) | 重新配置認證金鑰 |
| **reconfigure-last-counter** (integer) | 接收到的 forcerenew 訊息數量 |
| dhcp-server-v6  | |
| address  | |

### 選單專用命令 {#menu-specific-commands-1}

| 屬性 | 描述 |
| :-- | :-- |
| **release** (*numbers*) | 釋放當前繫結並重啟 DHCPv6 用戶端 |
| **renew** (*numbers*) | 續租當前租約。如果續租操作未成功，用戶端會嘗試重新初始化租約（即像尚未收到 IP 地址一樣啟動租約請求過程（rebind）） |

### 指令碼 {#script}

可以使用 DHCP 用戶端新增一個指令碼，在獲取並應用字首或地址時執行，或者在字首或地址到期並被移除時執行。根據字首或地址狀態變化，用戶端有兩組獨立的變數，因為用戶端可以同時獲取兩者，並且它們對路由器配置可能有不同的影響。

#### dhcp-client 的可用變數 {#available-variables-for-dhcp-client}

- pd-valid - 值 - 1 或 0 - 字首是否已獲取並應用
- pd-prefix - 值 ipv6/num（帶掩碼的 IPv6 字首）- 字首本身
- na-valid - 值 - 1 或 0 - 地址是否已獲取並應用
- na-address - 值 - IPv6 地址 - 地址

### IAID {#iaid}

要確定將使用什麼 IAID，請將執行 DHCP 用戶端的介面的內部 ID 從十六進位制轉換為十進位制。

例如，DHCP 用戶端執行在介面 PPPoE-out1 上。要獲取內部 ID，請使用以下命令：

```ros
[admin@t36] /interface> :put [find name="pppoe-out1"] 
*15
```

現在將十六進位制值 15 轉換為十進位制，即可得到 IAID=21

### 配置示例 {#configuration-examples-1}

#### 簡單 DHCPv6 用戶端 {#simple-dhcpv6-client}

這個簡單示例演示如何啟用 dhcp 用戶端以接收 IPv6 字首並將其新增到地址池。

```ros
/ipv6/dhcp-client/add request=prefix pool-name=test-ipv6 pool-prefix-length=64 interface=ether13 

```

詳細列印應顯示用戶端狀態，我們可以驗證是否收到字首

```ros
[admin@x86-test] /ipv6/dhcp-client> print detail 
Flags: D - dynamic, X - disabled, I - invalid
 0 interface=bypass pool-name="test-ipv6" pool-prefix-length=64 status=bound 
prefix=2001:db8:7501:ff04::/62 expires-after=2d23h11m53s request=prefix
```

請注意，伺服器給我們的字首是 2001:db8:7501:ff04::/62。它也應該被新增到 IPv6 地址池中

```ros
[admin@MikroTik] /ipv6/pool> print 
Flags: D - dynamic 
# NAME PREFIX REQUEST PREFIX-LENGTH
0 D test-ipv6 2001:db8:7501:ff04::/62 prefix 64

```

它工作了！現在你可以使用這個地址池，例如用於 pppoe 用戶端。

#### 將接收到的字首用於本地 RA {#use-received-prefix-for-local-ra}

考慮以下設定：

![](/img/443bb0b3b79cfaa3.webp)

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

配置完成後，我們可以驗證每個 CE 路由器都收到了自己的字首

在伺服器上：

```ros
[admin@R1] /ipv6/dhcp-server/binding> print
 Flags: X - disabled, D - dynamic 
# ADDRESS DUID IAID SERVER STATUS
 1 D 2001:db8:1::/64 0019d1393536 566 server1 bound 
2 D 2001:db8:2::/64 0019d1393535 565 server1 bound
```

在用戶端上：

```ros
[admin@CE1] /ipv6/dhcp-client> print 
Flags: D - dynamic, X - disabled, I - invalid 
# INTERFACE STATUS REQUEST PREFIX 
0 to-R1 bound prefix 2001:db8:1::/64 

[admin@CE1] /ipv6/dhcp-client> /ipv6/pool/print 
Flags: D - dynamic 
# NAME PREFIX PREFIX-LENGTH
0 D my-ipv6 2001:db8:1::/64 64
```

我們還可以看到 IPv6 地址已自動從字首池新增：

```ros
[admin@CE1] /ipv6/address> print 
Flags: X - disabled, I - invalid, D - dynamic, G - global, L - link-local 
# ADDRESS FROM-POOL INTERFACE ADVERTISE 0 G 2001:db8:1::1/64 to-clients yes 
..
```

地址池使用情況顯示 'Address' 正在分配該地址池

```ros
[admin@CE1] /ipv6/pool/used> print
 POOL PREFIX OWNER INFO 
my-ipv6 2001:db8:1::/64 Address to-clients
```

## DHCP 伺服器 {#dhcp-server}

### 概述 {#summary-2}

DHCP（動態主機配置協定）用於在網路中輕鬆分配 IP 地址。MikroTik RouterOS 實現包括伺服器端和用戶端部分，並符合 RFC 2131。

路由器支援為每個類乙太網介面提供單獨的伺服器。MikroTik RouterOS DHCP 伺服器支援基本功能：為每個請求用戶端提供 IP 地址/網路掩碼租約、預設閘道器、域名、DNS 伺服器和 WINS 伺服器（用於 Windows 用戶端）資訊（在 DHCP networks 子選單中設定）。

為使 DHCP 伺服器工作，還必須配置 IP 地址池（不要將 DHCP 伺服器自身的 IP 地址包含在地址池範圍內），並且還必須配置 DHCP networks。

也可以使用 RADIUS 伺服器為 DHCP 用戶端分配租約；RADIUS 伺服器支援的引數如下：

#### Access-Request {#access-request}

- NAS-Identifier - 路由器身份。
- NAS-IP-Address - 路由器自身的 IP 地址。
- NAS-Port - 配置 DHCP 伺服器的介面 ID。此值與 IF-MIB::ifIndex 相同。
- NAS-Port-Id - 配置 DHCP 伺服器的介面名稱。
- NAS-Port-Type - Ethernet。
- Calling-Station-Id - 用戶端識別符號（active-client-id）。
- Framed-IP-Address - 用戶端 IP 地址（active-address）。
- Called-Station-Id - DHCP 伺服器名稱。
- User-Name - 用戶端 MAC 地址（active-mac-address）。
- Password - " "。

#### Access-Accept {#access-accept}

- Framed-IP-Address - 將分配給用戶端的 IP 地址。
- Framed-Pool - 用於向用戶端分配 IP 地址的 IP 地址池。
- Rate-Limit - DHCP 用戶端的資料速率限制。格式為：rx-rate[/tx-rate] [rx-burst-rate[/tx-burst-rate] [rx-burst-threshold[/tx-burst-threshold] [rx-burst-time[/tx-burst-time][priority] [rx-rate-min[/tx-rate-min]]]]。所有速率應為數字，可帶 'k'（1,000 倍）或 'M'（1,000,000 倍）。如果未指定 tx-rate，則 rx-rate 也用作 tx-rate。tx-burst-rate、tx-burst-threshold 和 tx-burst-time 同理。如果 rx-burst-threshold 和 tx-burst-threshold 均未指定（但指定了 burst-rate），則 rx-rate 和 tx-rate 用作突發閾值。如果 rx-burst-time 和 tx-burst-time 均未指定，則預設使用 1s。Priority 取值為 1..8，其中 1 表示最高優先順序，8 表示最低優先順序。如果未指定 rx-rate-min 和 tx-rate-min，則使用 rx-rate 和 tx-rate 值。rx-rate-min 和 tx-rate-min 值不能超過 rx-rate 和 tx-rate 值。
- Ascend-Data-Rate - TX/RX 資料速率限制；如果提供多個屬性，第一個限制 tx 資料速率，第二個限制 RX 資料速率。如果與 Ascend-Xmit-Rate 一起使用，則指定 RX 速率。0 表示不限速。
- Ascend-Xmit-Rate - tx 資料速率限制。可用於僅指定 TX 限制，而不是傳送兩個連續的 Ascend-Data-Rate 屬性（在這種情況下，Ascend-Data-Rate 將指定接收速率）。0 表示不限速。
- Session-Timeout - 最大租約時間（lease-time）。

:::warning
DHCP 伺服器需要一個真實介面來接收原始乙太網封包。如果介面是 Bridge 介面，則 Bridge 必須有一個真實介面作為該橋接的埠連線，以接收原始乙太網封包。它不能在虛擬（空橋接）介面上正常工作。

:::

### DHCP 伺服器屬性 {#dhcp-server-properties}

| 屬性 | 描述 |
| :-- | :-- |
| **add-arp** (*yes \| no*; 預設：**no**) | 是否新增動態 ARP 條目。如果設定為 **no**，則應在該介面上啟用 ARP 模式，或在 *`/ip/arp`* 子選單中透過管理方式定義靜態 ARP 條目。 |
| **add-dns-entries** (*yes \| no*; 預設：**no**) | 設定為 **yes** 時，DHCP 伺服器會使用用戶端的主機名為每個租約自動建立動態 DNS A 記錄。主機名取自用戶端傳送的 DHCP 選項 12。生成的 FQDN 透過將 **add-dns-entries-suffix**（如果未設定字尾，則使用 DHCP 網路配置中的 **domain**）附加到主機名來形成。 |
| **add-dns-entries-suffix** (*string*; 預設：**""**) | 建立動態 DNS 條目時附加到主機名的字尾。例如，如果設定為 `example.lan` 且用戶端主機名為 `laptop`，則將建立 DNS 條目 `laptop.example.lan`。如果留空，則改用 DHCP 網路配置中的 **domain** 值。 |
| **address-pool** (*string \| static-only*; 預設：**static-only**) | 用於為用戶端獲取 IP 地址的 IP 地址池。如果設定為 **static-only**，則只允許具有靜態租約的用戶端（在 lease 子選單中新增）。 |
| **allow-dual-stack-queue** (*yes \| no*; 預設：**yes**) | 為 IPv4 和 IPv6 地址建立單個簡單佇列條目，並使用 MAC 地址和 DUID 進行標識。需要 IPv6 DHCP 伺服器也啟用此選項才能正常工作。 |
| **always-broadcast** (*yes \| no*; 預設：**no**) | 更改是否強制廣播 DHCP 回覆：no - 根據用戶端的廣播標誌傳送回覆。如果伺服器連續傳送三個提議，第三個和第四個提議將作為廣播發送；yes - 即使用戶端未指定廣播標誌，回覆也始終廣播。 |
| **authoritative** (*after-10sec-delay \| after-2sec-delay \| yes \| no*; 預設：**yes**) | 該選項更改伺服器響應 DHCP 請求的方式：yes - 回覆用戶端對不可從此伺服器獲取的地址的請求時，DHCP 伺服器將傳送否定確認（DHCPNAK）；no - DHCP 伺服器忽略用戶端對不可從此伺服器獲取的地址的請求；after-10sec-delay - "secs &lt; 10" 的請求將按 "no" 設定的情況處理，而 "secs &gt;= 10" 的請求將按 "yes" 情況處理；after-2sec-delay - "secs &lt; 2" 的請求將按 "no" 設定的情況處理，而 "secs &gt;= 2" 的請求將按 "yes" 情況處理；  如果應忽略所有 "secs < x" 的請求，則應使用 **delay-threshold=x** 設定。 |
| **bootp-lease-time** (*forever \| lease-time \| time*; 預設：**forever**) | 接受兩個預定義選項或時間值：forever - 租約永不過期lease-time - 使用 lease-time 引數中的時間 |
| **bootp-support** (*none \| static \| dynamic*; 預設：**static**) | 對 BOOTP 用戶端的支援：none - 不響應 BOOTP 請求static - 僅向 BOOTP 用戶端提供靜態租約dynamic - 向 BOOTP 用戶端提供靜態和動態租約 |
| **client-mac-limit** (*integer \| unlimited*; 預設：**unlimited**) | 指定是否限制每個單一 MAC 地址的特定用戶端數量，或保持不限制。請注意，此設定不應在中繼設定中使用。 |
| **conflict-detection** (*yes \| no*; 預設：**yes**) | 允許停用/啟用衝突檢測。如果啟用該選項，則每當伺服器嘗試分配租約時，它將傳送 ICMP 和 ARP 訊息以檢測網路中是否已存在這樣的地址。如果上述任一訊息得到回覆，則該地址被視為已使用。 |
| **delay-threshold** (*time \| none*; 預設：**none**) | 如果 DHCP 封包中的 secs 欄位小於延遲閾值，則忽略此封包。如果設定為 **none** - 沒有閾值（處理所有 DHCP 封包） |
| **dhcp-option-set** (*name \| none*; 預設：**none**) | 使用在 option sets 選單中定義的自定義 DHCP 選項集。 |
| **dynamic-lease-identifiers** (*list of client-id, client-mac, opt-82*; 預設：**client-id,client-mac**) | 指定生成動態 DHCP 租約時使用和儲存哪些引數。 |
| **insert-queue-before** (*bottom \| first \| name*; 預設：**first**) | 指定將具有 rate-limit 引數設定的靜態 DHCP 租約的動態簡單佇列條目放置在何處。 |
| **interface** (*string*; 預設：) | DHCP 伺服器將執行的介面。 |
| **lease-script** (*string*; 預設：**""**) | 在分配或取消分配租約後執行的指令碼。可在指令碼中使用的內部 "global" 變數：leaseBound - 如果已繫結則設定為 "1"，否則設定為 "0"leaseServerName - DHCP 伺服器名稱leaseActMAC - 活動 mac 地址leaseActIP - 活動 IP 地址lease-agent-circuit-id - 租約代理電路 IDlease-agent-remote-id - 租約代理遠端 IDlease-hostname - 用戶端主機名lease-options - 傳送給用戶端的選項陣列 |
| **lease-time** (*time*; 預設：**30m**) | 用戶端可以使用所分配地址的時間。用戶端將在此時間的一半後嘗試續租此地址，並在時間限制到期後請求新地址。 |
| **name** (*string*; 預設：) | 引用名稱 |
| **parent-queue** (*string \| none*; 預設：**none**) | 為此租約動態建立的佇列將配置為指定父佇列的子佇列。 |
| **relay** (*IP*; 預設：**0.0.0.0**) | 此 DHCP 伺服器應處理其請求的中繼 IP 地址：0.0.0.0 - DHCP 伺服器將僅用於來自用戶端的直接請求（不允許 DHCP 中繼）255.255.255.255 - DHCP 伺服器應用於來自 DHCP 中繼的任何傳入請求，但由 <code>`/ip/dhcp-server`</code> 子選單中存在的另一個 DHCP 伺服器處理的請求除外。 |
| **server-address** (*IP*; 預設：**0.0.0.0**) | 在用戶端引導過程的下一步中要使用的伺服器 IP 地址（例如，在介面分配了多個地址的情況下分配特定伺服器地址） |
| **support-broadband-tr101** (*yes \| no*; 預設：**no**) | 啟用或停用在 RADIUS Access-Request 和 Accounting-Request 訊息中包含額外的 Option 82 子選項（例如 0x81 actual upstream、0x82 actual downstream），如 RFC 4679 和 Broadband Forum TR-101 所述。  啟用後，DHCP 伺服器在 DHCP Option 82（中繼代理資訊）下包含特定子選項，RADIUS 伺服器使用這些子選項來識別寬頻接入網路（尤其是基於 DSL 基礎設施的網路）中的使用者線路引數。  此屬性僅在 `use-radius` 設定為 `yes` 或 `accounting` 時生效。 |
| **use-framed-as-classless** (*yes \| no*; 預設：**yes**) | 將 RADIUS Framed-Route 作為 DHCP 無類靜態路由轉發給 DHCP-client。每當同時收到 Framed-Route 和 Classless-Static-Route 時，優先使用 Classless-Static-Route。 |
| **use-radius** (*yes \| no \| accounting*; 預設：**no**) | 是否使用 RADIUS 伺服器：no - 不使用 RADIUS；yes - 使用 RADIUS 進行計費和租約；accounting - 僅使用 RADIUS 進行計費。 |
| **use-reconfigure** (*yes \| no*; 預設：**no**) | 允許伺服器向用戶端傳送 Reconfigure（*forcerenew*）訊息，提示它們續租配置而無需等待租約到期。 |
| **address-lists** (*string*; 預設：**none**) | 如果租約繫結，地址將新增到的地址列表。 |

:::info[動態 DNS 條目的 DNS 區域要求]
當 **add-dns-entries** 設定為 `yes` 時，DHCP 伺服器會使用用戶端的主機名為每個租約建立動態 DNS 記錄。這些記錄使用的域取自 **add-dns-entries-suffix** 引數，或回退到 DHCP 網路配置（`/ip/dhcp-server/network`）中設定的 **domain** 值。此域必須已作為區域存在於 DNS 靜態條目（`/ip/dns/static`）中，或由路由器的 DNS 服務處理。DHCP 伺服器不會自動建立父區域。

:::

### 租約 {#leases}

**子選單：** `/ip/dhcp-server/lease`

DHCP 伺服器 lease 子選單用於監控和管理伺服器租約。已發出的租約在此處顯示為動態條目。你還可以新增靜態租約，以向特定用戶端（由 MAC 地址標識）分配特定 IP 地址。

通常，DHCP 租約的分配如下：

- 未使用的租約處於 "waiting" 狀態。
- 如果用戶端請求 IP 地址，伺服器選擇一個。
- 如果用戶端收到靜態分配的地址，租約變為 offered，然後以相應的租約時間繫結。
- 如果用戶端收到動態地址（從 IP 地址池中獲取），路由器傳送 ping 封包並等待應答 0.5 秒。在此期間，租約標記為 testing。
- 如果地址沒有響應，租約變為 offered，然後以相應的租約時間繫結。
- 在其他情況下，租約在租約時間內變為 busy（有一個命令可以重新測試所有 busy 地址），並且用戶端的請求仍未得到應答（用戶端將很快再次嘗試）。

用戶端可以釋放租用的地址。動態租約被移除，分配的地址返回到地址池。但靜態租約將變為 busy，直到用戶端重新獲取該地址。

:::warning
靜態分配的 IP 地址不會被探測！

:::

| 屬性 | 描述 |
| :-- | :-- |
| **address** (*IP*; 預設：**0.0.0.0**) | 指定靜態租約的 IP 地址（或 IP 地址池）。如果設定為 **0.0.0.0** - 將使用 DHCP 伺服器中的地址池 |
| **address-lists** (*string*; 預設：**none**) | 如果租約繫結，地址將新增到的地址列表。 |
| **agent-circuit-id** (*hex string;*預設 **none***)* | 如果指定，值必須與請求的 Option 82 Agent Circuit ID 子選項匹配。 |
| **agent-remote-id** (*hex string;*預設 **none***)* | 如果指定，值必須與請求的 Option 82 Agent Remote ID 子選項匹配。 |
| **allow-dual-stack-queue** (*yes \| no*; 預設：**yes**) | 為 IPv4 和 IPv6 地址建立單個簡單佇列條目，並使用 MAC 地址和 DUID 進行標識。需要 [IPv6 DHCP 伺服器](./dhcp.md#dhcpv6-server) 也啟用此選項才能正常工作。 |
| **always-broadcast** (*yes \| no*; 預設：**no**) | 更改是否強制廣播 DHCP 回覆：no - 根據用戶端的廣播標誌傳送回覆。如果伺服器連續傳送三個提議，第三個和第四個提議將作為廣播發送；yes - 即使用戶端未指定廣播標誌，回覆也始終廣播。 |
| **block-access** (*yes \| no*; 預設：**no**) | 阻止此用戶端訪問 |
| **client-id** (*string*; 預設：**none**) | 如果指定，必須與請求的 DHCP 'client identifier' 選項匹配 |
| **dhcp-option** (*string*; 預設：**none**) | 從[選項列表](./dhcp.md#dhcp-options-1)新增其他 DHCP 選項。 |
| **dhcp-option-set** (*string*; 預設：**none**) | 新增附加的 DHCP 選項集。 |
| **insert-queue-before** (*bottom \| first \| name*; 預設：**first**) | 指定將具有 rate-limit 引數設定的靜態 DHCP 租約的動態簡單佇列條目放置在何處。 |
| **lease-time** (*time*; 預設：**0s**) | 用戶端可以使用該地址的時間。如果設定為 **0s**，租約將永不過期。 |
| **mac-address** (*MAC*; 預設：**00:00:00:00:00:00**) | 如果指定，必須與用戶端的 MAC 地址匹配 |
| **parent-queue** (*string \| none*; 預設：**none**) | 為此租約動態建立的佇列將配置為指定父佇列的子佇列。 |
| **queue-type** (*default, ethernet-default, multi-queue-ethernet-default, pcq-download-default, synchronous-default, default-small, hotspot-default, only-hardware-queue, pcq-upload-default, wireless-default*) | 可分配給特定租約的佇列型別 |
| **rate-limit** (*integer[/integer] [integer[/integer] [integer[/integer] [integer[/integer]]]];*; 預設：) | 新增動態簡單佇列，將 IP 的頻寬限制為指定速率。要求租約為靜態。格式為：rx-rate[/tx-rate] [rx-burst-rate[/tx-burst-rate] [rx-burst-threshold[/tx-burst-threshold] [rx-burst-time[/tx-burst-time]]]]。所有速率應為數字，可帶 'k'（1,000 倍）或 'M'（1,000,000 倍）。如果未指定 tx-rate，則 rx-rate 也用作 tx-rate。tx-burst-rate、tx-burst-threshold 和 tx-burst-time 同理。如果 rx-burst-threshold 和 tx-burst-threshold 均未指定（但指定了 burst-rate），則 rx-rate 和 tx-rate 用作突發閾值。如果 rx-burst-time 和 tx-burst-time 均未指定，則預設使用 1s。 |
| ***routes*** ([dst-address/mask] [gateway] [distance]; 預設：***none***) | 用戶端連線時在伺服器上顯示的路由。可以指定多個路由，用逗號分隔。此設定對 OpenVPN 將被忽略。 |
| **server** (*string*) | 服務此用戶端的伺服器名稱 |
| **use-src-mac**(*yes \| no*; 預設：**no**) | 設定此選項後，伺服器使用源 MAC 地址而不是接收到的 CHADDR 來分配地址。 |
| **status** (waiting \| testing \| declined \| offered \| bound \| authorizing \| conflict) | 顯示 DHCP `lease` 的狀態：waiting - 等待靜態 DHCP 租約繫結testing - 檢查 ARP 衝突declined - DHCP 用戶端回覆 decline 封包offered - 伺服器向 DHCP 用戶端提供地址，但尚未收到 DHCP 請求回覆bound - DHCP 用戶端接受 DHCP 租約authorizing - 與 RADIUS 通訊conflict - 檢測到 ARP 衝突 |

#### 選單專用命令 {#menu-specific-commands-2}

|  |  |
| :-- | :-- |
| **check-status** (*id*) | 檢查給定 busy（狀態為 conflict 或 declined）動態租約的狀態，並在無響應時釋放它 |
| **make-static** (*id*) | 將動態租約轉換為靜態租約 |
| **send-reconfigure** (*id*) | 傳送 Reconfigure（*forcerenew*）訊息 |

#### 儲存配置 {#store-configuration}

**子選單：** `/ip/dhcp-server/config`

**將租約儲存到磁碟：** 配置 DHCP 租約儲存到磁碟的頻率。如果每次租約更改都儲存到磁碟，將發生大量磁碟寫入，這對 Compact Flash 非常不利（尤其是租約時間非常短時）。為了最小化磁碟寫入，所有更改每隔 store-leases-disk 秒儲存到磁碟。此外，租約在正常關機和重啟時始終儲存到磁碟。

對租約的手動更改——新增/移除靜態租約、移除動態租約——將導致此租約的更改推送到儲存。

**Accounting：** DHCP 伺服器配置中的 accounting 引數啟用或停用 DHCP 租約計費。啟用計費後，DHCP 伺服器記錄有關 IP 地址分配和租約續租的資訊。此資訊可用於跟蹤和監控網路使用情況、分析流量模式或生成 IP 地址分配報告。

**Interim-update：** interim-update 引數確定 DHCP 伺服器是否在租約期間向計費伺服器傳送定期更新。這些更新提供有關租約持續時間、使用情況和其他相關詳細資訊。啟用臨時更新可以更準確地跟蹤租約活動。

**Radius-password：** radius-password 引數用於設定 RADIUS（遠端認證撥入使用者服務）伺服器的密碼。RADIUS 是一種網路協定，通常用於為網路訪問提供集中認證、授權和計費。將 DHCP 伺服器配置為與 RADIUS 伺服器通訊以進行認證或計費時，需要指定正確的密碼以建立安全連線。此引數確保 DHCP 伺服器可以使用指定密碼向 RADIUS 伺服器進行認證。

#### 速率限制 {#rate-limiting}

可以透過使用 DHCPv4 租約為特定 IPv4 地址設定頻寬。這可以透過在 DHCPv4 租約本身上設定速率限制來完成；這樣做後，將為與該 DHCPv4 租約對應的 IPv4 地址新增動態簡單佇列規則。透過使用 *rate-limit* 引數，可以方便地限制使用者的頻寬。

:::warning
為使任何佇列正常工作，流量不得被 FastTrack 處理，請確保你的防火牆不會對要限制的流量進行 FastTrack。

:::

首先，將 DHCPv4 租約設為靜態，否則將無法為 DHCPv4 租約設定速率限制：

```ros
[admin@MikroTik] > /ip/dhcp-server/lease/print 
Flags: X - disabled, R - radius, D - dynamic, B - blocked 
 #   ADDRESS               MAC-ADDRESS       HOST-NAME               SERVER               RATE-LIMIT               STATUS 
 0 D 192.168.88.254        6C:3B:6B:7C:41:3E MikroTik                DHCPv4_Server                                 bound 

[admin@MikroTik] > /ip/dhcp-server/lease/make-static 0

[admin@MikroTik] > /ip/dhcp-server/lease/print 
Flags: X - disabled, R - radius, D - dynamic, B - blocked 
 #   ADDRESS               MAC-ADDRESS       HOST-NAME               SERVER               RATE-LIMIT               STATUS 
 0   192.168.88.254        6C:3B:6B:7C:41:3E MikroTik                DHCPv4_Server                                 bound
```

然後可以為 DHCPv4 租約設定速率，這將建立一個新的動態簡單佇列條目：

```ros
[admin@MikroTik] > /ip/dhcp-server/lease/set 0 rate-limit=10M/10M

[admin@MikroTik] > /queue/simple/print 
Flags: X - disabled, I - invalid, D - dynamic 
 0  D name="dhcp-ds<6C:3B:6B:7C:41:3E>" target=192.168.88.254/32 parent=none packet-marks="" priority=8/8 queue=default-small/default-small limit-at=10M/10M max-limit=10M/10M burst-limit=0/0 burst-threshold=0/0 burst-time=0s/0s 
      bucket-size=0.1/0.1
```

:::warning
預設啟用 allow-dual-stack-queue；這將為 DHCPv6 繫結和 DHCPv4 租約新增單個動態簡單佇列條目。未啟用此選項時，將為 IPv6 和 IPv4 新增單獨的動態簡單佇列條目。

:::

如果啟用了 *allow-dual-stack-queue*，則將建立一個包含 IPv4 和 IPv6 地址的單個動態簡單佇列條目：

```ros
[admin@MikroTik] > /queue/simple/print 
Flags: X - disabled, I - invalid, D - dynamic 
 0  D name="dhcp-ds<6C:3B:6B:7C:41:3E>" target=192.168.88.254/32,fdb4:4de7:a3f8:418c::/66 parent=none packet-marks="" priority=8/8 queue=default-small/default-small limit-at=10M/10M max-limit=10M/10M burst-limit=0/0 burst-threshold=0/0 
      burst-time=0s/0s bucket-size=0.1/0.1 
```

### 網路 {#network}

**子選單：** `/ip/dhcp-server/network`

## 屬性 {#properties-2}

| 屬性 | 描述 |
| :-- | :-- |
| **address** (*IP/netmask*; 預設：) | DHCP 伺服器將從中租用地址的網路 |
| **boot-file-name** (*string*; 預設：) | 引導檔名 |
| **caps-manager** (*string*; 預設：) | 一個或多個 CAPsMAN 系統管理器的逗號分隔 IP 地址列表。將使用 DHCP Option 138（capwap）。 |
| **dhcp-option** (*string*; 預設：) | 從選項列表新增其他 DHCP 選項。 |
| **dhcp-option-set** (*string*; 預設：) | 新增附加的 DHCP 選項集。 |
| **dns-none** (*yes \| no*; 預設：**no**) | 如果設定，DHCP 伺服器將不會把路由器上配置的 DNS 伺服器傳遞給 DHCP 用戶端。 |
| **dns-server** (*string*; 預設：) | 將傳遞給 DHCP 用戶端的 DNS 伺服器。可以指定兩個逗號分隔的 DNS 伺服器，分別用作 DHCP 用戶端的主 DNS 伺服器和輔助 DNS 伺服器。預設情況下，如果沒有配置 DNS 伺服器，則來自 IP>DNS 的路由器動態 DNS 伺服器將傳遞給 DHCP 用戶端；如果沒有配置動態 DNS 伺服器，則來自 IP>DNS 的路由器靜態 DNS 伺服器將傳遞給 DHCP 用戶端。 |
| **domain** (*string*; 預設：) | DHCP 用戶端將把它用作網路介面卡的 'DNS domain' 設定。 |
| **gateway** (*IP*; 預設：**0.0.0.0**) | DHCP 用戶端使用的預設閘道器。 |
| **netmask** (*integer: 0..32*; 預設：**0**) | DHCP 用戶端使用的實際網路掩碼。如果設定為 '0' - 將使用網路地址中的網路掩碼。 |
| **next-server** (*IP*; 預設：) | 引導時要使用的下一個伺服器的 IP 地址。 |
| **ntp-none** (*yes \| no*; 預設：**no**) | 如果設定，DHCP 伺服器將不會把路由器上配置的 NTP 伺服器傳遞給 DHCP 用戶端。 |
| **ntp-server** (*IP*; 預設：) | DHCP 用戶端將把這些用作預設 NTP 伺服器。可以指定兩個逗號分隔的 NTP 伺服器，分別用作 DHCP 用戶端的主 NTP 伺服器和輔助 NTP 伺服器 |
| **wins-server** (*IP*; 預設：) | Windows DHCP 用戶端將把這些用作預設 WINS 伺服器。可以指定兩個逗號分隔的 WINS 伺服器，分別用作 DHCP 用戶端的主 WINS 伺服器和輔助 WINS 伺服器 |

### RADIUS 支援 {#radius-support}

自 RouterOS v6.43 起，可以使用 RADIUS 為每個租約分配速率限制。為此，需要從 RADIUS 伺服器為租約傳遞 Mikrotik-Rate-Limit 屬性。要實現這一點，首先需要將 DHCPv4 伺服器設定為使用 RADIUS 分配租約。以下是設定示例：

```ros
/radius
add address=10.0.0.1 secret=VERYsecret123 service=dhcp
/ip/dhcp-server
set dhcp1 use-radius=yes
```

之後，需要告訴 RADIUS 伺服器傳遞 Mikrotik-Rate-Limit 屬性。如果你使用 FreeRADIUS 與 MySQL，則需要為 DHCPv4 用戶端使用的 MAC 地址在 **radcheck** 和 **radreply** 表中新增相應條目。以下是表條目示例：

```routeros
INSERT INTO `radcheck` (`username`, `attribute`, `op`, `value`) VALUES
('00:0C:42:00:D4:64', 'Auth-Type', ':=', 'Accept'),

INSERT INTO `radreply` (`username`, `attribute`, `op`, `value`) VALUES
('00:0C:42:00:D4:64', 'Framed-IP-Address', '=', '192.168.88.254'),
('00:0C:42:00:D4:64', 'Mikrotik-Rate-Limit', '=', '10M'),
```

### 警報 {#alerts}

要儘快發現網路中出現的任何惡意 DHCP 伺服器，可以使用 DHCP Alert 工具。它將監控介面上的所有 DHCP 回覆，並檢查此回覆是否來自有效的 DHCP 伺服器。如果檢測到來自未知 DHCP 伺服器的回覆，將觸發警報：

```ros
[admin@MikroTik] /ip/dhcp-server/alert> /log/print
00:34:23 dhcp,critical,error,warning,info,debug dhcp alert on Public:
    discovered unknown dhcp server, mac 00:02:29:60:36:E7, ip 10.5.8.236
[admin@MikroTik] /ip/dhcp-server/alert>
```

當系統發出有關惡意 DHCP 伺服器的警報時，它可以執行自定義指令碼。

由於 DHCP 回覆可以是單播，惡意 DHCP 檢測器可能根本收不到發往其他 DHCP 用戶端的任何提議。為解決此問題，惡意 DHCP 檢測器也會充當 DHCP 用戶端——它每分鐘傳送一次 DHCP discover 請求。

:::warning
不建議在配置為 DHCP 用戶端的裝置上使用 DHCP 警報。由於警報本身會生成 DHCP 發現數據包，可能影響 DHCP 用戶端自身的執行。僅在 DHCP 伺服器或使用靜態 IP 地址的裝置上使用此功能。

:::

**子選單：** `/ip/dhcp-server/alert`

## 屬性 {#properties-3}

| 屬性 | 描述 |
| :-- | :-- |
| **alert-timeout**(none \| time; 預設：1h) | 警報被遺忘的時間。如果在該時間之後檢測到同一伺服器，將生成新警報。如果設定為 **none**，超時將永不過期。 |
| **interface** (*string*; 預設：) | 執行惡意 DHCP 伺服器查詢器的介面。 |
| **on-alert** (*string*; 預設：) | 檢測到未知 DHCP 伺服器時執行的指令碼。 |
| **valid-server**(*string*; 預設：) | 有效 DHCP 伺服器的 MAC 地址列表。 |

## 只讀屬性 {#read-only-properties-2}

| 屬性 | 描述 |
| :-- | :-- |
| **unknown-server**(*string*) | 檢測到的未知 DHCP 伺服器的 MAC 地址列表。伺服器在 alert-timeout 後從此列表中移除。 |

## 選單專用命令 {#menu-specific-commands-3}

| 屬性 | 描述 |
| :-- | :-- |
| **reset-alert**(*id*) | 清除介面上的所有警報 |

### DHCP 選項 {#dhcp-options-1}

**子選單：** `/ip/dhcp-server/option`

藉助 DHCP Option 列表，可以為 DHCP 伺服器定義要通告的其他自定義選項。選項優先順序如下：

- radius。
- lease。
- server。
- network。

這是填充用戶端選項請求的順序。

根據 DHCP 協定，只有當 DHCP 用戶端請求某個引數並在 DHCP 請求的 Parameter-List（程式碼 55）屬性中指定相應程式碼時，才會將該引數返回給用戶端。如果程式碼未包含在 Parameter-List 屬性中，DHCP 伺服器不會將其傳送給 DHCP 用戶端，但**從 RouterOS v7.1rc5 起，即使 DHCP-client 不請求此類引數，也可以從伺服器端強制傳送 DHCP 選項**：

```ros
/ip/dhcp-server/option/set force=yes
```

**屬性**

| 屬性 | 描述 |
| :-- | :-- |
| **code** (*integer:1..254*; 預設：) | dhcp 選項程式碼。所有程式碼可在 '[link](http://www.iana.org/assignments/bootp-dhcp-parameters)' 獲取。 |
| **name** (*string*; 預設：) | 選項的描述性名稱 |
| **value** (*string*; 預設：) | 引數值。選項可用的資料型別為：'test' -&gt; ASCII 轉十六進位制 0x74657374'10.10.10.10' -&gt; Unicode IP 轉十六進位制 0x0a0a0a0as'10.10.10.10' -&gt; ASCII 轉十六進位制 0x31302e31302e31302e3130s'160' -&gt; ASCII 轉十六進位制 0x313630'10' -&gt; 十進位制轉十六進位制 0x0a0x0a0a -&gt; 不轉換$(VARIABLE) -&gt; 硬編碼值 RouterOS 有可使用的預定義變數： HOSTNAME - 用戶端主機名RADIUS_MT_STR1 - 來自 radius MT attr nr. 24RADIUS_MT_STR2 - 來自 radius MT attr nr. 25REMOTE_ID - 代理 remote-idNETWORK_GATEWAY - '`/ip/dhcp-server/network`' 中的第一個閘道器，請注意，如果從 lease 使用，此選項將不起作用 現在還可以將資料型別組合為一個，例如："0x01'vards'$(HOSTNAME)"  例如，如果 HOSTNAME 為 'kvm'，則原始值將為 0x0176617264736b766d。 |
| **raw-value** (*HEX string* ) | 只讀欄位，顯示原始 DHCP 選項值（實際傳送的格式） |
| force  | |

#### DHCP 選項集 {#dhcp-option-sets}

**子選單：** `/ip/dhcp-server/option/sets`

此選單允許將多個選項組合到選項集中，之後可用於覆蓋預設 DHCP 伺服器選項集。

#### 示例 {#example}

**無類路由**

無類路由在用戶端的路由表中新增指定路由。在我們的示例中，它將新增：

- dst-address=160.0.0.0/24 gateway=10.1.101.1
- dst-address=0.0.0.0/0 gateway=10.1.101.1

根據 RFC 3442：第一部分是網路掩碼（"18" = 網路掩碼 /24）。第二部分是目標網路的重要部分（"A00000" = 160.0.0）。第三部分是閘道器 IP 地址（"0A016501" = 10.1.101.1）。然後是預設路由的部分，目標網路掩碼（0x00 = 0.0.0.0/0），後跟預設路由（0x0A016501 = 10.1.101.1）

```ros
/ip/dhcp-server/option
add code=121 name=classless value=0x18A000000A016501000A016501
/ip/dhcp-server/network
set 0 dhcp-option=classless
```

結果：

```ros
[admin@MikroTik] /ip/route> print
Flags: X - disabled, A - active, D - dynamic, C - connect, S - static, r - rip, b - bgp, o - ospf,
m - mme, B - blackhole, U - unreachable, P - prohibit
 #      DST-ADDRESS        PREF-SRC        GATEWAY            DISTANCE
 0 ADS  0.0.0.0/0                          10.1.101.1         0
 1 ADS  160.0.0.0/24                       10.1.101.1         0
```

更穩健的方法是使用內建變數。上一個示例可以重寫為：

```ros
/ip/dhcp-server/option
add name=classless code=121 value="0x18A00000\$(NETWORK_GATEWAY)0x00\$(NETWORK_GATEWAY)"
```

**自動代理配置**

```ros
/ip/dhcp-server/option 
  add code=252 name=auto-proxy-config value="'https://autoconfig.something.lv/wpad.dat'"
```

### 選項匹配器 {#option-matcher}

選項匹配器允許透過任意 DHCP 選項標識 DHCP 用戶端，並從特定 IP 地址池分配 IP 地址。

可以執行 `exact`（提供的 *value* 應完全匹配）或 `substring` 匹配（將在選項字串中的任何位置查詢 *value* 匹配——可以匹配開頭、中間或末尾的值）。

子字串匹配在值可能因終端裝置而變化的情況下很有用，例如，如果裝置傳送的 class-identifier 不僅包含廠商資訊，還包含確切的 MAC 或其他附加資訊。

:::info
可以為同一個選項定義兩個子字串匹配，例如一個匹配 "ABC"，另一個匹配 "ABCDE"。如果有一個值為 "ABCDEF" 的 DHCP 選項，兩個條目都會匹配它，但將隨機選擇應用哪個匹配器。

:::

:::warning
具有靜態租約的用戶端將繼續收到其靜態地址，即使被選項匹配器匹配也是如此。

:::

#### **屬性** {#properties-4}

| 屬性 | 描述 |
| :-- | :-- |
| **address-pool** (*string \| static-only*; 預設：**static-only**) | 用於為用戶端獲取 IP 地址的 IP 地址池。如果設定為 **static-only**，則只允許具有靜態租約的用戶端（在 lease 子選單中新增）。 |
| **code** (*integer:1..254*; 預設：) | DHCP 選項程式碼。所有程式碼可在 '[link](http://www.iana.org/assignments/bootp-dhcp-parameters)' 獲取。 |
| **comment** (*string*; 預設：) | 選項匹配器的簡短描述。 |
| **disabled** (*yes \| no*; 預設：**no**) | 專案是否被停用 |
| **matching-type** (*exact \| substring*; 預設：) | 匹配方法：exact - 選項應完全匹配該值；substring - 值可以匹配選項字串中的任何位置——開頭、中間或末尾。 |
| **name** (*string*; 預設：) | 選項匹配器的描述性名稱。 |
| **option-set** (*name \| none*; 預設：**none**) | 在 Option Sets 選單中定義的自定義 DHCP 選項集。 |
| **server** (*string* \| *all*; 預設：) | 服務此選項匹配器的伺服器名稱。 |
| **value** (*string*; 預設：) | 將在選項中搜尋的值。  值可用的資料型別為：string；HEX。 |

#### 選項匹配器示例 {#option-matcher-examples}

按 *exact* Vendor class identifier（DHCP 選項 60）匹配 *dhcp1* 伺服器用戶端，並從 *pool1* 分配地址：

```ros
/ip/dhcp-server/matcher
add address-pool=pool1 code=60 matching-type=exact name=test1 server=dhcp1 value=android-dhcp-11
```

按配置為十六進位制值的 *exact* Client Id（DHCP 選項 61）匹配所有 DHCP 伺服器上的用戶端，並從 *pool2* 分配地址：

```ros
/ip/dhcp-server/matcher
add address-pool=pool2 code=61 matching-type=exact name=test2 server=all value=0x016c3b6bed8364
```

按 Hostname（DHCP 選項 12）*部分*匹配 *dhcp2* 伺服器用戶端，並從 *pool3* 分配地址：

```ros
/ip/dhcp-server/matcher
add address-pool=pool3 code=12 matching-type=substring name=test3 server=dhcp2 value=MikroTik
```

### 配置示例 {#configuration-examples-2}

#### 設定 {#setup}

要簡單配置 DHCP 伺服器，可以使用 `setup` 命令。

首先，在介面上配置 IP 地址：

```ros
[admin@MikroTik] > /ip/address/add address=192.168.88.1/24 interface=ether3 disabled=no
```

然後使用 `setup`，該命令將自動詢問必要引數：

```ros
[admin@MikroTik] > /ip/dhcp-server/setup 
Select interface to run DHCP server on 

dhcp server interface: ether3
Select network for DHCP addresses 

dhcp address space: 192.168.88.0/24
Select gateway for given network 

gateway for dhcp network: 192.168.88.1
Select pool of ip addresses given out by DHCP server 

addresses to give out: 192.168.88.2-192.168.88.254
Select DNS servers 

dns servers: 10.155.126.1,10.155.0.1,                               
Select lease time 

lease time: 10m
```

就這些。你已配置了一個活動的 DHCP 伺服器。

#### 手動配置 {#manual-configuration}

要手動配置 DHCP 伺服器以響應本地請求，必須配置以下內容：

- 用於分配地址的 **IP 地址池**。確保你的閘道器/DHCP 伺服器地址不在該地址池中。

```ros
/ip/pool/add name=dhcp_pool0 ranges=192.168.88.2-192.168.88.254
```

- 一個 **network**，指示 DHCP 伺服器將從中租用地址的子網，以及其他資訊，如閘道器、DNS 伺服器、NTP 伺服器、DHCP 選項等。

```ros
/ip/dhcp-server/network/add address=192.168.88.0/24 dns-server=192.168.88.1 gateway=192.168.88.1
```

- 在我們的情況下，裝置本身充當閘道器，因此我們將把 **address** 新增到橋接介面：

```ros
/ip/address/add address=192.168.88.1/24 interface=bridge1 network=192.168.88.0
```

- 最後，新增 **DHCP Server**，這裡我們將新增之前建立的地址 **pool**，並指定 DHCP 伺服器應在哪個 **interface** 上工作。

```ros
/ip/dhcp-server/add address-pool=dhcp_pool0 disabled=no interface=bridge1 name=dhcp1
```

## DHCPv6 伺服器 {#dhcpv6-server}

### 概述 {#summary-3}

**標準：** `RFC 3315, RFC 3633`

用戶端和伺服器標識使用單個 DUID；只有 IAID 會因用戶端所分配介面的不同而變化。

用戶端繫結會建立一個動態地址池，其超時設定為繫結的到期時間（注意，現在動態地址池可以有超時），每次繫結續租時都會更新。

當用戶端繫結到字首時，DHCP 伺服器會新增路由資訊，以瞭解如何到達所分配的字首。

### 常規 {#general}

**子選單：** `/ipv6/dhcp-server`

此子選單列出並允許配置 DHCP-PD 伺服器。

### DHCPv6 伺服器屬性 {#dhcpv6-server-properties}

| 屬性 | 描述 |
| :-- | :-- |
| **address-pool** (*enum \| static-only*; 預設：**static-only**) | 用於為用戶端獲取 IPv6 地址的 [IPv6 地址池](../cli-reference/ipv6/pool/index.md)，池的字首長度必須指定為 /128。 |
| **prefix-pool (*enum \| static-only*; 預設：static-only)** | 用於為用戶端獲取 IPv6 字首的 [IPv6 地址池](../cli-reference/ipv6/pool/index.md)。 |
| ****allow-dual-stack-queue****(*yes \| no*; 預設：****yes****) | 為 IPv4 和 IPv6 地址建立單個簡單佇列條目，並使用 MAC 地址和 DUID 進行標識。需要 IPv6 DHCP 伺服器也啟用此選項才能正常工作。 |
| **address-lists** (*string*; 預設：) | 逗號分隔的地址列表。伺服器發出的地址或字首將新增到這些列表中。 |
| **binding-script** (*string*; 預設：) | 在分配或取消分配繫結後執行的指令碼。可在指令碼中使用的內部 "global" 變數：bindingBound - 如果已繫結則設定為 "1"，否則設定為 "0"bindingServerName - dhcp 伺服器名稱bindingDUID - DUIDbindingAddress - 活動地址bindingPrefix - 活動字首 |
| **dhcp-option** (*string*; 預設：**none**) | 從[選項列表](./dhcp.md#dhcp-options-1)新增其他 DHCP 選項。 |
| **insert-queue-before** (*bottom \| first \| name*; 預設：**first**) | 指定將具有 rate-limit 引數設定的靜態 DHCP 租約的動態簡單佇列條目放置在何處。 |
| **parent-queue** (*string \| none*; 預設：**none**) | 為此租約動態建立的佇列將配置為指定父佇列的子佇列。 |
| **preference** (*integer [0..255]*; 預設：255) | 定義多個伺服器響應時用戶端選擇中的伺服器優先順序。 |
| **disabled** (*yes \| no*; 預設：**no**) | DHCP-PD 伺服器是否參與字首分配過程。 |
| **interface** (*string*; 預設：) | 伺服器將執行的介面。 |
| **lease-time** (*time*; 預設：**3d**) | 用戶端可以使用所分配地址的時間。用戶端將在此時間的一半後嘗試續租此地址，並在時間限制到期後請求新地址。 |
| **rapid-commit (**yes \| no; 預設：**yes)** | 啟用兩訊息交換（Solicit 和 Reply），透過跳過標準四訊息過程來加快用戶端配置。 |
| ****route-distance****(*integer [0..255]*; 預設：**1**) | 指定為指向 DHCPv6 用戶端的動態安裝路由設定的距離。 |
| **use-radius** (*yes \| no \| accounting*; 預設：**no**) | 是否使用 RADIUS 伺服器：no - 不使用 RADIUS；yes - 使用 RADIUS 進行計費和租約；accounting - 僅使用 RADIUS 進行計費。 |
| ****use-reconfigure****(*yes \| no*; 預設：**no**) | 允許伺服器向用戶端傳送 Reconfigure 訊息，提示它們續租或更新配置而無需等待租約到期。 |
| **name** (*string*; 預設：) | 引用名稱 |
| **address-lists** (*string*; 預設：**none**) | 如果租約繫結，地址將新增到的地址列表。 |
| **ignore-ia-na-bindings** (*yes \| no*; 預設：**no**) | 不回覆 DHCPv6 地址請求，僅處理字首。如果沒有此設定，即使伺服器未配置 address-pool，它也必須回覆用戶端沒有可用地址。這可能導致 DHCPv6 用戶端在迴圈中請求地址和字首的情況。 |

#### 只讀屬性 {#read-only-properties-3}

| 屬性 | 描述 |
| :-- | :-- |
| **dynamic** (*yes \| no*) |  |
| **invalid** (*yes \| no*) |  |

### 繫結 {#bindings}

**子選單：** `/ipv6/dhcp-server/binding`

DUID 僅用於動態繫結，因此如果它發生變化，用戶端將收到與之前不同的字首。

| 屬性 | 描述 |
| :-- | :-- |
| **address** (*IPv6 prefix*; 預設：) | 將分配給用戶端的 IPv6 字首 |
| **allow-dual-stack-queue** (*yes \| no*; 預設：**yes**) | 為 IPv4 和 IPv6 地址建立單個簡單佇列條目，並使用 MAC 地址和 DUID 進行標識。需要 IPv4 DHCP 伺服器也啟用此選項才能正常工作。 |
| **comment** (*string*; 預設：) | 專案的簡短描述。 |
| **disabled** (*yes \| no*; 預設：**no**) | 專案是否被停用 |
| **dhcp-option** (*string*; 預設：) | 從選項列表新增其他 DHCP 選項。 |
| **life-time** (*time*; 預設：**3d**) | 繫結到期後的時間段。 |
| **duid** (*hex string*; 預設：) | DUID 值。只能以十六進位制格式指定。 |
| **iaid** (*integer [0..4294967295]*; 預設：) | 身份關聯識別符號，Client ID 的一部分。 |
| **prefix-pool** (*string*; 預設：) | 向 DHCPv6 用戶端通告的字首池。 |
| **rate-limit** (*integer[/integer] [integer[/integer] [integer[/integer] [integer[/integer]]]]*; 預設：) | 新增動態簡單佇列，將 IP 的頻寬限制為指定速率。要求租約為靜態。格式為：rx-rate[/tx-rate] [rx-burst-rate[/tx-burst-rate] [rx-burst-threshold[/tx-burst-threshold] [rx-burst-time[/tx-burst-time]]]]。所有速率應為數字，可帶 'k'（1,000 倍）或 'M'（1,000,000 倍）。如果未指定 tx-rate，則 rx-rate 也用作 tx-rate。tx-burst-rate、tx-burst-threshold 和 tx-burst-time 同理。如果 rx-burst-threshold 和 tx-burst-threshold 均未指定（但指定了 burst-rate），則 rx-rate 和 tx-rate 用作突發閾值。如果 rx-burst-time 和 tx-burst-time 均未指定，則預設使用 1s。 |
| **server** (*string \| all*; 預設：**all**) | 伺服器名稱。如果設定為 **all**，則繫結應用於所有已建立的 DHCP-PD 伺服器。 |
| ia-type  | |
| address-lists  | |
| insert-queue-before  | |
| parent-queue  | |
| queue-type  | |

## 只讀屬性 {#read-only-properties-4}

| 屬性 | 描述 |
| :-- | :-- |
| **dynamic** (*yes \| no*) | 專案是否為動態建立。 |
| **expires-after** (*time*) | 繫結到期後的時間段。 |
| **last-seen** (*time*) | 自上次看到用戶端以來的時間段。 |
| **status** (*waiting \| offered \| bound*) | 可能有三種狀態值：waiting - 如果未使用，則顯示用於靜態繫結。對於動態繫結，如果以前使用過，則顯示此狀態。伺服器將等待 10 分鐘以允許舊用戶端獲取此繫結，否則繫結將被清除，字首將提供給其他用戶端。offered - 如果收到 solicit 訊息，並且伺服器以 advertise 訊息響應，但未收到請求。在此狀態下，用戶端有 2 分鐘時間獲取此繫結，否則它將被釋放，對於靜態繫結則狀態變為 waiting。bound - 當前已繫結。 |
| **reconfigure-key** (string) | 重新配置認證金鑰 |
| **reconfigure-last-sent**(integer) | 已傳送的 Reconfigure（*forcerenew*）訊息數量 |
| **reconfigure-status** |  |
| active-server  | |
| client-address  | |
例如，動態分配的 /62 字首

```ros
[admin@RB493G] /ipv6/dhcp-server/binding> print detail
 Flags: X - disabled, D - dynamic 
0 D address=2a02:610:7501:ff00::/62 duid="1605fcb400241d1781f7" iaid=0
 server=local-dhcp life-time=3d status=bound expires-after=2d23h40m10s 
last-seen=19m50s 
1 D address=2a02:610:7501:ff04::/62 duid="0019d1393535" iaid=2 
server=local-dhcp life-time=3d status=bound expires-after=2d23h43m47s 
last-seen=16m13s
```

## 選單專用命令 {#menu-specific-commands-4}

| 屬性 | 描述 |
| :-- | :-- |
| **make-static** () | 將動態繫結設為靜態。 |
| **send-reconfigure** (*id*) | 傳送 Reconfigure（*forcerenew*）訊息 |

#### 速率限制 {#rate-limiting-1}

可以透過使用 DHCPv6 繫結為特定 IPv6 地址設定頻寬。這可以透過在 DHCPv6 繫結本身上設定速率限制來完成；這樣做後，將為與該 DHCPv6 繫結對應的 IPv6 地址新增動態簡單佇列規則。透過使用 `rate-limit` 引數，可以方便地限制使用者的頻寬。

:::warning
為使任何佇列正常工作，流量不得被 FastTrack 處理，請確保你的防火牆不會對要限制的流量進行 FastTrack。

:::

首先，將 DHCPv6 繫結設為靜態；否則將無法為 DHCPv6 繫結設定速率限制：

```ros
[admin@MikroTik] > /ipv6/dhcp-server/binding/print 
Flags: X - disabled, D - dynamic 
# ADDRESS DUID SERVER STATUS 
0 D fdb4:4de7:a3f8:418c::/66 0x6c3b6b7c413e DHCPv6_Server bound

[admin@MikroTik] > /ipv6/dhcp-server/binding/make-static 0

[admin@MikroTik] > /ipv6/dhcp-server/binding/print
Flags: X - disabled, D - dynamic 
# ADDRESS DUID SERVER STATUS 
0 fdb4:4de7:a3f8:418c::/66 0x6c3b6b7c413e DHCPv6_Server bound 

```

然後可以為 DHCPv6 繫結設定速率，這將建立一個新的動態簡單佇列條目：

```ros
[admin@MikroTik] > /ipv6/dhcp-server/binding/set 0 rate-limit=10M/10 
[admin@MikroTik] > /queue/simple/print 
Flags: X - disabled, I - invalid, D - dynamic 
0 D name="dhcp<6c3b6b7c413e fdb4:4de7:a3f8:418c::/66>" target=fdb4:4de7:a3f8:418c::/66 parent=none packet-marks="" priority=8/8 queue=default
-small/default-small limit-at=10M/10M max-limit=10M/10M burst-limit=0/0 
burst-threshold=0/0 burst-time=0s/0s bucket-size=0.1/0.1
```

:::warning
預設啟用 `allow-dual-stack-queue`；這將為 DHCPv6 繫結和 DHCPv4 租約新增單個動態簡單佇列條目。未啟用此選項時，將為 IPv6 和 IPv4 新增單獨的動態簡單佇列條目。

:::

如果啟用了 `allow-dual-stack-queue`，則將建立一個包含 IPv4 和 IPv6 地址的單個動態簡單佇列條目：

```ros
[admin@MikroTik] > /queue/simple/print 
Flags: X - disabled, I - invalid, D - dynamic
 0 D name="dhcp-ds<6C:3B:6B:7C:41:3E>" target=192.168.1.200/32,fdb4:4de7:a3f8:418c::/66 parent=none packet-marks="" priority=8/8 queue=default
-small/default-small limit-at=10M/10M max-limit=10M/10M 
burst-limit=0/0 burst-threshold=0/0 burst-time=0s/0s bucket-size=0.1/0.1
```

### RADIUS 支援 {#radius-support-1}

自 RouterOS v6.43 起，可以使用 RADIUS 為每個 DHCPv6 繫結分配速率限制。為此，需要從 RADIUS 伺服器為 DHCPv6 繫結傳遞 Mikrotik-Rate-Limit 屬性。要實現這一點，首先需要將 DHCPv6 伺服器設定為使用 RADIUS 分配繫結。以下是設定示例：

```ros
/radius 
add address=10.0.0.1 secret=VERYsecret123 service=dhcp 
/ipv6/dhcp-server 
set dhcp1 use-radius=yes
```

之後，需要告訴 RADIUS 伺服器傳遞 Mikrotik-Rate-Limit 屬性。如果你使用 FreeRADIUS 與 MySQL，則需要為 DHCPv6 用戶端使用的 MAC 地址在 **radcheck** 和 **radreply** 表中新增相應條目。以下是表條目示例：

```ros
INSERT INTO `radcheck` (`username`, `attribute`, `op`, `value`) VALUES 
('000c4200d464', 'Auth-Type', ':=', 'Accept'),
 INSERT INTO `radreply` (`username`, `attribute`, `op`, `value`) VALUES 
('000c4200d464', 'Delegated-IPv6-Prefix', '=', 'fdb4:4de7:a3f8:418c::/66'), 
('000c4200d464', 'Mikrotik-Rate-Limit', '=', '10M');
```

:::warning
預設啟用 allow-dual-stack-queue，如果 IPv4 租約中的 MAC 地址（或 DUID，如果 DHCPv4 用戶端支援 RFC4361 中的 `Node-specific Client Identifiers`）匹配，將新增單個動態佇列條目；但 DHCPv6 用戶端的 DUID 並不總是基於執行 DHCPv6 用戶端的介面的 MAC 地址，DUID 是按裝置生成的。因此，可能不會建立單個動態佇列條目，而是建立單獨的動態佇列條目。

:::

### 配置示例 {#configuration-example}

#### 啟用 IPv6 字首委派 {#enabling-ipv6-prefix-delegation}

假設我們已經有一個執行中的 DHCP 伺服器。

要啟用 IPv6 字首委派，首先需要建立一個地址池：

```ros
/ipv6/pool/add name=myPool prefix=2001:db8:7501::/60 prefix-length=62

```

請注意，prefix-length 為 62 位，這意味著用戶端將從 /60 池中接收 /62 字首。

下一步是啟用 DHCP-PD：

```ros
/ipv6/dhcp-server/add name=myServer prefix-pool=myPool interface=local
```

要測試我們的伺服器，我們將在 Ubuntu 機器上設定 wide-dhcpv6：

- 安裝 wide-dhcpv6-client。
- 按上述內容編輯 "/etc/wide-dhcpv6/dhcp6c.conf"。

:::tip
你也可以將 RouterOS 用作 DHCP-PD 用戶端。

:::

```ros
interface eth2{
send ia-pd 0;
};

id-assoc pd {
prefix-interface eth3{
sla-id 1;
sla-len 2;
};
};
```

- 執行 DHCP-PD 用戶端。

```ros
sudo dhcp6c -d -D -f eth2
```

- 驗證字首已新增到：

```ros
mrz@bumba:/media/aaa$ ip -6 addr
 .. 
2: eth3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qlen 1000
 inet6 2001:db8:7501:1:200:ff:fe00:0/64 scope global
 valid_lft forever preferred_lft forever
 inet6 fe80::224:1dff:fe17:81f7/64 scope link
 valid_lft forever preferred_lft forever
```

- 可以將繫結設為特定用戶端的靜態繫結，以便它始終收到相同字首。

```ros
[admin@RB493G] /ipv6/dhcp-server/binding> print 
Flags: X - disabled, D - dynamic 
# ADDRESS DU IAID SER.. STATUS 0 D 2001:db8:7501:1::/62 16 0 loc.. bound 
[admin@RB493G] /ipv6/dhcp-server/binding> make-static 0
```

- DHCP-PD 還會在 IPv6 路由表中安裝指向所分配字首的路由：

```ros
[admin@RB493G] /ipv6/route> print
 Flags: X - disabled, A - active, D - dynamic, C - connect, S - static, r - rip, o - ospf, b - bgp, U - unreachable
 # DST-ADDRESS GATEWAY DISTANCE 
... 
2 ADS 2001:db8:7501:1::/62 fe80::224:1dff:fe17:8... 1
```

#### 啟用 IPv6 地址委派 {#enabling-ipv6-address-delegation}

DHCPv6 伺服器端的地址委派工作方式與配置字首伺服器幾乎完全相同。唯一的區別是，在配置中必須指定 address-pool 而不是 prefix-pool，並且此伺服器使用的地址池必須定義為使用 /128 字首長度。當然，你也可以建立一個僅分配靜態地址的伺服器，並跳過使用地址池。

```ros
[admin@MikroTik] > /ipv6/pool/print detail 
Flags: D - dynamic 
 0   name="myAddressPool" prefix=2001:db8:7501::/120 prefix-length=128 
[admin@MikroTik] > /ipv6/dhcp-server/print detail                                 
Flags: D - dynamic; X - disabled, I - invalid 
 0    name="myDHCP" interface=ether2 prefix-pool=static-only 
      address-pool=myAddressPool lease-time=3d rapid-commit=yes use-radius=no 
      preference=255 dhcp-option="" route-distance=1 use-reconfigure=no 
      address-lists="" duid="0x00030001b813f4840556" 
```

此配置已經足以與 DHCPv6 用戶端（例如 RouterOS 用戶端）配合工作。

```ros
[admin@MikroTik] > /ipv6/dhcp-client/print detail 
Flags: D - dynamic; X - disabled, I - invalid 
 0    interface=ether2 status=bound duid="0x00030001b123f48407f0" 
      dhcp-server-v6=fe80::ba69:f4af:fe14:558 request=address 
      add-default-route=no use-peer-dns=yes allow-reconfigure=no 
      dhcp-options="" pool-name="" pool-prefix-length=64 prefix-hint=::/0 
      prefix-address-lists="" dhcp-options="" 
      address=2001:db8:7501::, 2d23h59m51s
```

然而，通常計算機等終端裝置不知道其網路是否由 DHCP 伺服器管理。這就是為什麼 DHCPv6 伺服器配置與 SLAAC 功能結合使用。你甚至可以避免使用 SLAAC 來為本地網路裝置通告字首，你只需要向網路裝置通告 "managed-address-configuration" 選項。

```ros
[admin@MikroTik] > /ipv6/nd/print detail 
Flags: X - disabled, I - invalid; * - default 
 0    interface=ether2 ra-interval=3m20s-10m ra-delay=3s mtu=unspecified 
      reachable-time=unspecified retransmit-interval=unspecified 
      ra-lifetime=30m ra-preference=medium hop-limit=unspecified 
      advertise-mac-address=yes advertise-dns=yes 
      managed-address-configuration=yes other-configuration=no
[admin@MikroTik] > /ipv6/nd/prefix/print detail 
Flags: X - disabled, I - invalid; D - dynamic 
 0    prefix=::/64 6to4-interface=none interface=ether2 on-link=yes 
      autonomous=yes valid-lifetime=4w2d preferred-lifetime=1w 
```

現在，例如，連線到路由器 ether2 介面的計算機將從 RouterOS ND 配置收到通告訊息，說明此網路正在使用 "managed-address-configuration"，這通常會在終端使用者裝置上啟用 DHCPv6 用戶端來請求 IPv6 地址。

此處提供了帶有若干註釋的伺服器完整配置備份。

```ros
#用于 'bridge' 的地址池，其 prefix-length 必须为 128
/ipv6/pool
add name=myLocalLan prefix=2001:db8::/100 prefix-length=128
#使用指定的 'address' 池的 DHCPv6 服务器
/ipv6/dhcp-server
add address-pool=myLocalLan interface=bridge name=myLocalServer prefix-pool=""
#我们必须 'advertise' 这是一个受管网络，以便 LAN 设备使用 DHCPv6 客户端
#RFC 4861、RFC 4862、RFC 8415 'M - 托管地址配置'
/ipv6/nd
add interface=bridge managed-address-configuration=yes
#我们必须在 'bridge' 接口上启用通告
#我们甚至可以添加未指定前缀的接口，因为这里我们只需要
#用来通告 'option'，以表明这是一个受管网络
/ipv6/nd/prefix
add interface=bridge
```

:::warning
伺服器配置可能因用戶端使用的作業系統而異。例如，macOS 在使用此類配置初始化時會獲得地址，但如果字首設定為 "none"，則可能在睡眠後不續租，因為 macOS 在沒有 SLAAC 地址的情況下不使用 DHCPv6 用戶端。其他用戶端也可能需要將 "autonomous" 選項設定為 "no" 才能觸發 DHCPv6 用戶端使用。這只是一個配置示例——根據用戶端裝置的不同，可能需要調整設定。

:::

## DHCP 中繼 {#dhcp-relay}

### 概述 {#summary-4}

**子選單：** `/ip/dhcp-relay`

DHCP 中繼的目的是充當 DHCP 用戶端和 DHCP 伺服器之間的代理。在 DHCP 伺服器與 DHCP 用戶端不在同一廣播域的網路中很有用。

DHCP 中繼不會在 DHCP-server 列表中選擇特定 DHCP 伺服器；它只是將傳入請求傳送到所有列出的伺服器。

### 屬性 {#properties-5}

| 屬性 | 描述 |
| :-- | :-- |
| **add-relay-info** (*yes \| no*; 預設：**no**) | 如果根據 RFC 3046 啟用，則新增 DHCP 中繼代理資訊。Agent Circuit ID 子選項包含介面的 mac 地址，Agent Remote ID 子選項包含接收請求的用戶端的 MAC 地址。 |
| **delay-threshold** (*time \| none*; 預設：**none**) | 如果 DHCP 封包中的 secs 欄位小於 delay-threshold，則忽略此封包 |
| **dhcp-server** (IPv4 address [IPv4]*; 預設：) | DHCP 請求應轉發到的 DHCP 伺服器 IP 地址列表 |
| **interface** (interface; 預設：) | DHCP 中繼將工作的介面名稱。 |
| **local-address** (*IP*; 預設：**0.0.0.0**) | 此 DHCP 中繼的唯一 IP 地址，DHCP 伺服器需要用它來區分中繼。如果設定為 **0.0.0.0** - IP 地址將自動從中繼執行介面上分配的地址中選擇 |
| **relay-info-remote-id** (*string*; 預設：) | 指定的字串將用於構造 Option 82，而不是用戶端的 MAC 地址。Option 82 包含：接收封包的介面 + 用戶端 mac 地址或 **relay-info-remote-id** |
| **name** (*string*; 預設：) | 中繼的描述性名稱 |
| **local-address-as-src-ip(**yes \| no; 預設：**no**) | 將本地地址用作傳送到 DHCP 伺服器的 Discover/Request 封包的源地址 |
| **disabled** (yes \| no; 預設：no) | 中繼是否被停用。預設情況下，它未被停用 |
| **dhcp-server-vrf**(vrf; 預設：main) | 指定 DHCP 中繼應操作的 VRF。 |

### 配置示例 {#configuration-example-1}

假設你有多個 IP 網路位於其他路由器“後面”，但你希望將所有 DHCP 伺服器保留在單個路由器上。為此，你需要在網路中配置 DHCP 中繼，將來自用戶端的 DHCP 請求中繼到 DHCP 伺服器。

此示例將向你展示如何配置一個 DHCP 伺服器和一個 DHCP 中繼，為位於 DHCP-Relay 路由器後面的 2 個 IP 網路（192.168.1.0/24 和 192.168.2.0/24）提供服務。

![](/img/84cd8b761999e3b8.webp)

## IP 地址配置 {#ip-address-configuration}

DHCP-Server 的 IP 地址：

```ros
[admin@DHCP-Server] /ip/address> print
Flags: X - disabled, I - invalid, D - dynamic
 #   ADDRESS            NETWORK         BROADCAST       INTERFACE
 0   192.168.0.1/24     192.168.0.0     192.168.0.255   To-DHCP-Relay
 1   10.1.0.2/24	10.1.0.0	10.1.0.255	Public
[admin@DHCP-Server] /ip/address>
```

DHCP-Relay 的 IP 地址：

```ros
[admin@DHCP-Relay] /ip/address> print
Flags: X - disabled, I - invalid, D - dynamic
 #   ADDRESS            NETWORK         BROADCAST       INTERFACE
 0   192.168.0.2/24     192.168.0.0     192.168.0.255   To-DHCP-Server
 1   192.168.1.1/24     192.168.1.0     192.168.1.255   Local1
 2   192.168.2.1/24     192.168.2.0     192.168.2.255   Local2
[admin@DHCP-Relay] /ip/address>
```

## DHCP 伺服器設定 {#dhcp-server-setup}

要在 DHCP-Server 路由器上設定 2 個 DHCP 伺服器，請新增 2 個地址池。用於網路 192.168.1.0/24 和 192.168.2.0：

```ros
/ip/pool/add name=Local1-Pool ranges=192.168.1.11-192.168.1.100
/ip/pool/add name=Local2-Pool ranges=192.168.2.11-192.168.2.100
[admin@DHCP-Server] /ip/pool> print
 # NAME                                         RANGES
 0 Local1-Pool                                  192.168.1.11-192.168.1.100
 1 Local2-Pool                                  192.168.2.11-192.168.2.100
[admin@DHCP-Server] /ip/pool>
```

建立 DHCP 伺服器：

```ros
/ip/dhcp-server/add interface=To-DHCP-Relay relay=192.168.1.1 \
   address-pool=Local1-Pool name=DHCP-1 disabled=no
/ip/dhcp-server/add interface=To-DHCP-Relay relay=192.168.2.1 \
   address-pool=Local2-Pool name=DHCP-2 disabled=no
[admin@DHCP-Server] /ip/dhcp-server> print
Flags: X - disabled, I - invalid
 #   NAME         INTERFACE     RELAY           ADDRESS-POOL LEASE-TIME ADD-ARP
 0   DHCP-1       To-DHCP-Relay 192.168.1.1     Local1-Pool  3d00:00:00
 1   DHCP-2       To-DHCP-Relay 192.168.2.1     Local2-Pool  3d00:00:00
[admin@DHCP-Server] /ip/dhcp-server>
```

配置相應的網路：

```ros
/ip/dhcp-server/network/add address=192.168.1.0/24 gateway=192.168.1.1 \
   dns-server=159.148.60.20
/ip/dhcp-server/network/add address=192.168.2.0/24 gateway=192.168.2.1 \
   dns-server=159.148.60.20
[admin@DHCP-Server] /ip/dhcp-server/network> print
 # ADDRESS            GATEWAY         DNS-SERVER      WINS-SERVER     DOMAIN
 0 192.168.1.0/24     192.168.1.1     159.148.60.20
 1 192.168.2.0/24     192.168.2.1     159.148.60.20
[admin@DHCP-Server] /ip/dhcp-server/network>
```

## DHCP 中繼配置 {#dhcp-relay-config}

DHCP-Server 的配置已完成。現在讓我們配置 DHCP-Relay：

```ros
/ip/dhcp-relay/add name=Local1-Relay interface=Local1 \
   dhcp-server=192.168.0.1 local-address=192.168.1.1 disabled=no
/ip/dhcp-relay/add name=Local2-Relay interface=Local2 \
   dhcp-server=192.168.0.1 local-address=192.168.2.1 disabled=no
[admin@DHCP-Relay] /ip/dhcp-relay> print
Flags: X - disabled, I - invalid
 #   NAME                        INTERFACE      DHCP-SERVER     LOCAL-ADDRESS
 0   Local1-Relay                Local1         192.168.0.1     192.168.1.1
 1   Local2-Relay                Local2         192.168.0.1     192.168.2.1
[admin@DHCP-Relay] /ip/dhcp-relay>
```

### 使用 VRF 的 DHCP 中繼（7.15 引入） {#dhcp-relay-with-vrf-introduced-in-715}

讓我們採用之前的設定，但假設到 DHCP 伺服器的介面和到 DHCP 用戶端的介面都新增到 VRF 中：

```ros
/ip/vrf
add interfaces=To-DHCP-Server name=vrf_server
add interfaces=Local2 name=vrf2
add interfaces=Local1 name=vrf1
```

在 DHCP-relay 配置中應新增 dhcp-server-vrf：

```ros
/ip/dhcp-relay/set dhcp-server-vrf=vrf_server numbers=0,1
```

由於 VRF 配置，存在多個路由表——我們應該新增額外路由：

```ros
/ip/route
add disabled=no distance=1 dst-address=192.168.0.0/24 gateway=To-DHCP-Server@vrf_server pref-src="" routing-table=vrf1 scope=10 suppress-hw-offload=no \
    target-scope=10
add disabled=no distance=1 dst-address=192.168.0.0/24 gateway=To-DHCP-Server@vrf_server pref-src="" routing-table=vrf2 scope=10 suppress-hw-offload=no \
    target-scope=10
add disabled=no dst-address=192.168.1.0/24 gateway=Local1@vrf1 routing-table=vrf_server suppress-hw-offload=no
add disabled=no distance=1 dst-address=192.168.2.0/24 gateway=Local2@vrf2 pref-src="" routing-table=vrf_server scope=30 suppress-hw-offload=no \
    target-scope=10
```

為實現 DHCP 伺服器與 DHCP 中繼成功通訊，我們應該新增 NAT 規則：

```ros
/ip/firewall/nat
add action=dst-nat chain=dstnat dst-address=192.168.2.1 dst-port=67 in-interface=To-DHCP-Server protocol=udp src-address=192.168.0.1 to-addresses=\
    192.168.0.2
add action=dst-nat chain=dstnat dst-address=192.168.1.1 dst-port=67 in-interface=To-DHCP-Server protocol=udp src-address=192.168.0.1 to-addresses=\
    192.168.0.2
```

## DHCPv6 中繼 {#dhcpv6-relay}

### 概述 {#summary-5}

**子選單：** `/ipv6/dhcp-relay`

RouterOS 中的 DHCPv6 中繼充當中介，將本地介面上收到的 DHCPv6 用戶端請求轉發到遠端 DHCPv6 伺服器。中繼會新增一個包含其自身鏈路本地地址的 Hop‑By‑Hop 選項，使伺服器能夠知道用戶端的網路位置。來自伺服器的響應會返回給中繼，中繼移除 Hop‑By‑Hop 選項並將回覆傳遞給發起請求的用戶端。這允許單個 DHCPv6 伺服器為多個子網提供服務，而無需直接連線到每個子網，同時保留正確的地址分配和字首委派。中繼需要啟用 IPv6 轉發，併為 UDP 埠 546（用戶端）和 547（伺服器）設定適當的防火牆允許規則。

### 屬性 {#properties-6}

| 屬性 | 描述 |
| :-- | :-- |
| **comment** (*string*; 預設：) | 專案的描述性名稱。 |
| **delay-threshold** (*time \| none*; 預設：**none**) | 如果 DHCP 封包中的 secs 欄位小於 delay-threshold，則忽略此封包。 |
| **dhcp-server** (*IPv6 address [IPv6]%interface*; 預設：) | DHCP 請求應轉發到的 DHCP 伺服器 IP 地址列表（可選地，介面也可以與 IPv6 地址一起指定）。 |
| **interface** (*interface*; 預設：) | DHCP 中繼將工作的介面名稱。 |
| **name** (*string*; 預設：) | 中繼的描述性名稱 |
| **dhcp-options**(*DHCPv6 option*; 預設：**client\_mac**) | 中繼插入到轉發的 DHCPv6 封包中的 DHCPv6 選項列表。預設情況下，中繼插入選項 79。 |
| **disabled** (*yes \| no*; 預設：no) | 中繼是否被停用。預設情況下，它未被停用。 |
| **link-address**(*IPv6 address [IPv6]*; 預設：:: ) | 伺服器可用於標識用戶端所在鏈路的 IPv6 地址。 |
| **store-relayed-bindings**(*yes \| no*; 預設：**no**) | 檢查中繼的 DHCP 通告並存儲已分配的字首。例如，應使用它來避免中繼重啟時丟失路由資訊。預設情況下，它被停用。 |
