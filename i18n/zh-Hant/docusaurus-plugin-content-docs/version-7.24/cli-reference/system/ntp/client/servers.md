---
sidebar_key: "cli-reference/system/ntp/client/servers"
sidebar_position: 2
title: "servers"
sidebar_label: "servers"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/system/ntp/client/servers
captured_at: '2026-11-01T21:29:55+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/ntp/client/servers {#systemntpclientservers}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="address" typ="address (flags=46D)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="min-poll" typ="num"></ArgTableRow>
<ArgTableRow arg="max-poll" typ="num"></ArgTableRow>
<ArgTableRow arg="iburst" typ="bool"></ArgTableRow>
<ArgTableRow arg="auth-key" typ="enum (none) { none:0 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="resolved-address" typ="address (flags=46)"></ArgTableRow>
</ArgTable>
