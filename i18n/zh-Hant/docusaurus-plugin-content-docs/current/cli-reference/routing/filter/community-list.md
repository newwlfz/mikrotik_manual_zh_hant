---
sidebar_key: "cli-reference/routing/filter/community-list"
sidebar_position: 4
title: "community-list"
sidebar_label: 'community-list'
source: https://manual.mikrotik.com/docs/cli-reference/routing/filter/community-list
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/filter/community-list {#routingfiltercommunity-list}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="list" typ="enum" mandatory="1">引用名稱。</ArgTableRow>
<ArgTableRow arg="communities" typ="object">
以 **公認** 名稱或以下格式表示的 community 列表：`as:number`，其中每一段可以是 [0..65535] 範圍內的整數。
接受的 **公認** 名稱：
- `accept-own`
- `graceful-shutdown`
- `no-advertise`
- `no-llgr`
- `route-filter-6`
- `accept-own-nh`
- `internet`
- `no-export`
- `no-peer`
- `route-filter-xlate-4`
- `blackhole`
- `llgr-stale`
- `local-as`
- `route-filter-4`
- `route-filter-xlate-6`
</ArgTableRow>
<ArgTableRow arg="regexp" typ="string">用於匹配 community 的正則表示式匹配器。正則表示式條目用於匹配，並由 `delete`/`filter` 使用。只有具體的 community 值會被 `append`/`set` 使用。</ArgTableRow>
</ArgTable>
