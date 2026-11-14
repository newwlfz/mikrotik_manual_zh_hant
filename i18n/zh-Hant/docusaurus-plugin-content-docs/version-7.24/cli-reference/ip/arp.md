---
sidebar_key: "cli-reference/ip/arp"
sidebar_position: 2
title: "arp"
sidebar_label: "arp"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/arp
captured_at: '2026-11-01T21:28:24+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/arp {#iparp}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">無效</ArgTableRow>
<ArgTableRow arg="H" typ="dhcp">dhcp</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
<ArgTableRow arg="P" typ="published">published</ArgTableRow>
<ArgTableRow arg="C" typ="complete">complete</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="published" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
<ArgTableRow arg="vrf" typ="enum"></ArgTableRow>
</ArgTable>
