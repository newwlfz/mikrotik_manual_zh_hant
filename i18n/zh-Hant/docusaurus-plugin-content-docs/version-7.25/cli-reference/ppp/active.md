---
sidebar_key: "cli-reference/ppp/active"
sidebar_position: 2
title: "active"
sidebar_label: 'active'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ppp/active
captured_at: '2026-11-01T21:24:58+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ppp/active {#pppactive}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="R" typ="radius">radius</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="service" typ="enum (any | async | pptp | pppoe | l2tp | ovpn | sstp) { any:0, async:1, pptp:2, pppoe:3, l2tp:5, ovpn:6, sstp:7 }"></ArgTableRow>
<ArgTableRow arg="caller-id" typ="string"></ArgTableRow>
<ArgTableRow arg="address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="encoding" typ="string"></ArgTableRow>
<ArgTableRow arg="session-id" typ="num"></ArgTableRow>
<ArgTableRow arg="limit-bytes-in" typ="num"></ArgTableRow>
<ArgTableRow arg="limit-bytes-out" typ="num"></ArgTableRow>
</ArgTable>
