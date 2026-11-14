---
title: "文件更新 - 2026年9月24日"
date: 2026-09-24
slug: /changelog-2026-09-24
source: https://manual.mikrotik.com/changelog/changelog-2026-09-24
captured_at: '2026-11-04T06:08:50+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026 年 9 月 24 日文件變更摘要。

## 網路管理 {#network-management}

- **[Cloud](/docs/network-management/cloud)**：圍繞雲服務的作用重寫了概覽，增加了服務表、這些服務對應的選單以及哪些服務預設執行，並統一說明路由器如何連線到 cloud2.mikrotik.com（UDP 埠 15252）和中繼伺服器。危險提示框和六個警告框已移除；保留了一條關於可用性的說明（MikroTik 裝置和具有付費許可證的 CHR，不適用於 x86）。DDNS 和時間更新行為已在 RouterOS 7.25 上透過抓包和重啟進行驗證：DNS 名稱是小寫的序列號，TTL 為 60 秒；位於 NAT 後的路由器每分鐘傳送一次更新；ddns-enabled=auto 會刪除該名稱；use-local-address 會將其指向本地地址。時間更新在啟動時設定一次時鐘，而不是在 force-update 時設定，也不會在 NTP 用戶端啟用時設定。刪除了錯誤的 update-time=auto 說明以及 DNS 名稱會永久儲存的說法。屬性表已移至 CLI 參考。
- **[Cloud backup](/docs/network-management/cloud/cloud-backup)**：新頁面，從 Cloud 概覽中移出，並用經過測試的示例重寫，涵蓋上傳、替換、刪除、使用秘密下載金鑰在另一臺路由器上下載，以及下載並應用。內容涵蓋單槽位限制及其錯誤訊息、密碼要求，以及對未加密備份檔案的拒絕。
- **[Back To Home（遠端回家）](/docs/network-management/cloud/back-to-home)**：應用操作說明現在改為編號步驟。新增章節列出了 Back To Home 向路由器新增的內容（back-to-home-vpn WireGuard 介面、192.168.216.0/24 和 fc00:0:0:216::/64 地址、動態防火牆和 NAT 規則，以及 vpn.mynetname.net 名稱），如何在 /ip/cloud/back-to-home-user 中管理使用者（含經過測試的用戶端配置），以及撤銷會移除什麼：所有使用者，並在下次啟用時使用新金鑰。這取代了舊版中手動刪除 WireGuard 對端的建議以及不必要的 ddns-enabled=yes 步驟。
- **[File Share](/docs/network-management/cloud/file-share)**：根據透過中繼進行的測試重寫了頁面，涵蓋目錄共享和檔案共享、?dl 下載（目錄使用 download.zip）、上傳（除非 allow-uploads=yes，否則以 403 拒絕）、過期、停用、Let's Encrypt 證書和中繼的工作方式，以及如何使用 remove-certificate 停止服務並刪除證書。修正了 WinBox 選單名稱，並從頁面元資料中刪除了不存在的選單。
- **[Communication with MikroTik Cloud Services](/docs/network-management/cloud/communication-mikrotik-cloud-servers)**：修正了到 MikroTik 伺服器的連線表：cloud backup 也會為 print 建立連線，File Share 在最後一個共享被移除後停止，Back To Home 和 File Share 也會使用中繼伺服器。
- **[Cloud](/docs/network-management/cloud)**、**[Cloud backup](/docs/network-management/cloud/cloud-backup)**、**[Back To Home](/docs/network-management/cloud/back-to-home)**、**[File Share](/docs/network-management/cloud/file-share)**、**[Communication with MikroTik Cloud Services](/docs/network-management/cloud/communication-mikrotik-cloud-servers)**：現在每個頁面的正文都以任務為導向，並以“技術細節”章節結尾。該章節涵蓋使用的伺服器和埠、DDNS 更新和啟動時時間更新的工作方式、Back To Home 向路由器新增的內容、File Share 證書和中繼的工作方式，以及路由器無法連線到雲伺服器時會發生什麼。
- **[DNS](/docs/network-management/dns)**：圍繞任務重寫了頁面，所有內容均在 RouterOS 7.25 上測試：將路由器用作網路的 DNS 伺服器（包括預設配置和防火牆）、靜態條目（記錄型別、正則表示式及其命令列轉義、指向其他伺服器的 FWD 條目、填充防火牆地址列表）、DNS over HTTPS、adlists、forwarders 和 mDNS 中繼器。“技術細節”章節說明了查詢如何得到應答、上游伺服器如何選擇，以及快取、DoH、adlists、forwarders、VRF 和 mDNS 中繼器如何工作。修正了靜態條目的預設值（啟用）和重疊條目的規則，並記錄了 DoH 沒有回退、adlists 僅阻止 A 和 AAAA 查詢且在匯入前需要足夠大的快取、forwarders 不會跳過已失效的伺服器，以及 mDNS 中繼器僅處理 IPv4。屬性表已移至 CLI 參考，17 條提示已改為純文字。
- **[DNS](/docs/network-management/dns)**：為新手和高階讀者重新組織了重寫後的頁面：引言說明 DNS 可在預設配置下工作，並且路由器的這些功能僅適用於將其用作 DNS 伺服器的裝置；新增的“檢查與故障排除”章節涵蓋 :resolve、應答狀態和 dns 日誌主題；各項任務按照讀者需要的順序排列。補充說明 adlists 預設驗證伺服器證書（ssl-verify）、達到 max-concurrent-queries 時會丟棄新查詢，並修正了關於設定更改（會立即生效）以及 mDNS 中繼器所需防火牆規則的措辭。
- **[Proxy](/docs/network-management/proxy)**：該章節索引現在改為兩個 Web 代理的簡短概覽，一個是面向網路中用戶端的 Web 代理，另一個是面向路由器後方伺服器的反向代理，並附有指向 SOCKS 的連結。舊的 Web 代理內容已移至其獨立頁面。
- **[Web Proxy](/docs/network-management/proxy/web-proxy)**：根據 RouterOS 7.25 上的測試重寫了頁面，使用常規代理和透明代理、作為父代理的第二臺路由器以及測試 Web 伺服器。現在解釋了 HTTPS：代理會為常規用戶端中繼 CONNECT 隧道，僅按主機名、地址和埠過濾，無法快取這些隧道，也無法在透明模式下處理 HTTPS。新增章節涵蓋防止代理變成開放代理（它監聽所有 IPv4 和 IPv6 地址，並開啟到任意埠的隧道）、使用 monitor、connections 和 web-proxy 日誌主題進行檢查與故障排除、主機和路徑規則如何匹配（整字串且不區分大小寫的主機名、路徑中的查詢字串、: 正則表示式）、redirect 動作、透過 reset-html 生成的可編輯錯誤頁面、快取會儲存哪些響應以及何時不詢問伺服器直接應答、X-Cache 和快取命中時的 DSCP 標記、父代理和 Direct 列表、代理新增的標頭，以及一張簡短的 HTTP 方法表。刪除了 dst-host 會匹配 URL 中單詞的錯誤說法、過時的 redirect-to 引數、Direct 列表自相矛盾的預設值以及複製的 RFC 2616 文字。屬性表已移至 CLI 參考。
- **Cloud 章節圖片**：將截圖轉換為 WebP，刪除了九個未使用的重複檔案，併為每張圖片添加了替代文字。
- **[SOCKS](/docs/network-management/socks)** 和 **[Socksify](/docs/network-management/socks/socksify)**：根據 RouterOS 7.25 上的測試重寫了這兩個頁面，並在兩臺路由器之間的線路上捕獲了經代理的連線。SOCKS 頁面現在首先介紹如何啟用伺服器，並說明預設的 version=4 會拒絕 SOCKS5 用戶端、訪問列表如何決定（首個匹配生效，無匹配則允許，因此限制性列表以拒絕規則結尾）、使用者建立後即為啟用狀態（舊預設值是錯誤的），以及如何通過當前 print 示例監控連線。Socksify 頁面說明了 NAT action=socksify 的作用、上游必須是 IPv4 地址上的 SOCKS5 伺服器、設定更改僅在記錄被停用並重新啟用後生效，以及該服務拒絕代理 LAN（RFC 1918）目標，日誌為 cannot socksify LAN destination。Tor 示例和警告框現在使用 dst-address-type=!local，因為不帶該引數的規則會重定向路由器自身的服務，並可能切斷管理訪問。屬性表已移至 CLI 參考。

