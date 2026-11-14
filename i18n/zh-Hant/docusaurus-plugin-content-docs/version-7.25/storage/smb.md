---
sidebar_key: "storage/smb"
sidebar_position: 11
title: "SMB"
sidebar_label: "SMB"
description: "RouterOS 包含內建 SMB 伺服器，可透過 SMB/CIFS 協定進行檔案共享，支援 SMB2.1、3.0 和 3.1.1。使用者可以透過 `/ip/smb`、`/ip/smb/shares` 和 `/ip/smb/users` 配置伺服器設定、共享和使用者許可權。Storage 軟體包還增加了 SMB 用戶端，用於將遠端共享掛載為磁碟。"
tags:
  - 'smb'
source: https://manual.mikrotik.com/docs/7.25/storage/smb
captured_at: '2026-11-04T11:21:42+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

RouterOS 內建 **SMB 伺服器**，可將路由器上的資料夾共享給網路用戶端。此外，[Storage 軟體包](./index.md) 還增加了 **SMB 用戶端**，允許 RouterOS 將遠端 SMB 共享掛載為磁碟。

## SMB 伺服器 {#smb-server}

**子選單：** `/ip/smb` **所需軟體包：** `system`

SMB 伺服器為路由器上配置的資料夾提供檔案共享訪問，允許網路用戶端透過 SMB/CIFS 協定瀏覽、讀取、寫入和管理路由器儲存介質上的檔案。這使路由器能夠充當簡單的網路附加儲存（NAS）裝置，用於在區域網路內共享檔案、備份資料或路由器配置備份檔案。

:::warning
RouterOS 僅支援 SMB2.1、SMB3.0 和 SMB3.1.1。由於存在安全漏洞，不支援 SMB1。

SMIPS 裝置不支援 SMB。
:::

新增第一個共享後，伺服器會自動啟動（`enabled=auto` 為預設值；相關設定請參見 [`/ip/smb`](../cli-reference/ip/smb/index.md)），也可以將其限制為特定介面並重命名。

### 共享 {#shares}

**子選單：** `/ip/smb/shares`

[`/ip/smb/shares`](../cli-reference/ip/smb/shares.md) 配置可透過 SMB 訪問的共享名稱和目錄。如果配置中提供的目錄不存在，將自動建立。可以透過 `valid-users` / `invalid-users` 按共享限制訪問，透過 `require-encryption` 強制加密（建議 macOS 用戶端使用），並透過 `read-only` 設定只讀訪問。

### 使用者 {#users}

**子選單：** `/ip/smb/users`

[`/ip/smb/users`](../cli-reference/ip/smb/users.md) 設定可訪問路由器 SMB 共享的使用者。每個使用者都有一個名稱、一個密碼，以及一個適用於所有共享的 `read-only` 限制（預設值：是）。系統會自動建立一個預設的 `guest` 使用者，且預設處於停用狀態。

### 示例 {#example}

要透過 SMB 服務使 RouterOS 資料夾可用，請按照以下步驟操作：

- 建立使用者。

```ros
/ip/smb/users/add read-only=no name=mtuser password=mtpasswd
```

- 新增共享資料夾。

```ros
/ip/smb/shares/add directory=backup name=backup
```

- 啟用 SMB 服務：

```ros
#此步骤是可选的，因为默认值为 "enabled=auto"
/ip/smb/set enabled=yes
```

現在檢查結果：

- 檢查常規服務設定。

```ros
/ip/smb/print
      enabled: yes
        status: enabled
        domain: MSHOME
       comment: MikrotikSMB
    interfaces: all
```

- SMB 使用者設定

```ros
/ip/smb/users/print
Flags: X - DISABLED; * - DEFAULT; r - READ-ONLY
Columns: NAME, PASSWORD
#     NAME    PASSWORD
0 X*r guest          
1     mtuser  mtpasswd
```

- 最後是 SMB 共享設定。

```ros
/ip/smb/shares/print
Flags: X - DISABLED; * - DEFAULT
Columns: NAME, DIRECTORY, REQUIRE-ENCRYPTION
#    NAME    DIRECTORY  REQUIRE-ENCRYPTION
;;; default share
0 X* pub     /pub       no               
1    backup  backup     no
```

現在，可以進行其他配置更改，例如停用預設使用者和共享等。

## SMB 用戶端 {#smb-client}

**子選單：** `/disk` **所需軟體包：** [Storage 軟體包](./index.md)

Storage 軟體包增加了一個 SMB 用戶端，可將遠端 SMB 共享掛載為路由器上的本地磁碟。該軟體包目前支援 SMB2.1、SMB3.0 和 SMB3.1.1 方言（由於安全漏洞，不支援 SMB1）。

### 配置示例 {#configuration-example}

```ros
/disk/add smb-address=10.155.145.11 smb-share=share1 smb-user=user smb-password=password type=smb
```

隨後，掛載的共享會作為磁碟出現在 `/file` 中，並可像任何其他磁碟一樣進行管理。
