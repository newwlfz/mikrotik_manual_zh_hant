---
sidebar_key: "cli-reference/interface/list/member"
sidebar_position: 1
title: "member"
sidebar_label: 'member'
source: https://manual.mikrotik.com/docs/cli-reference/interface/list/member
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/list/member {#interfacelistmember}
**型別：** 目錄

靜態介面成員列表。透過 `include` 和 `exclude` 語句動態新增的介面不會出現在此子選單中。

:::info
使用網橋和列表時需謹慎。將網橋新增為成員與新增其所有埠並不相同。將所有從埠新增為成員與新增網橋本身並不相同。這可能影響 Neighbour Discovery 的功能。
:::

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">成員條目已停用。</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態新增的成員。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="list" typ="enum" mandatory="1">成員所屬介面列表的名稱。</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">作為列表成員的介面名稱。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="dynamic" typ="bool">該成員是否為動態新增。</ArgTableRow>
</ArgTable>
