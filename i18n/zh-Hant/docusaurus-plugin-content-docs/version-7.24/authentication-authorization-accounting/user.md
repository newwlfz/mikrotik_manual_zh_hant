---
sidebar_key: "authentication-authorization-accounting/user"
sidebar_position: 7
title: "使用者"
sidebar_label: "使用者"
description: "MikroTik RouterOS 使用者管理頁面詳細介紹了透過本地或 RADIUS 伺服器進行使用者身份驗證、密碼複雜性設定、定義訪問許可權的使用者組策略，以及路由器使用者資料庫屬性（包括登入地址、不活動操作和密碼管理）。"
tags:
  - 'user-management'
  - 'radius'
  - 'user-groups'
source: https://manual.mikrotik.com/docs/7.24/authentication-authorization-accounting/user
captured_at: '2026-11-04T11:27:00+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 概述 {#summary}

MikroTik RouterOS 路由器使用者功能管理從任何管理工具連線到路由器的使用者。使用者透過本地資料庫或指定的 RADIUS 伺服器進行身份驗證。每個使用者都分配到一個使用者組，該使用者組表示此使用者的許可權。組策略是各個策略項的組合。

如果使用者身份驗證透過 RADIUS 執行，則應事先配置 [RADIUS](./radius.md) 用戶端。

## 使用者設定 {#user-settings}

settings 子選單允許控制路由器使用者的密碼複雜性要求。

| 屬性 | 描述 |
| :-- | :-- |
| **minimum-password-length** (*integer*; 0..4294967295; 預設值：) | 指定使用者密碼的最小字元長度 |
| **minimum-categories** (*integer*; 0..4; 預設值：) | 指定密碼的複雜性要求，其中類別為*大寫字母、小寫字母、數字、符號。*  |

## 使用者組 {#user-groups}

路由器使用者組提供了一種便捷方式，可為不同使用者類別分配不同的許可權和訪問許可權。

### 屬性 {#properties}

| 屬性 | 描述 |
| :-- | :-- |
| **name** (*string*; 預設值：) | 使用者組的名稱 |
| **policy** (*local \| telnet \| ssh \| ftp \| reboot \| read \| write \| policy \| test \| winbox \| password \| web \| sniff \| sensitive \| api \| rest-api \| romon*; 預設值：**none**) | 允許的策略列表： 登入策略： local - 授予透過控制檯本地登入許可權的策略；telnet - 授予透過 telnet 遠端登入許可權的策略；ssh - 授予透過 Secure Shell 協定遠端登入許可權的策略；web - 授予透過 WebFig 遠端登入許可權的策略；winbox - 授予透過 WinBox 和頻寬測試身份驗證遠端登入許可權的策略；password - 授予更改當前登入使用者密碼（自己的密碼）許可權的策略；api - 授予透過 API 訪問路由器許可權；rest-api - 授予透過 REST API 訪問路由器許可權；ftp - 授予透過 FTP 遠端登入完整許可權的策略。允許讀取/寫入/擦除檔案，以及從路由器傳輸檔案或向路由器傳輸檔案。應與 read/write 策略一起使用；romon - 授予連線到 RoMon 伺服器許可權的策略。配置策略： reboot - 允許重啟路由器的策略；read - 授予對路由器配置讀取訪問許可權的策略。允許所有不更改路由器配置的控制檯命令。不影響 FTP；write - 授予對路由器配置寫入訪問許可權的策略，但使用者管理除外。此策略不允許讀取配置，因此請確保同時啟用 read 策略；policy - 授予使用者管理許可權的策略。應與 write 策略一起使用。還允許檢視其他使用者建立的全域性變數（還需要 'test' 策略）。允許設計皮膚（還需要 "sensitive" 策略）；test - 授予執行 ping、traceroute、bandwidth-test、無線掃描、snooper、fetch、email 和其他測試命令許可權的策略；sensitive - 授予更改 "hide sensitive" 選項的許可權，如果停用此策略，則不顯示敏感資訊；sniff - 授予使用封包嗅探工具、torch 工具、流量生成器許可權的策略。 |
| **skin** (*name*; 預設值：**default**) | 用於 WebFig 的皮膚 |

### 預設組 {#default-groups}

有三個無法刪除的預設系統組：

```ros
[admin@MikroTik] > /user/group/print 
0 name="read" policy=local,telnet,ssh,reboot,read,test,winbox,password,web,sniff,sensitive,api,romon,rest-api,!ftp,!write,!policy skin=default 

1 name="write" policy=local,telnet,ssh,reboot,read,write,test,winbox,password,web,sniff,sensitive,api,romon,rest-api,!ftp,!policy skin=default 

2 name="full" policy=local,telnet,ssh,ftp,reboot,read,write,policy,test,winbox,password,web,sniff,sensitive,api,romon,rest-api skin=default 
```

