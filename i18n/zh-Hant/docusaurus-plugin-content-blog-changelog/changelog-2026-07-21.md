---
title: "文件更新 - 2026年7月21日"
date: 2026-07-21
slug: /changelog-2026-07-21
source: https://manual.mikrotik.com/changelog/changelog-2026-07-21
captured_at: '2026-11-04T06:08:16+08:00'
tags:
  - label: "Documentation changelog"
    permalink: changelog
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

2026 年 7 月 21 日文件變更摘要。

## 入門 {#getting-started}

- **[CHR 和 x86 許可](/docs/getting-started/routeros-licensing/chr/chr-licensing)**：記錄了 CHR 和 x86 許可證的賬戶繫結、試用到期以及許可證轉移行為。

## 硬體 {#hardware}

- **[磁碟](/docs/hardware/disks)**：記錄了 USB 連線驅動器上 SED 與 FSTRIM 的限制，澄清了基於容器的 swap 行為，更正了磁碟 trim 的描述，並新增了 swap 最大大小限制。
- **[RouterBOARD](/docs/hardware/routerboard)**：交叉引用了 resource print 所顯示的新的 minimum-firmware 和 minimum-version 欄位。

## 診斷與監控 {#diagnostics--monitoring}

- **[Resource](/docs/diagnostics-monitoring-and-troubleshooting/resource)**：記錄了 resource print 所顯示的 minimum-firmware 和 minimum-version 欄位。

## 儲存 {#storage}

- **[自加密驅動器](/docs/storage/self-encrypting-drives)**：說明了當 SED 位於 USB 橋接器之後時的一項 FSTRIM 限制。
- **[RAID](/docs/storage/raid)**：記錄了 /disk raid-scrub-cancel 命令。

## 容器 {#containers}

- **[容器應用](/docs/containers/apps)**：記錄瞭如何選擇容器應用所使用的 Web 埠。
