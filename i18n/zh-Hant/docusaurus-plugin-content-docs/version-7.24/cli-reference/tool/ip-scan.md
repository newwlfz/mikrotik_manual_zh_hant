---
sidebar_key: "cli-reference/tool/ip-scan"
sidebar_position: 9
title: "ip-scan"
sidebar_label: "ip-scan"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/tool/ip-scan
captured_at: '2026-11-01T21:30:15+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/ip-scan {#toolip-scan}
**條件：** !smips
**型別：** 命令

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="D" typ="dhcp">dhcp</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="address-range" typ="ipRange"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="time" typ="num"></ArgTableRow>
<ArgTableRow arg="dns" typ="string"></ArgTableRow>
<ArgTableRow arg="snmp" typ="string"></ArgTableRow>
<ArgTableRow arg="netbios" typ="string"></ArgTableRow>
</ArgTable>
