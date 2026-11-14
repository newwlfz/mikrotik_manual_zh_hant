---
sidebar_key: "network-management/dhcp/server"
sidebar_position: 2
title: "DHCP 伺服器"
sidebar_label: "DHCP 伺服器"
description: "RouterOS DHCP 伺服器從 IP 池中向用戶端分配 IPv4 地址和網路設定，並支援靜態租約、網路、DHCP 選項和選項集、選項匹配器、RADIUS 支援、速率限制以及惡意 DHCP 伺服器告警。"
tags:
  - 'dhcp'
source: https://manual.mikrotik.com/docs/7.25/network-management/dhcp/server
captured_at: '2026-11-04T11:21:14+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

**子選單：** `/ip/dhcp-server`

DHCP 伺服器為路由器所服務網路中的用戶端分配 IPv4 地址和網路設定。它從 IP 地址池中租用地址，併發送匹配的 DHCP 網路的設定：閘道器、DNS 伺服器、域名、NTP 和 WINS 伺服器以及其他選項。它還可以分發繫結到特定用戶端的靜態租約，並從 RADIUS 伺服器獲取租約。有關 DHCP 交換、租約和續租的工作方式，請參閱 [DHCP 概念](./index.md)。

DHCP 伺服器需要：

- 伺服器介面上的 IP 地址。沒有它，伺服器會顯示為無效。
- 一個包含待分配地址的 IP 地址池（`/ip/pool`）。不要把路由器自身的地址包含在地址池中。
- 一個 DHCP 網路（`/ip/dhcp-server/network`），其中包含傳送給該子網用戶端的設定。
- DHCP 伺服器本身（`/ip/dhcp-server`），它將介面與地址池關聯起來。

`setup` 命令會一步建立地址池、網路和伺服器。以下配置示例展示了這兩種方式。

每個介面可以有一個 DHCP 伺服器，用於直接連線的用戶端。對於透過 DHCP 中繼傳來的請求，同一介面上可以有更多伺服器，每個中繼地址對應一個（請參閱 `relay` 屬性）。

:::warning
DHCP 伺服器需要一個真實介面來接收原始乙太網封包。當它執行在網橋上時，網橋至少需要一個能接收這些封包的埠；在空網橋上伺服器無法正常工作。
:::

## 配置示例 {#configuration-examples}

### 設定 {#setup}

`setup` 命令會一步建立 IP 地址池、網路和 DHCP 伺服器。它會依次詢問每個值，並根據介面地址給出建議值。

首先，為介面新增 IP 地址：

```ros
/ip/address/add address=192.168.88.1/24 interface=ether3
```

