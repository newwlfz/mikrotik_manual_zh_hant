---
sidebar_key: "cli-reference/iot/lora/send"
sidebar_position: 6
title: "send"
sidebar_label: 'send'
source: https://manual.mikrotik.com/docs/cli-reference/iot/lora/send
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## iot/lora/send {#iotlorasend}
**包：** iot
**型別：** 命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="device-id" typ="num">裝置 ID</ArgTableRow>
<ArgTableRow arg="payload" typ="string">TX 封包載荷</ArgTableRow>
<ArgTableRow arg="power" typ="num">射頻功率，單位 dBm</ArgTableRow>
<ArgTableRow arg="frequency" typ="num">無線電發射頻率，單位 MHz（例如 868500000）</ArgTableRow>
<ArgTableRow arg="bandwidth" typ="enum (125kHz | 250kHz | 500kHz) { 125kHz:125, 250kHz:250, 500kHz:500 }">LoRa 頻寬，單位 kHz [125, 250, 500]</ArgTableRow>
<ArgTableRow arg="spread-factor" typ="enum (SF7 | SF8 | SF9 | SF10 | SF11 | SF12 | MULTI) { SF7:0x02, SF8:0x04, SF9:0x08, SF10:0x10, SF11:0x21, SF12:0x40, MULTI:0x7E }">擴頻因子</ArgTableRow>
<ArgTableRow arg="modulation" typ="enum (MOD_CW | MOD_LORA | MOD_FSK) { MOD_CW:0x08, MOD_LORA:0x10, MOD_FSK:0x20 }">調製型別</ArgTableRow>
<ArgTableRow arg="preamble" typ="num">前導碼長度</ArgTableRow>
<ArgTableRow arg="inverted" typ="bool">反轉極性</ArgTableRow>
</ArgTable>
