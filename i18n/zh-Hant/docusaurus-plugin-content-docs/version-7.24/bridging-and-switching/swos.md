---
title: "SwOS"
description: "SwOS 是專為 MikroTik 交換器硬體管理所打造的輕量作業系統。它可在所有標準 Ethernet 訊框上提供最大的線速 Layer 2 轉送能力，並無縫處理 IPv4、IPv6 與非 IP 流量。"
source: https://manual.mikrotik.com/docs/7.24/bridging-and-switching/swos
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

# SwOS 簡介 {#introduction-to-swos}

SwOS 是專為管理 MikroTik 交換器硬體而打造的輕量級作業系統。它可在所有標準 Ethernet 訊框上提供最大的線速 Layer 2 轉送能力，並無縫處理 IPv4、IPv6 與非 IP 流量。

### 核心與進階功能 {#core--advanced-features}

除了標準的網管交換器功能之外，SwOS 還提供完整的網路功能套件：

* **VLAN 管理：** 完整支援複雜 VLAN 設定，包括 access 與 trunking 埠。
* **流量控制：** 進階廣播風暴控制、頻寬限制與埠對埠轉送設定。
* **監控與鏡像：** 入口／出口流量鏡像，以及即時埠層級統計資料。
* **安全性與篩選：** 細緻的 Access Control List（ACL）引擎，可依 MAC、IP 與埠層級規則比對流量。
* **硬體卸載：** 在支援的設備型號上，直接由硬體驅動操作特定 MAC 與 IP 標頭欄位。

:::note 管理限制
SwOS 只能透過標準網頁瀏覽器（HTTP）並經由 IPv4 進行設定。它不支援透過序列主控台／SSH 使用命令列介面（CLI）存取、API 存取、WinBox 或其他替代管理協定。
:::

<DocCardList />
