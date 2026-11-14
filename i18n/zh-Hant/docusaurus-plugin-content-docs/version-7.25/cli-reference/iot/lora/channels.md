---
sidebar_key: "cli-reference/iot/lora/channels"
sidebar_position: 1
title: "channels"
sidebar_label: 'channels'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/iot/lora/channels
captured_at: '2026-11-01T21:23:37+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## iot/lora/channels {#iotlorachannels}
**包：** iot
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="radio" typ="enum (radio0 | radio1 | radio2 | radio3) { radio0:0, radio1:1, radio2:2, radio3:3 }"></ArgTableRow>
<ArgTableRow arg="freq-off" typ="num"></ArgTableRow>
<ArgTableRow arg="bandwidth" typ="enum (7.8_kHz | 15.6_kHz | 31.2_kHz | 62.5_kHz | 125_kHz | 250_kHz | 500_kHz | 200_kHz | 400_kHz | 800_kHz | 1600_kHz)"></ArgTableRow>
<ArgTableRow arg="spread-factor" typ="enum (SF7 | SF8 | SF9 | SF10 | SF11 | SF12 | SF5 | SF6)"></ArgTableRow>
<ArgTableRow arg="datarate" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (MSF | LoRa | FSK)"></ArgTableRow>
<ArgTableRow arg="freq" typ="num"></ArgTableRow>
</ArgTable>
