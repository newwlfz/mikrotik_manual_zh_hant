---
sidebar_key: "getting-started/configuration-management/backup"
sidebar_position: 1
title: "備份"
sidebar_label: "備份"
description: "RouterOS 備份功能可儲存和恢復路由器配置（包括 MAC 地址），並提供加密或未加密儲存選項。它支援將備份儲存到檔案並重新載入回同一裝置，同時對版本相容性和敏感資料處理給出了警告。"
tags:
  - 'backup'
  - 'system-configuration'
  - 'encryption'
source: https://manual.mikrotik.com/docs/7.24/getting-started/configuration-management/backup
captured_at: '2026-11-04T11:28:29+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

RouterOS 備份功能允許將路由器配置儲存為二進位制格式檔案，之後可在同一裝置上重新應用。系統的備份檔案還包含裝置的 MAC 地址，載入備份檔案時會恢復這些地址。

我們建議在相同版本的 RouterOS 上恢復備份。

:::danger
如果路由器上安裝了 The Dude 或 User-manager，則系統備份不會包含這些服務的配置，因此應額外注意儲存這些服務的配置。如果要儲存配置，請使用這些服務提供的工具機制來儲存/匯出配置。

**警告：** 系統備份包含有關裝置及其配置的敏感資訊；請始終考慮加密備份檔案，並將備份檔案儲存在安全的地方。
:::

## 儲存備份 {#saving-a-backup}

**子選單：** `/system/backup/save`

| 屬性 | 說明 |
| :-- | :-- |
| **dont-encrypt** (*yes \| no*; 預設：**no**) | 停用備份檔案加密。請注意，自 RouterOS v6.43 起，如果未提供密碼，備份檔案將不加密。 |
| **encryption** (*aes-sha256 \| rc4*; 預設：**aes-sha256**) | 用於加密備份檔案的加密演算法。請注意，`rc4` 不被視為安全的加密方法，僅出於與舊版 RouterOS 相容的原因而提供。 |
| **name** (*string*; 預設：**[identity]-[date]-[time].backup**) | 備份檔案的檔名。 |
| **password** (*string*; 預設： ) *[敏感](./list-of-menus-with-sensitive-parameters.md)* | 加密備份檔案的密碼。請注意，自 RouterOS v6.43 起，如果未提供密碼，備份檔案將不加密。 |

:::danger
在低於 v6.43 的 RouterOS 版本中，如果未提供密碼，則備份檔案將使用當前使用者的密碼加密，除非使用了 *dont-encrypt* 屬性或當前使用者的密碼為空。
:::

備份檔案將位於 `/file` 選單下，可使用 FTP 或 Winbox 下載。

## 載入備份 {#loading-a-backup}

載入無密碼的備份：

```ros
[admin@MikroTik] > /system/backup/load name=auto-before-reset.backup password=""
```

| 屬性 | 說明 |
| :-- | :-- |
| **name** (*string*; 預設： ) | 備份檔案的檔名。 |
| **password** (*string*; 預設： ) *[敏感](./list-of-menus-with-sensitive-parameters.md)* | 加密備份檔案的密碼。 |

## 示例 {#example}

要將路由器配置儲存到檔案 test 並設定密碼：

```ros
[admin@MikroTik] > /system/backup/save name=test password=<YOUR_PASSWORD> 
Configuration backup saved 
```

要檢視路由器上儲存的檔案：

```ros
[admin@MikroTik] > /file/print 
# NAME TYPE SIZE CREATION-TIME 
0 test.backup backup 12567 2018-09-08 21:07:50 
[admin@MikroTik] >
```

要載入已儲存的備份檔案 test：

```ros
[admin@MikroTik] > /system/backup/load name=test 
password: <YOUR_PASSWORD> 
Restore and reboot? [y/N]: y 
Restoring system configuration 
System configuration restored, rebooting now
```

## 雲備份 {#cloud-backup}

自 RouterOS v6.44 起，可以將裝置的備份檔案安全地儲存在 MikroTik 的雲伺服器上。有關此功能的更多資訊，請參閱 [IP/Cloud](../../network-management/cloud/index.md) 頁面。
