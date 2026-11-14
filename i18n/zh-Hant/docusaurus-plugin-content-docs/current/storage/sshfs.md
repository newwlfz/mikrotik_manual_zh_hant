---
sidebar_key: "storage/sshfs"
sidebar_position: 12
title: "SSHFS"
sidebar_label: "SSHFS"
description: "SSHFS 允許將遠端 SSH 伺服器上的資料夾作為 RouterOS 中的本地磁碟掛載，使用 `/disk` 的 `sshfs` 型別。掛載透過遠端地址、使用者憑據和路徑進行配置，並像其他網路檔案系統一樣顯示在 `/file` 中。"
tags:
  - 'ssh'
  - 'storage'
  - 'sshfs'
source: https://manual.mikrotik.com/docs/storage/sshfs
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

SSHFS（SSH 檔案系統）透過 SSH 將遠端資料夾掛載為路由器上的本地磁碟。它透過 `/disk/add type=sshfs` 進行配置，隨後遠端目錄會像其他已掛載儲存一樣出現在 `/file` 下，因此可以在本地瀏覽和複製檔案。

RouterOS 在 `/disk` 下跟蹤每個 sshfs 條目，其 slot 由地址和路徑自動生成，例如地址 `192.168.88.1` 和路徑 `/srv/files` 對應 `sshfs-192-168-88-1--srv-files`，並以 `sshfs://<user>@<address>:<port>//<path>` 的形式暴露該掛載。

## 配置示例 {#configuration-example}

```ros
/disk/add type=sshfs sshfs-address=192.168.88.1 sshfs-port=22 sshfs-user=user sshfs-password=superSecret sshfs-path=/srv/files
```

新增條目後，路由器會在後臺開始連線；在連線過程中（或遠端端不可達期間），該條目會顯示 `state=mounting`：

```ros
[admin@MikroTik] > /disk/print where type=sshfs
Columns: SLOT, FS, MOUNT-POINT, STATE
#   SLOT                                FS     MOUNT-POINT  STATE
0   sshfs-192-168-88-1--srv-files  sshfs  sshfs-192-168-88-1--srv-files   mounting
```

掛載完成後，遠端資料夾會作為目錄出現在 `/file` 下的掛載點中（`/file/print`）。

可以使用 `/disk/set` 調整該條目，例如更改埠：

```ros
/disk/set [find where type=sshfs] sshfs-port=2222
```

使用 `/disk/remove <slot>` 移除掛載。

身份驗證使用遠端 SSH 伺服器的使用者名稱/密碼（`sshfs-user` / `sshfs-password`）。`sshfs-local-user` 在路由器上是隻讀的，表示該掛載所執行的本地 RouterOS 使用者（例如 `admin`）。
