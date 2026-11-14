---
sidebar_key: "cli-reference/ip/dhcp-client/option"
sidebar_position: 1
title: "option"
sidebar_label: "option"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/dhcp-client/option
captured_at: '2026-11-01T21:28:26+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/dhcp-client/option {#ipdhcp-clientoption}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="*" typ="default">default</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="code" typ="alt { number: num [1 .. 254]
, option: enum (hostname | vendor-specific | vendor-class-id | client-id) { hostname:12, vendor-specific:43, vendor-class-id:60, client-id:61 }
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="value" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="raw-value" typ="string"></ArgTableRow>
</ArgTable>
