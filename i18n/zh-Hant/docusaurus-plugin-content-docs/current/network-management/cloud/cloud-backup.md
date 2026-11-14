---
sidebar_key: "network-management/cloud/cloud-backup"
sidebar_position: 2
title: "雲備份"
sidebar_label: "雲備份"
description: "在 MikroTik 雲伺服器上儲存一個加密的 RouterOS 備份，替換或刪除它，並使用其秘密下載金鑰在同一臺或其他路由器上下載或恢復它。"
tags:
  - 'backup'
  - 'cloud'
source: https://manual.mikrotik.com/docs/network-management/cloud/cloud-backup
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

雲備份會把路由器配置的加密[備份](../../getting-started/configuration-management/backup.md)儲存在 MikroTik 雲伺服器上。之後你可以將其下載到同一臺路由器，或使用其金鑰下載金鑰下載到另一臺路由器（例如替換裝置）。每臺裝置都有一個備份槽位。

## 上傳備份 {#upload-a-backup}

要一步建立當前配置的備份並上傳：

```ros
[admin@MikroTik] > /system/backup/cloud/upload-file action=create-and-upload name=home-router password=Str0ng-Passw0rd
  status: finished
[admin@MikroTik] > /system/backup/cloud/print detail
0  name="home-router" size=31.5KiB ros-version="7.25" date=2026-09-24 10:11:16
   status="ok" secret-download-key="Xy3kP9qLm2Rt7vWz8Bn4Cd5"
```

路由器會使用 `password` 加密備份，該引數為必填。請保管好密碼：恢復備份時需要用到它。`name` 只是雲列表中的名稱。

要上傳之前儲存的備份檔案，請在儲存時設定密碼，使其加密。路由器會拒絕未加密的檔案，並提示 `src file must be AES encrypted`。

```ros
/system/backup/save name=home-router password=Str0ng-Passw0rd
/system/backup/cloud/upload-file action=upload src-file=home-router.backup name=home-router
```

## 替換或刪除備份 {#replace-or-delete-the-backup}

該槽位只能容納一個備份，因此第二次上傳會失敗，並提示 `Server error: All slots used. Delete file to free up space.`。要覆蓋已儲存的備份，請在 `replace` 中指定其名稱：

```ros
/system/backup/cloud/upload-file action=create-and-upload name=home-router password=Str0ng-Passw0rd replace=home-router
```

新備份會獲得新的金鑰下載金鑰。

要刪除備份並釋放槽位：

```ros
/system/backup/cloud/remove-file number=0
```

## 下載或恢復備份 {#download-or-restore-the-backup}

要將此路由器的備份下載到其儲存中：

```ros
/system/backup/cloud/download-file action=download number=0
```

路由器會將檔案儲存為 `<name>.backup`，或使用你在 `dst-file` 中指定的名稱。要從中恢復配置，請使用 [`/system/backup/load`](../../getting-started/configuration-management/backup.md#restore-a-backup)。

要一步完成下載和恢復，請提供備份密碼。路由器會恢復配置並重啟：

```ros
/system/backup/cloud/download-file action=download-and-apply number=0 password=Str0ng-Passw0rd
```

在另一臺路由器上（例如替換裝置），使用原路由器的金鑰下載金鑰下載備份：

```ros
/system/backup/cloud/download-file action=download secret-download-key=Xy3kP9qLm2Rt7vWz8Bn4Cd5
```

任何擁有該金鑰的人都可以下載備份檔案，但沒有密碼就無法讀取它。請妥善保管金鑰，並使用強密碼。備份中還包含製作備份時所用裝置的 MAC 地址（參見[備份](../../getting-started/configuration-management/backup.md)）。

## 技術細節 {#technical-details}

- 路由器透過 TCP 埠 15252 連線到 `cloud2.mikrotik.com` 以進行雲備份。
- `/system/backup/cloud` 中的每條命令都會連線伺服器，`print` 也是如此，因此命令可能需要一段時間才能完成。命令執行時會顯示 `status: working...`。
- `upload-file` 會在連線之前檢查路由器上的檔案：如果沒有密碼，`create-and-upload` 會失敗並提示 `missing password`，而 `upload` 會拒絕未加密的檔案，並提示 `src file must be AES encrypted`。
- `download-file` 在使用 `download-and-apply` 時也會儲存檔案，因此下載的備份在恢復後仍會保留在 `/file` 中。

有關所有命令和屬性的資訊，請參閱 CLI 參考中的 [`/system/backup/cloud`](../../cli-reference/system/backup/cloud/index.md)。
