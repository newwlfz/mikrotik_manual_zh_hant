---
sidebar_key: "cli-reference/interface/lte/apn"
sidebar_position: 1
title: "apn"
sidebar_label: 'apn'
source: https://manual.mikrotik.com/docs/cli-reference/interface/lte/apn
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/lte/apn {#interfacelteapn}
**條件：** !smips
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="*" typ="default">default</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="apn" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="use-peer-dns" typ="bool"></ArgTableRow>
<ArgTableRow arg="use-network-apn" typ="bool">在 LTE 模式下使用網路提供的 APN</ArgTableRow>
<ArgTableRow arg="add-default-route" typ="bool"></ArgTableRow>
<ArgTableRow arg="default-route-distance" typ="num"></ArgTableRow>
<ArgTableRow arg="ip-type" typ="enum (ipv4 | ipv6 | auto)">請求的 PDN 型別</ArgTableRow>
<ArgTableRow arg="authentication" typ="enum (none | pap | chap)"></ArgTableRow>
<ArgTableRow arg="user" typ="string"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="passthrough-interface" typ="iface_enum { none:0 }"></ArgTableRow>
<ArgTableRow arg="passthrough-mac" typ="alt { auto: enum (static | auto)
, passthrough-peer: macAddr
 }">auto 將從第一個封包中學習 MAC</ArgTableRow>
<ArgTableRow arg="passthrough-subnet-size" typ="alt { subnet-enum: enum (auto | 32) { auto:0, 32:32 }
, subnet-size: num [16 .. 32]
 }"></ArgTableRow>
<ArgTableRow arg="ipv6-interface" typ="iface_enum { none:0 }">用於通告 IPv6 字首的介面</ArgTableRow>
</ArgTable>
