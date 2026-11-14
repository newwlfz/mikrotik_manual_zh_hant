---
sidebar_key: "authentication-authorization-accounting/user"
sidebar_position: 7
title: "使用者"
sidebar_label: "使用者"
description: "RouterOS 使用者管理：本地使用者資料庫、使用者組與策略、密碼複雜度與過期時間、會話空閒處理、SSH 金鑰認證，以及用於管理登入的 RADIUS 認證與計費。"
tags:
  - 'user-management'
  - 'radius'
  - 'user-groups'
source: https://manual.mikrotik.com/docs/authentication-authorization-accounting/user
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

`/user` 中的路由器使用者功能用於管理透過管理工具訪問路由器的賬戶：WinBox、WebFig、SSH 或 Telnet 控制檯、API 以及 REST API。RouterOS 依據本地使用者資料庫或 RADIUS 伺服器對使用者進行身份驗證。每個使用者只屬於一個使用者組，組的策略定義了該使用者可以在路由器上執行哪些操作。有關加固建議（為每位管理員分配賬戶、金鑰登入、服務限制），請參閱[保護您的路由器](../getting-started/securing-your-router.md)。

## 建立使用者 {#create-a-user}

預設配置中有一個使用者 `admin`，位於 `full` 組中。先建立一個具有使用者所需策略的組，然後新增使用者：

```ros
/user/group/add name=managers policy=ssh,read,write,password
/user/add name=john group=managers password="StrongPass123!"
```

```ros
[admin@MikroTik] > /user/group/print where name=managers
4  name="managers"
   policy=ssh,read,write,password,!local,!telnet,!ftp,!reboot,!policy,!test,
      !winbox,!web,!sniff,!sensitive,!api,!romon,!rest-api skin=default
```

未列出的策略會從該組中撤銷。密碼可包含任意字元，包括空格和 UTF-8。新增使用者時，password 引數是必填的；顯式設定為空密碼（`password=""`）則允許使用空密碼登入。

將 `address` 設定為 IP 字首，可讓該使用者只能從匹配的源地址登入：

```ros
/user/set john address=192.168.88.0/24
```

使用者名稱可包含字母、數字以及字元 `_` `.` `#` `-` `@`，必須以字母或數字結尾，且不能以 `.` 或 `-` 開頭。

有關所有使用者屬性的說明，請參閱 CLI 參考中的 [`/user`](../cli-reference/user/index.md)。

## 修改密碼 {#change-a-password}

使用者可以使用 `/password` 命令修改自己的密碼，既可在互動模式下進行，也可在一行命令中完成：

```ros
/password old-password=StrongPass123! new-password=NewStrongPass456 confirm-new-password=NewStrongPass456
```

使用者所屬的組必須包含 `password` 策略，否則命令會因 “not enough permissions” 而失敗。

管理員使用 `/user/set` 修改其他使用者的密碼：

```ros
/user/set john password="NewStrongPass456"
```

要強制使用者在下次登入時設定新密碼，請將當前密碼設為過期：

```ros
/user/expire-password john
```

```ros
[admin@MikroTik] > /user/print where name=john
Flags: E - EXPIRED
Columns: NAME, GROUP, ADDRESS, INACTIVITY-POLICY
#   NAME  GROUP     ADDRESS          INACTIVITY-POLICY
2 E john  managers  192.168.88.0/24  none
```

在下次互動式登入時，路由器會要求使用者輸入新密碼；由管理員設定的新密碼同樣會清除 `E` 標誌。

可透過 [`/user/settings`](../cli-reference/user/settings.md) 中的複雜度設定來要求更強的密碼：`minimum-password-length` 和 `minimum-categories`（密碼中必須包含數字、小寫字母、大寫字母和符號這幾類字元中的幾類）。

## 使用者組 {#user-groups}

組為使用者分配訪問許可權。策略的完整列表以及每項策略授予的許可權見 [`/user/group`](../cli-reference/user/group.md)。

RouterOS 有三個無法刪除的預設組：

