---
sidebar_key: "cli-reference/ip/hotspot/index"
sidebar_position: 4
title: "hotspot"
sidebar_label: "hotspot"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/hotspot
captured_at: '2026-11-01T21:28:39+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/hotspot {#iphotspot}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">無效</ArgTableRow>
<ArgTableRow arg="S" typ="HTTPS">HTTPS</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="interface" typ="alt { interface: iface_enum
, interface: iface_enum
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="address-pool" typ="enum (none) { none:0 }"></ArgTableRow>
<ArgTableRow arg="profile" typ="enum"></ArgTableRow>
<ArgTableRow arg="idle-timeout" typ="alt { symbolic-names: enum (none) { none:0 }
, time-interval: time
 }"></ArgTableRow>
<ArgTableRow arg="keepalive-timeout" typ="alt { symbolic-names: enum (none) { none:0 }
, time-interval: time
 }"></ArgTableRow>
<ArgTableRow arg="login-timeout" typ="alt { symbolic-names: enum (none) { none:0 }
, time-interval: time
 }"></ArgTableRow>
<ArgTableRow arg="addresses-per-mac" typ="enum (unlimited) { unlimited:0 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="ip-of-dns-name" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="proxy-status" typ="string"></ArgTableRow>
</ArgTable>
