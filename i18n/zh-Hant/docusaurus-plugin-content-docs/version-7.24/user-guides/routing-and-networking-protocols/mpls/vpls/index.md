---
sidebar_key: "routing-and-networking-protocols/mpls/vpls/index"
sidebar_position: 3
title: "VPLS"
sidebar_label: "VPLS"
description: "VPLS 頁面介紹 MikroTik RouterOS 的虛擬專用區域網路服務（VPLS）介面，詳細說明其作為使用 LDP 或 MP-BGP 協定的透明乙太網隧道的用途。它涵蓋 VPLS 功能，如偽線信令、分片和基於 BGP 的自動發現，以及 MPLS 標籤分發的前提條件和 i"
tags:
  - 'vpls'
  - 'ldp'
  - 'bgp'
slug: /user-guides/routing-and-networking-protocols/mpls/vpls/
source: https://manual.mikrotik.com/docs/7.24/user-guides/routing-and-networking-protocols/mpls/vpls
captured_at: '2026-11-04T11:33:52+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

虛擬專用區域網路服務 (VPLS) 介面可以像 [EoIP](../../../../virtual-private-networks/eoip.md) 介面一樣被視為隧道介面，以在客戶站點之間實現透明乙太網段轉發。

VPLS 隧道的協商可以透過 LDP 協定或 MP-BGP 完成——隧道兩端交換它們將用於隧道的標籤。

隧道中的資料轉發透過在封包上壓入 2 個標籤來實現：隧道標籤和傳輸標籤——確保流量送達隧道另一端的標籤。

MikroTik RouterOS 實現以下 VPLS 功能：

- VPLS LDP 信令 (RFC 4762)。
- Cisco 風格的靜態 VPLS 偽線 (RFC 4447 FEC 型別 0x80)。
- VPLS 偽線分片和重組 (RFC 4623)。
- 基於 VPLS MP-BGP 的自動發現和信令 (RFC 4761)。
- Cisco VPLS 基於 BGP 的自動發現 (draft-ietf-l2vpn-signaling-08)。
- 支援用於基於 BGP 的 VPLS 的多個匯入/匯出路由目標擴展團體（RFC 4761 和 draft-ietf-l2vpn-signaling-08 均支援）。

## VPLS 先決條件 {#vpls-prerequisites}

為了使 VPLS 能夠傳輸 MPLS 封包，骨幹網上應已執行一種標籤分發協定；它可以是 LDP、RSVP-TE 或靜態繫結。

在繼續之前，請熟悉 [LDP 所需的先決條件](../ldp.md#prerequisites-for-mpls) 和 RSVP-TE 的先決條件。

如果應將 BGP 用作 VPLS 發現和信令協定，則骨幹網應執行 iBGP，最好使用路由反射器。

## 示例設定 {#example-setup}

假設我們已經有一個來自 [LDP 配置示例](../ldp.md#example-setup) 的可正常工作的 LDP 設定。

路由器 R1、R3 和 R4 連線到客戶 A 站點，路由器 R1 和 R3 連線到客戶 B 站點。客戶需要站點之間的透明 L2 連線。
