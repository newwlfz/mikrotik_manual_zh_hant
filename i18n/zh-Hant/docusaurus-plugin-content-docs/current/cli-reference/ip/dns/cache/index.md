---
sidebar_key: "cli-reference/ip/dns/cache"
title: "cache"
sidebar_label: 'cache'
source: https://manual.mikrotik.com/docs/cli-reference/ip/dns/cache
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/dns/cache {#ipdnscache}
**型別：** 目錄

路由器可以從其快取中給出的應答：上游應答和靜態條目。要檢視完整列表（包括為靜態條目生成的 PTR 記錄），請參見 [`all`](./all.md)。有關概述，請參見 [DNS](../../../../network-management/dns.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="S" typ="static">該記錄來自 [`/ip/dns/static`](../static.md) 中的靜態條目。靜態記錄在此處顯示的 TTL 為 0s。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="type" typ="enum (A | NS | CNAME | MX | TXT | AAAA | SRV) { A:1, NS:2, CNAME:5, MX:15, TXT:16, AAAA:28, SRV:33 }">記錄型別。</ArgTableRow>
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
 }">記錄的資料，例如 `A` 記錄的地址。</ArgTableRow>
<ArgTableRow arg="name" typ="string">記錄的域名。</ArgTableRow>
<ArgTableRow arg="ttl" typ="time">記錄從快取中過期前的剩餘時間。該時間會倒計時，並且永遠不會超過 [`/ip/dns`](../index.md) 中的 `cache-max-ttl`。</ArgTableRow>
</ArgTable>
