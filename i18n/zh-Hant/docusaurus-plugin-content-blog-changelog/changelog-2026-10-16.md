---
title: "文件更新 - 2026年10月16日"
date: 2026-10-16
slug: /changelog-2026-10-16
source: https://manual.mikrotik.com/changelog/changelog-2026-10-16
captured_at: '2026-11-04T06:09:04+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026 年 10 月 16 日的文件變更摘要。

## 入門 {#getting-started}

- **[Backup](/docs/getting-started/configuration-management/backup)**：全面改寫，已在 hAP ax² 實驗室路由器上的 RouterOS 7.26beta1 上測試。改造成面向任務的頁面：儲存加密備份、在檔案列表中校驗它、恢復它（包括確切的確認流程）、備份包含與不包含的內容（特定於裝置，包含裝置的 MAC 地址；The Dude 和 User Manager 資料庫除外），以及一個故障排查章節。在實驗室驗證了：僅設定密碼即使用 aes-sha256 加密，dont-encrypt=yes 即使設定了密碼檔案也保持不加密，並且未加密的備份以可讀形式儲存配置。用全新的截圖替換了 2018 年代的示例輸出，並連結到更輕量的替代方案（安全模式、撤銷/重做）和 Files 頁面。

## CLI 參考 {#cli-reference}

- **[/system/backup/save](/docs/cli-reference/system/backup/save)**、**[/system/backup/load](/docs/cli-reference/system/backup/load)**：移除了“自 RouterOS v6.43 起”這類版本限定語；引數說明已在實驗室驗證並重寫（save：name、password、使用 aes-sha256 預設值與舊式 rc4 的 encryption、dont-encrypt；load：name、password、force-v6-to-v7-configuration-upgrade）。
- **[/tool/traffic-generator](/docs/cli-reference/tool/traffic-generator)**：全部 14 個頁面的完整引數說明（參見上文的 Traffic Generator），包括預設值（test-id 0、latency-distribution-max 100us、stats-samples-to-keep 100）和 stats 子選單的列。

## 開發者指南 {#developer-guides}

- **[API](/docs/developer-guides/api)**：協定參考已全面改寫，並針對 7.26beta1 實驗室路由器上的 API 服務進行了驗證（透過 8728 的明文登入與舊式 challenge、tags、帶 category=2 中斷 trap 的 listen/cancel、getall、query words、透過 .proplist 獲取 OID、traps）。重寫了初始登入章節，把明文方式作為登入方法，把 MD5 challenge-response 作為舊版 RouterOS 的方法（當前 RouterOS 會拒絕舊式響應）；更新了 OID 示例（cpu-load 不再附帶 OID）；修正了 trap 章節（並非每個 trap 都帶有 category 屬性）和 listen 示例（布林值現在列印為 true/false，已刪除項報告 =.dead=true）；移除了 2006/2010 年代的示例記錄；並說明無證書的 api-ssl 模式只提供匿名 Diffie-Hellman 加密套件，當前的 TLS 用戶端會拒絕它。
- **[Python 3 示例](/docs/developer-guides/api/python3-example)**：重寫了示例用戶端：優先使用明文登入並自動回退到舊式 challenge-response，修復了輸入關閉時的無限迴圈，採用 utf-8 編碼，並添加了說明證書要求的 secure-mode 註釋。重寫後的用戶端已針對實驗室 API 測試。
- **[開發者指南](/docs/developer-guides)**：精簡了著陸頁文字。
- **[Scripting](/docs/developer-guides/scripting)**：已重寫，並在 7.26beta1 實驗室路由器上逐條驗證。修正了作用域規則（全域性變數不限於其宣告所在的塊；在互動式 CLI 中，:local 在後續行中仍然可見；未宣告的變數可以讀取並返回空值，但給它賦值是編譯錯誤）、位運算子章節（&、|、^、&lt;&lt;、&gt;&gt; 作用於整數以及 IP/IPv6 地址；只有 ~ 僅限 IP —— IPv6 的移位是可行的）、十六進位制轉義規則（十六進位制字母必須大寫，\ff 解析為 \f + f）、:nothing 和 :tolf 參考行，以及 !comments 列印引數（它隱藏註釋橫幅，並不過濾條目）。更新了 :timestamp 示例和保留變數名說明（與內建屬性衝突的名稱在 where 表示式中會解析為每項屬性）。
- **[Scripting 示例](/docs/developer-guides/scripting/scripting-examples)**：已在實驗室驗證檔案建立/追加的變通方法和 DNS 快取站點遮蔽示例；添加了一條說明，指出 ppp-secret 解析器需要 CR/LF 行結尾，以及使用防火牆 tls-host（SNI、HTTPS）和 content（HTTP）匹配器進行站點遮蔽的另一種方法。
- **[Scripting 技巧與提示](/docs/developer-guides/scripting/scripting-tips-and-tricks)**：修正了三條關於宣告全域性變數的技巧，它們已不再符合當前 RouterOS —— 指令碼或函式可以讀取全域性變數，或呼叫另一個指令碼中定義的函式，而無需重新宣告；只有在修改其值時才需要宣告。指出 /interface wireless info hw-info 技巧僅適用於使用舊版 wireless 軟體包的裝置。

