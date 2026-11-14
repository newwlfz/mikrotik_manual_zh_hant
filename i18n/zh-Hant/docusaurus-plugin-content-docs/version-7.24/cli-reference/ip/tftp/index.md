---
sidebar_key: "cli-reference/ip/tftp/index"
sidebar_position: 1
title: "tftp"
sidebar_label: "tftp"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/tftp
captured_at: '2026-11-01T21:29:00+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/tftp {#iptftp}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="ip-addresses" typ="object { ip-addresses: alt { ip6: ip6Prefix
, ip: ipRange
 }
 }"></ArgTableRow>
<ArgTableRow arg="req-filename" typ="string"></ArgTableRow>
<ArgTableRow arg="real-filename" typ="string"></ArgTableRow>
<ArgTableRow arg="allow" typ="bool"></ArgTableRow>
<ArgTableRow arg="read-only" typ="bool"></ArgTableRow>
<ArgTableRow arg="allow-rollover" typ="bool"></ArgTableRow>
<ArgTableRow arg="allow-overwrite" typ="bool"></ArgTableRow>
<ArgTableRow arg="reading-window-size" typ="alt { window-size: enum (none | pipelining) { none:0 }
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="hits" typ="num"></ArgTableRow>
</ArgTable>
