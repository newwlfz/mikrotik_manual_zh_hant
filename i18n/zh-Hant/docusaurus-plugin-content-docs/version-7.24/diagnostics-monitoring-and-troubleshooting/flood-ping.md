---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/flood-ping"
sidebar_position: 7
title: "泛洪 Ping"
sidebar_label: "泛洪 Ping"
description: "RouterOS 中的 Flood Ping 工具會持續傳送 ICMP 回顯請求，用於測試網路穩定性、測量丟包情況，並在高流量條件下分析延遲，同時即時統計已傳送/已接收的封包和往返時間。"
tags:
  - 'icmp'
  - 'ipv6'
source: https://manual.mikrotik.com/docs/7.24/diagnostics-monitoring-and-troubleshooting/flood-ping
captured_at: '2026-11-04T11:27:55+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Flood Ping 工具是 RouterOS 中的一款診斷實用程式，旨在以儘可能高的速率向目標主機發送連續的 ICMP 回顯請求流。它主要用於對網路穩定性進行壓力測試，並衡量高流量條件下的丟包或延遲。

## 快速示例 {#quick-example}

要執行基本的負載測試或驗證鏈路穩定性，可以執行 flood-ping 向目標生成高頻 ICMP 流量。該工具提供有關丟包和往返時間 (RTT) 的即時統計資訊，幫助識別潛在的網路瓶頸。使用 `count` 引數限制測試持續時間，或省略該引數以使實用程式無限期執行，直到手動停止。

對 IPv4 目標執行大批次 ping 測試：

```ros
/tool/flood-ping address=10.155.114.1 count=1000
```

對 IPv6 目標執行 flood-ping，以驗證雙棧效能：

```ros
/tool/flood-ping address=2001:0db8::2 count=500
```

示例輸出：

```ros
[admin@MikroTik] > /tool/flood-ping address=10.155.114.1 count=1000
      sent: 1000
  received: 1000
   min-rtt:    0
   avg-rtt:    0
   max-rtt:    1

[admin@MikroTik] > /tool/flood-ping address=2001:0db8::2 count=500
      sent: 500
  received: 500
   min-rtt:   0
   avg-rtt:   0
   max-rtt:   3
```
