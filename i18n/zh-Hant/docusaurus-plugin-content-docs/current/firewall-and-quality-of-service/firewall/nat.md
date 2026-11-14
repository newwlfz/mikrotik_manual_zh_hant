---
sidebar_key: "firewall-and-quality-of-service/firewall/nat"
sidebar_position: 6
title: "NAT"
sidebar_label: "NAT"
description: "MikroTik RouterOS 中的 NAT 可在私有網路和公共網路之間實現 IPv4 地址轉換，既支援用於隱藏內部 IP 的源 NAT（偽裝），也支援用於將外部流量重定向到特定內部裝置的目的 NAT。文件說明了配置規則、NAT 型別以及連線跟蹤問題的故障排除提示。"
tags:
  - 'nat'
  - 'source-nat'
  - 'destination-nat'
source: https://manual.mikrotik.com/docs/firewall-and-quality-of-service/firewall/nat
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Network Address Translation 是一種網際網路標準，它允許區域網路中的主機使用一組 IP 地址進行內部通訊，並使用另一組 IP 地址進行外部通訊。使用 NAT 的區域網路稱為 *natted* 網路。要使 NAT 正常工作，每個 *natted* 網路中都應有一個 NAT 閘道器。NAT 閘道器（NAT 路由器）在封包往返區域網路的過程中執行 IP 地址重寫。在 RouterOS 中，NAT 支援 IPv4。RouterOS 不支援 NAT64。

NAT 僅匹配連線的第一個封包，連線跟蹤會記住該動作，並對屬於同一連線的所有其他封包執行該動作。

:::danger
每當更改或新增 NAT 規則時，都應清除連線跟蹤表；否則，在連線條目過期之前，NAT 規則可能看起來沒有正常工作。
:::

## NAT 型別 {#types-of-nat}

![](/img/cb0fefc65cae6a3e.webp)

NAT 有兩種型別：

- **源 NAT 或 srcnat。** 這種型別的 NAT 對源自 natted 網路的封包執行。NAT 路由器會在 IP 封包經過路由器時，將其私有源地址替換為新的公網 IP 地址。對向相反方向傳輸的回覆封包則執行相反操作。
- **目標 NAT 或 dstnat。** 這種型別的 NAT 對發往 natted 網路的封包執行。它最常用於使專用網路中的主機可從網際網路訪問。執行 dstnat 的 NAT 路由器會在 IP 封包經過路由器前往專用網路時，替換該封包的目標 IP 地址。

自 RouterOS v7 起，防火牆 NAT 有兩個新的 *INPUT* 和 *OUTPUT* 鏈，它們會用於處理交付給本地計算機上執行的應用程式以及從這些應用程式傳送的封包：

- **input** - 用於處理透過某個介面進入路由器、且目標 IP 地址為路由器地址之一的封包。經過路由器的封包不會按照 input 鏈的規則處理。
- **output** - 用於處理源自路由器並透過某個介面離開路由器的封包。經過路由器的封包不會按照 output 鏈的規則處理。

### 目標 NAT {#destination-nat}

![](/img/6cea619bfc3c118c.webp)

網路地址轉換透過修改封包 IP 頭中的網路地址資訊來工作。讓我們看一個常見設定：網路管理員希望從網際網路訪問辦公室伺服器。

我們希望允許來自網際網路的連線訪問本地 IP 為 10.0.0.3 的辦公室伺服器。在這種情況下，我們必須在辦公室閘道器路由器上配置目標地址轉換規則：

```ros
/ip/firewall/nat/add chain=dstnat action=dst-nat dst-address=172.16.16.1 dst-port=22 to-addresses=10.0.0.3 protocol=tcp
```

上述規則會執行轉換：當傳入連線請求目標地址為 172.16.16.1 的 TCP 埠 22 時，使用 *dst-nat* 動作並將封包重定向到本地 IP 地址為 10.0.0.3、埠為 22 的裝置。

:::tip
如果只允許家庭 PC 訪問，我們可以用 *"src-address=192.168.88.1"* 來改進 *dst-nat* 規則，該地址是家庭 PC 的公網（在此示例中）IP 地址。這也被認為更安全！
:::

### 源 NAT {#source-nat}

如果希望將本地裝置隱藏在從 ISP 收到的公網 IP 地址之後，應配置 MikroTik 路由器的源網路地址轉換（masquerading）功能。
假設你希望將辦公室計算機和伺服器都隱藏在公網 IP 172.16.16.1 之後。規則將如下所示：

