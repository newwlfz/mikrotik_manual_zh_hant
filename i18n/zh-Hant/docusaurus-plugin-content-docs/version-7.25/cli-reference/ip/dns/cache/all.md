---
sidebar_key: "cli-reference/ip/dns/cache/all"
sidebar_position: 1
title: "all"
sidebar_label: 'all'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/dns/cache/all
captured_at: '2026-11-01T21:23:55+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/dns/cache/all {#ipdnscacheall}
**型別：** 目錄

DNS 快取中的所有記錄，包括路由器為靜態條目建立的 PTR 記錄，以及解析器在內部保留的記錄。有關概述，請參閱 [DNS](../../../../network-management/dns.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="S" typ="static">該記錄來自 [`/ip/dns/static`](../static.md) 中的靜態條目，例如為靜態 `A` 或 `AAAA` 條目建立的 PTR 記錄。</ArgTableRow>
<ArgTableRow arg="N" typ="negative">快取的否定應答：名稱或記錄型別不存在。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">記錄的域名。</ArgTableRow>
<ArgTableRow arg="type" typ="enum (A | NS | MD | MF | CNAME | SOA | MB | MG | MR | NULL | WKS | PTR | HINFO | MINFO | MX | TXT | AAAA | SRV) { A:1, NS:2, MD:3, MF:4, CNAME:5, SOA:6, MB:7, MG:8, MR:9, NULL:10, WKS:11, PTR:12, HINFO:13, MINFO:14, MX:15, TXT:16, AAAA:28, SRV:33 }">記錄型別。</ArgTableRow>
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
 }">記錄的資料，例如 `A` 記錄的地址或 `PTR` 記錄的目標名稱。</ArgTableRow>
<ArgTableRow arg="ttl" typ="time">記錄從快取中過期前的剩餘時間。</ArgTableRow>
<ArgTableRow arg="responsible" typ="string">區域管理員的電子郵件地址，來自 `SOA` 記錄。</ArgTableRow>
<ArgTableRow arg="serial" typ="num">區域的序列號，來自 `SOA` 記錄。</ArgTableRow>
<ArgTableRow arg="refresh" typ="num">區域的重新整理間隔（以秒為單位），來自 `SOA` 記錄。</ArgTableRow>
<ArgTableRow arg="retry" typ="num">區域的重試間隔（以秒為單位），來自 `SOA` 記錄。</ArgTableRow>
<ArgTableRow arg="expire" typ="num">區域的過期時間（以秒為單位），來自 `SOA` 記錄。</ArgTableRow>
<ArgTableRow arg="minimum" typ="num">區域的最小 TTL（以秒為單位），來自 `SOA` 記錄。</ArgTableRow>
</ArgTable>
