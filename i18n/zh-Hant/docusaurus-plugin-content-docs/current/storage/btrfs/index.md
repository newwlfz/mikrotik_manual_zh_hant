---
sidebar_key: "storage/btrfs"
title: "Btrfs"
sidebar_label: "Btrfs"
description: "Btrfs 是一種穩定的寫時複製檔案系統，具備位腐爛保護、子卷和快照等特性。它隨 Storage 軟體包提供，並支援 RAID 配置、子卷管理和快照傳輸。"
tags:
  - 'btrfs'
  - 'storage'
  - 'file-system'
source: https://manual.mikrotik.com/docs/storage/btrfs
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

:::info
此功能需要 [儲存](../index.md) 軟體包。
:::

Btrfs 是一種功能豐富的寫時複製檔案系統。它是某些流行 Linux 發行版（例如 [Fedora](https://en.wikipedia.org/wiki/Fedora_Linux)）的預設檔案系統，並被許多大型公司所使用。多年來，它已被證明比其他流行的檔案系統更穩定、更靈活。最重要的特性包括：

- 位衰減防護（在 Btrfs-RAID 模式下使用時）。
- 子卷。
- 快照。
- 裝置之間的快照傳輸。

## 快速開始：將磁碟格式化為 Btrfs {#quickstart-format-a-disk-as-btrfs}

將單個磁碟格式化為 Btrfs，並在預設掛載點下使用它：

```routeros
/disk/print
/disk/format <disk-name> file-system=btrfs
/disk/btrfs/filesystem/print
```

格式化完成後，該磁碟會在 `/disk/btrfs/filesystem/print` 下以新的 Btrfs 檔案系統條目出現，預設標籤為 `<disk-name>-fs`（可使用 `/disk/btrfs/filesystem/set <label> label=MyLabel` 更改標籤）。該磁碟會像其他任何驅動器一樣掛載，並可在 `/file` 中訪問。在這裡，你可以為檔案系統設定標籤、建立[子卷和快照](./snapshots.md)、將多個磁碟組合成 [Btrfs RAID](./raid.md)，或設定常規[維護](./maintenance.md)。

Btrfs 功能位於三個選單下：

- [`/disk/btrfs/filesystem`](../../cli-reference/disk/btrfs/filesystem/index.md) - 每個已格式化的 Btrfs 檔案系統對應一個條目：標籤、裝置成員關係（[`add-device`](../../cli-reference/disk/btrfs/filesystem/add-device.md)、[`remove-device`](../../cli-reference/disk/btrfs/filesystem/remove-device.md)、[`replace-device`](../../cli-reference/disk/btrfs/filesystem/replace-device.md)）、RAID 配置檔案和維護任務（[`balance-start`](../../cli-reference/disk/btrfs/filesystem/balance-start.md)、[`scrub-start`](../../cli-reference/disk/btrfs/filesystem/scrub-start.md)、[`reset-counters`](../../cli-reference/disk/btrfs/filesystem/reset-counters.md)）。
- [`/disk/btrfs/subvolume`](../../cli-reference/disk/btrfs/subvolume.md) - 檔案系統的子卷和快照。
- [`/disk/btrfs/transfer`](../../cli-reference/disk/btrfs/transfer.md) - 向其他裝置傳送快照以及從其他裝置接收快照。

## 另請參閱 {#see-also}

- [Btrfs RAID](./raid.md) - RAID1 和 RAID10 配置、磁碟更換以及 BraidHealthCheck 指令碼。
- [Btrfs 子卷和快照](./snapshots.md) - 建立子卷、建立快照、在裝置之間傳輸快照。
- [Btrfs 維護](./maintenance.md) - 定期清理、平衡、自動快照輪換以及可用空間管理。
