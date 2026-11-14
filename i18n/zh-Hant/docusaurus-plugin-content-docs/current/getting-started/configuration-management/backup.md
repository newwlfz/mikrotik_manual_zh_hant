---
sidebar_key: "getting-started/configuration-management/backup"
sidebar_position: 1
title: "備份"
sidebar_label: "備份"
description: "將 RouterOS 配置儲存到二進位制檔案，對其進行加密，並在之後於同一裝置上恢復。"
tags:
  - 'backup'
  - 'system-configuration'
  - 'encryption'
source: https://manual.mikrotik.com/docs/getting-started/configuration-management/backup
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

系統備份會將整個路由器配置儲存到單個二進位制檔案中。在進行有風險的更改之前儲存備份，例如在升級前或進行一批防火牆修改前，並在配置損壞時恢復它。對於可能中斷連線的更改，或你計劃撤銷的更改，[安全模式](./index.md#safe-mode)和[撤銷/重做](./index.md#configuration-undo-and-redo)是更輕量的替代方案。

備份只有在建立它的裝置上才能可靠恢復。備份包含裝置的 MAC 地址，因此在另一臺裝置上恢復可能會導致介面配置錯誤。要在裝置之間複製配置，請改用 [export 和 import](./index.md#configuration-export)。

:::warning
備份包含敏感引數，例如密碼和金鑰；請參閱[包含敏感引數的選單列表](./list-of-menus-with-sensitive-parameters.md)。未設定密碼儲存的備份會以可讀形式儲存配置。請加密備份並將其儲存在安全的地方。
:::

## 儲存備份 {#save-a-backup}

將配置儲存到備份檔案：

```ros
[admin@MikroTik] > /system/backup/save name=config-before-update password=StrongPass
Configuration backup saved
```

該命令會在 [`/file`](../../cli-reference/file/index.md) 選單中建立檔案 `config-before-update.backup`：

```ros
[admin@MikroTik] > /file/print where name~"config-before-update"
Columns: NAME, TYPE, SIZE, LAST-MODIFIED
# NAME                         TYPE    SIZE     LAST-MODIFIED      
0 config-before-update.backup  backup  35.8KiB  2026-10-16 07:15:38
```

將副本儲存在路由器之外，例如使用 [WinBox 或 FTP](../../system-information-and-utilities/files.md) 下載該檔案。要定期建立備份，請新增一個執行 save 命令的 scheduler 條目；請參閱 [scheduler 示例](../../system-information-and-utilities/scheduler.md)。

提供 `password` 以加密備份檔案。如果沒有密碼，備份將以未加密形式儲存。`encryption` 選擇演算法：預設使用 `aes-sha256`，或使用 `rc4` 以相容較舊的 RouterOS 版本。即使提供了密碼，`dont-encrypt=yes` 也會以未加密形式儲存備份。

## 恢復備份 {#restore-a-backup}

使用與 `save` 時相同的備份名稱，不帶 `.backup` 副檔名。載入備份檔案並確認重啟：

```ros
[admin@MikroTik] > /system/backup/load name=config-before-update password=StrongPass
Restore and reboot? [y/N]: y
Restoring system configuration
System configuration restored, rebooting now
```

路由器會以恢復後的配置重啟。回答 `n` 可取消恢復。省略 `password` 時，RouterOS 會詢問密碼；對於未加密的備份，任意密碼均可使用。

:::note
請在建立備份所用的同一 RouterOS 版本上恢復備份。要載入在 RouterOS v6 上建立的備份，請新增 `force-v6-to-v7-configuration-upgrade=yes`。
:::

## 備份不包含的內容 {#what-the-backup-does-not-contain}

系統備份不包含 [The Dude](../../management-tools/dude.md) 或 [使用者管理器](../../authentication-authorization-accounting/user-manager.md#database) 的資料庫。兩者都在裝置上單獨儲存各自的資料，因此請使用它們各自的備份機制來儲存這些資料庫。

## 雲備份 {#cloud-backup}

將備份的加密副本儲存在 MikroTik 雲伺服器上，稍後將其下載到同一裝置或替換裝置。請參閱 [雲備份](../../network-management/cloud/cloud-backup.md)。

## 故障排除 {#troubleshoot}

- 恢復會失敗並顯示 `failure: bad password`。密碼與使用 `save` 時所使用的密碼不匹配；錯誤密碼會在恢復期間、確認之後報告。
- 執行 `load` 時未提供 `password` 引數的指令碼會失敗並顯示 `missing value(s) of argument(s) password`。請將密碼作為引數傳入；指令碼中無法使用互動式提示。
