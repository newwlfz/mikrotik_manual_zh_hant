---
sidebar_key: "cli-reference/certificate/enable-ssl-certificate"
sidebar_position: 9
title: "enable-ssl-certificate"
sidebar_label: 'enable-ssl-certificate'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/certificate/enable-ssl-certificate
captured_at: '2026-11-01T21:21:49+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## certificate/enable-ssl-certificate {#certificateenable-ssl-certificate}
**型別：** 命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="dns-name" typ="string">SSL 證書的域名</ArgTableRow>
<ArgTableRow arg="directory-url" typ="string">ACME 目錄 URL</ArgTableRow>
<ArgTableRow arg="eab-hmac-key" typ="string">base64url 編碼的 EAB hmac 金鑰</ArgTableRow>
<ArgTableRow arg="eab-kid" typ="string">EAB 賬戶 ID</ArgTableRow>
<ArgTableRow arg="reset-private-key" typ="bool">初始化新的私鑰</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="progress" typ="string"></ArgTableRow>
</ArgTable>
