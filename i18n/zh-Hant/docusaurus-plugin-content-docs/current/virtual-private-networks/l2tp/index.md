---
sidebar_key: "virtual-private-networks/l2tp"
title: "L2TP"
sidebar_label: "L2TP"
description: "本頁面介紹 MikroTik RouterOS 的 L2TP 配置,涵蓋用戶端與伺服器的設定,包括 authentication methods、MTU/MRRU 設定、IPsec 整合,以及在 Layer Two Tunneling Protocol 場景下的動態介面管理。"
tags:
  - 'l2tp'
  - 'ppp'
  - 'ipsec'
source: https://manual.mikrotik.com/docs/virtual-private-networks/l2tp
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本節涵蓋 L2TP 示例。可用於配置 LAC 和 LNS 場景以及相關的 L2TP 互操作案例。

Layer Two Tunneling Protocol "L2TP" 擴充套件了 PPP 模型，允許 L2 和 PPP 端點位於由分組交換網路互連的不同裝置上。L2TP 為每個 L2TP 連線包含 PPP 認證和計費。每個連線的完整認證和計費可以透過 RADIUS 用戶端或本地完成。L2TP 流量對控制包和封包都使用 UDP 協定。UDP 埠 1701 僅用於鏈路建立，後續流量使用任意可用的 UDP 埠（可以與 1701 不同）。這意味著，只要允許 UDP 流量透過防火牆或路由器，L2TP 就能與大多數防火牆和路由器（即使存在 NAT）配合使用。L2TP 標準定義於 [RFC 2661](https://tools.ietf.org/html/rfc2661)。L2TPv3 支援在 7.1 版本中新增，它支援 IPv4 和 IPv6。

## 簡介 {#introduction}

L2TP 可以像任何其他隧道協定一樣使用，無論是否加密。L2TP 標準指出，加密資料最安全的方式是 L2TP over IPsec（這是 Microsoft L2TP 用戶端的預設模式），因為特定隧道的所有 L2TP 控制包和封包在 IPsec 系統看來都是同質的 UDP/IP 封包。

支援 Multilink PPP (MP)，以提供 MRRU（能夠傳輸全長 1500 及更大封包的能力），並透過 Bridge Control Protocol (BCP) 在 PPP 鏈路上進行橋接，BCP 允許透過 PPP 鏈路傳送原始乙太網幀。這樣就可以在沒有 EoIP 的情況下建立橋接。網橋中應當有一個管理上設定的 MAC 地址，或者包含一個類似乙太網的介面，因為 PPP 鏈路沒有 MAC 地址。

:::warning
L2TP 不為隧道流量提供加密機制。可使用 IPsec 提供額外的安全層。
:::

## 快速示例 {#quick-example}

![](/img/f2cf148d94cfeff8.webp)

### L2TP 伺服器 {#l2tp-server}

在伺服器端，啟用 L2TP 伺服器併為特定使用者建立 PPP 配置檔案：

```ros
[admin@MikroTik] > /interface/l2tp-server/server/set enabled=yes
[admin@MikroTik] > /ppp/secret/add local-address=10.0.0.2 name=MT-User password=StrongPass profile=default-encryption remote-address=10.0.0.1 service=l2tp
```

### L2TP 用戶端 {#l2tp-client}

本示例配置一個 L2TP 用戶端，使用者名稱為 "MT-User"，密碼為 "StrongPass"，伺服器為 192.168.51.3：

```ros
[admin@MikroTik] > /interface/l2tp-client \
add connect-to=192.168.51.3 disabled=no name=MT-User password=StrongPass user=MT-User
[admin@MikroTik] > /interface/l2tp-client/print 
Flags: X - disabled, R - running 
0 R name="MT-User" max-mtu=1450 max-mru=1450 mrru=disabled connect-to=192.168.51.3 user="MT-User" 
password="StrongPass" profile=default-encryption keepalive-timeout=60 use-ipsec=no ipsec-secret="" 
allow-fast-path=no add-default-route=no dial-on-demand=no allow=pap,chap,mschap1,mschap2
```

## L2TP Ether {#l2tp-ether}

### 概述 {#overview}

Layer 2 Tunnel Protocol Version 3 (L2TPv3) 由 Internet Engineering Task Force (IETF) 的 [RFC 3931](https://tools.ietf.org/html/rfc3931) 定義。它對原始 L2TP 引入了多項改進，允許在 L2TP 內封裝二層（L2）載荷，以用於二層虛擬專用網路（VPN）。L2TP Ether 隧道在兩個端點之間傳輸原始乙太網幀（乙太網偽線，Pseudowire-Type 5）。

要建立 L2TP Ether 隧道，必須在用戶端側建立 L2TP Ether 介面，而在遠端（伺服器）側必須啟用 L2TP 伺服器。兩側配置正確後，它們之間會自動建立一個動態介面，從而跨越 IP 網路形成透明的二層連線。

L2TP Ether 可以封裝在 UDP 之上（`l2tp-proto-version=l2tpv3-udp`，預設值），也可以直接封裝在 IP 之上（`l2tp-proto-version=l2tpv3-ip`）。支援 IPv4 和 IPv6 覆蓋網路；`connect-to` 可接受 IPv4 或 IPv6 地址。

### 拓撲與角色 {#topology-and-roles}

L2TP Ether 隧道有兩種不同的角色：

- **主動（用戶端）側** — 建立一個 `/interface/l2tp-ether` 條目，將 `connect-to=` 指向伺服器。該側發起 L2TPv3 控制連線和乙太網會話。
- **被動（伺服器）側** — 只需啟用 L2TP 伺服器（`/interface/l2tp-server/server`）。當主動側連線時，RouterOS 會在伺服器上**自動建立一個動態的** `l2tp-ether` 介面（標誌 `D`）；無需在此手動配置。

通常將兩個介面都加入同一個網橋，使兩個站點共享一個二層域。

### 配置示例 {#configuration-example}

本示例在兩臺路由器之間建立 L2TP Ether 隧道。

#### 伺服器側（L2TP 伺服器） {#server-side-l2tp-server}

```ros
/interface/l2tp-server/server/set enabled=yes
```

#### 用戶端側（L2TP Ether 介面） {#client-side-l2tp-ether-interface}

```ros
/interface/l2tp-ether/add connect-to=1.1.1.1 disabled=no
```

在主動側驗證會話（示例輸出）：

```ros
[admin@MikroTik] > /interface/l2tp-ether/print
Flags: X - disabled, R - running, D - dynamic, u - unmanaged 
 0 R name="l2tp-ether1" mac-address=02:3D:2B:00:00:00 connect-to=1.1.1.1 ...
```

在被動側，隧道建立後會自動出現一個**動態**介面（標誌 `D`）（示例輸出）：

```ros
[admin@MikroTik] > /interface/l2tp-ether/print
Flags: X - disabled, R - running, D - dynamic, u - unmanaged 
 0 DR name="l2tp-ether1" mac-address=02:3D:2B:00:00:01 connect-to=0.0.0.0 ...
```

### 伺服器側的會話接受 {#server-side-session-acceptance}

伺服器是否接受傳入的乙太網會話由 `/interface/l2tp-server/server` 中的 L2TP 伺服器設定控制。完整屬性列表請參閱 [CLI 參考](../../cli-reference/interface/l2tp-server/server.md)。

| 設定 | 控制內容 |
|---|---|
| `max-sessions` | 伺服器上併發 L2TP 會話的最大數量。達到限制後，伺服器將拒絕新會話。 |
| `accept-proto-version` | 接受哪些 L2TP 協定版本（`all`、`l2tpv2`、`l2tpv3`）。 |
| `accept-pseudowire-type` | 接受哪些偽線型別（`all`、`ether`、`ppp`）。對於 L2TP Ether 隧道，必須允許 `ether`。 |
| `l2tpv3-ether-interface-list` | 動態乙太網偽線端點所附著的介面列表。 |
| `l2tpv3-circuit-id` | 伺服器為傳入會話使用的 L2TPv3 電路識別符號。 |
| `l2tpv3-cookie-length` | 伺服器通告的 L2TPv3 cookie 長度。 |
| `l2tpv3-digest-hash` | 伺服器使用的 L2TPv3 摘要雜湊演算法。 |

### 匹配 circuit-id 和 cookie {#matching-circuit-id-and-cookies}

當伺服器設定 `l2tpv3-circuit-id`、`l2tpv3-cookie-length` 或 `l2tpv3-digest-hash` 時，用戶端側的 `l2tp-ether` 條目中需要有對應的值（`circuit-id`、`cookie-length`、`digest-hash`）。如果這些值不一致，即使控制連線已經建立，會話也可能失敗 — 請檢查兩端是否一致。用戶端側屬性請參閱 [L2TP Ether CLI 參考](../../cli-reference/interface/l2tp-ether/index.md)。

### 驗證與故障排查 {#verify-and-troubleshoot}

如果 L2TP 控制連線已經建立，但乙太網會話立即被拆除，那麼即使傳輸層看起來正常，隧道也無法工作。

| 現象 | 可能原因 | 檢查方法 |
|---|---|---|
| 日誌顯示 `maximum session count reached`，隨後出現 CDN（`Result-Code=4`）且隧道斷開 | 達到伺服器會話限制時會話被拒絕 — 這是值得檢查的常見原因，並非確定的診斷 | 確認 `/interface/l2tp-server/server` 上的 `max-sessions` 沒有限制新會話 |
| 會話被拒絕，伺服器上沒有動態介面 | 偽線或協定型別未被接受 | `accept-pseudowire-type` 應允許 `ether`；`accept-proto-version` 應允許 `l2tpv3` |
| 被動側沒有動態介面 | 介面列表未涵蓋隧道端點 | 檢查 `l2tpv3-ether-interface-list` |
| 會話建立但沒有流量透過 | 用戶端與伺服器之間的 `circuit-id` / `cookie-length` / `digest-hash` 不一致 | 比較 `l2tp-ether` 和 `l2tp-server` 的設定 |

可隨時使用 [monitor](../../cli-reference/interface/l2tp-ether/monitor.md) 命令檢視活動會話：

```ros
/interface/l2tp-ether/monitor l2tp-ether1
```
