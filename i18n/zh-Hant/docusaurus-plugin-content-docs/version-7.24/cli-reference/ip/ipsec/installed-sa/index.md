---
sidebar_key: "cli-reference/ip/ipsec/installed-sa/index"
sidebar_position: 2
title: "installed-sa"
sidebar_label: "installed-sa"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/ipsec/installed-sa
captured_at: '2026-11-01T21:28:42+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/ipsec/installed-sa {#ipipsecinstalled-sa}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="S" typ="seen-traffic">seen-traffic</ArgTableRow>
<ArgTableRow arg="H" typ="hw-aead">hw-aead</ArgTableRow>
<ArgTableRow arg="A" typ="AH">AH</ArgTableRow>
<ArgTableRow arg="E" typ="ESP">ESP</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="spi" typ="num"></ArgTableRow>
<ArgTableRow arg="state" typ="enum (larval | mature | dying | dead) { larval:0, mature:1, dying:2, dead:3 }"></ArgTableRow>
<ArgTableRow arg="auth-algorithm" typ="enum (none | md5 | sha1 | sha256 | sha512) { none:0, md5:2, sha1:3, sha256:5, sha512:7 }"></ArgTableRow>
<ArgTableRow arg="enc-algorithm" typ="enum (none | des | 3des | null | aes-cbc | aes-ctr | aes-gcm | blowfish | twofish | camellia | chacha20poly1305) { none:0, des:2, 3des:3, null:11, aes-cbc:12, aes-ctr:13, aes-gcm:20, blowfish:7, twofish:253, camellia:22, chacha20poly1305:254 }"></ArgTableRow>
<ArgTableRow arg="enc-key-size" typ="num"></ArgTableRow>
<ArgTableRow arg="auth-key" typ="string"></ArgTableRow>
<ArgTableRow arg="enc-key" typ="string"></ArgTableRow>
<ArgTableRow arg="addtime" typ="date"></ArgTableRow>
<ArgTableRow arg="expires-in" typ="time"></ArgTableRow>
<ArgTableRow arg="add-lifetime" typ="composite { soft: time
, hard: time
 }"></ArgTableRow>
<ArgTableRow arg="current-bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="current-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="invalid-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="replay" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="src-address" typ="super { src-address: alt { ipv6: ip6Addr
, ip: ipAddr
 }
, [port] :num
 }"></ArgTableRow>
<ArgTableRow arg="dst-address" typ="super { dst-address: alt { ipv6: ip6Addr
, ip: ipAddr
 }
, [port] :num
 }"></ArgTableRow>
</ArgTable>
