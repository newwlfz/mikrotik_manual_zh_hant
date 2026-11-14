---
sidebar_key: "cli-reference/certificate/import"
sidebar_position: 11
title: "import"
sidebar_label: 'import'
source: https://manual.mikrotik.com/docs/cli-reference/certificate/import
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## certificate/import {#certificateimport}
**型別：** 命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="file-name" typ="file"></ArgTableRow>
<ArgTableRow arg="pem" typ="string">從貼上的 PEM 字串中匯入證書或私鑰；當提供 passphrase 時，接受加密的私鑰</ArgTableRow>
<ArgTableRow arg="passphrase" typ="string"></ArgTableRow>
<ArgTableRow arg="trusted" typ="bool">標記為受信任</ArgTableRow>
<ArgTableRow arg="trust-store" typ="alt { all: enum (all)
, component: ubit (ipsec, wpa-eap, capsman, fetch, sstp, ovpn, mqtt, email, netwatch, radius, container, userman, lora, wiliot, openflow, tr069, dot1x, dns, www, api, reverse-proxy, logging)
 }"></ArgTableRow>
<ArgTableRow arg="no-key-export" typ="bool">禁止匯出私鑰</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="certificates-imported" typ="num"></ArgTableRow>
<ArgTableRow arg="private-keys-imported" typ="num"></ArgTableRow>
<ArgTableRow arg="files-imported" typ="num"></ArgTableRow>
<ArgTableRow arg="decryption-failures" typ="num"></ArgTableRow>
<ArgTableRow arg="keys-with-no-certificate" typ="num"></ArgTableRow>
<ArgTableRow arg="keys-decrypted" typ="num"></ArgTableRow>
</ArgTable>
