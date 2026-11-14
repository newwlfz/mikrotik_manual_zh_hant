---
title: "文件更新 - 2026年9月25日"
date: 2026-09-25
slug: /changelog-2026-09-25
source: https://manual.mikrotik.com/changelog/changelog-2026-09-25
captured_at: '2026-11-04T06:08:51+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026 年 9 月 25 日文件變更摘要。

## 認證與 AAA {#authentication--aaa}

- **[使用者](/docs/authentication-authorization-accounting/user)**：整頁重寫：分步示例現在放在最前面（建立組和使用者、密碼修改與過期、SSH 金鑰匯入、使用 User Manager 的 RADIUS 登入），屬性表已移至 CLI 參考。實驗室驗證後修正了若干過時事實：key-owner SSH 金鑰引數改為 info，會話透過 /user/active/remove 關閉（request-logout 已移除），自己的密碼透過 /password 修改，使用者名稱字元規則已有準確說明。新增了經核實的細節：密碼規則（任意字元、空密碼）、無活動登出/鎖屏行為、SSH 金鑰檔案格式、Mikrotik-Group RADIUS 屬性、exclude-groups 保護以及 RADIUS 計費（Start/Stop 與 interim updates）。

## 橋接與交換 {#bridging--switching}

- **[L3 硬體解除安裝](/docs/bridging-and-switching/l3-hardware-offloading)**：說明了配備 Marvell 98DX7xxx 交換晶片的裝置也能在直接創建於乙太網交換埠上的 VLAN 介面之間解除安裝路由，無需網橋；在其他所有 L3HW 裝置上，VLAN 介面仍必須位於硬體解除安裝的網橋上。相應更新了 VLAN 間路由說明、功能表和每埠設定名稱（l3-hw-offloading）。

## CLI 參考 {#cli-reference}

- **[/system/ntp](/docs/cli-reference/system/ntp/client)**：補全了 NTP 各選單的所有描述 — client、client servers、server、symmetric keys、monitor-peers 欄位以及 reset-freq-drift — 並附經核實的預設值和行為，例如輪詢間隔範圍（2 的冪，預設 64 秒到 1024 秒）和 using-local-clock 回退狀態。
- **[/file](/docs/cli-reference/file)**：為 /file 及其 copy、head、read 和 tail 命令添加了選單介紹，並連結回指南。新增經核實的細節：contents 屬性限制在略低於 60 KiB（更大的檔案請使用 /file/read），read 需要 chunk-size，head/tail 預設 10 行，copy 會遞迴複製目錄，S 標誌和 url 屬性描述 Back To Home（遠端回家） File Share 條目。
- **[/user](/docs/cli-reference/user)**：補全了所有 /user 選單和命令的描述 — users、groups 及全部 17 項策略、settings、active sessions、AAA、expire-password 以及 SSH 公鑰/私鑰 — 包括經核實的預設值、範圍和列舉值。
- **[/system/scheduler](/docs/cli-reference/system/scheduler)**：補全了所有描述：start-date/start-time 預設值、有無 interval 時的啟動行為、days 的取值（unset、always、never、weekdays）及其與 interval 的組合方式、執行與啟動時間的對齊、預設策略，以及 next-run 何時為空。
- **[/disk](/docs/cli-reference/disk)**：補全了 /disk 選單及其命令（copy、format、check、repair、monitor-traffic、test、nvme-discover、settings、smart-info、blink）的描述，包括每個標誌（block device、mounted、swap、RAID member、SMB/NFS/iSCSI/NVMe-over-TCP 共享、TCG-Opal 自加密）、copy 偏移和進度狀態，以及 check 輸出。
- **[/routing/igmp-proxy/interface](/docs/cli-reference/routing/igmp-proxy/interface)、[/routing/pimsm/interface](/docs/cli-reference/routing/pimsm/interface)**：補全了 IGMP proxy 和 PIM-SM 的描述：全域性和每介面的 robustness 與 query 定時器（每介面值覆蓋全域性值）、querier 和流量計數器狀態欄位、IGMP 介面模板、DR 優先順序和 hello 定時器，以及 join-tracking、designated-router 和 RP-local 標誌。從 IGMP proxy 介面頁面移除了過時的 print 狀態示例。

## 開發者指南 {#developer-guides}

