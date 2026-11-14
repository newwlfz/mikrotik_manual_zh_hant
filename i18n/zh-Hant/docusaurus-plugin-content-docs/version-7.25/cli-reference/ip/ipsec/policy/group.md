---
sidebar_key: "cli-reference/ip/ipsec/policy/group"
sidebar_position: 1
title: "group"
sidebar_label: 'group'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/ipsec/policy/group
captured_at: '2026-11-01T21:24:12+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/ipsec/policy/group {#ipipsecpolicygroup}
**型別：** 目錄

此選單允許你建立策略模板所使用的額外策略組。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="*" typ="default">該項是否為預設項。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1">組名稱。</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum">此組中的策略所適用的介面。</ArgTableRow>
</ArgTable>
