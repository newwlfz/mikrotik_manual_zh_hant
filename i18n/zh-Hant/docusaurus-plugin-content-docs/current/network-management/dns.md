---
sidebar_key: "network-management/dns"
sidebar_position: 3
title: "DNS"
sidebar_label: "DNS"
description: "RouterOS DNS 解析器：將路由器用作網路的 DNS 伺服器，檢查並排查其問題，新增本地名稱，將域名傳送到其他伺服器，在防火牆中使用域名，使用 adlists 攔截廣告，使用 DNS over HTTPS，並在網路之間中繼 mDNS。"
tags:
  - 'dns'
  - 'doh'
  - 'adlist'
  - 'mdns'
source: https://manual.mikrotik.com/docs/network-management/dns
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

RouterOS 具有快取 DNS 解析器。路由器將其用於自身的查詢，並且它可以作為網路中裝置的 DNS 伺服器：它向上遊 DNS 伺服器（例如 ISP 的伺服器）發起查詢，並將它們的應答儲存在快取中。

在預設配置下，這已經可以正常工作，無需更改任何內容。以下各節介紹設定方法、檢查方法以及額外任務，例如本地名稱和廣告攔截。這些附加功能僅適用於將路由器用作其 DNS 伺服器的裝置：從 DHCP 獲取其他 DNS 伺服器（例如 1.1.1.1）的裝置會繞過路由器的靜態條目和廣告列表。

## 將路由器用作網路的 DNS 伺服器 {#use-the-router-as-the-dns-server-for-your-network}

預設配置已經執行此操作。要自行設定：

1. 允許路由器應答網路中的裝置：

   ```ros
   /ip/dns/set allow-remote-requests=yes
   ```

2. 將路由器地址作為 DNS 伺服器提供給 DHCP 用戶端：在 `/ip/dhcp-server/network` 中設定 `dns-server`，例如設定為 192.168.88.1（參見 [DHCP 伺服器](./dhcp/server.md)）。

路由器從其他服務獲取上游伺服器，例如透過 WAN 埠上的 DHCP 用戶端從 ISP 獲取。它們會在 `/ip/dns/print` 中顯示為 `dynamic-servers`。要使用其他上游伺服器，請在 `servers` 中設定它們。路由器會先嚐試它們，再嘗試動態伺服器：

```ros
/ip/dns/set servers=1.1.1.1,9.9.9.9
```

使用 `allow-remote-requests=yes` 時，路由器會在其所有地址的 UDP 和 TCP 埠 53 上應答 DNS 查詢。預設防火牆會丟棄來自網際網路的這些查詢。如果使用自己的防火牆規則，也請丟棄它們，以免路由器成為網際網路上任何人都能使用的開放解析器：

```ros
/ip/firewall/filter/add chain=input in-interface-list=WAN protocol=udp dst-port=53 action=drop comment="drop DNS from WAN"
/ip/firewall/filter/add chain=input in-interface-list=WAN protocol=tcp dst-port=53 action=drop comment="drop DNS from WAN"
```

## 檢查與故障排除 {#check-and-troubleshoot}

要在路由器本身上測試名稱：

```ros
:put [:resolve mikrotik.com]
```

要從網路中的計算機將路由器作為 DNS 伺服器進行測試，請直接向它查詢，例如使用 `nslookup mikrotik.com 192.168.88.1`。

DNS 伺服器的應答具有狀態：

- `NOERROR`：名稱存在。當該名稱沒有所請求型別的記錄時，應答仍可能不包含任何記錄。
- `NXDOMAIN`：名稱不存在。
- `SERVFAIL`：路由器無法獲得應答，例如因為沒有上游伺服器及時應答。

路由器會按其生存時間（TTL）將應答儲存在快取中。要檢視快取的應答，或在更改後清空快取：

```ros
/ip/dns/cache/print
/ip/dns/cache/flush
```

路由器會在 `dns` 主題中記錄 DNS 錯誤，例如關於 DoH 伺服器或廣告列表匯入的錯誤：

```ros
/log/print where topics~"dns"
```

如果裝置完全得不到應答，請檢查 `allow-remote-requests` 和防火牆規則。如果某個名稱解析為 `0.0.0.0`，則廣告列表在路由器上或上游伺服器上阻止了它。

## 本地名稱 {#local-names}

靜態條目由路由器自身應答名稱，例如用於網路中的裝置：

```ros
[admin@MikroTik] > /ip/dns/static/add name=nas.lan address=192.168.88.20
[admin@MikroTik] > /ip/dns/static/add name=printer.lan address=192.168.88.21
[admin@MikroTik] > /ip/dns/static/add name=example.lan address=192.168.88.30 match-subdomain=yes
[admin@MikroTik] > /ip/dns/static/print
Columns: NAME, TYPE, ADDRESS, TTL
# NAME         TYPE  ADDRESS        TTL
0 nas.lan      A     192.168.88.20  1d
1 printer.lan  A     192.168.88.21  1d
2 example.lan  A     192.168.88.30  1d
```

