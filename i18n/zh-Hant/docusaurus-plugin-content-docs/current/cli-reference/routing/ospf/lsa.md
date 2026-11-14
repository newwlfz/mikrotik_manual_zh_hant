---
sidebar_key: "cli-reference/routing/ospf/lsa"
sidebar_position: 5
title: "lsa"
sidebar_label: 'lsa'
source: https://manual.mikrotik.com/docs/cli-reference/routing/ospf/lsa
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/ospf/lsa {#routingospflsa}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="S" typ="self-originated">該 LSA 是否由路由器自身發起。</ArgTableRow>
<ArgTableRow arg="F" typ="flushing">flushing</ArgTableRow>
<ArgTableRow arg="W" typ="wraparound">wraparound</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="instance" typ="enum"></ArgTableRow>
<ArgTableRow arg="area" typ="enum">此 LSA 所屬的區域。</ArgTableRow>
<ArgTableRow arg="link" typ="address (flags=4i)"></ArgTableRow>
<ArgTableRow arg="link-instance-id" typ="num"></ArgTableRow>
<ArgTableRow arg="type" typ="string"></ArgTableRow>
<ArgTableRow arg="originator" typ="ipAddr">LSA 記錄的發起者。</ArgTableRow>
<ArgTableRow arg="id" typ="ipAddr">LSA 記錄 ID</ArgTableRow>
<ArgTableRow arg="sequence" typ="num">某條鏈路的 LSA 已更新次數。</ArgTableRow>
<ArgTableRow arg="age" typ="num">上次更新發生在多久以前（以秒為單位）。</ArgTableRow>
<ArgTableRow arg="checksum" typ="num"></ArgTableRow>
<ArgTableRow arg="body" typ="string"></ArgTableRow>
</ArgTable>
