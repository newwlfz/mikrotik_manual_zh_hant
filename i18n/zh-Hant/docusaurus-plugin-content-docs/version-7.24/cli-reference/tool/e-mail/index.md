---
sidebar_key: "cli-reference/tool/e-mail/index"
sidebar_position: 1
title: "e-mail"
sidebar_label: "e-mail"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/tool/e-mail
captured_at: '2026-11-01T21:30:14+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/e-mail {#toole-mail}
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="server" typ="alt { ipv6: ip6Addr
, ip: ipAddr
, fqdn: string
 }"></ArgTableRow>
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="tls" typ="enum (no | yes | starttls)"></ArgTableRow>
<ArgTableRow arg="vrf" typ="enum"></ArgTableRow>
<ArgTableRow arg="from" typ="string"></ArgTableRow>
<ArgTableRow arg="user" typ="string"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="certificate-verification" typ="enum (no | yes | yes-without-crl)">TLS 證書驗證</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="last-status" typ="enum (none | resolving-dns | in-progress | failed | succeeded)"></ArgTableRow>
<ArgTableRow arg="last-address" typ="alt { ip: ipAddr
, ipv6: ip6Addr
 }"></ArgTableRow>
</ArgTable>
