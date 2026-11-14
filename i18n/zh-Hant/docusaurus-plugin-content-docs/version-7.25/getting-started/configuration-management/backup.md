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
source: https://manual.mikrotik.com/docs/7.25/getting-started/configuration-management/backup
captured_at: '2026-11-04T11:16:05+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

RouterOS 備份功能允許將路由器配置儲存為二進位制格式檔案，之後可在同一裝置上重新應用。系統的備份檔案還包含裝置的 MAC 地址，載入備份檔案時會恢復這些地址。

應在相同版本的 RouterOS 上恢復備份。

如果路由器上安裝了 The Dude 或 User-manager，系統備份不包含這些服務的配置。請使用提供的工具機制來儲存和匯出這些服務的配置。

:::warning
系統備份包含有關裝置及其配置的[敏感資訊](./list-of-menus-with-sensitive-parameters.md)；始終考慮加密備份檔案並將備份檔案儲存在安全位置。
:::

## 儲存備份 {#saving-a-backup}

備份檔案透過執行 `/system/backup/save` 命令生成。引數說明請參閱 [CLI 參考](../../cli-reference/system/backup/save.md)。

生成的備份檔案位於 [`/file`](../../cli-reference/file/index.md) 選單中，可以使用 FTP 或其他管理工具下載。

:::danger
如果在低於 v6.43 的 RouterOS 版本中未提供密碼，則備份檔案會使用當前使用者的密碼加密，除非使用了 *dont-encrypt* 屬性或當前使用者的密碼為空。
:::

## 載入備份 {#loading-a-backup}

備份檔案透過執行 `/system/backup/load` 命令載入。引數說明請參閱 [CLI 參考](../../cli-reference/system/backup/load.md)。

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

你可以將裝置的備份檔案安全地儲存在 MikroTik 的雲伺服器上。更多詳情請參閱 [雲備份](../../network-management/cloud/cloud-backup.md)。