```ros
[admin@MikroTik] > /user/group/print
0  name="read"
   policy=local,telnet,ssh,reboot,read,test,winbox,password,web,sniff,
      sensitive,api,romon,rest-api,!ftp,!write,!policy skin=default

1  name="write"
   policy=local,telnet,ssh,reboot,read,write,test,winbox,password,web,sniff,
      sensitive,api,romon,rest-api,!ftp,!policy skin=default

2  name="full"
   policy=local,telnet,ssh,ftp,reboot,read,write,policy,test,winbox,password,
      web,sniff,sensitive,api,romon,rest-api
```

:::warning
即使是 `read` 組也包含 `reboot` 和 `sensitive` 策略。不要將其授予不受信任的使用者；應改為建立僅包含其所需策略的自定義組。
:::

策略前面的感嘆號 `!` 表示從該組中撤銷該策略。

### 建立只讀使用者 {#create-a-read-only-user}

若要允許某人檢視配置而不做任何更改，請建立一個具有 `read` 策略以及該使用者登入所用工具所需策略的組，然後將該使用者新增到該組中：

```ros
/user/group/add name=readonly policy=read,winbox,web,ssh
/user/add name=viewer group=readonly password="StrongPass123!"
```

該使用者可以在 WinBox、WebFig 以及透過 SSH 檢視配置。更改配置、重啟、執行 ping 和 torch 等工具，以及使用 `/password` 更改自己的密碼都會失敗，並提示 `not enough permissions`。如果沒有 `sensitive` 策略，該使用者無法看到密碼：`/export show-sensitive` 會將其顯示為 `*****`。

## 鎖定或關閉非活動會話 {#lock-or-close-inactive-sessions}

在使用者上設定 `inactivity-timeout`（範圍為 1 分鐘到 24 小時）和 `inactivity-policy`，以處理空閒的控制檯會話：

- `logout` 會關閉空閒會話，並提示 “`<name>` was logged out due to inactivity”。
- `lockscreen` 會鎖定會話，恢復時需輸入使用者密碼；按 <kbd>Control</kbd>+<kbd>D</kbd> 可關閉已鎖定的會話。

## SSH 金鑰 {#ssh-keys}

`/user/ssh-keys` 選單儲存分配給使用者的 SSH 公鑰，`/user/ssh-keys/private` 儲存用於在路由器透過 SSH 連線其他裝置（例如使用 `/system/ssh` 或 `/tool/fetch`）時標識路由器自身的私鑰。

:::warning
當用戶被分配了 SSH 金鑰後，SSH 將不再接受該使用者的密碼認證。支援的配置請參閱 [SSH](../management-tools/ssh.md) 頁面。
:::

將金鑰檔案上傳到路由器，併為其匯入給某個使用者：

```ros
/user/ssh-keys/import public-key-file=mykey.pub user=john info="john laptop"
```

```ros
[admin@MikroTik] > /user/ssh-keys/print where user=john
Columns: USER, KEY-TYPE, BITS, INFO
#  USER  KEY-TYPE  BITS  INFO
1  john  ed25519    256  john laptop
```

公鑰匯入支援 OpenSSH 單行格式、PKCS#1 PEM（`BEGIN RSA PUBLIC KEY`）以及 PKCS#8/SPKI PEM（`BEGIN PUBLIC KEY`）檔案。也可以使用 `/user/ssh-keys/add key="ssh-ed25519 AAAA..." user=john` 直接貼上 OpenSSH 格式的金鑰；金鑰字串末尾的註釋會成為該金鑰的 `info`。

私鑰匯入支援 PKCS#1 PEM（`BEGIN RSA PRIVATE KEY`）和 PKCS#8 檔案，包括未加密（`BEGIN PRIVATE KEY`）和加密（`BEGIN ENCRYPTED PRIVATE KEY`，需要 `passphrase` 引數）兩種：

```ros
/user/ssh-keys/private/import private-key-file=routerkey.pem user=john passphrase=keypass
```

不接受 OpenSSH 格式的私鑰（`BEGIN OPENSSH PRIVATE KEY`）。有關所有屬性的說明，請參閱 CLI 參考中的 [`/user/ssh-keys`](../cli-reference/user/ssh-keys/index.md) 和 [`/user/ssh-keys/private`](../cli-reference/user/ssh-keys/private/index.md)。

:::info
公鑰指數較弱（7 或更小）的 RSA 金鑰仍然可用，但在 `/user/ssh-keys` 和 `/user/ssh-keys/private` 的 print 輸出中會被標記為 `key uses insecure RSA public exponent!`。請用更強的金鑰對替換此類金鑰對。
:::

