---
sidebar_key: "storage/encrypted-storage"
sidebar_position: 3
title: "加密儲存（dm-crypt）"
sidebar_label: "加密儲存"
description: "加密儲存（dm-crypt）使用 `dm_crypt` 為塊裝置提供透明磁碟加密，並具有 slot name、encryption key 和 backend drive 等屬性。示例展示瞭如何在 USB 或 RAID1 陣列上建立加密檔案系統，並附有格式化說明。"
tags:
  - 'dm-crypt'
  - 'encryption'
  - 'storage'
source: https://manual.mikrotik.com/docs/7.24/storage/encrypted-storage
captured_at: '2026-11-04T11:33:05+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

:::info
此功能需要 [儲存](./index.md) 軟體包。
:::

與 `type=crypted` 配合使用的驅動器或裝置，用於建立 `dm_crypt` 加密儲存。`dm-crypt` 是一種透明磁碟加密子系統，用於為塊裝置提供加密。

## 屬性 {#properties}

| 屬性 | 描述 |
| :-- | :-- |
| **slot** *(string;* Default: ) | 檔案系統的名稱 |
| **encryption-key** *(string;* Default: ) | 用於解密的金鑰 |
| **crypted-backend** *(string;* Default: ) | 要加密的驅動器或分割區 |

## 示例 {#examples}

### 簡單的加密檔案系統 {#simple-crypted-file-system}

建立加密檔案系統：

```ros
/disk
add crypted-backend=usb1 encryption-key=<secret_key> slot=crypted-usb1 type=crypted
```

建立完成後，格式化檔案系統即可使用。

```ros
/disk/format crypted-usb1 file-system=ext4 
```

### 帶完整性檢查的加密 RAID1 陣列 {#crypted-raid1-array-with-integrity-check}

建立 RAID1 陣列，並在其上建立加密檔案系統：

```routeros
/disk
add raid-device-count=2 raid-type=1 slot=raid1 type=raid
set nvme3 raid-master=raid1 raid-role=0
set nvme4 raid-master=raid1 raid-role=1
add crypted-backend=raid1 encryption-key=<secret_key> slot=crypted-raid1 type=crypted  crypt-mode=encryption-and-integrity

```

將加密檔案系統格式化為 Btrfs：

```routeros
/disk
 format crypted-raid1 file-system=btrfs  
```
