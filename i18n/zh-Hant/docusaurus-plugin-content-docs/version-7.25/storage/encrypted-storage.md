---
sidebar_key: "storage/encrypted-storage"
sidebar_position: 3
title: "加密儲存（dm-crypt）"
sidebar_label: "加密儲存"
description: "加密儲存（dm-crypt）可為 RouterOS 中的塊裝置啟用透明磁碟加密，並透過 type=crypted 和加密金鑰進行配置。示例展示了在 USB 驅動器上或在 RAID1 陣列之上建立加密檔案系統。"
tags:
  - 'dm-crypt'
  - 'encryption'
  - 'storage'
source: https://manual.mikrotik.com/docs/7.25/storage/encrypted-storage
captured_at: '2026-11-04T11:21:25+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

:::info
此功能需要 [儲存](./index.md) 軟體包。
:::

RouterOS 支援使用 `dm-crypt` 進行透明的塊裝置加密。新增一個 `type=crypted` 的磁碟項，並將 `crypted-backend` 指向要加密的驅動器或分割區；解密透過 `encryption-key` 完成。

## 示例 {#examples}

### 簡單的加密檔案系統 {#simple-crypted-file-system}

建立加密檔案系統：

```ros
/disk/add crypted-backend=usb1 encryption-key=<secret_key> slot=crypted-usb1 type=crypted
```

建立完成後，格式化檔案系統即可使用：

```ros
/disk/format crypted-usb1 file-system=ext4
```

### 帶完整性檢查的加密 RAID1 陣列 {#crypted-raid1-array-with-integrity-check}

建立 RAID1 陣列並在其上放置加密檔案系統：

```routeros
/disk/add raid-device-count=2 raid-type=1 slot=raid1 type=raid
/disk/set nvme3 raid-master=raid1 raid-role=0
/disk/set nvme4 raid-master=raid1 raid-role=1
/disk/add crypted-backend=raid1 encryption-key=<secret_key> slot=crypted-raid1 type=crypted
```

將加密裝置格式化為 Btrfs：

```routeros
/disk/format crypted-raid1 file-system=btrfs
```
