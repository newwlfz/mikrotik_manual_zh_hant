---
sidebar_key: "cli-reference/interface/wireless/spectral-scan"
sidebar_position: 21
title: "spectral-scan"
sidebar_label: 'spectral-scan'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/wireless/spectral-scan
captured_at: '2026-11-01T21:23:30+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/wireless/spectral-scan {#interfacewirelessspectral-scan}
**包：** wireless-rep
**型別：** 命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="range" typ="alt { range: range [ .. 7000]
, band: enum (2.4ghz | 5ghz | current-channel) { 2.4ghz:1, 5ghz:2, current-channel:3 }
 }"></ArgTableRow>
<ArgTableRow arg="show-interference" typ="bool"></ArgTableRow>
<ArgTableRow arg="samples" typ="num"></ArgTableRow>
<ArgTableRow arg="buckets" typ="num"></ArgTableRow>
<ArgTableRow arg="peak-hold-time" typ="time"></ArgTableRow>
<ArgTableRow arg="save-file-name" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="freq" typ="num"></ArgTableRow>
<ArgTableRow arg="interference" typ="composite { type: enum (none | bluetooth-headset | bluetooth-stereo | cordless-phone | microwave-oven | cwa | video-bridge | wifi) { none:0xffffffff, bluetooth-headset:0, bluetooth-stereo:1, cordless-phone:2, microwave-oven:3, cwa:4, video-bridge:5, wifi:6 }
, rssi: num
 }"></ArgTableRow>
<ArgTableRow arg="dbm" typ="num"></ArgTableRow>
<ArgTableRow arg="graph" typ="meter"></ArgTableRow>
</ArgTable>
