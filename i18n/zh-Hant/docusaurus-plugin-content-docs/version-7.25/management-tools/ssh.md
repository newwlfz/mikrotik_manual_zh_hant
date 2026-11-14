---
sidebar_key: "management-tools/ssh"
sidebar_position: 7
title: "SSH"
sidebar_label: "SSH"
description: "RouterOS 內建 SSH 伺服器和用戶端。伺服器可自定義（加密演算法、金鑰型別、轉發、密碼和公鑰認證），其主機金鑰可以匯出、匯入和重新生成。用戶端（`ssh` 和 `ssh-exec`）會根據儲存的 known hosts 驗證遠端主機金鑰。"
tags:
  - 'ssh'
source: https://manual.mikrotik.com/docs/7.25/management-tools/ssh
captured_at: '2026-11-04T11:19:46+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

RouterOS 提供 SSH（SSH v2）伺服器，用於遠端管理路由器；同時也提供 SSH 用戶端，用於從路由器連線到其他裝置。它有兩個用戶端命令：[`/system/ssh`](../cli-reference/system/ssh.md) 用於互動式會話和手動執行命令，[`/system/ssh-exec`](../cli-reference/system/ssh-exec.md) 用於指令碼和排程器中的非互動式使用。

## SSH 伺服器 {#ssh-server}

SSH 伺服器預設啟用，並在 TCP/22 埠監聽傳入連線。你可以在 [服務](../system-information-and-utilities/services.md) 選單中更改埠並停用伺服器。

引數說明請參閱 [`/ip/ssh`](../cli-reference/ip/ssh/index.md) CLI 參考。

### 伺服器主機金鑰 {#server-host-key}

路由器的 SSH 主機金鑰會自動生成。使用以下命令顯示當前金鑰的指紋：

```ros
/ip/ssh/print
```

只讀的 `host-key-fingerprint` 值可讓管理員確認自己連線的是正確的路由器。

建立新的主機金鑰對（例如在舊金鑰洩露之後），可使用：

```ros
/ip/ssh/regenerate-host-key
```

更改 `host-key-type` 也會立即重新生成金鑰。任何重新生成之後，固定了舊金鑰的 SSH 用戶端都會報告指紋不匹配；請分發新的指紋（`/ip/ssh/print`）或更新已固定的條目。

:::info
如果主機金鑰是公鑰指數較弱（7 或更低）的 RSA 金鑰，則 SSH 主機金鑰會自動重新生成，並記錄該事件：

```text
ssh,critical host key uses insecure RSA public exponent! Host key will be regenerated!
```
:::

在新安裝中，預設主機金鑰型別為 Ed25519；從較舊 RouterOS 版本升級的路由器會保留其 RSA 金鑰。

使用 [`export-host-key`](../cli-reference/ip/ssh/export-host-key.md) 和 [`import-host-key`](../cli-reference/ip/ssh/import-host-key.md) 可將主機金鑰遷移到另一臺路由器（例如更換硬體時）。匯出的檔案按 `key-file-prefix` 命名，例如對於 `key-file-prefix=bbu` 的 RSA 金鑰，檔名為 `bbu_rsa.pem` 和 `bbu_rsa_pub.pem`。

### 使用公鑰登入 {#log-in-with-a-public-key}

