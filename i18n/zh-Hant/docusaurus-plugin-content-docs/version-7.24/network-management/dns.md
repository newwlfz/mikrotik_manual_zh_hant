---
sidebar_key: "network-management/dns"
sidebar_position: 4
title: "DNS"
sidebar_label: "DNS"
description: "本頁介紹 MikroTik RouterOS 中的 DNS 功能，說明如何將路由器配置為 DNS 快取或主伺服器，並提供遠端請求、快取策略和動態伺服器整合等選項。頁面還詳細介紹了快取大小、TTL 設定和 DNS over HTTPS（DoH）支援等配置屬性。"
tags:
  - 'dns'
  - 'doh'
  - 'adlist'
source: https://manual.mikrotik.com/docs/7.24/network-management/dns
captured_at: '2026-11-04T11:32:42+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 簡介 {#introduction}

Domain Name System (DNS) 通常指網際網路的電話簿。換句話說，DNS 是一個數據庫，它將字串（稱為主機名，例如 [mikrotik.com](https://mikrotik.com)）連結到特定 IP 地址，例如 159.148.172.205 或 2a02:610:7501:2000::205

啟用了 DNS 功能的 MikroTik 路由器可被設定為任何符合 DNS 規範的用戶端的 DNS 快取。此外，MikroTik 路由器還可以在其 DHCP 伺服器設定中指定為主 DNS 伺服器。啟用遠端請求後，MikroTik 路由器會響應埠 53 上的 TCP 和 UDP DNS 請求。

當同時設定靜態和動態伺服器時，優先使用靜態伺服器條目，但這並不表示始終會使用靜態伺服器（例如，之前從動態伺服器收到了查詢，但後來添加了靜態伺服器，此時將優先使用動態條目）。

:::tip
當使用 DNS 伺服器的 *allow-remote-requests* 時，請確保僅對已知主機限制透過 TCP 和 UDP 協定埠 53 訪問你的伺服器。

:::

在 LAN 上管理 DNS 功能有幾種方式：使用公共 DNS、將路由器用作快取，或者不干預 DNS 配置。以如下設定為例：Internet 服務提供商 (ISP) → 閘道器 (GW) → 區域網路 (LAN)。GW 是採用預設配置的 RouterOS 裝置：

- 未在 "GW" DHCP 伺服器網路配置中配置任何 DNS 伺服器——裝置會將從 `ISP` 收到的 DNS 伺服器 IP 地址配置轉發給 `LAN` 裝置。
- 在 "GW" DHCP 伺服器網路配置中配置 DNS 伺服器——裝置會將配置的 DNS 伺服器提供給 `LAN` 裝置（還必須啟用 "/ip/dns/set allow-remote-requests=yes"）。
- 在 "GW" DHCP 伺服器網路配置下的 DNS 伺服器中配置 "dns-none"——裝置不會將任何 **動態** DNS 伺服器轉發給 `LAN` 裝置。

### DNS 配置 {#dns-configuration}

DNS 設施用於為路由器本身以及連線到它的用戶端提供域名解析。

| 屬性 | 描述 |
| :-- | :-- |
| **allow-remote-requests** (*yes* \| *no*; 預設值：**no**) | 指定是否允許將路由器用作遠端用戶端的 DNS 快取。否則，僅路由器本身會使用 DNS 配置。 |
| **address-list-extra-time** *(time; 預設值：**0s**)* | 建立地址列表條目時新增到 TTL 的額外時間。 |
| **cache-max-ttl** (*time*; 預設值：**1w**) | 快取記錄的最大生存時間。換句話說，快取記錄將在 cache-max-TTL 時間後無條件過期。來自 DNS 伺服器的較短 TTL 會被遵循。 |
| **cache-size** (*integer[64..4294967295]*; 預設值：**2048**) | 指定 DNS 快取的大小，單位為 KiB。 |
| **max-concurrent-queries** (*integer*; 預設值：**100**) | 指定允許的併發查詢數。 |
| **max-concurrent-tcp-sessions** (*integer*; 預設值：**20**) | 指定允許的併發 TCP 會話數。 |
| **max-udp-packet-size** (*integer [50..65507]*; 預設值：**4096**) | 允許的 UDP 封包最大大小。 |
| **mdns-repeat-ifaces** (*介面列表*; 預設值： ) | 一旦此列表中的某個介面收到 mDNS 封包，它就會將其轉發到該列表中的所有其他介面。僅支援 IPv4。 |
| **query-server-timeout** (*time*; 預設值：**2s**) | 指定等待伺服器查詢響應的時長。 |
| **query-total-timeout** (*time*; 預設值：**10s**) | 指定等待查詢響應的總時長。請注意，配置此設定時必須考慮 "query-server-timeout" 和所用 DNS 伺服器的數量。 |
| **servers** (*IPv4/IPv6 地址列表@vrf*; 預設值： ) | DNS 伺服器 IPv4/IPv6 地址列表 |
| **cache-used** (*integer*) | 顯示當前已使用的快取大小，單位為 KiB |
| **dynamic-server** (*IPv4/IPv6 列表*) | 來自不同服務（例如 DHCP）的動態新增的 DNS 伺服器列表。 |
| **doh-max-concurrent-queries** (*integer*; 預設值：**50**) | 指定允許的 DoH 併發查詢數。 |
| **doh-max-server-connections** (*integer*; 預設值：**5**) | 指定允許到 DoH 伺服器的併發連線數。 |
| **doh-timeout** (*time*; 預設值：**5s**) | 指定等待 DoH 伺服器查詢響應的時長。 |
| **use-doh-server** (*string; 預設值： )* | 指定必須用於 DNS 查詢的 DoH 伺服器。如果指定，DoH 功能會覆蓋 "*servers*" 的使用。伺服器必須使用 "https://" 字首指定。僅支援一個 DoH 伺服器。 |
| **verify-doh-cert** (*yes* \| *no*; 預設值：**no**) | 指定在使用 DoH 伺服器時是否驗證它。將使用 "/certificate" 列表來驗證伺服器有效性。 |
| **vrf** (vrf; 預設值：main) | 指定應使用 DNS 解析器的 VRF。DNS 解析器僅處理來自指定 VRF 或來自解析器本身的請求。 |

```text
[admin@MikroTik] > ip dns print         
                      servers: 
              dynamic-servers: 10.155.0.1
               use-doh-server: 
              verify-doh-cert: no
   doh-max-server-connections: 5
   doh-max-concurrent-queries: 50
                  doh-timeout: 5s
        allow-remote-requests: yes
          max-udp-packet-size: 4096
         query-server-timeout: 2s
          query-total-timeout: 10s
       max-concurrent-queries: 100
  max-concurrent-tcp-sessions: 20
                   cache-size: 2048KiB
                cache-max-ttl: 1d
                   cache-used: 48KiB
```

動態 DNS 伺服器來自 RouterOS 中可用的不同設施，例如 DHCP 用戶端、VPN 用戶端、IPv6 路由器通告等。

伺服器按佇列順序處理——靜態伺服器作為有序列表，動態伺服器作為有序列表。當 DNS 快取必須向伺服器傳送請求時，它會逐一嘗試伺服器，直到其中一個響應。之後，該伺服器將用於所有型別的 DNS 請求。同一伺服器用於任何型別的 DNS 請求，例如 A 和 AAAA 型別。如果僅使用動態伺服器，則 DNS 返回結果可能會在重啟後發生變化，因為由於從上述設施接收速度不同，伺服器可能以不同順序載入到 IP/DNS 設定中。

如果某個時刻正在使用的伺服器變得不可用且無法提供 DNS 應答，則 DNS 快取會重新啟動 DNS 伺服器查詢過程，並再次遍歷指定伺服器列表。

### DNS 快取 {#dns-cache}

此選單提供兩個列表，其中包含儲存在伺服器上的 DNS 記錄：

- *"*`/ip/dns/cache`*"*：此選單提供 RouterOS 快取可用來回復用戶端請求的已快取 DNS 條目列表；
- *"*`/ip/dns/cache/all`*"*：此選單提供儲存的所有已快取 DNS 記錄的完整列表，包括例如 PTR 記錄。

:::tip
可以使用以下命令清空 DNS 快取：`/ip/dns/cache/flush`。

:::

### DNS 靜態 {#dns-static}

MikroTik RouterOS DNS 快取具有附加的內嵌 DNS 伺服器功能，允許你配置多種型別的 DNS 條目，供將路由器用作 DNS 伺服器的 DNS 用戶端使用。此功能還可用於向網路用戶端提供虛假 DNS 資訊。例如，它可以將針對特定域名集合（或整個網際網路）的任何 DNS 請求解析到你自己的頁面。

```text
[admin@MikroTik] /ip/dns/static/add name=www.mikrotik.com address=10.0.0.1

```

該伺服器還能夠基於基本正則表示式解析 DNS 請求，以便多個請求可以匹配同一條目。如果某個條目不遵循 DNS 命名標準，則將其視為正則表示式。列表按從上到下的順序檢查。先檢查正則表示式，然後檢查普通記錄。

使用正則表示式匹配 DNS 請求：

```text
[admin@MikroTik] /ip/dns/static/add regexp=".*mikrotik.*" address=10.0.0.2
```

如果 DNS 靜態條目列表匹配所請求的域名，則路由器將假定此路由器負責該名稱的任何型別 DNS 請求。例如，如果列表中只有 "A" 記錄，但路由器收到 "AAAA" 請求，那麼它會使用靜態列表中的 "A" 記錄進行回覆，並向上遊伺服器查詢 "AAAA" 記錄。如果存在記錄，則轉發該回復；如果不存在，則路由器會回覆一個不含任何記錄的 "ok" DNS 回覆。如果你想用不可用記錄覆蓋來自上游伺服器的域名記錄，那麼可以例如為特定域名新增靜態條目，併為其指定一個虛擬 IPv6 地址 "::ffff"。

將所有已配置 DNS 條目列為有序列表：

```text
[admin@MikroTik] /ip/dns/static/print 
Columns: NAME, REGEXP, ADDRESS, TTL
# NAME             REGEXP       ADDRESS   TTL
0 www.mikrotik.com               10.0.0.1  1d 
1                  [*mikrotik*]  10.0.0.2  1d
```

| 屬性 | 描述 |
| :-- | :-- |
| **address** (*IPv4/IPv6*) | 用於 "A" 或 "AAAA" 型別記錄的地址。 |
| **cname**(*string**)* | 域名的別名。 |
| **forward-to** | 特定 DNS 請求必須轉發到的域名伺服器的 IP 地址。 |
| **mx-exchange** (*string*) | MX 伺服器的域名。 |
| **name** (*string)* | 域名。 |
| **srv-port** (*integer*; 預設值：0) | 服務所在的 TCP 或 UDP 埠。 |
| **srv-target** | 提供服務的機器的規範主機名，以點結尾。 |
| **text** (*string**)* | 關於域名的文字資訊。 |
| **type**(*A* \| *AAAA* \| *CNAME* \| *FWD* \| *MX* \| *NS* \| *NXDOMAIN* \| *SRV* \| *TXT* ; 預設值：*A*) | DNS 記錄的型別。 |
| **address-list** (*string**)* | 當某些請求匹配該條目時，必須將地址動態新增到的防火牆地址列表名稱。TTL 到期後，該條目將從地址列表中移除。 |
| **comment**(*string**)* | 關於域名記錄的註釋。 |
| **disabled** (*yes* \| *no*; 預設值：yes) | DNS 記錄是否處於活動狀態。 |
| **match-subdomain** (*yes* \| *no*; 預設值：no) | 該記錄是否匹配子域請求。 |
| **mx-preference** (*integer*; 預設值：0) | 特定 MX 記錄的優先順序。 |
| **ns**(*string*) | 特定記錄的權威域名伺服器名稱。 |
| **regexp** (regex) | 用於驗證域名的正則表示式。 |
| **srv-priority** (*integer*; 預設值：0) | 特定 SRV 記錄的優先順序。 |
| **srv-weight** (*integer*; 預設值：0) | 特定 SRV 記錄的權重。 |
| **ttl** (*time*; 預設值：*24h*) | 快取記錄的最大生存時間。 |

:::info
對於每個靜態 A 和 AAAA 記錄，快取中會自動新增一條 PTR 記錄。

:::

:::warning
Regexp 區分大小寫，但 DNS 請求不區分大小寫，因此 RouterOS 在匹配任何靜態條目之前會將 DNS 名稱轉換為小寫。你應該只使用小寫字母編寫正則表示式。正則表示式匹配比純文字條目慢得多，因此建議儘量減少正則表示式規則的數量並最佳化表示式本身。

:::

:::warning
透過混合使用者介面（CLI 和 GUI）配置 regex 時要小心。從 CLI 新增條目本身可能需要跳脫字元。建議新增條目並執行 print 命令，以驗證 regex 在新增期間未被更改。

:::

## DNS over HTTPS (DoH) {#dns-over-https-doh}

RouterOS 支援 DNS over HTTPS (DoH)。DoH 使用 HTTPS 協定傳送和接收 DNS 請求，以獲得更好的資料完整性。主要目標是透過消除 "中間人" 攻擊 (MITM) 來提供隱私保護。

[影片：DoH 設定](http://youtube.com/watch?v=w4erB0VzyIE)

配置 DoH 伺服器：

```ros
/ip/dns/set use-doh-server=DoH_Server_Query_URL verify-doh-cert=yes
```

:::info
可以使用[內建證書頒發機構儲存](../authentication-authorization-accounting/certificates.md#built-in-trust-store-authorities)來驗證 DoH 伺服器證書，而無需手動匯入相關的根證書。
:::

:::info
僅支援一個 DoH 伺服器。

:::

請注意，路由器至少需要配置一個常規 DNS 伺服器，才能解析 DoH 主機名本身。

```ros
/ip/dns/set servers=1.1.1.1
```

如果未配置任何動態或靜態 DNS 伺服器，請按如下方式為 DoH 伺服器域名新增靜態 DNS 條目：

```ros
/ip/dns/static/add address=IP_Address name=Domain_Name
```

:::tip
如果正在使用 DoH 伺服器（DoH DNS 名稱可被解析），那麼它將是當時唯一工作的 DNS 服務，IP/DNS 伺服器列表中的標準 DNS 伺服器將不會被使用。

:::

:::tip
如果 *`/certificate/settings/set` crl-use* 設定為 *yes,* 則 RouterOS 會檢查證書鏈中每個證書的 CRL，因此應將整個證書鏈安裝到裝置中——從根 CA、中間 CA（如果有）開始，直到用於特定服務的證書。

例如，Google DoH、Cloudflare 和 OpenDNS 的完整證書鏈包含三個證書，NextDNS 有四個證書。

:::
:::info
ARM64、x86 和 CHR 裝置在與 DoH 伺服器通訊時會協商 HTTP/2。如果伺服器支援，路由器會使用 HTTP/2 進行 DNS over HTTPS 查詢，與 HTTP/1.1 相比可提供更好的多路複用並降低延遲。如果任一端不支援 HTTP/2，則連接回退到 HTTP/1.1。

:::

### 已知相容/不相容的 DoH 服務 {#known-compatibleincompatible-doh-services}

#### 相容的 DoH 服務 {#compatible-doh-services}

- Cloudflare
- Google
- NextDNS
- OpenDNS

#### 不相容的 DoH 服務 {#incompatible-doh-services}

- Mullvad
- Yandex
- UncensoredDNS
- Quad9

## Adlist {#adlist}

Adlist 是網路級廣告攔截的重要組成部分，包含一組精選的已知用於提供廣告的域名。此功能透過利用 Domain Name System (DNS) 解析來攔截對這些域名的 A 和 AAAA 請求。當用戶端裝置向 DNS 伺服器查詢 Adlist 中列出的域名時，DNS 解析過程會改變。DNS 伺服器不會返回廣告服務域名的實際 IP 地址，而是返回 IP 地址 0.0.0.0。這會有效地將請求空路由，因為 0.0.0.0 是不可路由的元地址，用於表示無效、未知或不適用目標。透過以這種方式重定向廣告相關請求，Adlist 功能可確保廣告內容不會載入，從而透過減少不需要的廣告流量來增強網路效能並改善使用者體驗。

[影片：Adlist 設定](http://youtube.com/watch?v=RMJnjyAOfLI)

:::warning
**配置之前，請增加 DNS 快取，因為它用於儲存 Adlist 條目。如果達到限制，DNS,error 主題中會列印錯誤 "*adlist read: max cache size reached*"**

:::

:::warning
Adlist 儲存在裝置的內部儲存器中。請確保有足夠的可用空間來儲存所需的 Adlist。

:::

| 屬性 | 描述 |
| :-- | :-- |
| url | 用於指定 Adlist 的 URL。 |
| ssl-verify | 指定是否驗證 Adlist URL 伺服器的 SSL 證書。將使用 "/certificate" 列表來驗證伺服器有效性。 |
| match-count | 匹配的 DNS 名稱請求數。 |
| name-count | 從 Adlist 匯入的 DNS 名稱數。 |
| file | 用於指定從中讀取 Adlist 資料的本地檔案路徑。 |
| pause | 暫時暫停使用所有 Adlist。 |
| reload | 檢查所有列表的更新；如果發現更新，則更新列表，按需移除或新增條目；執行 reload 時不會完整重新下載列表，而是隻進行必要的更新。**重要：** 更新列表並不強制使用 reload，Adlist 每四小時檢查一次新更新。 |

### Adlist 白名單 {#whitelist-for-adlist}

要將某些域從 Adlist 中豁免，需要建立一個靜態 DNS FWD 條目，例如 `/ip/dns/static/add name=bar.test type=FWD`。如果存在這樣的條目，並且路由器有相關的靜態 DNS 條目 `/ip/dns/static/add name=bar.test type=A`，則查詢將由路由器應答；或者，如果沒有靜態規則，則轉發到下一個 DNS（動態 DNS 或 `/ip/dns/set servers=` 下配置的 DNS）。DoH 也支援 FWD 條目。

### 配置示例 {#configuration-examples}

#### 基於 URL 的 Adlist {#url-based-adlist}

```ros
/ip/dns/adlist/add url=https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts ssl-verify=no
```

要檢視存在並匹配了多少個域名，可以執行：

```ros
/ip/dns/adlist/print 
Flags: X - disabled 
0 url="https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts" ssl-verify=no match-count=122 name-count=164769

```

#### 本地託管的 Adlist {#locally-hosted-adlist}

要建立 Adlist，可以建立一個包含域名的文字檔案。例如：

```
0.0.0.0 example1.com
0.0.0.0 eu1.example.com
0.0.0.0 ex.com
0.0.0.0 com.example.com
```

:::info
可以在 PC 上建立 txt 檔案，也可以在 RouterOS 中使用以下命令建立：

"/file/add name=host.txt"，然後在新增條目後執行 "/file/edit host.txt contents"。按 "ctrl o" 儲存條目。

:::

要將檔案新增到 Adlist：

```ros
/ip/dns/adlist/add file=host.txt

```

:::info
可以使用 `/ip/dns/adlist/print` 驗證檔案格式是否正確，結果將顯示已新增多少個主機名；主機名格式必須與上一示例中給出的格式一致。

:::

```ros
/ip/dns/adlist/print 
Flags: X - disabled 
 0   file=host.txt match-count=0 name-count=4 
```

## 轉發器 {#forwarders}

DNS Forwarders 允許使用者配置一個命名 DNS 轉發器，可用作靜態 FWD 條目的 *forward-to* 值。

對於每個 *Forwarder*，可以配置多個常規上游伺服器和 DoH 伺服器。配置的 *forwarder* 伺服器將按輪詢演算法使用——對於每個查詢，將使用下一個伺服器來解析 DNS 名稱。

### 轉發器配置 {#forwarder-configuration}

在 *`/ip/dns/forwarders`* 部分中，可以新增、修改或刪除 *forwarders*。

| 屬性 | 描述 |
| :-- | :-- |
| **name** (*string;* 預設值： ) | 轉發器名稱。 |
| **dns-servers** (*string*; 預設值： ) | 域名伺服器的 IP 地址或 DNS 名稱。可以包含多個記錄，例如 *dns-servers=1.1.1.1,8.8.8.8,local.dns* |
| **doh-servers**(*string;* 預設值： ) | DoH 伺服器的 URL。可以包含多個記錄。 |
| **verify-doh-cert** (*yes* \| *no**;* 預設值： *yes*) | 指定在使用 DoH 伺服器時是否驗證它。將使用 "/certificate" 列表來驗證伺服器有效性。 |

### 配置示例 {#configuration-example}

配置/新增一個 *forwarder*：

```routeros
/ip/dns/forwarders
add dns-servers=1.1.1.1,local.dns doh-servers=https://dns.google/dns-query name=forwarder1
```

配置/新增一個靜態 DNS FWD 條目：

```routeros
/ip/dns/static
add forward-to=forwarder1 name=mikrotik.com type=FWD
```

現在，每當路由器收到解析 [mikrotik.com](http://mikrotik.com) 的請求時，該請求將使用輪詢演算法轉發到 *1.1.1.1*、*local.dns* 或 *Google DoH* 伺服器。

## mDNS {#mdns}

RouterOS 支援[多播 DNS (mDNS)](https://datatracker.ietf.org/doc/html/rfc6762)，用於本地網路服務發現。預設情況下，mDNS 在單個子網內執行。mDNS 中繼功能允許使用 "mdns-repeat-ifaces" 屬性將 mDNS 功能擴充套件到不同介面或 VLAN。

### 使用 mDNS 中繼的影響 {#impact-of-using-mdns-repeater}

- 跨子網服務發現：不同子網或 VLAN 上的裝置可以相互發現，從而增強查詢服務（例如印表機、檔案共享）的能力。
- 網路流量增加：mDNS 中繼可能會增加多播流量，這可能導致擁塞，尤其是在裝置眾多的大型網路中。

mDNS 中繼通常用於以下裝置：

- Apple 生態系統（AirPrint、AirPlay）。
- 智慧家居裝置（Thread、IoT）。
- Chromecast 和媒體串流。
- Avahi（Linux/Unix）。

要在介面之間啟用 mDNS 中繼，使連線到這些介面的裝置能夠使用 mDNS 相互發現，請使用以下命令：

```routeros
/ip/dns/set mdns-repeat-ifaces=<interface1>,<interface2>
```

:::info
mDNS 中繼需要支援多播的介面（例如 Ethernet、VLAN、bridge）。不支援 WireGuard 等隧道介面。

目前僅支援 IPv4。

:::

:::warning
MikroTik mDNS Repeater 是一個本地服務，會攔截多播封包並重新廣播它們。它需要一條 "input" 規則。mDNS 多播流量不會經過 "forward" 鏈。如果你的防火牆規則較嚴格，用於保護路由器免受本地子網訪問，則必須在任何丟棄規則之前顯式允許 mDNS 流量——允許在 "input" 鏈上接收 UDP 埠 5353 的流量。

:::
