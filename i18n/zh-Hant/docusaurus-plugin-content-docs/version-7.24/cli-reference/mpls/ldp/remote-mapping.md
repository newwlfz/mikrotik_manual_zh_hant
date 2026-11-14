---
sidebar_key: "cli-reference/mpls/ldp/remote-mapping"
sidebar_position: 6
title: "remote-mapping"
sidebar_label: "remote-mapping"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/mpls/ldp/remote-mapping
captured_at: '2026-11-01T21:29:15+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## mpls/ldp/remote-mapping {#mplsldpremote-mapping}
**條件：** !smips
**型別：** 目錄

子選單顯示從其他路由器接收的路由的標籤繫結。如果無意動態使用 LDP，可以配置靜態對映。此表用於構建轉發表。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">繫結是否處於活動狀態並可被選為轉發候選。</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">條目是否為動態新增。</ArgTableRow>
<ArgTableRow arg="V" typ="vpls">vpls</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="vrf" typ="enum" unset="1">此對映所屬的 VRF 表名稱。</ArgTableRow>
<ArgTableRow arg="dst-address" typ="address (flags=46/)" mandatory="1">標籤分配到的目標字首。</ArgTableRow>
<ArgTableRow arg="label" typ="alt { label-enum: enum (expl-null | alert | expl-null6 | impl-null) { expl-null:0, alert:1, expl-null6:2, impl-null:3 }
, label-num: num [16 .. 1048576]
 }" mandatory="1">分配給目標的標籤編號。</ArgTableRow>
<ArgTableRow arg="nexthop" typ="address (flags=46i)" mandatory="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="peer" typ="object { peer-id: composite { id: ipAddr
, namespace: num
 }
 }"></ArgTableRow>
<ArgTableRow arg="path" typ="string"></ArgTableRow>
<ArgTableRow arg="pw-fec" typ="string"></ArgTableRow>
</ArgTable>