```ros
/ip/firewall/nat/add chain=srcnat src-address=10.0.0.0/24 action=src-nat to-addresses=172.16.16.1 out-interface=WAN
```

現在你的 ISP 將看到所有請求都來自 IP 172.16.16.1，而不會看到你的區域網路 IP 地址。

#### 偽裝 {#masquerade}

防火牆 NAT 的 `action=masquerade` 是 `action=srcnat` 的一種獨特變體。它專為公網 IP 可能隨機變化的特定場景而設計，例如 DHCP 伺服器更改分配的 IP，或 PPPoE 隧道在斷開後獲得不同的 IP；簡而言之——**當公網 IP 是動態的**。

```ros
/ip/firewall/nat/add chain=srcnat src-address=10.0.0.0/24 action=masquerade out-interface=WAN
```

每當介面斷開和/或其 IP 地址發生變化時，路由器都會清除與該介面相關的所有經 masquerade 處理的連線跟蹤條目，從而縮短公網 IP 變化後的系統恢復時間。如果使用 `srcnat` 而不是 `masquerade`*,*，連線跟蹤條目會保留，鏈路故障後連線可以直接恢復。

不幸的是，當主鏈路斷開後連線被路由到不同鏈路上時，這可能會導致不穩定鏈路出現一些問題。在這種情況下，可能發生以下情況：

- 斷開時，所有相關的連線跟蹤條目都會被清除。
- 每個被清除（之前經過 masquerade）的連線的後續封包將以 *new* 狀態進入防火牆，並且如果主介面尚未恢復，封包將透過替代路由（如果有）發出，從而建立新的 masquerade 連線。
- 主鏈路恢復，路由在主鏈路上恢復，因此屬於現有連線的封包會透過主介面傳送而不經過 masquerade，從而將本地 IP 洩露到公網。

為規避這種情況，可以建立一個 **blackhole** 路由，作為斷開時可能消失的路由的替代。

位於啟用了 NAT 的路由器後面的主機沒有真正的端到端連線。因此，某些網際網路協定在 NAT 場景中可能無法工作。需要從專用網路外部發起 TCP 連線的服務，或無狀態協定（如 UDP），可能會受到干擾。

為克服這些限制，RouterOS 包含許多所謂的 NAT 助手，可為各種協定啟用 NAT 穿越。

:::tip
儘管源 NAT 和 masquerade 執行相同的基本功能：將一個地址空間對映到另一個地址空間，但細節略有不同。最明顯的是，masquerade 會從繫結到封包出口介面的 IP 中選擇出站封包的源 IP 地址。
:::

#### CGNAT (NAT444) {#cgnat-nat444}

![](/img/835ed7e13ebaaa1f.webp)

為應對 IPv4 地址耗盡，部署了 RFC 6598。其思路是在運營商網路內部使用共享的 100.64.0.0/10 地址空間，並在運營商邊緣路由器上執行 NAT，將其轉換為單個公網 IP 或公網 IP 範圍。

由於這種設定的性質，它也被稱為 NAT444，而“正常”NAT 環境的 NAT44 網路則不同。這裡涉及三個不同的 IPv4 地址空間。

RouterOS 上的 CGNAT 配置與任何其他常規源 NAT 配置沒有區別：

```ros
/ip/firewall/nat
 add chain=srcnat action=src-nat src-address=100.64.0.0/10 to-address=2.2.2.2 out-interface=<public_if>
```

其中：

- 2.2.2.2 - 公網 IP 地址。
- public\_if - 提供商邊緣路由器上連線到網際網路的介面。

NAT444 的優點顯而易見：使用的公網 IPv4 地址更少。但這種技術也有重大缺點：

- 執行 CGNAT 的服務提供商路由器需要為所有地址轉換維護狀態表：這需要大量記憶體和 CPU 資源。
- 主機遊戲問題。當兩個使用同一外部公網 IPv4 地址的訂閱者嘗試相互連線時，某些遊戲會失敗。
- 出於法律原因跟蹤使用者意味著額外的日誌記錄，因為多個家庭共用一個公網地址。
- 任何需要傳入連線的功能都會失效。雖然常規 NAT 已經如此，但終端使用者通常仍可在其 NAT 路由器上設定埠轉發。CGNAT 使這變得不可能。這意味著無法在此託管 Web 伺服器，IP 電話預設也無法接收傳入呼叫。
- 某些 Web 伺服器僅允許來自同一公網 IP 地址的最大連線數，以此對抗 SYN 洪水等 DoS 攻擊。使用 CGNAT 時，此限制會更頻繁地達到，某些服務的質量可能較差。
- 6to4 需要全域性可達地址，在採用有限拓撲跨度地址的網路中無法工作。

