---
sidebar_key: "cli-reference/ip/kid-control/device/index"
sidebar_position: 1
title: "device"
sidebar_label: "device"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/kid-control/device
captured_at: '2026-11-01T21:28:49+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/kid-control/device {#ipkid-controldevice}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
<ArgTableRow arg="B" typ="blocked">blocked</ArgTableRow>
<ArgTableRow arg="L" typ="limited">limited</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未啟用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="all" typ="switch"></ArgTableRow>
<ArgTableRow arg="static" typ="switch"></ArgTableRow>
<ArgTableRow arg="dynamic" typ="switch"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr" mandatory="1"></ArgTableRow>
<ArgTableRow arg="user" typ="enum () { :0xffffffff }" mandatory="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="ip-address" typ="object { server: alt { ip: ipAddr
, ipv6: ip6Addr
 }
 }"></ArgTableRow>
<ArgTableRow arg="activity" typ="string"></ArgTableRow>
<ArgTableRow arg="rate-down" typ="num"></ArgTableRow>
<ArgTableRow arg="rate-up" typ="num"></ArgTableRow>
<ArgTableRow arg="bytes-down" typ="num"></ArgTableRow>
<ArgTableRow arg="bytes-up" typ="num"></ArgTableRow>
<ArgTableRow arg="idle-time" typ="time"></ArgTableRow>
</ArgTable>
