---
sidebar_key: "routing-and-networking-protocols/mpls/traffic-eng"
sidebar_position: 3
title: "流量工程"
sidebar_label: "流量工程"
description: "本頁面介紹 MikroTik RouterOS 流量工程（TE）隧道功能，涵蓋用於跟蹤 TE 隧道狀態和路徑的 `monitor` 等監控命令，以及使用 `/interface/traffic-eng/reoptimize` 根據網路變化調整 LSP 的重新最佳化技術。"
tags:
  - 'traffic-eng'
  - 'reoptimization'
  - 'explicit-route'
slug: /user-guides/routing-and-networking-protocols/mpls/traffic-eng
source: https://manual.mikrotik.com/docs/7.25/user-guides/routing-and-networking-protocols/mpls/traffic-eng
captured_at: '2026-11-04T11:22:25+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

### 監控 {#monitoring}

要驗證 TE 隧道的狀態，可以使用 **`monitor`** 命令。

```ros
/interface/traffic-eng/monitor 0 
tunnel-id: 12 
primary-path-state: on-hold 
secondary-path-state: established 
secondary-path: static 
active-path: static 
active-lspid: 3 
active-label: 66 
explicit-route: "S:192.168.55.10/32,L:192.168.55.13/32,L:192.168.55.17/32" 
recorded-route: "192.168.55.13[66],192.168.55.17[59],192.168.55.18[3]" 
reserved-bandwidth: 5.0Mbps
```

### 重新最佳化 {#reoptimization}

可以透過輸入命令 `/interface/traffic-eng/reoptimize [id]`（其中 [id] 是專案編號或介面名稱）手動重新最佳化路徑。它允許網路管理員根據頻寬、流量、管理策略或其他因素的變化，重新最佳化已建立的 LSP。

假設某條 TE 隧道在最佳路徑發生鏈路故障後選擇了另一條路徑。如果啟用了 `record-route` 引數，你可以透過檢視 **`explicit-route`** 或 **`recorded-route`** 的值來驗證最佳化情況。

```ros
/interface/traffic-eng/monitor 0 
tunnel-id: 12 
primary-path-state: established 
primary-path: dyn 
secondary-path-state: not-necessary 
active-path: dyn
active-lspid: 1
active-label: 67 
explicit-route: "S:192.168.55.10/32,S:192.168.55.13/32,S:192.168.55.14/32, 
S:192.168.55.17/32,S:192.168.55.18/32" 
recorded-route: "192.168.55.13[67],192.168.55.17[60],192.168.55.18[3]" 
reserved-bandwidth: 5.0Mbps
```

每當鏈路恢復時，TE 隧道將使用相同的路徑，即使它不是最佳路徑（除非配置了 `reoptimize-interval`）。要解決此問題，我們可以手動重新最佳化隧道路徑。

```ros
/interface/traffic-eng/reoptimize 0
```

```ros
/interface/traffic-eng/monitor 0 
tunnel-id: 12 
primary-path-state: established 
primary-path: dyn 
secondary-path-state: not-necessary 
active-path: dyn
active-lspid: 2
active-label: 81 
explicit-route: "S:192.168.55.5/32,S:192.168.55.2/32,S:192.168.55.1/32" 
recorded-route: "192.168.55.2[81],192.168.55.1[3]" 
reserved-bandwidth: 5.0Mbps
```

請注意 explicit-route 和 recorded-route 是如何變為更短路徑的。
