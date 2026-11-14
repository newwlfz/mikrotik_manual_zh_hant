---
sidebar_key: "routing-and-networking-protocols/unicast/rip"
sidebar_position: 6
title: "RIP"
sidebar_label: "RIP"
description: "MikroTik RouterOS 支援 RIP 版本 2，用於在自治系統內交換路由資訊，並基於跳數選擇最優路徑。可在 `/routing/rip` 下進行配置。"
tags:
  - 'routing'
  - 'rip'
slug: /user-guides/routing-and-networking-protocols/unicast/rip
source: https://manual.mikrotik.com/docs/7.25/user-guides/routing-and-networking-protocols/unicast/rip
captured_at: '2026-11-04T11:22:55+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

MikroTik RouterOS 實現了 RIP 版本 2（RFC 2453）。不支援版本 1（RFC 1058）。

RIP 使自治系統中的路由器能夠交換路由資訊。它始終使用可用的最佳路徑（即跳數（也就是路由器數量）最少的路徑）。配置位於 [`/routing/rip`](../../../cli-reference/routing/rip/instance.md) 下。
