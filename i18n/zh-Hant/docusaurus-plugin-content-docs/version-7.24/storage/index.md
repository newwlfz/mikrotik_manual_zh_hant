---
sidebar_key: "storage/index"
sidebar_position: 13
title: "儲存"
sidebar_label: "儲存"
description: "本頁介紹 RouterOS 儲存功能，包括磁碟加密、RAID 配置、Btrfs/XFS 檔案系統、iSCSI 和 NFS 等網路協定、透過 DLNA 進行媒體共享、使用 rsync 進行檔案同步，以及 ROSE 軟體包增強功能，可在多個平臺上實現企業級儲存管理。"
tags:
  - 'storage'
  - 'filesystems'
  - 'smb'
source: https://manual.mikrotik.com/docs/7.24/storage
captured_at: '2026-11-04T11:32:50+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本節介紹 RouterOS 的儲存功能：磁碟級選項（加密、RAID、Btrfs 等檔案系統）、網路儲存協定（iSCSI、NFS、SMB、NVMe over TCP）、媒體共享（DLNA）以及檔案同步（rsync）。

<DocCardList />

:::info

雖然支援普通硬碟，但為保證可靠性，我們建議使用具有斷電保護（PLP）功能的硬碟。

:::

**ROSE（RouterOS Enterprise）** 軟體包為 RouterOS 增加了資料中心功能——支援磁碟監控、使用 BTRFS 和 XFS 檔案系統的改進格式化、RAID、rsync、iSCSI、NVMe over TCP、NFS 以及 SMB 用戶端。此功能目前支援 **arm、arm64、x86** 和 **tile** 平臺。

內建的 SMB **伺服器**和 DLNA 媒體伺服器屬於基礎系統的一部分，不需要 ROSE 軟體包——請參閱 [SMB](./smb.md) 和 [DLNA 媒體伺服器](./dlna.md) 頁面。
