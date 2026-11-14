---
sidebar_key: "cli-reference/ip/dhcp-server/matcher"
sidebar_position: 4
title: "matcher"
sidebar_label: "matcher"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/dhcp-server/matcher
captured_at: '2026-11-01T21:28:28+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/dhcp-server/matcher {#ipdhcp-servermatcher}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="server" typ="enum (all)" mandatory="1">全域性或單個伺服器</ArgTableRow>
<ArgTableRow arg="address-pool" typ="enum (static-only)">用於此條目的地址池</ArgTableRow>
<ArgTableRow arg="option-set" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="code" typ="alt { number: num [1 .. 254]
, option: enum (vendor-specific) { vendor-specific:43 }
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="value" typ="string" mandatory="1">要匹配的選項內容，為字串或帶 0x 字首的十六進位制</ArgTableRow>
<ArgTableRow arg="matching-type" typ="enum (exact | substring)" mandatory="1"></ArgTableRow>
</ArgTable>
