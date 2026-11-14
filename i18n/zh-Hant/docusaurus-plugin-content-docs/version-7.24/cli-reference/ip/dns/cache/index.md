---
sidebar_key: "cli-reference/ip/dns/cache/index"
sidebar_position: 3
title: "cache"
sidebar_label: "cache"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/dns/cache
captured_at: '2026-11-01T21:28:30+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/dns/cache {#ipdnscache}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="S" typ="static">靜態</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="type" typ="enum (A | NS | CNAME | MX | TXT | AAAA | SRV) { A:1, NS:2, CNAME:5, MX:15, TXT:16, AAAA:28, SRV:33 }"></ArgTableRow>
<ArgTableRow arg="data" typ="alt { address: ipAddr
, name: string
, info: composite { rmail: string
, email: string
 }
, mx: composite { preference: num
, exchange: string
 }
, srv: composite { port: num
, target: string
 }
, soa-mname: string
, address6: ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="ttl" typ="time"></ArgTableRow>
</ArgTable>
