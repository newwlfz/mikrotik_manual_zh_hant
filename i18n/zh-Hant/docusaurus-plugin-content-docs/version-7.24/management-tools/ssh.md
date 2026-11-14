---
sidebar_key: "management-tools/ssh"
sidebar_position: 6
title: "SSH"
sidebar_label: "SSH"
description: "RouterOS 包含內建 SSH 伺服器，具有可自定義的設定，例如加密演算法配置、金鑰型別和轉發選項。它支援密碼和公鑰認證，並提供用於 export/import 主機金鑰並重新生成它們的命令。透過為使用者匯入公鑰，可以啟用 PKI 認證。"
tags:
  - 'ssh'
source: https://manual.mikrotik.com/docs/7.24/management-tools/ssh
captured_at: '2026-11-04T11:32:05+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## SSH 伺服器 {#ssh-server}

RouterOS 有一個內建的 SSH（SSH v2）伺服器，預設啟用，並在 TCP/22 埠監聽傳入連線。可以在 [服務](../system-information-and-utilities/services.md) 選單下更改埠並停用伺服器。

### 屬性 {#properties}

**子選單：** `/ip/ssh`

| 屬性 | 描述 |
| :-- | :-- |
| **password-authentication** (*yes-if-no-key* \| *yes \| no*; 預設：**yes-if-no-key**) | 當為使用者配置了公鑰授權時，是否同時允許密碼登入。 |
| **ciphers** (*3des-cbc *\| aes-cbc \| aes-ctr \| aes-gcm \| auto \| null*;* 預設：**auto**) | 允許配置 SSH 加密演算法。 |
| **forwarding-enabled** (*both \| local \| no \| remote*; 預設：**no**) | 允許控制要允許哪種 SSH 轉發方法：no - 停用 SSH 轉發；local - 允許 SSH 用戶端從伺服器（路由器）發起連線，此設定還控制動態轉發；remote - 允許 SSH 用戶端在伺服器（路由器）上監聽並轉發傳入連線；both - 允許本地和遠端轉發方法。 |
| **host-key-size** (*1024 \| 1536 \| 2048 \| 4096 \| 8192*; 預設：**2048**) | 重新生成主機金鑰時使用的 RSA 金鑰大小。 |
| **host-key-type** (*ed25519* \| *rsa*; 預設：**rsa**) | 選擇主機金鑰型別 |
| **publickey-authentication-options**  (*none* \| *touch-required* \| *verify-required*; 預設：**none**) | 設定公鑰認證選項。touch-required 選項會使使用 FIDO 認證器演算法的公鑰認證始終要求籤名證明存在物理使用者並明確確認了認證（通常透過觸控認證器）。verify-required 選項要求 FIDO 金鑰簽名證明使用者已透過驗證，例如透過 PIN。 |
| **strong-crypto** (*yes \| no*; 預設：**no**) | 使用更強的加密、HMAC 演算法，使用更大的 DH 素數並禁止較弱的選項：使用 256 和 192 位加密而不是 128 位；停用 null 加密；使用 sha256 進行雜湊而不是 sha1；停用 md5；使用 2048 位素數進行 Diffie-Hellman 交換而不是 1024 位。 |

### 命令 {#commands}

**export-host-key** (*key-file-prefix*)

將公有和私有 RSA/Ed25519 金鑰匯出到檔案。該命令接受兩個引數：

- **key-file-prefix** - 生成檔案使用的字首，例如，字首 'my' 將生成檔案 'my_rsa'、'my_rsa.pub' 等。
- **passphrase** - 私鑰口令 [sensitive](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)

:::info
主機金鑰以 PKCS#8 格式匯出。

**警告：** 匯出 SSH 主機金鑰需要 "sensitive" 使用者策略。
:::

---

**import-host-key** (*private-key-file*)

從指定檔案匯入並替換私有 RSA/Ed25519 金鑰。該命令接受兩個引數：

- **private-key-file** - 私有 RSA/Ed25519 金鑰檔案的名稱
- **passphrase** - 私鑰口令 [sensitive](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)

:::info
支援 PEM 或 PKCS#8 格式的私鑰。
:::

---

**regenerate-host-key** ()

在路由器上生成新的私鑰集（RSA/Ed25519）並替換當前私鑰集。請注意，之前匯入的金鑰可能會停止工作。

### 啟用 PKI 認證 {#enabling-pki-authentication}

為使用者 **admin** 匯入公鑰的示例

