---
sidebar_key: "bridging-and-switching/swos/index"
sidebar_position: 6
title: "SwOS"
sidebar_label: "SwOS"
description: "SwOS 是專為管理 MikroTik 交換硬體而構建的輕量級作業系統。它可在所有標準乙太網幀上提供最大線速二層轉發能力，無縫處理 IPv4、IPv6 和非 IP 流量。"
source: https://manual.mikrotik.com/docs/7.24/bridging-and-switching/swos
captured_at: '2026-11-04T11:27:06+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

# SwOS 簡介 {#introduction-to-swos}

SwOS 是一款專為管理 MikroTik 交換硬體而構建的輕量級作業系統。它在所有標準乙太網幀上提供最大線速的二層轉發能力，並無縫處理 IPv4、IPv6 和非 IP 流量。

### 核心與高階功能 {#core--advanced-features}

除了標準的受管交換器功能之外，SwOS 還提供了一套強大的網路功能：

* **VLAN 管理：** 完整支援複雜 VLAN 設定的配置，包括接入埠和幹道埠。
* **流量控制：** 高階廣播風暴控制、頻寬限制以及埠到埠轉發設定。
* **監控與映象：** 入站/出站流量映象，以及即時埠級統計資訊。
* **安全與過濾：** 細粒度的訪問控制列表（ACL）引擎，能夠依據 MAC、IP 和埠級規則匹配流量。
* **硬體解除安裝：** 在支援的裝置型號上，由硬體直接驅動的特定 MAC 和 IP 報頭欄位操作。

:::note 管理限制
SwOS 僅能透過基於 IPv4 的標準 Web 瀏覽器（HTTP）進行配置。它不支援透過序列控制檯/SSH 的命令列介面（CLI）訪問、API 訪問、WinBox 或其他替代管理協定。
:::

<DocCardList />
