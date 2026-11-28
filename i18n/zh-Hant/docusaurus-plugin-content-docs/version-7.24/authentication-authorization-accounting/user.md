---
title: "使用者"
description: "MikroTik RouterOS 使用者管理頁面詳細說明透過本機或 RADIUS 伺服器進行使用者驗證、密碼複雜度設定、定義存取權限的使用者群組原則，以及路由器使用者資料庫屬性，包括登入位址、閒置動作與密碼管理。"
tags:
  - 'user-management'
  - 'radius'
  - 'user-groups'
source: https://manual.mikrotik.com/docs/7.24/authentication-authorization-accounting/user
captured_at: '2026-11-28T10:19:39.818Z'
pagination_next: "high-availability-solutions"
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

## 摘要 {#summary}

MikroTik RouterOS 路由器使用者功能可管理透過任一管理工具連線至路由器的使用者。使用者會使用本機資料庫或指定的 RADIUS 伺服器進行驗證。每位使用者都會被指派至一個使用者群組，該群組代表此使用者的權限。群組政策是多個個別政策項目的組合。

若使用者驗證使用 RADIUS 執行，則必須事先設定 [RADIUS](/docs/authentication-authorization-accounting/radius) 用戶端。

## 使用者設定 {#user-settings}

settings 子選單可控制路由器使用者的密碼複雜度需求。

| 屬性 | 說明 |
| :-- | :-- |
| **minimum-password-length** (*integer*; 0..4294967295; Default: ) | 指定使用者密碼的最小字元長度 |
| **minimum-categories** (*integer*; 0..4; Default: ) | 指定密碼的複雜度需求，類別為 <em>uppercase, lowercase, digit, symbol.</em><br/> |

## 使用者群組 {#user-groups}

路由器使用者群組提供便利的方式，可將不同的權限與存取權指派給不同類別的使用者。

### 屬性 {#properties}

| Property | Description |
| :-- | :-- |
| **name** (*string*; Default: ) | 使用者群組的名稱 |
| **policy** (*local \| telnet \| ssh \| ftp \| reboot \| read \| write \| policy \| test \| winbox \| password \| web \| sniff \| sensitive \| api \| rest-api \| romon*; Default: **none**) | 允許的 policy 清單：<br/> 登入 policy：<br/><ul><li>local - 授予透過本機 console 登入權限的 policy</li><li>telnet - 授予透過 telnet 遠端登入權限的 policy</li><li>ssh - 授予透過 secure shell protocol 遠端登入權限的 policy</li><li>web - 授予透過 WebFig 遠端登入權限的 policy。</li><li>winbox - 授予透過 WinBox 遠端登入及 bandwidth test 驗證權限的 policy</li><li>password - 授予目前登入使用者變更密碼的權限（自己的密碼） </li><li>api - 授予透過 API 存取路由器的權限。</li><li>rest-api - 授予透過 REST API 存取路由器的權限。</li><li>ftp - 授予透過 FTP 遠端登入的完整權限。允許讀取／寫入／刪除檔案，以及從路由器傳輸檔案至路由器或從路由器傳出檔案。應與 read/write policy 一起使用。</li><li>romon - 授予連線至 RoMon 伺服器的權限。</li></ul> 設定 policy：<br/><ul><li>reboot - 允許重新啟動路由器的 policy</li><li>read - 授予讀取路由器設定權限的 policy。所有不會變更路由器設定的 console 指令皆允許。不影響 FTP</li><li>write - 授予寫入路由器設定權限的 policy，但不包括使用者管理。此 policy 不允許讀取設定，因此請務必同時啟用 read policy</li><li>policy - 授予使用者管理權限的 policy。應與 write policy 一起使用。也允許查看其他使用者建立的全域變數（也需要 'test' policy）。允許設計 <a href="/docs/management-tools/webfig#skins" rel="nofollow">skins</a>（也需要 "sensitive" policy）。</li><li>test - 授予執行 ping、traceroute、bandwidth-test、wireless scan、snooper、fetch、email 及其他測試指令權限的 policy</li><li>sensitive - 授予變更 "hide sensitive" 選項的權限，若停用此 policy，則不會顯示敏感資訊。</li><li>sniff - 授予使用 packet sniffer 工具、torch 工具、traffic generator 的權限。</li></ul> |
| **skin** (*name*; Default: **default**) | WebFig 使用的 skin |

### 預設群組 {#default-groups}

有三個無法刪除的預設系統群組：

