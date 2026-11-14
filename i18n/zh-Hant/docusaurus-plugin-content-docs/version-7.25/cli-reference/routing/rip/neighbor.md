---
sidebar_key: "cli-reference/routing/rip/neighbor"
sidebar_position: 5
title: "neighbor"
sidebar_label: 'neighbor'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/routing/rip/neighbor
captured_at: '2026-11-01T21:25:19+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/rip/neighbor {#routingripneighbor}
**型別：** 目錄

此子選單用於定義要與其交換路由資訊的相鄰路由器。通常，如果網路內組播工作正常，則無需新增鄰居。如果交換路由資訊時出現問題，可以將鄰居路由器新增到列表中。這將強制路由器使用常規單播封包與鄰居交換路由資訊。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="instance" typ="enum"></ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46i)"></ArgTableRow>
<ArgTableRow arg="routes" typ="num"></ArgTableRow>
<ArgTableRow arg="packets-total" typ="num"></ArgTableRow>
<ArgTableRow arg="packets-bad" typ="num"></ArgTableRow>
<ArgTableRow arg="entries-bad" typ="num"></ArgTableRow>
<ArgTableRow arg="last-update" typ="time">自上次更新以來的時間。</ArgTableRow>
</ArgTable>
