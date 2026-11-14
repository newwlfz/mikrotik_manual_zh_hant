---
sidebar_key: "cli-reference/dude/ros/arp"
sidebar_position: 2
title: "arp"
sidebar_label: 'arp'
source: https://manual.mikrotik.com/docs/cli-reference/dude/ros/arp
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## dude/ros/arp {#duderosarp}
**包：** dude
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
<ArgTableRow arg="H" typ="DHCP"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
<ArgTableRow arg="P" typ="published"></ArgTableRow>
<ArgTableRow arg="C" typ="complete"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="device" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="interface" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="published" typ="bool"></ArgTableRow>
</ArgTable>