## CLI 參考 {#cli-reference}

- **[/ip/dns](/docs/cli-reference/ip/dns)**、**[/ip/dns/static](/docs/cli-reference/ip/dns/static)**、**[/ip/dns/adlist](/docs/cli-reference/ip/dns/adlist)**、**[/ip/dns/forwarders](/docs/cli-reference/ip/dns/forwarders)**：描述了 DNS 解析器、靜態條目、快取、adlists 和 forwarders 的全部 69 個引數、標誌和命令（其中 51 個為空），並在 RouterOS 7.25 上檢查了預設值和行為。
- **[/ip/cloud](/docs/cli-reference/ip/cloud)**、**[/ip/cloud/back-to-home-user](/docs/cli-reference/ip/cloud/back-to-home-user)**、**[/ip/cloud/back-to-home-file](/docs/cli-reference/ip/cloud/back-to-home-file)**、**[/system/backup/cloud](/docs/cli-reference/system/backup/cloud)**：為 DDNS、時間更新、Back To Home 及其使用者、File Share 及其設定以及 cloud backup 的所有先前為空的引數、標誌和命令編寫了說明，全部在 RouterOS 7.25 上檢查。它們包含其他地方沒有記錄的行為，例如 Back To Home 使用者只能在 vpn-status 執行時新增、使用者建立後不能更改 expires、client-address 會自動分配，以及每條命令的狀態值和錯誤訊息。
- **[/ip/proxy](/docs/cli-reference/ip/proxy)**、**[/ip/proxy/access](/docs/cli-reference/ip/proxy/access)**、**[/ip/proxy/cache](/docs/cli-reference/ip/proxy/cache)**、**[/ip/proxy/direct](/docs/cli-reference/ip/proxy/direct)**：描述了 Web 代理設定，access、cache 和 direct 列表，connections，快取計數器，快取內容，monitor 以及命令（91 行中有 85 行為空），包括舊頁面未提及的帶 action-data 的 redirect 和 url-append 動作。
- **[/ip/socks](/docs/cli-reference/ip/socks)**、**[/ip/socks/access](/docs/cli-reference/ip/socks/access)**、**[/ip/socks/connections](/docs/cli-reference/ip/socks/connections)**、**[/ip/socks/users](/docs/cli-reference/ip/socks/users)**、**[/ip/socksify](/docs/cli-reference/ip/socksify)**：描述了 SOCKS 伺服器、其訪問列表、活動連線和使用者以及 socksify 服務的所有引數、標誌和只讀值，並在 RouterOS 7.25 上進行了檢查。這包括其他地方沒有記錄的行為，例如 version=4 僅接受 SOCKS4 用戶端、auth-method=password 在沒有使用者時會拒絕所有內容、訪問列表中的域名僅匹配基於名稱的請求，以及 vrf 選擇伺服器監聽的 VRF。

## 入門 {#getting-started}

- **[Backup](/docs/getting-started/configuration-management/backup)**、**[包含敏感引數的選單列表](/docs/getting-started/configuration-management/list-of-menus-with-sensitive-parameters)**：現在連結到新的 Cloud backup 頁面和 Back To Home 頁面。
