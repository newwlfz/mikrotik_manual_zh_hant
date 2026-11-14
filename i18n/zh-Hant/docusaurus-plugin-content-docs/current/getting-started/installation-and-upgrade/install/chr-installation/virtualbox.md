---
sidebar_key: "getting-started/installation-and-upgrade/install/chr-installation/virtualbox"
sidebar_position: 7
title: "CHR：VirtualBox 安裝"
sidebar_label: "CHR：VirtualBox 安裝"
description: "本頁提供在 VirtualBox 中安裝 MikroTik RouterOS Cloud Hosted Router (CHR) 的分步指南，涵蓋虛擬機器建立、配置以及包含登入說明的初始設定。"
tags:
  - 'virtualbox'
  - 'routeros-configuration'
  - 'network-adapters'
source: https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/install/chr-installation/virtualbox
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## CHR VirtualBox 安裝影片 {#chr-virtualbox-installation-video}

**[![](/img/b1b6f1c2752c2ba1.png)](https://www.youtube.com/watch?v=oHXkaHkSVVo)**

1. **下載 VirtualBox**  
   從官方網站安裝最新版本的 VirtualBox。

2. **下載 CHR 磁碟映象**  
   從 [MikroTik 下載頁面](https://mikrotik.com/download) 下載並解壓最新 Long-Term、Stable 或 Testing 版本的 Cloud Hosted Router (CHR) VDI 映象。

![](/img/b8bbe080282650df.png)

## 步驟 1：建立新虛擬機器 {#step-1-create-a-new-virtual-machine}

- 啟動 VirtualBox。
- 點選 **New** 建立新虛擬機器。

![](/img/72af47c1e8a1a068.png)

### 名稱和作業系統 {#name-and-operating-system}

- **Name**：輸入虛擬機器名稱（例如 MikroTik_CHR）
- **Type**：Linux
- **Version**：Other Linux (64-bit)

![](/img/093f05cdebabf23f.png)

## 步驟 2：配置記憶體大小 {#step-2-configure-memory-size}

- 至少分配 **512 MB RAM**（RouterOS 7 的最低要求）
- 分配所需的 CPU 數量

![](/img/4e95cf301fba533d.png)

## 步驟 3：新增虛擬硬碟 {#step-3-add-a-virtual-hard-disk}

- 選擇 **Use an Existing Virtual Hard Disk File**
- 選擇已下載的 `.vdi` 映象

![](/img/dd215579bb02c177.png)

點選 **Finish** 建立虛擬機器。

## 步驟 4：配置虛擬機器設定 {#step-4-configure-virtual-machine-settings}

選擇虛擬機器 → 點選 **Settings**

![](/img/0fc6a478e46dae13.png)

### 系統 {#system}

- 在啟動順序中停用 **Floppy** 和 **Optical**

![](/img/10efb5ed4436b0bf.png)

### 處理器 {#processor}

- 設定所需的 CPU 數量

### 網路 {#network}

- 網路卡 1：
  - 啟用網路介面卡
  - 連線到 **Bridged Adapter** 或 **NAT**（取決於你的環境）

![](/img/a9efaeab9a73ba15.png)

## 步驟 5：啟動虛擬機器 {#step-5-start-the-virtual-machine}

- 點選 **Start** 啟動虛擬機器

![](/img/38b5dcfb21bfadc3.png)

- 登入憑據：
  - 使用者名稱：`admin`
  - 密碼：*(空，請在首次登入後立即設定)*

![](/img/c90c90493a21cb3c.png)

## 恭喜 {#congratulations}

你已成功在 VirtualBox 上安裝 MikroTik CHR。

現在你可以使用控制檯、WinBox 或 WebFig 繼續進行 RouterOS 的初始配置。

## 支援的網路和磁碟介面 {#supported-network-and-disk-interfaces}

### 網路介面卡 {#network-adapters}

- E1000
- RTL8139
- Virtio（半虛擬化）

### 磁碟控制器 {#disk-controllers}

- IDE

> **警告：** 除非沒有更好的半虛擬化或合成選項可用，否則請避免使用 E1000 網路介面卡。在 VirtualBox 上，Virtio 能提供更好的效能。
