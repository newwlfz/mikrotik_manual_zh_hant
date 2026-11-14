---
sidebar_key: "getting-started/routeros-licensing"
title: "RouterOS 許可證金鑰"
sidebar_label: "RouterOS 許可證金鑰"
description: "RouterOS 授權說明了 MikroTik 硬體、CHR 和 x86 系統的 Software ID 與 System ID 詳細資訊。單獨的指南涵蓋各平臺的授權具體內容以及安裝說明。"
tags:
  - 'licensing'
  - 'mikrotik-hardware'
  - 'chr'
source: https://manual.mikrotik.com/docs/getting-started/routeros-licensing
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 概述 {#overview}

RouterOS 許可基於兩個識別符號：**Software ID** 和 **System ID**。這些識別符號決定了許可證在不同平臺上如何分配和管理。

- **Software ID** 用於 MikroTik 產品（RouterBOARD）和 x86 系統。
- **System ID** 用於 Cloud Hosted Router (CHR)。

由於不同平臺的許可行為有所不同，因此針對每種情況分別提供了指南。

## 許可指南 {#licensing-guides}

### MikroTik 硬體許可 {#mikrotik-hardware-licensing}

說明許可證級別、Software ID 行為以及 MikroTik 硬體裝置的許可。

[MikroTik 硬體許可指南](./mikrotik-hardware/index.md)

### CHR 許可 {#chr-licensing}

說明基於 System ID 的許可、CHR 啟用以及虛擬環境的許可選項。

[CHR 許可指南](./chr/chr-licensing.md)

### x86 許可 {#x86-licensing}

涵蓋許可證獲取、Software ID 行為以及基於 x86 的 RouterOS 安裝的許可證級別。

[x86 許可指南](./x86/index.md)

## 安裝指南 {#installation-guides}

### MikroTik 硬體重新安裝 {#mikrotik-hardware-reinstallation}

涵蓋使用 Netinstall 進行 RouterOS 重新安裝和恢復。

[Netinstall 指南](../installation-and-upgrade/netinstall/index.md)

### x86 安裝 {#x86-installation}

涵蓋 x86 系統要求和安裝方法，包括 USB 和 Netinstall 部署。

[x86 安裝指南](../installation-and-upgrade/install/x86-installation.md)

### CHR 安裝 {#chr-installation}

涵蓋在受支援的虛擬化平臺上部署和安裝 CHR。

[CHR 安裝指南](../installation-and-upgrade/install/chr-installation/index.md)
