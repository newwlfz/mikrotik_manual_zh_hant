---
title: "文件更新 - 2026年10月5日"
date: 2026-10-05
slug: /changelog-2026-10-05
source: https://manual.mikrotik.com/changelog/changelog-2026-10-05
captured_at: '2026-11-04T06:08:58+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026年10月5日文件變更摘要。

## 站點 {#site}

- **文件版本控制**：RouterOS 7.25 的文件已凍結為 **7.25** 版本，並可從版本下拉選單中選擇。當前文件現在描述 RouterOS 7.26。

## 管理工具 {#management-tools}

- **[CMR](/docs/management-tools/cmr)**：CMR 的新指南，cmr 軟體包中用於監控和管理 RouterOS 裝置群的伺服器，從 RouterOS 7.26beta1 開始提供。內容包括：

- CMR 能做和不能做什麼、伺服器與其用戶端如何連線，以及新使用者從哪裡開始。
- 啟用伺服器及其設定，以及配對裝置，包括典型場景和雙方對密碼與確認的要求。
- 管理裝置：裝置屬性、標籤和標籤選擇語法（+ 表示 AND，- 表示 AND NOT），以及在多臺裝置上同時執行命令。
- 即時儀表板 (/cmr/device/dashboard)，包含一張截圖及其八個部分的說明。
- 裝置群升級：升級規則、使用 trigger、run-next 或 device/upgrade 提前啟動升級、升級源和本地 packages-directory、任務狀態和結果（沒有可用升級的裝置會被視為升級失敗），以及 strategy 和 fail-policy 設定。
- 告警規則：條件、日誌、指令碼和 webhook 動作，device、event 和 alert 組中動作文字的佔位符，以及規則如何觸發。
- 網路拓撲：佈局、節點和鏈路，add-devices 和 rebuild-links，附帶一個已驗證的示例和一張截圖。
- 應用流量、集中式 WiFi 配置（網路、射頻、設定如何應用、網橋和 VLAN 行為），以及 VLAN 配置下發，包含一個已驗證的示例和導致控制器被鎖定的風險。

- **[CMR-Client](/docs/management-tools/cmr/client)**：裝置端的新頁面，屬於主 RouterOS 軟體包：使用 controller-addresses 啟用用戶端，從用戶端進行配對及其自身的 pairing-requirement（none、password 或 confirm），斷開連線，以及故障排除。

## CLI 參考 {#cli-reference}

- **[/cmr](/docs/cli-reference/cmr)**、**[/cmr/client](/docs/cli-reference/cmr/client)**：CMR 伺服器和用戶端的新參考，描述了每個引數：告警規則（alert、show-devices、test）、裝置（apptraffic、dashboard、pair、reboot、run-script、upgrade、wifi-logs）、拓撲（layout、node、link、add-devices、rebuild-links）、升級（upgrade、job、run-next、show-devices、trigger、version-check），以及 vlan 和 wifi 配置下發選單。
- **[/interface/ethernet/pon](/docs/cli-reference/interface/ethernet/pon)**、**[/interface/wifi/dashboard](/docs/cli-reference/lcd/show)**、**[/system/dashboard](/docs/cli-reference/lcd/show)**、**[/tool/apptraffic](/docs/cli-reference/tool/apptraffic)**：為 RouterOS 7.26beta1 重新生成了參考。新增命令：帶有 ONU 標識的 PON 設定（onu-model、onu-registration-id、onu-serial-number、onu-vendor-id，也出現在 [/interface/ethernet](/docs/cli-reference/interface/ethernet) 上）、WiFi 和系統儀表板、應用流量統計、[/interface/wireless/snooper/snoop](/docs/cli-reference/interface/wireless/snooper/snoop)，以及用於交換器規則的 reset-counters-all。新增引數：[網橋](/docs/cli-reference/interface/bridge) 上的 dhcp-snooping-vlan-ids、[埠隔離](/docs/cli-reference/interface/ethernet/switch/port-isolation) 中的 current-forwarding-override，以及 [LTE 介面](/docs/cli-reference/interface/lte) 上的 apn-profile。在 [/interface/vlan](/docs/cli-reference/interface/vlan) 上，force-mac-address 現在為 forced-mac-address，並且 Ethernet 和 [power-line](/docs/cli-reference/interface/pwr-line) 介面中的 bandwidth 已被移除。
- **[/interface/wifi/configuration](/docs/cli-reference/interface/wifi/configuration)**、**[/interface/wifi/network](/docs/cli-reference/interface/wifi/network)**、**[/caps-man/configuration](/docs/cli-reference/caps-man/configuration)**：來自子選單的設定現在會連同其字首一起列出，與在命令列中設定時相同，例如 security.authentication-types。WiFi 使用 aaa.、channel.、datapath.、interworking.、security. 和 steering.；舊版 CAPsMAN 使用 channel.、configuration.、datapath.、rates. 和 security.。
- **[CLI 參考](/docs/cli-reference)**：地址引數標誌說明了 i（用裸介面名代替地址，例如將點對點介面用作路由閘道器）和新的 % 標誌（地址上的介面字尾，例如 fe80::1%ether1）。每個接受 IPv6 地址的引數也接受帶有其 %interface 字尾的鏈路本地地址。

## 入門 {#getting-started}

- **[軟體包](/docs/getting-started/installation-and-upgrade/packages)**：新增了 cmr 軟體包，支援 arm、arm64 和 x86 架構，並提供了指向 CMR 指南的連結。

## 無線 {#wireless}

- **[WiFi](/docs/wireless/wifi)**：wifi-qcom-ac 驅動程式不支援 ft-preserve-vlanid 引數。
- **[Wi-Fi 5 (802.11ac)](/docs/wireless/wifi-ac)**：新增警告：wifi-qcom-ac 驅動程式適用於室內裝置。它可以安裝在室外型號（LDF 5 ac、LHG XL 5 ac、LHG XL 52 ac、NetMetal ac²、mANTBox 52 15s、SXTsq 5 ac）上，但不支援超過 2 km 的鏈路所需的 distance 設定，因此請在室外板卡上使用 wireless 驅動程式。