帶有共享地址空間源地址或目標地址的封包不得跨服務提供商邊界轉發。服務提供商必須在入站鏈路上過濾此類封包。在 RouterOS 中，可以透過邊緣路由器上的防火牆過濾器輕鬆完成：

```ros
/ip/firewall/filter
 add chain=input src-address=100.64.0.0/10 action=drop in-interface=<public_if>
 add chain=output dst-address=100.64.0.0/10 action=drop out-interface=<public_if>
 add chain=forward src-address=100.64.0.0/10 action=drop in-interface=<public_if>
 add chain=forward src-address=100.64.0.0/10 action=drop out-interface=<public_if>
 add chain=forward dst-address=100.64.0.0/10 action=drop out-interface=<public_if>
```

在大規模部署的 CGN 網路中，服務提供商可能被要求記錄對映後的地址，這可能會成為問題。幸運的是，RFC 7422 提出了一種管理 CGN 轉換的方法，可顯著減少所需的日誌記錄量，同時為濫用響應提供可追溯性。

RFC 指出，CGN 不必記錄每個連線，而是可以確定性地將客戶私有地址（在 CGN 面向客戶的介面上收到的地址，即內部側）對映到擴充套件了埠範圍的公網地址。

這意味著必須新增單獨的 NAT 規則來實現各自對映，如下例所示：

|  |  |
| :-- | :-- |
| **內部 IP** | **外部 IP/埠範圍** |
| 100.64.0.1 | 2.2.2.2:5000-5199 |
| 100.64.0.2 | 2.2.2.2:5200-5399 |
| 100.64.0.3 | 2.2.2.2:5400-5599 |
| 100.64.0.4 | 2.2.2.2:5600-5799 |
| 100.64.0.5 | 2.2.2.2:5800-5999 |

建議使用指令碼而不是手動編寫規則。以下示例可以調整以適應你的設定中的任何要求。

```ros
{
######## Adjustable values #########
:local StartingAddress 100.64.0.1
:local ClientCount 5
:local AddressesPerClient 2
:local PublicAddress 2.2.2.2
:local StartingPort 5000
:local PortsPerAddress 200
####################################

# 所有客户端链跳转
/ip/firewall/nat/add chain=srcnat action=jump jump-target=clients \
    src-address="$StartingAddress-$($StartingAddress + ($ClientCount * $AddressesPerClient) - 1)"

:local currentPort $StartingPort

:for c from=1 to=$ClientCount do={
    # 特定客户端链跳转
    :if ($AddressesPerClient > 1) do={
      /ip/firewall/nat/add chain=clients action=jump jump-target="client-$c" \
      src-address="$($StartingAddress + ($AddressesPerClient * ($c - 1)))-$($StartingAddress + ($AddressesPerClient * $c -1))"
    } else={
      /ip/firewall/nat/add chain=clients action=jump jump-target="client-$c" \
      src-address="$($StartingAddress + ($AddressesPerClient * ($c - 1)))"
    }

    # 转换规则
    :for a from=1 to=$AddressesPerClient do={
      /ip/firewall/nat/add chain="client-$c" action=src-nat protocol=tcp \
      src-address="$($StartingAddress + (($c -1) * $AddressesPerClient) + $a - 1)" to-address=$PublicAddress to-ports="$currentPort-$($currentPort + $PortsPerAddress - 1)"
      /ip/firewall/nat/add chain="client-$c" action=src-nat protocol=udp \
      src-address="$($StartingAddress + (($c -1) * $AddressesPerClient) + $a - 1)" to-address=$PublicAddress to-ports="$currentPort-$($currentPort + $PortsPerAddress - 1)"
      :set currentPort ($currentPort + $PortsPerAddress)
    }
}
}
```

這六個本地值可以調整，指令碼既可以直接貼上到終端中，也可以儲存在系統指令碼部分，以備以後需要重新生成配置。

執行後，你應該會得到一組規則：

