---
sidebar_key: "cli-reference/ipv6/dhcp-relay/option"
sidebar_position: 2
title: "option"
sidebar_label: "option"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ipv6/dhcp-relay/option
captured_at: '2026-11-01T21:29:02+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ipv6/dhcp-relay/option {#ipv6dhcp-relayoption}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="*" typ="default">default</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="code" typ="num" mandatory="1"></ArgTableRow>
<ArgTableRow arg="value" typ="string"></ArgTableRow>
<ArgTableRow arg="only-if-mac-available" typ="bool">僅當報文源自用戶端（而非另一箇中繼）且可推匯出 MAC 地址時，才會新增該選項</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="raw-value" typ="string"></ArgTableRow>
</ArgTable>