- IPv6 地址會生成 AAAA 條目。
- 路由器還會應答這些地址的反向查詢（PTR）。
- 使用 `match-subdomain=yes` 時，條目會為該名稱及其下的每個名稱應答，例如 `www.example.lan`。

當 DHCP 伺服器和 IP 鄰居發現功能的 `add-dns-entries` 設定開啟時，它們會自動新增靜態條目，並標記為 `D`（動態）。參見 [DHCP 伺服器](./dhcp/server.md) 和 [`/ip/neighbor/discovery-settings`](../cli-reference/ip/neighbor/discovery-settings.md)。

## 將域傳送到另一臺 DNS 伺服器 {#send-a-domain-to-another-dns-server}

`FWD` 條目會將針對某個名稱的查詢傳送到另一臺 DNS 伺服器，而不是正常的上游伺服器，例如將公司網路的名稱傳送到公司的 DNS 伺服器：

```ros
/ip/dns/static/add name=corp.example.com type=FWD forward-to=10.0.0.53 match-subdomain=yes
```

`forward-to` 接受 IP 地址、DNS 名稱或轉發器的名稱。沒有 `forward-to` 時，`FWD` 條目會將查詢傳送到正常的上游伺服器。

轉發器是用於 `FWD` 條目的 DNS 和 DoH 伺服器的命名組。路由器會依次將每個查詢傳送到組中的下一臺伺服器：

```ros
/ip/dns/forwarders/add name=branch dns-servers=10.1.0.53,10.1.1.53
/ip/dns/static/add name=branch.example.com type=FWD forward-to=branch match-subdomain=yes
```

路由器不會跳過轉發器中停止應答的伺服器：到達該伺服器的查詢會失敗。只新增可正常工作的伺服器。

## 在防火牆規則中使用域名 {#use-domain-names-in-firewall-rules}

使用 `address-list` 時，路由器會將其為某個條目應答的地址新增到防火牆地址列表。對於 `FWD` 條目，這些是上游應答中的地址：

```ros
/ip/dns/static/add name=example.com type=FWD address-list=example-com match-subdomain=yes
```

網路中的裝置透過路由器查詢 `example.com` 後，列表將包含應答中的地址：

```ros
[admin@MikroTik] > /ip/firewall/address-list/print where list=example-com
Flags: D - DYNAMIC
Columns: LIST, ADDRESS, CREATION-TIME
#   LIST         ADDRESS        CREATION-TIME
;;; created for example.com.
0 D example-com  198.51.100.10  2026-09-24 12:32:52
;;; created for example.com.
1 D example-com  198.51.100.11  2026-09-24 12:32:52
```

在防火牆規則中使用該列表，或在 mangle 規則中使用它來以不同方式路由某個域的流量（參見 [策略路由](../user-guides/routing-and-networking-protocols/policy-routing.md)）。當應答的 TTL 過去後，再加上 `/ip/dns` 中的 `address-list-extra-time`，路由器會移除條目。只有裝置的查詢會新增條目。路由器自身的查詢（例如使用 `:resolve`）不會新增。

## 使用廣告列表攔截廣告 {#block-ads-with-adlists}

廣告列表是一組域名列表，例如廣告和跟蹤伺服器，路由器會阻止這些域名。它對這些名稱的 A 查詢返回 `0.0.0.0`，對 AAAA 查詢返回 `::`，因此裝置無法訪問它們。

路由器會將廣告列表儲存在 DNS 快取中，因此請在新增列表前提高 `cache-size`。約 75 000 個名稱的列表需要約 6 MiB；示例也為正常快取留出了空間：

```ros
[admin@MikroTik] > /ip/dns/set cache-size=16384
[admin@MikroTik] > /ip/dns/adlist/add url=https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts
[admin@MikroTik] > /ip/dns/adlist/print
0  url="https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts"
   match-count=0 name-count=76524
```

`name-count` 顯示路由器匯入了多少個名稱，`match-count` 顯示該列表攔截了多少個查詢。

當快取太小時，路由器會停止匯入並記錄 `adlist read: max cache size reached`。之後提高 `cache-size` 不會補全列表。請移除該廣告列表並重新新增。

廣告列表也可以是路由器上的檔案，每行一個名稱，採用 hosts 檔案格式或純名稱：

```ros
/file/add name=adlist.txt contents="0.0.0.0 ads.example.net\ntracker.example.net\n"
/ip/dns/adlist/add file=adlist.txt
```

要停止阻止某個名稱，請為其新增 `FWD` 條目。路由器隨後會將其查詢傳送到上游伺服器：

```ros
/ip/dns/static/add name=ads.example.net type=FWD
```

