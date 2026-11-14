---
sidebar_key: "cli-reference/iot/wiliot/index"
sidebar_position: 5
title: "wiliot"
sidebar_label: "wiliot"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/iot/wiliot
captured_at: '2026-11-01T21:28:20+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## iot/wiliot {#iotwiliot}
**軟體包：** iot
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="spoof-gps" typ="bool"></ArgTableRow>
<ArgTableRow arg="lat" typ="num"></ArgTableRow>
<ArgTableRow arg="long" typ="num"></ArgTableRow>
<ArgTableRow arg="server" typ="enum (none)">使用的 MQTT 伺服器</ArgTableRow>
<ArgTableRow arg="scanner" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="advertiser" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="wi-fi" typ="iface_enum { none }"></ArgTableRow>
<ArgTableRow arg="features" typ="ubit (gateway, bridge)">支援的 Wiliot 功能</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
<ArgTableRow arg="gateway-id" typ="string"></ArgTableRow>
<ArgTableRow arg="type" typ="string"></ArgTableRow>
<ArgTableRow arg="owner" typ="string"></ArgTableRow>
</ArgTable>
