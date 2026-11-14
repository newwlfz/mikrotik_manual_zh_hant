---
sidebar_key: "cli-reference/certificate/scep-server/requests"
title: "requests"
sidebar_label: 'requests'
source: https://manual.mikrotik.com/docs/cli-reference/certificate/scep-server/requests
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## certificate/scep-server/requests {#certificatescep-serverrequests}
**型別：** 目錄

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="authority" typ="alt { ca: enum
, ra: enum
 }"></ArgTableRow>
<ArgTableRow arg="status" typ="enum (pending | granted | denied | authorized | waiting | failed | issued | invalid) { pending:1, granted:2, denied:3, authorized:4, waiting:10, failed:11, issued:12, invalid:13 }"></ArgTableRow>
<ArgTableRow arg="created" typ="date"></ArgTableRow>
<ArgTableRow arg="transaction-id" typ="string"></ArgTableRow>
<ArgTableRow arg="req-fingerprint" typ="string"></ArgTableRow>
<ArgTableRow arg="country" typ="string"></ArgTableRow>
<ArgTableRow arg="state" typ="string"></ArgTableRow>
<ArgTableRow arg="locality" typ="string"></ArgTableRow>
<ArgTableRow arg="organization" typ="string"></ArgTableRow>
<ArgTableRow arg="unit" typ="string"></ArgTableRow>
<ArgTableRow arg="common-name" typ="string"></ArgTableRow>
<ArgTableRow arg="serial-number" typ="string"></ArgTableRow>
<ArgTableRow arg="subject-alt-name" typ="object { alt-name: composite { type: enum (IP | DNS | email)
, value: alt { ip: alt { ipv6: ip6Addr
, ip: ipAddr
 }
, string: string
 }
 }
 }"></ArgTableRow>
</ArgTable>