- **[指令碼](/docs/developer-guides/scripting#script-permissions)**：修正了指令碼許可權章節：按名稱呼叫指令碼的 scheduler 條目會以該條目的策略執行，與普通的 /system script run 相同；只有 use-script-permissions 才使用指令碼自身的策略。示例日誌已在當前 RouterOS 版本上更新。

## 入門 {#getting-started}

- **[保護路由器安全](/docs/getting-started/securing-your-router)**：新增“使用者賬戶與組”步驟：每個管理員一個賬戶、自定義最小許可權組（內建的 read 組可以重啟路由器並檢視敏感配置），以及 SSH 金鑰登入（會為該使用者停用 SSH 密碼認證）。

## 硬體 {#hardware}

- **[磁碟](/docs/hardware/disks)**：將頁面重組為任務章節：磁碟如何被檢測（插槽名稱和 B/E/M 標誌）、格式化及所有檔案系統選項（包括 discard 和 wipe）、掛載點和 mount-point-template、分割區、交換空間（最高為 RAM 的 10 倍，用於容器）、RAM 支援的資料夾、映象掛載、磁碟上的日誌和 Web 代理快取、檢查與修復、效能測試、monitor-traffic、彈出、掃描與 trim（USB 驅動器不支援）以及 S.M.A.R.T.。屬性、標誌和設定表已移至 CLI 參考，大多數示例現在顯示當前 RouterOS 版本的輸出。
- **[S.M.A.R.T. 資訊](/docs/hardware/disks/smart)**：圍繞讀取 /disk/smart-info 重寫了頁面：哪些值對驅動器健康重要、輸出與 Linux 上 smartctl 報告相同，以及某些 USB 硬碟盒無法透傳 S.M.A.R.T. 資料。

## 高可用性解決方案 {#high-availability-solutions}

- **[多機箱鏈路聚合組](/docs/high-availability-solutions/multi-chassis-link-aggregation-group)**：移除了 MLAG 與 MVRP 不相容的過時說明。

## 網路管理 {#network-management}

- **[Web 代理](/docs/network-management/proxy/web-proxy)**：新增示例，說明將 cache-path 設定為不存在的路徑會自動建立目錄，並且快取隨後會在 /file 中顯示為 web-proxy store。

## 系統 {#system}

- **[NTP](/docs/system-information-and-utilities/ntp)**：圍繞經核實的 RouterOS v7 行為重寫了頁面：帶真實輸出的 client 和 server 示例、stopped/waiting/synchronized/using-local-clock 狀態含義、DHCP 提供的動態伺服器、FQDN 解析為 resolved-address、對稱金鑰認證（金鑰不匹配時 crypto NAK）以及 monitor-peers 輸出說明。用當前的 ntp 主題訊息替換了 RouterOS v6 SNTP 日誌章節。
- **[檔案](/docs/system-information-and-utilities/files)**：實驗室驗證後重做了頁面。修正了 /file/read 的描述（它在 data 中返回字串，而不是陣列），記錄了真實的 contents 大小限制、head/tail 的預設 10 行以及目錄複製是遞迴的。所有示例都已用當前 RouterOS 版本的輸出更新，頁面現在連結到 File Share 和 Rsync 指南以瞭解相關的 /file 屬性和選單。
- **[排程器](/docs/system-information-and-utilities/scheduler)**：圍繞經核實的 RouterOS v7 行為重寫了頁面。修正了若干說法：days 預設未設定（不是 always，後者會在每天 start-time 重新啟動）、同時到期的條目以不固定順序執行、啟動條目在介面和 DHCP 就緒之前執行，且 days 不支援一天或更長的間隔。新增了執行如何計算以及許可權如何應用的說明，並用實用示例替換了寫日誌的演示：每晚備份和匯出、夜間關閉 LED、每次重啟後傳送郵件、工作時間開放訪客 Wi-Fi、每週郵件備份、新 RouterOS 版本通知、每週隨機訪客 Wi-Fi 密碼，以及按時間段限制訪客頻寬。

## 使用者指南 {#user-guides}

- **[IGMP Proxy](/docs/user-guides/routing-and-networking-protocols/multicast/igmp-proxy)**：將 /routing/igmp-proxy/interface/print 的輸出更新為當前 RouterOS 格式，包含 upstream、robustness 和 query 定時器列。
