---
sidebar_key: "cli-reference/routing/ospf/area/range"
sidebar_position: 1
title: "range"
sidebar_label: 'range'
source: https://manual.mikrotik.com/docs/cli-reference/routing/ospf/area/range
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/ospf/area/range {#routingospfarearange}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未啟用</ArgTableRow>
<ArgTableRow arg="A" typ="advertise">advertise</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="area" typ="enum" mandatory="1">與該範圍關聯的 OSPF 區域。</ArgTableRow>
<ArgTableRow arg="prefix" typ="address (flags=46/)" mandatory="1">該範圍的網路字首。</ArgTableRow>
<ArgTableRow arg="advertise" typ="bool">是否建立彙總 LSA 並將其通告到相鄰區域。</ArgTableRow>
<ArgTableRow arg="cost" typ="num" unset="1">該範圍將建立的彙總 LSA 的開銷。預設 - 使用所有已使用路由（即落在該範圍內的路由）中的最大開銷。</ArgTableRow>
</ArgTable>
