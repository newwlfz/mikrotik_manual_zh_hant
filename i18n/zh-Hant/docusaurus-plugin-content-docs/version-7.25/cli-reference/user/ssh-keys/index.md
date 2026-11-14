---
sidebar_key: "cli-reference/user/ssh-keys/index"
sidebar_position: 2
title: "ssh-keys"
sidebar_label: 'ssh-keys'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/user/ssh-keys
captured_at: '2026-11-01T21:26:12+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## user/ssh-keys {#userssh-keys}
**型別：** 目錄

分配給使用者的 SSH 公鑰；這些金鑰用於認證這些使用者的傳入 SSH 登入。當用戶至少分配了一個金鑰時，SSH 伺服器會拒絕該使用者的密碼認證，並且僅提供公鑰認證。完整指南請參閱 [使用者](../../../authentication-authorization-accounting/user.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="user" typ="enum">該金鑰分配到的系統使用者。</ArgTableRow>
<ArgTableRow arg="info" typ="string">金鑰的自由文字標籤。使用 `key` 新增金鑰時，貼上的 OpenSSH 金鑰字串中的末尾註釋會成為該金鑰的 `info`，並覆蓋此引數。</ArgTableRow>
<ArgTableRow arg="key" typ="string">公鑰字串，僅在新增新金鑰時設定。僅接受 OpenSSH 單行格式；PEM 塊會被拒絕。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="key-type" typ="enum (rsa | ed25519 | ed25519-sk)">金鑰型別：`rsa`、`ed25519` 或 `ed25519-sk`。</ArgTableRow>
<ArgTableRow arg="bits" typ="num">金鑰長度（以位為單位）。</ArgTableRow>
<ArgTableRow arg="fingerprint" typ="string">金鑰的 SHA256 指紋（base64 格式，例如 `SHA256:...`）。</ArgTableRow>
</ArgTable>
