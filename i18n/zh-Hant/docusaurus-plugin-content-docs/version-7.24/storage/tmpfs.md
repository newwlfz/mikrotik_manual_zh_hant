---
sidebar_key: "storage/tmpfs"
sidebar_position: 12
title: "臨時檔案系統（Tmpfs）"
sidebar_label: "臨時檔案系統"
description: "Tmpfs 允許將 RAM 用作檔案系統，最大大小可配置，但在重啟或斷電後會被清除。"
tags:
  - 'storage'
  - 'tmpfs'
source: https://manual.mikrotik.com/docs/7.24/storage/tmpfs
captured_at: '2026-11-04T11:33:20+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

:::info
此功能需要 [儲存](./index.md) 軟體包。
:::

Tmpfs 允許將一部分 RAM 用作檔案系統。它不能用作塊裝置。

:::warning

tmpfs 在重啟或斷電後會被清除。

:::

## 屬性 {#properties}

| 屬性 | 描述 |
| :-- | :-- |
| **tmpfs-max-size** | tmpfs 檔案系統的最大大小 |

## 配置示例 {#configuration-example}

```ros
add type=tmpfs tmpfs-max-size=10G
```
