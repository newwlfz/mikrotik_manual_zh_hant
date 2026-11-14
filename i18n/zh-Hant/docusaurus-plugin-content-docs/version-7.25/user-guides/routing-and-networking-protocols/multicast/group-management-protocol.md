---
sidebar_key: "routing-and-networking-protocols/multicast/group-management-protocol"
sidebar_position: 1
title: "組管理協定"
sidebar_label: "組管理協定"
description: "組管理協定使介面能夠在沒有專用用戶端的情況下接收組播流，支援 IGMP 和 MLD 協定。它允許透過傳送成員報告和響應查詢來測試組播路由，並在停用時自動清理。"
tags:
  - 'igmp'
  - 'mld'
  - 'multicast'
slug: /user-guides/routing-and-networking-protocols/multicast/group-management-protocol
source: https://manual.mikrotik.com/docs/7.25/user-guides/routing-and-networking-protocols/multicast/group-management-protocol
captured_at: '2026-11-04T11:22:27+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Group Management Protocol 允許任意介面成為組播流的接收者。它允許在不使用專用 IGMP 或 MLD 用戶端的情況下測試組播路由和交換配置。該選項自 RouterOS v7.4 起可用，支援 IGMP v1、v2、v3 和 MLD v1、v2 協定。

預設情況下，介面使用 IGMP v3 和 MLD v2。如果收到 IGMP v1、v2 或 MLD v1 查詢，介面將回退到相應版本。在介面上建立 Group Management Protocol 後，它會發送未經請求的成員報告（加入）封包，並響應查詢訊息。如果配置被刪除或停用，介面將傳送離開訊息。

## 示例 {#examples}

---

此示例展示如何在介面上配置一個簡單的組播監聽器。

首先，在介面上新增 IP 地址：

```ros
/ip/address
add address=192.168.10.10/24 interface=ether1 network=192.168.10.0
```

然後在同一介面上配置 Group Management Protocol：

```ros
/routing/gmp
add groups=229.1.1.1 interfaces=ether1
```

現在可以檢查你的組播網路，檢視路由器或交換器是否已建立適當的組播轉發條目，以及介面上是否正在接收組播資料（參見介面統計資訊，或使用 [封包嗅探器](../../../diagnostics-monitoring-and-troubleshooting/packet-sniffer.md) 和 [Torch](../../../diagnostics-monitoring-and-troubleshooting/torch.md)）。
