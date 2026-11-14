---
sidebar_key: "cli-reference/mpls/ldp/accept-filter"
sidebar_position: 1
title: "accept-filter"
sidebar_label: 'accept-filter'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/mpls/ldp/accept-filter
captured_at: '2026-11-01T21:24:47+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## mpls/ldp/accept-filter {#mplsldpaccept-filter}
**條件：** !smips
**型別：** 目錄

應從 LDP 鄰居接受的標籤繫結列表。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="vrf" typ="enum (any) { any:0xffffffff }" unset="1"></ArgTableRow>
<ArgTableRow arg="prefix" typ="address (flags=46/)" unset="1">要匹配的字首。</ArgTableRow>
<ArgTableRow arg="neighbor" typ="address (flags=46/)" unset="1">此過濾器適用的鄰居。</ArgTableRow>
<ArgTableRow arg="accept" typ="bool" unset="1">是否接受來自鄰居的、針對指定字首的標籤繫結。如果引數未設定，則不會接受匹配的字首。</ArgTableRow>
</ArgTable>
