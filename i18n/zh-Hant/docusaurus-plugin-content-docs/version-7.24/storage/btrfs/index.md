---
sidebar_key: "storage/btrfs/index"
sidebar_position: 1
title: "Btrfs"
sidebar_label: "Btrfs"
description: "Btrfs 是一種穩定的寫時複製檔案系統，具有 bitrot 防護、子卷和快照等特性。它在 RouterOS v7.18beta2+ 中透過 Storage 軟體包提供，並支援 RAID 配置、子卷管理和快照傳輸。"
tags:
  - 'btrfs'
  - 'storage'
  - 'file-system'
source: https://manual.mikrotik.com/docs/7.24/storage/btrfs
captured_at: '2026-11-04T11:32:56+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

:::info
Btrfs 頁面上描述的功能從 RouterOS v7.18beta2 開始可用，並且需要 [儲存](../index.md) 軟體包。
:::

Btrfs 是一種功能豐富的寫時複製檔案系統，自 2007 年就已存在。它是一些流行 Linux 發行版（如 [Fedora](https://en.wikipedia.org/wiki/Fedora_Linux)）的預設檔案系統，並被許多大型公司（如 [Meta](https://en.wikipedia.org/wiki/Meta_Platforms)）在其資料中心中使用。多年來，它已證明自身穩定且比其他流行檔案系統更靈活。最重要的特性包括：

- 位衰減保護（在 Btrfs-RAID 模式下使用時）。
- 子卷。
- 快照。
- 傳輸。

## 快速開始：將磁碟格式化為 Btrfs {#quickstart-format-a-disk-as-btrfs}

將單個磁碟格式化為 Btrfs，並在預設掛載點下訪問它：

```routeros
/disk/print
/disk/format <disk-name> file-system=btrfs
/disk/btrfs/filesystem/print
```

格式化後，該磁碟會以 Btrfs 檔案系統條目的形式出現在 `/disk/btrfs/filesystem/print` 下。從這裡你可以為其新增標籤、配置子卷/快照，或將多個磁碟組合成 Btrfs RAID。

## 另請參閱 {#see-also}

- [Btrfs RAID](./raid.md) — RAID1 和 RAID10 配置、磁碟更換以及 BraidHealthCheck 指令碼。
- [Btrfs 子卷和快照](./snapshots.md) — 建立子卷、拍攝快照、在裝置之間傳輸快照。
- [Btrfs 維護](./maintenance.md) — 定期清理、均衡、自動快照輪換以及可用空間管理。
