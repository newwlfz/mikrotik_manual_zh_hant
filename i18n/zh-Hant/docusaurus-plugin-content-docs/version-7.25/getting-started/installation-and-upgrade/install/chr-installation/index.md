---
sidebar_key: "getting-started/installation-and-upgrade/install/chr-installation/index"
sidebar_position: 6
title: "CHR：安裝"
sidebar_label: "CHR：安裝"
description: "本頁面概述了在虛擬環境中安裝和配置雲託管路由器（CHR）的相關內容，涵蓋系統要求、RAM 計算、磁碟映像格式、下載說明、虛擬機器設定以及訪問詳情。"
tags:
  - 'chr'
  - 'virtualization'
source: https://manual.mikrotik.com/docs/7.25/getting-started/installation-and-upgrade/install/chr-installation
captured_at: '2026-11-04T11:16:14+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 概述和系統要求 {#overview-and-system-requirements}

Cloud Hosted Router (CHR) 是 RouterOS 的虛擬化版本，旨在運行於 x86_64 虛擬環境。它提供與 MikroTik 硬體裝置相同的核心路由、防火牆、VPN 和管理功能。

## 主機系統要求 {#host-system-requirements}

- **CPU**：支援虛擬化的 64 位處理器
- **RAM**：256 MB 或更多
- **磁碟**：128 MB 或更多

## 容量限制 {#capacity-limits}

### RouterOS 版本 6 {#routeros-version-6}

- CHR 虛擬硬碟最大大小：16 GB

### RouterOS 版本 7 {#routeros-version-7}

- 最大 RAM 和磁碟空間受 Linux 核心 5.6.3 限制，並取決於具體硬體。

## 計算最低 RAM 要求 {#calculating-minimum-ram-requirements}

最低所需 RAM 取決於您的 CPU 數量和介面數量。使用下方適當的公式計算近似值：

- **RouterOS v6**:
  
  `RAM = 128 + [ 8 × (CPU_COUNT) × (INTERFACE_COUNT - 1) ]`

- **RouterOS v7**:
  
  `RAM = 512 + [ 8 × (CPU_COUNT) × (INTERFACE_COUNT - 1) ]`

**建議**：對於 CHR 例項，至少分配 1024 MiB RAM。

## 軟體要求 {#software-requirements}

- **軟體包版本**：RouterOS v6.34 或更高版本

## 可用的磁碟映像格式 {#available-disk-image-formats}

- **RAW 磁碟映像**：`.img` 檔案
- **VirtualBox 磁碟映像**：`.vdi` 檔案
- **VMware 磁碟映像**：`.vmdk` 檔案
- **Hyper-V 磁碟映像**：`.vhdx` 檔案
- **OVA 裝置**：`.ova` 檔案

:::warning
這些僅是磁碟映像，必須掛載到虛擬機器。
:::

## 下載 CHR 映像 {#download-the-chr-image}

1. 前往 [MikroTik 下載頁面](https://mikrotik.com/download/chr) 的 Cloud Hosted Router 部分。
2. 選擇適用於您平臺的映像格式。
3. 下載檔案。

## 建立並配置虛擬機器 {#create-and-configure-a-virtual-machine}

1. 在您的虛擬機器監控程式中建立新虛擬機器。
2. 將 CHR 磁碟映像作為系統磁碟掛載。
3. 啟動虛擬機器。

### 虛擬網路介面卡 {#virtual-network-adapters}

:::info
**Fast Path 支援**

- RouterOS v7：**vmxnet3** 和 **virtio-net** 介面支援 Fast Path。
- RouterOS v6：不支援 Fast Path。

:::

## 訪問 CHR {#access-chr}

- 使用者名稱：`admin`
- 密碼：無（應在首次登入後立即設定強密碼）

首次啟動後，CHR 預設執行在 Free 許可證下。要啟用試用版或升級，請使用 `/system/license/renew`。

## 特定平臺指南 {#platform-specific-guides}

### 支援的虛擬化平臺 {#supported-virtualization-platforms}

- [CHR：VMware ESXi 安裝](./esxi.md)
- VMware Fusion
- [Proxmox VE (KVM/QEMU)](./proxmox.md)
- [CHR：Hyper-V 安裝](./hyperv.md)
- [VirtualBox](./virtualbox.md)
- Xen Server

:::warning
CHR 無法在 **bhyve** 虛擬機器監控程式上執行。CHR 不支援半虛擬化平臺。
:::

> **注意：** 使用 Hyper-V 時僅支援第 1 代虛擬機器。

> **重要：** 任何虛擬機器監控程式都不支援半虛擬化。

### 支援的雲平臺 {#supported-cloud-platforms}

- Amazon Web Services (AWS)
- Google Cloud Platform (GCP)
- [CHR：Hetzner Cloud 安裝](./hetzner.md)
- Linode
- Microsoft Azure
- [Vultr](./vultr.md)
