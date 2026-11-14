---
sidebar_key: "user-guides/routing-and-networking-protocols/unicast/rpki"
sidebar_position: 7
title: "RPKI"
sidebar_label: "RPKI"
description: "RouterOS 使用 RPKI 驗證 BGP 字首來源和 AS 路徑。它會為 ASPA 資料協商 RTR 協定版本 2,並對較舊的驗證器回退到版本 1。"
tags:
  - 'rpki'
  - 'bgp'
  - 'aspa'
source: https://manual.mikrotik.com/docs/user-guides/routing-and-networking-protocols/unicast/rpki
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

RouterOS 實現 [RFC 8210](https://tools.ietf.org/html/rfc8210) 中定義的資源公鑰基礎設施 (RPKI) 到路由器協定 (RTR)。它還支援 [draft-ietf-sidrops-8210bis](https://datatracker.ietf.org/doc/draft-ietf-sidrops-8210bis/) 中定義的 RTR 協定版本 2，該版本增加了 ASPA 資料。RTR 是一種輕量級、低記憶體的協定，用於從 RPKI 驗證器獲取字首源資料和自治系統提供方授權 (ASPA) 資料。請參閱 [RIPE 部落格](https://blog.apnic.net/2019/10/28/how-to-installing-an-rpki-validator/) 上的驗證器設定示例。

配置位於 [`/routing/rpki`](./rpki.md) 下。

## RTR 協定版本 2 {#rtr-protocol-version-2}

RouterOS 以協定版本 2 (RTRv2) 啟動 RTR 會話。如果驗證器僅支援版本 1，RouterOS 會以版本 1 重新連線。回退是自動進行的；沒有任何引數用於選擇協定版本。

會話同步後，協商後的版本會顯示在 `/routing/rpki/session` 選單的 [`version`](../../../cli-reference/routing/rpki/session.md#version) 欄位中：

```ros
/routing/rpki/session print detail
```

版本 2 會話可以接收 ASPA PDU。版本 1 會話僅提供字首源資料。要使用 ASPA 驗證 AS 路徑，請使用支援 RTR 協定版本 2 併發布 ASPA 物件的驗證器。

## 字首源驗證 {#prefix-origin-validation}

假設你的網路在 IP 地址 `192.168.1.1` 上有一個 RTR 伺服器：

```ros
/routing/rpki
add group=myRpkiGroup address=192.168.1.1 port=8282 refresh-interval=20
```

[`group`](./rpki.md#group)、[`address`](./rpki.md#address)、[`port`](./rpki.md#port) 和 [`refresh-interval`](./rpki.md#refresh-interval) 引數用於配置 RTR 連線。其他引數包括 [`vrf`](./rpki.md#vrf)、[`preference`](./rpki.md#preference)、[`retry-interval`](./rpki.md#retry-interval) 和 [`expire-interval`](./rpki.md#expire-interval)。

連線建立並收到驗證器資料庫後，使用 [`rpki-check`](../../../cli-reference/routing/rpki/rpki-check.md) 檢查字首有效性：

```text
[admin@MikroTik] /routing/rpki> rpki-check group=myRpkiGroup prefix=70.132.18.0/24 origin-as=16509
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

## ASPA 驗證 {#aspa-validation}

ASPA 物件為客戶 AS 授權一組提供方 AS。RouterOS 會根據 ASPA 物件驗證 BGP AS 路徑，以檢測字首源驗證無法檢測的路由洩漏。ASPA 驗證補充字首源驗證；同時使用兩者來檢測無效源和路由洩漏。驗證遵循 [draft-ietf-sidrops-aspa-verification](https://datatracker.ietf.org/doc/draft-ietf-sidrops-aspa-verification/)。

ASPA 驗證需要：

- 一個支援 RTR 協定版本 2 併發布 ASPA 物件的驗證器。
- 在 eBGP 連線上使用 [`local.role`](../../../cli-reference/routing/bgp/connection.md#local.role) 配置的 RFC 9234 角色。`ibgp`、`ibgp-rr` 和 `ebgp` 角色不提供 ASPA 驗證所需的角色資訊，因此使用這些角色的會話不會執行 ASPA 驗證。請參閱 [路由洩漏防護](./bgp/route-leak-prevention.md)。
- 在路由過濾鏈中使用 `rpki-aspa-verify` 命令啟用 ASPA 驗證。

以下示例對從提供商接收的路由同時驗證字首來源和 AS 路徑。該示例假定已存在一個名為 `to-provider` 的 BGP 連線：

```ros
/routing/rpki
add group=rpki1 address=192.0.2.10 port=8282

/routing/bgp/connection
set [find where name=to-provider] local.role=ebgp-customer

/routing/filter/rule
add chain=bgp_in rule="rpki-verify rpki1"
add chain=bgp_in rule="rpki-aspa-verify rpki1"
add chain=bgp_in rule="if (rpki invalid || rpki-aspa invalid) { reject } else { accept }"
```

`rpki-verify` 命令選擇用於字首來源驗證的組。`rpki-aspa-verify` 命令選擇用於 ASPA 驗證的組。兩個命令可以使用同一個組。

### ASPA 驗證狀態 {#aspa-validation-states}

`rpki-aspa` 過濾屬性以及 [`rpki-aspa`](../../../cli-reference/routing/route.md#rpki-aspa) 路由屬性具有以下取值：

- `valid` - AS 路徑與 ASPA 資料一致。
- `invalid` - AS 路徑包含未授權的 AS 對。該路由很可能是路由洩漏。
- `unknown` - ASPA 資料未覆蓋路徑中的至少一個 AS 對。
- `unverified` - 未執行 ASPA 驗證，例如因為 BGP 會話沒有 RFC 9234 角色，或者過濾鏈未選擇用於 ASPA 的 RPKI 組。在此狀態下，`/routing/route` 輸出不會顯示 `rpki-aspa` 屬性。

在過濾器中使用該狀態來接受或拒絕路由：

```ros
/routing/filter/rule
add chain=bgp_in rule="rpki-aspa-verify rpki1"
add chain=bgp_in rule="if (rpki-aspa invalid) { reject } else { accept }"
```

ASPA 校驗僅提供狀態。過濾規則定義操作。`else` 分支接受具有 `valid`、`unknown` 和 `unverified` 狀態的路由。新增更嚴格的規則，以根據您的路由策略處理這些狀態。

### 驗證 ASPA 校驗 {#verify-aspa-validation}

檢查協商的 RTR 版本：

```ros
/routing/rpki/session print detail
```

檢查路由的 ASPA 狀態：

```ros
/routing/route print detail where rpki-aspa=invalid
```

[`rpki-check`](../../../cli-reference/routing/rpki/rpki-check.md) 和 [`rpki-query`](../../../cli-reference/routing/rpki/rpki-query.md) 命令僅檢查字首源資料。ASPA 狀態取決於完整的 AS 路徑和 BGP 角色，因此使用 `rpki-aspa` 路由屬性或過濾規則來檢查它。
