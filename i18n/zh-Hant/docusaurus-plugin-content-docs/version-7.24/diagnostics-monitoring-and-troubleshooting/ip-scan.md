---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/ip-scan"
sidebar_position: 16
title: "IP 掃描"
sidebar_label: "IP 掃描"
description: "RouterOS 中的 IP Scan 工具會掃描網路以查詢活動裝置，收集 IP 地址、MAC 地址、響應時間、DNS 名稱、SNMP 字串和 NET-BIOS 名稱。它可以按 IPv4 字首或介面監聽進行掃描，並帶有針對衝突設定的警告。"
tags:
  - 'ip'
  - 'arp'
  - 'scanning'
source: https://manual.mikrotik.com/docs/7.24/diagnostics-monitoring-and-troubleshooting/ip-scan
captured_at: '2026-11-04T11:27:56+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

IP 掃描工具允許使用者基於某個網路字首或透過設定要監聽的介面來掃描網路。無論採用哪種方式，該工具都會從網路中收集特定資料：

- address - 網路裝置的 IP 地址。
- mac-address - 網路裝置的 MAC 地址。
- time - 發現網路裝置時的響應時間。
- DNS - 網路裝置的 DNS 名稱。
- SNMP - 裝置的 SNMP 名稱。
- NET-BIOS  - 裝置通告的 NET-BIOS 名稱（如果裝置通告了該名稱）。

使用 IP 掃描工具時，使用者必須選擇要掃描的內容：

- 特定的 IPv4 字首 - 該工具將嘗試掃描所有 IP 地址或已設定的地址。
- 路由器的介面 - 該工具將嘗試監聽“經過”的封包，並在有所發現時嘗試彙總結果。

:::danger
可以同時設定兩者，但此時結果可能不確定！
:::

## 快速示例 {#quick-example}

`/tool/ip-scan` 實用程式是使用者發現特定 IP 範圍內活動主機的重要診斷工具。它在識別未授權裝置、驗證 IP 地址分配或在缺少文件時梳理網段方面尤為有用。透過傳送 ICMP 和 ARP 請求，它可以即時概覽可達地址、其關聯的 MAC 地址，甚至相容裝置的 SNMP 身份字串。

該工具常用於初始站點審計，或在動態 DHCP 環境中排查連線問題時使用。透過對本地子網執行掃描，你可以快速將物理硬體與邏輯 IP 地址關聯起來，以檢測 IP 衝突或流氓接入點。這種可見性對於維護網路完整性、確保所有已連線基礎設施符合預期部署拓撲至關重要。

在以下示例中，我們將掃描 10.155.126.0/24 網路上的裝置：

```ros
[admin@MikroTik] > /tool/ip-scan address-range=10.155.126.1-10.155.126.255
Columns: ADDRESS, MAC-ADDRESS, TIMe, SNMP
  ADDRESS         MAC-ADDRESS        TIM  SNMP     
  10.155.126.1    E4:8D:8C:1C:D3:18  2ms  CCR1036-8G-2S+
  10.155.126.251                     2ms           
  10.155.126.151  E4:8D:8C:49:49:DB  1ms           
  10.155.126.153  6C:3B:6B:48:0E:8B  1ms  750Gr3         
  10.155.126.249  CC:2D:E0:8D:01:88  0ms  CRS328-24P-4S+   
  10.155.126.250  B8:69:F4:B3:1B:D2  0ms           
  10.155.126.252  6C:3B:6B:ED:83:69  0ms           
  10.155.126.253  6C:3B:6B:ED:81:83  0ms
```