## RADIUS 認證 {#radius-authentication}

路由器使用者的遠端 AAA 會針對 RADIUS 伺服器對管理登入進行身份驗證，並向其傳送計費記錄。請先配置 RADIUS 用戶端：新增一個帶 `service=login` 的 [`/radius`](../cli-reference/radius/index.md) 條目，然後啟用 [`/user/aaa`](../cli-reference/user/aaa.md)。作為 RADIUS 伺服器，任何安裝了 [使用者管理器](./user-manager.md) 軟體包的 RouterOS 均可使用：

```ros
# 在 RADIUS 服务器上
/user-manager/set enabled=yes
/user-manager/router/add name=main address=192.168.88.24 shared-secret=radiusSecret
/user-manager/user/add name=john-remote password=JohnPass456

# 在用户登录的路由器上
/radius/add service=login address=192.168.88.36 secret=radiusSecret
/user/aaa/set use-radius=yes
```

預設情況下，User Manager 允許每個使用者只有一個併發登入（`shared-users`）；當第一個會話仍處於活動狀態時，使用相同名稱的第二次登入會被拒絕。

只有當用戶名在本地使用者資料庫中不存在時才會查詢 RADIUS；同名的本地使用者始終優先。透過 RADIUS 認證的使用者會獲得 `default-group`（預設為 `read`），除非伺服器傳送了指定其他本地組的 `Mikrotik-Group` 屬性（在 User Manager 中，可透過 `attributes="Mikrotik-Group:full"` 在使用者上設定該屬性）。`exclude-groups` 中列出的組絕不會被伺服器接受，此時使用者會獲得 `default-group`。

活動的 RADIUS 認證會話會在 `/user/active/print` 中顯示 `R`（radius）標誌。

## 監控活動會話 {#monitor-active-sessions}

`/user/active/print` 顯示已連線的管理會話：

```ros
[admin@MikroTik] > /user/active/print
Flags: R - RADIUS
Columns: WHEN, NAME, ADDRESS, VIA
#   WHEN                 NAME         ADDRESS        VIA
0 R 2026-09-25 09:32:20  john-remote  192.168.88.17  ssh
```

使用 `/user/active/remove` 關閉會話：

```ros
/user/active/remove [find name=john-remote]
```

有關會話屬性（包括 `M`（by-romon）標誌和完整的 `via` 列表），請參閱 [`/user/active`](../cli-reference/user/active.md)。

## 技術細節 {#technical-details}

### 密碼過期流程 {#expired-password-flow}

`/user/expire-password` 會在使用者上設定 `E` 標誌。在下次互動式登入時，路由器會列印 “Change your password (Ctrl-C to skip)”，然後要求輸入 “new password” 和 “repeat new password”；若兩者不一致，會列印 “New passwords do not match!” 並重復提示。按 <kbd>Control</kbd>+<kbd>C</kbd> 可跳過修改。非互動式會話（透過 SSH 執行命令）不會出現提示。為該使用者設定新密碼會清除該標誌。

### RADIUS 認證與計費 {#radius-authentication-and-accounting}

- 轉發到 RADIUS 的密碼登入使用 MS-CHAPv2 進行認證（Access-Request 中攜帶 `MS-CHAP-Challenge` 和 `MS-CHAP2-Response`）。
- 當 `accounting=yes` 時，路由器在登入時傳送 Accounting-Request（Start），在登出時傳送（Stop）；`interim-update` 設定在會話活動期間傳送 Interim-Update 訊息的間隔。管理會話的計費不包含頻寬計數器。
- `radius` 日誌主題會顯示實際交換的屬性：`/system/logging/add topics=radius`。

## 延伸閱讀 {#read-more}

- CLI 參考中的 [`/user`](../cli-reference/user/index.md)、[`/user/settings`](../cli-reference/user/settings.md)、[`/user/group`](../cli-reference/user/group.md)、[`/user/active`](../cli-reference/user/active.md)、[`/user/aaa`](../cli-reference/user/aaa.md)、[`/user/ssh-keys`](../cli-reference/user/ssh-keys/index.md)
- [RADIUS 用戶端](./radius.md)
- [使用者管理器](./user-manager.md)
- [SSH](../management-tools/ssh.md)
