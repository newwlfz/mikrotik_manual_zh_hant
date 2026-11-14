---
sidebar_key: "cli-reference/tool/e-mail/send"
sidebar_position: 1
title: "send"
sidebar_label: "send"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/tool/e-mail/send
captured_at: '2026-11-01T21:30:14+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/e-mail/send {#toole-mailsend}
**型別：** 命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="server" typ="alt { ipv6: ip6Addr
, ip: ipAddr
, fqdn: string
 }"></ArgTableRow>
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="to" typ="multi { array-id, to: string
 }"></ArgTableRow>
<ArgTableRow arg="cc" typ="multi { array-id, cc: string
 }"></ArgTableRow>
<ArgTableRow arg="from" typ="string"></ArgTableRow>
<ArgTableRow arg="subject" typ="string"></ArgTableRow>
<ArgTableRow arg="body" typ="string"></ArgTableRow>
<ArgTableRow arg="file" typ="multi { array-id, file: file
 }"></ArgTableRow>
<ArgTableRow arg="user" typ="string"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="tls" typ="enum (no | yes | starttls)"></ArgTableRow>
<ArgTableRow arg="certificate-verification" typ="enum (no | yes | yes-without-crl)">TLS 證書驗證</ArgTableRow>
</ArgTable>
