---
sidebar_key: "cli-reference/ip/ipsec/peer"
sidebar_position: 6
title: "peer"
sidebar_label: "peer"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/ipsec/peer
captured_at: '2026-11-01T21:28:46+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/ipsec/peer {#ipipsecpeer}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
<ArgTableRow arg="R" typ="responder">responder</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="address" typ="alt { prefix6: ip6Prefix
, prefix4: ipPrefix
, dns: string
 }"></ArgTableRow>
<ArgTableRow arg="local-address" typ="alt { ipv6: ip6Addr
, ip: ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="passive" typ="bool">被動對等體不會發起連線</ArgTableRow>
<ArgTableRow arg="port" typ="num">對等體埠</ArgTableRow>
<ArgTableRow arg="profile" typ="enum"></ArgTableRow>
<ArgTableRow arg="exchange-mode" typ="enum (main | aggressive | ike2)"></ArgTableRow>
<ArgTableRow arg="send-initial-contact" typ="bool"></ArgTableRow>
<ArgTableRow arg="ppk-secret" typ="string">帶 "static-ppk-secret" ID 的靜態 PPK 金鑰，當此對等體不存在一次性金鑰/psk 時使用，請確保該金鑰具有 256 位熵</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="current-address" typ="alt { ipv6: ip6Addr
, ip: ipAddr
 }"></ArgTableRow>
</ArgTable>
