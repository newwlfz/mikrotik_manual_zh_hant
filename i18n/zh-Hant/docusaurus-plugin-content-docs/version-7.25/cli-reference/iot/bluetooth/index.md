---
sidebar_key: "cli-reference/iot/bluetooth/index"
sidebar_position: 4
title: "bluetooth"
sidebar_label: 'bluetooth'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/iot/bluetooth
captured_at: '2026-11-01T21:23:32+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## iot/bluetooth {#iotbluetooth}
**包：** iot
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="offline"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="random-static-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="antenna" typ="enum (internal | external) { internal:0, external:1 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="public-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="rx-bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-errors" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-errors" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-evt" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-cmd" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-acl" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-acl" typ="num"></ArgTableRow>
</ArgTable>
