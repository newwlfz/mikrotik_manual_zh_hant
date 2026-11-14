---
sidebar_key: "storage/ramdisk"
sidebar_position: 8
title: "記憶體盤"
sidebar_label: "記憶體盤"
description: "RAMdisk 允許將 RAM 用作儲存塊裝置，支援 RAID 配置，並且需要 Storage 軟體包。它會在重啟或斷電時被清除，可透過 ramdisk-size 屬性配置大小。"
tags:
  - 'storage'
  - 'ramdisk'
source: https://manual.mikrotik.com/docs/7.24/storage/ramdisk
captured_at: '2026-11-04T11:33:10+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

:::info
此功能需要 [儲存](./index.md) 軟體包。
:::

RAMdisk 允許將部分 RAM 用作附加裝置（塊裝置）。與 tmpfs 相比，這允許將 RAM 用作 RAID 的一部分，或用於任何其他需要裝置（而非資料夾）的配置。

:::warning

RAMdisk 在重啟或斷電時會被清除。

:::

## 屬性 {#properties}

| 屬性 | 描述 |
| :-- | :-- |
| **ramdisk-size** | 要建立的塊裝置大小 |

## 配置示例 {#configuration-example}

```ros
/disk/add type=ramdisk ramdisk-size=500M
```

使用前請先格式化 ramdisk：

```routeros
/disk/format ramdisk1
```
