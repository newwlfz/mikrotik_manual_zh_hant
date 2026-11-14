---
sidebar_key: "routing-and-networking-protocols/unicast/bgp/faq"
sidebar_position: 5
title: "常見問題"
sidebar_label: "常見問題"
description: "常見問題。"
tags:
  - 'routing'
  - 'bgp'
slug: /user-guides/routing-and-networking-protocols/unicast/bgp/faq
source: https://manual.mikrotik.com/docs/7.25/user-guides/routing-and-networking-protocols/unicast/bgp/faq
captured_at: '2026-11-04T11:22:41+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 為什麼 eBGP 無法連線到環回地址？ {#why-ebgp-does-not-connect-to-loopback-address}

eBGP 預設只能建立一跳範圍內的連線。環回地址會再多一跳，因為它是透過直連網路路由的。對於多跳會話，請設定 [`multihop`](../../../../cli-reference/routing/bgp/connection.md#multihop)`=yes`。

## BGP 網路同步到底是什麼意思？ {#what-does-bgp-network-synchronization-exactly-mean}

除非路由表中存在匹配的活動 IGP 或直連路由（字首完全匹配），否則 BGP 不會通告該網路。同步的主要原因是避免路由環路。如果 IGP 不可靠，或者必須始終通告該網路，那麼可以為每個要通告的網路字首新增靜態 blackhole 路由，或者在 [`/routing/bgp/connection`](../../../../cli-reference/routing/bgp/connection.md#output.network) 配置中設定 [`output.network-blackhole=yes`](../../../../cli-reference/routing/bgp/connection.md)，以便為每個 BGP 網路自動新增活動的 blackhole 路由。

## 如何隱藏我自己的 AS？ {#how-to-hide-my-own-as}

如果 [`/routing/bgp/connection`](../../../../cli-reference/routing/bgp/connection.md#output.default-prepend) 配置中的 [`output.default-prepend`](../../../../cli-reference/routing/bgp/connection.md) 設定為 0，或者在輸出[路由過濾器](../../../../cli-reference/routing/filter/rule.md)中將 `bgp-path-prepend` 設定為 0，則對端自己的 AS 會從 **AS_PATH** 中移除。

## 遠端對端多次前置其 AS。如何覆蓋該前置操作？ {#remote-peer-prepends-its-as-several-times-how-to-override-the-prepend}

在 BGP 輸入[路由過濾器](../../../../cli-reference/routing/filter/rule.md)中設定 `bgp-path-peer-prepend 1`，即可移除遠端對端的前置操作。

## BGP 不選擇 AS 路徑最短的路由，或其他度量被忽略 {#bgp-does-not-pick-route-with-shortest-as-path-or-other-metrics-are-ignored}

BGP 最佳路徑選擇僅對由同一 [BGP 例項](../../../../cli-reference/routing/bgp/instance.md) 接收的路由生效。

## 從某個對端接收的 BGP 路由未通告給另一個對端 {#bgp-routes-received-from-one-peer-are-not-advertised-to-another-peer}

最常見的配置錯誤：

- 輸出[過濾器](../../../../cli-reference/routing/filter/rule.md)阻止了重分發。
- 兩個對端未執行在同一個 [BGP 例項](../../../../cli-reference/routing/bgp/instance.md) 上。