## 診斷、監控與故障排查 {#diagnostics-monitoring--troubleshooting}

- **[Traffic Generator](/docs/diagnostics-monitoring-and-troubleshooting/traffic-generator)**：改為面向任務的頁面：屬性表移入 CLI 參考，其中 14 個頁面都獲得了完整的引數說明（包括帶 IPv4/IPv6/UDP/TCP 頭部欄位的 packet-template 構建器和 stats 子選單）。將流屬性 num 更正為 id（舊名稱已不存在），新增了 packet-count、cpu-core 和只讀的 default-port 流屬性，用 ipv6 和 tcp 頭部更新了 header-stack/first-header 列舉，並移除了快捷命令的 duration 和 freeze-frame-interval 引數（在 7.26 上已不存在）。device-mode 資訊框現在說明：每種 device mode 下流量生成器預設都是停用的、如何檢查它，以及啟用它需要物理確認（按下按鈕或斷電重啟）。修正了 IPsec 基準測試示例 —— enc-algorithms=aes-128 在 RouterOS 7 上是語法錯誤，現改為 aes-128-cbc。
- **[降級 RouterOS](/docs/diagnostics-monitoring-and-troubleshooting/downgrading-routeros)**：已按當前 RouterOS 更正 —— factory-software 欄位已更名為 minimum-version，架構報告為 architecture-name；用真實的 /system/resource/print 捕獲替換了虛構的示例輸出，指出降級需要主 routeros 軟體包以及每個已安裝的額外軟體包（例如 wireless 驅動），並且路由器會在重啟期間降級到所上傳軟體包的版本。
- **[使用 Elasticsearch 進行 NetFlow 分析](/docs/diagnostics-monitoring-and-troubleshooting/traffic-flow/netflow-analysis-with-elasticsearch)**、**[使用 Elasticsearch 的 CEF](/docs/diagnostics-monitoring-and-troubleshooting/log/cef-with-elasticsearch)**、**[使用 Elasticsearch 的 Syslog](/docs/diagnostics-monitoring-and-troubleshooting/log/syslog-with-elasticsearch)**：已在實驗室驗證 RouterOS 側的命令（/system/logging/action 使用 remote-log-format=syslog/cef、syslog-facility、cef-event-delimiter、syslog-time-format；/ip/traffic-flow 使用介面列表和預設 2055/UDP 上的目標，NetFlow v9），修復了缺失的圖片替代文字和格式錯誤的 ros_paths，並澄清了 CEF 示例的動作名稱和 Elastic 側的預設埠。

## 虛擬專用網路 {#virtual-private-networks}

-

**[GRE](/docs/virtual-private-networks/gre)**：在一對透過 GRE 隧道相連的 7.26beta1 實驗室路由器上逐條驗證並重寫。修正了 keepalive 章節 —— keepalive 預設啟用（10s,10，最小間隔 1 秒；設為 0 秒會被拒絕，取消該屬性會移除它，但對觀察到的 running 標誌行為沒有任何改變），並且在所測試的版本上，即使遠端不可達，隧道仍保持 running 標誌（running 標誌只保證遠端曾應答過一次）；重新整理了圍繞它的無狀態/黑洞說明。移除了 GRE 可用於橋接設計的說法 —— 在 RouterOS 7 上該介面無法作為橋埠新增（EoIP 覆蓋二層）。在實驗室確認了開銷數字（在 1500 位元組介面上，GRE over IPv4 的 actual-mtu 為 1476，GRE over IPv6 為 1456），驗證了 ipsec-secret 需要停用 fast-path，添加了故障排查章節，並重新整理了雙站點示例（包括在實驗室執行確切的配置）。

-

**[EoIP](/docs/virtual-private-networks/eoip)**：在一對透過橋接 EoIP 隧道相連的 7.26beta1 實驗室路由器上逐條驗證並重寫。端到端確認了二層行為（跨隧道的橋接、ARP、RSTP 和 MAC 學習）以及 42 位元組開銷（帶 key 的 8 位元組 GRE 頭部、完整的內部乙太網幀、外部 IPv4 頭部）—— 在 1500 位元組路徑上，EoIP over IPv4 的 actual-mtu 為 1458，IPv6 為 1444。記錄了真實的 keepalive 行為：預設啟用（10s,10），當對端在 interval × retries 時間內不應答時會移除 running 標誌；小於 1 秒的值會被拒絕，取消 keepalive 會關閉該機制（此時即使對端已死，標誌仍保持 up）。說明了僅憑 running 標誌並不能證明 tunnel-id 匹配（id 不匹配時兩端都保持 running，但丟棄所有流量）、MAC 地址處理（預設本地管理，接受任意值 —— 每個橋內保持唯一）以及 IPsec 選項（ipsec-secret，IPv4 上需要 allow-fast-path=no；IPv6 選單沒有 fast-path 屬性）。針對預設 RouterOS 配置重做了雙站點無線示例（LAN 埠已經橋接），並在實驗室驗證了確切的配置。
