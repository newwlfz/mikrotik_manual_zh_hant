---
sidebar_key: "getting-started/installation-and-upgrade/netinstall/index"
sidebar_position: 2
title: "網路安裝"
sidebar_label: "網路安裝"
description: "本頁介紹 Netinstall——用於安裝和重新安裝 RouterOS 的 MikroTik 工具，幫助在 Windows、Linux 和 Netinstall 軟體包方法之間進行選擇，並描述使用 Etherboot 模式的常見裝置安裝工作流程。"
tags:
  - 'netinstall'
source: https://manual.mikrotik.com/docs/7.25/getting-started/installation-and-upgrade/netinstall
captured_at: '2026-11-04T11:16:33+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Netinstall 是一個用於在 MikroTik 裝置上安裝和重新安裝 RouterOS 的實用工具。它可用於恢復無法訪問的裝置、執行全新安裝，或在系統損壞或配置錯誤時重新安裝 RouterOS。

該工具提供 Windows 版本（圖形介面）和 Linux 版本（命令列）。從 RouterOS 7.24beta1 開始，除 SMIPS 裝置外，所有 MikroTik 架構均提供 **Netinstall 軟體包**。

## 選擇 Netinstall 方法 {#choose-a-netinstall-method}

選擇與你的環境相匹配的安裝方法：

- [Windows 版 Netinstall](./netinstall-windows.md) - 適用於 Windows 系統的圖形介面。
- [Linux 版 Netinstall](./netinstall-linux.md) - 適用於 Linux 系統的命令列工具。
- [**Netinstall 軟體包**](./netinstall-package.md) - 可直接在受支援的 MikroTik 裝置上啟用 Netinstall 功能的 RouterOS 軟體包。

你可以從 [MikroTik 下載](https://mikrotik.com/download)頁面下載 Netinstall 工具和 RouterOS 軟體包。

:::danger
Netinstall 會重新格式化系統驅動器，這會清除所有配置資料和使用者檔案。

Netinstall 不會移除 RouterOS 許可證金鑰，也不會重設 RouterBOOT 設定。例如，重新安裝期間 CPU 頻率保持不變。
:::

## 使用 Netinstall 的裝置安裝工作流程 {#device-installation-workflow-using-netinstall}

以下工作流程適用於所有 Netinstall 方法。

### 準備 Netinstall 主機 {#prepare-the-netinstall-host}

在與待重灌裝置連線到同一二層（L2）網段的計算機或 MikroTik 路由器上啟動 Netinstall。為獲得最佳效果，請使用專用網路介面以及簡單的交換器或集線器，以避免 IP、DHCP 或 BOOTP 衝突。

### 將裝置啟動到 Etherboot 模式 {#boot-the-device-into-etherboot-mode}

Etherboot 模式是 MikroTik 裝置上的一種特殊啟動狀態，允許你使用 Netinstall 重新安裝 RouterOS。

有兩種 booter 選項可用：**常規 Booter** 和**備份 Booter**。建議同時驗證這兩種選項，以防其中一種無法使用。

- **常規 Booter：** 要透過序列控制檯進入 etherboot 模式，請按住 <kbd>Control</kbd>+<kbd>E</kbd>。或者，在裝置通電後等待 1–2 秒再按下 **Reset** 按鈕。

- **Backup Booter:** 關閉裝置。按住 **Reset** 按鈕，然後給裝置上電。等待 **LED** 序列（閃爍 → 常亮 → 熄滅），然後鬆開按鈕。裝置將啟動進入 **BOOTP** 模式，可透過 Netinstall 重新安裝 RouterOS。視型號而定，這可能由 **USR, USER, System** 或 **ACT** LED 指示，或由 SFP 埠 LED 指示。

### 安裝裝置 {#install-the-device}

使用 Netinstall 安裝 RouterOS，並配置所需的軟體包、引數和配置指令碼。

## 其他參考 {#additional-references}

- [RouterOS 配置管理](../../configuration-management/index.md)
- [RouterOS 軟體包](../packages.md)
- [RouterBOOT 配置](../routerboot.md)
- [MikroTik 下載](https://mikrotik.com/download)
