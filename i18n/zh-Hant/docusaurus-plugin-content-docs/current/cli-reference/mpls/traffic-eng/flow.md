---
sidebar_key: "cli-reference/mpls/traffic-eng/flow"
sidebar_position: 1
title: "flow"
sidebar_label: 'flow'
source: https://manual.mikrotik.com/docs/cli-reference/mpls/traffic-eng/flow
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## mpls/traffic-eng/flow {#mplstraffic-engflow}
**條件：** !smips
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="N" typ="ingress"></ArgTableRow>
<ArgTableRow arg="E" typ="egress"></ArgTableRow>
<ArgTableRow arg="F" typ="forwarding"></ArgTableRow>
<ArgTableRow arg="R" typ="reservation"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="vrf" typ="enum"></ArgTableRow>
<ArgTableRow arg="session" typ="string"></ArgTableRow>
<ArgTableRow arg="sender" typ="string"></ArgTableRow>
<ArgTableRow arg="label" typ="num"></ArgTableRow>
<ArgTableRow arg="out-labels" typ="multi { array-id, out-label: num
 }"></ArgTableRow>
<ArgTableRow arg="out-nexthop" typ="address (flags=46i)"></ArgTableRow>
<ArgTableRow arg="bw" typ="num"></ArgTableRow>
<ArgTableRow arg="style" typ="enum (unknown | shared | fixed) { unknown:0, shared:1, fixed:2 }"></ArgTableRow>
<ArgTableRow arg="psb" typ="string"></ArgTableRow>
<ArgTableRow arg="blockade" typ="string"></ArgTableRow>
<ArgTableRow arg="resv" typ="string"></ArgTableRow>
<ArgTableRow arg="rsb" typ="string"></ArgTableRow>
</ArgTable>