```ros
[admin@MikroTik] > ip firewall nat print
Flags: X - disabled, I - invalid; D - dynamic
 0    chain=srcnat action=jump jump-target=clients
      src-address=100.64.0.1-100.64.0.10

 1    chain=clients action=jump jump-target=client-1
      src-address=100.64.0.1-100.64.0.2

 2    chain=client-1 action=src-nat to-addresses=2.2.2.2 to-ports=5000-5199
      protocol=tcp src-address=100.64.0.1

 3    chain=client-1 action=src-nat to-addresses=2.2.2.2 to-ports=5000-5199
      protocol=udp src-address=100.64.0.1

 4    chain=client-1 action=src-nat to-addresses=2.2.2.2 to-ports=5200-5399
      protocol=tcp src-address=100.64.0.2

 5    chain=client-1 action=src-nat to-addresses=2.2.2.2 to-ports=5200-5399
      protocol=udp src-address=100.64.0.2

 6    chain=clients action=jump jump-target=client-2
      src-address=100.64.0.3-100.64.0.4

 7    chain=client-2 action=src-nat to-addresses=2.2.2.2 to-ports=5400-5599
      protocol=tcp src-address=100.64.0.3

 8    chain=client-2 action=src-nat to-addresses=2.2.2.2 to-ports=5400-5599
      protocol=udp src-address=100.64.0.3

 9    chain=client-2 action=src-nat to-addresses=2.2.2.2 to-ports=5600-5799
      protocol=tcp src-address=100.64.0.4

10    chain=client-2 action=src-nat to-addresses=2.2.2.2 to-ports=5600-5799
      protocol=udp src-address=100.64.0.4

11    chain=clients action=jump jump-target=client-3
      src-address=100.64.0.5-100.64.0.6

12    chain=client-3 action=src-nat to-addresses=2.2.2.2 to-ports=5800-5999
      protocol=tcp src-address=100.64.0.5

13    chain=client-3 action=src-nat to-addresses=2.2.2.2 to-ports=5800-5999
      protocol=udp src-address=100.64.0.5

14    chain=client-3 action=src-nat to-addresses=2.2.2.2 to-ports=6000-6199
      protocol=tcp src-address=100.64.0.6

15    chain=client-3 action=src-nat to-addresses=2.2.2.2 to-ports=6000-6199
      protocol=udp src-address=100.64.0.6

[...]
```

#### 髮夾 NAT {#hairpin-nat}

髮夾網路地址轉換（*NAT Loopback*）是指區域網路中的裝置可以透過閘道器路由器的公網 IP 地址訪問區域網路中的另一臺機器。

![](/img/6cea619bfc3c118c.webp)

在上面的示例中，閘道器路由器具有以下 `dst-nat` 配置規則：

```ros
/ip/firewall/nat/add chain=dstnat action=dst-nat dst-address=172.16.16.1 dst-port=443 to-addresses=10.0.0.3 to-ports=443 protocol=tcp
```

當來自家庭 PC 的使用者與 Web 伺服器建立連線時，路由器會按配置執行 DST NAT：

1. 用戶端傳送一個源 IP 地址為 192.168.88.1、目標 IP 地址為 172.16.16.1、埠為 443 的封包，以請求某些 Web 資源。
2. 路由器對封包執行目標 NAT，將其轉換為 10.0.0.3，並相應地替換封包中的目標 IP 地址。源 IP 地址保持不變：192.168.88.1。
3. 伺服器回覆用戶端的請求，回覆封包的源 IP 地址為 10.0.0.3，目標 IP 地址為 192.168.88.1。
4. 路由器確定該封包屬於之前的連線，並撤銷目標 NAT，將原始目標 IP 地址放入源 IP 地址欄位。目標 IP 地址為 192.168.88.1，源 IP 地址為 172.16.16.1。
5. 用戶端收到其期望的回覆封包，連線建立。

![](/img/8e40bd6d38f0e7d5.webp)

但當與 Web 伺服器處於同一網路的用戶端請求連線到 Web 伺服器的 **公網** IP 地址時，就會出現一個 **問題**：