然後執行 `setup`，並確認或更改每個建議值：

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
Select whether the DHCP server sends DNS servers to clients
send dns: yes
Select DNS servers (leave empty to use servers from DNS settings)
dns servers: 192.168.88.1
Select lease time
lease time: 1800s
```

DHCP 伺服器現在已在 ether3 上執行。

### 手動配置 {#manual-configuration}

要手動配置相同的 DHCP 伺服器，請自行建立每個部分：

1. 新增伺服器所在介面上的路由器 IP 地址。在此示例中，路由器也是網路的閘道器：

   ```ros
   /ip/address/add address=192.168.88.1/24 interface=bridge1
   ```

2. 建立一個包含待分配地址的 IP 地址池。不要把路由器自身的地址包含在地址池中：

   ```ros
   /ip/pool/add name=dhcp_pool0 ranges=192.168.88.2-192.168.88.254
   ```

3. 新增一個網路條目，其中包含傳送給用戶端的設定，例如閘道器和 DNS 伺服器：

   ```ros
   /ip/dhcp-server/network/add address=192.168.88.0/24 dns-server=192.168.88.1 gateway=192.168.88.1
   ```

4. 在介面上新增 DHCP 伺服器，並指定地址池：

   ```ros
   /ip/dhcp-server/add address-pool=dhcp_pool0 interface=bridge1 name=dhcp1
   ```

## 屬性 {#properties}

DHCP 伺服器的所有屬性都在 [`/ip/dhcp-server`](../../cli-reference/ip/dhcp-server/index.md) CLI 參考中說明。以下行為需要進一步解釋。

### 對未知地址的請求 {#requests-for-unknown-addresses}

從另一個網路遷移過來、或伺服器已不再持有其租約的用戶端，可能會請求一個伺服器無法提供的地址。當 `authoritative=yes`（預設值）時，伺服器會用 DHCPNAK 響應此類請求，因此用戶端會立即重新開始，而不是等待請求超時。當 `authoritative=no` 時，伺服器會忽略此類廣播請求（例如來自重新繫結用戶端的請求），並將其留給其他伺服器。對於單播續租請求，伺服器總會響應：以 DHCPNAK 響應，或者在請求的地址在地址池中空閒時提供新租約。

要讓另一臺伺服器先響應，例如讓主伺服器響應、將此路由器作為備份，請設定 `delay-threshold`。這樣伺服器會忽略請求，直到用戶端已嘗試達到設定時間；用戶端會在其請求的 `secs` 欄位中報告該時間。

### DHCP 中繼後的用戶端 {#clients-behind-a-dhcp-relay}

伺服器只有在設定了 `relay` 屬性時才會響應中繼請求：將其設為中繼的地址（即中繼的 `local-address`），或設為 `255.255.255.255` 以匹配任意中繼。這樣同一介面上可以執行多個伺服器，每個中繼對應一個。完整示例請參閱 [DHCP 中繼](./relay.md)。

### 用戶端的 DNS 條目 {#dns-entries-for-clients}

當 `add-dns-entries=yes` 時，伺服器會為每個已繫結租約新增一條動態 DNS 條目（A 型別），這樣用戶端就可以透過路由器的 DNS 解析器按名稱訪問。名稱為用戶端傳送的主機名後跟 `add-dns-entries-suffix`（預設 `lan`），例如 `laptop.lan`，條目的 TTL 為租約時間。當網路沒有 `domain` 時，伺服器還會將該字尾作為用戶端的域名傳送。

## 網路 {#network}

**子選單：** `/ip/dhcp-server/network`

網路條目包含傳送給地址位於該網路中的用戶端的設定：閘道器、DNS 和 NTP 伺服器、域名、選項以及網路啟動設定。當未設定 `dns-server` 或 `ntp-server` 時，伺服器會發送路由器自身使用的 DNS 或 NTP 伺服器；設定 `dns-none` 或 `ntp-none` 則不傳送任何伺服器。所有屬性都在 [`/ip/dhcp-server/network`](../../cli-reference/ip/dhcp-server/network.md) CLI 參考中說明。

## 租約 {#leases}

**子選單：** `/ip/dhcp-server/lease`

租約選單以動態條目顯示伺服器已發出的租約，以及你新增的靜態租約；靜態租約用於給用戶端固定地址、來自特定地址池的地址或它自己的設定。所有租約屬性、狀態值和命令都在 [`/ip/dhcp-server/lease`](../../cli-reference/ip/dhcp-server/lease/index.md) CLI 參考中說明。

當用戶端請求地址時，伺服器會選擇一個：

- 具有靜態租約的用戶端會獲得其租約中的地址。靜態地址不會進行衝突檢查。
- 其他用戶端會從地址池中獲得一個空閒地址。啟用 `conflict-detection`（預設）時，伺服器會先用 ARP 請求和 ICMP 回顯請求檢查該地址，這會使提供地址延遲約半秒。如果另一臺主機應答，該地址會以 `conflict` 狀態保留為租約，保留時間為租約時間，然後向用戶端提供另一個空閒地址。

然後伺服器提供該地址，當用戶端請求它時，租約即被繫結。當用戶端釋放地址或租約到期時，動態租約會移除，地址返回地址池；靜態租約則保留，並在用戶端返回時再次使用。

### 租約儲存 {#lease-storage}

伺服器會定期將租約儲存到磁碟，預設每 5 分鐘一次，以減少對快閃記憶體的寫入。該間隔和 RADIUS 計費設定位於 `/ip/dhcp-server/config` 中，請參閱 [`/ip/dhcp-server/config`](../../cli-reference/ip/dhcp-server/config.md) CLI 參考。

### 速率限制 {#rate-limiting}

你可以使用租約的 `rate-limit` 屬性限制用戶端的頻寬。然後伺服器會為租約地址新增一個動態簡單佇列。

:::warning
佇列不適用於 FastTracked 流量。請確保防火牆不會對您想要限制的流量執行 FastTrack。
:::

只有靜態租約才能設定速率限制，因此首先將租約設為靜態：

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

然後設定速率限制。伺服器會為該租約建立一個動態簡單佇列：

```ros
[admin@MikroTik] > /ip/dhcp-server/lease/set 0 rate-limit=10M/10M

[admin@MikroTik] > /queue/simple/print 
Flags: X - disabled, I - invalid, D - dynamic 
 0  D name="dhcp-ds<MikroTik/6C:3B:6B:7C:41:3E>" target=192.168.88.254/32 parent=none packet-marks="" priority=8/8 queue=default-small/default-small limit-at=10M/10M max-limit=10M/10M burst-limit=0/0 burst-threshold=0/0 burst-time=0s/0s 
      bucket-size=0.1/0.1
