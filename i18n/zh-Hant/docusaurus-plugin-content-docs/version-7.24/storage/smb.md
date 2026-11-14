---
sidebar_key: "storage/smb"
sidebar_position: 11
title: "SMB"
sidebar_label: "SMB"
description: "RouterOS 包含內建 SMB 伺服器，用於透過 SMB/CIFS 協定進行檔案共享，支援 SMB2.1、3.0 和 3.1.1，並針對 SMB1 和 SMIPS 裝置提供安全警告。使用者可透過 `/ip/smb`、`/ip/smb/shares` 和 `/ip/` 配置共享、設定使用者許可權並管理訪問許可權。"
tags:
  - 'smb'
source: https://manual.mikrotik.com/docs/7.24/storage/smb
captured_at: '2026-11-04T11:33:17+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

RouterOS 內建 **SMB 伺服器**，可將路由器上的資料夾共享給網路用戶端。此外，[ROSE 軟體包](./index.md)還提供了 **SMB 用戶端**，允許 RouterOS 將遠端 SMB 共享掛載為磁碟。

## SMB 伺服器 {#smb-server}

**子選單：** `/ip/smb` **所需軟體包：** `system`

SMB 伺服器為路由器上配置的資料夾提供檔案共享訪問，允許網路用戶端透過 SMB/CIFS 協定瀏覽、讀取、寫入和管理路由器儲存介質上的檔案。這使路由器能夠充當簡單的網路附加儲存（NAS）裝置，用於在區域網路內共享檔案、備份資料或路由器配置備份檔案。

:::warning
RouterOS 僅支援 SMB2.1、SMB3.0 和 SMB3.1.1。由於安全漏洞，不支援 SMB1。

**注意：** SMIPS 裝置不支援 SMB。
:::

### 伺服器設定 {#server-settings}

| 屬性 | 描述 |
| :-- | :-- |
| **comment** (*string*; 預設值：**MikrotikSMB**) | 為伺服器設定註釋 |
| **domain** (*string*; 預設值：**MSHOME**) | Windows 工作組的名稱 |
| **enabled** (*yes \| no \| auto* 預設值：**auto**) | 預設值為 'auto'。這意味著當在 `/ip/smb/share` 下配置了第一個未停用的 SMB 共享時，SMB 伺服器將自動啟用 |
| **interface** (*string*; 預設值：**all**) | 執行 SMB 服務的介面列表。all - SMB 將在所有介面上可用。 |

:::warning
從 7.14 版本開始，'allow-guest' 選項已被位於 `/ip/smb/users` 中的預設訪客使用者取代。現在可以在此部分停用或啟用該預設訪客使用者。
:::

### 共享設定 {#share-settings}

**子選單：** `/ip/smb/shares`

允許配置 SMB 可訪問的共享名稱和目錄。

如果配置中提供的目錄不存在，將自動建立。

| 屬性 | 描述 |
| :-- | :-- |
| **comment** (*string*; 預設值：**default share**) | 為共享設定註釋 |
| **disabled** (*yes \| no*; 預設值：**no**) | 如果停用，該共享將無法訪問。 |
| **valid-users**（*字串*列表；\| 預設值：） | 指定允許訪問 Samba 共享的使用者。如果留空，所有使用者都可以訪問該共享。一旦在此定義了使用者，則只有這些使用者才能訪問該共享 |
| **invalid-users**（*字串*列表；\| 預設值：） | 用於指定被明確拒絕訪問 Samba 共享的使用者。 |
| **require-encryption** (*yes*\| *no*; 預設值：***no***) | 強制對特定 Samba 共享的所有連線使用加密。建議將其更改為 "Yes"，以確保與 macOS 用戶端更好的穩定性。 |
| **name** (*string*; 預設值：) | SMB 共享的名稱 |
| **directory** (*string*; 預設值：) | 分配給 SMB 共享的路由器上的目錄。如果留空，將使用根資料夾中的 *name* 引數值。 |

### 使用者設定 {#user-setup}

**子選單：** `/ip/smb/users`

設定可訪問路由器 SMB 共享的使用者。

| 屬性 | 描述 |
| :-- | :-- |
| **comment** (*string*; 預設值：) | 為使用者設定描述 |
| **disabled** (*yes \| no*; 預設值：**no**) | 定義使用者是啟用還是停用 |
| **name** (*string*; 預設值：) | SMB 服務使用者的登入名 |
| **password** (*string*; 預設值：) *[sensitive](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | SMB 使用者連線 SMB 服務的密碼 |
| **read-only** (*yes \| no*; 預設值：**yes**) | 設定使用者訪問共享時僅具有隻讀許可權還是完全訪問許可權。 |

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

**子選單：** `/disk` **所需軟體包：** [儲存](./index.md)

ROSE 軟體包添加了一個 SMB 用戶端，可將遠端 SMB 共享掛載為路由器上的本地磁碟。ROS 軟體包目前支援 SMB2.1、SMB3.0 和 SMB3.1.1 方言（由於安全漏洞，不支援 SMB1）。

### 屬性 {#properties}

| 屬性 | 描述 |
| :-- | :-- |
| **smb-address** | SMB 伺服器的 IP 地址 |
| **smb-password***[sensitive](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | SMB 密碼 |
| **smb-share** | 要連線的共享名稱 |
| **smb-user** | SMB 使用者 |

### 配置示例 {#configuration-example}

用戶端

```ros
add smb-address=10.155.145.11 smb-share=share1 smb-user=user smb-password=password type=smb
```
