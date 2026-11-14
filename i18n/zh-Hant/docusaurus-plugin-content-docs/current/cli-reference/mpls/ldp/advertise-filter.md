---
sidebar_key: "cli-reference/mpls/ldp/advertise-filter"
sidebar_position: 2
title: "advertise-filter"
sidebar_label: 'advertise-filter'
source: https://manual.mikrotik.com/docs/cli-reference/mpls/ldp/advertise-filter
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## mpls/ldp/advertise-filter {#mplsldpadvertise-filter}
**條件：** !smips
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="vrf" typ="enum (any) { any:0xffffffff }" unset="1"></ArgTableRow>
<ArgTableRow arg="prefix" typ="address (flags=46/)" unset="1">要匹配的字首。</ArgTableRow>
<ArgTableRow arg="neighbor" typ="address (flags=46/)" unset="1">此過濾器適用的鄰居。</ArgTableRow>
<ArgTableRow arg="advertise" typ="bool" unset="1">是否向鄰居通告指定字首的標籤繫結。如果引數為 unset，則不會通告匹配的字首。</ArgTableRow>
</ArgTable>
