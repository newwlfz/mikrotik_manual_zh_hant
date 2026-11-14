---
sidebar_key: "cli-reference/user/ssh-keys/private/index"
sidebar_position: 2
title: "private"
sidebar_label: 'private'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/user/ssh-keys/private
captured_at: '2026-11-01T21:26:13+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## user/ssh-keys/private {#userssh-keysprivate}
**型別：** 目錄

SSH 私鑰用於在到其他裝置的出站 SSH 連線中標識路由器，例如透過 [`/system/ssh`](../../../system/ssh.md) 或 [`/tool/fetch`](../../../tool/fetch.md)。所有屬性均為只讀；金鑰透過 [`/user/ssh-keys/private/import`](./import.md) 新增。完整指南請參閱 [使用者](../../../../authentication-authorization-accounting/user.md)。

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="user" typ="enum">擁有該金鑰的系統使用者。</ArgTableRow>
<ArgTableRow arg="key-type" typ="enum (rsa | ed25519)">金鑰型別：`rsa` 或 `ed25519`。</ArgTableRow>
<ArgTableRow arg="bits" typ="num">金鑰長度（位）。</ArgTableRow>
<ArgTableRow arg="info" typ="string">該金鑰的自由文字標籤。</ArgTableRow>
</ArgTable>
