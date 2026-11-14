---
sidebar_key: "cli-reference/routing/pimsm/igmp-interface-template"
sidebar_position: 2
title: "igmp-interface-template"
sidebar_label: 'igmp-interface-template'
source: https://manual.mikrotik.com/docs/cli-reference/routing/pimsm/igmp-interface-template
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/pimsm/igmp-interface-template {#routingpimsmigmp-interface-template}
**條件：** !smips
**型別：** 目錄

IGMP 介面模板選單用於定義哪些介面執行 IGMP/MLD 查詢器以及將使用哪些查詢器引數。它獨立於 PIM [`interface-template`](./interface-template.md) 進行配置，因此一個介面可以執行 PIM、IGMP/MLD 或兩者兼有。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">該模板已停用。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="instance" typ="enum" mandatory="1">此模板所屬的 PIM 例項。</ArgTableRow>
<ArgTableRow arg="interfaces" typ="object { interface: iface_enum
 }" unset="1">遵循此模板並執行 IGMP/MLD 的介面。</ArgTableRow>
<ArgTableRow arg="robustness" typ="num">此模板的介面上 IGMP/MLD 查詢器的穩健性值。</ArgTableRow>
<ArgTableRow arg="query-interval" typ="time">在此模板的介面上傳送 IGMP/MLD 通用查詢的頻率。</ArgTableRow>
<ArgTableRow arg="query-response-interval" typ="time">在此模板的介面上，IGMP/MLD 通用查詢中通告的最大響應時間。</ArgTableRow>
<ArgTableRow arg="last-member-query-interval" typ="time">在此模板的介面上，IGMP/MLD 組特定查詢中通告的響應時間。</ArgTableRow>
</ArgTable>
