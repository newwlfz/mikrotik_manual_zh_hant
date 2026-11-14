---
title: "文件更新 - 2026年5月28日"
date: 2026-05-28
slug: /changelog-2026-05-28
source: https://manual.mikrotik.com/changelog/changelog-2026-05-28
captured_at: '2026-11-04T06:07:47+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026年5月28日文件變更摘要。

## 入門 {#getting-started}

- **[入門](/docs/getting-started)**：在落地頁新增了 Quickstart 區塊，列出訪問新路由器管理介面的四個步驟（瀏覽器訪問 192.168.88.1、WinBox 或 MikroTik 移動應用）。並說明管理員密碼現在印在路由器上的貼紙上，不再是空密碼。First Time Configuration 現已置頂於該章節。

## 儲存 {#storage}

- **[儲存](/docs/storage)**：儲存現在是獨立的頂級文件章節。此前分散在 Extended Features 下的內容被重組為單獨的頁面：iSCSI、NFS、NVMe over TCP、SMB（服務端和用戶端）、RAID、加密儲存、rsync、ramdisk、tmpfs、自加密硬碟和 DLNA。舊 URL 透過重定向保留，因此現有連結仍可繼續使用。
- **[Btrfs](/docs/storage/btrfs)**：860 行的 Btrfs 單篇長文已拆分為四個專題頁面：[概述](/docs/storage/btrfs)（簡介、特性、快速開始）、[RAID](/docs/storage/btrfs/raid)（RAID1、RAID10、裝置更換、健康檢查指令碼）、[快照](/docs/storage/btrfs/snapshots)（子卷、快照、傳輸）和[維護](/docs/storage/btrfs/maintenance)（定期 scrubbing、balance、快照輪換、可用空間管理）。

## 容器 {#containers}

- **[容器](/docs/containers)**：容器現在是頂級章節（此前巢狀在 Extended Features 下）。各應用的示例指南——FreeRADIUS、HAProxy、Home Assistant、Matrix Synapse、Mosquitto、Postgres、Thingsboard——已歸入新的 Examples 子章節，頂級選單僅保留 Apps、VETH 和 Examples。

## 硬體 {#hardware}

- **[S.M.A.R.T.](/docs/hardware/disks/smart)**：S.M.A.R.T. 磁碟健康監控文件已從 Storage 移至 Hardware/Disks，與其他磁碟相關內容放在一起。
