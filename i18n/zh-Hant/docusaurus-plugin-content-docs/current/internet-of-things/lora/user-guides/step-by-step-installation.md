---
sidebar_key: "internet-of-things/lora/user-guides/step-by-step-installation"
sidebar_position: 3
title: "逐步安裝"
sidebar_label: "逐步安裝"
description: "本頁提供在 MikroTik RouterOS 上安裝和配置 LoRa mini-PCIe 卡的分步指南，包括硬體安裝、GUI 設定、軟體包管理以及初始網路伺服器配置。"
tags:
  - 'lora'
  - 'winbox'
source: https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/step-by-step-installation
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

### LoRa 卡安裝 {#lora-card-installation}

本節將以 LtAP LTE kit 為例。

開啟路由器外殼。具體到 LtAP，卸下所有螺絲後，請小心地將上蓋移到左側，因為 LTE 天線連線在其內側：

![1.png](/img/e6edfdc7248e1ed2.webp)

將 R11e-LoRa 卡插入 mini-PCIe 插槽，並將兩顆螺絲擰入螺紋嵌件：

![](/img/3216d372cb58a8f1.webp)

將天線連線到卡上（UFL 聯結器）。在此情況下還使用了 UFL → SMA 線纜，因為 LtAP 的外殼為其預留了專用插槽。

![](/img/05f26ab703eb8d36.webp)

完成上述步驟後，即可合上路由器外殼並繼續進行配置。

### 配置 {#configuration}

#### GUI 設定 {#gui-setup}

透過 Winbox 或 WebFig 連線到路由器。

Winbox 可從[連結](https://mikrotik.com/download/winbox)下載。

執行它：

![](/img/b7d80526b099c3a2.webp)

強烈建議將 RouterOS 版本升級到最新可用版本。安裝該版本將執行重啟：

![](/img/64b1cc1f682aa7fd.webp)

如果您的裝置沒有 **IoT>LoRa** 選單，請下載專門適用於您路由器架構和 rOS 版本的“**Extra packages**”。您可以在 Winbox 視窗頂部或 System →  Resources → Architecture Name 中檢視路由器架構型別。
[https://mikrotik.com/download](https://mikrotik.com/download)
![](/img/7decbeb5ac631167.webp)

下載並解壓軟體包後，將 **IoT** 軟體包上傳到路由器。也可以透過拖放完成。上傳完成後，它應出現在檔案目錄中。重啟路由器（System → Reboot）以安裝該軟體包：
![](/img/c32844e13e18cf6c.webp)

重啟後，該軟體包應顯示在軟體包列表中：
![](/img/ce2d0ed5613a49ce.webp)

在 **IoT>LoRa>Devices** 下檢查 LoRa 閘道器是否已初始化。如果它是 LtAP 型號，請確保將 USB Type 設定為 Mini-PCIe：
![](/img/d9b29f2a829113c8.webp)

一旦網關出現（在 **IoT>LoRa>Devices** 下），請選擇它，從預設伺服器中選擇 Network Servers，或新增自己的伺服器（在 **IoT>LoRa>Servers** 下），然後啟用它：
![](/img/fe16df773e7591ff.webp)

轉到 Traffic 標籤頁，以監控周圍節點發送請求：
![](/img/399073389e674daf.webp)

以上是 LoRa mini-PCIe 卡的基本安裝和配置。如需更多設定，請檢視：[常規屬性](../general-properties.md)
