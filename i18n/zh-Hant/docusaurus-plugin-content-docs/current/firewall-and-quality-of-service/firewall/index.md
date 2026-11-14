---
sidebar_key: "firewall-and-quality-of-service/firewall"
title: "防火牆"
sidebar_label: "防火牆"
description: "MikroTik RouterOS 防火牆提供有狀態和無狀態封包過濾、NAT 以及高階流量分類，以保護網路資料流並防止未經授權的訪問。它包含 filter/raw、mangle 和 nat 模組，並帶有預定義鏈，可實現高效的規則管理。"
tags:
  - 'firewall'
  - 'packet-flow'
source: https://manual.mikrotik.com/docs/firewall-and-quality-of-service/firewall
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![Firewall fundamentals](/img/f4625aee0e2b1d17.webp)

防火牆透過利用連線跟蹤實現有狀態封包過濾，並提供無狀態封包過濾，從而提供用於管理發往路由器、來自路由器以及經過路由器的資料流的安全功能。它與網路地址轉換 (NAT) 一起，可作為防止未經授權訪問直連網路和路由器本身的工具，同時也可作為出站流量的過濾器。

網路防火牆可防止外部威脅接觸網路內部可用的敏感資料。每當不同網路連線在一起時，總存在來自網路外部的人闖入你的 LAN 的威脅。此類入侵可能導致私有資料被竊取和傳播、有價值的資料被篡改或銷燬，或者整個硬碟被擦除。防火牆被用作防止或最小化連線到其他網路時固有安全風險的手段。配置正確的防火牆在高效且安全的網路基礎設施部署中起著關鍵作用。

MikroTik RouterOS 具有非常強大的防火牆實現，其功能包括：

- 無狀態封包檢查。
- 有狀態封包檢查。
- 第 7 層協定檢測。
- 對等協定過濾。
- 流量分類依據：
  - 源 MAC 地址。
  - IP 地址（網路或列表）和地址型別（廣播、本地、組播、單播）。
  - 埠或埠範圍。
  - IP 協定。
  - 協定選項（ICMP 型別和程式碼欄位、TCP 標誌、IP 選項和 MSS）。
  - 封包進入或離開的介面。
  - 內部流和連線標記。
  - DSCP 位元組。
  - 封包內容。
  - 封包到達速率和序列號。
  - 封包大小。
  - 封包到達時間。

以及更多內容！

防火牆分為三個主要模組：

- **filter/raw** - 用於根據配置的策略拒絕流量。如果不需要連線跟蹤，在 RAW 表中進行過濾可以節省資源。
- **mangle** - 用於標記特定連線、封包、流，設定優先順序以及執行其他任務。
- **nat** - 用於設定地址轉換規則、重定向和埠轉發。

## 鏈 {#chains}

防火牆過濾規則按鏈分組。這樣可以讓封包在一個鏈中與一項共同條件匹配，然後傳遞到另一個鏈以根據其他共同條件進行處理。

例如，封包應匹配 IP 地址:埠對。當然，可以透過向 forward 鏈新增所需數量的 IP 地址:埠匹配規則來實現，但更好的方法可能是新增一條匹配來自特定 IP 地址的流量的規則。然後，可以將針對不同埠執行匹配的規則新增到 "**mychain**" 鏈中，而無需指定 IP 地址。

```ros
/ip/firewall/filter 
add chain=mychain protocol=tcp dst-port=22 action=accept
add chain=mychain protocol=tcp dst-port=23 action=accept

add action=jump chain=input src-address=1.1.1.2/32 jump-target="mychain"
```

處理鏈時，規則按列出順序從上到下從鏈中獲取。如果封包匹配規則的條件，則對其執行指定動作，並且不再處理該鏈中的更多規則（例外是 **passthrough** 動作和某些 [Mangle](./mangle.md) 動作）。

如果封包未匹配鏈中的任何規則，則它會被接受。

每個防火牆模組都有其自己的預定義鏈：

- **raw**：
  - prerouting
  - output
- **filter**：
  - input
  - forward
  - output
- **mangle**：
  - prerouting
  - input
  - forward
  - output
  - postrouting
- **nat**：
  - srcnat
  - dstnat
  - input
  - output

更詳細的 RouterOS 封包處理在 [RouterOS 中的封包流程](../packet-flow-in-routeros.md) 圖中描述。
