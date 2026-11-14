---
sidebar_key: "cli-reference/caps-man/security"
sidebar_position: 14
title: "security"
sidebar_label: 'security'
source: https://manual.mikrotik.com/docs/cli-reference/caps-man/security
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## caps-man/security {#caps-mansecurity}
**包：** wireless-rep
**型別：** 目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="authentication-types" typ="ubit (wpa-psk, wpa2-psk, wpa-eap, wpa2-eap)" unset="1"></ArgTableRow>
<ArgTableRow arg="encryption" typ="ubit (aes-ccm, tkip)" unset="1"></ArgTableRow>
<ArgTableRow arg="group-encryption" typ="enum (aes-ccm | tkip)" unset="1"></ArgTableRow>
<ArgTableRow arg="group-key-update" typ="time"></ArgTableRow>
<ArgTableRow arg="passphrase" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="eap-methods" typ="multi { array-id, method: enum (eap-tls | passthrough) { eap-tls:13, passthrough:0xffffffff }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="eap-radius-accounting" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="tls-mode" typ="enum (verify-certificate | dont-verify-certificate | no-certificates | verify-certificate-with-crl)"></ArgTableRow>
<ArgTableRow arg="tls-certificate" typ="enum (none) { none:0xffffffff }"></ArgTableRow>
<ArgTableRow arg="disable-pmkid" typ="bool" unset="1"></ArgTableRow>
</ArgTable>
