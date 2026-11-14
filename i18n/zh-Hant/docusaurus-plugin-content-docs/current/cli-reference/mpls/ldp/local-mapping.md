---
sidebar_key: "cli-reference/mpls/ldp/local-mapping"
sidebar_position: 4
title: "local-mapping"
sidebar_label: 'local-mapping'
source: https://manual.mikrotik.com/docs/cli-reference/mpls/ldp/local-mapping
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## mpls/ldp/local-mapping {#mplsldplocal-mapping}
**條件：** !smips
**型別：**目錄

此子選單顯示路由器本地繫結到各路由的標籤。如果不需要動態使用 LDP，也可以在此選單中配置靜態對映。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">繫結是否處於活動狀態，以及能否被選為轉發的候選項。</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">該條目是否為動態新增。</ArgTableRow>
<ArgTableRow arg="E" typ="egress">egress</ArgTableRow>
<ArgTableRow arg="G" typ="gateway">目標是否可透過閘道器到達。</ArgTableRow>
<ArgTableRow arg="L" typ="local">目標在路由器上是否本地可達。</ArgTableRow>
<ArgTableRow arg="V" typ="vpls">vpls</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="vrf" typ="enum" unset="1">此對映所屬的 VRF 表的名稱。</ArgTableRow>
<ArgTableRow arg="dst-address" typ="address (flags=46/)" unset="1" mandatory="1">標籤所分配到的目標字首。</ArgTableRow>
<ArgTableRow arg="label" typ="alt { label-enum: enum (expl-null | alert | expl-null6 | impl-null) { expl-null:0, alert:1, expl-null6:2, impl-null:3 }
, label-num: num [16 .. 1048576]
 }" mandatory="1">分配給目標的標籤號。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="adv-path" typ="string"></ArgTableRow>
<ArgTableRow arg="peers" typ="object { peer-id: composite { id: ipAddr
, namespace: num
 }
 }">此條目被通告到的對等體的 IP 地址和標籤空間。</ArgTableRow>
<ArgTableRow arg="pw-fec" typ="string"></ArgTableRow>
</ArgTable>