要暫時停止所有廣告列表，例如停止 10 分鐘：

```ros
/ip/dns/adlist/pause duration=10m
```

[影片：Adlist 設定](https://youtube.com/watch?v=RMJnjyAOfLI)

## DNS over HTTPS {#dns-over-https}

使用 DNS over HTTPS（DoH）時，路由器會透過 HTTPS 將其上游查詢加密傳送到一臺 DoH 伺服器：

```ros
/ip/dns/set use-doh-server=https://cloudflare-dns.com/dns-query verify-doh-cert=yes
```

保留 `servers` 或 `dynamic-servers`，或為 DoH 伺服器的主機名新增靜態條目：路由器會透過其正常 DNS 伺服器查詢該名稱。使用 `verify-doh-cert=yes` 時，路由器會根據內建信任儲存和 `/certificate` 中的證書檢查伺服器證書（參見 [證書](../authentication-authorization-accounting/certificates.md#built-in-trust-store-authorities)）。

某些 DoH 服務需要 HTTP/2，只有 ARM64 和 x86 裝置（包括 CHR）支援：

- Cloudflare、Control D、Google、NextDNS 和 OpenDNS 可在所有裝置上工作。
- Mullvad、Quad9 和 UncensoredDNS 僅在 ARM64 和 x86 裝置上工作。

設定 DoH 伺服器後，路由器會將所有上游查詢傳送到它，並且不會回退到正常 DNS 伺服器。無法訪問 DoH 伺服器時，裝置會得到 `SERVFAIL`。`FWD` 條目會繼續使用它們自己的伺服器。

[影片：DoH 設定](https://youtube.com/watch?v=w4erB0VzyIE)

## 更多記錄型別和正則表示式 {#more-record-types-and-regular-expressions}

靜態條目還可以包含其他記錄型別：

- `CNAME` 為名稱提供別名。路由器會將其與目標的地址一起應答，目標地址可以來自靜態條目或上游：`/ip/dns/static/add name=files.lan type=CNAME cname=nas.lan`。
- `NXDOMAIN` 使名稱不存在，適用於所有記錄型別：`/ip/dns/static/add name=tracker.example.com type=NXDOMAIN`。
- `MX` 指定域的郵件伺服器：`/ip/dns/static/add name=lan type=MX mx-exchange=mail.lan mx-preference=10`。
- `TXT` 儲存文字：`/ip/dns/static/add name=lan type=TXT text="managed by RouterOS"`。

要使用一個條目匹配多個名稱，請使用正則表示式代替 `name`：

```ros
/ip/dns/static/add regexp="^host[0-9]+\\.lan\$" address=192.168.88.40
```

路由器會以小寫形式將表示式與名稱匹配，因此請使用小寫編寫。在命令列中，反斜槓寫作 `\\`，`$` 寫作 `\$`：上面的條目儲存為 `^host[0-9]+\.lan$`。

為每個名稱和記錄型別只建立一個條目。當多個條目匹配同一個名稱時，例如一個帶有 `match-subdomain=yes` 的條目和一個針對其下名稱的條目，列表順序並不決定由哪個條目應答。

## mDNS 中繼器 {#mdns-repeater}

多播 DNS（mDNS）使裝置能夠在本地網路中相互發現，例如印表機（AirPrint）、媒體播放器（AirPlay、Chromecast）和智慧家居裝置。mDNS 停留在單個網路中。mDNS 中繼器會在你列出的介面之間轉發它，因此不同網路或 VLAN 中的裝置可以相互發現：

```ros
/ip/dns/set mdns-repeat-ifaces=bridge,vlan20
```

使用承載多播的介面，例如 Ethernet、VLAN、bridge 或 EoIP 介面。中繼會向每個列出的網路新增多播流量。

路由器自身接收 mDNS 封包，因此它們會經過防火牆的 input 鏈。預設防火牆會在 `LAN` 介面列表中的介面上接受它們。如果你的 input 規則在某個列出的介面上丟棄 UDP 埠 5353，例如某個不在 `LAN` 中的 VLAN，請在丟棄流量的規則之前新增此規則：

```ros
/ip/firewall/filter/add chain=input protocol=udp dst-port=5353 action=accept comment="accept mDNS"
```

## 技術細節 {#technical-details}

### 路由器如何應答查詢 {#how-the-router-answers-a-query}

路由器的應答取決於該名稱存在的條目：

| 該名稱的條目 | 應答 |
| :-- | :-- |
| 無 | 來自快取或上游伺服器。 |
| 靜態條目，例如 A | 來自該條目，針對其記錄型別。其他記錄型別來自上游；當上遊沒有時，路由器返回不帶記錄的 `NOERROR`。 |
| 名稱位於廣告列表中 | A 返回 `0.0.0.0`，AAAA 返回 `::`，即使存在靜態 A 或 AAAA 條目也是如此。其他記錄型別來自上游。 |
| `FWD` 條目 | 來自 `forward-to` 伺服器，或來自上游伺服器。廣告列表不適用。 |
| `FWD` 和 A 條目 | 來自 A 條目。 |
| `NXDOMAIN` 條目 | 對所有記錄型別返回 `NXDOMAIN`。 |

名稱以小寫形式匹配。快取使用剩餘 TTL 應答。

### 上游伺服器 {#upstream-servers}

- 路由器會先按順序嘗試靜態 `servers`，然後嘗試 `dynamic-servers`，例如啟用了 `use-peer-dns=yes` 的 DHCP 用戶端的伺服器。
- 路由器會等待 `query-server-timeout` 以獲得應答，然後才嘗試下一臺伺服器。當某臺伺服器應答後，路由器會在後續查詢中繼續使用它。
- 當沒有伺服器在 `query-total-timeout` 內應答時，裝置會得到 `SERVFAIL`。
- 當有 `max-concurrent-queries` 個查詢正在等待上游應答時，路由器會丟棄新查詢，包括它本可以從快取應答的查詢，直到其中一個等待的查詢完成。
- `/ip/dns` 中的更改會立即生效。此時到達的查詢可能保持未應答，裝置會再次傳送它。快取會保留。

### 快取 {#cache}

- `cache-max-ttl` 限制上游應答的 TTL。靜態條目使用自己的 `ttl`，預設為 1 天。
- 廣告列表會計入 `cache-size`：每個名稱需要約 75 位元組。
- `/ip/dns/cache` 列出路由器給出的應答。`/ip/dns/cache/all` 還會列出它儲存的其他記錄，例如靜態條目的 PTR 記錄。正則表示式條目沒有 PTR 記錄。

### 廣告列表 {#adlists}

- 每行一個名稱，可以單獨出現，也可以跟在地址（`0.0.0.0`、`127.0.0.1` 或 `::1`）之後，如同 hosts 檔案中的寫法。以 `#` 開頭的行以及行尾都是註釋。名稱必須為小寫，不支援 `*.example.com` 之類的萬用字元。
- 只阻止所列出的名稱，不會阻止其下方的名稱。被阻止的應答 TTL 為 2 秒。
- 停用 adlist 不會釋放其名稱佔用的快取記憶體；這些名稱仍計入 `cache-size`。只有移除該列表才會釋放。
- 路由器會驗證 HTTPS adlist URL 的證書（`ssl-verify=yes`）。對於使用自簽名證書的伺服器，請將其 CA 證書匯入 `/certificate`，或設定 `ssl-verify=no`。
- 路由器每 4 小時檢查所有列表是否有變更；`/ip/dns/adlist/reload` 會立即檢查。路由器將列表儲存在其磁碟上。
- 一臺路由器最多可擁有 64 個 adlist。

### DNS over HTTPS {#dns-over-https-1}

- 路由器會保持一條到 DoH 伺服器的 HTTPS 連線（TCP 埠 443），並透過它傳送所有查詢。
- 在 ARM64 和 x86 裝置上，當伺服器支援時，路由器使用 HTTP/2。其他裝置使用 HTTP/1.1。
- DoH 錯誤會記錄在 `dns` 主題中，例如 `DoH server connection error: timeout connecting`。

### 轉發器 {#forwarders}

- 轉發器的伺服器會在 `dns-servers` 和 `doh-servers` 之間輪流處理查詢，每次一個。傳送到不應答伺服器的查詢會在 `query-total-timeout` 後失敗。
- 對於轉發器，`verify-doh-cert` 預設開啟，這一點與 `/ip/dns` 中不同。

### VRF {#vrf}

- 解析器會應答 `vrf` 中所設定 VRF 內的裝置，預設為 `main`。其他 VRF 中的裝置得不到應答。
- 上游伺服器透過主路由表訪問。要訪問另一個 VRF 中的伺服器，請將其寫為 `address@vrf`，例如 `servers=10.0.0.1@vrf1`。

### mDNS 中繼器 {#mdns-repeater-1}

- 路由器中繼 IPv4 mDNS（UDP 埠 5353 到 224.0.0.251），並在其他介面上從其自身地址傳送這些封包。IPv6 mDNS（ff02::fb）不會中繼。
- 諸如 WireGuard 的三層隧道不承載多播，因此無法透過它們中繼 mDNS。

有關所有屬性，請參見 CLI 參考中的 [`/ip/dns`](../cli-reference/ip/dns/index.md)、[`/ip/dns/static`](../cli-reference/ip/dns/static.md)、[`/ip/dns/adlist`](../cli-reference/ip/dns/adlist/index.md) 和 [`/ip/dns/forwarders`](../cli-reference/ip/dns/forwarders.md)。
