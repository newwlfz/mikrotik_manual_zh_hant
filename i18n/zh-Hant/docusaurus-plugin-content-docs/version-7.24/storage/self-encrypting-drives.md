---
sidebar_key: "storage/self-encrypting-drives"
sidebar_position: 10
title: "自加密硬碟（SED）"
sidebar_label: "自加密硬碟"
description: "本頁介紹 MikroTik RouterOS''s 自加密硬碟（SED）支援，該功能需要 Storage 軟體包。文中說明了 Opal 合規性，列出了透過標記（o/O）標示的受支援硬碟，並提供了為 SATA 裝置設定或取消加密密碼的命令。"
source: https://manual.mikrotik.com/docs/7.24/storage/self-encrypting-drives
captured_at: '2026-11-04T11:33:14+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

:::info
此功能需要 [儲存](./index.md) 軟體包。
:::

要使用 SED，驅動器必須符合 [Opal](https://en.wikipedia.org/wiki/Opal_Storage_Specification) 規範。購買驅動器之前，請查閱驅動器製造商的文件，以確認特定驅動器是否支援此功能。

RouterOS 會為受支援的驅動器新增 **o（支援但未啟用）** 或 **O（支援且已啟用）** 標誌：

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

要設定 TCG-OPAL-SELF-ENCRYPTION：

```ros
/disk
/disk/set sata1 self-encryption-password=securepassword
```

要取消設定：

```ros
/disk
/disk/unset sata1 self-encryption-password
```

或

```ros
/disk
/disk/set sata1 !self-encryption-password

```
