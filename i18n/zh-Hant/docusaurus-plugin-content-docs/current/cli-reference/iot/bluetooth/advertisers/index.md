---
sidebar_key: "cli-reference/iot/bluetooth/advertisers"
title: "advertisers"
sidebar_label: 'advertisers'
source: https://manual.mikrotik.com/docs/cli-reference/iot/bluetooth/advertisers
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## iot/bluetooth/advertisers {#iotbluetoothadvertisers}
**軟體包：** iot
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="min-interval" typ="num"></ArgTableRow>
<ArgTableRow arg="max-interval" typ="num"></ArgTableRow>
<ArgTableRow arg="own-address-type" typ="enum (public | random-static | rpa-fallback-to-public | rpa-fallback-to-random)">AdvA 欄位中使用的地址型別</ArgTableRow>
<ArgTableRow arg="channel-map" typ="ubit (37, 38, 39)"></ArgTableRow>
<ArgTableRow arg="phy" typ="enum (1M | 2M | CODED) { 1M:0, 2M:1, CODED:2 }"></ArgTableRow>
<ArgTableRow arg="legacy" typ="bool"></ArgTableRow>
<ArgTableRow arg="ad-structures" typ="multi { array-id, structure: enum
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="device" typ="enum"></ArgTableRow>
<ArgTableRow arg="ad-size" typ="num"></ArgTableRow>
</ArgTable>
