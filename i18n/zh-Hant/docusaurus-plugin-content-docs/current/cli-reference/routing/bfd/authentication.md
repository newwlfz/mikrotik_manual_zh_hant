---
sidebar_key: "cli-reference/routing/bfd/authentication"
sidebar_position: 1
title: "authentication"
sidebar_label: 'authentication'
source: https://manual.mikrotik.com/docs/cli-reference/routing/bfd/authentication
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/bfd/authentication {#routingbfdauthentication}
**條件：** BFD_AUTHENTICATION
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未啟用</ArgTableRow>
<ArgTableRow arg="T" typ="transmit">transmit</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="keyring" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="key-id" typ="num" mandatory="1"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (none | simple-password | keyed-md5 | meticulous-keyed-md5 | keyed-sha1 | meticulous-keyed-sha1)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="key" typ="string"></ArgTableRow>
<ArgTableRow arg="transmit-after" typ="date"></ArgTableRow>
<ArgTableRow arg="accept-before" typ="date"></ArgTableRow>
</ArgTable>
