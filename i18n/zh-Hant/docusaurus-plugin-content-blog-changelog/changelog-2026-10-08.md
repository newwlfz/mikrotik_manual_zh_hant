---
title: "文件更新 - 2026年10月8日"
date: 2026-10-08
slug: /changelog-2026-10-08
source: https://manual.mikrotik.com/changelog/changelog-2026-10-08
captured_at: '2026-11-04T06:08:59+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026 年 10 月 8 日文件變更摘要。

## 儲存 {#storage}

- **[Btrfs RAID](/docs/storage/btrfs/raid)**：新增“擴充套件 Btrfs-RAID”指南。使用 add-device 新增成員時，每塊磁碟都按其完整容量登記，但在 balance-start 轉換配置檔之前不會移動任何資料（兩塊盤的 RAID1 會變成四塊盤的 RAID10，可用容量翻倍）。

## 管理工具 {#management-tools}

- **[CMR](/docs/management-tools/cmr)**：澄清了配對方式：每條 pair 命令都使用另一臺裝置的使用者名稱和密碼——伺服器的 [/cmr/device/pair](/docs/cli-reference/cmr/device/pair) 使用用戶端的使用者，用戶端的 [/cmr/client/pair](/docs/cli-reference/cmr/client/pair) 使用伺服器的使用者。配對通常可以在一個控制檯上完成；只有 confirm 會強制在伺服器控制檯上執行操作。新增示例按各裝置自帶的初始密碼來配對：在每臺裝置上各執行一次 /cmr/device/pair username=admin password=&lt;來自該裝置的密碼&gt;，並使用 labels 而不是 all 來把一次執行限制在部分裝置上。

## 無線 {#wireless}

- **[Wi-Fi](/docs/wireless/wifi)**：該頁面現在在 Wi-Fi 6/7 之外也涵蓋 Wi-Fi HaLow（802.11ah）介面。Network 部分說明了 provisioning：labels 預設為 all，每個 radio 會自動獲得諸如 2ghz、5ghz 和 6ghz 以及其 MAC 地址的標籤，- 用於否定某個標籤，extra-labels 則分配更多標籤。新增“轉換為網路管理的 Wi-Fi / 從網路管理的 Wi-Fi 轉換”部分：RouterOS 選擇配置時所遵循的順序（static entry、provisioning、network、disabled stub），以及如何使用 provision 和 /interface/wifi/liberate 進行轉換。Radio capabilities 現在記錄了每個 hw-caps 值（channel-switch、hw-protection-mode、qos-classifier-dscp、sniffer、spectral），新增的“Radio settings”部分涵蓋 /interface/wifi/radio/settings（default-country、external-antenna、wifi-band）。
- **[Wi-Fi](/docs/wireless/wifi)**：同一輪修改中的更正：警告已移至其所屬的引數（加密演算法、802.11r 漫遊），澄清了 distance 和 vlan-id 的說明（HaLow 與 wifi-qcom-ac 不會解除安裝 VLAN），並修復了 spectral scan/history 與 WPS 用戶端示例。
