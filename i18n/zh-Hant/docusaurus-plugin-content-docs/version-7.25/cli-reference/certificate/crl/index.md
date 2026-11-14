---
sidebar_key: "cli-reference/certificate/crl/index"
sidebar_position: 3
title: "crl"
sidebar_label: 'crl'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/certificate/crl
captured_at: '2026-11-01T21:21:49+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## certificate/crl {#certificatecrl}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="E" typ="expired">已過期</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">無效</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="url" typ="string" mandatory="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="cert" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="trust-store" typ="alt { all: enum (all)
, component: ubit (ipsec, wpa-eap, capsman, fetch, sstp, ovpn, mqtt, email, netwatch, radius, container, userman, lora, wiliot, openflow, tr069, dot1x, dns, www, api, reverse-proxy, logging)
 }"></ArgTableRow>
<ArgTableRow arg="num" typ="num"></ArgTableRow>
<ArgTableRow arg="revoked" typ="num"></ArgTableRow>
<ArgTableRow arg="next-update" typ="date"></ArgTableRow>
<ArgTableRow arg="last-update" typ="date"></ArgTableRow>
<ArgTableRow arg="akid" typ="string"></ArgTableRow>
<ArgTableRow arg="fingerprint" typ="string"></ArgTableRow>
<ArgTableRow arg="signature" typ="string"></ArgTableRow>
</ArgTable>
