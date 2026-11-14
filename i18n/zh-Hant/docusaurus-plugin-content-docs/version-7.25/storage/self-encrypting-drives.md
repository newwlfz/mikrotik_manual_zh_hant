---
sidebar_key: "storage/self-encrypting-drives"
sidebar_position: 10
title: "自加密硬碟（SED）"
sidebar_label: "自加密硬碟"
description: "RouterOS 透過 TCG-Opal 標準支援自加密硬碟（SED），需要 Storage 軟體包。受支援的硬碟會在 /disk/print 中顯示 o（未啟用）/ O（已啟用）標誌，並且可以透過 self-encryption-password 啟用加密。"
source: https://manual.mikrotik.com/docs/7.25/storage/self-encrypting-drives
captured_at: '2026-11-04T11:21:45+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

:::info
此功能需要 [儲存](./index.md) 軟體包。
:::

要使用 SED，驅動器必須符合 [Opal](https://en.wikipedia.org/wiki/Opal_Storage_Specification) 規範。購買驅動器之前，請查閱驅動器製造商的文件，確認特定驅動器是否支援此功能。

在使用 USB 橋接的方案中不支援 SED；磁碟必須直接連線（SATA 或 NVMe）。

RouterOS 會用 **o（支援 TCG-OPAL，加密未啟用）** 或 **O（支援 TCG-OPAL 且加密已啟用）** 標誌標記受支援的驅動器：

```ros
/disk/print
Flags: B - BLOCK-DEVICE; M, F - FORMATTING; o - TCG-OPAL-SELF-ENCRYPTION-SUPPORTED (inactive); O - TCG-OPAL-SELF-ENCRYPTION-SUPPORTED (active)
Columns: SLOT, MODEL, SERIAL, INTERFACE, SIZE, FREE, FS, RAID-MASTER
#     SLOT   MODEL                  SERIAL           INTERFACE                   SIZE             FREE  FS    RAID
0 BMo sata1  Samsung SSD 860 2.5in  S3Z9NX0N414510L  SATA 6.0 Gbps  1 000 204 886 016  983 351 111 680  ext4  none
1 BMo sata2  Samsung SSD 860        S5GENG0N307602J  SATA 6.0 Gbps  1 000 204 886 016  983 351 128 064  ext4  none
2 BMO sata3  Samsung SSD 860        S5GENG0N307604H  SATA 6.0 Gbps  1 000 204 886 016  983 351 128 064  ext4  none
3 BMO sata4  Samsung SSD 860 2.5in  S4CSNX0N838150B  SATA 6.0 Gbps  1 000 204 886 016  983 351 128 064  ext4  none
```

要在驅動器上啟用自加密，請設定 `self-encryption-password`：

```ros
/disk/set sata1 self-encryption-password=securepassword
```

設定後，驅動器在斷電時會自行鎖定，並且每次連線時都需要密碼；RouterOS 會自動提供該密碼（標誌會變為 `O`）。

要停用自加密，請取消設定密碼：

```ros
/disk/unset sata1 self-encryption-password
```

或：

```ros
/disk/set sata1 !self-encryption-password
```
