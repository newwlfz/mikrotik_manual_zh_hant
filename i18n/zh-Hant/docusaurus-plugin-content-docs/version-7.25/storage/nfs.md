---
sidebar_key: "storage/nfs"
sidebar_position: 5
title: "NFS"
sidebar_label: "NFS"
description: "NFS 透過 NFS v4 在 RouterOS 中啟用網路目錄共享，需要 Storage 軟體包。它使用 TCP/2049 埠，並透過 /disk 的 nfs-sharing、nfs-address 和 nfs-share 引數進行配置。"
tags:
  - 'nfs'
  - 'storage'
source: https://manual.mikrotik.com/docs/7.25/storage/nfs
captured_at: '2026-11-04T11:21:33+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

:::info
此功能需要 [儲存](./index.md) 軟體包。
:::

NFS 允許透過網路共享本地目錄。RouterOS 目前僅支援 NFS v4 模式。

:::warning

NFS 使用 TCP/2049 埠。如果該埠不可用，在 `/disk print detail` 中你會看到狀態一直停留在 `nfs-state="mounting"`。
:::

## 配置示例 {#configuration-example}

主機：為已掛載的磁碟啟用 NFS 共享。

```ros
/disk/set pcie1-nvme1 nfs-sharing=yes
```

用戶端：新增一個 `type=nfs` 的裝置來掛載該共享。

```ros
/disk/add type=nfs nfs-address=192.168.1.1
```

Linux 用戶端：

```bash
mkdir /mnt/files
mount -t nfs 192.168.1.1:/ /mnt/files
```
