---
sidebar_key: "cli-reference/ip/smb/users"
sidebar_position: 2
title: "users"
sidebar_label: 'users'
source: https://manual.mikrotik.com/docs/cli-reference/ip/smb/users
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/smb/users {#ipsmbusers}
**條件：** !smips
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="D" typ="dynamic">該條目會自動建立。</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">該使用者已被停用，無法登入。</ArgTableRow>
<ArgTableRow arg="*" typ="default">該條目是由系統建立的預設條目。</ArgTableRow>
<ArgTableRow arg="r" typ="read-only">該使用者對共享具有 read-only 訪問許可權。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1">SMB 服務使用者的登入名。</ArgTableRow>
<ArgTableRow arg="password" typ="string">SMB 使用者的密碼。</ArgTableRow>
<ArgTableRow arg="read-only" typ="bool">使用者是否對共享具有 read-only 訪問許可權。預設值：yes。</ArgTableRow>
</ArgTable>
