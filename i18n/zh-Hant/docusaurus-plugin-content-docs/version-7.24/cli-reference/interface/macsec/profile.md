---
sidebar_key: "cli-reference/interface/macsec/profile"
sidebar_position: 2
title: "profile"
sidebar_label: "profile"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/macsec/profile
captured_at: '2026-11-01T21:27:29+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/macsec/profile {#interfacemacsecprofile}
**條件：** !smips
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="*" typ="default">default</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="ciphers" typ="multi { cipher: enum (aes-gcm-128 | aes-gcm-xpn-128)
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="server-priority" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="default-name" typ="string"></ArgTableRow>
</ArgTable>
