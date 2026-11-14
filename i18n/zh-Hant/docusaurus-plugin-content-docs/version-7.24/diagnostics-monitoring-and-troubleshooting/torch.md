---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/torch"
sidebar_position: 3
title: "Torch"
sidebar_label: "Torch"
description: "MikroTik Torch 是一種即時流量監控工具，可觀察流經介面的網路流量，從而能夠分析源/目的地址、埠、協定、MAC、VLAN ID 和 DSCP 值，以便進行故障排查。"
tags:
  - 'traffic-monitoring'
  - 'ipv6'
source: https://manual.mikrotik.com/docs/7.24/diagnostics-monitoring-and-troubleshooting/torch
captured_at: '2026-11-04T11:28:04+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

MikroTik Torch 是一個即時流量監控工具，用於觀察透過特定介面的流量。它是即時排查故障和分析網路負載的重要實用工具。

觀看我們[關於此功能的影片](https://youtu.be/45E2uwI3xhc)。

:::warning
Torch 捕獲的流量是在被防火牆過濾之前看到的。這意味著你會看到最終可能被防火牆規則丟棄的封包。
:::

```ros
/tool/torch interface=ether1 src-address=0.0.0.0/0 dst-address=0.0.0.0/0
```

你可以監控按以下方式分類的流量：

- 源地址和目的地址（IPv4 和 IPv6）。
- 埠和協定。
- MAC 協定和 MAC 地址。
- VLAN ID。
- DSCP。

### 使用示例 {#usage-example}

要監控來自特定子網的 `ether1` 上的 HTTP 和 HTTPS 流量（介面可以作為未命名引數）：

```ros
/tool/torch ether1 port=80,443 src-address=192.168.88.0/24
```

Torch 會顯示所選協定以及所選介面上每個條目的 TX/RX 資料速率。

:::warning
啟用了用戶端到用戶端轉發的無線用戶端之間的單播流量對 Torch 工具不可見。同樣，透過橋接上的硬體解除安裝處理的報文也不可見（不過未知單播、廣播和部分組播流量仍然可見）。
:::