```ros
[admin@MikroTik] > /user/group/print 
0 name="read" policy=local,telnet,ssh,reboot,read,test,winbox,password,web,sniff,sensitive,api,romon,rest-api,!ftp,!write,!policy skin=default 

1 name="write" policy=local,telnet,ssh,reboot,read,write,test,winbox,password,web,sniff,sensitive,api,romon,rest-api,!ftp,!policy skin=default 

2 name="full" policy=local,telnet,ssh,ftp,reboot,read,write,policy,test,winbox,password,web,sniff,sensitive,api,romon,rest-api skin=default 
```

請注意，即使 "*read*" 群組也包含 *sensitive*、*reboot,* 及其他重要 policy，這表示不應將此群組授予不受信任的使用者。若需要真正受限的群組，請建立自訂群組並定義特定 policy。所有群組皆可存取檔案操作。policy 項目名稱前的驚嘆號 '!' 表示 NOT。

## Router 使用者 {#router-users}

路由器使用者資料庫會儲存路由器管理人員的相關資訊，例如使用者名稱、密碼、允許存取位址及群組。

### 屬性 {#properties-1}

| 屬性 | 說明 |
| :-- | :-- |
| **address** (*IP/mask \| IPv6 prefix*；預設: ) | 允許使用者登入的主機或網路位址 |
| **group** (*string*；預設: ) | 使用者所屬群組的名稱 |
| **inactivity-policy** (*lockscreen* \| *logout* \| *none*；預設: ***none***) | 指定閒置時的動作：logout（使用者將被登出）或 lockscreen（工作階段將被鎖定，需要輸入密碼才能繼續）。僅適用於 CLI 工作階段。 |
| **inactivity-timeout** (*time*；預設: ***10min***) | 指定使用者被登出或工作階段被鎖定前的時間。最短逾時為 1 分鐘，最長逾時為 24 小時。僅適用於 CLI 工作階段。 |
| **name** (*string*；預設: ) | 使用者名稱。必須以英數字元開頭與結尾，但可以包含 "\_"、"."、"#"、"-" 與 "@" 符號。不過，使用者名稱中禁止使用 "\*" 符號。 |
| **password** (*string*；預設: ) *[sensitive](/docs/getting-started/configuration-management/list-of-menus-with-sensitive-parameters)* | 使用者密碼。若未指定，則保持空白（登入時按 <kbd>Enter</kbd>）。其符合標準 Unix 密碼特性，可包含字母、數字、"\*" 與 "\_" 符號。 |
| **last-logged-in** (*time and date*；預設: **""**) | 唯讀欄位。使用者上次登入的時間與日期。 |

### Actions

現有路由器使用者的動作。

| 動作 | 說明 |
| :-- | :-- |
| **password** | 變更使用者密碼的選項。 |
| **expire-password** | 使使用者密碼過期，下次登入時，路由器會提示變更密碼。 |

### 附註 {#notes}

有一個具有完整存取權限的預定義使用者：

```ros
[admin@MikroTik] /user> print
Flags: X - disabled
# NAME GROUP ADDRESS LAST-LOGGED-IN
0 ;;; system default user
admin full 0.0.0.0/0 2010-12-08 16:19:24

```

應始終至少有一個具有完整存取權限的使用者。若具有完整存取權限的使用者只有一個，則無法移除。

## 監控作用中使用者 {#monitoring-active-users}

```ros
/user/active/print
```

 此指令會顯示目前作用中的使用者與對應的統計資訊。

### 屬性 {#properties-2}

所有屬性皆為唯讀。

| 屬性 | 說明 |
| :-- | :-- |
| **address** (*IP/IPv6 address/MAC address*) | 使用者用來存取路由器的主機 IP/IPv6/MAC 位址。 |
| **group** (*string*) | 使用者所屬的群組。 |
| **name** (*string*) | 使用者名稱。 |
| **radius** (*true \| false*) | 使用者是否由 RADIUS 伺服器驗證。 |
| **via** (*telnet \| ssh \| winbox \| api \| rest-api \| web \| ftp* ) | 使用者的存取方式 |
| **by-romon**(MAC address) | RoMON agent MAC 位址 |
| **when** (*time*) | 使用者登入的時間與日期。 |

### 要求登出 {#request-logout}

可以使用 request logout 功能關閉作用中的工作階段。

```routeros
 /user/active/request-logout ACTIVE_USER_SESSION_NUMBER
```

## 遠端 AAA {#remote-aaa}

路由器使用者遠端 AAA 可透過 RADIUS 伺服器啟用路由器使用者驗證與計費。只有在本機使用者資料庫中找不到所需的使用者名稱時，才會查詢 RADIUS 使用者資料庫。

### 屬性 {#properties-3}