[在用戶端裝置上獲取 SSH 金鑰對](#log-in-using-ssh-key)（你將從中連線的裝置）。將 SSH 公鑰上傳到路由器並匯入。

有關受支援 SSH 金鑰的更多資訊，請參閱 [使用者 SSH 金鑰](../authentication-authorization-accounting/user.md#ssh-keys) 部分。

```ros
/user/ssh-keys/import public-key-file=id_rsa.pub user=admin
```

### SSH 金鑰對生成 {#ssh-key-pair-generation}

RouterOS 不支援 Linux 系統上可用的直接 SSH 金鑰生成。

要獲取 SSH 金鑰對（SSH 金鑰對會在首次 SSH 連線時自動生成），必須[匯出](#commands)裝置的 SSH 主機金鑰。

## SSH 用戶端 {#ssh-client}

**子選單：** `/system/ssh`

### **簡單登入到遠端主機** {#simple-log-in-to-remote-host}

可以連線到遠端主機並啟動 SSH 會話。該 IP 地址同時支援 IPv4 和 IPv6。

```ros
/system/ssh 192.168.88.1
/system/ssh 2001:db8:add:1337::beef
```

在這種情況下，提供給遠端主機的使用者名稱是登入到路由器的那個使用者名稱。如果需要其他值，則必須使用 *user=\<username>*。

```ros
/system/ssh 192.168.88.1 user=lala
/system/ssh 2001:db8:add:1337::beef user=lala
```

### **從路由器的特定 IP 地址登入** {#log-in-from-certain-ip-address-of-the-router}

出於測試或安全原因，可能需要使用連線的特定源地址登入到另一臺主機。在這種情況下，必須使用 *src-address=\<ip address>* 引數。請注意，此處的 IP 地址同時支援 IPv4 和 IPv6。

```ros
/system/ssh 192.168.88.1 src-address=192.168.89.2
/system/ssh 2001:db8:add:1337::beef src-address=2001:db8:bad:1000::2
```

在這種情況下，SSH 用戶端將嘗試繫結到指定的地址，然後向遠端主機發起 SSH 連線。

### **使用 SSH 金鑰登入** {#log-in-using-ssh-key}

為使用者 *admin* 匯入 RSA 私鑰的示例。

首先，將當前生成的 SSH 金鑰匯出到檔案：

```ros
/ip/ssh/export-host-key key-file-prefix=admin
```

將生成兩個檔案 *admin\_rsa* 和 *admin\_rsa.pub*。需要在 SSH 伺服器端信任 pub 檔案（[如何在 RouterOS 上啟用 SSH PKI](./ssh.md#enabling-pki-authentication)）。必須為特定使用者新增私鑰。

```ros
/user/ssh-keys/private/import user=admin private-key-file=admin_rsa
```

:::danger
只有對路由器擁有完全許可權的使用者才能更改 *`/user/ssh-keys/private`* 下的 'user' 屬性值
:::

在 SSH 伺服器上安裝並信任公鑰後，即可建立 PKI SSH 會話。

```ros
/system/ssh 192.168.1.1
```

觀看操作方法：

使用 [RSA 金鑰](http://youtube.com/watch?v=8tt7fSvdFRM) 登入。

使用 [Ed25519](http://youtube.com/watch?v=be-pBwhjRWA) 登入。

### **執行遠端命令** {#executing-remote-commands}

要執行遠端命令，必須在登入行末尾提供該命令

```ros
/system/ssh 192.168.88.1 "/ip/address/print"
/system/ssh 192.168.88.1 command="/ip/address/print"
/system/ssh 2001:db8:add:1337::beef "/ip/address/print"
/system/ssh 2001:db8:add:1337::beef command="/ip/address/print"
```

:::danger
*如果伺服器不支援 pseudo-tty（ssh -T 或 ssh host command），例如 MikroTik SSH 伺服器，則無法透過 SSH 傳送多行命令*
:::

例如，向 MikroTik 路由器傳送命令 `"/ip/address \n add address=1.1.1.1/24"` 將會失敗。

:::warning
如果你想透過 **scripts** 或 **scheduler** 執行遠端命令，請使用 **ssh-exec** 命令。
:::

## SSH 執行 {#ssh-exec}

**子選單：** `/system/ssh-exec`

命令 *ssh-exec* 是一個非互動式 SSH 命令，因此允許透過 scripts 和 scheduler 在裝置上遠端執行命令。

### **獲取資訊** {#retrieve-information}

該命令將返回兩個值：

- **exit-code**：如果命令執行成功則返回 0
- **output**：返回遠端執行命令的輸出

**示例：** 下面的程式碼將從裝置 10.10.10.1 獲取 ether1 的介面狀態，並將結果輸出到 "Log"

```ros
:local Status ([/system/ssh-exec address=10.10.10.1 user=remote command=":put ([/interface/ethernet/monitor [find where name=ether1] once as-value]->\"status\")" as-value]->"output")
:log info $Status
```

:::warning
出於安全原因，你不應使用在命令列中指定 "password" 引數的明文密碼。為確保遠端安全執行命令，強烈建議在兩端為使用者使用 SSH PKI 認證。

**注意：** 執行該命令的使用者組和指令碼策略需要 **test** 許可權
:::

觀看如何[透過 SSH 執行命令](http://youtube.com/watch?v=JfGfPSicTzs)。
