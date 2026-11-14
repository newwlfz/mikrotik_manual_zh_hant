---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/traceroute"
sidebar_position: 2
title: "跟蹤路由"
sidebar_label: "跟蹤路由"
description: "Traceroute 透過分析 TTL 值和 ICMP 的“Time Exceeded”訊息，顯示封包到達遠端主機所經過的路徑，有助於識別多跳網路中的路由問題或瓶頸。"
tags:
  - 'traceroute'
source: https://manual.mikrotik.com/docs/7.24/diagnostics-monitoring-and-troubleshooting/traceroute
captured_at: '2026-11-04T11:28:05+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

**子選單：** `/tool/traceroute`

**Traceroute** 顯示封包到達遠端主機所經過的路由器列表。**traceroute** 或 **tracepath** 工具幾乎可在所有類 Unix 作業系統上使用，而在 Microsoft Windows 作業系統上則提供 **tracert**。

Traceroute 的執行基於 TTL 值和 ICMP “Time Exceeded” 訊息。請記住，IP 頭中的 TTL 值用於避免路由環路。每一跳都會將 TTL 值減 1。如果 TTL 達到零，封包會被丟棄，並在此時向傳送方返回一條 ICMP Time Exceeded 訊息。

最初，透過 traceroute，TTL 值設定為 1；當下一個路由器發現 TTL = 1 的封包時，會將 TTL 值設定為零，並向源返回一條 ICMP "time exceeded" 訊息。此訊息讓源知道該封包將那個特定路由器作為一跳經過。下一次 TTL 值增加 1，依此類推。通常，通往目的地的路徑上的每個路由器都會將 TTL 欄位遞減一個單位，直到 TTL 達到零。

使用此命令，你可以檢視封包如何在網路中傳輸，以及可能在何處失敗或變慢。利用此資訊，你可以確定可能造成網路問題或故障的計算機、路由器、交換器或其他網路裝置。

## 快速示例 {#quick-example}

透過跟蹤到遠端目的地的路由，你可以確定連線問題是位於本地網路內、ISP 閘道器處，還是更上游的位置。

```ros
[admin@MikroTik] > tool traceroute 10.255.255.1
     ADDRESS                                    STATUS
   1       10.0.1.17 2ms 1ms 1ms 
   2    10.255.255.1 5ms 1ms 1ms
```

在此場景中，輸出確認了經本地閘道器 `10.0.1.17` 到目標主機 `10.255.255.1` 的成功路徑。在排查多跳 VPN 隧道或複雜路由表（其中流量可能從意外的出介面發出）時，此工具特別有用。監控每一跳的毫秒級響應時間有助於精確定位網路基礎設施中的具體瓶頸或抖動。
