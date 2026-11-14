---
sidebar_key: "user-guides/routing-and-networking-protocols/unicast/ospf/faq"
sidebar_position: 5
title: "常見問題"
sidebar_label: "常見問題"
description: "常見問題。"
tags:
  - 'routing'
  - 'ospf'
source: https://manual.mikrotik.com/docs/user-guides/routing-and-networking-protocols/unicast/ospf/faq
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 鄰居卡在 Init 狀態或頻繁振盪 {#neighbors-stuck-in-init-state-or-frequently-flapping}

最常見的配置錯誤原因：

- [`router-id`](../../../../cli-reference/routing/ospf/instance.md#router-id) 不唯一。
- 防火牆阻止了 OSPF 協定或 OSPF 使用的組播地址。
- 配置了 NAT，並且 NAT 正在修改 OSPF 封包。

最常見的網路問題：

- 鄰居透過會阻止或修改組播封包的 L2 裝置連線。
- 鄰居透過無線鏈路連線，而無線鏈路無法可靠地傳遞組播封包。
這兩種情況的解決方案都是配置 NBMA。
