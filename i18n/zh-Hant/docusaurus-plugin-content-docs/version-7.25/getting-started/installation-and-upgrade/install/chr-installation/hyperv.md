---
sidebar_key: "getting-started/installation-and-upgrade/install/chr-installation/hyperv"
sidebar_position: 4
title: "CHR：Hyper-V 安裝"
sidebar_label: "CHR：Hyper-V 安裝"
description: "本頁介紹在 Microsoft Hyper-V 上安裝 MikroTik RouterOS CHR，詳細說明支援的網路介面卡（synthetic 和 legacy）以及磁碟控制器（系統磁碟使用 IDE，輔助磁碟使用 SCSI），並附有 Hyper-V 文件的連結。"
source: https://manual.mikrotik.com/docs/7.25/getting-started/installation-and-upgrade/install/chr-installation/hyperv
captured_at: '2026-11-04T11:16:25+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 支援的網路和磁碟介面 {#supported-network-and-disk-interfaces}

### Microsoft Hyper-V {#microsoft-hyper-v}

**網路介面卡：**

- 網路介面卡（合成）
- 傳統網路介面卡

**磁碟控制器：**

- IDE
- SCSI

> **注意：** 在 Hyper-V 上，SCSI 控制器型別僅支援用於輔助磁碟。系統磁碟映像必須掛接到 IDE 控制器。

#### Hyper-V {#hyper-v}

**Hyper-V 文件：**

- https://technet.microsoft.com/en-us/library/cc816585(v=ws.10).aspx#Anchor_2
