---
sidebar_key: "cli-reference/user-manager/user/group"
sidebar_position: 3
title: "group"
sidebar_label: "group"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/user-manager/user/group
captured_at: '2026-11-01T21:30:34+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## user-manager/user/group {#user-managerusergroup}
**軟體包：** userman-5
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="*" typ="default"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="outer-auths" typ="ubit (pap, chap, mschap1, mschap2, eap-tls, eap-ttls, eap-peap, eap-mschap2)"></ArgTableRow>
<ArgTableRow arg="inner-auths" typ="ubit (ttls-pap, ttls-chap, ttls-mschap1, ttls-mschap2, peap-mschap2)"></ArgTableRow>
<ArgTableRow arg="attributes" typ="object { attribute-value: super { attribute: enum
, [value] :string
 }
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="default-name" typ="string"></ArgTableRow>
</ArgTable>
