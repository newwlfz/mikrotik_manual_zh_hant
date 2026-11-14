---
sidebar_key: "getting-started/index"
sidebar_position: 12
title: "入門"
sidebar_label: "入門"
description: "入門指南\"提供了 RouterOS 初始設定的基本說明，包括連線方法、管理介面訪問以及將 MikroTik 路由器投入服務所需的基本安全任務。"
tags:
  - 'first-time-configuration'
source: https://manual.mikrotik.com/docs/7.25/getting-started
captured_at: '2026-11-04T11:16:05+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

入門部分涵蓋 RouterOS 的初始設定、配置管理、安裝、授權、升級、備份以及首次安全設定任務。使用本節可將路由器投入執行並維護基礎系統。

## 快速入門：連線到路由器 {#quickstart-connect-to-your-router}

如果你剛剛拆開 MikroTik 裝置的包裝，並希望訪問其管理介面：

1. 將一根乙太網線從你的計算機連線到路由器上 **除** `ether1` 之外的任意埠。
2. 接通電源。等待大約一分鐘，讓裝置完成啟動。
3. 使用以下任意方式訪問管理介面：
   - 使用瀏覽器訪問 **`http://192.168.88.1`**（WebFig）
   - **[WinBox](https://mikrotik.com/download)**——適用於 Windows、macOS 和 Linux 的桌面 GUI
   - **MikroTik 移動應用**（iOS / Android）
4. 使用裝置專用密碼，以使用者 **`admin`** 登入；該密碼印在**路由器上的貼紙**上（也印在其包裝盒上）。

你已經進入。當準備實際配置網際網路訪問、Wi-Fi、防火牆規則等時，請遵循完整的[首次配置](./first-time-configuration.md)指南。

<DocCardList />
