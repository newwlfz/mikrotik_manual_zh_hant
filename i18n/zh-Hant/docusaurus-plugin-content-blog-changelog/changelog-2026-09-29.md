---
title: "文件更新 - 2026年9月29日"
date: 2026-09-29
slug: /changelog-2026-09-29
source: https://manual.mikrotik.com/changelog/changelog-2026-09-29
captured_at: '2026-11-04T06:08:54+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026 年 9 月 29 日文件變更摘要。

## 系統 {#system}

-

**[時鐘](/docs/system-information-and-utilities/clock)**：已重寫並在 RouterOS 7.26 上驗證。該頁面現在涵蓋時間來源（NTP 用戶端、帶 update-time 的 MikroTik 雲、GPS、手動）、命名時區和檢測到的時區，以及手動夏令時。它新增了故障排查列表，針對 1970 年日期、錯誤檢測到的時區，以及重啟後或設定日期後時鐘差一小時的問題。更正：在 time-zone-autodetect 開啟時手動設定的時區會在下一次啟動後被替換，而不是立即替換；dst-start/dst-end 中省略的日期或時間部分會被重設，而不是保留。另已更正：應分別用單獨的命令設定日期和時間，可接受的最晚日期是 2038-01-19 03:14:07 UTC，更晚的日期會被忽略。

-

**[Fetch](/docs/system-information-and-utilities/fetch)**：已重寫，每個示例都在兩臺路由器之間以及針對一臺記錄每次請求的伺服器進行了測試：

- FTP 和 SFTP 下載與上傳、URL 形式，以及從 /ip/tftp 使用 TFTP。
- 使用 check-certificate=yes 進行證書檢查（預設關閉），包括主機名、內建信任儲存和時鐘。
- 新任務：透過 SFTP 上傳備份、安全地下載並匯入指令碼，以及傳送 JSON webhook 通知。
- 更正：重定向計數（預設兩次重定向）、output=user（64512 位元組）和 user-with-headers（20480 位元組）的大小限制，以及舊的 4 KB 檔案限制（最大 60000 位元組的檔案可正常工作）。
- 指令碼示例現在會處理末尾換行符和失敗的請求。

-

**[TFTP](/docs/system-information-and-utilities/tftp)**：圍繞任務重寫，每個示例都針對 TFTP 用戶端執行：提供資料夾服務、為每次請求提供一個檔案、一個檔案對應兩個名稱、接受上傳以及拒絕請求。新增：包含用戶端錯誤碼和 tftp 日誌主題的故障排查列表、規則如何匹配（正則表示式、錨點、控制檯中的 \$），以及關於塊大小、流水線和超過 65535 個塊的檔案的技術細節。更正：read-only 預設為 yes，ip-addresses 是可選的，伺服器從第一條規則開始執行，以及舊的 (aaa.bin)|(bbb.bin) 示例匹配到的名稱遠多於預期。有一條警告說明了如何編寫只匹配你所提供名稱的規則。

-

**[服務](/docs/system-information-and-utilities/services)**：API 示例現在使用 available-from，而不是已棄用的 address，輸出是在 RouterOS 7.26 上捕獲的。

## 防火牆與 QoS {#firewall--qos}

- **[DDoS 防護](/docs/firewall-and-quality-of-service/user-guides/ddos-protection)**：使用第二臺路由器作為攻擊者和伺服器進行了測試。檢測在預設配置的 forward 鏈中有效。但是，對於埠轉發的服務，raw drop 規則從未匹配，因為它在目標 NAT 之前看到的是路由器的公網地址。本頁現在新增了一條 forward 鏈規則，在 NAT 之後丟棄檢測到的地址對，並在檢查命令中顯示其計數器。

## 診斷與監控 {#diagnostics--monitoring}

- **[封包嗅探器](/docs/diagnostics-monitoring-and-troubleshooting/packet-sniffer)**：圍繞為 Wireshark 捕獲到檔案、即時檢視封包、在控制檯中讀取捕獲內容以及透過 TZSP 流式傳輸到 Wireshark 進行重寫，輸出在 RouterOS 7.26 上捕獲。已測試並現已說明：傳給 start 或 quick 的過濾器會替換該次執行已儲存的過濾器，不同的過濾器總是會組合在一起，memory-scroll 保留最新或最前面的封包，嗅探器執行時關閉 fast path 和 FastTrack，嗅探器所見到的 NAT 和 VLAN 標籤，以及 filter-stream=yes 還會在使用流式伺服器時隱藏 ICMP。更正：filter-stream 預設為 no，舊頁面的檔案大小警告寫錯了引數。
- **[圖表](/docs/diagnostics-monitoring-and-troubleshooting/graphing)**：已重寫，包含針對介面和資源圖表、按客戶的佇列圖表以及 PPPoE 使用者的任務，並使用一臺 PC、第二臺路由器和一次 PPPoE 會話進行了測試。新增：圖表無需登入、誰可以檢視哪個圖表、allow-target 如何公開以子網或介面為目標的佇列（包括每個動態 PPP 佇列）、如何對客戶隱藏 WebFig、In 和 Out 對介面和佇列分別意味著什麼，以及 store-on-disk 在重啟後會保留什麼。移除：圖表的 WebFig 選單項，該選單項已不存在。

## 開發者指南 {#developer-guides}

- **[REST API](/docs/developer-guides/rest-api)**：路由器到路由器的 /tool/fetch 示例現在會指出當呼叫方路由器尚未匯入 CA 證書時顯示的錯誤（no trusted CA certificate found）。

## CLI 參考 {#cli-reference}

- **[/system/clock](/docs/cli-reference/system/clock)、[/system/clock/manual](/docs/cli-reference/system/clock/manual)**：所有描述均已更正：啟動時以及重新啟用時的自動檢測、日期限制、get gmt-offset 返回秒數，以及 dst-start 和 dst-end 中省略部分的重設方式。
- **[/tool/fetch](/docs/cli-reference/tool/fetch)**：全部 35 行均已根據 fetch 傳送的請求進行了檢查：

- header-field 語法，以及 POST 資料的預設內容型別。
- 基本認證，以及 FTP 的匿名登入。
- 壓縮、每種模式的預設埠，以及預設檔名。
- check-certificate 的值和錯誤。
- 結果限制，以及已下載大小和總大小的 KiB 舍入。

- **[/ip/tftp](/docs/cli-reference/ip/tftp)、[/ip/tftp/settings](/docs/cli-reference/ip/tftp/settings)**：所有行均根據實驗室測試進行了描述，包括 req-filename 如何匹配、real-filename 提供什麼、read-only 預設值、超過 65535 個塊後的迴繞，以及可接受的塊大小。
- **[/tool/sniffer](/docs/cli-reference/tool/sniffer)**：描述了全部九個選單（settings、start、stop、save、quick，以及 packet、protocol、host 和 connection 檢視）。IP 和 MAC 協定列表再次完整，其中的 EtherType 編號是從路由器讀回的。
- **[/tool/graphing](/docs/cli-reference/tool/graphing)**：設定以及介面、佇列和資源規則均已完整描述，包括預設值、訪問規則以及每個圖表的 In/Out 方向。
