---
sidebar_key: "cli-reference/routing/filter/community-ext-list"
sidebar_position: 2
title: "community-ext-list"
sidebar_label: "community-ext-list"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/routing/filter/community-ext-list
captured_at: '2026-11-01T21:29:30+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/filter/community-ext-list {#routingfiltercommunity-ext-list}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="list" typ="enum" mandatory="1">引用名稱。</ArgTableRow>
<ArgTableRow arg="communities" typ="object">
擴充套件 community 列表，以 **raw** 整數值或型別化格式 `type:value` 表示，其中 type 可以是：
- `rt` - route-target
- `soo` -  起源站點

該值取決於 type。
</ArgTableRow>
<ArgTableRow arg="regexp" typ="string">用於匹配 community 的正則表示式匹配器。僅包含 regexp 引數的 community 集合不能用於追加/刪除 community。</ArgTableRow>
</ArgTable>