1. 用戶端傳送一個源 IP 地址為 10.0.0.2、目標 IP 地址為 172.16.16.1、埠為 443 的封包，以請求某些 Web 資源。
2. 路由器對封包執行目標 NAT，將其轉換為 10.0.0.3，並相應地替換封包中的目標 IP 地址。源 IP 地址保持不變：10.0.0.2。
3. 伺服器回覆用戶端的請求。但是，請求的源 IP 地址與 Web 伺服器位於同一子網。Web 伺服器不會將回復發送回路由器，而是直接將其傳送回 10.0.0.2，回覆中的源 IP 地址為 10.0.0.3。
4. 用戶端收到回覆封包，但會將其丟棄，因為它期望收到來自 172.16.16.1 的封包，而不是來自 10.0.0.3 的封包。

為解決此問題，我們將按如下方式配置一條新的 *src-nat* 規則（髮夾 NAT 規則）：

```ros
/ip/firewall/nat
add action=masquerade chain=srcnat dst-address=10.0.0.3 out-interface=LAN protocol=tcp src-address=10.0.0.0/24
```

配置上述規則後：

1. 用戶端傳送一個源 IP 地址為 10.0.0.2、目標 IP 地址為 172.16.16.1、埠為 443 的封包，以請求某些 Web 資源。
2. 路由器對封包執行目標 NAT，將其轉換為 10.0.0.3，並相應地替換封包中的目標 IP 地址。它還對封包執行源 NAT，並將封包中的源 IP 地址替換為其 LAN 介面上的 IP 地址。目標 IP 地址為 10.0.0.3，源 IP 地址為 10.0.0.1。
3. Web 伺服器回覆請求，並將源 IP 地址為 10.0.0.3 的回覆傳送迴路由器 LAN 介面的 IP 地址 10.0.0.1。
4. 路由器確定該封包屬於之前的連線，並撤銷源 NAT 和目標 NAT，將原始目標 IP 地址 172.16.16.1 放入源 IP 地址欄位，將原始源 IP 地址 10.0.0.2 放入目標 IP 地址欄位。

### 端點無關 NAT {#endpoint-independent-nat}

端點無關 NAT 會在源 NAT 中建立對映，並對具有相同源 IP 和埠的所有後續封包使用同一對映。此對映透過以下規則建立：

```ros
/ip/firewall/nat
add action=endpoint-independent-nat chain=srcnat out-interface=WAN protocol=udp
```

此對映允許執行與源無關的過濾，從而允許將來自 WAN 的任意源的封包轉發到對映的內部 IP 和埠。以下規則啟用過濾：

```ros
/ip/firewall/nat
add action=endpoint-independent-nat chain=dstnat in-interface=WAN protocol=udp
```

:::danger
端點無關 NAT 僅適用於 UDP 協定。
:::

此外，endpoint-independent-nat 還可以接受幾個其他引數：

- `randomize-port` - 隨機化連線將對映到哪個公網埠。

更多資訊請參閱 [RFC 5128](https://www.ietf.org/rfc/rfc5128.txt) 第 2.2.3 節和第 2.2.5 節

## NAT 助手 {#nat-helpers}

位於啟用了 NAT 的路由器後面的主機沒有真正的端到端連線。因此，某些網際網路協定在 NAT 場景中可能無法工作。為克服這些限制，RouterOS 包含許多 NAT 助手，可為各種協定啟用 NAT 穿越。

NAT 助手可以從 `/ip/firewall/service-ports` 選單進行管理。

可用的 NAT 助手列表：

| 助手 | 描述 |
| :-- | :-- |
| **FTP** | FTP 服務助手 |
| **H323** | H323 服務助手 |
| **IRC** | IRC 服務助手 |
| **PPTP** | PPTP (GRE) 隧道助手 |
| **UDPLITE** | UDP-Lite 服務助手 |
| **DCCP** | DCCP 服務助手 |
| **SCTP** | SCTP 服務助手 |
| **SIP** | SIP 助手。附加選項：`sip-direct-media` 允許將 RTP 媒體流重定向為直接從主叫方傳送到被叫方。預設值為 `yes`。`sip-timeout` 允許調整 SIP UDP 連線的 TTL。預設值：1 小時。在某些環境中，您必須減小該值。 |
| **TFTP** | TFTP 服務助手 |
| **RTSP** | RTSP 服務助手 |

:::warning
如果未啟用連線跟蹤，則防火牆服務埠將顯示為不活動

**警告：** **udplite**、**dccp** 和 **sctp** 是連線跟蹤的內建服務。由於它們不是單獨載入的模組，因此無法單獨停用；它們會與連線跟蹤一起被停用。
:::
