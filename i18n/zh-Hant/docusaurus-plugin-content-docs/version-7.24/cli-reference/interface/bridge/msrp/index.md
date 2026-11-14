---
sidebar_position: 999
title: "msrp"
sidebar_label: "msrp"
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## interface/bridge/msrp {#interfacebridgemsrp}
**條件：** MSRP_ENABLE
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="bridge" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="rank" typ="num"></ArgTableRow>
<ArgTableRow arg="stream-id" typ="composite { mac: macAddr
, address: num
 }"></ArgTableRow>
<ArgTableRow arg="talker" typ="iface_enum { none }"></ArgTableRow>
<ArgTableRow arg="listener" typ="iface_enum { none }"></ArgTableRow>
<ArgTableRow arg="dst-mac" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="vid" typ="num"></ArgTableRow>
<ArgTableRow arg="max-frame-size" typ="num"></ArgTableRow>
<ArgTableRow arg="max-interval-frames" typ="num"></ArgTableRow>
<ArgTableRow arg="priority" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="age" typ="time"></ArgTableRow>
<ArgTableRow arg="active-talker" typ="iface_enum { none }"></ArgTableRow>
<ArgTableRow arg="active-listener" typ="iface_enum { none }"></ArgTableRow>
<ArgTableRow arg="debug-info" typ="string"></ArgTableRow>
</ArgTable>
