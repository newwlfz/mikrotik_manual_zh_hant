---
sidebar_key: "cli-reference/ip/reverse-proxy"
sidebar_position: 18
title: "reverse-proxy"
sidebar_label: "reverse-proxy"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/reverse-proxy
captured_at: '2026-11-01T21:28:55+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/reverse-proxy {#ipreverse-proxy}
**條件：** !smips
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="sni" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="ip-address" typ="alt { ipv6: ip6Addr
, ip: ipAddr
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="port" typ="num" mandatory="1"></ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="vrf" typ="enum"></ArgTableRow>
</ArgTable>
