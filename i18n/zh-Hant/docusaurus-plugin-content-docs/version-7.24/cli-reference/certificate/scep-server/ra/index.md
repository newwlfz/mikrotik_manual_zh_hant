---
sidebar_key: "cli-reference/certificate/scep-server/ra/index"
sidebar_position: 1
title: "ra"
sidebar_label: "ra"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/certificate/scep-server/ra
captured_at: '2026-11-01T21:26:28+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## certificate/scep-server/ra {#certificatescep-serverra}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="C" typ="smart-card-key">smart-card-key</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="server-url" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="template" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="challenge-password" typ="string"></ArgTableRow>
<ArgTableRow arg="ca-identity" typ="string"></ArgTableRow>
<ArgTableRow arg="fingerprint-algorithm" typ="enum (sha256 | sha1 | md5)"></ArgTableRow>
<ArgTableRow arg="ra-path" typ="string"></ArgTableRow>
<ArgTableRow arg="ra-transaction-lifetime" typ="time"></ArgTableRow>
<ArgTableRow arg="on-smart-card" typ="bool">將私鑰儲存在智慧卡上</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="req-fingerprint" typ="string"></ArgTableRow>
<ArgTableRow arg="ca-fingerprint" typ="string"></ArgTableRow>
<ArgTableRow arg="status" typ="string"></ArgTableRow>
</ArgTable>
