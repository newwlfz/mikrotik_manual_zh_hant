---
sidebar_key: "cli-reference/iot/bluetooth/scanners/advertisements/index"
sidebar_position: 2
title: "advertisements"
sidebar_label: 'advertisements'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/iot/bluetooth/scanners/advertisements
captured_at: '2026-11-01T21:23:35+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## iot/bluetooth/scanners/advertisements {#iotbluetoothscannersadvertisements}
**包：** iot
**型別：** 目錄

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="device" typ="enum"></ArgTableRow>
<ArgTableRow arg="pdu-type" typ="enum (adv-ind | adv-direct-ind | adv-scan-ind | adv-noconn-ind | scan-rsp | unknown) { adv-ind:0, adv-direct-ind:1, adv-scan-ind:2, adv-noconn-ind:3, scan-rsp:4, unknown:5 }"></ArgTableRow>
<ArgTableRow arg="time" typ="date"></ArgTableRow>
<ArgTableRow arg="epoch" typ="num">自 Unix 紀元以來的毫秒數</ArgTableRow>
<ArgTableRow arg="address-type" typ="enum (public | random) { public:0, random:1 }"></ArgTableRow>
<ArgTableRow arg="address" typ="macAddr">廣播者 Bluetooth 地址</ArgTableRow>
<ArgTableRow arg="rssi" typ="num">訊號強度</ArgTableRow>
<ArgTableRow arg="length" typ="num">廣播資料長度</ArgTableRow>
<ArgTableRow arg="data" typ="string">十六進位制格式的廣播資料</ArgTableRow>
<ArgTableRow arg="phy" typ="enum (1M | 2M | CODED-S8 | CODED-S2 | NONE) { 1M:0, 2M:1, CODED-S8:2, CODED-S2:3, NONE:4 }">廣播主 PHY</ArgTableRow>
<ArgTableRow arg="phy-secondary" typ="enum (1M | 2M | CODED-S8 | CODED-S2 | NONE) { 1M:0, 2M:1, CODED-S8:2, CODED-S2:3, NONE:4 }">廣播輔助 PHY</ArgTableRow>
<ArgTableRow arg="legacy" typ="bool">廣播傳統相容性</ArgTableRow>
<ArgTableRow arg="filter-comment" typ="string">匹配白名單過濾器的註釋</ArgTableRow>
</ArgTable>
