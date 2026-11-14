---
sidebar_key: "storage/ramdisk"
sidebar_position: 8
title: "記憶體盤"
sidebar_label: "記憶體盤"
description: "ramdisk 是 RAM 中的塊裝置。使用前請先格式化，或將其用作 RAID 成員。它需要 rose-storage 軟體包，並且每次重啟後都是空的。"
tags:
  - 'storage'
  - 'ramdisk'
source: https://manual.mikrotik.com/docs/7.25/storage/ramdisk
captured_at: '2026-11-04T11:21:42+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

RAM 磁碟是位於 RAM 中的塊裝置。與磁碟一樣，它需要先有檔案系統才能存放檔案，並且可以作為 RAID 的成員，或在任何需要裝置的地方使用。[tmpfs](./tmpfs.md) 則是位於 RAM 中的資料夾：它無需格式化即可存放檔案，但它不是裝置，不能格式化，也不能作為 RAID 成員。

:::info
Ramdisk 需要 `rose-storage` 軟體包（參見 [儲存](./index.md)）。要安裝路由器上可用的該軟體包，請啟用它並應用更改。應用更改會重啟路由器：

```ros
/system/package/enable rose-storage
/system/package/apply-changes
```

有關軟體包的更多資訊，請參見[軟體包](../getting-started/installation-and-upgrade/packages.md)。
:::

## 建立並格式化 RAM 磁碟 {#create-and-format-a-ramdisk}

新增一個 500 MB 的 RAM 磁碟：

```ros
/disk/add type=ramdisk ramdisk-size=500M
```

第一個 RAM 磁盤獲得槽位名稱 `ramdisk1`，後續的依次為 `ramdisk2`、`ramdisk3`，以此類推。大小會向上取整為 16 KiB 的倍數。新增 RAM 磁碟時，路由器不會預留 RAM。

使用前請先格式化 RAM 磁碟：

```ros
/disk/format ramdisk1 file-system=ext4
```

格式化後的 RAM 磁碟會掛載到其槽位名稱下，因此檔案會寫入諸如 `ramdisk1/capture.pcap` 的路徑。

:::warning
路由器重啟或斷電時，RAM 磁碟的內容會丟失。重啟後，RAM 磁碟會重新出現，但為空且沒有檔案系統，因此使用前請再次格式化。
:::

## 在 RAID 中使用 RAM 磁碟 {#use-ramdisks-in-a-raid}

RAM 磁碟可以作為 RAID 成員，例如在沒有磁碟的路由器上嘗試 RAID 配置。要用兩個 RAM 磁碟構建 RAID 1，請新增 RAID 並將兩個 RAM 磁碟都分配給它：

```ros
/disk/add type=raid raid-type=1 raid-device-count=2 slot=raid1
/disk/set ramdisk1 raid-master=raid1 raid-role=0
/disk/set ramdisk2 raid-master=raid1 raid-role=1
```

隨後 `/disk/print` 會顯示 `raid1`，其型號為 `RAID1 mirrored`，狀態為 `clean`，並且兩個 RAM 磁碟作為 RAID 成員，成員狀態為 `in_sync`。重啟後，路由器會從空的 RAM 磁碟重新組裝 RAID。有關 RAID 的更多資訊，請參見 [RAID](./raid/index.md)。

## 移除 RAM 磁碟 {#remove-a-ramdisk}

請先移除使用 RAM 磁碟的 RAID，然後移除 RAM 磁碟：

```ros
/disk/remove raid1
/disk/remove ramdisk1
/disk/remove ramdisk2
```

有關所有引數，請參見 [`/disk`](../cli-reference/disk/index.md) CLI 參考。
