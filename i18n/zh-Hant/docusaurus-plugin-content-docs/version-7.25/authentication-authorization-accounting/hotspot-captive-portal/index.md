---
sidebar_key: "authentication-authorization-accounting/hotspot-captive-portal/index"
sidebar_position: 2
title: "HotSpot - 強制門戶"
sidebar_label: "HotSpot - 強制門戶"
description: "MikroTik HotSpot 閘道器可為公共網路啟用用戶端認證，具備 DHCP 地址池、多種認證方式和 walled-garden 訪問等功能。它需要 IPv4，並具有特定的路由限制，文件中提供了用於設定的配置示例。"
tags:
  - 'hotspot'
  - 'firewall'
  - 'dhcp'
source: https://manual.mikrotik.com/docs/7.25/authentication-authorization-accounting/hotspot-captive-portal
captured_at: '2026-11-04T11:14:23+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

MikroTik HotSpot 閘道器在用戶端訪問公共網路之前為其提供身份驗證。

:::warning
HotSpot（強制門戶）使用 web-proxy，目前只能使用預設路由表，這使得 PCC(per connection-classifier) 因使用多個路由表而成為一種無效方法。
:::

:::warning
HotSpot 功能可能會被 device-mode 阻止。在配置 HotSpot 之前，請確保已在 `/system/device-mode` 中啟用該功能 ([更多資訊](../../system-information-and-utilities/device-mode.md).
:::

### HotSpot 屬性 {#hotspot-properties}

| 屬性 | 描述 |
| :--- | :--- |
| **name** | HotSpot 伺服器例項的描述性名稱。 |
| **interface** | HotSpot 服務將監聽用戶端請求的特定本地介面（物理或虛擬）。 |
| **address-pool** | HotSpot 用戶端將透過 DHCP 從中獲取 IP 地址的 IP 地址池。 |
| **profile** | 對 HotSpot 伺服器配置檔案的引用，其中包含登入方法和 HTML 目錄等常用設定。 |
| **idle-timeout** | 在未檢測到流量時，用戶端經過該無活動時段後會自動登出。 |
| **keepalive-timeout** | 用於檢查用戶端是否仍可訪問的時間間隔；如果用戶端無響應，則會終止會話。 |
| **login-timeout** | 登入頁面顯示後，允許用戶端完成身份驗證過程的最長持續時間。 |
| **addresses-per-mac** | 限制可與單個 MAC 地址關聯的 IP 地址數量。 |
| **proxy-status** | 指示 HotSpot 系統所使用的內部 web-proxy 的當前執行狀態。 |

### HotSpot 閘道器功能 {#hotspot-gateway-features}

- 使用路由器上的本地用戶端資料庫或遠端 RADIUS 伺服器對用戶端進行不同的身份驗證方法。
- 在路由器上的本地資料庫或遠端 RADIUS 伺服器中進行使用者計費。
- 圍牆花園系統，無需授權即可訪問某些網頁。
- 登入頁面修改，可在其中放置公司資訊。
- 自動且透明地將用戶端的任意 IP 地址更改為有效地址。
- HotSpot 可以通知 DHCP 用戶端它們位於強制門戶之後（RFC7710）。

HotSpot 僅在 IPv4 下才能可靠工作。HotSpot 依賴防火牆 NAT 規則，而目前 IPv6 不支援這些規則。

## 示例 {#example}

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

## 驗證 HotSpot 配置 {#verify-hotspot-configuration}

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

### **設定過程中詢問的引數** {#parameters-asked-during-the-setup-process}

| 引數 | 描述 |
| :-- | :-- |
| **hotspot interface** (*string*；預設值：**allow**) | 執行 HotSpot 的介面名稱。要在橋接介面上執行 HotSpot，請確保公共介面未包含在橋接埠中。 |
| **local address of network** (*IP*；預設值：**10.5.50.1/24**) | HotSpot 閘道器地址 |
| **masquerade network** (*yes \| no*；預設值：**yes**) | 是否對 HotSpot 網路進行偽裝；當為 **yes** 時，會向 *`/ip/firewall/nat`* 新增一條帶有 *action=masquerade* 的規則 |
| **address pool of network** (*string*；預設值：**yes**) | HotSpot 網路的地址池，用於將使用者 IP 地址更改為有效地址。在為不願更改其網路設定的移動用戶端提供網路訪問時很有用。 |
| **select certificate** (*none \| import-other-certificate*；預設值： ) | 當需要 HTTPS 授權方法時，選擇 SSL 證書。 |
| **ip address of smtp server** (*IP*；預設值：**0.0.0.0**) | SMTP 伺服器的 IP 地址，用於重定向 HotSpot 網路的 SMTP 請求（TCP 埠 25） |
| **dns servers** (*IP*；預設值：**0.0.0.0**) | 用於 HotSpot 用戶端的 DNS 伺服器地址，配置取自 HotSpot 閘道器的 *`/ip/dns`* 選單 |
| **dns name** (*string*；預設值：**""**) | HotSpot 伺服器的域名，需要完全限定域名，例如 [www.example.com](http://www.example.com) |
| **name of local hotspot user** (*string*；預設值：**"admin"**) | 自動建立的一個 HotSpot 使用者的使用者名稱，該使用者會被新增到 *`/ip/hotspot/user`* |
| **password for the user** (*string*；預設值： ) | 自動建立的 HotSpot 使用者的密碼 |

## HotSpot {#hotspot}

**子選單：** `/ip/hotspot`

該選單用於管理路由器的 HotSpot 伺服器。可以在乙太網、無線、VLAN 和橋接介面上執行 HotSpot。每個介面只允許一個 HotSpot 伺服器。在橋接介面上配置 HotSpot 時，請將 HotSpot 介面設定為橋接介面，而不是橋接埠；不要將公共介面新增到橋接埠。你可以手動將 HotSpot 伺服器新增到 *`/ip/hotspot`* 選單，但建議執行 *`/ip/hotspot/setup`*，它會新增所有必要設定。

| 引數 | 描述 |
| :-- | :-- |
| **name** (text) | HotSpot 伺服器的名稱或識別符號 |
| **address-pool** (name/none；預設值：*none*) | 用於將任意 HotSpot 用戶端 IP 地址更改為有效地址的地址空間。在為不願更改其網路設定的移動用戶端提供公共網路訪問時很有用 |
| **idle-timeout** (time/none；預設值：*5m*) | 未授權用戶端的無活動時段。當該用戶端沒有流量時（實際上，用戶端計算機應已關機），一旦達到超時時間，使用者就會從 HotSpot 主機列表中移除，其使用的地址變為可用 |
| **keepalive-timeout** (time/none；預設值：*none*) | 表示主機在從 HotSpot 中移除之前可以保持不可達多長時間的值 |
| **login-timeout** (time/none；預設值：*none*) | 如果主機在該時間段後仍未透過系統授權，則主機的條目會從主機表中刪除。迴圈會重複，直到主機登入系統。如果存在主機在未授權狀態下在主機表中停留太久後無法登入的情況，請啟用此選項。 |
| **interface** (介面名稱) | 執行 HotSpot 的介面 |
| **addresses-per-mac** (integer**/**unlimited；預設值：2) | 當多個 HotSpot 用戶端使用一個 MAC 地址連線時，允許與該 MAC 地址繫結的 IP 地址數量 |
| **profile** (name；預設值：***default*) | HotSpot 伺服器的預設 HotSpot 配置檔案，位於 *`/ip/hotspot/profile`* |

## 只讀 {#read-only}

| 引數 | 描述 |
| :-- | :-- |
| keepalive-timeout (只讀；time) | 應用於使用者的 keepalive-timeout 的確切值。該值表示主機可以保持不可達多久後從 HotSpot 中移除 |

## HotSpot 配置檔案 {#hotspot-profile}

此子選單包含 HotSpot 伺服器配置檔案列表。同一臺網關機器上可以有各種不同的 HotSpot 系統，定義為伺服器配置檔案。一個或多個介面可以分組到一個伺服器配置檔案中。特定介面上的伺服器設定很少——大部分配置都在伺服器配置檔案中設定。例如，可以為每個伺服器配置檔案製作完全不同的一組 servlet 頁面，並定義不同的 RADIUS 伺服器用於身份驗證。

| 屬性 | 描述 |
| :-- | :-- |
| **dns-name** (*string*; 預設值: **""**) | HotSpot 伺服器的 DNS 名稱。該 DNS 名稱用作 HotSpot 伺服器的名稱（即，它顯示為登入頁面的位置）。此名稱將自動作為靜態 DNS 條目新增到 DNS 快取中。 |
| **hotspot-address** (*IP*; 預設值: **0.0.0.0**) | HotSpot 服務的 IP 地址。 |
| **html-directory** (*string*; 預設值: **hotspot**) | 儲存 HotSpot HTML 頁面的目錄名稱（預設為 *hotspot* 目錄）。可以指定包含修改後 HTML 頁面的其他目錄。要更改 HotSpot 登入頁面，請從路由器獲取 HotSpot 檔案，修改後再上傳回同一位置。必須在 html-directory 欄位中輸入完整路徑，包括 "/flash/(hotspot\_dir)" |
| **html-directory-override** (*string*; 預設值: **none**) | HotSpot HTML 檔案的替代路徑。僅當自定義的 HotSpot HTML 檔案儲存在外部儲存裝置上時才應使用。 |
| **http-cookie-lifetime** (*time*; 預設值: **3d**) | HTTP cookie 的有效時間，此選項與 *cookie* HotSpot 登入方式相關 |
| **http-proxy** (*IP:Port*; 預設值: **0.0.0.0:0**) | HotSpot 服務的代理伺服器地址和埠，當使用預設值時，所有請求都由本地 `/ip/proxy` 解析 |
| **https-redirect** (*yes \| no*; 預設值: **yes**) | 當用戶訪問 https:// url 時，是否將未認證使用者重定向到 HotSpot 登入頁面。由於證書域名不匹配，這通常會導致錯誤，因此可以將此引數設定為 "no"，此時所有 https 請求將被直接拒絕，使用者必須訪問 http 頁面。 |
| **login-by** (*cookie\|http-chap\|http-pap\|https\|mac\|trial\|mac-cookie*; 預設值: **http-chap, cookie**) | 所使用的 HotSpot 認證方法<ul><li><strong>mac-cookie</strong> - 啟用 mac cookie 登入方式</li><li><strong>cookie</strong> - 只能與另一種 HTTP 認證方法一起使用。當用戶在 HotSpot 中首次認證時會生成 HTTP cookie。在 <em>cookie-lifetime</em> 有效期內，使用者不會被要求輸入登入名/密碼，而是自動完成認證</li><li><strong>http-chap</strong> - 使用者在 HotSpot 中認證需要登入名/密碼。使用帶 MD5 雜湊演算法的 CHAP 質詢-響應方法來保護密碼。</li><li><strong>http-pap</strong> - 使用者在 HotSpot 中認證需要登入名/密碼。使用者名稱和密碼以明文形式透過網路傳送。</li><li><strong>https</strong> - 使用者在 HotSpot 中認證需要登入名/密碼。用戶端與伺服器之間的登入名/密碼交換透過 SSL 隧道加密。</li><li><strong>mac</strong> - 用戶端無需登入表單即可認證。用戶端 MAC 地址被新增到 <code>/ip/hotspot/user</code> 資料庫中，用戶端一旦連線到 HotSpot 即完成認證</li><li><strong>trial</strong> - 允許用戶端在指定時間內無需 HotSpot 登入即可使用網際網路</li></ul> |
| **mac-auth-password** (*string*; 預設值: ) *[sensitive](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 與 MAC 認證一起使用，該欄位用於指定按 MAC 地址認證的使用者所需的密碼。當特定 RADIUS 伺服器拒絕密碼為空的用戶端認證時，需要此選項 |
| **name** (*string*; 預設值: ) | 配置檔案的描述性名稱 |
| **nas-port-type** (*string*; 預設值: **wireless-802.11**) | 傳送到 RADIUS 伺服器的 NAS-Port-Type 值，NAS-Port-Type 值在 RADIUS RFC 2865 中描述。此可選值屬性指示 HotSpot 伺服器物理埠的型別。 |
| **radius-accounting** (*yes \| no*; 預設值: **yes**) | 當設定為 yes 時，為每個使用者傳送 RADIUS 伺服器計費資訊 |
| **radius-default-domain** (*string*; 預設值: ) | 用於 RADIUS 請求的預設域。允許為每個 *`/ip/hotspot/profile`* 使用單獨的 RADIUS 伺服器。如果使用，應在 /radius domain 值下指定相同的域名。 |
| **radius-interim-update** (*time \| received*; 預設值: **received**) | 傳送計費更新的頻率。當設定為 *received* 時，使用 RADIUS 伺服器的 interim-time。**0s** 與 *received* 相同。 |
| **radius-location-name** (*string*; 預設值: ) | 要傳送到 RADIUS 伺服器的 RADIUS-Location-Id。用於在與 RADIUS 伺服器通訊期間標識 HotSpot 伺服器的位置。該值是可選的，並與 RADIUS 伺服器一起使用。 |
| **radius-mac-format** (*"XX XX XX XX XX XX"\|XX:XX:XX:XX:XX:XX\|XXXXXX-XXXXXX\|XXXXXXXXXXXX\|XX-XX-XX-XX-XX-XX\|XXXX:XXXX:XXXX\|XXXXXX:XXXXXX*; 預設值: **XX:XX:XX:XX:XX:XX**) | 用於設定使用者 mac 地址格式的選項，該地址在 AAA 會話期間傳送到 RADIUS 伺服器。 |
| **rate-limit** (*string*; 預設值: **""**) | 從路由器角度看的速率限制，形式為 **rx-rate[/tx-rate] [rx-burst-rate[/tx-burst-rate] [rx-burst-threshold[/tx-burst-threshold] [rx-burst-time[/tx-burst-time]]]] [priority] [rx-rate-min[/tx-rate-min]]**（因此 "rx" 是用戶端上傳，"tx" 是用戶端下載）。所有速率應為數字，可帶可選的 'k'（1,000 倍）或 'M'（1,000,000 倍）。如果未指定 tx-rate，則 rx-rate 也作為 tx-rate 使用。tx-burst-rate、tx-burst-threshold 和 tx-burst-time 同理。如果 rx-burst-threshold 和 tx-burst-threshold 均未指定（但指定了 burst-rate），則使用 rx-rate 和 tx-rate 作為突發閾值。如果 rx-burst-time 和 tx-burst-time 均未指定，則預設使用 1s。rx-rate-min 和 tx-rate-min 是 limit-at 屬性的值 |
| **smtp-server** (*IP*; 預設值: **0.0.0.0**) | 用於重定向 HotSpot 使用者 SMTP 請求的 SMTP 伺服器地址。 |
| **split-user-domain** (*yes \| no*; 預設值: **no**) | 當 RADIUS 伺服器以 "user@domain" 或 "domain\user" 格式提供使用者名稱時，將使用者名稱與域名分離 |
| **ssl-certificate** (*string \| none*; 預設值: **none**) | 路由器上僅用於 HTTPS 認證的 SSL 證書名稱。 |
| **trial-uptime** (*time/time*; 預設值: **30m/1d**) | 僅與 *trial* 認證方法一起使用。第一個時間值指定按 MAC 地址識別的試用使用者可以在無需 HotSpot 認證的情況下訪問公共網路的時長。第二個時間值指定必須經過多長時間後用戶才被允許再次使用試用。 |
| **trial-user-profile** (*string*; 預設值: **default**) | 為試用使用者指定 **HotSpot 使用者配置檔案**。 |
| **use-radius** (*yes \| no*; 預設值: **no**) | 使用 RADIUS 認證 HotSpot 使用者。 |

## HotSpot 使用者配置檔案 {#hotspot-user-profiles}

**子選單：** `/ip/hotspot/user/profile`

使用者配置檔案選單用於設定 HotSpot 用戶端的通用設定。配置檔案類似於具有相同設定、rate-limit、過濾鏈名稱等的使用者組。

| 屬性 | 描述 |
| :-- | :-- |
| **add-mac-cookie** (*yes\|no*; 預設值: **yes**) | 允許為使用者新增 mac cookie。 |
| **address-list** (*string*; 預設值: ) | 將新增使用者 IP 地址的地址列表名稱。用於按使用者組標記流量以進行 queue tree 配置。 |
| **address-pool** (*string \|none*; 預設值: **none**) | 使用者從中獲取 IP 的 IP 池名稱。當用戶在計算機上的網路設定配置不正確時，HotSpot 伺服器會進行轉換，並從池中分配正確的 IP 地址而不是錯誤的地址 |
| **advertise** (*yes \| no*; 預設值: **no**) | 啟用強制廣告彈窗。經過一定時間間隔後，會為 HotSpot 使用者顯示特定網頁。廣告頁面可能會被瀏覽器彈窗攔截器阻止。 |
| **advertise-interval** (*time[,time[,..]]*; 預設值: **30m,10m**) | 廣告彈窗之間的時間間隔集合。列表用完後，所有後續廣告都使用最後一個值，即 10 分鐘 |
| **advertise-timeout** (*time \| immediately \| never*; 預設值: **1m**) | 在阻止 HotSpot 用戶端網路訪問之前，廣告顯示的時長。未顯示廣告時不允許連線到網際網路。 |
| **advertise-url** (*string[,string[,..]]*; 預設值: ) | 廣告彈窗顯示的 URL 列表。最後一個 URL 使用完後，列表從頭開始。 |
| **idle-timeout** (*time \| none*; 預設值: **none**) | 已授權 HotSpot 用戶端的最大非活動時長。當沒有來自該用戶端的流量經過路由器時（例如計算機關閉），計時器開始計數。達到超時時間後，使用者被登出、從主機列表中移除，並且使用者使用的地址被釋放。 |
| **incoming-filter** (*string*; 預設值: ) | 應用於此配置檔案使用者傳入封包的防火牆鏈名稱。需要從內建鏈（input、forward、output）跳轉到 chain=hotspot 的規則 |
| **incoming-packet-mark** (*string*; 預設值: ) | 為此配置檔案每個使用者的傳入封包設定的包標記 |
| **keepalive-timeout** (*time \| none*; 預設值: ) | 已授權 HotSpot 用戶端的 keepalive 超時。用於檢測用戶端的計算機是否存活且可達。達到超時值時使用者被登出 |
| **mac-cookie-timeout** (*time*; 預設值: **3d**) | 選擇自上次登入或登出起的 mac-cookie 超時。 |
| **name** (*string*; 預設值: ) | 配置檔案的描述性名稱 |
| **on-login** (*string*; 預設值: **""**) | 當用戶從特定配置檔案登入 HotSpot 時要執行的指令碼名稱。可以從內部 <strong>user</strong> 和 <strong>interface</strong> 變數獲取使用者名稱。例如，<em>:log info "User $user logged in!"</em>。如果 HotSpot 設定在網橋介面上，則除非在網橋設定中設定了 <strong>use-ip-firewall</strong>，否則 <strong>interface</strong> 變數將顯示網橋作為實際介面。可用變數列表：<br/><ul><li>$user</li><li>$username（$user 的替代變數名）</li><li>$address</li><li>$"mac-address"</li><li>$interface</li></ul> |
| **on-logout** (*string*; 預設值: **""**) | 當用戶從 HotSpot 登出時要執行的指令碼名稱。可以從內部 <strong>user</strong> 和 <strong>interface</strong> 變數獲取使用者名稱。例如，<em>:log info "User $user logged in!"</em>。如果 HotSpot 設定在網橋介面上，則除非在網橋設定中設定了 <strong>use-ip-firewall</strong>，否則 <strong>interface</strong> 變數將顯示網橋作為實際介面。可用變數列表：<br/><ul><li>$user</li><li>$username（$user 的替代變數名）</li><li>$address</li><li>$"mac-address"</li><li>$interface</li><li>$cause</li></ul> 從 v6.34rc11 起，還有一些額外變數可用：<br/><ul><li>$uptime-secs - 最終會話時間（秒）</li><li>$bytes-in - 上傳位元組數</li><li>$bytes-out - 下載位元組數</li><li>$bytes-total - 上傳位元組數 + 下載位元組數</li><li>$packets-in - 上傳封包數</li><li>$packets-out - 下載封包數</li><li>$packets-total - 上傳封包數 + 下載封包數</li></ul> |
| **open-status-page** (*always \| http-login*; 預設值: **always**) | 用於為透過 mac 登入方式認證的使用者顯示狀態頁面的選項。例如，在狀態頁面（alogin.html）上顯示廣告<ul><li><strong>http-login</strong> - 僅為 HTTP 登入（包括 cookie 和 HTTPS）開啟狀態頁面</li><li><strong>always</strong> - 在 mac 登入的情況下也開啟 HTTP 狀態頁面</li></ul> |
| **outgoing-filter** (*string*; 預設值: ) | 應用於此配置檔案使用者傳出封包的防火牆鏈名稱。需要從內建鏈（input、forward、output）跳轉到 chain=hotspot 的規則 |
| **outgoing-packet-mark** (*string*; 預設值: ) | 為此配置檔案每個使用者的傳出封包設定的包標記 |
| **rate-limit** (*string*; 預設值: **""**) | 使用者登入 HotSpot 後，會為該使用者建立一個簡單的動態佇列。速率限制按以下形式配置 **[rx-rate[/tx-rate] [rx-burst-rate[/tx-burst-rate] [rx-burst-threshold[/tx-burst-threshold] [rx-burst-time[/tx-burst-time] [priority] [rx-rate-min[/tx-rate-min]]]]**。例如，要為用戶端設定 1M 下載、512k 上傳，則 rate-limit=512k/1M |
| **session-timeout** (*time*; 預設值: **0s**) | 用戶端允許的會話時間。超過此時間後，使用者被無條件登出 |
| **shared-users** (*integer*; 預設值: **1**) | 使用同一 HotSpot 使用者名稱同時登入的允許數量 |
| **status-autorefresh** (*time \| none*; 預設值: **none**) | HotSpot 狀態頁面自動重新整理間隔 |
| **transparent-proxy** (*yes \|*; 預設值: **yes**) | 為此配置檔案的已授權使用者使用透明 HTTP 代理 |

## HotSpot 使用者 {#hotspot-users}

這是實際新增用戶端使用者名稱/密碼資訊的選單。HotSpot 使用者的其他配置選項也在此處配置。

| 屬性 | 描述 |
| :-- | :-- |
| **address** (*IP*；預設值：**0.0.0.0**) | IP 地址；指定後，用戶端將透過 HotSpot 一對一 NAT 轉換獲得該地址。該地址不會將 HotSpot 登入限制為僅能從該地址登入 |
| **comment** (*string*；預設值： ) | HotSpot 使用者的描述性資訊。可用於指令碼為特定用戶端更改引數 |
| **email** (*string*；預設值： ) | HotSpot 用戶端的電子郵件，是 HotSpot 使用者的資訊性值 |
| **limit-bytes-in** (*integer*；預設值：**0**) | 可從使用者接收的最大位元組數。達到限制後，使用者會從 HotSpot 斷開連線。 |
| **limit-bytes-out** (*integer*；預設值：**0**) | 可從使用者傳輸的最大位元組數。達到限制後，使用者會從 HotSpot 斷開連線。 |
| **limit-bytes-total** (*integer*；預設值：**0**) | (limit-bytes-in+limit-bytes-out)。達到限制後，使用者會從 HotSpot 斷開連線。 |
| **limit-uptime** (*time*；預設值：**0**) | HotSpot 用戶端的執行時間限制。一旦達到該執行時間，使用者就會從 HotSpot 斷開連線。 |
| **mac-address** (*MAC*；預設值：**00:00:00:00:00:00**) | 僅允許用戶端從指定的 MAC 地址登入。如果值為 *00:00:00:00:00:00*，則允許任何 mac 地址。 |
| **name** (*string*；預設值： ) | HotSpot 登入頁面使用者名稱。使用 MAC 地址身份驗證時，名稱配置為用戶端的 MAC 地址 |
| **password** (*string*；預設值： ) *[敏感](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 使用者密碼 |
| **profile** (*string*；預設值：**default**) | 在 *`/ip/hotspot/user/profile`* 中配置的使用者配置檔案 |
| **routes** (*string*；預設值： ) | 用戶端連線時新增到 HotSpot 閘道器的路由。路由格式為 **dst-address gateway metric**（例如，*192.168.1.0/24 192.168.0.1 1*） |
| **server** (*string \| all*；預設值：**all**) | 允許使用者登入的 HotSpot 伺服器名稱 |
| **otp-secret** (*string*；預設值： ) *[敏感](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 用於 HotSpot 使用者授權的一次性密碼令牌。它可作為 HotSpot 使用者身份驗證的單獨 "密碼" 使用。 |

## 只讀屬性 {#read-only-properties}

| 屬性 | 描述 |
| :-- | :-- |
| **bytes-in** (*integer*) | 從用戶端接收的資料位元組總數。 |
| **bytes-out** (*integer*) | 傳送給用戶端的資料位元組總數。 |
| **packets-in** (*integer*) | 從用戶端接收的封包總數。 |
| **packets-out** (*integer*) | 傳送給用戶端的封包總數。 |
| **uptime** (*time*) | 自用戶端透過身份驗證以來的當前會話持續時間。 |

## HotSpot 活動 {#hotspot-active}

**子選單：** `/ip/hotspot/active`

HotSpot 活動選單顯示所有在 HotSpot 中透過身份驗證的用戶端；該選單僅供參考（只讀）。此處無法更改任何內容，但可以使用 remove 命令將使用者登出。

| 引數 | 描述 |
| :-- | :-- |
| **server** (只讀；name) | 用戶端登入的 HotSpot 伺服器名稱 |
| **user** (只讀；name) | HotSpot 使用者的名稱 |
| **domain** (只讀；text) | 使用者的域（如果從使用者名稱中分離），該引數僅與 RADIUS 身份驗證一起使用 |
| **address** (只讀；IP address) | HotSpot 使用者的 IP 地址 |
| **mac-address** (只讀；MAC-address) | HotSpot 使用者的 MAC 地址 |
| **login-by** (只讀；多選：cookie **/** http-chap **/** http-pap **/** https **/** mac **/** mac-cookie **/** trial) | HotSpot 用戶端使用的身份驗證方法 |
| **uptime** (只讀；time) | 使用者的當前會話時間，顯示使用者已登入多長時間 |
| **idle-time** (只讀；time) | 使用者已空閒的時間 |
| **session-time-left** (只讀；time) | 應用於使用者的 session-time 的確切值。該值顯示允許使用者線上多長時間，達到 **uptime** 後會自動登出 |
| **idle-timeout** (只讀；time) | 使用者 idle-timeout 的確切值 |
| **keepalive-timeout** (只讀；time) | 應用於使用者的 keepalive-timeout 的確切值。該值表示主機可以保持不可達多久後從 HotSpot 中移除 |
| **limit-bytes-in** (只讀；integer) | 該值顯示從用戶端接收了多少位元組；當為 HotSpot 使用者配置了相應引數時，該選項生效 |
| **limit-bytes-out** (只讀；integer) | 該值顯示向用戶端傳送了多少位元組；當為 HotSpot 使用者配置了相應引數時，該選項生效 |
| **limit-bytes-total** (只讀；integer) | 該值顯示從用戶端傳送/接收的總位元組數；當為 HotSpot 使用者配置了相應引數時，該選項生效 |

## HotSpot 主機 {#hotspot-host}

**子選單：** `/ip/hotspot/host`

主機表列出所有連線到 HotSpot 伺服器的計算機。主機表僅供參考，無法在其中更改任何值：

| 引數 | 描述 |
| :-- | :-- |
| **mac-address** (只讀；MAC-address) | HotSpot 使用者 MAC 地址 |
| **address** (只讀；IP address) | HotSpot 用戶端的原始 IP 地址 |
| **to-address** (只讀；IP address) | HotSpot 分配的新用戶端地址，可能與原始 **address** 相同 |
| **server** (只讀；name) | 用戶端連線到的 HotSpot 伺服器名稱 |
| **bridge-port** (只讀；name) | 用戶端連線到的 *`/interface/bridge/port`*；當 HotSpot 未在橋上配置時，該值未知 |
| **uptime** (只讀；time) | 該值顯示使用者線上（連線到 HotSpot）多長時間 |
| **idle-time** (只讀；time) | 使用者已空閒的時間 |
| **idle-timeout** (只讀；time) | 用戶端 idle-timeout 的值（未授權用戶端） |
| **keepalive-timeout** (只讀；time) | 未授權用戶端的 keepalive-timeout 值 |
| **bytes-in** (只讀；integer) | 從未授權用戶端接收的位元組數 |
| **packet-in** (只讀；integer) | 從未授權用戶端接收的封包數 |
| **bytes-out** (只讀；integer) | 傳送給未授權用戶端的位元組數 |
| **packet-out** (只讀；integer) | 傳送給未授權用戶端的封包數 |

## HotSpot 圍牆花園 {#hotspot-walled-garden}

圍牆花園是一種系統，允許未經授權使用某些資源，但訪問其他資源需要授權。例如，這對於提供有關 HotSpot 服務提供商或計費選項的一些常規資訊很有用。

該選單僅管理 HTTP 和 HTTPs 協定的圍牆花園。其他協定也可以包含在圍牆花園中，但這在其他位置配置（在 `/ip/hotspot/walled-garden/ip` 中）。

| 屬性 | 描述 |
| :-- | :-- |
| **action** (*allow \| deny*；預設值：**allow**) | 當封包匹配規則時要執行的動作allow - 無需授權即可訪問網頁deny - 訪問網頁需要授權 |
| **server** (*string*；預設值： ) | 應用規則的 HotSpot 伺服器名稱。 |
| **src-address** (*IP*；預設值： ) | 使用者的源地址，通常是 HotSpot 用戶端的 IP 地址 |
| **method** (*string*；預設值： ) | 請求的 HTTP 方法 |
| **dst-host** (*string*；預設值： ) | 目標 Web 伺服器的域名 |
| **dst-port** (*integer*；預設值： ) | 用戶端傳送請求到的 TCP 埠號 |
| **path** (*string*；預設值： ) | 請求的路徑。路徑位於 '''http://dst\_host' 之後 |

# 只讀屬性 {#read-only-properties-1}

| 屬性 | 描述 |
| :-- | :-- |
| **dst-address** (*IP*) |  |
| **hits** (*integer*) |  |

萬用字元屬性（dst-host 和 path）匹配完整字串（即，如果它們設定為 "example"，則不會匹配 "[example.com](http://example.com)"）。可用萬用字元為 '\*'（匹配任意數量的任意字元）和 '?'（匹配任意一個字元）。此處也接受正則表示式，但如果應將屬性視為正則表示式，則它應以冒號 (':') 開頭。為了表示給定模式之前不允許有任何符號，我們在模式開頭使用 ^ 符號。為了指定給定模式之後不允許有任何符號，我們在模式末尾使用 $ 符號。

### 示例 {#example-1}

要僅允許在圍牆花園中繞過訪問 "[www.example.com/test](http://www.example.com/test)"，而不允許訪問 "[www.example.com/test/test.php](http://www.example.com/test/test.php)"：

```
/ip/hotspot/walled-garden
add dst-host=:^www.example.com path=":/test\$"
```

## HotSpot 圍牆花園 ip {#hotspot-walled-garden-ip}

用於為其他協定和不同的源/目標地址（或地址列表）繞過 HotSpot 身份驗證。用於不同的服務（Winbox、SSH、Telnet、SIP 等）。

| 屬性 | 描述 |
| :-- | :-- |
| **action** (*accept \|drop\|reject*；預設值：**allow**) | 當封包匹配規則時要執行的動作allow - 無需授權即可訪問開放的服務drop - 訪問該服務需要授權reject - 訪問該服務需要授權；訪問該服務時，將生成 ICMP 拒絕訊息 host-unreachable |
| **server** (*string*；預設值： ) | 應用規則的 HotSpot 伺服器名稱。 |
| **src-address** (*IP*；預設值： ) | 使用者的源地址，通常是 HotSpot 用戶端的 IP 地址 |
| **dst-address** (*IP*；預設值： ) | 目標 IP 地址，即 WEB 伺服器的 IP 地址。如果已指定 **dst-host**，則忽略。 |
| **src-address-list** (*string*；預設值： ) | 源地址列表名稱 |
| **dst-address-list** (*string*；預設值： ) | 目標地址列表。如果已指定 **dst-host**，則忽略。 |
| **dst-host** (*string*；預設值： ) | 目標 Web 伺服器的域名。指定此引數後，會將動態條目新增到圍牆花園 |
| **dst-port** (*integer*；預設值： ) | 用戶端傳送請求到的 TCP 埠號 |
| **protocol** (*integer \| string*；預設值： ) | IP 協定 |

## IP 繫結 {#ip-binding}

**子選單：** `/ip/hotspot/ip-binding`

IP 繫結 HotSpot 選單允許設定靜態一對一 NAT 轉換，允許特定 HotSpot 用戶端無需任何身份驗證即可繞過，還允許阻止特定主機和子網訪問 HotSpot 網路

| 屬性 | 描述 |
| :-- | :-- |
| **address** (*IP Range*; 預設值: **""**) | 用戶端的原始 IP 地址 |
| **mac-address** (*MAC*; 預設值: **""**) | 用戶端的 MAC 地址 |
| **server** (*string \| all*; 預設值: **"all"**) | HotSpot 伺服器名稱。<ul><li><strong>all</strong> - 將應用於所有 HotSpot 伺服器</li></ul> |
| **to-address** (*IP*; 預設值: **""**) | 用戶端的新 IP 地址，轉換在路由器上進行（用戶端對轉換一無所知） |
| **type** (*blocked \| bypassed \| regular*; 預設值: **""**) | IP 繫結操作的型別<ul><li><strong>regular</strong> - 根據規則執行一對一 NAT，將 <strong>address</strong> 轉換為 <strong>to-address</strong></li><li><strong>bypassed</strong> - 執行轉換，但使用戶端免於登入 HotSpot</li><li><strong>blocked</strong> - 不執行轉換，並且來自主機的封包被丟棄</li></ul> |

## Cookies {#cookies}

該選單包含傳送給 HotSpot 用戶端的所有 cookie，這些用戶端透過 cookie 方法授權。所有條目均為只讀。

**子選單：** `/ip/hotspot/cookie`

| 屬性 | 描述 |
| :-- | :-- |
| **domain** (*string*) | 域名（如果從使用者名稱中分離） |
| **expires-in** (*time*) | cookie 的有效期 |
| **mac-address** (*MAC*) | 用戶端的 MAC 地址 |
| **user** (*string*) | HotSpot 使用者名稱 |

## MAC Cookie {#mac-cookie}

MAC cookie 是一項 HotSpot 功能，旨在改善智慧手機、筆記型電腦和其他移動裝置的可訪問性。

當啟用 MAC cookie 功能時（在使用者配置檔案中設定 **login-by**=mac-cookie、**add-mac-cookie**=yes），會執行以下操作：

- **首次成功登入**。如果只有一個具有該 MAC 地址的主機，Mac cookie 會記錄該 MAC 地址的使用者名稱和密碼。Cookie 超時設定為等於 mac-cookie-timeout 的值。
- **出現新主機**。HotSpot 會檢查該 MAC 地址是否存在 mac cookie 記錄，並使用記錄的使用者名稱和密碼登入該主機。如果同一 MAC 地址有多個主機，則不會登入該使用者，並且該地址的 MAC cookie 記錄會被刪除。

當**使用者登出**時，mac cookie 會在以下情況下被移除：

- user-request - 使用者點選了登出按鈕。
- admin-reset - 從 radius 伺服器斷開連線，或從 HotSpot 活動選單中移除使用者。
- nas-request - 達到流量限制。
- session-timeout。

要偵錯 mac-cookie 相關問題，需要啟用 HotSpot 偵錯日誌，並查詢某個主機的 mac-cookie 登入失敗的原因。

### 伺服器移除 mac cookie 的原因 {#reasons-when-mac-cookie-is-removed-by-server}

- `/ip/hotspot/cookie/remove [number]`。
- Radius 伺服器傳送 Disconnect-Request。
- 終端使用者已透過 HotSpot 狀態頁面自行登出。
- 終端使用者已達到其資料上限（"traffic limit reached"）。
- Session-Timeout。
- 如果 mac-cookie 登入失敗。
- 如果伺服器檢測到主機表中有多個具有相同 mac-address 的條目。

### HotSpot API JSON 的屬性（RFC 7710） {#properties-of-the-hotspot-api-json-rfc-7710}

基於文件中提供的 `api.json` 模板，以下是用於向用戶端裝置傳達強制門戶狀態的每個屬性的說明：

- **captive**：一個布林值（`true` 或 `false`），用於告知用戶端裝置當前是否受強制門戶限制。如果使用者已透過身份驗證，則返回 `false`。
- **user-portal-url**：使用者可訪問登入頁面或管理其當前會話的特定 URL。在 MikroTik RouterOS 中，此值由 `$(link-login-only)` 變數動態填充。
- **seconds-remaining**：（可選）一個整數，表示當前會話到期前剩餘的秒數。僅在配置了會話超時時包含此值。
- **bytes-remaining**：（可選）一個整數，表示使用者可用的剩餘資料配額（以位元組為單位）。僅當對 HotSpot 使用者應用了資料限制時才包含此值。
- **can-extend-session**：一個布林值，指示使用者是否能夠延長其當前會話，或透過門戶購買/請求更多時間/資料。

## 在 HotSpot 伺服器上使用 mangle 進行負載均衡 {#load-balancing-with-mangle-on-hotspot-server}

在多上行鏈路 HotSpot 設定中（例如 [PCC](../../high-availability-solutions/load-balancing/per-connection-classifier.md)，預設路由通常可能無法按預期工作，因為路由器會優先處理 mangle 規則，而不是本地目標檢查。

要解決此問題，請確保發往 HotSpot 伺服器的流量在評估 **mangle** 鏈之前透過 **local** 表路由。你可以透過以下方式實現：

1. 調整 "`/routing/settings"`（[路由表查詢](../../user-guides/routing-and-networking-protocols/routing-decision.md#routing-table-lookup)。
2. 或者，新增特定的 "`/routing/rule"` 條目，以強制 HotSpot 伺服器的流量首先使用 **local** 表（包括用於檢測 HotSpot 伺服器的 HTTP 80 流量）。
