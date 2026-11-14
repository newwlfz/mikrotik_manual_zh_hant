---
sidebar_key: "cli-reference/ip/ipsec/installed-sa/index"
sidebar_position: 2
title: "installed-sa"
sidebar_label: 'installed-sa'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/ipsec/installed-sa
captured_at: '2026-11-01T21:24:10+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/ipsec/installed-sa {#ipipsecinstalled-sa}
**型別：** 目錄

此選單提供有關已安裝安全關聯的資訊，包括金鑰。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="S" typ="seen-traffic">SA 是否已有流量透過。</ArgTableRow>
<ArgTableRow arg="H" typ="hw-aead">是否使用硬體 AEAD 加速。</ArgTableRow>
<ArgTableRow arg="A" typ="AH">SA 是否使用 AH 協定。</ArgTableRow>
<ArgTableRow arg="E" typ="ESP">SA 是否使用 ESP 協定。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="spi" typ="num">安全引數索引值。</ArgTableRow>
<ArgTableRow arg="state" typ="enum (larval | mature | dying | dead) { larval:0, mature:1, dying:2, dead:3 }">當前 SA 狀態。</ArgTableRow>
<ArgTableRow arg="auth-algorithm" typ="enum (none | md5 | sha1 | sha256 | sha512) { none:0, md5:2, sha1:3, sha256:5, sha512:7 }">認證演算法。</ArgTableRow>
<ArgTableRow arg="enc-algorithm" typ="enum (none | des | 3des | null | aes-cbc | aes-ctr | aes-gcm | blowfish | twofish | camellia | chacha20poly1305) { none:0, des:2, 3des:3, null:11, aes-cbc:12, aes-ctr:13, aes-gcm:20, blowfish:7, twofish:253, camellia:22, chacha20poly1305:254 }">加密演算法。</ArgTableRow>
<ArgTableRow arg="enc-key-size" typ="num">加密金鑰長度（以位為單位）。</ArgTableRow>
<ArgTableRow arg="auth-key" typ="string">認證金鑰值。</ArgTableRow>
<ArgTableRow arg="enc-key" typ="string">加密金鑰值。</ArgTableRow>
<ArgTableRow arg="addtime" typ="date">SA 的新增時間。</ArgTableRow>
<ArgTableRow arg="expires-in" typ="time">SA 到期剩餘時間。</ArgTableRow>
<ArgTableRow arg="add-lifetime" typ="composite { soft: time
, hard: time
 }">
SA 的新增生存時間，格式為 soft/hard：
- soft - 在此時間段之後，IKE 將嘗試建立新的 SA；
- hard - 在此時間段之後，該 SA 將被刪除。
</ArgTableRow>
<ArgTableRow arg="current-bytes" typ="num">SA 已處理的位元組數。</ArgTableRow>
<ArgTableRow arg="current-packets" typ="num">SA 已處理的封包數。</ArgTableRow>
<ArgTableRow arg="invalid-packets" typ="num">無效封包數。</ArgTableRow>
<ArgTableRow arg="replay" typ="num">重放視窗大小。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="src-address" typ="super { src-address: alt { ipv6: ip6Addr
, ip: ipAddr
 }
, [port] :num
 }">源地址和埠。</ArgTableRow>
<ArgTableRow arg="dst-address" typ="super { dst-address: alt { ipv6: ip6Addr
, ip: ipAddr
 }
, [port] :num
 }">目標地址和埠。</ArgTableRow>
</ArgTable>
