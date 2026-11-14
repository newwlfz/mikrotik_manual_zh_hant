---
sidebar_key: "cli-reference/user/ssh-keys/index"
sidebar_position: 2
title: "ssh-keys"
sidebar_label: "ssh-keys"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/user/ssh-keys
captured_at: '2026-11-01T21:30:36+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## user/ssh-keys {#userssh-keys}
**型別：** 目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="user" typ="enum"></ArgTableRow>
<ArgTableRow arg="key" typ="string">僅用於新增新金鑰</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="key-type" typ="enum (rsa | ed25519 | ed25519-sk)"></ArgTableRow>
<ArgTableRow arg="bits" typ="num"></ArgTableRow>
<ArgTableRow arg="info" typ="string"></ArgTableRow>
<ArgTableRow arg="fingerprint" typ="string"></ArgTableRow>
</ArgTable>