```

:::note
`allow-dual-stack-queue` 預設啟用，因此同一用戶端的 DHCP 租約和 DHCPv6 繫結共享一個動態簡單佇列。若未啟用，伺服器會為 IPv4 和 IPv6 分別建立佇列。
:::

共享佇列同時包含 IPv4 和 IPv6 地址：

```ros
[admin@MikroTik] > /queue/simple/print 
Flags: X - disabled, I - invalid, D - dynamic 
 0  D name="dhcp-ds<MikroTik/6C:3B:6B:7C:41:3E>" target=192.168.88.254/32,fdb4:4de7:a3f8:418c::/66 parent=none packet-marks="" priority=8/8 queue=default-small/default-small limit-at=10M/10M max-limit=10M/10M burst-limit=0/0 burst-threshold=0/0 
      burst-time=0s/0s bucket-size=0.1/0.1 
```

## RADIUS 支援 {#radius-support}

DHCP 伺服器還可以從 RADIUS 伺服器獲取租約（`use-radius=yes`）。它會發送並接受以下 RADIUS 屬性。

### Access-Request {#access-request}

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

### Access-Accept {#access-accept}

- Framed-IP-Address - 將分配給用戶端的 IP 地址。
- Framed-Pool - 用於向用戶端分配 IP 地址的 IP 地址池。
- Rate-Limit - 對 DHCP 用戶端的資料速率限制。格式為：`rx-rate[/tx-rate] [rx-burst-rate[/tx-burst-rate] [rx-burst-threshold[/tx-burst-threshold] [rx-burst-time[/tx-burst-time][priority] [rx-rate-min[/tx-rate-min]]]]`。所有速率都應為數字，可帶可選的 'k'（1,000 倍）或 'M'（1,000,000 倍）。如果未指定 tx-rate，則 rx-rate 也用作 tx-rate。tx-burst-rate、tx-burst-threshold 和 tx-burst-time 同理。如果 rx-burst-threshold 和 tx-burst-threshold 均未指定（但指定了 burst-rate），則使用 rx-rate 和 tx-rate 作為突發閾值。如果 rx-burst-time 和 tx-burst-time 均未指定，則預設使用 1s。priority 取值為 1..8，其中 1 表示最高優先順序，8 表示最低優先順序。如果未指定 rx-rate-min 和 tx-rate-min，則使用 rx-rate 和 tx-rate 的值。rx-rate-min 和 tx-rate-min 的值不能超過 rx-rate 和 tx-rate 的值。
- Ascend-Data-Rate - 提供多個屬性時的 TX/RX 資料速率限制，第一個限制 tx 資料速率，第二個限制 RX 資料速率。如果與 Ascend-Xmit-Rate 一起使用，則指定 RX 速率。0 表示無限制。
- Ascend-Xmit-Rate - tx 資料速率限制。它可以只用於指定 TX 限制，而不必傳送兩個連續的 Ascend-Data-Rate 屬性（在這種情況下，Ascend-Data-Rate 將指定接收速率）。0 表示無限制。
- Session-Timeout - 最大租約時間（lease-time）。

### 每個租約的速率限制 {#rate-limit-per-lease}

RADIUS 伺服器可以使用 Mikrotik-Rate-Limit 屬性為每個租約分配速率限制。首先，將 DHCP 伺服器設定為使用 RADIUS：

```ros
/radius
add address=10.0.0.1 secret=VERYsecret123 service=dhcp
/ip/dhcp-server
set dhcp1 use-radius=yes
```

然後配置 RADIUS 伺服器傳送 Mikrotik-Rate-Limit 屬性。對於使用 MySQL 的 FreeRADIUS，請為用戶端的 MAC 地址在 `radcheck` 和 `radreply` 表中新增條目，例如：

```sql
INSERT INTO `radcheck` (`username`, `attribute`, `op`, `value`) VALUES
('00:0C:42:00:D4:64', 'Auth-Type', ':=', 'Accept');

INSERT INTO `radreply` (`username`, `attribute`, `op`, `value`) VALUES
('00:0C:42:00:D4:64', 'Framed-IP-Address', '=', '192.168.88.254'),
('00:0C:42:00:D4:64', 'Mikrotik-Rate-Limit', '=', '10M');
```

## 警報 {#alerts}

DHCP 警報會在介面上發現流氓 DHCP 伺服器。它會監視介面上的 DHCP 回覆，並檢查每個回覆是否來自有效的 DHCP 伺服器。來自未知伺服器的回覆會被記錄，警報還可以執行指令碼：

```ros
[admin@MikroTik] > /log/print where topics~"dhcp"
 00:34:23 dhcp,critical,error dhcp alert on Public: discovered unknown dhcp server, mac 00:02:29:60:36:E7, ip 10.5.8.236
```

由於 DHCP 回覆可能是單播的，警報可能看不到其他伺服器傳送給用戶端的提供訊息。因此警報還會充當 DHCP 用戶端：它大約每分鐘傳送自己的 DHCPDISCOVER。

:::warning
不要在同時作為同一介面 DHCP 用戶端的路由器上使用 DHCP alert：alert 傳送的 DHCPDISCOVER 訊息可能會干擾 DHCP 用戶端。請在 DHCP 伺服器上或在使用靜態 IP 地址的路由器上使用該 alert。
:::

**子選單：** `/ip/dhcp-server/alert`

新警報建立時處於停用狀態；新增後請啟用它們。所有警報屬性都在 [`/ip/dhcp-server/alert`](../../cli-reference/ip/dhcp-server/alert/index.md) CLI 參考中說明。

## DHCP 選項 {#dhcp-options}

**子選單：** `/ip/dhcp-server/option`

你可以定義額外的選項供 DHCP 伺服器傳送。當同一選項在多個層級上設定時，以下層級中靠前者優先：

1. RADIUS。
2. 租約。
3. 伺服器。
4. 網路。

只有當用戶端在其引數請求列表（選項 55）中請求某個選項時，伺服器才會傳送該選項。即使用戶端未請求也要傳送某個選項，請在該選項上設定 `force`，例如以下示例中的 `auto-proxy-config` 選項：

```ros
/ip/dhcp-server/option/set [find name=auto-proxy-config] force=yes
```

所有選項屬性，包括選項值的寫法以及它們可以包含哪些變數，都在 [`/ip/dhcp-server/option`](../../cli-reference/ip/dhcp-server/option/index.md) CLI 參考中說明。

### DHCP 選項集 {#dhcp-option-sets}

**子選單：** `/ip/dhcp-server/option/sets`

此選單允許將多個選項組合到選項集中，之後可用於覆蓋預設 DHCP 伺服器選項集。

### 示例 {#example}

**無類路由**

無類靜態路由選項（選項 121，RFC 3442）會向用戶端傳送路由。此示例傳送一條到 160.0.0.0/24 的路由和一條預設路由，二者都經由 10.1.101.1。該值由以下部分組成：

- `18` - 字首長度 24。
- `A00000` - 目標地址 160.0.0 的有效八位組。
- `0A016501` - 閘道器 10.1.101.1。
- `00` - 字首長度 0，即預設路由。
- `0A016501` - 預設路由的閘道器 10.1.101.1。

收到選項 121 的用戶端會忽略路由器選項（選項 3），因此這裡也包含了預設路由。

```ros
/ip/dhcp-server/option
add code=121 name=classless value=0x18A000000A016501000A016501
/ip/dhcp-server/network
set 0 dhcp-option=classless
```

用戶端上的結果：

```ros
[admin@MikroTik] > /ip/route/print
Flags: D - DYNAMIC; A - ACTIVE; c - CONNECT, d - DHCP
Columns: DST-ADDRESS, GATEWAY, DISTANCE
    DST-ADDRESS   GATEWAY     DISTANCE
DAd 0.0.0.0/0     10.1.101.1         1
DAd 160.0.0.0/24  10.1.101.1         1
```

使用 `$(NETWORK_GATEWAY)` 變數時，閘道器取自網路設定，而不是直接寫入值中：

```ros
/ip/dhcp-server/option
add name=classless code=121 value="0x18A00000\$(NETWORK_GATEWAY)0x00\$(NETWORK_GATEWAY)"
```

**自動代理配置**

```ros
/ip/dhcp-server/option 
  add code=252 name=auto-proxy-config value="'https://autoconfig.something.lv/wpad.dat'"
```

## 選項匹配器 {#option-matcher}

選項匹配器根據用戶端請求中的任意 DHCP 選項來識別 DHCP 用戶端，並從特定 IP 地址池為其分配地址。它會精確比較選項（`exact`），或在選項中的任意位置查詢該值（`substring`）。當選項包含的內容多於你要匹配的部分時，例如供應商類識別符號還包含裝置型號或 MAC 地址，請使用子字串匹配。

:::note
當兩個子字串匹配器匹配同一選項時，例如一個匹配 "ABC"，另一個匹配 "ABCDE"，而選項值為 "ABCDEF"，則實際應用哪個是隨機的。
:::

:::note
擁有靜態租約的用戶端會保留其靜態地址，即使匹配器匹配到它們也是如此。
:::

所有匹配器屬性都在 [`/ip/dhcp-server/matcher`](../../cli-reference/ip/dhcp-server/matcher.md) CLI 參考中說明。

### 選項匹配器示例 {#option-matcher-examples}

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
