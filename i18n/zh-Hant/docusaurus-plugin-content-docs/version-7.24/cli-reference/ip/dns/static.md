---
sidebar_key: "cli-reference/ip/dns/static"
sidebar_position: 4
title: "static"
sidebar_label: "static"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/dns/static
captured_at: '2026-11-01T21:28:31+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/dns/static {#ipdnsstatic}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="regexp" typ="string"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (NXDOMAIN | A | NS | CNAME | MX | TXT | AAAA | SRV | FWD) { NXDOMAIN:65281, A:1, NS:2, CNAME:5, MX:15, TXT:16, AAAA:28, SRV:33, FWD:65280 }"></ArgTableRow>
<ArgTableRow arg="forward-to" typ="alt { forwarder: enum
, ip: ipAddr
, ipv6: ip6Addr
, host: string
 }"></ArgTableRow>
<ArgTableRow arg="address" typ="alt { ip: ipAddr
, ipv6: ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="mx-preference" typ="num"></ArgTableRow>
<ArgTableRow arg="mx-exchange" typ="string"></ArgTableRow>
<ArgTableRow arg="cname" typ="string"></ArgTableRow>
<ArgTableRow arg="text" typ="string"></ArgTableRow>
<ArgTableRow arg="ns" typ="string"></ArgTableRow>
<ArgTableRow arg="srv-priority" typ="num"></ArgTableRow>
<ArgTableRow arg="srv-weight" typ="num"></ArgTableRow>
<ArgTableRow arg="srv-port" typ="num"></ArgTableRow>
<ArgTableRow arg="srv-target" typ="string"></ArgTableRow>
<ArgTableRow arg="ttl" typ="time"></ArgTableRow>
<ArgTableRow arg="match-subdomain" typ="bool"></ArgTableRow>
<ArgTableRow arg="address-list" typ="string"></ArgTableRow>
</ArgTable>
