---
sidebar_key: "cli-reference/ip/ipsec/identity"
sidebar_position: 2
title: "identity"
sidebar_label: "identity"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/ipsec/identity
captured_at: '2026-11-01T21:28:43+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/ipsec/identity {#ipipsecidentity}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="peer" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="auth-method" typ="enum (pre-shared-key | digital-signature | eap | eap-radius | pre-shared-key-xauth | rsa-key | rsa-signature-hybrid)"></ArgTableRow>
<ArgTableRow arg="eap-methods" typ="multi { array-id, method: enum (eap-tls | eap-ttls | eap-peap | eap-mschapv2)
 }">EAP 方法</ArgTableRow>
<ArgTableRow arg="mode-config" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="notrack-chain" typ="string">為 dynamic 策略新增 dynamic raw notrack 規則</ArgTableRow>
<ArgTableRow arg="my-id" typ="alt { string: composite { type: enum (fqdn | user-fqdn | key-id)
, data: string
 }
, address: composite { type: enum (address)
, data: alt { ipv6: ip6Addr
, ip: ipAddr
 }
 }
, other: enum (auto | dn)
 }"></ArgTableRow>
<ArgTableRow arg="remote-id" typ="alt { string: composite { type: enum (fqdn | user-fqdn | key-id)
, data: string
 }
, address: composite { type: enum (address)
, data: alt { ipv6: ip6Addr
, ip: ipAddr
 }
 }
, auto: enum (auto | ignore | dn)
 }"></ArgTableRow>
<ArgTableRow arg="match-by" typ="enum (remote-id | certificate)">響應方的身份查詢方法</ArgTableRow>
<ArgTableRow arg="key" typ="enum ()">用於 raw RSA 認證的金鑰（僅 ike1）</ArgTableRow>
<ArgTableRow arg="remote-key" typ="enum ()">用於 raw RSA 認證的遠端金鑰（僅 ike1）</ArgTableRow>
<ArgTableRow arg="secret" typ="string">預共享金鑰</ArgTableRow>
<ArgTableRow arg="certificate" typ="multi { array-id, certificate: enum
 }">本地證書</ArgTableRow>
<ArgTableRow arg="remote-certificate" typ="enum (none) { none:-1 }">當對端未傳送證書時使用此證書</ArgTableRow>
<ArgTableRow arg="username" typ="string">EAP 或 XAuth 使用者</ArgTableRow>
<ArgTableRow arg="password" typ="string">EAP 或 XAuth 密碼</ArgTableRow>
<ArgTableRow arg="generate-policy" typ="enum (no | port-override | port-strict)"></ArgTableRow>
<ArgTableRow arg="policy-template-group" typ="enum"></ArgTableRow>
</ArgTable>
