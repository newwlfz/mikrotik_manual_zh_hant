---
sidebar_key: "cli-reference/iot/bluetooth/connections/characteristics"
sidebar_position: 2
title: "characteristics"
sidebar_label: "characteristics"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/iot/bluetooth/connections/characteristics
captured_at: '2026-11-01T21:28:11+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## iot/bluetooth/connections/characteristics {#iotbluetoothconnectionscharacteristics}
**包：** iot
**型別：** 目錄

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="uuid" typ="string"></ArgTableRow>
<ArgTableRow arg="handle" typ="num"></ArgTableRow>
<ArgTableRow arg="service-name" typ="string"></ArgTableRow>
<ArgTableRow arg="service-uuid" typ="string"></ArgTableRow>
<ArgTableRow arg="props" typ="multi { array-id, props: enum (bcast | read | write-no-resp | write | notify | indicate | write-signed | ext) { bcast:0x01, read:0x02, write-no-resp:0x04, write:0x08, notify:0x10, indicate:0x20, write-signed:0x40, ext:0x80 }
 }"></ArgTableRow>
<ArgTableRow arg="pdev" typ="enum"></ArgTableRow>
</ArgTable>
