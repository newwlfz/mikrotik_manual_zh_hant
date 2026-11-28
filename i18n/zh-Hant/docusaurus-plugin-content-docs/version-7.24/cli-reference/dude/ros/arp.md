---
title: "arp"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/dude/ros/arp
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

-----------

## dude/ros/arp 
**套件：** dude
**類型：** 目錄

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
<ArgTableRow arg="H" typ="DHCP"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
<ArgTableRow arg="P" typ="published"></ArgTableRow>
<ArgTableRow arg="C" typ="complete"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="device" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="interface" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="published" typ="bool"></ArgTableRow>
</ArgTable>
