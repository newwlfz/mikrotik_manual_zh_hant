---
sidebar_key: "storage/nfs"
sidebar_position: 5
title: "NFS"
sidebar_label: "NFS"
description: "NFS 使 RouterOS 能夠使用 NFS v4 進行網路目錄共享，需要 Storage 軟體包。它使用埠 2049，幷包含 nfs-address、nfs-share 和 nfs-sharing 等配置屬性。示例配置展示了在主機裝置上啟用 NFS，以及從 Linux 用戶端掛載 NFS 共享。"
tags:
  - 'nfs'
  - 'storage'
source: https://manual.mikrotik.com/docs/7.24/storage/nfs
captured_at: '2026-11-04T11:33:03+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

:::info
此功能需要 [儲存](./index.md) 軟體包。
:::

NFS 允許透過網路共享本地目錄。RouterOS 目前僅支援 NFS v4 模式。

:::warning

NFS 使用 TCP/2049 埠。如果該埠不可用，在 `disk print detail` 中你會看到狀態一直停留在 `nfs-state="mounting"`。

:::

## 屬性 {#properties}

| 屬性 | 描述 |
| :-- | :-- |
| **nfs-address** | NFS 目標的 IP 地址。（主機裝置 IP） |
| **nfs-share** | 指定要掛載的資料夾（用戶端引數） |
| **nfs-sharing** | 在主機裝置上停用/啟用 NFS |

## 配置示例 {#configuration-example}

主機

```ros
/disk
set pcie1-nvme1 nfs-sharing=yes
```

用戶端

```ros
/disk
add type=nfs nfs-address=192.168.1.1
```

Linux 用戶端

```bash
mkdir /mnt/files
mount -t nfs 192.168.1.1:/ /mnt/files
```
