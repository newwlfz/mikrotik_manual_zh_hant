---
sidebar_key: "user-guides/routing-and-networking-protocols/mpls/exp-bit-and-mpls-queuing"
sidebar_position: 1
title: "EXP 位和 MPLS 佇列"
sidebar_label: "EXP 位和 MPLS 佇列"
description: "本頁說明 MPLS 封包中的 EXP 位，以及 RouterOS 如何為 QoS 處理該位，包括優先順序標記、佇列策略和 MPLS mangle 規則。文中詳細介紹了在封包交換、倒數第二跳彈出和本地處理期間如何處理 EXP 位，並給出了在 RouterOS 中配置 MPLS mangle 規則的示例。"
tags:
  - 'mpls'
source: https://manual.mikrotik.com/docs/user-guides/routing-and-networking-protocols/mpls/exp-bit-and-mpls-queuing
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

當 MPLS 標籤附加到封包時，它會使封包長度增加 32 bits（4 bytes）。這 32 bits 的構成如下：

- 標籤值本身（20 bits）。
- EXP（“experimental”）欄位（3 bits）。
- Time to live 欄位（8 bits）。
- Bottom of stack 欄位（1 bit）。

MPLS 標準未規定“experimental”位的用途，但最常見的用途是攜帶 QoS 資訊，類似於 VLAN 標籤中的 802.1q 優先順序。EXP 欄位僅包含 3 bits，這意味著它可以攜帶 0 到 7 的值，從而支援 8 個流量類別。

## RouterOS 中 EXP 欄位的處理 {#exp-field-treatment-in-routeros}

當 RouterOS 收到 MPLS 封包時，會將封包的 "ingress priority" 值設定為頂層標籤內攜帶的值。"ingress priority" 不是封包頭部中的欄位，而是 RouterOS 在處理封包時為其分配的額外標記。當 RouterOS 為 MPLS 封包新增標籤時，會將 EXP 位設定為分配給該封包的 "priority"（不是 "ingress priority"）。當 RouterOS 交換 MPLS 封包時，會自動將 "ingress priority" 複製到 "priority"。這樣，常規 MPLS 交換就會在整個標籤交換路徑上傳遞優先順序資訊。

有關 "ingress priority" 和 "priority" 處理的更多資訊，另請參閱 [WMM 與 VLAN 優先順序](../../../bridging-and-switching/user-guides/wmm-and-vlan-priority.md)。

EXP 欄位的行為取決於對封包執行的動作：

- 如果 RouterOS 對封包進行 MPLS 交換（彈出標籤並壓入新標籤），新標籤中的 EXP 欄位與收到的標籤一致，因為：
  - RouterOS 會將 "ingress priority" 設定為收到的標籤中的 EXP 位。
  - 交換會自動將 "priority" 設定為 "ingress priority"。
  - RouterOS 為封包新增新標籤，並將其 EXP 位設定為 "priority" 中的值。
- 如果 RouterOS 透過 penultimate-hop-popping 對封包進行 MPLS 交換（路由器彈出收到的標籤且不壓入新標籤），EXP 欄位的優先順序會保留在封包的 "priority" 欄位中。其他 MAC 協定（例如 WMM 或 802.1q VLAN）隨後可以使用此值：
  - RouterOS 會將 "ingress priority" 設定為收到的標籤中的 EXP 位。
  - 交換會自動將 "priority" 設定為 "ingress priority"。
  - RouterOS 在不壓入標籤的情況下將封包交換到下一跳，並且這一過程透過 VLAN 介面進行。
  - VLAN 介面會將 VLAN 頭部中的 802.1q 優先順序設定為封包的 "priority" 值。

penultimate-hop-popping 可能會在最後一跳丟失透過標籤交換路徑傳遞的 QoS 資訊。如果需要保留此資訊，請為標籤交換路徑中的最後一跳使用 Explicit NULL 標籤而不是 Implicit NULL 標籤，以停用 penultimate-hop-popping。預設情況下，MPLS TE 隧道會為最後一跳使用 Explicit NULL 標籤。

- 如果 RouterOS 透過標籤交換路徑傳送封包（路由器將第一個標籤壓入封包），它會將 EXP 位設定為 "priority" 中的值。你可以使用防火牆規則或其他方式（例如來自 IP 頭部中的 DSCP 欄位）正確設定此值。
- 如果 RouterOS 收到用於本地處理的封包，它會將 "ingress priority" 設定為收到封包的 EXP 欄位。然後，你可以使用此值更新封包的 DSCP 欄位，或使用防火牆規則將 "priority" 設定為 "ingress priority"。

## MPLS Mangle 與佇列 {#mpls-mangle-and-queuing}

RouterOS 防火牆僅適用於 IP 流量，這意味著你不能直接在 mangle 中標記 MPLS 封包並透過佇列對其進行限制。你必須在新增 MPLS 頭部之前的入口邊緣路由器上，或在移除 MPLS 標籤之後的出口邊緣路由器上執行排隊。

從 ROS v7.17 開始，RouterOS 包含 MPLS Mangle。此功能允許你在標籤交換（P）路由器上或 MPLS 封裝後的 PE 輸出上，根據 EXP 位新增封包標記，或更改分配的 EXP 位。

此配置可從 `/mpls/mangle` 選單訪問。

### 基本示例 {#basic-example}

讓我們看一個非常基本的示例：在 LSP 上的標籤交換路由器（P）上，我們希望標記 EXP 位為 0 的封包，限制頻寬並將 EXP 位改為 3：

```routeros
/mpls/mangle
add chain=forward exp=0 set-exp=3 set-mark=m0

/queue/tree
add limit-at=10M max-limit=10M name=mpls_queue packet-mark=m0 parent=sfp-sfpplus2
```

MPLS 封包不能使用基於 IMQ 介面的佇列（simple queue、queue tree global）進行排隊。必須使用以“真實”介面作為父級的 queue tree。

MPLS Mangle 表會顯示匹配的封包計數，這對於偵錯配置很有用：

```ros
[admin@CCR2004_2XS_111] /mpls/mangle> print 
Flags: X - DISABLED
Columns: CHAIN, EXP, SET-EXP, SET-MARK, PACKETS
#   CHAIN    EXP  SET-EXP  SET-MARK  PACKETS
0   forward    0        3  m0        221 654
```

MPLS mangle 規則不會像常規防火牆 mangle 規則那樣逐行執行。相反，MPLS Mangle 會一次性應用所有動作。

例如，請檢視以下規則集：

```routeros
/mpls/mangle
add chain=forward exp=0 set-mark=m0
add chain=forward exp=0 set-exp=3
add chain=forward exp=3 set-mark=m3
```

在此示例中，如果傳入封包的 EXP 位值為 0，則第三條規則不適用。

為特定 EXP 位設定動作後，其他規則無法修改它：

```ros
[admin@CCR2004_2XS_111] /mpls/mangle> add chain=forward exp=0 set-mark=m4
failure: conflicting forward set-mark rule
```
