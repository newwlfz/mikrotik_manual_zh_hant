---
title: "文件更新 - 2026年10月1日"
date: 2026-10-01
slug: /changelog-2026-10-01
source: https://manual.mikrotik.com/changelog/changelog-2026-10-01
captured_at: '2026-11-04T06:08:54+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026 年 10 月 1 日所做的文件更改摘要。

## 入門 {#getting-started}

- **[Supout.rif](/docs/getting-started/supout-rif)**：已重寫。更正：該檔案是文字，包含經過編碼的各個部分，並非二進位制檔案。新增：該檔案包含哪些內容以及何時建立它、將其寫入資料夾、使用 scheduler 在指定時間建立它、使用 Files 或 scp 下載它、崩潰後自動生成的 autosupout.rif，以及檔案格式。截圖現在位於正確的 WinBox 和 WebFig 章節中，並帶有替代文字。[Try before RMA](/docs/hardware/try-before-rma) 現在連結到這裡，而不是 Resource 頁面。

## 儲存 {#storage}

-

**[Tmpfs](/docs/storage/tmpfs)**：已重寫，並在 RouterOS 7.26 上測試。更正：tmpfs 是基礎 RouterOS 軟體包的一部分，不需要 Storage 軟體包（SMIPS 裝置上也沒有）。新增章節：

- 建立 RAM 資料夾，以及各個大小的含義：十進位制單位、是最大 RAM 而非預留 RAM、未設定 tmpfs-max-size 時約為 RAM 的一半，以及總大小檢查。
- 檢查該資料夾共享了什麼：在預設配置開啟自動磁碟共享的路由器上（例如 hAP ax²），新建資料夾會透過 SMB 共享給無需密碼的 guest 使用者，並透過 DLNA 共享。如何檢查，以及如何建立不共享的資料夾或停止共享。
- 將封包捕獲儲存在 RAM 中並下載它們，檢查資料夾有多滿（資料夾滿了會導致寫入失敗），調整其大小並刪除它。
- 技術細節：重啟後該資料夾會再次被掛載為空，並且 tmpfs 無法被格式化（塊裝置請使用 Ramdisk）。
- [Disks](/docs/hardware/disks) 的 "RAM-backed folder" 章節現在連結到這裡。

-

**[DLNA Media Server](/docs/storage/dlna)**：已重寫，並使用一臺計算機和另一臺路由器作為播放器進行了測試：

- 與區域網路中的電視共享 USB 磁碟，並使用 allowed-ip 或 allowed-hostname 將伺服器限制為單一裝置（DHCP 主機名，精確匹配且區分大小寫；兩者只能設定一個）。有一條註釋說明這些限制不是訪問控制。
- 自動磁碟共享所建立的動態伺服器（hAP ax² 預設配置會開啟它）。它們無法被編輯，因此在新增受限伺服器之前，請關閉該磁碟的媒體共享。
- 列出哪些檔案：僅列出副檔名為小寫的媒體檔案，影片旁邊的 .srt 檔案會成為其字幕。沒有 path 的伺服器共享路由器的整個檔案列表。
- 故障排除，以及技術細節：SSDP 發現、TCP 埠 2828 上的 HTTP、縮圖，以及伺服器為何只在其自身介面上響應。

## 防火牆與 QoS {#firewall--qos}

- **[Address lists](/docs/firewall-and-quality-of-service/firewall/address-lists)**：已從單個 v6 時代的示例重寫為多項任務，每項均按原文匯入並在 RouterOS 7.26 上測試：

- 使用 raw 規則阻止來自地址列表的流量，適用於 IPv4 和 IPv6。
- 透過 DNS 名稱允許來自動態地址的 SSH 和 WinBox，規則放置在預設丟棄規則之前，並警告這會開放什麼。
- 阻止探測關閉埠的主機一天，並帶有一個該規則會跳過的受信任列表，因為一個帶有偽造源地址的封包就足以將其列入。
- 檢視、刪除、匯出和匯入條目。file= 必須位於 where 之前，否則匯出會列印到終端而不會寫入檔案。
- 條目的行為方式：靜態和動態條目以及重啟後會保留什麼、超時（最長 35w3d13h13m56s，每次新匹配都會重設）、字首和範圍如何儲存，以及 DNS 名稱如何解析。
- 更正：以短格式書寫的範圍（例如 203.0.113.1-254）會被儲存為 DNS 名稱，不會匹配任何內容，並且 IPv6 列表不接受範圍。

## 診斷與監控 {#diagnostics--monitoring}

- **[Speed Test](/docs/diagnostics-monitoring-and-troubleshooting/speed-test)**：已重寫，並在兩臺路由器之間以及與路由器自身的頻寬伺服器之間進行了測試。

