---
sidebar_key: "cli-reference/user/ssh-keys/import"
sidebar_position: 1
title: "import"
sidebar_label: 'import'
source: https://manual.mikrotik.com/docs/cli-reference/user/ssh-keys/import
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## user/ssh-keys/import {#userssh-keysimport}
**型別：** 命令

從路由器根目錄中的檔案匯入 SSH 公鑰，並將其分配給使用者。接受的格式：OpenSSH 單行格式、PKCS#1 PEM（"BEGIN RSA PUBLIC KEY"）和 PKCS#8/SPKI PEM（"BEGIN PUBLIC KEY"）。完整指南請參閱 [使用者](../../../authentication-authorization-accounting/user.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="public-key-file" typ="file">路由器根目錄中金鑰檔案的名稱。</ArgTableRow>
<ArgTableRow arg="user" typ="enum">要分配金鑰的系統使用者。</ArgTableRow>
<ArgTableRow arg="info" typ="string">金鑰的自由文字標籤。</ArgTableRow>
</ArgTable>
