---
sidebar_key: "routing-and-networking-protocols/unicast/bgp/route-leak-prevention"
sidebar_position: 4
title: "路由洩露防護"
sidebar_label: "路由洩露防護"
description: "使用 RFC 9234 中定義的 BGP 角色來防止並檢測路由洩漏。"
tags:
  - 'routing'
  - 'bgp'
  - 'rfc-9234'
slug: /user-guides/routing-and-networking-protocols/unicast/bgp/route-leak-prevention
source: https://manual.mikrotik.com/docs/7.25/user-guides/routing-and-networking-protocols/unicast/bgp/route-leak-prevention
captured_at: '2026-11-04T11:22:47+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

當 BGP 發言人向對等體通告路由，而根據配置的業務關係該對等體本不應收到這些路由時，就會發生路由洩漏。例如，中轉客戶將從某個提供商學習到的路由重新通告給另一個提供商，可能導致流量經過該客戶的網路進行路由，從而可能繞過預期路徑，並造成路由環路或流量攔截。

[RFC 9234](https://datatracker.ietf.org/doc/rfc9234/) — *使用 UPDATE 和 OPEN 訊息中的角色預防和檢測路由洩漏* — 定義了一種機制：為每個 eBGP 會話分配一個描述兩個對等體之間關係的角色，以此來預防和檢測路由洩漏。RouterOS 透過 `local.role` 引數實現該機制，該引數對每個 BGP 連線都是必需的，並定義本地路由器在 BGP 會話中的角色。

`ibgp`、`ibgp-rr` 和 `ebgp` 角色不參與 RFC 9234 角色協商。會話將作為傳統 BGP 會話建立，不交換 Role 能力。

其餘五個角色參與 RFC 9234 角色協商：

| 角色 | 描述 |
| :-- | :-- |
| `ebgp-provider` | 中轉提供商。 |
| `ebgp-rs` | 路由伺服器。 |
| `ebgp-rs-client` | 路由伺服器用戶端。 |
| `ebgp-customer` | 中轉客戶。 |
| `ebgp-peer` | 橫向對等體（對等關係）。 |

### 關係型別 {#relationship-types}

這些角色描述兩個 eBGP 對等體之間的業務關係：

- **中轉提供商—客戶**：提供商向客戶出售中轉服務，使客戶能夠訪問提供商的完整路由表（通常是整個網際網路）。客戶將其自有字首及其下游客戶的字首通告給提供商。提供商將其學習到的所有路由（包括來自其他客戶和對等體的路由）通告給客戶。在此關係中，提供商是上游，客戶是下游。
- **路由伺服器—用戶端**：路由伺服器是一種中立的 BGP 發言人，通常部署在網際網路交換點（IXP）。它本身不轉發流量——它只在用戶端之間反射路由資訊。路由伺服器用戶端連線到路由伺服器，以便與其他用戶端交換路由，而無需與每個用戶端建立直接對等會話。路由伺服器不修改 AS_PATH 或 NEXT_HOP，也不出現在資料路徑中。
- **橫向對等體**：兩個具有對等關係的網路僅交換各自的路由及各自客戶的路由。雙方都不通告從其他對等體或提供商學習到的路由。對等通常是無結算的，即兩個網路之間不進行金錢交換。

兩個對等體必須配置為匹配的角色，會話才能成功建立。

## 角色協商 {#role-negotiation}

當 BGP 會話配置了 RFC 9234 角色時，路由器會在 OPEN 訊息中傳送 BGP Role 能力（能力程式碼 9）。當本地路由器收到遠端對等體的 OPEN 訊息時，它會根據本地配置的 `local.role` 檢查收到的角色是否符合預期角色：

| 本地角色 | 預期的遠端角色 |
| :-- | :-- |
| `ebgp-provider` | `ebgp-customer` |
| `ebgp-customer` | `ebgp-provider` |
| `ebgp-rs` | `ebgp-rs-client` |
| `ebgp-rs-client` | `ebgp-rs` |
| `ebgp-peer` | `ebgp-peer` |

如果遠端對等體未傳送 Role 能力，或者收到的角色與預期角色不匹配，路由器會發送一條 NOTIFICATION 訊息，其中包含錯誤碼 2（OPEN Message Error）、錯誤子碼 8（Role Mismatch），並終止會話。

協商後的角色可在會話監控輸出中檢視：

- `remote.role` — 在 OPEN 訊息中從遠端對等體收到的角色。
- `local.role` — 本地配置的角色。

## 配置 {#configuration}

`local.role` 引數在 [`/routing/bgp/connection`](../../../../cli-reference/routing/bgp/connection.md) 選單中配置。

如果會話建立成功，可以在 [`/rouring/bgp/session`](../../../../cli-reference/routing/bgp/session/index.md) 選單中監控協商後的能力和選定的角色。

當遠端對等體支援 BGP Role 能力時，`remote.capabilities` 欄位會包含 `role`。`remote.role` 欄位顯示從遠端對等體收到的實際角色。

如果會話因角色不匹配而未能建立，`input.last-notification` 欄位會包含從對等體收到的十六進位制編碼的 NOTIFICATION 訊息。

### 示例：中轉提供商到客戶 {#example-transit-provider-to-customer}

連線到下游客戶的中轉提供商：

```ros
# 提供商侧（AS 64500）
/routing/bgp/instance
add name=instance1 as=64500
/routing/bgp/connection
add name=to-customer remote.address=198.51.100.1 instance=instance1 local.role=ebgp-provider

# 客户侧（AS 64501）
/routing/bgp/instance
add name=instance1 as=64501
/routing/bgp/connection
add name=to-provider remote.address=192.0.2.1 instance=instance1 local.role=ebgp-customer
```

兩個對等體必須配置為匹配的角色。配置為 `ebgp-provider` 的對等體預期遠端為 `ebgp-customer`，反之亦然。

### 示例：帶多個用戶端的路由伺服器 {#example-route-server-with-multiple-clients}

連線到多個用戶端的 IXP 路由伺服器：

```ros
# 路由服务器侧（AS 65500）
/routing/bgp/instance
add name=instance1 as=65500
/routing/bgp/connection
add name=rs-client1 remote.address=203.0.113.1 instance=instance1 local.role=ebgp-rs
add name=rs-client2 remote.address=203.0.113.2 instance=instance1 local.role=ebgp-rs

# 路由服务器客户端侧（AS 64601）
/routing/bgp/instance
add name=instance1 as=64601
/routing/bgp/connection
add name=to-rs remote.address=203.0.113.254 instance=instance1 local.role=ebgp-rs-client
```

### 示例：兩個網路之間的對等 {#example-peering-between-two-networks}

兩個具有對等關係的網路：

```ros
# Network A (AS 64500)
/routing/bgp/instance
add name=instance1 as=64500
/routing/bgp/connection
add name=to-peer-b remote.address=192.0.2.2 instance=instance1 local.role=ebgp-peer

# Network B (AS 64700)
/routing/bgp/instance
add name=instance1 as=64700
/routing/bgp/connection
add name=to-peer-a remote.address=192.0.2.1 instance=instance1 local.role=ebgp-peer
```

### 示例：iBGP 和路由反射器 {#example-ibgp-and-route-reflector}

內部 BGP 會話不使用 RFC 9234 角色協商：

```ros
# iBGP peer
/routing/bgp/instance
add name=instance1 as=64500
/routing/bgp/connection
add name=ibgp-peer1 remote.address=10.0.0.2 instance=instance1 local.role=ibgp

# iBGP 路由反射器客户端
/routing/bgp/connection
add name=rr-client1 remote.address=10.0.0.3 instance=instance1 local.role=ibgp-rr
```
