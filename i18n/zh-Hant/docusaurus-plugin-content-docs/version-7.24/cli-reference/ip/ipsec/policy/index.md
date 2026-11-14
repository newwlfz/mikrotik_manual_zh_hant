---
sidebar_key: "cli-reference/ip/ipsec/policy/index"
sidebar_position: 2
title: "policy"
sidebar_label: "policy"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/ipsec/policy
captured_at: '2026-11-01T21:28:48+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/ipsec/policy {#ipipsecpolicy}
**型別：**目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="T" typ="template">template</ArgTableRow>
<ArgTableRow arg="B" typ="backup">backup</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">無效</ArgTableRow>
<ArgTableRow arg="A" typ="active">已啟用</ArgTableRow>
<ArgTableRow arg="*" typ="default">default</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="peer" typ="multi { array-id, peer: enum
 }">自動啟用對等體建立連線，與 shunt 策略一起使用</ArgTableRow>
<ArgTableRow arg="tunnel" typ="bool"></ArgTableRow>
<ArgTableRow arg="group" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="src-address" typ="alt { prefix6: ip6Prefix
, prefix4: ipPrefix
 }"></ArgTableRow>
<ArgTableRow arg="src-port" typ="num"></ArgTableRow>
<ArgTableRow arg="dst-address" typ="alt { prefix6: ip6Prefix
, prefix4: ipPrefix
 }"></ArgTableRow>
<ArgTableRow arg="dst-port" typ="num"></ArgTableRow>
<ArgTableRow arg="protocol" typ="enum (all) { all:255 }"></ArgTableRow>
<ArgTableRow arg="action" typ="enum (encrypt | discard | none) { encrypt:2, discard:0, none:1 }"></ArgTableRow>
<ArgTableRow arg="level" typ="enum (require | use | unique) { require:2, use:1, unique:3 }"></ArgTableRow>
<ArgTableRow arg="ipsec-protocols" typ="enum (ah | esp) { ah:1, esp:2 }">使用哪種 IPsec 協定</ArgTableRow>
<ArgTableRow arg="sa-src-address" typ="alt { ipv6: ip6Addr
, ip: ipAddr
 }">端點地址</ArgTableRow>
<ArgTableRow arg="sa-dst-address" typ="alt { ipv6: ip6Addr
, ip: ipAddr
 }">端點地址</ArgTableRow>
<ArgTableRow arg="proposal" typ="enum"></ArgTableRow>
<ArgTableRow arg="template" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="ph2-count" typ="num"></ArgTableRow>
<ArgTableRow arg="ph2-state" typ="enum (spawning | starting | ready-to-send | getspi-sent | getspi-done | msg1-sent | ready-to-establish | commiting | adding-sa | established | expired | no-phase2) { spawning:0, starting:1, ready-to-send:2, getspi-sent:3, getspi-done:4, msg1-sent:5, ready-to-establish:6, commiting:7, adding-sa:8, established:9, expired:10, no-phase2:11 }"></ArgTableRow>
</ArgTable>