- 前提條件：遠端路由器的頻寬測試伺服器、其所在組具有 test 和 winbox 策略的使用者、裝置模式，以及兩臺路由器上的防火牆規則。如果測試路由器上沒有規則，其防火牆會丟棄 UDP 下載流量。
- 新增章節，包含經過測試的、用於透過網際網路進行測試的防火牆規則。要限制誰可以執行測試，請使用伺服器的 allowed-addresses4 和 allowed-addresses6：使用者的地址設定不會限制頻寬測試登入。
- 一張解釋結果行的表格，以及對 CPU 警告的解釋。
- 針對 authentication failed、缺少吞吐量或 UDP 行以及裝置模式的故障排除。
- 技術細節：test-duration 由五部分組成（預設 10 秒，至少 5 秒）、每秒 20 次 ping、TCP 連線以及所使用的埠。
- 更正了舊的引數說明。預設 connection-count 為 20，或者當執行測試的路由器 CPU 核心數超過 20 時，為其核心數（在 64 核路由器上測試）。

- **[Bandwidth test](/docs/diagnostics-monitoring-and-troubleshooting/bandwidth-test)**：現在連結到 Speed Test。
- **[Detect Internet](/docs/diagnostics-monitoring-and-troubleshooting/detect-internet)**：已重寫，狀態規則在實驗鏈路上經過測試。當路由器到 8.8.8.8 的活動路由經過某個介面時，該介面變為 wan；當到 cloud.mikrotik.com 的路由也經過它，並且雲服務在 UDP 埠 30000 上應答時，則變為 internet。刪除了舊規則（即 DHCP 使介面成為 WAN）以及它會安裝 DHCP 用戶端和路由的警告（這在實驗環境中並未發生）。已驗證並保留：一小時的 LAN 鎖定，以及僅在鏈路變化後才返回 lan。新增：在預設配置的路由器上捕獲的示例、它會填充的介面列表以及它們為何不應屬於 trust 規則、一條說明它不是故障轉移健康檢查的註釋、故障排除以及如何將其關閉。
- **[Watchdog](/docs/diagnostics-monitoring-and-troubleshooting/watchdog)**：在對實驗路由器故意觸發 ping watchdog 重啟後重寫。路由器在 ping-timeout 內對地址 ping 六次，當六次全部失敗時重啟，隨後日誌會顯示 System rebooted because of ping watchdog timeout。no-ping-delay 現在為 ping-start-after-boot。新增：一個實際示例、關於反覆重啟的警告、啟動後應等待多久，以及支援輸出設定。
- **[DNS update](/docs/diagnostics-monitoring-and-troubleshooting/dynamic-dns)**：Dynamic DNS 頁面現在介紹 /tool/dns-update，並針對常見情況指向 IP Cloud DDNS 和 Fetch。已針對測試 DNS 伺服器進行測試：更新透過 TCP 埠 53 進行，使用 hmac-md5 簽名，並替換該名稱的 A 記錄；name 相對於 zone；預設 TTL 為一天。新增：前提條件、如何保持名稱最新，以及每條錯誤訊息的含義。

## 系統 {#system}

- **[IP Packing](/docs/system-information-and-utilities/ip-packing)**：已重寫。刪除了 v6 風格的發現命令；前提條件現在說明兩臺路由器上的介面都必須執行鄰居發現。新增：如何使用鄰居列表的 unpack 欄位檢查它，以及它增加的延遲。一條警告說明，路由器透過打包鏈路開啟的 TCP 連線會失敗。

## CLI 參考 {#cli-reference}

- **[/disk](/docs/cli-reference/disk)、[/disk/settings](/docs/cli-reference/disk/settings)**：tmpfs-max-size 描述了單位、預設大小、總大小檢查以及即時調整大小。自動共享相關行註明 hAP ax² 預設配置會開啟它們。
- **[/ip/firewall/address-list](/docs/cli-reference/ip/firewall/address-list)、[/ipv6/firewall/address-list](/docs/cli-reference/ipv6/firewall/address-list)**：新的引言和更正後的行。只有恰好為一個字首的範圍才會被儲存為字首，帶超時的條目是動態的且不會被儲存，並解釋了 dynamic=yes 和 DNS 名稱。
- **[/ip/firewall/raw](/docs/cli-reference/ip/firewall/raw) 以及其他 filter、mangle、raw 和 NAT 表（IPv4 和 IPv6）**：address-list-timeout 現在涵蓋時間（每次新匹配都會重設）、none-dynamic（與 0s 相同）和 none-static。
- **[/system/sup-output](/docs/cli-reference/system/sup-output)、[/ip/media](/docs/cli-reference/ip/media)、[/ip/media/settings](/docs/cli-reference/ip/media/settings)**：所有行均已說明，包括媒體伺服器的預設值、allowed-ip 和 allowed-hostname，以及縮圖效果。
- **[/interface/detect-internet](/docs/cli-reference/interface/detect-internet)、[/interface/detect-internet/state](/docs/cli-reference/interface/detect-internet/state)、[/system/watchdog](/docs/cli-reference/system/watchdog)、[/tool/dns-update](/docs/cli-reference/tool/dns-update)、[/ip/packing](/docs/cli-reference/ip/packing)**：所有行均已說明，包含來自指南頁面的預設值和已驗證行為。
- **[/tool/speed-test](/docs/cli-reference/tool/speed-test)**：全部 14 行均已說明：connection-count 和 test-duration 的範圍與預設值、測試使用者所需的策略、status 值以及結果行。
