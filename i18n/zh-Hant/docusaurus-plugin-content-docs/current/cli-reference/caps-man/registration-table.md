---
sidebar_key: "cli-reference/caps-man/registration-table"
sidebar_position: 12
title: "registration-table"
sidebar_label: 'registration-table'
source: https://manual.mikrotik.com/docs/cli-reference/caps-man/registration-table
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## caps-man/registration-table {#caps-manregistration-table}
**軟體包：** wireless-rep
**型別：** 目錄

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="ssid" typ="string"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="radio-name" typ="string"></ArgTableRow>
<ArgTableRow arg="tx-rate" typ="string"></ArgTableRow>
<ArgTableRow arg="rx-rate" typ="string"></ArgTableRow>
<ArgTableRow arg="tx-signal" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-signal" typ="num"></ArgTableRow>
<ArgTableRow arg="uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="packets" typ="composite { tx: num
, rx: num
 }"></ArgTableRow>
<ArgTableRow arg="bytes" typ="composite { tx: num
, rx: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-rate-set" typ="string"></ArgTableRow>
<ArgTableRow arg="eap-identity" typ="string"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num"></ArgTableRow>
<ArgTableRow arg="last-ip" typ="ipAddr"></ArgTableRow>
</ArgTable>
