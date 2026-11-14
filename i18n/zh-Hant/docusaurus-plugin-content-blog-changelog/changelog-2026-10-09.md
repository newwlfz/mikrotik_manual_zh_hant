---
title: "文件更新 - 2026年10月9日"
date: 2026-10-09
slug: /changelog-2026-10-09
source: https://manual.mikrotik.com/changelog/changelog-2026-10-09
captured_at: '2026-11-04T06:09:01+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026 年 10 月 9 日的文件變更摘要。

## 診斷與監控 {#diagnostics--monitoring}

- **[Netwatch](/docs/diagnostics-monitoring-and-troubleshooting/netwatch)**：已重寫，並在 RouterOS 7.26beta1 上完成測試。每種探測型別（simple、ICMP、TCP-conn、HTTP-GET、HTTPS-GET、DNS）都有獨立章節，配有可執行的示例，並說明閾值如何決定判定結果——包括即使未設定閾值也有預設值，以及 early-success-detection 和 early-failure-detection 如何與 thr-loss-count 配合工作。Scripts 章節介紹了探測變數、內部 *sys 使用者以及允許的四種指令碼策略。
- **[鄰居發現](/docs/system-information-and-utilities/neighbor-discovery)**：已重寫。新增“選擇參與發現的介面”章節（discover-interface-list、mode=rx-only、主介面與從介面的行為），以及一個 LLDP-MED Network Policy 示例，該示例為 VoIP 電話埠配置帶標籤的語音 VLAN 和不帶標籤的 PC 資料。LLDP TLV、老化（aging）和 SNMP 行為在“技術細節”中說明。
- **[Profiler](/docs/diagnostics-monitoring-and-troubleshooting/profiler)**：已重寫。說明了 cpu=total、cpu=all 和單核檢視、duration 與 freeze-frame-interval、最初幾幀顯示的內容、“查詢繁忙程式”的操作步驟，以及完整分類表，包括系統行和未分類的回退項。
- **[Health](/docs/diagnostics-monitoring-and-troubleshooting/health)**：已擴充，新增完整的讀數表（名稱、單位、編號）、電壓與溫度詳情、電源狀態表、舊裝置說明、風扇控制行為（包括 PoE-out 負載表和手動風扇控制），以及監控選項：SNMP trap 和 OID、REST API 和一個郵件告警示例。
- **[Traffic Flow](/docs/diagnostics-monitoring-and-troubleshooting/traffic-flow)**：已重寫。涵蓋啟用該服務和選擇介面、封包取樣、匯出目標、流計數器監視器、IPFIX 欄位選擇、一個最小化的端到端示例，以及關於哪些流量會被計數的說明（僅 CPU 路由的流量，映象幀永遠不會到達 input 鏈）。
- **[Resource](/docs/diagnostics-monitoring-and-troubleshooting/resource)**：已重寫。包括即時監控、每核 CPU 明細、帶示例的中斷（IRQ）繫結、Receive Packet Steering 及其適用場景、PCI/USB/SCSI 硬體對映，以及 USB 裝置授權和電源復位。
- **[介面統計與 monitor-traffic](/docs/diagnostics-monitoring-and-troubleshooting/interface-stats-and-monitor-traffic)**：已重寫。解釋了 stats 和 stats-detail 計數器（包括 Fast Path 計數器、佇列丟包和鏈路斷開計數），以及 monitor-traffic 中即時每秒速率和配合 /tool/traffic-monitor 使用的指令碼觸發器。

## 管理工具 {#management-tools}

- **[RoMON](/docs/management-tools/romon)**：已重寫。涵蓋啟用、選擇參與埠（萬用字元預設條目、僅物理介面）、使用金鑰保護覆蓋網路——包括可直接透過 RoMON 本身執行的分步金鑰輪換——發現路由器、RoMON ping、透過 RoMON 使用 SSH 以及 WinBox 訪問。文中說明了 RB5009 交換晶片的限制，並在“技術細節”中給出 EtherType 和組播 MAC 詳情。

## 系統 {#system}

- **[精確時間協定](/docs/system-information-and-utilities/precision-time-protocol)**：已重寫。包括配置（profile 與埠、按 profile 的預設）、VLAN 埠上的 PTP（網橋 VLAN 表要求以及帶標籤幹線的替代方案）、IGMP snooping 靜態 MDB 條目、使用 /system/ptp/status 和 /system/ptp/monitor 進行同步監控，以及支援的裝置列表。

## 硬體 {#hardware}

- **[PoE](/docs/hardware/poe-out)**：由原來的 PoE-Out 頁面改造成一份通用 PoE 指南，同時涵蓋 PoE out（PSE）和 PoE in（PD）。新增 802.3af/at/bt 功率等級表、如何從裝置規格判斷其支援的被動 PoE、PoE in 配置與供電要求、兩個方向的示例、日誌與告警，以及故障排查。

## CLI 參考 {#cli-reference}

- **[/tool/netwatch](/docs/cli-reference/tool/netwatch)**、**[/tool/profile](/docs/cli-reference/tool/profile)**、**[/tool/romon](/docs/cli-reference/tool/romon)**、**[/tool/traffic-monitor](/docs/cli-reference/tool/traffic-monitor)**：補充並修正了引數說明：netwatch 探測預設值（包括 simple 探測的 60 秒間隔）、VRF 與鏈路本地主機語法，以及修正後的 early-detection 說明；profiler 檢視；RoMON 埠限制與金鑰；traffic-monitor 觸發器單位。
- **[/system/health](/docs/cli-reference/system/health)**、**[/system/ptp](/docs/cli-reference/system/ptp)**、**[/system/resource](/docs/cli-reference/system/resource)**、**[/ip/traffic-flow](/docs/cli-reference/ip/traffic-flow)**、**[/interface](/docs/cli-reference/interface)**、**[/interface/monitor-traffic](/docs/cli-reference/interface/monitor-traffic)**：為已重寫的頁面補充說明：health 讀數與風扇設定、PTP profile 預設與埠、resource 計數器與 IRQ/RPS、Traffic Flow 與 IPFIX 欄位，以及介面計數器和速率行。
