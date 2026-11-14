---
sidebar_key: "routing-and-networking-protocols/unicast/rpki"
sidebar_position: 7
title: "RPKI"
sidebar_label: "RPKI"
description: "RouterOS 支援使用 Resource Public Key Infrastructure 透過 RPKI 進行 BGP 字首驗證，並透過 RTR 協定實現安全的路由源驗證。配置包括設定 RTR 伺服器，以及根據 RPKI 有效性狀態應用過濾器來接受或拒絕路由。"
tags:
  - 'rpki'
  - 'bgp'
slug: /user-guides/routing-and-networking-protocols/unicast/rpki
source: https://manual.mikrotik.com/docs/7.24/user-guides/routing-and-networking-protocols/unicast/rpki
captured_at: '2026-11-04T11:34:17+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

RouterOS 實現了 [`RFC 8210`](https://tools.ietf.org/html/rfc8210) 中定義的 Resource Public Key Infrastructure (RPKI) to Router Protocol。RTR 是一種輕量級、低記憶體佔用的協定，用於從 RPKI 驗證器獲取字首驗證資料。可在 [RIPE 部落格](https://blog.apnic.net/2019/10/28/how-to-installing-an-rpki-validator/) 上檢視驗證器設定示例。

配置位於 [`/routing/rpki`](./rpki.md) 下。

## 基本示例 {#basic-example}

假設你的網路在 IP 地址 `192.168.1.1` 上有一個 RTR 伺服器：

```ros
/routing/rpki
add group=myRpkiGroup address=192.168.1.1 port=8282 refresh-interval=20
```

[`group`](./rpki.md#group)、[`address`](./rpki.md#address)、[`port`](./rpki.md#port) 和 [`refresh-interval`](./rpki.md#refresh-interval) 引數用於配置 RTR 連線。其他引數包括 [`vrf`](./rpki.md#vrf)、[`preference`](./rpki.md#preference)、[`retry-interval`](./rpki.md#retry-interval) 和 [`expire-interval`](./rpki.md#expire-interval)。

連線建立並收到驗證器資料庫後，使用 [`rpki-check`](../../../cli-reference/routing/rpki/rpki-check.md) 檢查字首有效性：

```text
[admin@rack1_b33_CCR1036] /routing/rpki> rpki-check group=myRpkiGroup prfx=70.132.18.0/24 origin-as=16509
    valid
```

在[路由過濾器](../route-selection-and-filtering.md)中使用快取的資料庫，根據 RPKI 有效性接受或拒絕字首。首先設定一個 [`/routing/filter/rule`](../../../cli-reference/routing/filter/rule.md)，用於定義哪個 RPKI 組執行驗證。之後，過濾器可以匹配 RPKI 資料庫中的狀態。狀態可以是以下四個值之一：

- **valid** - 資料庫中有記錄且源 AS 有效。
- **invalid** - 資料庫中有記錄且源 AS 無效。
- **unknown** - 資料庫中沒有關於該字首和源 AS 的資訊。
- **unverified** - 當該 RPKI 組的任何會話都未同步資料庫時設定。使用此值來處理 RPKI 完全故障。

```ros
/routing/filter/rule
add chain=bgp_in rule="rpki-verify myRpkiGroup"
add chain=bgp_in rule="if (rpki invalid) { reject } else { accept }"
```
