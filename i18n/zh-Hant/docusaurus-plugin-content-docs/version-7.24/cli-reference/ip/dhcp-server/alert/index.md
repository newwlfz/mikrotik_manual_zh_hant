---
sidebar_key: "cli-reference/ip/dhcp-server/alert/index"
sidebar_position: 1
title: "alert"
sidebar_label: "alert"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/dhcp-server/alert
captured_at: '2026-11-01T21:28:27+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/dhcp-server/alert {#ipdhcp-serveralert}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">無效</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="valid-server" typ="multi { mac-address: macAddr
 }"></ArgTableRow>
<ArgTableRow arg="on-alert" typ="alt { script: string
 }"></ArgTableRow>
<ArgTableRow arg="alert-timeout" typ="alt { symbolic-names: enum (none) { none:0 }
, time-interval: time
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="unknown-server" typ="multi { mac-address: macAddr
 }"></ArgTableRow>
</ArgTable>