| 屬性 | 說明 |
| :-- | :-- |
| **accounting** (*yes \| no*；預設：**yes**) | 是否應將登入、登出的計費資訊傳送給 RADIUS 伺服器。頻寬使用統計不屬於 `/user` 計費的一部分 |
| **exclude-groups** (*list of group names*；預設： ) | exclude-groups 由不允許供 RADIUS 驗證使用者使用的群組組成。如果 RADIUS 伺服器提供此清單中指定的群組，則會改用 default-group。這可防止權限提升，例如某個使用者（沒有 policy 權限）可以變更 RADIUS 伺服器清單、架設自己的 RADIUS 伺服器，並 <br/>以 admin 登入。 |
| **default-group** (*string*；預設：**read**) | 透過 RADIUS 伺服器驗證的使用者預設使用的使用者群組。 |
| **interim-update** (*time*；預設：**0s**) | Interim-Update 時間間隔 |
| **use-radius** (*yes \|no*；預設：**no**) | 啟用透過 RADIUS 進行使用者驗證 |

:::info
如果你使用 RADIUS，則需要在 RADIUS 伺服器中啟用 CHAP 支援，WinBox 才能運作。
:::

## SSH 金鑰 {#ssh-keys}

 此選單可匯入用於 SSH 驗證的私密金鑰與公開金鑰。

:::warning
預設情況下，如果已為使用者新增 SSH 金鑰，則不允許該使用者透過密碼以 SSH 登入。詳細資訊請參閱 [SSH](/docs/management-tools/ssh) 頁面。
:::

### 公開金鑰 {#public-keys}

此選單用於匯入（或新增）及列出已匯入的公開金鑰。公開金鑰用於在使用 SSH 金鑰登入路由器時，確認另一台設備的身分。

:::info
支援 PEM、PKCS#8 或 OpenSSH 格式的 RSA、Ed25519 與 Ed25519-sk 金鑰。
:::

| 屬性 | 說明 |
| :-- | :-- |
| **user** (read-only*)* | 已指派 SSH 金鑰的系統使用者 |
| **info** (read-only*)* | 金鑰資訊 |
| **key-type** (read-only*)* | 金鑰類型 |
| **bits** (read-only*)* | 金鑰長度 |
| **fingerprint** (read-only*)* | SHA256 (Base64) 格式的金鑰指紋 |

#### 匯入公開 SSH 金鑰 {#import-public-ssh-key}

匯入公開 SSH 金鑰時，必須指定金鑰檔案、要指派 SSH 金鑰的系統使用者，也可以選擇指定金鑰擁有者。

| 屬性 | 說明 |
| :-- | :-- |
| **user** (*string*; Default: ) | 已指派 SSH 金鑰的系統使用者 |
| **key-owner** (*string*) | SSH 金鑰擁有者 |
| **public-key-file** (*string*) | 路由器根目錄中包含公開金鑰的檔案名稱 |

#### 新增公開 SSH 金鑰 {#add-public-ssh-key}

可以*新增*公開 SSH 金鑰（貼上 SSH 金鑰字串），必須提供金鑰字串，以及要指派 SSH 金鑰的系統使用者。

:::note
只能以 OpenSSH 格式*新增*金鑰
:::

| 屬性 | 說明 |
| :-- | :-- |
| **user** (*string*; Default: ) | 已指派 SSH 金鑰的系統使用者 |
| **key** (*string*) | 公開金鑰 |

### 私密金鑰 {#private-keys}

此選單用於匯入及列出已匯入的私密金鑰。私密金鑰用於在使用 SSH 金鑰登入另一部設備時，驗證路由器的身分。

匯入私密金鑰時，可以指定 key-owner。

:::info
支援 PEM 或 PKCS#8 格式的 RSA 與 Ed25519 金鑰。
:::

| 屬性 | 說明 |
| :-- | :-- |
| **user** (*string*; Default: ) | 已指派 SSH 金鑰的系統使用者 |
| **key-owner** (*string*) | SSH 金鑰擁有者 |
| **key-type** (read-only*)* | 金鑰類型 |
| **bits** (read-only*)* | 金鑰長度 |

#### 匯入私密 SSH 金鑰 {#import-private-ssh-key}

匯入私密 SSH 金鑰時，必須指定金鑰檔案、要指派 SSH 金鑰的系統使用者，也可以選擇提供金鑰密語並指定金鑰擁有者。

| 屬性 | 說明 |
| :-- | :-- |
| **user** (*string*; Default: ) | 已指派 SSH 金鑰的系統使用者 |
| **key-owner** (*string*) | SSH 金鑰擁有者 |
| **passphrase** *(string) [sensitive](/docs/getting-started/configuration-management/list-of-menus-with-sensitive-parameters)* | 金鑰檔案密語 |
| **private-key-file** (*string*) | 路由器根目錄中包含私密金鑰的檔案名稱 |
