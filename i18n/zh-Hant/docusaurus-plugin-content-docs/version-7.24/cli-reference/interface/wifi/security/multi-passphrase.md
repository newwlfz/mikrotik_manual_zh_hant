---
sidebar_key: "cli-reference/interface/wifi/security/multi-passphrase"
sidebar_position: 1
title: "multi-passphrase"
sidebar_label: "multi-passphrase"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/wifi/security/multi-passphrase
captured_at: '2026-11-01T21:27:52+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/wifi/security/multi-passphrase {#interfacewifisecuritymulti-passphrase}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="E" typ="expired">已過期</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="group" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="passphrase" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="expires" typ="date" unset="1"></ArgTableRow>
<ArgTableRow arg="isolation" typ="bool" unset="1"></ArgTableRow>
</ArgTable>
