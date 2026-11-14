---
sidebar_key: "network-management/proxy/index"
sidebar_position: 2
title: "代理"
sidebar_label: "代理"
description: "RouterOS 有兩種 Web 代理：Web 代理會轉發、過濾並快取網路中用戶端的 Web 請求，而反向代理則使路由器後方的 Web 伺服器能夠透過主機名經 HTTPS 訪問。"
tags:
  - 'proxy'
  - 'reverse-proxy'
source: https://manual.mikrotik.com/docs/7.25/network-management/proxy
captured_at: '2026-11-04T11:21:09+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

代理接受來自用戶端的請求，並代表用戶端連線到伺服器。RouterOS 有兩種用於 Web 流量的代理，它們的工作方向相反：

| 代理 | 選單 | 用戶端 | 伺服器 | 用途 |
| :-- | :-- | :-- | :-- | :-- |
| [Web 代理](./web-proxy.md) | `/ip/proxy` | 位於你的網路中 | 位於網際網路上 | 過濾並快取使用者的 Web 請求，或將其轉發到另一個代理。 |
| [反向代理](./reverse-proxy.md) | `/ip/reverse-proxy` | 位於網際網路上 | 位於路由器後方 | 使路由器後方的 Web 伺服器可透過主機名以 HTTPS 訪問。 |

對於 Web 瀏覽器以外的應用程式，RouterOS 還在 `/ip/socks` 中提供了 [SOCKS 代理](../socks/index.md)。
