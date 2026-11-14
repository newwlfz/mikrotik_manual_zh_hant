---
sidebar_key: "cli-reference/iot/bluetooth/connections/async-data"
title: "async-data"
sidebar_label: 'async-data'
source: https://manual.mikrotik.com/docs/cli-reference/iot/bluetooth/connections/async-data
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## iot/bluetooth/connections/async-data {#iotbluetoothconnectionsasync-data}
**軟體包：** iot
**型別：** 目錄

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="pdev" typ="string"></ArgTableRow>
<ArgTableRow arg="uuid" typ="string"></ArgTableRow>
<ArgTableRow arg="data-text" typ="string"></ArgTableRow>
<ArgTableRow arg="data-hex" typ="string"></ArgTableRow>
<ArgTableRow arg="data-bytes" typ="multi { array-id, value: num
 }"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (notification | indication) { notification:0x01, indication:0x02 }"></ArgTableRow>
<ArgTableRow arg="time" typ="date"></ArgTableRow>
</ArgTable>
