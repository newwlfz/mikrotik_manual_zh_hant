---
title: "HotSpot - 強制入口網站"
description: "MikroTik HotSpot Gateway 可為公用網路提供用戶端驗證，並具備 DHCP 位址集區、多種驗證方法與 walled-garden 存取等功能。它需要 IPv4，且有特定的路由限制，並提供設定範例供安裝時參考。"
tags:
  - 'hotspot'
  - 'firewall'
  - 'dhcp'
source: https://manual.mikrotik.com/docs/7.24/authentication-authorization-accounting/hotspot-captive-portal
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

MikroTik HotSpot Gateway 會在用戶端存取公用網路前提供驗證。

:::warning
Hotspot（captive portal）會使用 web-proxy，目前僅能使用預設路由表，因此 PCC（per connection-classifier）不是有效的方法，因為它會使用多個路由表。
:::

:::warning
HotSpot 功能可能會被 device-mode 封鎖。設定 HotSpot 前，請確認它已在 `/system/device-mode` 中啟用（[更多資訊](/docs/system-information-and-utilities/device-mode)。
:::

### HotSpot 屬性 {#hotspot-properties}

| 屬性 | 說明 |
| :--- | :--- |
| **name** | HotSpot 伺服器實例的描述性名稱。 |
| **interface** | HotSpot 服務會監聽用戶端要求的特定本機介面（實體或虛擬）。 |
| **address-pool** | HotSpot 用戶端透過 DHCP 取得 IP 位址的 IP 位址集區。 |
| **profile** | HotSpot Server Profile 的參考，其中包含登入方法與 HTML 目錄等通用設定。 |
| **idle-timeout** | 閒置期間，若未偵測到流量，用戶端會自動登出。 |
| **keepalive-timeout** | 用來檢查用戶端是否仍可連線的時間間隔；若用戶端沒有回應，工作階段就會終止。 |
| **login-timeout** | 登入頁面顯示後，允許用戶端完成驗證程序的最長時間。 |
| **addresses-per-mac** | 限制可與單一 MAC 位址建立關聯的 IP 位址數量。 |
| **proxy-status** | 指出 HotSpot 系統使用的內部 web-proxy 目前運作狀態。 |

### HotSpot Gateway 功能 {#hotspot-gateway-features}

- 多種用戶端驗證方法，可使用路由器上的本機用戶端資料庫或遠端 RADIUS 伺服器。
- 使用者計費，可記錄在路由器上的本機資料庫或遠端 RADIUS 伺服器中。
- walled-garden 系統，可未經授權存取部分網頁。
- 登入頁面修改，可在其中放入公司資訊。
- 自動且透明地將用戶端的任何 IP 位址變更為有效位址。
- HotSpot 可通知 DHCP 用戶端它們位於 captive portal 後方（RFC7710）。

Hotspot 只有在使用 IPv4 時才能可靠運作。Hotspot 依賴 Firewall NAT 規則，而目前不支援 IPv6。

## 範例 {#example}

```ros
[admin@MikroTik] /ip/hotspot> setup 
Select interface to run HotSpot on 

hotspot interface: ether3
Set HotSpot address for interface 

local address of network: 10.5.50.1/24
masquerade network: yes
Set pool for HotSpot addresses 

address pool of network: 10.5.50.2-10.5.50.254
Select hotspot SSL certificate 

select certificate: none
Select SMTP server 

ip address of smtp server: 0.0.0.0
Setup DNS configuration 

dns servers: 10.1.101.1
DNS name of local hotspot server 

dns name: myhotspot
Create local hotspot user 

name of local hotspot user: admin
password for the user: 
[admin@MikroTik] /ip/hotspot>
```

## 驗證 HotSpot 設定 {#verify-hotspot-configuration}

```ros
[admin@MikroTik] /ip/hotspot> print 
Flags: X - disabled, I - invalid, S - HTTPS 
# NAME INTERFACE ADDRESS-POOL PROFILE IDLE-TIMEOUT
0 hotspot1 ether3 hs-pool-3 hsprof1 5m 
[admin@MikroTik] /ip/hotspot> 
[admin@MikroTik] /ip/pool> print 
# NAME RANGES 
0 hs-pool-3 10.5.50.2-10.5.50.254 
[admin@MikroTik] /ip/pool> /ip/dhcp-server 
[admin@MikroTik] /ip/dhcp-server> print 
Flags: X - disabled, I - invalid 
# NAME INTERFACE RELAY ADDRESS-POOL LEASE-TIME ADD-ARP
0 dhcp1 ether3 hs-pool-3 1h 
[admin@MikroTik] /ip/dhcp-server> /ip/firewall/nat 
[admin@MikroTik] /ip/firewall/nat> print 
Flags: X - disabled, I - invalid, D - dynamic 
0 X ;;; place hotspot rules here
chain=unused-hs-chain action=passthrough 

1 ;;; masquerade hotspot network
chain=srcnat action=masquerade src-address=10.5.50.0/24 
[admin@MikroTik] /ip/firewall/nat> 
```

### **設定程序期間詢問的參數** {#parameters-asked-during-the-setup-process}

