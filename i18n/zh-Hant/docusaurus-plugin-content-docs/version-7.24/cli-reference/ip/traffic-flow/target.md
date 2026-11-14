---
sidebar_key: "cli-reference/ip/traffic-flow/target"
sidebar_position: 3
title: "target"
sidebar_label: "target"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/traffic-flow/target
captured_at: '2026-11-01T21:28:59+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/traffic-flow/target {#iptraffic-flowtarget}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="src-address" typ="alt { ip: ipAddr
, ipv6: ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="dst-address" typ="alt { ip: ipAddr
, ipv6: ip6Addr
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="version" typ="enum (1 | 5 | 9 | ipfix) { 1:1, 5:5, 9:9, ipfix:10 }"></ArgTableRow>
<ArgTableRow arg="v9-template-refresh" typ="num"></ArgTableRow>
<ArgTableRow arg="v9-template-timeout" typ="time"></ArgTableRow>
</ArgTable>
