---
sidebar_key: "cli-reference/routing/filter/community-large-list"
sidebar_position: 3
title: "community-large-list"
sidebar_label: "community-large-list"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/routing/filter/community-large-list
captured_at: '2026-11-01T21:29:29+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/filter/community-large-list {#routingfiltercommunity-large-list}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="list" typ="enum" mandatory="1">引用名稱。</ArgTableRow>
<ArgTableRow arg="communities" typ="object">以如下格式表示的大型社群列表：`admin:value1:value2`，其中每個部分可以是 [0..4294967295] 範圍內的整數。</ArgTableRow>
<ArgTableRow arg="regexp" typ="string">用於匹配社群的正則表示式匹配器。僅使用 regexp 引數設定的社群集合不能用於追加/刪除社群。</ArgTableRow>
</ArgTable>
