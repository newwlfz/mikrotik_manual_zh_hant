---
sidebar_key: "cli-reference/iot/bluetooth/scanners"
title: "scanners"
sidebar_label: 'scanners'
source: https://manual.mikrotik.com/docs/cli-reference/iot/bluetooth/scanners
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## iot/bluetooth/scanners {#iotbluetoothscanners}
**軟體包：** iot
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="type" typ="enum (passive | active) { passive:0, active:1 }"></ArgTableRow>
<ArgTableRow arg="interval" typ="num"></ArgTableRow>
<ArgTableRow arg="window" typ="num"></ArgTableRow>
<ArgTableRow arg="own-address-type" typ="enum (public | random-static | rpa-fallback-to-public | rpa-fallback-to-random) { public:0, random-static:1, rpa-fallback-to-public:2, rpa-fallback-to-random:3 }">掃描請求中使用的地址型別</ArgTableRow>
<ArgTableRow arg="filter-policy" typ="enum (default | whitelist) { default:0, whitelist:1 }"></ArgTableRow>
<ArgTableRow arg="filter-duplicates" typ="enum (off | keep-oldest | keep-newest | keep-unique) { off:0, keep-oldest:1, keep-newest:2, keep-unique:3 }">丟棄來自同一廣播者的重複廣播</ArgTableRow>
<ArgTableRow arg="phy" typ="enum (1M | 2M | CODED) { 1M:0, 2M:1, CODED:2 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="device" typ="enum"></ArgTableRow>
</ArgTable>
