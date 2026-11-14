---
sidebar_key: "cli-reference/user/ssh-keys/private/import"
sidebar_position: 1
title: "import"
sidebar_label: 'import'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/user/ssh-keys/private/import
captured_at: '2026-11-01T21:26:13+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## user/ssh-keys/private/import {#userssh-keysprivateimport}
**型別：** 命令

從路由器根目錄下的檔案中匯入私鑰 SSH 金鑰。接受的格式：PKCS#1 PEM RSA（"BEGIN RSA PRIVATE KEY"）、PKCS#8（"BEGIN PRIVATE KEY"）以及加密的 PKCS#8（"BEGIN ENCRYPTED PRIVATE KEY"，需要 `passphrase`）。OpenSSH 格式的私鑰（"BEGIN OPENSSH PRIVATE KEY"）會被拒絕。完整指南請參見 [使用者](../../../../authentication-authorization-accounting/user.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="private-key-file" typ="file">路由器根目錄中金鑰檔案的名稱。</ArgTableRow>
<ArgTableRow arg="user" typ="enum">擁有該金鑰的系統使用者。</ArgTableRow>
<ArgTableRow arg="passphrase" typ="string">加密金鑰檔案的密碼短語。</ArgTableRow>
<ArgTableRow arg="info" typ="string">金鑰的自由文字標籤。</ArgTableRow>
</ArgTable>