要為傳入連線啟用 PKI 認證，請匯入連線使用者的公鑰。先在發起連線的裝置上生成金鑰對（參見[使用 SSH 金鑰登入](#log-in-with-an-ssh-key)），將公鑰檔案上傳到路由器，然後為該使用者匯入：

```ros
/user/ssh-keys/import public-key-file=id_rsa.pub user=admin
```

當至少有一把金鑰分配給某個使用者時，該使用者的密碼登入會被拒絕（在預設的 `password-authentication=yes-if-no-key` 下）。有關支援的金鑰格式的更多資訊，請參閱 [使用者 SSH 金鑰](../authentication-authorization-accounting/user.md#ssh-keys) 一節。

## SSH 用戶端 {#ssh-client}

互動式 [`/system/ssh`](../cli-reference/system/ssh.md) 命令透過 SSH 將路由器連線到遠端主機。它從控制檯使用；對於指令碼和排程器，請使用 [`ssh-exec`](#run-remote-commands-from-scripts)。

### 登入遠端主機 {#log-in-to-a-remote-host}

連線到遠端主機並啟動 SSH 會話。該地址支援 IPv4 和 IPv6：

```ros
/system/ssh 192.168.88.3
/system/ssh 2001:db8:add:1337::beef
```

該命令會傳遞你當前登入的路由器賬戶的使用者名稱。使用 `user=<username>` 以其他使用者身份登入：

```ros
/system/ssh 192.168.88.3 user=noc
/system/ssh 2001:db8:add:1337::beef user=noc
```

### 從路由器的指定地址登入 {#log-in-from-a-specific-address-of-the-router}

要從指定源地址登入主機（例如為了防火牆規則或測試），請使用 `src-address=<ip address>` 引數。該地址支援 IPv4 和 IPv6：

```ros
/system/ssh 192.168.88.3 src-address=192.168.89.2
/system/ssh 2001:db8:add:1337::beef src-address=2001:db8:bad:1000::2
```

在這種情況下，SSH 用戶端會繫結到指定地址，然後向遠端主機發起 SSH 連線。

### 使用 SSH 金鑰登入 {#log-in-with-an-ssh-key}

RouterOS 無法自行生成使用者金鑰對，因此金鑰對必須來自其他地方。可以在你的管理裝置上生成 RSA 或 Ed25519 金鑰對，或者複用路由器自己的主機金鑰對：用 [`/ip/ssh/export-host-key`](../cli-reference/ip/ssh/export-host-key.md) 匯出它，然後匯入匯出的私鑰檔案。

將私鑰檔案上傳到路由器（透過 WinBox 的 Files 選單或透過 SFTP），併為發起傳出連線的使用者匯入它：

```ros
/user/ssh-keys/private/import user=admin private-key-file=id_rsa
```

只有對路由器擁有完全許可權的使用者才能更改 `/user/ssh-keys/private` 下的 `user` 屬性值。

金鑰檔案必須為 PEM 格式（PKCS#1、PKCS#8 或加密的 PKCS#8）。OpenSSH 私鑰格式（"BEGIN OPENSSH PRIVATE KEY"）的金鑰會被拒絕；請使用 `ssh-keygen -m PEM` 生成金鑰，或用 `ssh-keygen -p -m PEM` 轉換現有金鑰。

相應的公鑰必須安裝在 SSH 伺服器端（對於 RouterOS 伺服器，請參閱[使用公鑰登入](#log-in-with-a-public-key)）。匯入私鑰後，SSH 會話無需密碼即可登入：

```ros
/system/ssh 192.168.88.3
```

觀看如何[使用 RSA 金鑰](http://youtube.com/watch?v=8tt7fSvdFRM)或[使用 Ed25519 金鑰](http://youtube.com/watch?v=be-pBwhjRWA)登入。

### 驗證遠端主機金鑰 {#verify-remote-host-keys}

如果不進行驗證，SSH 用戶端會接受任何主機金鑰，這會使連線容易受到路徑上的攻擊者攻擊。用戶端主機金鑰驗證由 [`/ip/ssh`](../cli-reference/ip/ssh/index.md) 中的 `known-hosts-validation` 控制：在新安裝中它預設啟用；從較舊 RouterOS 版本升級的路由器會保留先前的設定，因此在啟用之前，這些路由器上的驗證仍處於關閉狀態。

受信任的伺服器金鑰儲存在 [`/ip/ssh/known-hosts`](../cli-reference/ip/ssh/known-hosts.md) 中。

啟用驗證後，互動式用戶端在首次連線到新伺服器時會詢問，並在確認後固定該金鑰：

```text
host key not trusted: SHA256:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
do you want to trust this host key? <y/n>
```

當伺服器之後提供的金鑰與已固定的金鑰不同時，用戶端不會靜默繼續，而是詢問是否更新已儲存的金鑰：

```text
host key mismatch for 192.168.88.3
old fingerprint: SHA256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
new fingerprint: SHA256:bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
do you want to update the host key? <y/n>
```

非互動式命令無法詢問：對於未知或不匹配的伺服器，`ssh-exec`（以及透過 SFTP 的 fetch）會以 `host key not trusted` 失敗。對於指令碼化連線，請提前固定伺服器金鑰、傳遞 `known-hosts-ignore=yes` 以僅跳過該條命令的驗證，或設定 `known-hosts-trusted-subnets` 以對整段子網（例如管理網路）跳過驗證。

使用伺服器的公鑰提前固定其金鑰——從伺服器管理員處或在工作站上使用 `ssh-keyscan 192.168.88.3` 獲取 OpenSSH 格式的金鑰行（`<type> <base64>`），然後將其新增：

```ros
/ip/ssh/known-hosts/add host=192.168.88.3 key="ssh-ed25519 AAAA..." \
    comment="backup server"
```

對互動式用戶端的信任提示回答 `y` 也會以同樣的方式固定金鑰，因此，在透過一次互動式 `/system/ssh` 登入並確認金鑰之後，原本因 `host key not trusted` 而失敗的指令碼化 `ssh-exec` 便可正常工作。

在停用驗證的情況下，不會詢問或儲存任何主機金鑰，並且會接受任何金鑰。

### 在遠端主機上執行命令 {#run-a-command-on-a-remote-host}

要執行遠端命令，請在登入行末尾提供該命令：

```ros
/system/ssh 192.168.88.3 "/ip/address/print"
/system/ssh 192.168.88.3 command="/ip/address/print"
/system/ssh 2001:db8:add:1337::beef "/ip/address/print"
/system/ssh 2001:db8:add:1337::beef command="/ip/address/print"
```

:::note
MikroTik SSH 伺服器不提供偽終端（OpenSSH 中的 `ssh -T` 模式）。多行命令（例如 `"/ip/address \n add address=1.1.1.1/24"`）在較舊的 RouterOS 版本上會失敗；RouterOS 7.25 及更高版本可以執行它們。
:::

如果你希望透過**指令碼**或**排程器**執行遠端命令，請使用 [`ssh-exec`](../cli-reference/system/ssh-exec.md) 命令。

## 從指令碼執行遠端命令 {#run-remote-commands-from-scripts}

`ssh-exec` 命令是非互動式 SSH 命令，允許你透過指令碼和排程器在遠端裝置上執行命令。引數說明請參閱 [`ssh-exec`](../cli-reference/system/ssh-exec.md) CLI 參考。

### 獲取資訊 {#retrieve-information}

該命令返回兩個值：

- **exit-code**：遠端命令 shell 報告的退出碼——命令執行時為 `0`；執行 `exit` 的命令會設定該退出碼。而 RouterOS 命令的失敗則會以錯誤文字的形式出現在 `output` 中
- **output**：返回遠端執行命令的輸出，包括遠端命令失敗時的錯誤訊息，例如 `input does not match any value...`

**示例：** 以下程式碼從裝置 10.10.10.1 獲取 ether1 的鏈路狀態，並將結果輸出到 "Log"。該示例假設使用者 `remote` 已設定為使用公鑰認證（命令列中不含 `password=`），並且伺服器的主機金鑰已固定，這是新安裝中[主機金鑰驗證](#verify-remote-host-keys)所要求的：

```ros
:local res ([/system/ssh-exec address=10.10.10.1 user=remote \
    command=":put ([/interface ethernet monitor ether1 once as-value]->\"status\")" \
    as-value])
:log info ($res->"output")
```

:::warning
不要在命令列 `password` 引數中放置明文密碼；它會出現在指令碼和命令歷史中。改為在雙方使用者上使用 SSH PKI 認證。

執行該命令的使用者組和指令碼策略需要 **test** 許可權。
:::

觀看如何[透過 SSH 執行命令](http://youtube.com/watch?v=JfGfPSicTzs)。

所有引數請參閱 [`/ip/ssh`](../cli-reference/ip/ssh/index.md)、[`/system/ssh`](../cli-reference/system/ssh.md) 和 [`/system/ssh-exec`](../cli-reference/system/ssh-exec.md) CLI 參考。