請注意，即使是 "*read*" 組也包含 *sensitive*、*reboot,* 和其他重要策略，這意味著不應將此組授予不受信任的使用者。對於真正受限的組，請建立自定義組並定義特定策略。所有組都可以訪問檔案操作。策略項名稱前面的感嘆號 '!' 表示 NOT。

## 路由器使用者 {#router-users}

路由器使用者資料庫儲存有關路由器管理人員的資訊，例如使用者名稱、密碼、允許的訪問地址和組。

### 屬性 {#properties-1}

| 屬性 | 說明 |
| :-- | :-- |
| **address** (*IP/mask \| IPv6 prefix*; 預設值：) | 允許使用者登入的主機或網路地址 |
| **group** (*string*; 預設值：) | 使用者所屬組的名稱 |
| **inactivity-policy** (*lockscreen* \| *logout* \| *none*; 預設值：***none***) | 指定無活動操作 - logout（使用者將被登出）或 lockscreen（會話將被鎖定，需要輸入密碼才能繼續）。僅適用於 CLI 會話。 |
| **inactivity-timeout** (*time*; 預設值：***10min***) | 指定使用者被登出或會話被鎖定之前的時間。最小超時 - 1 分鐘，最大超時 - 24 小時。僅適用於 CLI 會話。 |
| **name** (*string*; 預設值：) | 使用者名稱。必須以字母數字字元開頭和結尾，但可以包含 "\_"、"."、"#"、"-" 和 "@" 符號。但是，使用者名稱中禁止使用 "\*" 符號。 |
| **password** (*string*; 預設值：) *[sensitive](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 使用者密碼。如果未指定，則留空（登入時按 <kbd>Enter</kbd>）。它符合 Unix 密碼的標準特性，可以包含字母、數字、"\*" 和 "\_" 符號。 |
| **last-logged-in** (*time and date*; 預設值：**""**) | 只讀欄位。使用者上次登入的時間和日期。 |

### 操作 {#actions}

現有路由器使用者的操作。

| 操作 | 說明 |
| :-- | :-- |
| **password** | 更改使用者密碼的選項。 |
| **expire-password** | 使使用者密碼過期，下次登入時，路由器將提示更改密碼。 |

### 備註 {#notes}

有一個具有完全訪問許可權的預定義使用者：

```ros
[admin@MikroTik] /user> print
Flags: X - disabled
# NAME GROUP ADDRESS LAST-LOGGED-IN
0 ;;; system default user
admin full 0.0.0.0/0 2010-12-08 16:19:24

```

始終應至少有一個具有完全訪問許可權的使用者。如果具有完全訪問許可權的使用者是唯一一個，則無法將其刪除。

## 監控活動使用者 {#monitoring-active-users}

```ros
/user/active/print
```

 該命令顯示當前活動使用者及其各自的統計資訊。

### 屬性 {#properties-2}

所有屬性均為只讀。

| 屬性 | 說明 |
| :-- | :-- |
| **address** (*IP/IPv6 address/MAC address*) | 使用者訪問路由器時所使用的主機 IP/IPv6/MAC 地址。 |
| **group** (*string*) | 使用者所屬的組。 |
| **name** (*string*) | 使用者名稱。 |
| **radius** (*true \| false*) | 使用者是否由 RADIUS 伺服器進行身份驗證。 |
| **via** (*telnet \| ssh \| winbox \| api \| rest-api \| web \| ftp* ) | 使用者的訪問方式 |
| **by-romon**(MAC 地址) | RoMON 代理 MAC 地址 |
| **when** (*time*) | 使用者登入的時間和日期。 |

### 請求登出 {#request-logout}

可以使用 request logout 功能關閉活動會話。

```routeros
 /user/active/request-logout ACTIVE_USER_SESSION_NUMBER
```

## 遠端 AAA {#remote-aaa}

路由器使用者遠端 AAA 可透過 RADIUS 伺服器啟用路由器使用者身份驗證和計費。僅當在本地使用者資料庫中找不到所需使用者名稱時，才會查詢 RADIUS 使用者資料庫。

### 屬性 {#properties-3}

| 屬性 | 描述 |
| :-- | :-- |
| **accounting** (*yes \| no*; 預設值：**yes**) | 是否應向 RADIUS 伺服器傳送登入、登出的計費資訊。頻寬使用統計不屬於 `/user` 計費的一部分 |
| **exclude-groups** (*list of group names*; 預設值：) | exclude-groups 由不允許用於透過 radius 身份驗證的使用者的組組成。如果 radius 伺服器提供的組在此列表中指定，則將改用 default-group。這是為了防止許可權提升，即一個使用者（沒有 policy 許可權）可以更改 radius 伺服器列表、設定自己的 radius 伺服器並以 admin 身份登入。 |
| **default-group** (*string*; 預設值：**read**) | 透過 RADIUS 伺服器身份驗證的使用者預設使用的使用者組。 |
| **interim-update** (*time*; 預設：**0s**) | Interim-Update 時間間隔 |
| **use-radius** (*yes \|no*; 預設值：**no**) | 啟用透過 RADIUS 的使用者身份驗證 |

:::info
如果使用 RADIUS，則需要在 RADIUS 伺服器中啟用 CHAP 支援，WinBox 才能正常工作。
:::

## SSH 金鑰 {#ssh-keys}

 此選單允許匯入用於 SSH 身份驗證的私鑰和公鑰。

:::warning
預設情況下，如果為使用者添加了 SSH 金鑰，則不允許該使用者透過密碼進行 SSH 登入。有關詳細資訊，請參閱 [SSH](../management-tools/ssh.md) 頁面。
:::

### 公鑰 {#public-keys}

此選單用於匯入（或新增）並列出已匯入的公鑰。當使用 SSH 金鑰登入路由器時，公鑰用於驗證另一臺裝置的身份。

:::info
支援 PEM、PKCS#8 或 OpenSSH 格式的 RSA、Ed25519 和 Ed25519-sk 金鑰。
:::

| 屬性 | 說明 |
| :-- | :-- |
| **user** (只讀*)* | 已為其分配 SSH 金鑰的系統使用者 |
| **info** (只讀*)* | 金鑰資訊 |
| **key-type** (只讀*)* | 金鑰型別 |
| **bits** (只讀*)* | 金鑰長度 |
| **fingerprint** (只讀*)* | SHA256 (Base64) 格式的金鑰指紋 |

#### 匯入 SSH 公鑰 {#import-public-ssh-key}

匯入 SSH 公鑰時，必須指定金鑰檔案、將為其分配 SSH 金鑰的系統使用者；可選地，可以指定金鑰所有者。

| 屬性 | 說明 |
| :-- | :-- |
| **user** (*string*; 預設值：) | 已為其分配 SSH 金鑰的系統使用者 |
| **key-owner** (*string*) | SSH 金鑰所有者 |
| **public-key-file** (*string*) | 路由器根目錄中包含公鑰的檔名 |

#### 新增 SSH 公鑰 {#add-public-ssh-key}

可以*新增* SSH 公鑰（貼上 SSH 金鑰字串），必須提供金鑰字串以及將為其分配 SSH 金鑰的系統使用者。

:::note
只能*新增* OpenSSH 格式的金鑰
:::

| 屬性 | 說明 |
| :-- | :-- |
| **user** (*string*; 預設值：) | 已為其分配 SSH 金鑰的系統使用者 |
| **key** (*string*) | 公鑰 |

### 私鑰 {#private-keys}

此選單用於匯入並列出已匯入的私鑰。當使用 SSH 金鑰登入另一臺裝置時，私鑰用於驗證路由器的身份。

匯入私鑰時，可以指定 key-owner。

:::info
支援 PEM 或 PKCS#8 格式的 RSA 和 Ed25519 金鑰。
:::

| 屬性 | 說明 |
| :-- | :-- |
| **user** (*string*; 預設值：) | 已為其分配 SSH 金鑰的系統使用者 |
| **key-owner** (*string*) | SSH 金鑰所有者 |
| **key-type** (只讀*)* | 金鑰型別 |
| **bits** (只讀*)* | 金鑰長度 |

#### 匯入 SSH 私鑰 {#import-private-ssh-key}

匯入 SSH 私鑰時，必須指定金鑰檔案、將為其分配 SSH 金鑰的系統使用者；可選地，可以提供金鑰口令並指定金鑰所有者。

| 屬性 | 說明 |
| :-- | :-- |
| **user** (*string*; 預設值：) | 已為其分配 SSH 金鑰的系統使用者 |
| **key-owner** (*string*) | SSH 金鑰所有者 |
| **passphrase** *(string) [sensitive](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 金鑰檔案口令 |
| **private-key-file** (*string*) | 路由器根目錄中包含私鑰的檔名 |
