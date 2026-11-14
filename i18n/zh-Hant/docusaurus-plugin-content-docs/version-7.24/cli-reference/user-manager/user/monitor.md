---
sidebar_key: "cli-reference/user-manager/user/monitor"
sidebar_position: 4
title: "monitor"
sidebar_label: "monitor"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/user-manager/user/monitor
captured_at: '2026-11-01T21:30:35+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## user-manager/user/monitor {#user-managerusermonitor}
**包：** userman-5
**型別：** 命令

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="total-uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="total-download" typ="num"></ArgTableRow>
<ArgTableRow arg="total-upload" typ="num"></ArgTableRow>
<ArgTableRow arg="active-sessions" typ="num"></ArgTableRow>
<ArgTableRow arg="active-sub-sessions" typ="num"></ArgTableRow>
<ArgTableRow arg="actual-profile" typ="enum"></ArgTableRow>
<ArgTableRow arg="attributes-details" typ="object { attribute-value: super { attribute: enum
, [value] :string
, [value-type] :enum (ip-address | string | uint32 | hex | ip6-prefix | macro)
, [raw-value] :0xstring
 }
 }"></ArgTableRow>
</ArgTable>
