---
sidebar_key: "cli-reference/mpls/traffic-eng/path"
sidebar_position: 3
title: "path"
sidebar_label: 'path'
source: https://manual.mikrotik.com/docs/cli-reference/mpls/traffic-eng/path
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## mpls/traffic-eng/path {#mplstraffic-engpath}
**條件：** !smips
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="use-cspf" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="setup-priority" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="holding-priority" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="record-route" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="affinity-include-all" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="affinity-include-any" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="affinity-exclude" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="reoptimize-interval" typ="time" unset="1"></ArgTableRow>
<ArgTableRow arg="hops" typ="multi { array-id, array-id, hop: super { address: address (flags=46)
, [strict] /enum (loose | strict)
 }
 }" unset="1"></ArgTableRow>
</ArgTable>