| Parameter | Description |
| :-- | :-- |
| **hotspot interface** (*string*; Default: **allow**) | 要執行 HotSpot 的介面名稱。若要在 bridge 介面上執行 HotSpot，請確認公用介面未包含在 bridge 連接埠中。 |
| **local address of network** (*IP*; Default: **10.5.50.1/24**) | HotSpot 閘道器位址 |
| **masquerade network** (*yes \| no*; Default: **yes**) | 是否偽裝 HotSpot 網路，當為 **yes** 時，會在 *`/ip/firewall/nat`* 新增一條 *action=masquerade* 規則 |
| **address pool of network** (*string*; Default: **yes**) | HotSpot 網路的位址集區，用於將使用者 IP 位址變更為有效位址。適合用於提供網路存取給不願意變更網路設定的行動用戶端。 |
| **select certificate** (*none \| import-other-certificate*; Default: ) | 當需要 HTTPS 授權方法時，選擇 SSL 憑證。 |
| **ip address of smtp server** (*IP*; Default: **0.0.0.0**) | SMTP 伺服器的 IP 位址，HotSpot 網路的 SMTP 要求（TCP 連接埠 25）會重新導向至此 |
| **dns servers** (*IP*; Default: **0.0.0.0**) | HotSpot 用戶端使用的 DNS 伺服器位址，設定取自 HotSpot 閘道器的 *`/ip/dns`* 選單 |
| **dns name** (*string*; Default: **""**) | HotSpot 伺服器的網域名稱，需要完整網域名稱，例如 [www.example.com](http://www.example.com) |
| **name of local hotspot user** (*string*; Default: **"admin"**) | 自動建立的一位 HotSpot 使用者名稱，新增至 *`/ip/hotspot/user`* |
| **password for the user** (*string*; Default: ) | 自動建立的 HotSpot 使用者密碼 |

## HotSpot

**子選單：** `/ip/hotspot`

此選單用於管理路由器的 HotSpot 伺服器。可以在 Ethernet、wireless、VLAN 與 bridge 介面上執行 HotSpot。每個介面只允許一個 HotSpot 伺服器。在 bridge 介面上設定 HotSpot 時，請將 HotSpot 介面設為 bridge 介面，而非 bridge 連接埠，且不要將公用介面加入 bridge 連接埠。您可以手動在 *`/ip/hotspot`* 選單中新增 HotSpot 伺服器，但建議執行 *`/ip/hotspot/setup`*，它會新增所有必要的設定。

| Parameters | Description |
| :-- | :-- |
| **name** (text) | HotSpot 伺服器的名稱或識別碼 |
| **address-pool** (name/none; default: *none*) | 用於將任何 HotSpot 用戶端 IP 位址變更為有效位址的位址空間。適合用於提供公用網路存取給不願意變更網路設定的行動用戶端 |
| **idle-timeout** (time/none; default: *5m*) | 未授權用戶端的閒置期間。當此用戶端沒有流量時（也就是用戶端電腦應已關閉），一旦達到逾時時間，使用者就會從 HotSpot 主機清單中移除，其使用的位址會變為可用 |
| **keepalive-timeout** (time/none; default: *none*) | 主機可保持無法連線多久才會從 HotSpot 移除的值 |
| **login-timeout** (time/none; default: *none*) | 一段時間後，若主機尚未向系統完成授權，該主機項目就會從主機表中刪除。迴圈會持續，直到主機登入系統為止。若有用戶端在主機表中未授權太久後無法登入，請啟用此設定。 |
| **interface** (name of an interface) | 要執行 HotSpot 的介面 |
| **addresses-per-mac** (integer**/**unlimited; default: 2) | 允許多個 HotSpot 用戶端使用同一個 MAC 位址連線時，可與該 MAC 位址綁定的 IP 位址數量 |
| **profile** (name; default: ***default*)** | HotSpot 伺服器的預設 HotSpot profile，位於 *`/ip/hotspot/profile`* |

## Read-only

| Parameters | Description |
| :-- | :-- |
| keepalive-timeout (read-only; time) | 套用至使用者的 keepalive-timeout 實際值。此值顯示主機可保持無法連線多久才會從 HotSpot 移除 |

## HotSpot 設定檔 {#hotspot-profile}

此子選單包含 HotSpot 伺服器設定檔清單。同一閘道器上可以有多種不同的 HotSpot 系統，定義為 Server Profile。一或多個介面可以歸入同一個伺服器設定檔。特定介面上伺服器的設定項目很少，大部分組態都是在伺服器設定檔中設定。例如，可以為每個伺服器設定檔建立完全不同的 servlet 頁面集合，並定義不同的 RADIUS 伺服器進行驗證。

| Property | Description |
| :-- | :-- |
| **dns-name** (*string*; Default: **""**) | HotSpot 伺服器的 DNS 名稱。這是用作 HotSpot 伺服器名稱的 DNS 名稱（也就是會顯示為登入頁面的位置）。此名稱會自動新增為 DNS 快取中的靜態 DNS 項目。 |
| **hotspot-address** (*IP*; Default: **0.0.0.0**) | HotSpot 服務的 IP 位址。 |
| **html-directory** (*string*; Default: **hotspot**) | 存放 HotSpot HTML 頁面的目錄名稱（預設為 *hotspot* 目錄）。可以指定不同的目錄來存放修改過的 HTML 頁面。若要變更 HotSpot 登入頁面，請從路由器取得 HotSpot 檔案，修改後再上傳回相同位置。html-directory 欄位中必須輸入完整路徑，包括 "/flash/(hotspot\_dir)" |
| **html-directory-override** (*string*; Default: **none**) | Hotspot HTML 檔案的替代路徑。僅當自訂的 hotspot HTML 檔案存放在外部儲存裝置時才應使用。 |
| **http-cookie-lifetime** (*time*; Default: **3d**) | HTTP cookie 有效期間，此選項與 *cookie* HotSpot 登入方法有關 |
| **http-proxy** (*IP:Port*; Default: **0.0.0.0:0**) | HotSpot 服務的 Proxy 伺服器位址與埠，使用預設值時，所有要求都會由本機 `/ip/proxy` 解析 |
| **https-redirect** (*yes \| no*; Default: **yes**) | 當未驗證使用者造訪 https:// URL 時，是否將其重新導向至 hotspot 登入頁面。由於憑證網域名稱會不相符，這通常會導致錯誤，因此可將此參數設為 "no"，所有 https 要求將直接被拒絕，使用者必須造訪 http 頁面。 |
| **login-by** (*cookie\|http-chap\|http-pap\|https\|mac\|trial\|mac-cookie*; Default: **http-chap, cookie**) | 使用的 HotSpot 驗證方法<ul><li><strong>mac-cookie</strong> - 啟用 mac cookie 方法登入</li><li><strong>cookie</strong> - 只能與另一種 HTTP 驗證方法搭配使用。當使用者第一次在 HotSpot 驗證時，會產生 HTTP cookie。在 *cookie-lifetime* 生效期間，不會要求使用者輸入登入／密碼，而是自動完成驗證。</li><li><strong>http-chap</strong> - 使用者在 HotSpot 驗證時需要登入／密碼。使用具 MD5 雜湊演算法的 CHAP challenge-response 方法保護密碼。</li><li><strong>http-pap</strong> - 使用者在 HotSpot 驗證時需要登入／密碼。使用者名稱與密碼會以純文字透過網路傳送。</li><li><strong>https</strong> - 使用者在 HotSpot 驗證時需要登入／密碼。用戶端與伺服器之間的登入／密碼交換會透過 SSL 通道加密。 </li><li><strong>mac</strong> - 用戶端不需填寫登入表單即可完成驗證。用戶端 MAC 位址會新增至 <code>/ip/hotspot/user</code> 資料庫，用戶端連線至 HotSpot 後即完成驗證</li><li><strong>trial</strong> - 允許用戶端在指定時間內使用網際網路，而無需 HotSpot 登入</li></ul> |
| **mac-auth-password** (*string*; Default: ) *[sensitive](/docs/getting-started/configuration-management/list-of-menus-with-sensitive-parameters)* | 與 MAC 驗證搭配使用，此欄位用於指定要依 MAC 位址驗證的使用者密碼。當特定 RADIUS 伺服器拒絕空白密碼用戶端的驗證時，需要此選項 |
| **name** (*string*; Default: ) | 設定檔的描述性名稱 |
| **nas-port-type** (*string*; Default: **wireless-802.11**) | 要傳送至 RADIUS 伺服器的 NAS-Port-Type 值，NAS-Port-Type 值說明於 RADIUS RFC 2865。此選用值屬性表示 HotSpot 伺服器的實體埠類型。 |
| **radius-accounting** (*yes \| no*; Default: **yes**) | 使用 yes 時，傳送每位使用者的 RADIUS 伺服器計費資訊 |
| **radius-default-domain** (*string*; Default: ) | RADIUS 要求要使用的預設網域。允許每個 *`/ip/hotspot/profile`* 使用不同的 RADIUS 伺服器。使用時，應在 /radius domain 值下指定相同的網域名稱。 |
| **radius-interim-update** (*time \| received*; Default: **received**) | 傳送計費更新的頻率。設定為 *received* 時，會使用 RADIUS 伺服器的 interim-time。**0s** 與 *received* 相同。 |
| **radius-location-name** (*string*; Default: ) | 要傳送至 RADIUS 伺服器的 RADIUS-Location-Id。用於在與 RADIUS 伺服器通訊時識別 HotSpot 伺服器的位置。值為選用，並與 RADIUS 伺服器搭配使用。 |
| **radius-mac-format** (*"XX XX XX XX XX XX"\|XX:XX:XX:XX:XX:XX\|XXXXXX-XXXXXX\|XXXXXXXXXXXX\|XX-XX-XX-XX-XX-XX\|XXXX:XXXX:XXXX\|XXXXXX:XXXXXX*; Default: **XX:XX:XX:XX:XX:XX**) | 設定 AAA 工作階段期間傳送至 RADIUS 伺服器的使用者 MAC 位址格式選項。 |
| **rate-limit** (*string*; Default: **""**) | 以 **rx-rate[/tx-rate] [rx-burst-rate[/tx-burst-rate] [rx-burst-threshold[/tx-burst-threshold] [rx-burst-time[/tx-burst-time]]]] [priority] [rx-rate-min[/tx-rate-min]]** 形式表示速率限制，以路由器角度來看（因此 "rx" 是用戶端上傳，"tx" 是用戶端下載）。所有速率應為數字，並可搭配 'k'（1,000 倍）或 'M'（1,000,000 倍）。若未指定 tx-rate，則 rx-rate 也會作為 tx-rate。tx-burst-rate、tx-burst-threshold 與 tx-burst-time 亦同。若 rx-burst-threshold 與 tx-burst-threshold 都未指定（但指定了 burst-rate），則 rx-rate 與 tx-rate 會作為突發臨界值。若 rx-burst-time 與 tx-burst-time 都未指定，則使用 1s 作為預設值。rx-rate-min 與 tx-rate min 是 limit-at 屬性的值 |
| **smtp-server** (*IP*; Default: **0.0.0.0**) | 用於重新導向 HotSpot 使用者 SMTP 要求的 SMTP 伺服器位址。 |
| **split-user-domain** (*yes \| no*; Default: **no**) | 當 RADIUS 伺服器以 "user@domain" 或 "domain\user" 格式提供使用者名稱時，從網域名稱中分割使用者名稱 |
| **ssl-certificate** (*string \| none*; Default: **none**) | 路由器上僅用於 HTTPS 驗證的 SSL 憑證名稱。 |
| **trial-uptime** (*time/time*; Default: **30m/1d**) | 僅與 *trial* 驗證方法搭配使用。第一個時間值指定由 MAC 位址識別的試用使用者在無需 HotSpot 驗證的情況下，可以使用公用網路多久。第二個時間值指定必須經過多少時間，才允許使用者再次試用。 |
| **trial-user-profile** (*string*; Default: **default**) | 指定試用使用者的 **hotspot user profile**。 |
| **use-radius** (*yes \| no*; Default: **no**) | 使用 RADIUS 驗證 HotSpot 使用者。 |

## HotSpot 使用者設定檔 {#hotspot-user-profiles}

**子選單：** `/ip/hotspot/user/profile`

使用者設定檔選單用於通用 HotSpot 用戶端設定。設定檔類似具有相同設定集合、rate-limit、filter chain 名稱等的使用者群組。

| Property | Description |
| :-- | :-- |
| **add-mac-cookie** (*yes\|no*; Default: **yes**) | 允許為使用者新增 mac cookie。 |
| **address-list** (*string*; Default: ) | 使用者的 IP 位址將會加入的位址清單名稱。適合用於依使用者群組標記流量，以進行 queue tree 組態。 |
| **address-pool** (*string \|none*; Default: **none**) | 使用者取得 IP 的 IP pool 名稱。當使用者電腦上的網路設定組態不正確時，HotSpot 伺服器會進行轉換，並從集區指派正確的 IP 位址，而不是不正確的位址 |
| **advertise** (*yes \| no*; Default: **no**) | 啟用強制廣告快顯。經過特定間隔後，會對 HotSpot 使用者顯示特定網頁。廣告頁面可能會被瀏覽器的快顯封鎖程式封鎖。 |
| **advertise-interval** (*time[,time[,..]]*; Default: **30m,10m**) | 廣告快顯之間的間隔集合。清單完成後，所有後續廣告都會使用最後一個值，10 分鐘 |
| **advertise-timeout** (*time \| immediately \| never*; Default: **1m**) | 在封鎖 HotSpot 用戶端的網路存取前，廣告顯示的時間。廣告未顯示時，不允許連線至網際網路。 |
| **advertise-url** (*string[,string[,..]]*; Default: ) | 廣告快顯所顯示的 URL 清單。使用最後一個 URL 後，清單會從頭開始。 |
| **idle-timeout** (*time \| none*; Default: **none**) | 已授權 HotSpot 用戶端的最長閒置期間。當沒有來自該用戶端並通過路由器的流量時，計時器就會開始計時，例如電腦已關閉。達到逾時時，使用者會被登出、從 host 清單中移除，並釋出使用者使用的位址。 |
| **incoming-filter** (*string*; Default: ) | 套用至來自此設定檔使用者的傳入封包的防火牆 chain 名稱。需要從內建 chain（input、forward、output）到 chain=hotspot 的 jump 規則 |
| **incoming-packet-mark** (*string*; Default: ) | 加在來自此設定檔每位使用者的傳入封包上的封包標記 |
| **keepalive-timeout** (*time \| none*; Default: ) | 已授權 HotSpot 用戶端的 keepalive 逾時。用於偵測用戶端電腦是否仍在線且可連線。達到逾時值時，使用者會被登出 |
| **mac-cookie-timeout** (*time*; Default: **3d**) | 從上次登入或登出開始計算 mac-cookie 逾時。 |
| **name** (*string*; Default: ) | 設定檔的描述性名稱 |
| **on-login** (*string*; Default: **""**) | 當使用者從特定設定檔登入 HotSpot 時要執行的 Script 名稱。可以從內部 <strong>user</strong> 與 <strong>interface</strong> 變數取得使用者名稱。例如，<em>:log info "User $user logged in!"</em>。如果 hotspot 設在 bridge 介面上，則 <strong>interface</strong> 變數會顯示 bridge 作為實際介面，除非在 bridge 設定中設定了 <strong>use-ip-firewall</strong>。可用變數清單：<br/><ul><li>$user</li><li>$username ($user 的替代變數名稱)</li><li>$address</li><li>$"mac-address"</li><li>$interface</li></ul> |
| **on-logout** (*string*; Default: **""**) | 當使用者從 HotSpot 登出時要執行的 Script 名稱。可以從內部 <strong>user</strong> 與 <strong>interface</strong> 變數取得使用者名稱。例如，<em>:log info "User $user logged in!"</em> 。如果 hotspot 設在 bridge 介面上，則 <strong>interface</strong> 變數會顯示 bridge 作為實際介面，除非在 bridge 設定中設定了 <strong>use-ip-firewall</strong>。可用變數清單：<br/><ul><li>$user</li><li>$username ($user 的替代變數名稱)</li><li>$address</li><li>$"mac-address"</li><li>$interface</li><li>$cause</li></ul> 從 v6.34rc11 開始，提供一些額外變數：<br/><ul><li>$uptime-secs - 最終工作階段時間，單位為秒</li><li>$bytes-in - 上傳位元組數</li><li>$bytes-out - 下載位元組數</li><li>$bytes-total - 上傳位元組數 + 下載位元組數</li><li>$packets-in - 上傳封包數</li><li>$packets-out - 下載封包數</li><li>$packets-total - 上傳封包數 + 下載封包數</li></ul> |
| **open-status-page** (*always \| http-login*; Default: **always**) | 針對以 mac 登入方法驗證的使用者顯示狀態頁面的選項。例如，在狀態頁面上顯示廣告（alogin.html）<ul><li><strong>http-login</strong> - 僅針對 HTTP 登入開啟狀態頁面（包括 cookie 與 HTTPS）</li><li><strong>always</strong> - 即使是 mac 登入，也開啟 HTTP 狀態頁面</li></ul> |
| **outgoing-filter** (*string*; Default: ) | 套用至來自此設定檔使用者的傳出封包的防火牆 chain 名稱。需要從內建 chain（input、forward、output）到 chain=hotspot 的 jump 規則 |
| **outgoing-packet-mark** (*string*; Default: ) | 加在來自此設定檔每位使用者的傳出封包上的封包標記 |
| **rate-limit** (*string*; Default: **""**) | 使用者登入 HotSpot 後，會為其建立簡單的動態佇列。速率限制以下列形式設定 **[rx-rate[/tx-rate] [rx-burst-rate[/tx-burst-rate] [rx-burst-threshold[/tx-burst-threshold] [rx-burst-time[/tx-burst-time] [priority] [rx-rate-min[/tx-rate-min]]]]**。例如，若要為用戶端設定 1M 下載、512k 上傳，請使用 rate-limit=512k/1M |
| **session-timeout** (*time*; Default: **0s**) | 用戶端允許的工作階段時間。超過此時間後，使用者會被無條件登出 |
| **shared-users** (*integer*; Default: **1**) | 使用相同 HotSpot 使用者名稱同時登入的允許使用者人數 |
| **status-autorefresh** (*time \| none*; Default: **none**) | HotSpot 狀態頁面自動重新整理間隔 |
| **transparent-proxy** (*yes \|*; Default: **yes**) | 對此設定檔的已授權使用者使用透明 HTTP Proxy |

## HotSpot 使用者 {#hotspot-users}

這是實際新增用戶端使用者／密碼資訊的選單。HotSpot 使用者的其他設定選項也可在此設定。

| Property | Description |
| :-- | :-- |
| **address** (*IP*; Default: **0.0.0.0**) | IP 位址，指定後，用戶端將從 HotSpot 一對一 NAT 轉換取得該位址。此位址不會限制 HotSpot 僅能從該位址登入 |
| **comment** (*string*; Default: ) | HotSpot 使用者的描述資訊。可供指令稿用來變更特定用戶端的參數 |
| **email** (*string*; Default: ) | HotSpot 用戶端的電子郵件，為 HotSpot 使用者的資訊性數值 |
| **limit-bytes-in** (*integer*; Default: **0**) | 可從使用者接收的最大位元組數。達到限制後，使用者將從 HotSpot 中斷連線。 |
| **limit-bytes-out** (*integer*; Default: **0**) | 可傳送給使用者的最大位元組數。達到限制後，使用者將從 HotSpot 中斷連線。 |
| **limit-bytes-total** (*integer*; Default: **0**) | （limit-bytes-in+limit-bytes-out）。達到限制後，使用者將從 HotSpot 中斷連線。 |
| **limit-uptime** (*time*; Default: **0**) | HotSpot 用戶端的上線時間限制。一旦達到上線時間，使用者就會從 HotSpot 中斷連線。 |
| **mac-address** (*MAC*; Default: **00:00:00:00:00:00**) | 用戶端僅允許從指定的 MAC 位址登入。若值為 *00:00:00:00:00:00*，則允許任何 MAC 位址。 |
| **name** (*string*; Default: ) | HotSpot 登入頁面使用者名稱。使用 MAC 位址驗證時，名稱會設定為用戶端的 MAC 位址 |
| **password** (*string*; Default: ) *[sensitive](/docs/getting-started/configuration-management/list-of-menus-with-sensitive-parameters)* | 使用者密碼 |
| **profile** (*string*; Default: **default**) | 在 *`/ip/hotspot/user/profile`* 中設定的使用者設定檔 |
| **routes** (*string*; Default: ) | 用戶端連線時新增至 HotSpot 閘道器的路由。路由格式為 **dst-address gateway metric**（例如，*192.168.1.0/24 192.168.0.1 1*） |
| **server** (*string \| all*; Default: **all**) | 允許使用者登入的 HotSpot 伺服器名稱 |
| **otp-secret** (*string*; Default: ) *[sensitive](/docs/getting-started/configuration-management/list-of-menus-with-sensitive-parameters)* | 用於 HotSpot 使用者授權的一次性密碼權杖。可作為 HotSpot 使用者驗證的獨立「密碼」。 |

## 唯讀屬性 {#read-only-properties}

| Property | Description |
| :-- | :-- |
| **bytes-in** (*integer*) | 從用戶端接收的資料位元組總數。 |
| **bytes-out** (*integer*) | 傳送給用戶端的資料位元組總數。 |
| **packets-in** (*integer*) | 從用戶端接收的封包總數。 |
| **packets-out** (*integer*) | 傳送給用戶端的封包總數。 |
| **uptime** (*time*) | 自用戶端通過驗證以來的目前工作階段持續時間。 |

## 作用中的 HotSpot {#hotspot-active}

**子選單：** `/ip/hotspot/active`

HotSpot active 選單會顯示所有已在 HotSpot 通過驗證的用戶端，此選單僅供參考（唯讀）。除了可使用 remove 指令將使用者登出之外，無法在此變更任何內容。

| Parameters | Description |
| :-- | :-- |
| **server** (read-only; name) | 使用者登入的 HotSpot 伺服器名稱 |
| **user** (read-only; name) | HotSpot 使用者名稱 |
| **domain** (read-only; text) | 使用者的網域（若與使用者名稱分開），此參數僅用於 RADIUS 驗證 |
| **address** (read-only; IP address) | HotSpot 使用者的 IP 位址 |
| **mac-address** (read-only; MAC-address) | HotSpot 使用者的 MAC 位址 |
| **login-by** (read-only; multiple-choice: cookie **/** http-chap **/** http-pap **/** https **/** mac **/** mac-cookie **/** trial) | HotSpot 用戶端使用的驗證方法 |
| **uptime** (read-only; time) | 使用者目前的工作階段時間，顯示使用者已登入多久 |
| **idle-time** (read-only; time) | 使用者閒置的時間量 |
| **session-time-left** (read-only; time) | 套用於使用者的 session-time 精確值。此值顯示使用者可上線多久，直到達到 **uptime** 而自動登出 |
| **idle-timeout** (read-only; time) | 使用者 idle-timeout 的精確值 |
| **keepalive-timeout** (read-only; time) | 套用於使用者的 keepalive-timeout 精確值。此值顯示主機可保持無法連線多久，之後便會從 HotSpot 中移除 |
| **limit-bytes-in** (read-only; integer) | 顯示從用戶端接收的位元組數，當 HotSpot 使用者設定了對應參數時，此選項才會生效 |
| **limit-bytes-out** (read-only; integer) | 顯示傳送給用戶端的位元組數，當 HotSpot 使用者設定了對應參數時，此選項才會生效 |
| **limit-bytes-total** (read-only; integer) | 顯示從用戶端傳送／接收的位元組總數，當 HotSpot 使用者設定了對應參數時，此選項才會生效 |

## HotSpot 主機 {#hotspot-host}

**子選單：** `/ip/hotspot/host`

host 表列出所有連線至 HotSpot 伺服器的電腦。host 表僅供參考，無法變更其中的任何值：

| 參數 | 說明 |
| :-- | :-- |
| **mac-address** (read-only; MAC-address) | HotSpot 使用者的 MAC 位址 |
| **address** (read-only; IP address) | HotSpot 用戶端原始的 IP 位址 |
| **to-address** (read-only; IP address) | HotSpot 指派的新用戶端位址，可能與原始的 **address** 相同 |
| **server** (read-only; name) | 用戶端連線的 HotSpot 伺服器名稱 |
| **bridge-port** (read-only; name) | 用戶端連線的 *`/interface/bridge/port`*，當 HotSpot 未設定於 bridge 上時，值為未知 |
| **uptime** (read-only; time) | 顯示使用者上線（連線至 HotSpot）的時間 |
| **idle-time** (read-only; time) | 使用者閒置的時間 |
| **idle-timeout** (read-only; time) | 用戶端的 idle-timeout 值（未授權用戶端） |
| **keepalive-timeout** (read-only; time) | 未授權用戶端的 keepalive-timeout 值 |
| **bytes-in** (read-only; integer) | 自未授權用戶端接收的位元組數 |
| **packet-in** (read-only; integer) | 自未授權用戶端接收的封包數 |
| **bytes-out** (read-only; integer) | 傳送至未授權用戶端的位元組數 |
| **packet-out** (read-only; integer) | 傳送至未授權用戶端的封包數 |

## HotSpot 圍牆花園 {#hotspot-walled-garden}

Walled garden 是一種系統，可允許未經授權使用某些資源，但存取其他資源時需要授權。舉例來說，這可用於提供 HotSpot 服務供應商或計費選項的一般資訊。

此選單僅管理 HTTP 與 HTTPs 通訊協定的 Walled Garden。其他通訊協定也可以加入 Walled Garden，但那是在其他位置設定（於 `/ip/hotspot/walled-garden/ip`）。

| 屬性 | 說明 |
| :-- | :-- |
| **action** (*allow \| deny*; Default: **allow**) | 當封包符合規則時執行的動作<ul><li><strong>allow</strong> - 允許在未授權的情況下存取網頁</li><li><strong>deny</strong> - 存取網頁需要授權</li></ul> |
| **server** (*string*; Default: ) | 套用規則的 HotSpot 伺服器名稱。 |
| **src-address** (*IP*; Default: ) | 使用者的來源位址，通常是 HotSpot 用戶端的 IP 位址 |
| **method** (*string*; Default: ) | 要求的 HTTP 方法 |
| **dst-host** (*string*; Default: ) | 目的地網頁伺服器的網域名稱 |
| **dst-port** (*integer*; Default: ) | 用戶端傳送要求的 TCP 埠號 |
| **path** (*string*; Default: ) | 要求的路徑。路徑位於 '''http://dst\_host' 之後 |

# 唯讀屬性 {#read-only-properties-1}

| 屬性 | 說明 |
| :-- | :-- |
| **dst-address** (*IP*) |  |
| **hits** (*integer*) |  |

萬用字元屬性（dst-host 與 path）會比對完整字串（亦即，若設定為「example」，將不會比對「[example.com](http://example.com)」）。可用的萬用字元為 '\*'（比對任意數量的任意字元）與 '?'（比對任意一個字元）。此處也接受規則運算式，但若某個屬性應視為規則運算式，則應以冒號（':'）開頭。為了表示給定模式之前不允許有任何符號，我們會在模式開頭使用 ^ 符號。為了指定給定模式之後不允許有任何符號，我們會在模式結尾使用 $ 符號。

### 範例 {#example-1}

若只要允許 walled garden 中略過驗證的存取到「[www.example.com/test](http://www.example.com/test)」，但不允許到「[www.example.com/test/test.php](http://www.example.com/test/test.php)」：

```
/ip/hotspot/walled-garden
add dst-host=:^www.example.com path=":/test\$"
```

## HotSpot 圍牆花園 ip {#hotspot-walled-garden-ip}

用於略過其他協定與不同 src/dst 位址（或 address-lists）的 HotSpot 驗證。用於不同服務（Winbox、SSH、Telnet、SIP 等）。

| 屬性 | 說明 |
| :-- | :-- |
| **action** (*accept \|drop\|reject*; Default: **allow**) | 當封包符合規則時要執行的動作<ul><li><strong>allow</strong> - 允許在未授權的情況下存取已開啟的服務</li><li><strong>drop</strong> - 存取服務需要授權</li><li><strong>reject</strong> - 存取服務需要授權，當存取服務時，會產生 ICMP reject 訊息 host-unreachable</li></ul> |
| **server** (*string*; Default: ) | 套用規則的 HotSpot 伺服器名稱。 |
| **src-address** (*IP*; Default: ) | 使用者的來源位址，通常為 HotSpot 用戶端的 IP 位址 |
| **dst-address** (*IP*; Default: ) | 目的地 IP 位址，也就是 WEB-server 的 IP 位址。若已指定 **dst-host**，則忽略此項目。 |
| **src-address-list** (*string*; Default: ) | 來源位址清單名稱 |
| **dst-address-list** (*string*; Default: ) | 目的地位址清單。若已指定 **dst-host**，則忽略此項目。 |
| **dst-host** (*string*; Default: ) | 目的地 web-server 的網域名稱。指定此參數時，會將一個動態項目新增至 Walled Garden |
| **dst-port** (*integer*; Default: ) | 用戶端傳送要求的 TCP 埠號 |
| **protocol** (*integer \| string*; Default: ) | IP 協定 |

## IP 繫結 {#ip-binding}

**子選單：** `/ip/hotspot/ip-binding`

IP-Binding HotSpot 選單可設定靜態一對一 NAT 轉譯，允許特定 HotSpot 用戶端不需任何驗證即可略過，也可封鎖特定主機與子網路連入 HotSpot 網路。

| 屬性 | 說明 |
| :-- | :-- |
| **address** (*IP Range*；預設： **""**) | 用戶端的原始 IP 位址 |
| **mac-address** (*MAC*；預設： **""**) | 用戶端的 MAC 位址 |
| **server** (*string \| all*；預設： **"all"**) | HotSpot 伺服器名稱。<ul><li><strong>all</strong> - 將套用至所有 hotspot 伺服器</li></ul> |
| **to-address** (*IP*；預設： **""**) | 用戶端的新 IP 位址，轉譯會在路由器上進行（用戶端不會知道任何關於轉譯的資訊） |
| **type** (*blocked \| bypassed \| regular*；預設： **""**) | IP-binding 動作的類型<ul><li><strong>regular</strong> - 依規則執行一對一 NAT，將 <strong>address</strong> 轉譯為 <strong>to-address</strong></li><li><strong>bypassed</strong> - 執行轉譯，但排除用戶端登入 HotSpot</li><li><strong>blocked</strong> - 不執行轉譯，並丟棄來自主機的封包</li></ul> |

## Cookie {#cookies}

此選單包含所有傳送給 HotSpot 用戶端的 Cookie，這些用戶端是透過 Cookie 方法完成授權。所有項目都是唯讀的。

**子選單：** `/ip/hotspot/cookie`

| 屬性 | 說明 |
| :-- | :-- |
| **domain** (*string*) | 網域名稱（若從使用者名稱拆分而來） |
| **expires-in** (*time*) | Cookie 的有效期限 |
| **mac-address** (*MAC*) | 用戶端的 MAC 位址 |
| **user** (*string*) | HotSpot 使用者名稱 |

## MAC Cookie

MAC cookie 是 hotspot 功能，旨在提升智慧型手機、筆電與其他行動設備的可用性。

當 MAC cookie 功能啟用時（在使用者設定檔中設定 **login-by**=mac-cookie、**add-mac-cookie**=yes），會執行下列動作：

- **首次成功登入**。如果只有一部主機使用該 MAC 位址，Mac cookie 會記錄該 MAC 位址的使用者名稱與密碼。Cookie 逾時值會設定為等於 mac-cookie-timeout 的值。
- **出現新主機**。Hotspot 會檢查該 MAC 位址是否有 mac cookie 記錄，並使用記錄的使用者名稱與密碼登入該主機。如果有多部主機使用相同的 MAC 位址，使用者將不會登入，且該位址的 MAC cookie 記錄會被刪除。

當**使用者登出**時，在下列情況下會移除 mac cookie：

- user-request - 使用者按一下登出按鈕。
- admin-reset - 與 radius 伺服器中斷連線，或使用者從 hotspot active 選單中移除。
- nas-request - 已達到流量限制。
- session-timeout。

若要偵錯 mac-cookie 問題，需要啟用 hotspot 偵錯日誌，並查看特定主機的 mac-cookie 登入失敗原因。

### 伺服器移除 mac cookie 的原因 {#reasons-when-mac-cookie-is-removed-by-server}

- `/ip/hotspot/cookie/remove [number]`。
- Radius 伺服器傳送 Disconnect-Request。
- 使用者已透過 hotspot 狀態頁面自行登出。
- 使用者已達到其資料用量上限（「traffic limit reached」）。
- Session-Timeout。
- 若 mac-cookie 登入失敗。
- 若伺服器偵測到 host table 中有超過一個具有相同 mac-address 的項目。

### HotSpot API JSON 的屬性（RFC 7710） {#properties-of-the-hotspot-api-json-rfc-7710}

根據文件中提供的 `api.json` 範本，以下是用於向用戶端設備傳達 captive portal 狀態的每個屬性說明：

- **captive**：布林值（`true` 或 `false`），用於告知用戶端設備目前是否受到 captive portal 限制。如果使用者已完成驗證，則會傳回 `false`。
- **user-portal-url**：使用者可存取登入頁面或管理目前工作階段的特定 URL。在 MikroTik RouterOS 中，此值會由 `$(link-login-only)` 變數動態填入。
- **seconds-remaining**：（選用）整數，表示目前工作階段到期前剩餘的秒數。只有在設定工作階段逾時時才會包含此項目。
- **bytes-remaining**：（選用）整數，表示使用者可用的剩餘資料配額，單位為位元組。只有在對 HotSpot 使用者套用資料限制時才會包含此項目。
- **can-extend-session**：布林值，指出使用者是否能夠延長目前工作階段，或透過入口網站購買／要求更多時間／資料。

## 在 Hotspot 伺服器上使用 mangle 進行負載平衡 {#load-balancing-with-mangle-on-hotspot-server}

在多上行鏈路的 Hotspot 設定中（例如 [PCC](/docs/high-availability-solutions/load-balancing/per-connection-classifier)），預設路由通常可能無法如預期般運作，因為路由器會優先處理 mangle 規則，而非本機目的地檢查。

若要修正此問題，請確保目的地為 Hotspot 伺服器的流量在評估 **mangle** 鏈之前，先透過 **local** 表路由。你可以透過下列方式達成：

1. 調整「`/routing/settings`」（[路由表查詢](/docs/user-guides/routing-and-networking-protocols/routing-decision#routing-table-lookup)）。
2. 或者，新增特定「`/routing/rule`」項目，強制 Hotspot 伺服器的流量先使用 local 表（包括用於偵測 Hotspot 伺服器的 HTTP 80 流量）。
