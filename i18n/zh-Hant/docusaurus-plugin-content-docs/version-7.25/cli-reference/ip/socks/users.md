---
sidebar_key: "cli-reference/ip/socks/users"
sidebar_position: 3
title: "users"
sidebar_label: 'users'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/socks/users
captured_at: '2026-11-01T21:24:27+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/socks/users {#ipsocksusers}
**型別：** 目錄

SOCKS5 使用者名稱/密碼認證使用者，當 [`/ip/socks`](./index.md) 設定了 `auth-method=password` 時使用。新建使用者預設處於啟用狀態。更多資訊請參閱 [SOCKS](../../../network-management/socks/index.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用。該使用者無法透過認證。新建使用者預設處於啟用狀態。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1">用於 SOCKS5 認證的使用者名稱。</ArgTableRow>
<ArgTableRow arg="password" typ="string" mandatory="1">用於 SOCKS5 認證的密碼。不會顯示在 `print` 輸出中。</ArgTableRow>
<ArgTableRow arg="only-one" typ="bool"></ArgTableRow>
<ArgTableRow arg="rate-limit" typ="string">應用於該使用者代理連線的速率限制，單位為位元每秒，例如 `64000`。</ArgTableRow>
</ArgTable>
