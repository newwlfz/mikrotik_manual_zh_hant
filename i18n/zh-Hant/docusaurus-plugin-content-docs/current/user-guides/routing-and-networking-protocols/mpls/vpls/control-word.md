---
sidebar_key: "user-guides/routing-and-networking-protocols/mpls/vpls/control-word"
sidebar_position: 1
title: "控制字"
sidebar_label: "控制字"
description: "VPLS 在 RouterOS 中使用 Control Words (CW) 進行封包分片和重組，增加 4 位元組開銷以處理 L2MTU 限制。CW 欄位包括 flags、fragmentation indicators、length 和用於封包跟蹤的 sequence numbers，其使用由 `use-control-word` 引數控制。"
tags:
  - 'vpls'
  - 'mpls'
  - 'control-word'
  - 'fragmentation'
source: https://manual.mikrotik.com/docs/user-guides/routing-and-networking-protocols/mpls/vpls/control-word
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

VPLS 允許遠端站點透過分組交換網路（PSN）上的 **偽線（PW）** 隧道連線站點，從而共享一個 Ethernet 廣播域。由於 VPLS 封裝會增加額外開銷，LSP 中的每個介面都應能夠傳輸足夠大的封包。

每個 Ethernet 晶片組在可傳輸的最大封包大小方面都有硬體限制。即使現在，仍有隻支援一個 Vlan 標籤的 Ethernet 網路，這意味著不含 Ethernet 頭部和校驗和的最大封包大小（L2MTU）為 1504 位元組。顯然，這不足以在不進行分片的情況下轉發經過 VPLS 封裝的 Ethernet 幀（至少需要支援 1526 的 L2MTU）。有關 RouterBOARD 上支援的最大 L2MTU，請參閱 [RouterOS 中的 MTU](../../../../hardware/mtu-in-routeros.md)。

由於並非所有 RouterBOARD 都支援足夠大的 L2MTU 來在不進行分片的情況下傳輸經過 VPLS 封裝的封包，RouterOS 根據 RFC 4623 增加了使用 4 位元組 **Control Word (CW)** 的偽線分片與重組（PWE3）支援。

## Control Word 的使用 {#control-word-usage}

在 RouterOS 中，Control Word 用於 VPLS 隧道內的封包分片和重組。這是透過使用可選的 **Control Word (CW)** 來實現的。CW 被新增在 PW 標籤（解複用器）和封包有效載荷之間，並增加額外的 4 位元組開銷。

:::warning
未實現 OOO 封包的重排序，亂序分片將被丟棄
:::

CW 的使用由 VPLS 配置中的 `use-control-word` 引數控制。

![](/img/53a24ce6c27ddc30.jpg#gh-light-mode-only)
![](/img/012019abb10aff98.png#gh-dark-mode-only)

如你所見，**Control Word** 被劃分為 5 個欄位：

- 0000 - 4 位，標識該封包是 PW（不是 IP）。
- Flags - 4 位。
- Frag - 2 位值，表示有效載荷分片。
- Len - 6 位。
- Seq - 16 位序列號，用於檢測封包丟失/亂序。

根據 RFC，序列號的生成和處理是可選的。
